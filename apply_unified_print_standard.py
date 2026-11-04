#!/usr/bin/env python3
import re
import subprocess

print("=== STARTING UNIFIED PRINT STANDARD IMPLEMENTATION ===")

svg_logo_snippet = '''<div class="w-10 h-10 rounded-xl bg-gradient-to-br from-blue-600 to-indigo-700 flex items-center justify-center text-white shrink-0 p-1 shadow-sm" style="-webkit-print-color-adjust: exact; print-color-adjust: exact;">
                    <svg class="w-full h-full" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <circle cx="16" cy="16" r="13.2" stroke="#ffffff" stroke-width="3.4" />
                        <path d="M 7.5 11.5 H 24.5 M 16 11.5 V 24.5" stroke="#ffffff" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round" />
                        <circle cx="16" cy="11.5" r="2.1" fill="#38bdf8" />
                    </svg>
                </div>'''

unified_footer_snippet = '''                <!-- DEDICATED PRINT-ONLY TECHNICAL NOTES & SIGNATURE BOX -->
                <div id="printFooterBox" class="hidden print:block mt-3 pt-2.5 border-t border-slate-300 text-xs">
                    <div class="grid grid-cols-2 gap-4">
                        <div>
                            <span class="font-bold text-slate-800 block mb-1 text-[9px] uppercase tracking-wider">Note di Cantiere / Prescrizioni Tecniche:</span>
                            <div class="border border-dashed border-slate-400 h-14 rounded-lg p-1.5 text-[8.5px] text-slate-600 leading-tight">
                                • Verificare quote effettive e tolleranze esecutive in loco prima della posa.<br>
                                • Il presente elaborato riassume i parametri di calcolo e le verifiche normative di progetto.
                            </div>
                        </div>
                        <div>
                            <span class="font-bold text-slate-800 block mb-1 text-[9px] uppercase tracking-wider">Timbro e Firma del Tecnico / Progettista:</span>
                            <div class="border border-slate-300 h-14 rounded-lg flex items-end justify-center pb-1 text-[8.5px] text-slate-400">
                                Data, Timbro e Firma Professionale
                            </div>
                        </div>
                    </div>
                    <div class="text-[8px] text-slate-400 text-center mt-2 pt-1 border-t border-slate-200">
                        Documento tecnico generato da <strong>OmniTools Lab</strong> (https://www.omnitoolslab.com) — Precision Utilities Suite.
                    </div>
                </div>'''

# -------------------------------------------------------------
# 1. REFACTOR build_rampe_i18n.py
# -------------------------------------------------------------
with open('/Users/ilalu/Documents/Altenative Businnes/Calcolatore_Pendenza/build_rampe_i18n.py', 'r', encoding='utf-8') as f:
    rampe_code = f.read()

# Unified @page and @media print
old_page_rampe = re.search(r'@page\s*\{\{.*?\}\}\s*@media print\s*\{\{.*?\}\}', rampe_code, re.DOTALL)
if old_page_rampe:
    new_page_rampe = '''@page {{
            size: A4 portrait;
            margin: 8mm 10mm 8mm 10mm;
        }}
        @media print {{
            header, footer, nav,
            .no-print,
            #faqSection, #faqContainer, #normSection, #shareStrip,
            #suggestModal, #installBanner, #iosModal, #suggestBanner,
            #heroContainer, #modeSelectorBar, #controlsColumn,
            button, input[type=range], details, .faq-accordion {{ 
                display: none !important; 
            }}
            body {{ 
                background: white !important; 
                color: #0f172a !important; 
                padding: 0 !important; 
                margin: 0 !important;
                font-size: 10pt !important; 
                line-height: 1.25 !important;
                -webkit-print-color-adjust: exact !important;
                print-color-adjust: exact !important;
            }}
            main {{ 
                max-width: 100% !important; 
                margin: 0 !important; 
                padding: 0 !important; 
            }}
            #resultsColumn {{
                width: 100% !important;
                max-width: 100% !important;
                display: block !important;
                margin: 0 !important;
                padding: 0 !important;
            }}
            .print-border {{ 
                border: 1px solid #cbd5e1 !important; 
                box-shadow: none !important;
            }}
            #rampSvg {{
                max-height: 160px !important;
            }}
        }}'''
    rampe_code = rampe_code[:old_page_rampe.start()] + new_page_rampe + rampe_code[old_page_rampe.end():]

