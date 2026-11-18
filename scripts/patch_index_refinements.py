import json
import re

with open('Calcolatore_Pendenza/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update TRANSLATIONS JSON
pattern = r'const TRANSLATIONS = (\{.*?\});\s+function detectInitialLanguage'
m = re.search(pattern, text, re.DOTALL)
if m:
    data = json.loads(m.group(1))
    
    # English
    data['en']['hero_title'] = "Real-time technical calculations & verification."
    data['en']['hero_subtitle'] = "Precision engineering and financial offline calculators for construction, MEP, print and business. Reference formulas, zero sign-up, instant offline readiness."
    
    # Spanish
    if 'es' in data:
        data['es']['hero_title'] = "Cálculos y verificaciones técnicas en tiempo real."
        data['es']['hero_subtitle'] = "Calculadoras técnicas de precisión para construcción, instalaciones, gráfica y finanzas. Fórmulas de referencia, sin registro, listas offline."
        
    # French
    if 'fr' in data:
        data['fr']['hero_title'] = "Calculs et vérifications techniques en temps réel."
        data['fr']['hero_subtitle'] = "Calculateurs techniques de précision pour le bâtiment, les réseaux, le graphisme et la finance. Formules de référence, sans inscription, prêts hors-ligne."

    # German
    if 'de' in data:
        data['de']['hero_title'] = "Technische Berechnungen & Prüfungen in Echtzeit."
        data['de']['hero_subtitle'] = "Präzise technische Rechner für Bau, Haustechnik, Druck und Finanzen. Referenzformeln, ohne Registrierung, sofort offline bereit."

    # Portuguese
    if 'pt' in data:
        data['pt']['hero_title'] = "Cálculos e verificações técnicas em tempo real."
        data['pt']['hero_subtitle'] = "Calculadoras técnicas de precisão para construção, instalações, gráfica e finanças. Fórmulas de referência, sem registo, prontas offline."

    new_json_str = json.dumps(data, ensure_ascii=False)
    text = text[:m.start(1)] + new_json_str + text[m.end(1):]
    print("Updated TRANSLATIONS in index.html successfully!")
else:
    print("Could not find TRANSLATIONS in index.html")

# 2. Update OmniFood filter button styling
# Replace #filterFoodBtn .icon-square color from #0284c7 to #ea580c
text = text.replace(
    '#filterFoodBtn .icon-square { background-color: #0284c7 !important; }',
    '#filterFoodBtn .icon-square { background-color: #ea580c !important; }'
)

text = text.replace(
    '.omni-filter-btn.active-food {\n            border: 1.5px solid #0284c7 !important;\n            background-color: #f0f9ff !important;\n        }',
    '.omni-filter-btn.active-food {\n            border: 1.5px solid #ea580c !important;\n            background-color: #fff7ed !important;\n        }'
)

text = text.replace(
    'html.omni-dark .omni-filter-btn.active-food { background-color: rgba(12, 74, 110, 0.3) !important; }',
    'html.omni-dark .omni-filter-btn.active-food { background-color: rgba(194, 65, 12, 0.3) !important; }'
)

# 3. Update Hero Title single line rendering on desktop
# We want white-space: nowrap on desktop (lg / xl), responsive font size
old_hero_style = '''        /* Hero Title */
        #heroTitle {
            font-size: clamp(30px, 4.5vw, 42px) !important;
            line-height: 1.15 !important;
            font-weight: 800 !important;
            color: #0f172a !important;
            letter-spacing: -0.025em !important;
            margin-top: 12px !important;
            margin-bottom: 14px !important;
            display: block !important;
        }'''

new_hero_style = '''        /* Hero Title */
        #heroTitle {
            font-size: clamp(24px, 3.2vw, 38px) !important;
            line-height: 1.15 !important;
            font-weight: 800 !important;
            color: #0f172a !important;
            letter-spacing: -0.025em !important;
            margin-top: 12px !important;
            margin-bottom: 14px !important;
            display: block !important;
            max-width: 960px !important;
            margin-left: auto !important;
            margin-right: auto !important;
        }
        @media (min-width: 860px) {
            #heroTitle {
                white-space: nowrap !important;
            }
        }'''

if old_hero_style in text:
    text = text.replace(old_hero_style, new_hero_style)
    print("Updated #heroTitle style successfully!")
else:
    print("old_hero_style not found")

# Also update the HTML tag class of #heroTitle:
text = text.replace(
    '<h1 id="heroTitle" class="text-[30px] sm:text-[42px] font-extrabold text-[#0F172A] dark:text-white tracking-[-0.025em] leading-[1.15] max-w-3xl mx-auto mt-3 mb-3.5">',
    '<h1 id="heroTitle" class="text-[24px] sm:text-[34px] md:text-[38px] font-extrabold text-[#0F172A] dark:text-white tracking-[-0.025em] leading-[1.15] max-w-5xl mx-auto mt-3 mb-3.5 whitespace-normal md:whitespace-nowrap">'
)

# 4. Update the sharp rules for tabs in index.html to white theme
old_tab_rules = '''        #omniChromeTabsBar {
            background-color: #020617 !important;
            border-bottom: 1px solid #1e293b !important;
        }
        #omniTabHome {
            background-color: #1e293b !important;
            color: #ffffff !important;
            border-top: 2px solid #2563eb !important;
            border-right: 1px solid #334155 !important;
            border-radius: 0px !important;
        }
        #omniTabHome svg, #omniTabHome span {
            color: #ffffff !important;
            stroke: #ffffff !important;
        }
        .omni-dyn-tab {
            height: 34px !important;
            border-radius: 0px !important;
            display: inline-flex !important;
            align-items: center !important;
        }
        .omni-dyn-tab.active-tab {
            background-color: #1e293b !important;
            color: #ffffff !important;
            border-top: 2px solid #3b82f6 !important;
            border-right: 1px solid #334155 !important;
            font-weight: 600 !important;
        }
        .omni-dyn-tab.inactive-tab {
            background-color: #0f172a !important;
            color: #cbd5e1 !important;
            border-top: 2px solid transparent !important;
            border-right: 1px solid #1e293b !important;
            font-weight: 500 !important;
        }
        .omni-dyn-tab a {
            color: inherit !important;
            text-decoration: none !important;
        }
        .omni-dyn-tab .close-tab {
            color: #94a3b8 !important;
        }
        .omni-dyn-tab .close-tab:hover {
            color: #ffffff !important;
            background-color: #e11d48 !important;
        }'''

new_tab_rules = '''        #omniChromeTabsBar {
            background-color: #ffffff !important;
            border-bottom: 1px solid #e2e8f0 !important;
        }
        #omniTabHome {
            background-color: #ffffff !important;
            color: #0f172a !important;
            border-top: 2px solid #2563eb !important;
            border-right: 1px solid #cbd5e1 !important;
            border-radius: 0px !important;
            font-weight: 700 !important;
            box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.05) !important;
        }
        #omniTabHome svg {
            color: #2563eb !important;
            stroke: #2563eb !important;
        }
        #omniTabHome span {
            color: #0f172a !important;
        }
        .omni-dyn-tab {
            height: 34px !important;
            border-radius: 0px !important;
            display: inline-flex !important;
            align-items: center !important;
        }
        .omni-dyn-tab.active-tab {
            background-color: #ffffff !important;
            color: #0f172a !important;
            border-top: 2px solid #2563eb !important;
            border-right: 1px solid #cbd5e1 !important;
            font-weight: 700 !important;
            box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.05) !important;
        }
        .omni-dyn-tab.inactive-tab {
            background-color: #f8fafc !important;
            color: #475569 !important;
            border-top: 2px solid transparent !important;
            border-right: 1px solid #e2e8f0 !important;
            font-weight: 500 !important;
        }
        .omni-dyn-tab.inactive-tab:hover {
            background-color: #f1f5f9 !important;
            color: #0f172a !important;
        }
        .omni-dyn-tab a {
            color: inherit !important;
            text-decoration: none !important;
        }
        .omni-dyn-tab .close-tab {
            color: #94a3b8 !important;
        }
        .omni-dyn-tab .close-tab:hover {
            color: #ffffff !important;
            background-color: #e11d48 !important;
        }

        /* Top Bar DESK and Nuovo Tool Buttons */
        #topDeskBtn {
            background-color: #fffbeb !important;
            color: #b45309 !important;
            border: 1px solid #fcd34d !important;
        }
        #topDeskBtn:hover {
            background-color: #fef3c7 !important;
            color: #92400e !important;
        }
        #topNewToolBtn {
            background-color: #f8fafc !important;
            color: #334155 !important;
            border: 1px solid #cbd5e1 !important;
        }
        #topNewToolBtn:hover {
            background-color: #f1f5f9 !important;
            color: #0f172a !important;
        }'''

if old_tab_rules in text:
    text = text.replace(old_tab_rules, new_tab_rules)
    print("Updated tab rules in index.html style successfully!")
else:
    print("old_tab_rules not found")

# In HTML static markup for #omniTabHome in index.html:
text = text.replace(
    'class="flex items-center gap-2 px-3.5 h-[34px] bg-[#1E293B] text-white font-semibold border-t-2 border-blue-600 shrink-0 text-[12px] border-r border-slate-700"',
    'class="flex items-center gap-2 px-3.5 h-[34px] bg-white text-[#0F172A] font-bold border-t-2 border-blue-600 shrink-0 text-[12px] border-r border-slate-200 shadow-xs"'
)
text = text.replace(
    '<svg class="w-3.5 h-3.5 text-white shrink-0"',
    '<svg class="w-3.5 h-3.5 text-blue-600 shrink-0"'
)

# DESK button in index.html
text = text.replace(
    'class="px-3 h-[28px] bg-amber-500/10 hover:bg-amber-500/20 text-amber-300 hover:text-white text-xs font-semibold transition border border-amber-500/30 flex items-center gap-1.5 cursor-pointer"',
    'class="px-3 h-[28px] bg-amber-50 hover:bg-amber-100 text-amber-900 text-xs font-semibold transition border border-amber-300 flex items-center gap-1.5 cursor-pointer"'
)
text = text.replace(
    '<svg class="w-3.5 h-3.5 text-amber-400 shrink-0"',
    '<svg class="w-3.5 h-3.5 text-amber-600 shrink-0"'
)

# Nuovo Tool button in index.html
text = text.replace(
    'class="px-3 h-[28px] bg-slate-800 hover:bg-slate-700 text-slate-200 hover:text-white text-xs font-medium transition flex items-center gap-1.5 border border-slate-700 cursor-pointer"',
    'class="px-3 h-[28px] bg-slate-100 hover:bg-slate-200 text-slate-700 hover:text-slate-900 text-xs font-medium transition flex items-center gap-1.5 border border-slate-300 cursor-pointer"'
)
text = text.replace(
    '<svg class="w-3.5 h-3.5 text-slate-300 shrink-0"',
    '<svg class="w-3.5 h-3.5 text-slate-600 shrink-0"'
)

with open('Calcolatore_Pendenza/index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("index.html fully patched!")
