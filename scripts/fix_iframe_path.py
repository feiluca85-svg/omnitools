import glob
import re

files = glob.glob('Calcolatore_Pendenza/*.html') + glob.glob('Calcolatore_Pendenza/en/*.html')

target_expr = '<iframe src="${(window.location.pathname.startsWith(\'/en/\') && tool.url_en) ? (tool.url_en + \'.html\') : (tool.url.replace(/^\\//, \'\') + \'.html\')}" class="w-full flex-1 border-0"></iframe>'
clean_expr = '<iframe src="${(window.location.pathname.startsWith(\'/en/\') && tool.url_en) ? (\'/\' + tool.url_en.replace(/^\\/+/, \'\') + \'.html\') : (\'/\' + tool.url.replace(/^\\/+/, \'\') + \'.html\')}" class="w-full flex-1 border-0"></iframe>'

count = 0
for fp in files:
    with open(fp, 'r', encoding='utf-8') as f:
        c = f.read()
    
    if target_expr in c:
        c = c.replace(target_expr, clean_expr)
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(c)
        count += 1

print(f"Patched iframe src clean in {count} files.")