# Unified print header with SVG logo
old_header_rampe = re.search(r'<div id=\"printHeader\".*?</div>\s*</div>\s*</div>', rampe_code, re.DOTALL)
if old_header_rampe:
    new_header_rampe = f'''<div id="printHeader" class="hidden print:block mb-3 pb-2 border-b-2 border-slate-900">
                    <div class="flex items-center justify-between">
                        <div class="flex items-center gap-2.5">
                            {svg_logo_snippet}
                            <div>
                                <div class="flex items-center gap-1.5 leading-none">
                                    <span class="text-base font-black tracking-tight text-slate-900 font-jakarta">Omni<span class="text-blue-600">Tools</span> Lab</span>
                                    <span class="text-[9px] font-extrabold uppercase bg-slate-100 text-slate-800 px-1.5 py-0.5 rounded border border-slate-300">SCHEDA TECNICA A4</span>
                                </div>
                                <h1 class="text-xs font-bold text-slate-700 mt-1">RampaFacile — Verifica Conformità Pendenza Rampa & Barriere Architettoniche</h1>
                            </div>
                        </div>
                        <div class="text-right text-[10px] text-slate-600 font-mono leading-tight">
                            <div id="printReportDate" class="font-bold text-slate-900">Data: 04/11/2026</div>
                            <div>DM 236/89 • ADA • CTE • DIN</div>
                            <div class="text-blue-600 font-bold">omnitoolslab.com/rampe</div>
                        </div>
                    </div>
                </div>'''
    rampe_code = rampe_code[:old_header_rampe.start()] + new_header_rampe + rampe_code[old_header_rampe.end():]

with open('/Users/ilalu/Documents/Altenative Businnes/Calcolatore_Pendenza/build_rampe_i18n.py', 'w', encoding='utf-8') as f:
    f.write(rampe_code)
print("build_rampe_i18n.py updated with unified print standard.")


# -------------------------------------------------------------
# 2. REFACTOR build_scale_i18n.py
# -------------------------------------------------------------
with open('/Users/ilalu/Documents/Altenative Businnes/Calcolatore_Pendenza/build_scale_i18n.py', 'r', encoding='utf-8') as f:
    scale_code = f.read()

old_page_scale = re.search(r'@page\s*\{\{.*?\}\}\s*@media print\s*\{\{.*?\}\}', scale_code, re.DOTALL)
if old_page_scale:
    new_page_scale = '''@page {{
            size: A4 portrait;
            margin: 8mm 10mm 8mm 10mm;
        }}
        @media print {{
            header, footer, nav,
            .no-print,
            #faqSection, #faqContainer, #normSection, #shareStrip,
            #suggestModal, #installBanner, #iosModal, #suggestBanner,
            #heroContainer, #modeSelectorBar, #controlsColumn,
            button, input[type=range], details, .faq-accordion {{ 
                display: none !important; 
            }}
            body {{ 
                background: white !important; 
                color: #0f172a !important; 
                padding: 0 !important; 
                margin: 0 !important;
                font-size: 10pt !important; 
                line-height: 1.25 !important;
                -webkit-print-color-adjust: exact !important;
                print-color-adjust: exact !important;
            }}
            main {{ 
                max-width: 100% !important; 
                margin: 0 !important; 
                padding: 0 !important; 
            }}
            #resultsColumn {{
                width: 100% !important;
                max-width: 100% !important;
                display: block !important;
                margin: 0 !important;
                padding: 0 !important;
            }}
            .print-border {{ 
                border: 1px solid #cbd5e1 !important; 
                box-shadow: none !important;
            }}
            #stairSvg {{
                max-height: 160px !important;
            }}
        }}'''
    scale_code = scale_code[:old_page_scale.start()] + new_page_scale + scale_code[old_page_scale.end():]

