import json

with open('/Users/ilalu/Documents/Altenative Businnes/Calcolatore_Pendenza/translations_hub.json', 'r', encoding='utf-8') as f:
    hub_t = json.load(f)

copertura_data = {
    "it": {
        "tool_copertura_title": "CoperturaFacile",
        "tool_copertura_hook": "Quanto inchiostro consumerà la commessa?",
        "tool_copertura_desc": "Analisi densitometrica CMYK e TAC (Total Area Coverage) in tempo reale. Calcola il consumo in grammi e il costo copia con privacy totale.",
        "tool_copertura_cta": "Calcola Copertura & Costi",
        "tool_copertura_badge": "CMYK & Costo Copia"
    },
    "en": {
        "tool_copertura_title": "InkCoverage",
        "tool_copertura_hook": "How much ink will the print run consume?",
        "tool_copertura_desc": "Real-time CMYK densitometric and TAC (Total Area Coverage) analysis. Calculate consumption in grams and cost per copy client-side.",
        "tool_copertura_cta": "Calculate Coverage & Cost",
        "tool_copertura_badge": "CMYK & Cost per Copy"
    },
    "es": {
        "tool_copertura_title": "CoberturaFacil",
        "tool_copertura_hook": "¿Cuánta tinta consumirá la tirada?",
        "tool_copertura_desc": "Análisis densitométrico CMYK y TAC en tiempo real. Calcula el consumo en gramos y coste por copia con total privacidad.",
        "tool_copertura_cta": "Calcular Cobertura y Costes",
        "tool_copertura_badge": "CMYK y Coste Copia"
    },
    "fr": {
        "tool_copertura_title": "CouvertureEncre",
        "tool_copertura_hook": "Combien d'encre consommera le tirage ?",
        "tool_copertura_desc": "Analyse densitométrique CMJN et TAC en temps réel. Calcule la consommation en grammes et le coût par tirage en toute confidentialité.",
        "tool_copertura_cta": "Calculer Couverture & Coûts",
        "tool_copertura_badge": "CMJN & Coût Copie"
    },
    "de": {
        "tool_copertura_title": "FarbdeckungRechner",
        "tool_copertura_hook": "Wie viel Farbe verbraucht der Druckauftrag?",
        "tool_copertura_desc": "Echtzeit-Densitometrie für CMYK & TAC (Total Area Coverage). Berechnet Farbverbrauch in Gramm und Stückkosten lokal im Browser.",
        "tool_copertura_cta": "Farbdeckung Berechnen",
        "tool_copertura_badge": "CMYK & Stückkosten"
    },
    "pt": {
        "tool_copertura_title": "CoberturaTinta",
        "tool_copertura_hook": "Quanta tinta gastará a tiragem?",
        "tool_copertura_desc": "Análise densitométrica CMYK e TAC em tempo real. Calcule o consumo em gramas e o custo por cópia com total privacidade.",
        "tool_copertura_cta": "Calcular Cobertura e Custos",
        "tool_copertura_badge": "CMYK e Custo Cópia"
    }
}

for lang in hub_t:
    if lang in copertura_data:
        hub_t[lang].update(copertura_data[lang])

with open('/Users/ilalu/Documents/Altenative Businnes/Calcolatore_Pendenza/translations_hub.json', 'w', encoding='utf-8') as f:
    json.dump(hub_t, f, ensure_ascii=False, indent=2)

print("translations_hub.json updated with tool_copertura.")
