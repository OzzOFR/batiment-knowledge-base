"""
Génération des figures vectorielles SVG pour la base de connaissances bâtiment.
Chaque figure est un schéma technique précis avec annotations et cotes.
"""
import os
import math

OUTPUT_DIR = "/home/ubuntu/batiment-knowledge-base/figures/svg"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ─── Helpers SVG ──────────────────────────────────────────────────────────────

def svg_start(w, h, title=""):
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
  <defs>
    <style>
      text {{ font-family: Arial, sans-serif; }}
      .titre {{ font-size: 13px; font-weight: bold; fill: #1a1a2e; }}
      .label {{ font-size: 10px; fill: #333; }}
      .cote {{ font-size: 9px; fill: #666; }}
      .note {{ font-size: 9px; fill: #888; font-style: italic; }}
      .hachure {{ fill: url(#hachure_beton); }}
      .hachure_bois {{ fill: url(#hachure_bois); }}
      .hachure_sol {{ fill: url(#hachure_sol); }}
      .hachure_isolant {{ fill: url(#hachure_isolant); }}
    </style>
    <pattern id="hachure_beton" patternUnits="userSpaceOnUse" width="8" height="8">
      <rect width="8" height="8" fill="#e8e8e8"/>
      <circle cx="2" cy="2" r="1" fill="#999"/>
      <circle cx="6" cy="6" r="1" fill="#999"/>
    </pattern>
    <pattern id="hachure_bois" patternUnits="userSpaceOnUse" width="6" height="6">
      <rect width="6" height="6" fill="#f5deb3"/>
      <line x1="0" y1="3" x2="6" y2="3" stroke="#c8a06e" stroke-width="0.5"/>
    </pattern>
    <pattern id="hachure_sol" patternUnits="userSpaceOnUse" width="8" height="8">
      <rect width="8" height="8" fill="#c8b89a"/>
      <line x1="0" y1="4" x2="8" y2="0" stroke="#a0896a" stroke-width="0.7"/>
      <line x1="0" y1="8" x2="8" y2="4" stroke="#a0896a" stroke-width="0.7"/>
    </pattern>
    <pattern id="hachure_isolant" patternUnits="userSpaceOnUse" width="10" height="10">
      <rect width="10" height="10" fill="#fff9c4"/>
      <path d="M0,5 Q2.5,0 5,5 Q7.5,10 10,5" stroke="#f9a825" stroke-width="1" fill="none"/>
    </pattern>
    <marker id="arrow" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">
      <path d="M0,0 L0,6 L8,3 z" fill="#555"/>
    </marker>
    <marker id="arrow_rev" markerWidth="8" markerHeight="8" refX="2" refY="3" orient="auto">
      <path d="M8,0 L8,6 L0,3 z" fill="#555"/>
    </marker>
  </defs>
  <!-- Fond blanc -->
  <rect width="{w}" height="{h}" fill="white" stroke="#ccc" stroke-width="1"/>
  <!-- Titre -->
  <text x="{w//2}" y="22" text-anchor="middle" class="titre">{title}</text>
  <!-- Cadre -->
  <rect x="5" y="5" width="{w-10}" height="{h-10}" fill="none" stroke="#aaa" stroke-width="0.5"/>
'''

def svg_end():
    return "</svg>\n"

def cote(x1, y1, x2, y2, texte, offset=15, side="top"):
    """Ligne de cote avec flèches et texte"""
    mx, my = (x1+x2)/2, (y1+y2)/2
    if side == "top":
        return f'''
  <line x1="{x1}" y1="{y1-offset}" x2="{x2}" y2="{y2-offset}" stroke="#555" stroke-width="0.8" marker-start="url(#arrow_rev)" marker-end="url(#arrow)"/>
  <line x1="{x1}" y1="{y1}" x2="{x1}" y2="{y1-offset}" stroke="#555" stroke-width="0.5" stroke-dasharray="2,2"/>
  <line x1="{x2}" y1="{y2}" x2="{x2}" y2="{y2-offset}" stroke="#555" stroke-width="0.5" stroke-dasharray="2,2"/>
  <text x="{mx}" y="{my-offset-3}" text-anchor="middle" class="cote">{texte}</text>'''
    elif side == "right":
        return f'''
  <line x1="{x1+offset}" y1="{y1}" x2="{x2+offset}" y2="{y2}" stroke="#555" stroke-width="0.8" marker-start="url(#arrow_rev)" marker-end="url(#arrow)"/>
  <line x1="{x1}" y1="{y1}" x2="{x1+offset}" y2="{y1}" stroke="#555" stroke-width="0.5" stroke-dasharray="2,2"/>
  <line x1="{x2}" y1="{y2}" x2="{x2+offset}" y2="{y2}" stroke="#555" stroke-width="0.5" stroke-dasharray="2,2"/>
  <text x="{x1+offset+3}" y="{(y1+y2)/2+4}" class="cote">{texte}</text>'''
    return ""

def legende_item(x, y, couleur, texte):
    return f'''
  <rect x="{x}" y="{y-8}" width="12" height="10" fill="{couleur}" stroke="#999" stroke-width="0.5"/>
  <text x="{x+16}" y="{y}" class="note">{texte}</text>'''

# ─── Figure 1 : Semelle filante ───────────────────────────────────────────────

def gen_semelle_filante():
    w, h = 600, 420
    svg = svg_start(w, h, "Semelle filante en béton armé — Coupe transversale")

    # Sol naturel
    svg += f'<rect x="50" y="200" width="500" height="80" fill="url(#hachure_sol)" stroke="#a0896a" stroke-width="1"/>'
    svg += f'<text x="310" y="250" text-anchor="middle" class="label">Sol naturel</text>'

    # Hors-gel annotation
    svg += f'<line x1="30" y1="120" x2="30" y2="200" stroke="#e53935" stroke-width="1.5" stroke-dasharray="4,3"/>'
    svg += f'<text x="5" y="165" class="cote" fill="#e53935" transform="rotate(-90,5,165)">Hors-gel ≥ 0,80 m</text>'

    # Semelle béton
    svg += f'<rect x="150" y="200" width="300" height="80" fill="url(#hachure_beton)" stroke="#333" stroke-width="1.5"/>'
    svg += f'<text x="300" y="248" text-anchor="middle" class="label">Béton armé C25/30</text>'

    # Mur porteur au-dessus
    svg += f'<rect x="230" y="80" width="140" height="120" fill="url(#hachure_beton)" stroke="#333" stroke-width="1.5"/>'
    svg += f'<text x="300" y="148" text-anchor="middle" class="label">Mur porteur</text>'

    # Ferraillage (aciers longitudinaux)
    for x in [180, 210, 390, 420]:
        svg += f'<circle cx="{x}" cy="255" r="5" fill="#e53935" stroke="#333" stroke-width="1"/>'
    svg += f'<text x="300" y="272" text-anchor="middle" class="cote">Aciers longitudinaux HA</text>'

    # Cadres / épingles
    svg += f'<rect x="175" y="215" width="250" height="55" fill="none" stroke="#e53935" stroke-width="1.5" stroke-dasharray="4,2"/>'
    svg += f'<text x="430" y="245" class="cote" fill="#e53935">Cadres HA</text>'

    # Cotes
    svg += cote(150, 200, 450, 200, "L = 60 cm min.", offset=20, side="top")
    svg += cote(450, 200, 450, 280, "h = 25 cm min.", offset=20, side="right")
    svg += cote(230, 80, 370, 80, "e mur", offset=20, side="top")

    # Débord annotation
    svg += f'<line x1="150" y1="310" x2="230" y2="310" stroke="#1565c0" stroke-width="1" marker-start="url(#arrow_rev)" marker-end="url(#arrow)"/>'
    svg += f'<text x="190" y="325" text-anchor="middle" class="cote" fill="#1565c0">Débord ≥ 10 cm</text>'

    # Enrobage
    svg += f'<line x1="150" y1="340" x2="180" y2="340" stroke="#555" stroke-width="0.8" marker-end="url(#arrow)"/>'
    svg += f'<text x="155" y="355" class="cote">Enrobage ≥ 3 cm</text>'

    # Niveau sol fini
    svg += f'<line x1="40" y1="200" x2="560" y2="200" stroke="#2e7d32" stroke-width="1" stroke-dasharray="6,3"/>'
    svg += f'<text x="555" y="196" text-anchor="end" class="note" fill="#2e7d32">NGF sol</text>'

    # Légende
    svg += f'<text x="50" y="375" class="cote" font-weight="bold">Légende :</text>'
    svg += legende_item(50, 390, "url(#hachure_beton)", "Béton armé C25/30")
    svg += legende_item(200, 390, "url(#hachure_sol)", "Sol naturel")
    svg += f'<circle cx="360" cy="382" r="5" fill="#e53935" stroke="#333" stroke-width="1"/>'
    svg += f'<text x="376" y="387" class="note">Aciers HA (ferraillage)</text>'

    svg += f'<text x="300" y="408" text-anchor="middle" class="note">Source : Champly, Nouvelle Encyclopédie Pratique du Bâtiment — Vol.1 Arpentage, Fondations</text>'
    svg += svg_end()
    return svg

# ─── Figure 2 : Ferme de charpente traditionnelle ────────────────────────────

def gen_ferme_charpente():
    w, h = 650, 400
    svg = svg_start(w, h, "Ferme de charpente traditionnelle — Vue de face")

    cx, base_y = 325, 320
    span = 500
    height = 200
    x_left, x_right = cx - span//2, cx + span//2

    # Entrait (poutre horizontale basse)
    svg += f'<rect x="{x_left-10}" y="{base_y-8}" width="{span+20}" height="16" fill="url(#hachure_bois)" stroke="#8B4513" stroke-width="1.5"/>'
    svg += f'<text x="{cx}" y="{base_y+25}" text-anchor="middle" class="label">Entrait</text>'

    # Arbalétriers (chevrons inclinés)
    peak_y = base_y - height
    svg += f'<polygon points="{x_left},{base_y} {cx},{peak_y} {cx+8},{peak_y} {x_left+12},{base_y}" fill="url(#hachure_bois)" stroke="#8B4513" stroke-width="1.5"/>'
    svg += f'<polygon points="{x_right},{base_y} {cx},{peak_y} {cx-8},{peak_y} {x_right-12},{base_y}" fill="url(#hachure_bois)" stroke="#8B4513" stroke-width="1.5"/>'
    svg += f'<text x="{x_left+60}" y="{base_y-80}" class="label" transform="rotate(-22,{x_left+60},{base_y-80})">Arbalétrier</text>'
    svg += f'<text x="{x_right-60}" y="{base_y-80}" class="label" text-anchor="end" transform="rotate(22,{x_right-60},{base_y-80})">Arbalétrier</text>'

    # Poinçon (vertical central)
    mid_y = (base_y + peak_y) // 2
    svg += f'<rect x="{cx-6}" y="{peak_y}" width="12" height="{base_y-peak_y}" fill="url(#hachure_bois)" stroke="#8B4513" stroke-width="1.5"/>'
    svg += f'<text x="{cx+20}" y="{mid_y}" class="label">Poinçon</text>'

    # Jambes de force
    jdf_x_l = x_left + span//4
    jdf_x_r = x_right - span//4
    svg += f'<line x1="{jdf_x_l}" y1="{base_y}" x2="{cx-5}" y2="{mid_y}" stroke="#8B4513" stroke-width="8"/>'
    svg += f'<line x1="{jdf_x_r}" y1="{base_y}" x2="{cx+5}" y2="{mid_y}" stroke="#8B4513" stroke-width="8"/>'
    svg += f'<text x="{jdf_x_l-30}" y="{(base_y+mid_y)//2}" class="label" text-anchor="end">Jambe de force</text>'

    # Contre-fiches
    svg += f'<line x1="{jdf_x_l}" y1="{base_y}" x2="{x_left+30}" y2="{base_y-60}" stroke="#8B4513" stroke-width="6" stroke-dasharray="8,3"/>'
    svg += f'<line x1="{jdf_x_r}" y1="{base_y}" x2="{x_right-30}" y2="{base_y-60}" stroke="#8B4513" stroke-width="6" stroke-dasharray="8,3"/>'
    svg += f'<text x="{x_left+10}" y="{base_y-70}" class="cote">Contre-fiche</text>'

    # Appuis (murs)
    svg += f'<rect x="{x_left-30}" y="{base_y}" width="40" height="40" fill="url(#hachure_beton)" stroke="#333" stroke-width="1.5"/>'
    svg += f'<rect x="{x_right-10}" y="{base_y}" width="40" height="40" fill="url(#hachure_beton)" stroke="#333" stroke-width="1.5"/>'
    svg += f'<text x="{x_left-10}" y="{base_y+55}" class="label">Sablière</text>'
    svg += f'<text x="{x_right+10}" y="{base_y+55}" class="label">Sablière</text>'

    # Cotes
    svg += cote(x_left, base_y, x_right, base_y, f"Portée = {span//10} m", offset=25, side="top")
    svg += cote(x_right, peak_y, x_right, base_y, f"Flèche = {height//10} m", offset=30, side="right")

    # Angle de pente
    angle = math.degrees(math.atan(height / (span/2)))
    svg += f'<text x="{x_left+80}" y="{base_y-15}" class="cote">α = {angle:.0f}°</text>'

    svg += f'<text x="{w//2}" y="{h-8}" text-anchor="middle" class="note">Source : Champly, Nouvelle Encyclopédie Pratique du Bâtiment — Vol.4 Charpentes bois</text>'
    svg += svg_end()
    return svg

# ─── Figure 3 : Coupe mur maçonnerie ─────────────────────────────────────────

def gen_mur_maconnerie():
    w, h = 500, 500
    svg = svg_start(w, h, "Mur porteur en maçonnerie — Coupe verticale")

    # Fondation
    svg += f'<rect x="120" y="380" width="260" height="60" fill="url(#hachure_beton)" stroke="#333" stroke-width="1.5"/>'
    svg += f'<text x="250" y="415" text-anchor="middle" class="label">Semelle béton armé</text>'

    # Sol
    svg += f'<rect x="50" y="380" width="400" height="30" fill="url(#hachure_sol)" stroke="#a0896a" stroke-width="1"/>'
    svg += f'<line x1="50" y1="380" x2="450" y2="380" stroke="#2e7d32" stroke-width="1.5"/>'
    svg += f'<text x="455" y="376" class="note" fill="#2e7d32">NGF</text>'

    # Mur briques
    mur_x, mur_y, mur_w, mur_h = 170, 100, 160, 280
    svg += f'<rect x="{mur_x}" y="{mur_y}" width="{mur_w}" height="{mur_h}" fill="#f4a460" stroke="#8B4513" stroke-width="1.5"/>'

    # Joints horizontaux
    for y in range(mur_y+20, mur_y+mur_h, 20):
        svg += f'<line x1="{mur_x}" y1="{y}" x2="{mur_x+mur_w}" y2="{y}" stroke="#8B4513" stroke-width="0.5"/>'

    # Joints verticaux alternés
    for i, y in enumerate(range(mur_y, mur_y+mur_h, 20)):
        offset = 0 if i % 2 == 0 else mur_w//4
        for x in range(mur_x+offset, mur_x+mur_w, mur_w//2):
            svg += f'<line x1="{x}" y1="{y}" x2="{x}" y2="{y+20}" stroke="#8B4513" stroke-width="0.5"/>'

    svg += f'<text x="{mur_x+mur_w//2}" y="{mur_y+mur_h//2}" text-anchor="middle" class="label">Briques</text>'

    # Chaînage haut
    svg += f'<rect x="{mur_x}" y="{mur_y}" width="{mur_w}" height="25" fill="url(#hachure_beton)" stroke="#333" stroke-width="1.5"/>'
    svg += f'<text x="{mur_x+mur_w+10}" y="{mur_y+16}" class="label">Chaînage BA</text>'

    # Chaînage bas
    svg += f'<rect x="{mur_x}" y="{mur_y+mur_h-25}" width="{mur_w}" height="25" fill="url(#hachure_beton)" stroke="#333" stroke-width="1.5"/>'
    svg += f'<text x="{mur_x+mur_w+10}" y="{mur_y+mur_h-12}" class="label">Chaînage BA</text>'

    # Linteau
    svg += f'<rect x="{mur_x+40}" y="{mur_y+130}" width="80" height="20" fill="url(#hachure_beton)" stroke="#333" stroke-width="1.5"/>'
    svg += f'<text x="{mur_x+80}" y="{mur_y+125}" text-anchor="middle" class="label">Linteau BA</text>'

    # Baie
    svg += f'<rect x="{mur_x+40}" y="{mur_y+150}" width="80" height="80" fill="#b3e5fc" stroke="#0288d1" stroke-width="1" stroke-dasharray="4,2"/>'
    svg += f'<text x="{mur_x+80}" y="{mur_y+195}" text-anchor="middle" class="cote" fill="#0288d1">Baie</text>'

    # Cotes
    svg += cote(mur_x, mur_y, mur_x+mur_w, mur_y, "e = 20 cm", offset=20, side="top")
    svg += cote(mur_x+mur_w, mur_y, mur_x+mur_w, mur_y+mur_h, "H mur", offset=25, side="right")

    # Joints mortier annotation
    svg += f'<line x1="{mur_x-30}" y1="{mur_y+60}" x2="{mur_x}" y2="{mur_y+60}" stroke="#555" stroke-width="0.8" marker-end="url(#arrow)"/>'
    svg += f'<text x="{mur_x-35}" y="{mur_y+57}" text-anchor="end" class="cote">Joint mortier 1 cm</text>'

    svg += f'<text x="{w//2}" y="{h-8}" text-anchor="middle" class="note">Source : Champly, Nouvelle Encyclopédie Pratique du Bâtiment — Vol.2 Maçonnerie</text>'
    svg += svg_end()
    return svg

# ─── Figure 4 : Plancher à poutrelles et hourdis ─────────────────────────────

def gen_plancher_poutrelles():
    w, h = 600, 380
    svg = svg_start(w, h, "Plancher à poutrelles et hourdis — Coupe transversale")

    # Table de compression
    svg += f'<rect x="80" y="80" width="440" height="30" fill="url(#hachure_beton)" stroke="#333" stroke-width="1.5"/>'
    svg += f'<text x="300" y="100" text-anchor="middle" class="label">Table de compression BA (5 cm)</text>'

    # Treillis soudé
    for x in range(100, 520, 30):
        svg += f'<line x1="{x}" y1="80" x2="{x}" y2="110" stroke="#e53935" stroke-width="1"/>'
    svg += f'<line x1="80" y1="90" x2="520" y2="90" stroke="#e53935" stroke-width="1"/>'
    svg += f'<text x="530" y="93" class="cote" fill="#e53935">Treillis soudé</text>'

    # Poutrelles (3 poutrelles)
    poutrelles_x = [130, 250, 370]
    for px in poutrelles_x:
        # Corps de la poutrelle (T inversé)
        svg += f'<rect x="{px-12}" y="110" width="24" height="100" fill="url(#hachure_beton)" stroke="#333" stroke-width="1.5"/>'
        svg += f'<rect x="{px-20}" y="185" width="40" height="25" fill="url(#hachure_beton)" stroke="#333" stroke-width="1.5"/>'
        # Armature tendue
        svg += f'<circle cx="{px}" cy="200" r="5" fill="#e53935" stroke="#333" stroke-width="1"/>'

    svg += f'<text x="250" y="230" text-anchor="middle" class="label">Poutrelle béton précontraint</text>'

    # Hourdis entre poutrelles
    hourdis_positions = [(130+24, 250-24), (250+24, 370-24)]
    for hx1, hx2 in hourdis_positions:
        svg += f'<rect x="{hx1}" y="110" width="{hx2-hx1}" height="100" fill="#fff9c4" stroke="#f9a825" stroke-width="1"/>'
        # Motif polystyrène
        for y in range(120, 200, 20):
            svg += f'<line x1="{hx1+5}" y1="{y}" x2="{hx2-5}" y2="{y}" stroke="#f9a825" stroke-width="0.5"/>'
        svg += f'<text x="{(hx1+hx2)//2}" y="{165}" text-anchor="middle" class="cote">Hourdis</text>'

    # Appuis sur murs
    svg += f'<rect x="50" y="80" width="80" height="140" fill="url(#hachure_beton)" stroke="#333" stroke-width="1.5"/>'
    svg += f'<rect x="470" y="80" width="80" height="140" fill="url(#hachure_beton)" stroke="#333" stroke-width="1.5"/>'
    svg += f'<text x="90" y="250" text-anchor="middle" class="label">Mur porteur</text>'
    svg += f'<text x="510" y="250" text-anchor="middle" class="label">Mur porteur</text>'

    # Appui minimum
    svg += f'<line x1="80" y1="270" x2="130" y2="270" stroke="#1565c0" stroke-width="1" marker-start="url(#arrow_rev)" marker-end="url(#arrow)"/>'
    svg += f'<text x="105" y="285" text-anchor="middle" class="cote" fill="#1565c0">Appui ≥ 5 cm</text>'

    # Cotes
    svg += cote(130, 80, 250, 80, "Entraxe = 60 cm", offset=20, side="top")
    svg += cote(470, 80, 470, 210, "H = 20 cm", offset=30, side="right")

    # Légende
    svg += f'<text x="80" y="320" class="cote" font-weight="bold">Légende :</text>'
    svg += legende_item(80, 340, "url(#hachure_beton)", "Béton armé")
    svg += legende_item(220, 340, "#fff9c4", "Hourdis polystyrène")
    svg += f'<circle cx="370" cy="332" r="5" fill="#e53935" stroke="#333" stroke-width="1"/>'
    svg += f'<text x="386" y="337" class="note">Armatures précontraintes</text>'

    svg += f'<text x="{w//2}" y="{h-8}" text-anchor="middle" class="note">Source : Champly, Nouvelle Encyclopédie Pratique du Bâtiment — Vol.1 Arpentage, Fondations</text>'
    svg += svg_end()
    return svg

# ─── Figure 5 : Schéma VMC simple flux ───────────────────────────────────────

def gen_vmc_simple_flux():
    w, h = 580, 480
    svg = svg_start(w, h, "VMC simple flux — Schéma de principe")

    # Bâtiment (coupe)
    svg += f'<rect x="60" y="60" width="460" height="360" fill="#f8f9fa" stroke="#333" stroke-width="2"/>'

    # Planchers
    svg += f'<line x1="60" y1="240" x2="520" y2="240" stroke="#555" stroke-width="2"/>'
    svg += f'<text x="30" y="160" class="label" text-anchor="middle" transform="rotate(-90,30,160)">Étage</text>'
    svg += f'<text x="30" y="320" class="label" text-anchor="middle" transform="rotate(-90,30,320)">RDC</text>'

    # Pièces sèches (chambres, salon) - entrées d'air
    rooms_dry = [(80, 80, 140, 140, "Chambre"), (300, 80, 140, 140, "Séjour"),
                 (80, 260, 140, 140, "Chambre"), (300, 260, 140, 140, "Salon")]
    for rx, ry, rw, rh, rname in rooms_dry:
        svg += f'<rect x="{rx}" y="{ry}" width="{rw}" height="{rh}" fill="#e3f2fd" stroke="#1565c0" stroke-width="1"/>'
        svg += f'<text x="{rx+rw//2}" y="{ry+rh//2}" text-anchor="middle" class="label">{rname}</text>'
        # Entrée d'air (grille en bas de fenêtre)
        svg += f'<rect x="{rx+rw-20}" y="{ry+10}" width="20" height="15" fill="#1565c0" stroke="#0d47a1" stroke-width="1"/>'
        svg += f'<text x="{rx+rw+5}" y="{ry+20}" class="cote" fill="#1565c0">EA</text>'
        # Flèche entrée d'air
        svg += f'<line x1="{rx+rw+15}" y1="{ry+17}" x2="{rx+rw}" y2="{ry+17}" stroke="#1565c0" stroke-width="1.5" marker-end="url(#arrow)"/>'

    # Pièces humides (cuisine, SDB, WC) - bouches d'extraction
    rooms_wet = [(460, 80, 0, "Cuisine"), (460, 170, 0, "SDB"), (460, 260, 0, "WC"), (460, 350, 0, "WC")]
    for rx, ry, _, rname in rooms_wet:
        svg += f'<rect x="{rx-60}" y="{ry}" width="60" height="60" fill="#fce4ec" stroke="#c62828" stroke-width="1"/>'
        svg += f'<text x="{rx-30}" y="{ry+35}" text-anchor="middle" class="label">{rname}</text>'
        # Bouche extraction
        svg += f'<circle cx="{rx-30}" cy="{ry+10}" r="8" fill="#c62828" stroke="#b71c1c" stroke-width="1"/>'
        svg += f'<text x="{rx+5}" y="{ry+14}" class="cote" fill="#c62828">BE</text>'

    # Gaine de ventilation (colonne)
    svg += f'<rect x="430" y="60" width="20" height="360" fill="#ffecb3" stroke="#f57f17" stroke-width="1.5"/>'
    svg += f'<text x="440" y="250" text-anchor="middle" class="label" transform="rotate(-90,440,250)">Gaine VMC</text>'

    # Caisson VMC (en toiture)
    svg += f'<rect x="390" y="30" width="100" height="40" fill="#fff3e0" stroke="#e65100" stroke-width="2"/>'
    svg += f'<text x="440" y="55" text-anchor="middle" class="label">Caisson VMC</text>'

    # Rejet en toiture
    svg += f'<line x1="440" y1="30" x2="440" y2="10" stroke="#e65100" stroke-width="2" marker-end="url(#arrow)"/>'
    svg += f'<text x="450" y="15" class="cote" fill="#e65100">Rejet air vicié</text>'

    # Flux d'air (flèches de circulation)
    svg += f'<text x="220" y="200" text-anchor="middle" class="cote" fill="#1565c0">→ Flux d\'air naturel →</text>'
    svg += f'<text x="220" y="380" text-anchor="middle" class="cote" fill="#1565c0">→ Flux d\'air naturel →</text>'

    # Légende
    svg += f'<rect x="60" y="435" width="12" height="10" fill="#e3f2fd" stroke="#1565c0" stroke-width="1"/>'
    svg += f'<text x="78" y="445" class="note">Pièces sèches (EA = Entrée d\'Air)</text>'
    svg += f'<rect x="280" y="435" width="12" height="10" fill="#fce4ec" stroke="#c62828" stroke-width="1"/>'
    svg += f'<text x="298" y="445" class="note">Pièces humides (BE = Bouche d\'Extraction)</text>'

    svg += f'<text x="{w//2}" y="{h-5}" text-anchor="middle" class="note">Réf. : DTU 68.3 — Installations de ventilation mécanique contrôlée</text>'
    svg += svg_end()
    return svg

# ─── Figure 6 : Fissures en façade ───────────────────────────────────────────

def gen_fissures_facade():
    w, h = 620, 460
    svg = svg_start(w, h, "Typologies de fissures en façade — Diagnostic")

    # 4 façades schématiques
    facades = [
        (50, 60, 120, 160, "Tassement différentiel", "#e53935"),
        (220, 60, 120, 160, "Retrait thermique", "#f57c00"),
        (390, 60, 120, 160, "Surcharge ponctuelle", "#7b1fa2"),
        (50, 270, 120, 160, "Défaut de linteau", "#1565c0"),
        (220, 270, 120, 160, "Corrosion armatures", "#c62828"),
        (390, 270, 120, 160, "Mouvement fondation", "#2e7d32"),
    ]

    for fx, fy, fw, fh, label, color in facades:
        # Façade
        svg += f'<rect x="{fx}" y="{fy}" width="{fw}" height="{fh}" fill="#f5f5f5" stroke="#999" stroke-width="1.5"/>'
        svg += f'<text x="{fx+fw//2}" y="{fy+fh+18}" text-anchor="middle" class="cote" fill="{color}">{label}</text>'

    # Fissure tassement (diagonale depuis angle)
    svg += f'<line x1="50" y1="220" x2="120" y2="100" stroke="#e53935" stroke-width="2.5"/>'
    svg += f'<line x1="50" y1="200" x2="100" y2="100" stroke="#e53935" stroke-width="1.5" stroke-dasharray="3,2"/>'

    # Fissure retrait (horizontale)
    svg += f'<line x1="220" y1="140" x2="340" y2="140" stroke="#f57c00" stroke-width="2"/>'
    svg += f'<line x1="220" y1="160" x2="340" y2="160" stroke="#f57c00" stroke-width="1" stroke-dasharray="3,2"/>'
    svg += f'<line x1="220" y1="180" x2="340" y2="180" stroke="#f57c00" stroke-width="1.5"/>'

    # Fissure surcharge (verticale sous charge)
    svg += f'<rect x="430" y="60" width="40" height="20" fill="#7b1fa2" opacity="0.3" stroke="#7b1fa2" stroke-width="1"/>'
    svg += f'<text x="450" y="73" text-anchor="middle" class="cote" fill="#7b1fa2">Charge</text>'
    svg += f'<line x1="450" y1="80" x2="450" y2="220" stroke="#7b1fa2" stroke-width="2.5"/>'
    svg += f'<line x1="440" y1="80" x2="440" y2="180" stroke="#7b1fa2" stroke-width="1" stroke-dasharray="3,2"/>'
    svg += f'<line x1="460" y1="80" x2="460" y2="180" stroke="#7b1fa2" stroke-width="1" stroke-dasharray="3,2"/>'

    # Fissure défaut linteau (en arc)
    svg += f'<rect x="75" y="340" width="70" height="50" fill="#b3e5fc" stroke="#0288d1" stroke-width="1"/>'
    svg += f'<text x="110" y="368" text-anchor="middle" class="cote" fill="#0288d1">Baie</text>'
    svg += f'<path d="M75,340 Q110,310 180,340" stroke="#1565c0" stroke-width="2.5" fill="none"/>'
    svg += f'<path d="M80,340 Q110,315 175,340" stroke="#1565c0" stroke-width="1" fill="none" stroke-dasharray="3,2"/>'

    # Fissure corrosion (horizontale avec gonflement)
    svg += f'<line x1="220" y1="350" x2="340" y2="350" stroke="#c62828" stroke-width="3"/>'
    for x in range(225, 340, 20):
        svg += f'<ellipse cx="{x}" cy="350" rx="8" ry="5" fill="#ef9a9a" stroke="#c62828" stroke-width="1" opacity="0.7"/>'
    svg += f'<text x="280" y="375" text-anchor="middle" class="cote" fill="#c62828">Gonflement</text>'

    # Fissure mouvement fondation (oblique depuis base)
    svg += f'<line x1="390" y1="430" x2="510" y2="290" stroke="#2e7d32" stroke-width="2.5"/>'
    svg += f'<line x1="400" y1="430" x2="510" y2="300" stroke="#2e7d32" stroke-width="1.5" stroke-dasharray="3,2"/>'

    # Légende générale
    svg += f'<text x="{w//2}" y="{h-25}" text-anchor="middle" class="cote" font-weight="bold">Gravité : trait plein = fissure active / tirets = fissure stabilisée</text>'
    svg += f'<text x="{w//2}" y="{h-10}" text-anchor="middle" class="note">Source : AQC — Observatoire de la Qualité de la Construction 2026 + Champly Vol.2</text>'
    svg += svg_end()
    return svg

# ─── Figure 7 : Toiture-terrasse étanchéité ──────────────────────────────────

def gen_toiture_terrasse():
    w, h = 580, 380
    svg = svg_start(w, h, "Étanchéité de toiture-terrasse inaccessible — Coupe")

    layers = [
        (80, 80, 440, 25, "url(#hachure_beton)", "#333", "Support béton armé"),
        (80, 105, 440, 15, "#e8f5e9", "#2e7d32", "Pare-vapeur (bitume SBS)"),
        (80, 120, 440, 60, "url(#hachure_isolant)", "#f9a825", "Isolant thermique (laine minérale 12 cm)"),
        (80, 180, 440, 20, "#ffccbc", "#bf360c", "Membrane d'étanchéité bicouche"),
        (80, 200, 440, 40, "#d7ccc8", "#795548", "Protection lourde (gravillon 4/8 — 5 cm)"),
    ]

    for lx, ly, lw, lh, fill, stroke, label in layers:
        svg += f'<rect x="{lx}" y="{ly}" width="{lw}" height="{lh}" fill="{fill}" stroke="{stroke}" stroke-width="1"/>'
        svg += f'<text x="{lx+lw+10}" y="{ly+lh//2+4}" class="label">{label}</text>'

    # Acrotère
    svg += f'<rect x="50" y="60" width="30" height="180" fill="url(#hachure_beton)" stroke="#333" stroke-width="1.5"/>'
    svg += f'<rect x="520" y="60" width="30" height="180" fill="url(#hachure_beton)" stroke="#333" stroke-width="1.5"/>'
    svg += f'<text x="65" y="55" text-anchor="middle" class="label">Acrotère</text>'

    # Relevé d'étanchéité
    svg += f'<rect x="50" y="100" width="30" height="80" fill="#ffccbc" stroke="#bf360c" stroke-width="1.5"/>'
    svg += f'<rect x="520" y="100" width="30" height="80" fill="#ffccbc" stroke="#bf360c" stroke-width="1.5"/>'
    svg += f'<line x1="30" y1="100" x2="50" y2="100" stroke="#bf360c" stroke-width="1" marker-end="url(#arrow)"/>'
    svg += f'<text x="5" y="96" class="cote" fill="#bf360c">Relevé</text>'
    svg += f'<text x="5" y="108" class="cote" fill="#bf360c">≥ 15 cm</text>'

    # Pente (flèche)
    svg += f'<line x1="80" y1="200" x2="520" y2="215" stroke="#1565c0" stroke-width="1" stroke-dasharray="5,3"/>'
    svg += f'<text x="300" y="230" text-anchor="middle" class="cote" fill="#1565c0">Pente ≥ 1,5%</text>'

    # Évacuation EP
    svg += f'<circle cx="300" cy="240" r="15" fill="#b3e5fc" stroke="#0288d1" stroke-width="2"/>'
    svg += f'<text x="300" y="244" text-anchor="middle" class="cote" fill="#0288d1">EP</text>'
    svg += f'<line x1="300" y1="255" x2="300" y2="280" stroke="#0288d1" stroke-width="2" marker-end="url(#arrow)"/>'
    svg += f'<text x="320" y="272" class="cote" fill="#0288d1">Évacuation EP</text>'

    # Cotes épaisseurs
    svg += cote(530, 80, 530, 240, "Épaisseur totale", offset=20, side="right")

    # Légende
    svg += f'<text x="{w//2}" y="{h-8}" text-anchor="middle" class="note">Réf. : DTU 43.1 — Travaux d\'étanchéité des toitures-terrasses avec éléments porteurs en maçonnerie</text>'
    svg += svg_end()
    return svg

# ─── Génération de toutes les figures ─────────────────────────────────────────

FIGURES = {
    "fondation-semelle-filante": gen_semelle_filante,
    "charpente-ferme-traditionnelle": gen_ferme_charpente,
    "mur-brique-parpaing-coupe": gen_mur_maconnerie,
    "plancher-hourdis-poutrelles": gen_plancher_poutrelles,
    "ventilation-vmc-simple-flux": gen_vmc_simple_flux,
    "fissure-facade-diagnostic": gen_fissures_facade,
    "etancheite-toiture-terrasse": gen_toiture_terrasse,
}

if __name__ == "__main__":
    for fig_id, gen_func in FIGURES.items():
        path = os.path.join(OUTPUT_DIR, f"{fig_id}.svg")
        svg_content = gen_func()
        with open(path, "w", encoding="utf-8") as f:
            f.write(svg_content)
        print(f"✓ {fig_id}.svg ({len(svg_content)} chars)")

    print(f"\n{len(FIGURES)} figures générées dans {OUTPUT_DIR}")