old_header_scale = re.search(r'<div id=\"printHeader\".*?</div>\s*</div>\s*</div>', scale_code, re.DOTALL)
if old_header_scale:
    new_header_scale = f'''<div id="printHeader" class="hidden print:block mb-3 pb-2 border-b-2 border-slate-900">
                    <div class="flex items-center justify-between">
                        <div class="flex items-center gap-2.5">
                            {svg_logo_snippet}
                            <div>
                                <div class="flex items-center gap-1.5 leading-none">
                                    <span class="text-base font-black tracking-tight text-slate-900 font-jakarta">Omni<span class="text-blue-600">Tools</span> Lab</span>
                                    <span class="text-[9px] font-extrabold uppercase bg-slate-100 text-slate-800 px-1.5 py-0.5 rounded border border-slate-300">SCHEDA TECNICA A4</span>
                                </div>
                                <h1 class="text-xs font-bold text-slate-700 mt-1">ScalaFacile — Relazione Tecnica Dimensionamento Gradini & Formula di Blondel</h1>
                            </div>
                        </div>
                        <div class="text-right text-[10px] text-slate-600 font-mono leading-tight">
                            <div id="printReportDate" class="font-bold text-slate-900">Data: 04/11/2026</div>
                            <div>Blondel 2a+p=63 • DIN 18065</div>
                            <div class="text-blue-600 font-bold">omnitoolslab.com/scale</div>
                        </div>
                    </div>
                </div>'''
    scale_code = scale_code[:old_header_scale.start()] + new_header_scale + scale_code[old_header_scale.end():]

with open('/Users/ilalu/Documents/Altenative Businnes/Calcolatore_Pendenza/build_scale_i18n.py', 'w', encoding='utf-8') as f:
    f.write(scale_code)
print("build_scale_i18n.py updated with unified print standard.")


# -------------------------------------------------------------
# 3. REFACTOR build_tubi_i18n.py
# -------------------------------------------------------------
with open('/Users/ilalu/Documents/Altenative Businnes/Calcolatore_Pendenza/build_tubi_i18n.py', 'r', encoding='utf-8') as f:
    tubi_code = f.read()

# Add @page and update print CSS
old_style_tubi = re.search(r'<style>.*?</style>', tubi_code, re.DOTALL)
if old_style_tubi:
    new_style_tubi = '''<style>
        @page {
            size: A4 portrait;
            margin: 8mm 10mm 8mm 10mm;
        }
        @media print {
            header, footer, nav,
            .no-print,
            #faqSection, #normSection, #shareStrip,
            #presetsSection, #calcTabs, #langSelect, button, input[type=range],
            details, .faq-accordion {
                display: none !important;
            }
            body {
                background-color: #ffffff !important;
                color: #0f172a !important;
                font-size: 10pt !important;
                line-height: 1.25 !important;
                padding: 0 !important;
                margin: 0 !important;
                -webkit-print-color-adjust: exact !important;
                print-color-adjust: exact !important;
            }
            main {
                max-width: 100% !important;
                margin: 0 !important;
                padding: 0 !important;
                width: 100% !important;
            }
            .print-only {
                display: block !important;
            }
            .shadow-sm, .shadow-md, .shadow-lg, .shadow-2xs {
                box-shadow: none !important;
            }
            .border {
                border-color: #cbd5e1 !important;
            }
            .bg-slate-900 {
                background-color: #ffffff !important;
                border: 1px solid #cbd5e1 !important;
            }
            #pipeSvg {
                max-height: 150px !important;
            }
        }
        .print-only {
            display: none;
        }
    </style>'''
    tubi_code = tubi_code[:old_style_tubi.start()] + new_style_tubi + tubi_code[old_style_tubi.end():]

