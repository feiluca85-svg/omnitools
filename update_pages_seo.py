import re

g_tag = '<meta name="google-site-verification" content="MRdbDm9lLhokeD3I0FOpUSOhNaF_2WaveKvu52FxtG4">'

# 1. build_scale_i18n.py
with open('/Users/ilalu/Documents/Altenative Businnes/Calcolatore_Pendenza/build_scale_i18n.py', 'r', encoding='utf-8') as f:
    scale_code = f.read()

scale_code = re.sub(
    r'<title>.*?</title>',
    '<title>Calcolo Scale, Alzata e Pedata Online — Formula di Blondel (2a + p = 63 cm)</title>',
    scale_code, count=1
)
scale_code = re.sub(
    r'<meta name="description" content=".*?">',
    '<meta name="description" content="Calcolatore professionale per il dimensionamento di scale interne, esterne e da cantiere. Calcolo automatico di alzata, pedata, numero gradini, pendenza e verifica ergonomica con Legge di Blondel (2a + p = 63 cm) e norme DIN 18065.">',
    scale_code, count=1
)
if g_tag not in scale_code:
    scale_code = scale_code.replace('<head>', f'<head>\n    {g_tag}')

with open('/Users/ilalu/Documents/Altenative Businnes/Calcolatore_Pendenza/build_scale_i18n.py', 'w', encoding='utf-8') as f:
    f.write(scale_code)
print("build_scale_i18n.py SEO updated")

# 2. build_tubi_i18n.py
with open('/Users/ilalu/Documents/Altenative Businnes/Calcolatore_Pendenza/build_tubi_i18n.py', 'r', encoding='utf-8') as f:
    tubi_code = f.read()

tubi_code = re.sub(
    r'<title>.*?</title>',
    '<title>Calcolo Pendenza Tubi di Scarico e Fognatura — Dislivello e Autopulizia UNI EN 12056</title>',
    tubi_code, count=1
)
tubi_code = re.sub(
    r'<meta name="description" content=".*?">',
    '<meta name="description" content="Calcolatore online per pendenza tubazioni di scarico fognario, caduta per metro lineare (cm/m), dislivello e dimensionamento diametri Ø 40-200 mm con verifica di autopulizia acque nere e grigie secondo UNI EN 12056 e UNI EN 752.">',
    tubi_code, count=1
)
if g_tag not in tubi_code:
    tubi_code = tubi_code.replace('<head>', f'<head>\n    {g_tag}')

with open('/Users/ilalu/Documents/Altenative Businnes/Calcolatore_Pendenza/build_tubi_i18n.py', 'w', encoding='utf-8') as f:
    f.write(tubi_code)
print("build_tubi_i18n.py SEO updated")

# 3. build_rampe_i18n.py
with open('/Users/ilalu/Documents/Altenative Businnes/Calcolatore_Pendenza/build_rampe_i18n.py', 'r', encoding='utf-8') as f:
    rampe_code = f.read()

rampe_code = re.sub(
    r'<title>.*?</title>',
    '<title>Calcolo Pendenza Rampa Disabili e Garage Online — Formula DM 236/89 & ADA</title>',
    rampe_code, count=1
)
rampe_code = re.sub(
    r'<meta name="description" content=".*?">',
    '<meta name="description" content="Calcolatore professionale per pendenza rampe in percentuale (%) e gradi, dislivello e sviluppo a terra. Verifica immediata conformità per disabili e carrozzine (DM 236/89, ADA) e rampe carrabili autorimesse.">',
    rampe_code, count=1
)
if g_tag not in rampe_code:
    rampe_code = rampe_code.replace('<head>', f'<head>\n    {g_tag}')

with open('/Users/ilalu/Documents/Altenative Businnes/Calcolatore_Pendenza/build_rampe_i18n.py', 'w', encoding='utf-8') as f:
    f.write(rampe_code)
print("build_rampe_i18n.py SEO updated")

# 4. build_dorso_i18n.py
with open('/Users/ilalu/Documents/Altenative Businnes/Calcolatore_Pendenza/build_dorso_i18n.py', 'r', encoding='utf-8') as f:
    dorso_code = f.read()

dorso_code = re.sub(
    r'<title>.*?</title>',
    '<title>Calcolo Spessore Dorso Libro e Copertina Stesa Online — InDesign & KDP</title>',
    dorso_code, count=1
)
dorso_code = re.sub(
    r'<meta name="description" content=".*?">',
    '<meta name="description" content="Calcolatore professionale di spessore del dorso libro e copertina aperta con refili 3 mm per brossura fresata, colla PUR e filo refe. Calcolo esatto da numero pagine, grammatura e mano carta con quote per Adobe InDesign e Amazon KDP.">',
    dorso_code, count=1
)
if g_tag not in dorso_code:
    dorso_code = dorso_code.replace('<head>', f'<head>\n    {g_tag}')

with open('/Users/ilalu/Documents/Altenative Businnes/Calcolatore_Pendenza/build_dorso_i18n.py', 'w', encoding='utf-8') as f:
    f.write(dorso_code)
print("build_dorso_i18n.py SEO updated")

# 5. build_dpi_i18n.py
with open('/Users/ilalu/Documents/Altenative Businnes/Calcolatore_Pendenza/build_dpi_i18n.py', 'r', encoding='utf-8') as f:
    dpi_code = f.read()

dpi_code = re.sub(
    r'<title>.*?</title>',
    '<title>Convertitore Pixel Centimetri e DPI — Calcolo Risoluzione Stampa e Distanza Occhio</title>',
    dpi_code, count=1
)
dpi_code = re.sub(
    r'<meta name="description" content=".*?">',
    '<meta name="description" content="Convertitore online tra Pixel, Centimetri e Risoluzione DPI/PPI per stampa tipografica, offset, digitale e grande formato (poster, manifesti). Include formula acuità visiva dell\'occhio umano in base alla distanza di osservazione.">',
    dpi_code, count=1
)
if g_tag not in dpi_code:
    dpi_code = dpi_code.replace('<head>', f'<head>\n    {g_tag}')

with open('/Users/ilalu/Documents/Altenative Businnes/Calcolatore_Pendenza/build_dpi_i18n.py', 'w', encoding='utf-8') as f:
    f.write(dpi_code)
print("build_dpi_i18n.py SEO updated")
