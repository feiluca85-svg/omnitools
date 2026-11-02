import math
from PIL import Image, ImageDraw

def create_modern_logo(size=512):
    scale = 2
    dim = size * scale
    img = Image.new('RGBA', (dim, dim), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # 1. Vibrant Electric Cobalt Blue rounded background (Apple / Figma style)
    # Gradient from #2563eb (electric blue) to #1d4ed8 (deep cobalt)
    bg_margin = int(12 * scale)
    corner_radius = int(112 * scale)
    
    # Draw gradient rounded rect
    for i in range(dim):
        ratio = i / dim
        # Linear blend from #3b82f6 to #1e40af
        r = int(59 * (1 - ratio) + 30 * ratio)
        g = int(130 * (1 - ratio) + 64 * ratio)
        b = int(246 * (1 - ratio) + 175 * ratio)
        # We can draw line by line or use a mask
    
    # Simpler and perfectly crisp with mask:
    mask = Image.new('L', (dim, dim), 0)
    mask_draw = ImageDraw.Draw(mask)
    mask_draw.rounded_rectangle(
        [bg_margin, bg_margin, dim - bg_margin, dim - bg_margin],
        radius=corner_radius,
        fill=255
    )
    
    # Gradient canvas
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

    # 2. Modern Swiss Icon: Bold Geometric "Omni-Ring" + "Precision Drafting T"
    center = dim / 2
    
    # Outer Ring 'O' - Bold, pure white
    ring_radius = 160 * scale
    ring_width = int(34 * scale)
    draw.ellipse(
        [center - ring_radius, center - ring_radius, center + ring_radius, center + ring_radius],
        outline=(255, 255, 255, 255),
        width=ring_width
    )
    
    # Horizontal bar of T
    bar_w = 210 * scale
    bar_h = 34 * scale
    bar_y = center - 65 * scale
    draw.rounded_rectangle(
        [center - bar_w/2, bar_y - bar_h/2, center + bar_w/2, bar_y + bar_h/2],
        radius=int(17 * scale),
        fill=(255, 255, 255, 255)
    )
    
    # Vertical stem of T
    stem_w = 34 * scale
    stem_top = bar_y
    stem_bottom = center + 95 * scale
    draw.rounded_rectangle(
        [center - stem_w/2, stem_top, center + stem_w/2, stem_bottom],
        radius=int(17 * scale),
        fill=(255, 255, 255, 255)
    )
    
    # Central Cyan/Sky Blue Precision Focus Point
    dot_r = 22 * scale
    draw.ellipse(
        [center - dot_r, bar_y - dot_r, center + dot_r, bar_y + dot_r],
        fill=(56, 189, 248, 255) # cyan-400
    )

    final = img.resize((size, size), Image.Resampling.LANCZOS)
    return final

icon_512 = create_modern_logo(512)
icon_512.save("/Users/ilalu/Documents/Altenative Businnes/Calcolatore_Pendenza/icon-512.png")

icon_192 = create_modern_logo(192)
icon_192.save("/Users/ilalu/Documents/Altenative Businnes/Calcolatore_Pendenza/icon-192.png")

icon_64 = create_modern_logo(64)
icon_64.save("/Users/ilalu/Documents/Altenative Businnes/Calcolatore_Pendenza/favicon.png")

print("Generated modern high-contrast logos successfully!")