# Replace old print header in tubi
old_header_tubi = re.search(r'<!-- Print-only Header -->.*?<!-- Hero Section -->', tubi_code, re.DOTALL)
if old_header_tubi:
    new_header_tubi = f'''<!-- UNIFIED A4 PRINT HEADER -->
        <div class="print-only mb-3 pb-2 border-b-2 border-slate-900">
            <div class="flex items-center justify-between">
                <div class="flex items-center gap-2.5">
                    {svg_logo_snippet}
                    <div>
                        <div class="flex items-center gap-1.5 leading-none">
                            <span class="text-base font-black tracking-tight text-slate-900 font-jakarta">Omni<span class="text-blue-600">Tools</span> Lab</span>
                            <span class="text-[9px] font-extrabold uppercase bg-slate-100 text-slate-800 px-1.5 py-0.5 rounded border border-slate-300">SCHEDA TECNICA A4</span>
                        </div>
                        <h1 class="text-xs font-bold text-slate-700 mt-1">ScaricoFacile — Relazione Idraulica Pendenza Tubazioni & Verifica Autopulizia</h1>
                    </div>
                </div>
                <div class="text-right text-[10px] text-slate-600 font-mono leading-tight">
                    <div id="printReportDate" class="font-bold text-slate-900">Data: 04/11/2026</div>
                    <div>UNI EN 12056 • UNI EN 752</div>
                    <div class="text-blue-600 font-bold">omnitoolslab.com/tubi</div>
                </div>
            </div>
        </div>

        <!-- DEDICATED PRINT-ONLY INPUT SUMMARY -->
        <div id="printInputsSummary" class="hidden print:block mb-2 p-2.5 bg-slate-50 border border-slate-300 rounded-xl text-xs">
            <div class="grid grid-cols-3 gap-2">
                <div>
                    <span class="text-[9px] text-slate-500 uppercase font-bold block">Lunghezza Tratta (L):</span>
                    <span id="printLengthVal" class="text-xs font-extrabold text-slate-900">4.0 m</span>
                </div>
                <div>
                    <span class="text-[9px] text-slate-500 uppercase font-bold block">Diametro Nominale:</span>
                    <span id="printDiamVal" class="text-xs font-extrabold text-slate-900">Ø 110 mm</span>
                </div>
                <div>
                    <span class="text-[9px] text-slate-500 uppercase font-bold block">Criterio Normativo:</span>
                    <span class="text-xs font-extrabold text-slate-900">Autopulizia (v ≥ 0.7 m/s)</span>
                </div>
            </div>
        </div>

        <!-- Hero Section -->'''
    tubi_code = tubi_code[:old_header_tubi.start()] + new_header_tubi + tubi_code[old_header_tubi.end():]

# Add no-print to normative guide section in tubi
tubi_code = tubi_code.replace(
    '<!-- Technical Normative Guide & Reference Table -->\n        <section class="bg-white rounded-3xl',
    '<!-- Technical Normative Guide & Reference Table -->\n        <section id="normSection" class="no-print bg-white rounded-3xl'
)

# Add no-print to FAQ section in tubi
tubi_code = tubi_code.replace(
    '<!-- FAQ Accordion Section -->\n        <section class="bg-white rounded-3xl',
    '<!-- FAQ Accordion Section -->\n        <section id="faqSection" class="no-print bg-white rounded-3xl'
)

# Add print footer in tubi before main closing
if 'printFooterBox' not in tubi_code:
    tubi_code = tubi_code.replace(
        '<!-- Action Buttons: Print & Copy -->',
        f'{unified_footer_snippet}\n\n            <!-- Action Buttons: Print & Copy -->'
    )

with open('/Users/ilalu/Documents/Altenative Businnes/Calcolatore_Pendenza/build_tubi_i18n.py', 'w', encoding='utf-8') as f:
    f.write(tubi_code)
print("build_tubi_i18n.py updated with unified print standard.")


# -------------------------------------------------------------
# 4. REFACTOR build_dorso_i18n.py
# -------------------------------------------------------------
with open('/Users/ilalu/Documents/Altenative Businnes/Calcolatore_Pendenza/build_dorso_i18n.py', 'r', encoding='utf-8') as f:
    dorso_code = f.read()

