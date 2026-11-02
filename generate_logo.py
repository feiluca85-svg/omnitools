import math
from PIL import Image, ImageDraw, ImageFilter

def create_omnitools_icon(size=512):
    # High-resolution super-sampling for silky smooth anti-aliased geometry
    scale = 2
    dim = size * scale
    img = Image.new('RGBA', (dim, dim), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    center = dim / 2
    
    # Background: modern dark squircle with subtle radial/vertical depth
    bg_margin = int(12 * scale)
    corner_radius = int(108 * scale)
    
    # Base squircle
    draw.rounded_rectangle(
        [bg_margin, bg_margin, dim - bg_margin, dim - bg_margin],
        radius=corner_radius,
        fill=(15, 23, 42, 255) # slate-900
    )

    # Subtle inner glow / gradient layer
    overlay = Image.new('RGBA', (dim, dim), (0, 0, 0, 0))
    ov_draw = ImageDraw.Draw(overlay)
    ov_draw.rounded_rectangle(
        [bg_margin + 2*scale, bg_margin + 2*scale, dim - bg_margin - 2*scale, dim - bg_margin - 2*scale],
        radius=corner_radius - 2*scale,
        outline=(51, 65, 85, 200), # slate-700
        width=int(3 * scale)
    )
    img = Image.alpha_composite(img, overlay)
    draw = ImageDraw.Draw(img)

    # Geometric OmniTools Emblem:
    # An isometric interlocking Hexa-O / Infinity Prism
    # 6 outer vertices and 6 inner vertices representing 360° totality (Omni) & calibrated tools (Tools)
    r_outer = 175 * scale
    r_mid = 118 * scale
    r_inner = 55 * scale

    def hex_pt(r, angle_deg):
        rad = math.radians(angle_deg - 30)
        return (center + r * math.cos(rad), center + r * math.sin(rad))

    # Outer 6 vertices (0, 60, 120, 180, 240, 300)
    p_out = [hex_pt(r_outer, i * 60) for i in range(6)]
    p_mid = [hex_pt(r_mid, i * 60) for i in range(6)]
    p_in  = [hex_pt(r_inner, i * 60) for i in range(6)]

    # Dynamic 3-facet dimensional planes (Cobalt Blue, Cyan, Indigo-Violet)
    # Facet 1: Top Right & Top (Electric Blue #2563eb -> #3b82f6)
    f1 = [p_out[0], p_out[1], p_mid[1], p_in[1], p_in[0], p_mid[0]]
    draw.polygon(f1, fill=(37, 99, 235, 255))

    # Facet 2: Bottom & Bottom Right (Cyan / Precision Teal #06b6d4 -> #0ea5e9)
    f2 = [p_out[1], p_out[2], p_out[3], p_mid[3], p_in[2], p_mid[1]]
    draw.polygon(f2, fill=(14, 165, 233, 255))

    # Facet 3: Left & Top Left (Deep Indigo / Violet #4f46e5 -> #6366f1)
    f3 = [p_out[3], p_out[4], p_out[5], p_out[0], p_mid[0], p_in[5], p_in[4], p_mid[3]]
    draw.polygon(f3, fill=(79, 70, 229, 255))

    # Add the central "T-Square / Precision drafting nexus" in crisp white & translucent glow
    # This forms the "T" inside the "O", representing Tools within Omni
    t_bar_h = 24 * scale
    t_stem_w = 26 * scale
    
    # Precision caliper / compass diamond accent at the core
    core_pts = [
        (center, center - 62 * scale),
        (center + 42 * scale, center + 15 * scale),
        (center, center + 55 * scale),
        (center - 42 * scale, center + 15 * scale)
    ]
    draw.polygon(core_pts, fill=(255, 255, 255, 240))
    
    # Internal acute drafting notch (creating the stylized T)
    notch = [
        (center - 18 * scale, center - 62 * scale),
        (center + 18 * scale, center - 62 * scale),
        (center + 18 * scale, center + 38 * scale),
        (center - 18 * scale, center + 38 * scale)
    ]
    draw.polygon(notch, fill=(15, 23, 42, 255))

    # Central pivot pin (gold/amber precision bead)
    pivot_r = 11 * scale
    draw.ellipse(
        [center - pivot_r, center - pivot_r, center + pivot_r, center + pivot_r],
        fill=(245, 158, 11, 255) # amber-500
    )

    # Downsample with Lanczos filter for ultra-sharp anti-aliasing
    final_img = img.resize((size, size), Image.Resampling.LANCZOS)
    return final_img

# Generate 512, 192, and a 64px favicon
icon_512 = create_omnitools_icon(512)
icon_512.save("/Users/ilalu/Documents/Altenative Businnes/Calcolatore_Pendenza/icon-512.png")

icon_192 = create_omnitools_icon(192)
icon_192.save("/Users/ilalu/Documents/Altenative Businnes/Calcolatore_Pendenza/icon-192.png")

icon_64 = create_omnitools_icon(64)
icon_64.save("/Users/ilalu/Documents/Altenative Businnes/Calcolatore_Pendenza/favicon.png")

print("Generated icon-512.png, icon-192.png, favicon.png successfully")
