import math
from PIL import Image, ImageDraw

def create_modern_logo(size=512):
    scale = 2
    dim = size * scale
    img = Image.new('RGBA', (dim, dim), (0, 0, 0, 0))
    
    # 1. Vibrant Electric Cobalt Blue rounded background
    bg_margin = int(10 * scale)
    corner_radius = int(105 * scale)
    
    mask = Image.new('L', (dim, dim), 0)
    mask_draw = ImageDraw.Draw(mask)
    mask_draw.rounded_rectangle(
        [bg_margin, bg_margin, dim - bg_margin, dim - bg_margin],
        radius=corner_radius,
        fill=255
    )
    
    grad = Image.new('RGBA', (dim, dim))
    for y in range(dim):
        ratio = y / dim
        r = int(37 * (1 - ratio) + 29 * ratio)
        g = int(99 * (1 - ratio) + 78 * ratio)
        b = int(235 * (1 - ratio) + 216 * ratio)
        for x in range(dim):
            grad.putpixel((x, y), (r, g, b, 255))
            
    img.paste(grad, (0, 0), mask)
    draw = ImageDraw.Draw(img)

    center = dim / 2
    
    # 2. BOLD & LARGE: White symbol fills ~78% of the squircle
    ring_radius = 210 * scale
    ring_width = int(46 * scale)
    draw.ellipse(
        [center - ring_radius, center - ring_radius, center + ring_radius, center + ring_radius],
        outline=(255, 255, 255, 255),
        width=ring_width
    )
    
    # Horizontal bar of T
    bar_w = 270 * scale
    bar_h = 46 * scale
    bar_y = center - 75 * scale
    draw.rounded_rectangle(
        [center - bar_w/2, bar_y - bar_h/2, center + bar_w/2, bar_y + bar_h/2],
        radius=int(23 * scale),
        fill=(255, 255, 255, 255)
    )
    
    # Vertical stem of T
    stem_w = 46 * scale
    stem_top = bar_y
    stem_bottom = center + 130 * scale
    draw.rounded_rectangle(
        [center - stem_w/2, stem_top, center + stem_w/2, stem_bottom],
        radius=int(23 * scale),
        fill=(255, 255, 255, 255)
    )
    
    # Central Cyan/Sky Blue Precision Focus Point
    dot_r = 28 * scale
    draw.ellipse(
        [center - dot_r, bar_y - dot_r, center + dot_r, bar_y + dot_r],
        fill=(56, 189, 248, 255)
    )

    final = img.resize((size, size), Image.Resampling.LANCZOS)
    return final

icon_512 = create_modern_logo(512)
icon_512.save("/Users/ilalu/Documents/Altenative Businnes/Calcolatore_Pendenza/icon-512.png")

icon_192 = create_modern_logo(192)
icon_192.save("/Users/ilalu/Documents/Altenative Businnes/Calcolatore_Pendenza/icon-192.png")

icon_64 = create_modern_logo(64)
icon_64.save("/Users/ilalu/Documents/Altenative Businnes/Calcolatore_Pendenza/favicon.png")

print("Re-generated larger, bold high-impact logo icons successfully!")
