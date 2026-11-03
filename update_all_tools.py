#!/usr/bin/env python3
import re
import subprocess

files = ['build_rampe_i18n.py', 'build_scale_i18n.py', 'build_dorso_i18n.py', 'build_dpi_i18n.py']

partner_banner = '''
                <div class="pt-2.5 text-center">
                    <a href="/partnership" class="inline-flex items-center gap-1.5 text-xs font-bold text-indigo-400 hover:text-indigo-300 transition">
                        <span>🤝</span> <span>Diventa Partner Ufficiale o Sponsor della Suite OmniTools</span>
                    </a>
                </div>
'''

tubi_box_active = '''                    <div class="p-2 rounded-xl bg-slate-800 border border-cyan-500/50 flex items-center justify-between transition">
                        <span class="font-bold text-white">🚰 ScaricoFacile</span>
                        <span class="text-[9px] px-1.5 py-0.2 bg-cyan-500/20 text-cyan-300 font-bold rounded">Attivo</span>
                    </div>'''

tubi_box_link = '''                    <a href="/tubi" class="p-2 rounded-xl bg-slate-800/60 hover:bg-slate-800 border border-slate-700/60 flex items-center justify-between transition group">
                        <span class="font-bold text-slate-300 group-hover:text-white">🚰 ScaricoFacile</span>
                        <span class="text-[9px] px-1.5 py-0.2 bg-cyan-500/20 text-cyan-400 font-bold rounded">Attivo</span>
                    </a>'''

for fn in files:
    path = f"/Users/ilalu/Documents/Altenative Businnes/Calcolatore_Pendenza/{fn}"
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Add insights script in head if missing
    if '/_vercel/insights/script.js' not in content:
        content = content.replace(
            '<script src="https://cdn.tailwindcss.com"></script>',
            '<script src="https://cdn.tailwindcss.com"></script>\n    <script defer src="/_vercel/insights/script.js"></script>'
        )

    # 2. Update the grid to 5 cols and add tubi + partner
    pattern = r'<div class="grid grid-cols-2 sm:grid-cols-4 gap-2 pt-3 text-\[11px\]">(.*?)</div>\s*</div>'
    match = re.search(pattern, content, re.DOTALL)
    if match:
        inner = match.group(1)
        if '/tubi' not in inner and 'ScaricoFacile' not in inner:
            # Add tubi link
            new_inner = inner.strip() + '\n' + tubi_box_link + '\n'
            replacement = f'<div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-5 gap-2 pt-3 text-[11px]">\n{new_inner}                </div>{partner_banner}            </div>'
            content = content[:match.start()] + replacement + content[match.end():]

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {fn}")

# Rebuild all HTML files
scripts = ['build_rampe_i18n.py', 'build_scale_i18n.py', 'build_dorso_i18n.py', 'build_dpi_i18n.py']
for s in scripts:
    print(f"Recompiling with {s}...")
    subprocess.run(["python3", f"/Users/ilalu/Documents/Altenative Businnes/Calcolatore_Pendenza/{s}"], check=True)

print("All tools recompiled successfully!")
