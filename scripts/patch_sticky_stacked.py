import glob

files = glob.glob('Calcolatore_Pendenza/*.html') + glob.glob('Calcolatore_Pendenza/en/*.html')

css_target = '#omniChromeTabsBar {\n            background-color: #ffffff !important;\n            border-bottom: 1px solid #e2e8f0 !important;\n        }'
css_fixed = '''#omniChromeTabsBar {
            position: sticky !important;
            top: 0px !important;
            z-index: 50 !important;
            background-color: #ffffff !important;
            border-bottom: 1px solid #e2e8f0 !important;
        }
        header.sticky {
            position: sticky !important;
            top: 42px !important;
            z-index: 40 !important;
        }'''

count = 0
for fp in files:
    with open(fp, 'r', encoding='utf-8') as f:
        c = f.read()

    changed = False
    if css_target in c:
        c = c.replace(css_target, css_fixed)
        changed = True

    # Also update any header class that has md:top-[38px] to md:top-[42px]
    if 'md:top-[38px]' in c:
        c = c.replace('md:top-[38px]', 'md:top-[42px]')
        changed = True

    if changed:
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(c)
        count += 1

print(f"Updated sticky header & tabs alignment across {count} HTML files.")