# Switch from landscape to A4 portrait
old_page_dorso = re.search(r'@page\s*\{\{.*?\}\}\s*@media print\s*\{\{.*?\}\}', dorso_code, re.DOTALL)
if old_page_dorso:
    new_page_dorso = '''@page {{
            size: A4 portrait;
            margin: 8mm 10mm 8mm 10mm;
        }}
        @media print {{
            header, footer, nav,
            .no-print,
            #faqSection, #faqContainer, #normSection, #shareStrip,
            #suggestModal, #installBanner, #iosModal, #suggestBanner,
            #heroContainer, #modeSelectorBar, #controlsColumn,
            button, input[type=range], details, .faq-accordion {{ 
                display: none !important; 
            }}
            body {{ 
                background: white !important; 
                color: #0f172a !important; 
                padding: 0 !important; 
                margin: 0 !important;
                font-size: 10pt !important; 
                line-height: 1.25 !important;
                -webkit-print-color-adjust: exact !important;
                print-color-adjust: exact !important;
            }}
            main {{ 
                max-width: 100% !important; 
                margin: 0 !important; 
                padding: 0 !important; 
            }}
            #resultsColumn {{
                width: 100% !important;
                max-width: 100% !important;
                display: block !important;
                margin: 0 !important;
                padding: 0 !important;
            }}
            .print-border {{ 
                border: 1px solid #cbd5e1 !important; 
                box-shadow: none !important;
            }}
            #blueprintSvg {{
                max-height: 160px !important;
            }}
        }}'''
    dorso_code = dorso_code[:old_page_dorso.start()] + new_page_dorso + dorso_code[old_page_dorso.end():]

old_header_dorso = re.search(r'<div id=\"printHeader\".*?</div>\s*</div>\s*</div>', dorso_code, re.DOTALL)
if old_header_dorso:
    new_header_dorso = f'''<div id="printHeader" class="hidden print:block mb-3 pb-2 border-b-2 border-slate-900">
                    <div class="flex items-center justify-between">
                        <div class="flex items-center gap-2.5">
                            {svg_logo_snippet}
                            <div>
                                <div class="flex items-center gap-1.5 leading-none">
                                    <span class="text-base font-black tracking-tight text-slate-900 font-jakarta">Omni<span class="text-blue-600">Tools</span> Lab</span>
                                    <span class="text-[9px] font-extrabold uppercase bg-slate-100 text-slate-800 px-1.5 py-0.5 rounded border border-slate-300">SCHEDA TECNICA A4</span>
                                </div>
                                <h1 class="text-xs font-bold text-slate-700 mt-1">DorsoFacile — Scheda Tecnica Prestampa Fustella & Copertina Stesa</h1>
                            </div>
                        </div>
                        <div class="text-right text-[10px] text-slate-600 font-mono leading-tight">
                            <div id="printReportDate" class="font-bold text-slate-900">Data: 04/11/2026</div>
                            <div>Refilo 3 mm • Brossura PUR</div>
                            <div class="text-blue-600 font-bold">omnitoolslab.com/dorso</div>
                        </div>
                    </div>
                </div>'''
    dorso_code = dorso_code[:old_header_dorso.start()] + new_header_dorso + dorso_code[old_header_dorso.end():]

with open('/Users/ilalu/Documents/Altenative Businnes/Calcolatore_Pendenza/build_dorso_i18n.py', 'w', encoding='utf-8') as f:
    f.write(dorso_code)
print("build_dorso_i18n.py updated with unified print standard.")


# -------------------------------------------------------------
# 5. REFACTOR build_dpi_i18n.py
# -------------------------------------------------------------
with open('/Users/ilalu/Documents/Altenative Businnes/Calcolatore_Pendenza/build_dpi_i18n.py', 'r', encoding='utf-8') as f:
    dpi_code = f.read()

