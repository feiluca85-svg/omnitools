import math
from PIL import Image, ImageDraw, ImageFont

def draw_logo(draw, x, y, size=80):
    # Background rounded rect for logo
    r = 20
    draw.rounded_rectangle([x, y, x + size, y + size], radius=r, fill="#2563eb", outline="#3b82f6", width=2)
    # Circle
    cx, cy = x + size / 2, y + size / 2
    radius = size * 0.38
    stroke = max(3, int(size * 0.09))
    draw.ellipse([cx - radius, cy - radius, cx + radius, cy + radius], outline="#ffffff", width=stroke)
    # Crosshair T
    top_y = cy - radius
    bot_y = cy + radius * 0.8
    bar_w = radius * 1.05
    draw.line([cx - bar_w, top_y + stroke, cx + bar_w, top_y + stroke], fill="#ffffff", width=stroke)
    draw.line([cx, top_y + stroke, cx, bot_y], fill="#ffffff", width=stroke)
    # Cyan center dot
    dot_r = stroke * 0.85
    draw.ellipse([cx - dot_r, top_y + stroke - dot_r, cx + dot_r, top_y + stroke + dot_r], fill="#38bdf8")

def create_og_card(filename, division, title, subtitle, pill_text, path_label):
    W, H = 1200, 630
    img = Image.new("RGB", (W, H), color="#0b1329")
    draw = ImageDraw.Draw(img)

    # Subtle radial glow simulation in center-top
    for r in range(400, 0, -10):
        alpha = int(25 * (1 - r / 400))
        # Draw soft concentric circles
        draw.ellipse([W/2 - r*1.3, -50 - r*0.5, W/2 + r*1.3, 350 + r*0.5], outline=(37, 99, 235, alpha))

    # Grid background pattern
    grid_color = (255, 255, 255, 12)
    for gx in range(0, W, 50):
        draw.line([(gx, 0), (gx, H)], fill="#111c3a", width=1)
    for gy in range(0, H, 50):
        draw.line([(0, gy), (W, gy)], fill="#111c3a", width=1)

    # Accent top border
    draw.line([(0, 0), (W, 0)], fill="#3b82f6", width=6)

    # Load system fonts
    font_bold = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
    font_reg = "/System/Library/Fonts/Supplemental/Arial.ttf"
    
    f_brand = ImageFont.truetype(font_bold, 36)
    f_badge = ImageFont.truetype(font_bold, 18)
    f_title = ImageFont.truetype(font_bold, 54)
    f_sub = ImageFont.truetype(font_reg, 24)
    f_tag = ImageFont.truetype(font_bold, 20)
    f_url = ImageFont.truetype(font_bold, 22)

    # Top brand bar
    draw_logo(draw, 70, 60, size=70)
    draw.text((155, 68), "OmniTools", fill="#ffffff", font=f_brand)
    bbox_ot = draw.textbbox((155, 68), "OmniTools", font=f_brand)
    draw.text((bbox_ot[2] + 4, 68), "Lab", fill="#38bdf8", font=f_brand)
    
    # Division Badge Pill
    div_bbox = draw.textbbox((0, 0), division, font=f_badge)
    div_w = div_bbox[2] - div_bbox[0] + 24
    div_x = W - 70 - div_w
    draw.rounded_rectangle([div_x, 72, div_x + div_w, 108], radius=18, fill="#1e293b", outline="#334155", width=2)
    draw.text((div_x + 12, 80), division, fill="#94a3b8", font=f_badge)

    # Main Card Title (word wrap if needed)
    words = title.split()
    lines = []
    curr = []
    for w in words:
        curr.append(w)
        line_str = " ".join(curr)
        bbox = draw.textbbox((0, 0), line_str, font=f_title)
        if (bbox[2] - bbox[0]) > 1050:
            curr.pop()
            lines.append(" ".join(curr))
            curr = [w]
    if curr:
        lines.append(" ".join(curr))

    y_text = 200
    for line in lines[:3]:
        draw.text((70, y_text), line, fill="#ffffff", font=f_title)
        y_text += 68

    # Subtitle
    y_text += 12
    draw.text((70, y_text), subtitle, fill="#94a3b8", font=f_sub)

    # Feature Tag Pill at Bottom Left
    draw.rounded_rectangle([70, H - 110, 70 + 440, H - 60], radius=14, fill="#1e293b", outline="#3b82f6", width=2)
    draw.text((90, H - 96), pill_text, fill="#38bdf8", font=f_tag)

    # URL watermark at Bottom Right
    draw.text((W - 70 - draw.textbbox((0, 0), path_label, font=f_url)[2], H - 94), path_label, fill="#64748b", font=f_url)

    img.save(filename, "PNG", optimize=True)
    print(f"Generated {filename}")

if __name__ == "__main__":
    cards = [
        (
            "og-hub.png",
            "SUITE DI CALCOLO",
            "Tutti gli strumenti di calcolo tecnico, a portata di click.",
            "Precisione millimetrica per cantiere, grafica ed editoria. 100% gratuito e offline.",
            "⚡ ZERO LOGIN • 100% OFFLINE",
            "omnitoolslab.com"
        ),
        (
            "og-rampe.png",
            "🏗️ OMNIBUILDING",
            "Calcolo Pendenza Rampa & Dislivello",
            "Verifica conformità normativa DM 236/89, ADA & rampe garage carrabili.",
            "📐 DM 236/89 • SCHEDA A4",
            "omnitoolslab.com/rampe"
        ),
        (
            "og-scale.png",
            "🏗️ OMNIBUILDING",
            "Calcolo Scale, Alzata & Pedata",
            "Dimensionamento ergonomico del numero di gradini con la Legge di Blondel.",
            "🪜 BLONDEL 2a + p = 63 • DIN 18065",
            "omnitoolslab.com/scale"
        ),
        (
            "og-dorso.png",
            "🎨 OMNIGRAPH",
            "Calcolo Spessore Dorso Libro & Copertina",
            "Calcolo esatto del dorso per pagine, grammatura e mano con refili per InDesign.",
            "📖 BROSSURA & PUR • REFILO 3 MM",
            "omnitoolslab.com/dorso"
        ),
        (
            "og-dpi.png",
            "🎨 OMNIGRAPH",
            "Calcolo Risoluzione Stampa, Pixel & DPI",
            "Conversione istantanea Pixel ↔ cm ↔ DPI con acuità visiva e distanza occhio.",
            "🖼️ OFFSET • DIGITALE • GRANDE FORMATO",
            "omnitoolslab.com/dpi"
        )
    ]
    for fn, div, tit, sub, pil, path in cards:
        create_og_card(f"/Users/ilalu/Documents/Altenative Businnes/Calcolatore_Pendenza/{fn}", div, tit, sub, pil, path)
