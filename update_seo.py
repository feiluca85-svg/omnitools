import json

# 1. Aggiorniamo translations_hub.json con chiavi ad altissimo volume di ricerca SEO
with open('/Users/ilalu/Documents/Altenative Businnes/Calcolatore_Pendenza/translations_hub.json', 'r', encoding='utf-8') as f:
    hub = json.load(f)

# Italiano
hub['it']['title'] = "OmniTools Lab — Calcolatori Tecnici Online: Pendenze Rampe, Scale, Tubi e Dorso"
hub['it']['hero_title'] = "Calcolatori tecnici di precisione per cantiere, architettura e grafica."
hub['it']['hero_subtitle'] = "Calcolo rapido e conforme alle normative: pendenza rampe disabili (DM 236), alzata e pedata scale (Blondel), pendenza tubazioni di scarico (UNI EN 12056), spessore dorso libro e risoluzione stampa DPI."
hub['it']['tool_rampe_title'] = "Calcolo Pendenza Rampa"
hub['it']['tool_rampe_badge'] = "DM 236/89 & Garage"
hub['it']['tool_rampe_desc'] = "Calcolo pendenza in percentuale (%) e gradi, dislivello e lunghezza a terra con verifica disabili DM 236/89 e rampe carrabili."
hub['it']['tool_scale_title'] = "Calcolo Scale, Alzata e Pedata"
hub['it']['tool_scale_badge'] = "Legge di Blondel"
hub['it']['tool_scale_desc'] = "Dimensionamento ergonomico del numero di gradini, alzata e pedata con verifica della formula di Blondel 2a + p = 63 cm e DIN 18065."
hub['it']['tool_tubi_title'] = "Calcolo Pendenza Tubi e Scarichi"
hub['it']['tool_tubi_badge'] = "UNI EN 12056 & Fognature"
hub['it']['tool_tubi_desc'] = "Pendenza tubazioni di scarico, caduta per metro lineare (cm/m) e verifica autopulizia per acque nere e grigie secondo UNI EN 12056."
hub['it']['tool_dorso_title'] = "Calcolo Spessore Dorso Libro"
hub['it']['tool_dorso_badge'] = "Copertina & InDesign"
hub['it']['tool_dorso_desc'] = "Spessore dorso libro per brossura fresata e filo refe da numero pagine, grammatura e mano carta con quote e refili per InDesign."
hub['it']['tool_dpi_title'] = "Calcolo Risoluzione Stampa, Pixel e DPI"
hub['it']['tool_dpi_badge'] = "DPI ↔ cm ↔ Pixel"
hub['it']['tool_dpi_desc'] = "Conversione tra Pixel, Centimetri e DPI per stampa offset, digitale e grande formato con calcolo distanza visiva dell'occhio umano."

# Inglese
hub['en']['title'] = "OmniTools Lab — Free Engineering & Graphic Calculators: Ramp Slope, Stairs, Pipe Fall"
hub['en']['hero_title'] = "Precision technical calculators for job site, civil engineering and prepress."
hub['en']['hero_subtitle'] = "Instant, standard-compliant tools: ramp slope % (ADA & European norms), stair riser & tread (Blondel's formula), sewer pipe fall (EN 12056), and book spine width."
hub['en']['tool_rampe_title'] = "Ramp Slope Calculator"
hub['en']['tool_scale_title'] = "Stair Sizing & Step Calculator"
hub['en']['tool_tubi_title'] = "Sewer Pipe Fall & Slope Calculator"
hub['en']['tool_dorso_title'] = "Book Spine Width Calculator"
hub['en']['tool_dpi_title'] = "Print Resolution & DPI Calculator"

with open('/Users/ilalu/Documents/Altenative Businnes/Calcolatore_Pendenza/translations_hub.json', 'w', encoding='utf-8') as f:
    json.dump(hub, f, ensure_ascii=False, indent=2)

print("translations_hub.json updated with high-intent SEO keywords!")