old_page_dpi = re.search(r'@page\s*\{\{.*?\}\}\s*@media print\s*\{\{.*?\}\}', dpi_code, re.DOTALL)
if old_page_dpi:
    new_page_dpi = '''@page {{
            size: A4 portrait;
            margin: 8mm 10mm 8mm 10mm;
        }}
        @media print {{
            header, footer, nav,
            .no-print,
            #faqSection, #faqContainer, #normSection, #shareStrip,
            #suggestModal, #installBanner, #iosModal, #suggestBanner,
            #heroContainer, #modeSelectorBar, #controlsColumn,
            button, input[type=range], details, .faq-accordion {{ 
                display: none !important; 
            }}
            body {{ 
                background: white !important; 
                color: #0f172a !important; 
                padding: 0 !important; 
                margin: 0 !important;
                font-size: 10pt !important; 
                line-height: 1.25 !important;
                -webkit-print-color-adjust: exact !important;
                print-color-adjust: exact !important;
            }}
            main {{ 
                max-width: 100% !important; 
                margin: 0 !important; 
                padding: 0 !important; 
            }}
            #resultsColumn {{
                width: 100% !important;
                max-width: 100% !important;
                display: block !important;
                margin: 0 !important;
                padding: 0 !important;
            }}
            .print-border {{ 
                border: 1px solid #cbd5e1 !important; 
                box-shadow: none !important;
            }}
        }}'''
    dpi_code = dpi_code[:old_page_dpi.start()] + new_page_dpi + dpi_code[old_page_dpi.end():]

old_header_dpi = re.search(r'<div id=\"printHeader\".*?</div>\s*</div>\s*</div>', dpi_code, re.DOTALL)
if old_header_dpi:
    new_header_dpi = f'''<div id="printHeader" class="hidden print:block mb-3 pb-2 border-b-2 border-slate-900">
                    <div class="flex items-center justify-between">
                        <div class="flex items-center gap-2.5">
                            {svg_logo_snippet}
                            <div>
                                <div class="flex items-center gap-1.5 leading-none">
                                    <span class="text-base font-black tracking-tight text-slate-900 font-jakarta">Omni<span class="text-blue-600">Tools</span> Lab</span>
                                    <span class="text-[9px] font-extrabold uppercase bg-slate-100 text-slate-800 px-1.5 py-0.5 rounded border border-slate-300">SCHEDA TECNICA A4</span>
                                </div>
                                <h1 class="text-xs font-bold text-slate-700 mt-1">RisoluzioneFacile — Scheda Tecnica di Risoluzione Stampa, Megapixel & DPI</h1>
                            </div>
                        </div>
                        <div class="text-right text-[10px] text-slate-600 font-mono leading-tight">
                            <div id="printReportDate" class="font-bold text-slate-900">Data: 04/11/2026</div>
                            <div>Offset • Digitale • Acuità Visiva</div>
                            <div class="text-blue-600 font-bold">omnitoolslab.com/dpi</div>
                        </div>
                    </div>
                </div>'''
    dpi_code = dpi_code[:old_header_dpi.start()] + new_header_dpi + dpi_code[old_header_dpi.end():]

with open('/Users/ilalu/Documents/Altenative Businnes/Calcolatore_Pendenza/build_dpi_i18n.py', 'w', encoding='utf-8') as f:
    f.write(dpi_code)
print("build_dpi_i18n.py updated with unified print standard.")

# -------------------------------------------------------------
# 6. RECOMPILE ALL 5 FILES
# -------------------------------------------------------------
scripts = ['build_rampe_i18n.py', 'build_scale_i18n.py', 'build_tubi_i18n.py', 'build_dorso_i18n.py', 'build_dpi_i18n.py']
for s in scripts:
    print(f"Recompiling {s}...")
    subprocess.run(["python3", f"/Users/ilalu/Documents/Altenative Businnes/Calcolatore_Pendenza/{s}"], check=True)

print("=== ALL 5 TOOLS RECOMPILED WITH UNIFIED PRINT STANDARD ===")
