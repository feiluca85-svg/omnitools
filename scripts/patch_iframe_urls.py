import glob
import re

files = glob.glob('Calcolatore_Pendenza/*.html') + glob.glob('Calcolatore_Pendenza/en/*.html')

old_iframe = '<iframe src="${tool.url}" class="w-full flex-1 border-0"></iframe>'
new_iframe = '<iframe src="${(window.location.pathname.startsWith(\'/en/\') && tool.url_en) ? (tool.url_en + \'.html\') : (tool.url.replace(/^\\//, \'\') + \'.html\')}" class="w-full flex-1 border-0"></iframe>'

count = 0
for fp in files:
    with open(fp, 'r', encoding='utf-8') as f:
        c = f.read()
    
    if old_iframe in c:
        c = c.replace(old_iframe, new_iframe)
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(c)
        count += 1

print(f"Patched iframe src in {count} files.")
