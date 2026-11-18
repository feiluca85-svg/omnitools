import glob

files = glob.glob('Calcolatore_Pendenza/*.html') + glob.glob('Calcolatore_Pendenza/en/*.html')
matching = []
for fp in files:
    with open(fp, 'r', encoding='utf-8') as f:
        c = f.read()
    if '<iframe src="${tool.url}"' in c:
        matching.append(fp)
print(f"Found {len(matching)} files with iframe src tool.url")
