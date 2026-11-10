import json
import sys
import os

from nav_header import render_suite_header, render_suite_header_js
from unified_footer import render_unified_footer, render_unified_footer_js

cur_dir = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(cur_dir, "translations_piastrelle.json")
with open(json_path, "r", encoding="utf-8") as f:
    t_data = json.load(f)

t_json_str = json.dumps(t_data, ensure_ascii=False)

header_html = render_suite_header("piastrelle")
header_js = render_suite_header_js()
footer_html = render_unified_footer("piastrelle")
footer_js = render_unified_footer_js()

html_code = f"""<!DOCTYPE html>
<html lang="it">
<head>
    <meta name="google-site-verification" content="MRdbDm9lLhokeD3I0FOpUSOhNaF_2WaveKvu52FxtG4">
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0">
    <title>Calcolo Piastrelle, Sfrido, Sacchi Colla e Fughe Online | PiastrellaFacile</title>
    <meta name="description" content="Calcolatore professionale per pavimenti e rivestimenti. Calcola metri quadri da ordinare con percentuale di sfrido per tagli, numero di scatole, sacchi di colla (kg) e stucco per fughe con distinta materiali immediata.">
    
    <!-- Canonical & SEO Meta Tags -->
    <link rel="canonical" href="https://www.omnitoolslab.com/piastrelle">
    <meta name="robots" content="index, follow">
    <meta property="og:type" content="website">
    <meta property="og:title" content="PiastrellaFacile — Calcolo Piastrelle, Sfrido, Colla & Fughe">
    <meta property="og:description" content="Calcola con precisione mq da acquistare, scatole piastrelle, sacchi di colla da 25 kg e stucco fughe.">
    <meta property="og:url" content="https://www.omnitoolslab.com/piastrelle">
    <meta property="og:site_name" content="OmniTools Lab">
    <meta property="og:image" content="https://www.omnitoolslab.com/og-building.png">
    <meta property="og:image:width" content="1200">
    <meta property="og:image:height" content="630">
    <meta name="twitter:card" content="summary_large_image">

    <!-- Favicon & PWA -->
    <link rel="icon" type="image/svg+xml" href="/favicon.svg">
    <link rel="alternate icon" href="/favicon.png">
    <link rel="manifest" href="/manifest-building.json">
    <meta name="theme-color" content="#d97706">

    <!-- Fonts & Tailwind CSS CDN -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;700&display=swap" rel="stylesheet">
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {{
            theme: {{
                extend: {{
                    fontFamily: {{
                        sans: ['Plus Jakarta Sans', 'system-ui', 'sans-serif'],
                        mono: ['JetBrains Mono', 'monospace'],
                        jakarta: ['Plus Jakarta Sans', 'sans-serif'],
                    }}
                }}
            }}
        }}
    </script>
    
    <!-- Unified OmniDesk Floating Dock -->
    <script src="/desk_dock.js" defer></script>

    <style>
        /* Modern subtle scrollbar */
        ::-webkit-scrollbar {{ width: 6px; height: 6px; }}
        ::-webkit-scrollbar-track {{ background: #f1f5f9; }}
        ::-webkit-scrollbar-thumb {{ background: #cbd5e1; border-radius: 9999px; }}
        ::-webkit-scrollbar-thumb:hover {{ background: #94a3b8; }}

        /* Print Strict A4 1-Page Optimization */
        @media print {{
            @page {{
                size: A4 portrait;
                margin: 6mm 8mm;
            }}
            body {{
                background: #ffffff !important;
                color: #000000 !important;
                font-size: 8.5pt !important;
                line-height: 1.15 !important;
                padding: 0 !important;
            }}
            .no-print, header, footer, nav, #faqSection, #shareStrip, #suggestModal, #installBanner {{
                display: none !important;
            }}
            .print-only {{
                display: block !important;
            }}
            .print-container {{
                box-shadow: none !important;
                border: 1px solid #cbd5e1 !important;
                padding: 10px !important;
                margin: 0 !important;
                max-width: 100% !important;
                page-break-inside: avoid !important;
            }}
        }}
    </style>
</head>
<body class="bg-slate-50 text-slate-900 min-h-screen flex flex-col antialiased selection:bg-amber-100 selection:text-amber-900">

    {header_html}

    <!-- MAIN APP CONTAINER -->
    <main class="max-w-5xl mx-auto px-3 sm:px-6 py-2.5 sm:py-5 flex-1 w-full space-y-4 sm:space-y-6">
        
        <!-- Hero Header -->
        <div id="heroContainer" class="text-center max-w-2xl mx-auto pt-1 sm:pt-2">
            <div class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-amber-50 border border-amber-200/80 text-[11px] font-extrabold text-amber-800 tracking-wide uppercase mb-2">
                <span>🧱</span>
                <span id="heroBadge">OmniBuilding · Cantiere & Fai-da-te</span>
            </div>
            <h1 id="heroTitle" class="text-2xl sm:text-4xl font-extrabold text-slate-900 tracking-tight leading-tight mb-1.5 sm:mb-2 font-jakarta">
                Calcolo Piastrelle, Sfrido, Colla & Fughe
            </h1>
            <p id="heroDesc" class="text-slate-600 text-xs sm:text-sm leading-relaxed px-2">
                Calcolatore professionale per pavimenti e rivestimenti. Calcola metri quadri da acquistare con sfrido per tagli, numero di scatole, sacchi di colla (kg) e stucco per fughe con distinta materiali immediata.
            </p>
        </div>

        <!-- 2-COLUMN WORKSPACE: CONTROLS & LIVE BILL OF MATERIALS -->
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-4 sm:gap-6 items-start">
            
            <!-- LEFT COLUMN: INPUT CONTROLS -->
            <div class="lg:col-span-7 space-y-4">
                
                <!-- CARD 1: ROOM SURFACE MEASUREMENTS -->
                <div class="bg-white rounded-3xl p-4 sm:p-5 border border-slate-200/80 shadow-xs space-y-3.5">
                    <div class="flex items-center justify-between pb-2 border-b border-slate-100">
                        <div class="flex items-center gap-2">
                            <span class="w-6 h-6 rounded-lg bg-amber-500 text-white flex items-center justify-center font-bold text-xs">1</span>
                            <h2 id="secRoomTitle" class="text-sm sm:text-base font-extrabold text-slate-900">Misure Superficie da Piastrellare</h2>
                        </div>
                        <!-- Mode Pill Toggle -->
                        <div class="inline-flex p-0.5 rounded-xl bg-slate-100 border border-slate-200/80 text-xs font-bold">
                            <button type="button" id="btnModeDims" onclick="setRoomMode('dims')" class="px-2.5 py-1 rounded-lg bg-white text-slate-800 shadow-2xs transition">L × W</button>
                            <button type="button" id="btnModeDirect" onclick="setRoomMode('direct')" class="px-2.5 py-1 rounded-lg text-slate-500 hover:text-slate-900 transition">m² Netti</button>
                        </div>
                    </div>
                    
                    <p id="secRoomDesc" class="text-xs text-slate-500">Inserisci le dimensioni dell'ambiente o direttamente i metri quadri netti.</p>

                    <!-- Dimensions Input Mode -->
                    <div id="dimsInputGroup" class="grid grid-cols-2 gap-3">
                        <div>
                            <label id="lblLength" class="block text-xs font-bold text-slate-700 mb-1">Lunghezza Stanza (m)</label>
                            <input type="number" id="inputLength" value="5.0" min="0.5" max="100" step="0.05" oninput="calculateAll()" class="w-full bg-slate-50 border border-slate-200 rounded-xl px-3 py-2 text-sm font-bold text-slate-800 focus:bg-white focus:ring-2 focus:ring-amber-500 focus:outline-none transition">
                        </div>
                        <div>
                            <label id="lblWidth" class="block text-xs font-bold text-slate-700 mb-1">Larghezza Stanza (m)</label>
                            <input type="number" id="inputWidth" value="4.0" min="0.5" max="100" step="0.05" oninput="calculateAll()" class="w-full bg-slate-50 border border-slate-200 rounded-xl px-3 py-2 text-sm font-bold text-slate-800 focus:bg-white focus:ring-2 focus:ring-amber-500 focus:outline-none transition">
                        </div>
                    </div>

                    <!-- Direct Area Input Mode (Hidden initially) -->
                    <div id="directInputGroup" class="hidden">
                        <label id="lblNetSqm" class="block text-xs font-bold text-slate-700 mb-1">Superficie Netta (m²)</label>
                        <input type="number" id="inputDirectSqm" value="20.0" min="0.5" max="5000" step="0.1" oninput="calculateAll()" class="w-full bg-slate-50 border border-slate-200 rounded-xl px-3 py-2 text-sm font-bold text-slate-800 focus:bg-white focus:ring-2 focus:ring-amber-500 focus:outline-none transition">
                    </div>

                    <!-- Openings Deduction (Doors / Windows / Pillars) -->
                    <div>
                        <label id="lblOpenings" class="block text-[11px] font-bold text-slate-600 mb-1">Detrazione Porte / Aperture (m² opzionale)</label>
                        <input type="number" id="inputOpenings" value="0" min="0" max="500" step="0.1" oninput="calculateAll()" class="w-full bg-slate-50 border border-slate-200 rounded-xl px-3 py-1.5 text-xs text-slate-700 focus:bg-white focus:ring-2 focus:ring-amber-500 focus:outline-none transition">
                    </div>
                </div>

                <!-- CARD 2: TILE SIZE & PATTERN -->
                <div class="bg-white rounded-3xl p-4 sm:p-5 border border-slate-200/80 shadow-xs space-y-3.5">
                    <div class="flex items-center gap-2 pb-2 border-b border-slate-100">
                        <span class="w-6 h-6 rounded-lg bg-amber-500 text-white flex items-center justify-center font-bold text-xs">2</span>
                        <h2 id="secTileTitle" class="text-sm sm:text-base font-extrabold text-slate-900">Formato Piastrella & Schema di Posa</h2>
                    </div>

                    <p id="secTileDesc" class="text-xs text-slate-500">Scegli la dimensione delle piastrelle e il tipo di posa per calcolare lo sfrido reale.</p>

                    <!-- Presets Pills -->
                    <div>
                        <span id="lblTilePreset" class="block text-xs font-bold text-slate-700 mb-1.5">Formati Comuni</span>
                        <div class="flex flex-wrap gap-1.5">
                            <button type="button" onclick="setTilePreset(60, 60, 9)" class="px-2.5 py-1 rounded-lg bg-slate-100 hover:bg-amber-100 hover:text-amber-900 text-xs font-semibold text-slate-700 border border-slate-200 transition">60 × 60 cm</button>
                            <button type="button" onclick="setTilePreset(30, 60, 9)" class="px-2.5 py-1 rounded-lg bg-slate-100 hover:bg-amber-100 hover:text-amber-900 text-xs font-semibold text-slate-700 border border-slate-200 transition">30 × 60 cm</button>
                            <button type="button" onclick="setTilePreset(80, 80, 10)" class="px-2.5 py-1 rounded-lg bg-slate-100 hover:bg-amber-100 hover:text-amber-900 text-xs font-semibold text-slate-700 border border-slate-200 transition">80 × 80 cm</button>
                            <button type="button" onclick="setTilePreset(20, 120, 10)" class="px-2.5 py-1 rounded-lg bg-slate-100 hover:bg-amber-100 hover:text-amber-900 text-xs font-semibold text-slate-700 border border-slate-200 transition">20 × 120 (Listoni)</button>
                            <button type="button" onclick="setTilePreset(20, 20, 8)" class="px-2.5 py-1 rounded-lg bg-slate-100 hover:bg-amber-100 hover:text-amber-900 text-xs font-semibold text-slate-700 border border-slate-200 transition">20 × 20 cm</button>
                        </div>
                    </div>

                    <!-- Custom Dimensions -->
                    <div class="grid grid-cols-3 gap-2.5">
                        <div>
                            <label id="lblTileW" class="block text-[11px] font-bold text-slate-700 mb-1">Larghezza (cm)</label>
                            <input type="number" id="tileWidth" value="60" min="5" max="300" step="0.5" oninput="calculateAll()" class="w-full bg-slate-50 border border-slate-200 rounded-xl px-2.5 py-1.5 text-xs font-bold text-slate-800 focus:bg-white focus:ring-2 focus:ring-amber-500 focus:outline-none transition">
                        </div>
                        <div>
                            <label id="lblTileH" class="block text-[11px] font-bold text-slate-700 mb-1">Altezza (cm)</label>
                            <input type="number" id="tileHeight" value="60" min="5" max="300" step="0.5" oninput="calculateAll()" class="w-full bg-slate-50 border border-slate-200 rounded-xl px-2.5 py-1.5 text-xs font-bold text-slate-800 focus:bg-white focus:ring-2 focus:ring-amber-500 focus:outline-none transition">
                        </div>
                        <div>
                            <label id="lblTileThick" class="block text-[11px] font-bold text-slate-700 mb-1">Spessore (mm)</label>
                            <input type="number" id="tileThick" value="9" min="3" max="30" step="0.5" oninput="calculateAll()" class="w-full bg-slate-50 border border-slate-200 rounded-xl px-2.5 py-1.5 text-xs font-bold text-slate-800 focus:bg-white focus:ring-2 focus:ring-amber-500 focus:outline-none transition">
                        </div>
                    </div>

                    <!-- Layout Pattern & Waste Margin -->
                    <div>
                        <label id="lblPattern" class="block text-xs font-bold text-slate-700 mb-1">Schema di Posa & Sfrido Tagli</label>
                        <select id="selectPattern" onchange="onPatternChange()" class="w-full bg-slate-50 border border-slate-200 rounded-xl px-3 py-2 text-xs font-bold text-slate-800 focus:bg-white focus:ring-2 focus:ring-amber-500 focus:outline-none transition">
                            <option value="10" selected id="optStraight">Posa Dritta Standard (+10% sfrido)</option>
                            <option value="12" id="optOffset">Posa Sfalsata / A Correre (+12% sfrido)</option>
                            <option value="15" id="optDiagonal">Posa in Diagonale (+15% sfrido)</option>
                            <option value="20" id="optHerringbone">Posa a Spina di Pesce (+20% sfrido)</option>
                            <option value="custom" id="optCustom">Sfrido Personalizzato (%)</option>
                        </select>
                        <div id="customWasteGroup" class="hidden mt-2">
                            <label id="lblCustomWaste" class="block text-[11px] font-bold text-slate-600 mb-1">Percentuale Sfrido (%)</label>
                            <input type="number" id="customWasteInput" value="10" min="0" max="50" step="1" oninput="calculateAll()" class="w-full bg-slate-50 border border-slate-200 rounded-xl px-3 py-1.5 text-xs text-slate-800 focus:bg-white focus:ring-2 focus:ring-amber-500 focus:outline-none transition">
                        </div>
                    </div>

                    <!-- Packaging Info (Boxes) -->
                    <div class="grid grid-cols-2 gap-3 pt-1">
                        <div>
                            <label id="lblBoxCoverage" class="block text-xs font-bold text-slate-700 mb-1">Mq per Scatola (m²)</label>
                            <input type="number" id="boxCoverage" value="1.44" min="0.1" max="20" step="0.01" oninput="calculateAll()" class="w-full bg-slate-50 border border-slate-200 rounded-xl px-3 py-2 text-xs font-bold text-slate-800 focus:bg-white focus:ring-2 focus:ring-amber-500 focus:outline-none transition">
                        </div>
                        <div>
                            <label id="lblBoxPieces" class="block text-xs font-bold text-slate-700 mb-1">Pezzi per Scatola (opzionale)</label>
                            <input type="number" id="boxPieces" value="4" min="1" max="100" step="1" oninput="calculateAll()" class="w-full bg-slate-50 border border-slate-200 rounded-xl px-3 py-2 text-xs font-bold text-slate-800 focus:bg-white focus:ring-2 focus:ring-amber-500 focus:outline-none transition">
                        </div>
                    </div>
                </div>

                <!-- CARD 3: ADHESIVE & GROUT CONSUMPTIONS -->
                <div class="bg-white rounded-3xl p-4 sm:p-5 border border-slate-200/80 shadow-xs space-y-3.5">
                    <div class="flex items-center gap-2 pb-2 border-b border-slate-100">
                        <span class="w-6 h-6 rounded-lg bg-amber-500 text-white flex items-center justify-center font-bold text-xs">3</span>
                        <h2 id="secMaterialsTitle" class="text-sm sm:text-base font-extrabold text-slate-900">Colla (Adesivo) & Stucco per Fughe</h2>
                    </div>

                    <p id="secMaterialsDesc" class="text-xs text-slate-500">Stima precisa dei consumi di cantiere in base al sottofondo e alla fuga.</p>

                    <!-- Grout Width & Adhesive Notch Selection -->
                    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
                        <div>
                            <label id="lblGroutWidth" class="block text-xs font-bold text-slate-700 mb-1">Larghezza Fuga (mm)</label>
                            <input type="number" id="groutWidth" value="2.0" min="0.5" max="20" step="0.5" oninput="calculateAll()" class="w-full bg-slate-50 border border-slate-200 rounded-xl px-3 py-2 text-xs font-bold text-slate-800 focus:bg-white focus:ring-2 focus:ring-amber-500 focus:outline-none transition">
                        </div>
                        <div>
                            <label id="lblBagWeight" class="block text-xs font-bold text-slate-700 mb-1">Peso Sacco Colla (kg)</label>
                            <input type="number" id="bagWeight" value="25" min="5" max="50" step="5" oninput="calculateAll()" class="w-full bg-slate-50 border border-slate-200 rounded-xl px-3 py-2 text-xs font-bold text-slate-800 focus:bg-white focus:ring-2 focus:ring-amber-500 focus:outline-none transition">
                        </div>
                    </div>

                    <div>
                        <label id="lblAdhesiveNotch" class="block text-xs font-bold text-slate-700 mb-1">Tipo Spatola / Applicazione Colla</label>
                        <select id="selectAdhesive" onchange="calculateAll()" class="w-full bg-slate-50 border border-slate-200 rounded-xl px-3 py-2 text-xs font-bold text-slate-800 focus:bg-white focus:ring-2 focus:ring-amber-500 focus:outline-none transition">
                            <option value="3.0" id="notchSmall">Dente 6 mm (Piccoli formati, ~3.0 kg/m²)</option>
                            <option value="4.5" selected id="notchMedium">Dente 8-10 mm (Standard 30x60 / 60x60, ~4.5 kg/m²)</option>
                            <option value="6.0" id="notchLarge">Doppia Spalmatura (Grandi Lastre / Esterni, ~6.0 kg/m²)</option>
                        </select>
                    </div>
                </div>

            </div>

            <!-- RIGHT COLUMN: BILL OF MATERIALS & GRAPHICAL PREVIEW -->
            <div class="lg:col-span-5 space-y-4">
                
                <!-- SUMMARY COMPILATION CARD -->
                <div class="bg-white rounded-3xl p-5 border-2 border-amber-500/30 shadow-lg shadow-amber-500/5 space-y-4 print-container">
                    
                    <div class="flex items-center justify-between pb-3 border-b border-slate-100">
                        <div>
                            <span class="text-[10px] font-extrabold uppercase px-2 py-0.5 rounded-full bg-amber-100 text-amber-900 border border-amber-300">Distinta Materiali</span>
                            <h2 id="summaryTitle" class="text-base sm:text-lg font-black text-slate-900 mt-1">Computo per l'Acquisto</h2>
                        </div>
                        <div class="w-10 h-10 rounded-xl bg-amber-500 text-white flex items-center justify-center text-lg shadow-sm">
                            🛒
                        </div>
                    </div>

                    <!-- Metrics Grid -->
                    <div class="space-y-3">
                        
                        <!-- Net vs Gross Area -->
                        <div class="grid grid-cols-2 gap-2 p-3 rounded-2xl bg-slate-50 border border-slate-200/80">
                            <div>
                                <span id="resNetAreaLabel" class="text-[11px] font-bold text-slate-500 block">Superficie Netta</span>
                                <span id="valNetArea" class="text-base font-extrabold font-mono text-slate-800">20.00 m²</span>
                            </div>
                            <div>
                                <span id="resGrossAreaLabel" class="text-[11px] font-extrabold text-amber-800 block">Totale con Sfrido</span>
                                <span id="valGrossArea" class="text-lg font-black font-mono text-amber-600">22.00 m²</span>
                            </div>
                        </div>

                        <!-- Boxes & Tiles Count -->
                        <div class="p-3.5 rounded-2xl bg-amber-50/60 border border-amber-200">
                            <div class="flex items-baseline justify-between">
                                <span id="resBoxesLabel" class="text-xs font-bold text-amber-900">Scatole da Acquistare</span>
                                <span id="valBoxes" class="text-2xl font-black font-mono text-amber-700">16 Scatole</span>
                            </div>
                            <div class="flex items-center justify-between text-[11px] text-amber-800/80 mt-1 pt-1 border-t border-amber-200/60">
                                <span id="valTotalSqmMade">Copertura effettiva: 23.04 m²</span>
                                <span id="valTotalTiles">Totale pezzi: ~64</span>
                            </div>
                        </div>

                        <!-- Adhesive Mortar & Grout -->
                        <div class="grid grid-cols-2 gap-2">
                            <!-- Adhesive -->
                            <div class="p-3 rounded-2xl bg-slate-50 border border-slate-200/80">
                                <span id="resAdhesiveBagsLabel" class="text-[11px] font-bold text-slate-600 block">Sacchi Colla (25kg)</span>
                                <span id="valAdhesiveBags" class="text-xl font-black font-mono text-slate-900 mt-0.5 block">4 Sacchi</span>
                                <span id="valAdhesiveKg" class="text-[10px] font-mono text-slate-500 mt-0.5 block">Totale: ~99 kg</span>
                            </div>

                            <!-- Grout -->
                            <div class="p-3 rounded-2xl bg-slate-50 border border-slate-200/80">
                                <span id="resGroutKgLabel" class="text-[11px] font-bold text-slate-600 block">Stucco per Fughe</span>
                                <span id="valGroutKg" class="text-xl font-black font-mono text-slate-900 mt-0.5 block">1.5 kg</span>
                                <span id="valGroutDetails" class="text-[10px] font-mono text-slate-500 mt-0.5 block">Fuga 2mm · 9mm spess.</span>
                            </div>
                        </div>

                    </div>

                    <!-- Contingency / Warning Note -->
                    <div class="flex items-start gap-2 p-2.5 rounded-xl bg-amber-50/50 border border-amber-200 text-[11px] text-amber-800">
                        <span class="text-base shrink-0">⚠️</span>
                        <p id="resWasteWarning" class="leading-relaxed">
                            Include riserva per tagli perimetrali e sfridi di cantiere. Conserva sempre almeno 1 scatola integra per future riparazioni.
                        </p>
                    </div>

                    <!-- Action Buttons -->
                    <div class="pt-2 flex flex-col sm:flex-row gap-2 no-print">
                        <button type="button" onclick="copyMaterialsList()" class="flex-1 py-2.5 px-3 rounded-xl bg-slate-900 hover:bg-slate-800 text-white font-extrabold text-xs shadow-md transition active:scale-95 flex items-center justify-center gap-1.5 cursor-pointer">
                            <span>📋</span>
                            <span id="btnCopyList">Copia Lista Spesa</span>
                        </button>
                        <button type="button" onclick="window.print()" class="py-2.5 px-4 rounded-xl bg-amber-500 hover:bg-amber-600 text-white font-extrabold text-xs shadow-md shadow-amber-500/20 transition active:scale-95 flex items-center justify-center gap-1.5 cursor-pointer">
                            <span>🖨️</span>
                            <span id="btnPrint">Stampa Scheda A4</span>
                        </button>
                    </div>

                    <div id="copyToast" class="hidden text-center text-xs font-bold text-emerald-600 py-1 transition-all">
                        ✓ Distinta copiata negli appunti!
                    </div>

                    <!-- Print-Only Box for Technician Signature -->
                    <div class="print-only hidden pt-6 border-t border-slate-300 mt-4 text-[10px] text-slate-600">
                        <div class="grid grid-cols-2 gap-4">
                            <div>
                                <p class="font-bold">Cliente / Committente:</p>
                                <p class="border-b border-slate-300 h-6 mt-1"></p>
                            </div>
                            <div>
                                <p class="font-bold">Firma & Timbro Tecnico / Posatore:</p>
                                <p class="border-b border-slate-300 h-6 mt-1"></p>
                            </div>
                        </div>
                    </div>

                </div>

                <!-- DYNAMIC PATTERN VISUAL PREVIEW CARD -->
                <div class="bg-white rounded-3xl p-4 sm:p-5 border border-slate-200/80 shadow-xs space-y-3 no-print">
                    <div class="flex items-center justify-between">
                        <h3 id="previewTitle" class="text-xs sm:text-sm font-extrabold text-slate-800">Anteprima Grafica Schema di Posa</h3>
                        <span id="previewPatternBadge" class="text-[10px] font-bold text-amber-700 bg-amber-50 px-2 py-0.5 rounded-md border border-amber-200">Dritta (+10%)</span>
                    </div>

                    <!-- SVG Grid Canvas -->
                    <div class="w-full h-40 bg-slate-100 rounded-2xl border border-slate-200/90 overflow-hidden flex items-center justify-center relative p-2 shadow-inner">
                        <svg id="patternSvg" class="w-full h-full" viewBox="0 0 400 200" preserveAspectRatio="xMidYMid meet">
                            <!-- Injected dynamically via JS -->
                        </svg>
                    </div>
                </div>

            </div>

        </div>

        <!-- FAQ ACCORDION SECTION (SEO & USER GUIDANCE) -->
        <div id="faqSection" class="mt-8 pt-6 border-t border-slate-200/80 space-y-3 no-print">
            <h2 id="faqTitle" class="text-base sm:text-lg font-extrabold text-slate-900 tracking-tight">
                Domande Frequenti su Calcolo Piastrelle, Scarti e Materiali
            </h2>
            
            <div class="space-y-2 text-xs sm:text-sm">
                
                <details class="bg-white rounded-2xl p-3.5 sm:p-4 border border-slate-200 group">
                    <summary id="faq1Q" class="font-bold text-slate-800 cursor-pointer list-none flex items-center justify-between">
                        <span>Perché è indispensabile aggiungere lo sfrido (10-20%) al calcolo delle piastrelle?</span>
                        <span class="text-slate-500 group-open:rotate-180 transition-transform">▼</span>
                    </summary>
                    <p id="faq1A" class="mt-2 text-slate-600 leading-relaxed text-xs">
                        Durante la posa, ogni piastrella che tocca una parete o un pilastro deve essere tagliata. La parte rimanente del taglio spesso non è riutilizzabile altrove. In più, è fondamentale conservare almeno una scatola integra di riserva: in caso di future riparazioni idrauliche, crepe o rotture, reperire la stessa identica piastrella dello stesso bagno di colore (tono/calibro) è quasi impossibile dopo pochi mesi.
                    </p>
                </details>

                <details class="bg-white rounded-2xl p-3.5 sm:p-4 border border-slate-200 group">
                    <summary id="faq2Q" class="font-bold text-slate-800 cursor-pointer list-none flex items-center justify-between">
                        <span>Quanti sacchi di colla servono per metro quadro?</span>
                        <span class="text-slate-500 group-open:rotate-180 transition-transform">▼</span>
                    </summary>
                    <p id="faq2A" class="mt-2 text-slate-600 leading-relaxed text-xs">
                        Il consumo varia in base alla dimensione della piastrella e alla dentatura della spatola. Per piastrelle fino a 30x30 cm con spatola da 6 mm si consumano circa 2.5-3 kg/m²; per formati medi come 60x60 cm con spatola da 8-10 mm servono circa 4-5 kg/m²; per grandi formati oltre 80 cm o pavimentazioni esterne è obbligatoria la doppia spalmatura (sul fondo e sul retro della piastrella), con consumi di circa 5.5-7 kg/m². Un sacco standard da 25 kg copre indicativamente tra i 4 e i 6 m².
                    </p>
                </details>

                <details class="bg-white rounded-2xl p-3.5 sm:p-4 border border-slate-200 group">
                    <summary id="faq3Q" class="font-bold text-slate-800 cursor-pointer list-none flex items-center justify-between">
                        <span>Come si calcola la quantità di stucco per le fughe?</span>
                        <span class="text-slate-500 group-open:rotate-180 transition-transform">▼</span>
                    </summary>
                    <p id="faq3A" class="mt-2 text-slate-600 leading-relaxed text-xs">
                        La quantità si calcola con la formula standard internazionale: [(A + B) / (A × B)] × C × D × 1.6, dove A e B sono lunghezza e larghezza della piastrella in cm, C è lo spessore in mm, D è la larghezza della fuga in mm e 1.6 è il coefficiente medio di densità dello stucco. Piastrelle grandi con fughe sottili (2 mm) richiedono pochissimo stucco (circa 200-300 g/m²), mentre formati piccoli come mosaici o piastrelle rustiche con fughe larghe (5 mm) richiedono oltre 1-1.5 kg/m².
                    </p>
                </details>

                <details class="bg-white rounded-2xl p-3.5 sm:p-4 border border-slate-200 group">
                    <summary id="faq4Q" class="font-bold text-slate-800 cursor-pointer list-none flex items-center justify-between">
                        <span>Come calcolo i metri quadri se la stanza ha una forma a L o irregolare?</span>
                        <span class="text-slate-500 group-open:rotate-180 transition-transform">▼</span>
                    </summary>
                    <p id="faq4A" class="mt-2 text-slate-600 leading-relaxed text-xs">
                        È sufficiente dividere mentalmente la stanza in due o più rettangoli regolari (ad esempio rettangolo A 3x4m = 12m² e rettangolo B 2x2.5m = 5m²), sommarli (12 + 5 = 17m²) e inserire il valore nella modalità "Metri Quadri Netti Noti". In presenza di nicchie o pareti fuori squadro, consigliamo di selezionare una percentuale di sfrido leggermente superiore (+15%).
                    </p>
                </details>

                <details class="bg-white rounded-2xl p-3.5 sm:p-4 border border-slate-200 group">
                    <summary id="faq5Q" class="font-bold text-slate-800 cursor-pointer list-none flex items-center justify-between">
                        <span>Cosa significa rettificato e che fuga richiede?</span>
                        <span class="text-slate-500 group-open:rotate-180 transition-transform">▼</span>
                    </summary>
                    <p id="faq5A" class="mt-2 text-slate-600 leading-relaxed text-xs">
                        Le piastrelle rettificate presentano bordi tagliati perfettamente a 90° dopo la cottura, consentendo di realizzare fughe minime di 1.5 - 2 mm per un effetto continuo moderno. Le piastrelle tradizionali con bordo naturale/stondato richiedono invece fughe di almeno 3 - 4 mm.
                    </p>
                </details>

            </div>
        </div>

    </main>

    {footer_html}

    <!-- CORE LOGIC & I18N SCRIPT -->
    <script>
        const TRANSLATIONS = {t_json_str};
        let currentLang = 'it';
        let currentRoomMode = 'dims'; // 'dims' or 'direct'

        function setRoomMode(mode) {{
            currentRoomMode = mode;
            const btnDims = document.getElementById('btnModeDims');
            const btnDirect = document.getElementById('btnModeDirect');
            const dimsGroup = document.getElementById('dimsInputGroup');
            const directGroup = document.getElementById('directInputGroup');

            if (mode === 'dims') {{
                btnDims.className = "px-2.5 py-1 rounded-lg bg-white text-slate-800 shadow-2xs transition";
                btnDirect.className = "px-2.5 py-1 rounded-lg text-slate-500 hover:text-slate-900 transition";
                dimsGroup.classList.remove('hidden');
                directGroup.classList.add('hidden');
            }} else {{
                btnDirect.className = "px-2.5 py-1 rounded-lg bg-white text-slate-800 shadow-2xs transition";
                btnDims.className = "px-2.5 py-1 rounded-lg text-slate-500 hover:text-slate-900 transition";
                directGroup.classList.remove('hidden');
                dimsGroup.classList.add('hidden');
            }}
            calculateAll();
        }}

        function setTilePreset(w, h, th) {{
            document.getElementById('tileWidth').value = w;
            document.getElementById('tileHeight').value = h;
            document.getElementById('tileThick').value = th;
            
            // Automatic estimation of coverage per box
            const sqmPerTile = (w * h) / 10000;
            let pieces = 4;
            if (sqmPerTile > 0.5) pieces = 2;
            else if (sqmPerTile < 0.1) pieces = 25;
            else if (sqmPerTile < 0.2) pieces = 8;
            
            document.getElementById('boxPieces').value = pieces;
            document.getElementById('boxCoverage').value = (sqmPerTile * pieces).toFixed(2);
            calculateAll();
        }}

        function onPatternChange() {{
            const sel = document.getElementById('selectPattern');
            const customGroup = document.getElementById('customWasteGroup');
            if (sel.value === 'custom') {{
                customGroup.classList.remove('hidden');
            }} else {{
                customGroup.classList.add('hidden');
            }}
            calculateAll();
        }}

        function calculateAll() {{
            // 1. Calculate Net Area
            let netArea = 0;
            if (currentRoomMode === 'dims') {{
                const l = parseFloat(document.getElementById('inputLength').value) || 0;
                const w = parseFloat(document.getElementById('inputWidth').value) || 0;
                netArea = l * w;
            }} else {{
                netArea = parseFloat(document.getElementById('inputDirectSqm').value) || 0;
            }}

            const deductions = parseFloat(document.getElementById('inputOpenings').value) || 0;
            netArea = Math.max(0, netArea - deductions);

            // 2. Waste Percentage
            let wastePct = 10;
            const patternVal = document.getElementById('selectPattern').value;
            if (patternVal === 'custom') {{
                wastePct = parseFloat(document.getElementById('customWasteInput').value) || 10;
            }} else {{
                wastePct = parseFloat(patternVal) || 10;
            }}

            // 3. Gross Area to Purchase
            const grossArea = netArea * (1 + (wastePct / 100));

            // 4. Boxes & Pieces
            const boxCov = parseFloat(document.getElementById('boxCoverage').value) || 1.44;
            const piecesPerBox = parseInt(document.getElementById('boxPieces').value) || 4;
            const boxesNeeded = boxCov > 0 ? Math.ceil(grossArea / boxCov) : 0;
            const totalCoverageMade = boxesNeeded * boxCov;
            const totalPieces = boxesNeeded * piecesPerBox;

            // 5. Adhesive (Colla)
            const adhesiveRate = parseFloat(document.getElementById('selectAdhesive').value) || 4.5;
            const bagWt = parseFloat(document.getElementById('bagWeight').value) || 25;
            const totalAdhesiveKg = grossArea * adhesiveRate;
            const totalAdhesiveBags = bagWt > 0 ? Math.ceil(totalAdhesiveKg / bagWt) : 0;

            // 6. Grout (Stucco Fughe) ISO Formula: ((A + B) / (A * B)) * C * D * 1.6
            const tileW = parseFloat(document.getElementById('tileWidth').value) || 60;
            const tileH = parseFloat(document.getElementById('tileHeight').value) || 60;
            const tileThick = parseFloat(document.getElementById('tileThick').value) || 9; // mm
            const groutW = parseFloat(document.getElementById('groutWidth').value) || 2.0; // mm

            let groutRateKgPerSqm = 0;
            if (tileW > 0 && tileH > 0) {{
                // ((A+B)/(A*B)) * C * D * 1.6  (A and B in cm, C and D in mm)
                groutRateKgPerSqm = ((tileW + tileH) / (tileW * tileH)) * tileThick * groutW * 1.6;
            }}
            const totalGroutKg = Math.max(0.5, (netArea * groutRateKgPerSqm));

            // Update DOM
            document.getElementById('valNetArea').textContent = `${{netArea.toFixed(2)}} m²`;
            document.getElementById('valGrossArea').textContent = `${{grossArea.toFixed(2)}} m²`;
            
            const t = TRANSLATIONS[currentLang] || TRANSLATIONS['it'];
            const boxSuffix = currentLang === 'en' ? 'Boxes' : (currentLang === 'es' ? 'Cajas' : (currentLang === 'fr' ? 'Cartons' : (currentLang === 'de' ? 'Pakete' : 'Scatole')));
            document.getElementById('valBoxes').textContent = `${{boxesNeeded}} ${{boxSuffix}}`;
            
            document.getElementById('valTotalSqmMade').textContent = `${{t.label_box_coverage ? t.label_box_coverage.split('(')[0] : 'Copertura'}}: ${{totalCoverageMade.toFixed(2)}} m²`;
            document.getElementById('valTotalTiles').textContent = `${{t.res_total_tiles || 'Totale pezzi'}}: ~${{totalPieces}}`;

            const bagSuffix = currentLang === 'en' ? 'Bags' : (currentLang === 'es' ? 'Sacos' : (currentLang === 'fr' ? 'Sacs' : (currentLang === 'de' ? 'Säcke' : 'Sacchi')));
            document.getElementById('valAdhesiveBags').textContent = `${{totalAdhesiveBags}} ${{bagSuffix}}`;
            document.getElementById('valAdhesiveKg').textContent = `Totale: ~${{Math.round(totalAdhesiveKg)}} kg`;

            document.getElementById('valGroutKg').textContent = `${{totalGroutKg.toFixed(1)}} kg`;
            document.getElementById('valGroutDetails').textContent = `Fuga ${{groutW}}mm · ${{tileThick}}mm spess.`;

            // Draw SVG Preview
            renderPatternSvg(patternVal, tileW, tileH);
        }}

        function renderPatternSvg(pattern, tw, th) {{
            const svg = document.getElementById('patternSvg');
            if (!svg) return;

            let html = '';
            const isOffset = pattern === '12';
            const isDiagonal = pattern === '15';
            const isHerringbone = pattern === '20';

            const w = 40;
            const h = tw === th ? 40 : 25;

            if (isDiagonal) {{
                html += '<g transform="rotate(45 200 100)">';
                for (let x = -100; x < 500; x += 45) {{
                    for (let y = -100; y < 300; y += 45) {{
                        html += `<rect x="${{x}}" y="${{y}}" width="40" height="40" fill="#ffffff" stroke="#d97706" stroke-width="1.5" rx="2" opacity="0.9"/>`;
                    }}
                }}
                html += '</g>';
            }} else if (isHerringbone) {{
                for (let x = 20; x < 380; x += 60) {{
                    for (let y = 10; y < 190; y += 40) {{
                        html += `<rect x="${{x}}" y="${{y}}" width="45" height="15" fill="#ffffff" stroke="#d97706" stroke-width="1.5" rx="1.5"/>`;
                        html += `<rect x="${{x+15}}" y="${{y+15}}" width="15" height="45" fill="#fef3c7" stroke="#b45309" stroke-width="1.5" rx="1.5"/>`;
                    }}
                }}
            }} else {{
                // Grid or Offset
                for (let row = 0; row < 6; row++) {{
                    const xOffset = (isOffset && row % 2 !== 0) ? (w / 2) : 0;
                    for (let col = -1; col < 11; col++) {{
                        const px = col * (w + 4) + xOffset + 10;
                        const py = row * (h + 4) + 10;
                        html += `<rect x="${{px}}" y="${{py}}" width="${{w}}" height="${{h}}" fill="#ffffff" stroke="#d97706" stroke-width="1.5" rx="2" opacity="0.95"/>`;
                    }}
                }}
            }}

            svg.innerHTML = html;
        }}

        function copyMaterialsList() {{
            const net = document.getElementById('valNetArea').textContent;
            const gross = document.getElementById('valGrossArea').textContent;
            const boxes = document.getElementById('valBoxes').textContent;
            const adhesive = document.getElementById('valAdhesiveBags').textContent + ' (' + document.getElementById('valAdhesiveKg').textContent + ')';
            const grout = document.getElementById('valGroutKg').textContent;

            const text = `📋 DISTINTA ACQUISTO PIASTRELLE (OmniTools Lab):\\n- Superficie Netta: ${{net}}\\n- Da Ordinare (con sfrido): ${{gross}}\\n- Scatole Piastrelle: ${{boxes}}\\n- Colla / Adesivo: ${{adhesive}}\\n- Stucco Fughe: ${{grout}}\\nGenerato su: https://www.omnitoolslab.com/piastrelle`;

            navigator.clipboard.writeText(text).then(() => {{
                const toast = document.getElementById('copyToast');
                toast.classList.remove('hidden');
                setTimeout(() => toast.classList.add('hidden'), 2500);
            }});
        }}

        function setLanguage(lang) {{
            currentLang = lang;
            localStorage.setItem('omnitools_lang', lang);
            try {{ window.dispatchEvent(new CustomEvent('omnitools_lang_changed', {{ detail: {{ lang: lang }} }})); }} catch(e) {{}}
            const sel = document.getElementById('langSelect');
            if (sel) sel.value = lang;
            document.documentElement.lang = lang;
            const t = TRANSLATIONS[lang] || TRANSLATIONS['it'];
            if (!t) return;

            document.getElementById('heroBadge').textContent = `OmniBuilding · ${{t.badge || 'Cantiere'}}`;
            document.getElementById('heroTitle').textContent = t.hero_title;
            document.getElementById('heroDesc').textContent = t.hero_desc;

            document.getElementById('secRoomTitle').textContent = t.sec_room_title;
            document.getElementById('secRoomDesc').textContent = t.sec_room_desc;
            document.getElementById('btnModeDims').textContent = t.mode_dimensions.split('(')[0].trim();
            document.getElementById('btnModeDirect').textContent = t.mode_direct_sqm.split('(')[0].trim();
            document.getElementById('lblLength').textContent = t.label_length;
            document.getElementById('lblWidth').textContent = t.label_width;
            document.getElementById('lblNetSqm').textContent = t.label_net_sqm;
            document.getElementById('lblOpenings').textContent = t.label_openings_deduct;

            document.getElementById('secTileTitle').textContent = t.sec_tile_title;
            document.getElementById('secTileDesc').textContent = t.sec_tile_desc;
            document.getElementById('lblTilePreset').textContent = t.label_tile_preset;
            document.getElementById('lblTileW').textContent = t.label_tile_w;
            document.getElementById('lblTileH').textContent = t.label_tile_h;
            document.getElementById('lblTileThick').textContent = t.label_tile_thick;
            document.getElementById('lblPattern').textContent = t.label_pattern;

            document.getElementById('optStraight').textContent = t.pattern_straight;
            document.getElementById('optOffset').textContent = t.pattern_offset;
            document.getElementById('optDiagonal').textContent = t.pattern_diagonal;
            document.getElementById('optHerringbone').textContent = t.pattern_herringbone;
            document.getElementById('optCustom').textContent = t.pattern_custom;

            document.getElementById('lblBoxCoverage').textContent = t.label_box_coverage;
            document.getElementById('lblBoxPieces').textContent = t.label_box_pieces;

            document.getElementById('secMaterialsTitle').textContent = t.sec_materials_title;
            document.getElementById('secMaterialsDesc').textContent = t.sec_materials_desc;
            document.getElementById('lblGroutWidth').textContent = t.label_grout_width;
            document.getElementById('lblBagWeight').textContent = t.label_bag_weight;
            document.getElementById('lblAdhesiveNotch').textContent = t.label_adhesive_notch;

            document.getElementById('notchSmall').textContent = t.notch_small;
            document.getElementById('notchMedium').textContent = t.notch_medium;
            document.getElementById('notchLarge').textContent = t.notch_large;

            document.getElementById('summaryTitle').textContent = t.summary_title;
            document.getElementById('resNetAreaLabel').textContent = t.res_net_area;
            document.getElementById('resGrossAreaLabel').textContent = t.res_gross_area;
            document.getElementById('resBoxesLabel').textContent = t.res_boxes;
            document.getElementById('resAdhesiveBagsLabel').textContent = t.res_adhesive_bags;
            document.getElementById('resGroutKgLabel').textContent = t.res_grout_kg;
            document.getElementById('resWasteWarning').textContent = t.res_waste_warning;

            document.getElementById('btnCopyList').textContent = t.btn_copy_list;
            document.getElementById('btnPrint').textContent = t.btn_print;
            document.getElementById('previewTitle').textContent = t.preview_title;

            // FAQs
            for (let i = 1; i <= 5; i++) {{
                const qEl = document.getElementById(`faq${{i}}Q`);
                const aEl = document.getElementById(`faq${{i}}A`);
                if (qEl && t[`faq${{i}}_q`]) qEl.firstElementChild.textContent = t[`faq${{i}}_q`];
                if (aEl && t[`faq${{i}}_a`]) aEl.textContent = t[`faq${{i}}_a`];
            }}

            const disc = document.getElementById('legalDisclaimerText');
            if (disc && t.disclaimer_text) disc.textContent = t.disclaimer_text;

            calculateAll();
        }}

        window.addEventListener('DOMContentLoaded', () => {{
            const stored = localStorage.getItem('omnitools_lang');
            const browserLang = (navigator.language || 'it').slice(0, 2).toLowerCase();
            const lang = stored || (['it', 'en', 'es', 'fr', 'de', 'pt'].includes(browserLang) ? browserLang : 'it');
            setLanguage(lang);
            calculateAll();
        }});

        window.addEventListener('omnitools_lang_changed', (e) => {{
            if (e.detail && e.detail.lang && e.detail.lang !== currentLang) {{
                setLanguage(e.detail.lang);
            }}
        }});
    </script>

    {header_js}
    {footer_js}

</body>
</html>
"""

output_path = os.path.join(cur_dir, "piastrelle.html")
with open(output_path, "w", encoding="utf-8") as f:
    f.write(html_code)

print("SUCCESS: piastrelle.html generated perfectly!")
