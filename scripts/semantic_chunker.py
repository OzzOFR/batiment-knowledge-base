"""
Chunker sémantique amélioré pour la base de connaissances bâtiment.

Stratégie :
1. Découpe d'abord par sections (titres H1/H2/H3 Markdown)
2. Chaque chunk est préfixé par le titre de sa section pour le contexte
3. Si une section est trop longue, elle est subdivisée par paragraphes
4. Les chunks trop courts sont fusionnés avec le suivant
5. Overlap optionnel entre chunks consécutifs d'une même section

Usage :
    from semantic_chunker import SemanticChunker
    chunker = SemanticChunker()
    chunks = chunker.chunk_markdown(content, source_title="Mon document")
"""

import re
from dataclasses import dataclass
from typing import Optional


@dataclass
class Chunk:
    """Un chunk de texte avec ses métadonnées."""
    content: str          # Texte du chunk (avec préfixe de section)
    section_title: str    # Titre de la section d'origine
    section_level: int    # Niveau du titre (1, 2, 3...)
    chunk_index: int      # Index du chunk dans le document
    char_count: int       # Nombre de caractères


class SemanticChunker:
    """
    Chunker sémantique qui découpe les documents Markdown par sections.
    
    Paramètres :
    - max_chars : taille maximale d'un chunk en caractères (défaut: 1500)
    - min_chars : taille minimale d'un chunk (les plus petits sont fusionnés)
    - overlap_chars : chevauchement entre chunks consécutifs (défaut: 200)
    - prefix_section : si True, préfixe chaque chunk avec le titre de sa section
    """
    
    def __init__(
        self,
        max_chars: int = 1500,
        min_chars: int = 150,
        overlap_chars: int = 200,
        prefix_section: bool = True
    ):
        self.max_chars = max_chars
        self.min_chars = min_chars
        self.overlap_chars = overlap_chars
        self.prefix_section = prefix_section
        
        # Pattern pour les titres Markdown H1-H4
        self.heading_pattern = re.compile(r'^(#{1,4})\s+(.+)$', re.MULTILINE)
    
    def _extract_sections(self, text: str) -> list[dict]:
        """
        Extrait les sections d'un texte Markdown.
        Retourne une liste de dicts : {level, title, content}
        """
        # Supprimer le front-matter YAML
        if text.startswith('---'):
            end = text.find('---', 3)
            if end != -1:
                text = text[end+3:].strip()
        
        sections = []
        
        # Trouver tous les titres avec leur position
        headings = list(self.heading_pattern.finditer(text))
        
        if not headings:
            # Pas de titres : traiter comme une seule section
            sections.append({
                'level': 0,
                'title': '',
                'content': text.strip()
            })
            return sections
        
        # Texte avant le premier titre
        if headings[0].start() > 0:
            intro = text[:headings[0].start()].strip()
            if intro:
                sections.append({
                    'level': 0,
                    'title': 'Introduction',
                    'content': intro
                })
        
        # Extraire chaque section
        for i, heading in enumerate(headings):
            level = len(heading.group(1))
            title = heading.group(2).strip()
            
            # Contenu : du titre courant jusqu'au prochain titre
            start = heading.end()
            end = headings[i+1].start() if i+1 < len(headings) else len(text)
            content = text[start:end].strip()
            
            sections.append({
                'level': level,
                'title': title,
                'content': content
            })
        
        return sections
    
    def _split_long_section(self, content: str) -> list[str]:
        """
        Découpe une section trop longue en sous-chunks par paragraphes.
        """
        paragraphs = re.split(r'\n{2,}', content)
        paragraphs = [p.strip() for p in paragraphs if p.strip() and len(p.strip()) > 20]
        
        sub_chunks = []
        current = ""
        
        for para in paragraphs:
            if len(current) + len(para) + 2 <= self.max_chars:
                current = (current + "\n\n" + para).strip()
            else:
                if current:
                    sub_chunks.append(current)
                
                # Si le paragraphe seul dépasse max_chars, le couper par phrases
                if len(para) > self.max_chars:
                    sentences = re.split(r'(?<=[.!?])\s+', para)
                    sent_chunk = ""
                    for sent in sentences:
                        if len(sent_chunk) + len(sent) + 1 <= self.max_chars:
                            sent_chunk = (sent_chunk + " " + sent).strip()
                        else:
                            if sent_chunk:
                                sub_chunks.append(sent_chunk)
                            sent_chunk = sent
                    if sent_chunk:
                        sub_chunks.append(sent_chunk)
                    current = ""
                else:
                    current = para
        
        if current:
            sub_chunks.append(current)
        
        return sub_chunks if sub_chunks else [content[:self.max_chars]]
    
    def _add_overlap(self, chunks: list[str]) -> list[str]:
        """Ajoute un chevauchement entre chunks consécutifs."""
        if len(chunks) <= 1 or self.overlap_chars <= 0:
            return chunks
        
        result = [chunks[0]]
        for i in range(1, len(chunks)):
            # Prendre les derniers overlap_chars du chunk précédent
            prev_tail = chunks[i-1][-self.overlap_chars:].strip()
            # Trouver le début d'une phrase dans le tail
            sentence_start = prev_tail.find('. ')
            if sentence_start != -1 and sentence_start < len(prev_tail) - 20:
                prev_tail = prev_tail[sentence_start+2:]
            
            result.append(prev_tail + "\n\n" + chunks[i] if prev_tail else chunks[i])
        
        return result
    
    def chunk_markdown(self, text: str, source_title: str = "") -> list[Chunk]:
        """
        Découpe un document Markdown en chunks sémantiques.
        
        Args:
            text: Contenu Markdown du document
            source_title: Titre du document source (pour le contexte)
        
        Returns:
            Liste de Chunk avec métadonnées
        """
        sections = self._extract_sections(text)
        
        all_chunks = []
        chunk_index = 0
        
        for section in sections:
            title = section['title']
            level = section['level']
            content = section['content']
            
            if not content:
                continue
            
            # Construire le préfixe de contexte
            prefix = ""
            if self.prefix_section and title:
                if source_title:
                    prefix = f"[{source_title} — {title}]\n\n"
                else:
                    prefix = f"[{title}]\n\n"
            elif self.prefix_section and source_title:
                prefix = f"[{source_title}]\n\n"
            
            # Découper la section si elle est trop longue
            if len(content) <= self.max_chars - len(prefix):
                sub_chunks = [content]
            else:
                sub_chunks = self._split_long_section(content)
            
            # Ajouter l'overlap entre sous-chunks
            if len(sub_chunks) > 1:
                sub_chunks = self._add_overlap(sub_chunks)
            
            # Fusionner les chunks trop courts avec le suivant
            merged = []
            buffer = ""
            for sc in sub_chunks:
                if len(buffer) + len(sc) < self.min_chars * 2:
                    buffer = (buffer + "\n\n" + sc).strip()
                else:
                    if buffer:
                        merged.append(buffer)
                    buffer = sc
            if buffer:
                merged.append(buffer)
            
            # Créer les objets Chunk
            for sc in merged:
                full_content = prefix + sc
                all_chunks.append(Chunk(
                    content=full_content,
                    section_title=title,
                    section_level=level,
                    chunk_index=chunk_index,
                    char_count=len(full_content)
                ))
                chunk_index += 1
        
        return all_chunks
    
    def chunk_plain_text(self, text: str, source_title: str = "") -> list[Chunk]:
        """
        Découpe un texte brut (non-Markdown) en chunks.
        Utilisé pour les textes OCR de Gallica/Archive.org.
        """
        # Nettoyer le texte OCR
        text = re.sub(r'\n{3,}', '\n\n', text)
        text = re.sub(r'[ \t]{2,}', ' ', text)
        
        # Découper par paragraphes
        paragraphs = re.split(r'\n{2,}', text)
        paragraphs = [p.strip() for p in paragraphs if p.strip() and len(p.strip()) > 30]
        
        chunks = []
        current = ""
        chunk_index = 0
        
        prefix = f"[{source_title}]\n\n" if source_title and self.prefix_section else ""
        
        for para in paragraphs:
            if len(current) + len(para) + 2 <= self.max_chars - len(prefix):
                current = (current + "\n\n" + para).strip()
            else:
                if current and len(current) >= self.min_chars:
                    chunks.append(Chunk(
                        content=prefix + current,
                        section_title="",
                        section_level=0,
                        chunk_index=chunk_index,
                        char_count=len(prefix + current)
                    ))
                    chunk_index += 1
                    # Overlap
                    if self.overlap_chars > 0:
                        tail = current[-self.overlap_chars:]
                        dot = tail.find('. ')
                        if dot != -1:
                            tail = tail[dot+2:]
                        current = tail + "\n\n" + para
                    else:
                        current = para
                else:
                    current = (current + "\n\n" + para).strip() if current else para
        
        if current and len(current) >= self.min_chars:
            chunks.append(Chunk(
                content=prefix + current,
                section_title="",
                section_level=0,
                chunk_index=chunk_index,
                char_count=len(prefix + current)
            ))
        
        return chunks


# ─── Test rapide ──────────────────────────────────────────────────────────────

if __name__ == "__main__":
    test_md = """---
titre: Test
---

# Maçonnerie

## Les mortiers

Le mortier est un mélange de liant et de granulats fins avec de l'eau.
Il existe plusieurs types de mortiers selon leur composition.

### Mortier de chaux

La chaux aérienne est obtenue par calcination du calcaire.
Elle durcit lentement au contact de l'air.

### Mortier de ciment

Le ciment Portland est le liant hydraulique le plus utilisé.
Il durcit rapidement même en milieu humide.

## Les briques

La brique est un matériau de construction en terre cuite.
Elle est fabriquée à partir d'argile malaxée et cuite au four.
"""
    
    chunker = SemanticChunker(max_chars=500, min_chars=100, overlap_chars=100)
    chunks = chunker.chunk_markdown(test_md, source_title="Test Maçonnerie")
    
    print(f"Nombre de chunks: {len(chunks)}")
    for i, chunk in enumerate(chunks):
        print(f"\n--- Chunk {i+1} (section: '{chunk.section_title}', {chunk.char_count} chars) ---")
        print(chunk.content[:200])
