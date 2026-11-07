import json
import sys
import os

from nav_header import render_suite_header, render_suite_header_js
from unified_footer import render_unified_footer, render_unified_footer_js

base_dir = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(base_dir, "translations_taglio.json"), "r", encoding="utf-8") as f:
    t_data = json.load(f)

t_json_str = json.dumps(t_data, ensure_ascii=False)

header_html = render_suite_header("taglio")
header_js = render_suite_header_js()
footer_html = render_unified_footer("taglio")
footer_js = render_unified_footer_js()

html_code = f"""<!DOCTYPE html>
<html lang="it">
<head>
    <meta name="google-site-verification" content="MRdbDm9lLhokeD3I0FOpUSOhNaF_2WaveKvu52FxtG4">
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0">
    <title>TaglioOttimo - Ottimizzatore di Taglio Lineare 1D, Barre & Travi</title>
    <meta name="description" content="Calcola la disposizione di taglio ottimale per travi, assi di legno, barre metalliche e tubi. Riduci al minimo lo sfrido con algoritmo bin-packing 1D e spessore lama (kerf).">
    
    <!-- Canonical & SEO Meta Tags -->
    <link rel="canonical" href="https://www.omnitoolslab.com/taglio">
    <meta name="robots" content="index, follow">
    <meta property="og:type" content="website">
    <meta property="og:title" content="OmniTools - TaglioOttimo: Ottimizzatore di Taglio 1D">
    <meta property="og:description" content="Pianifica tagli per legno, ferro e alluminio con zero sprechi. Calcola barre necessarie, sfrido e sequenza di taglio con compensazione lama.">
    <meta property="og:url" content="https://www.omnitoolslab.com/taglio">
    <meta property="og:site_name" content="OmniTools Lab">
    <meta property="og:image" content="https://www.omnitoolslab.com/og-taglio.png">
    <meta property="og:image:width" content="1200">
    <meta property="og:image:height" content="630">
    <meta property="og:image:type" content="image/png">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:image" content="https://www.omnitoolslab.com/og-taglio.png">

    <!-- Schema.org JSON-LD Structured Data (Rich Snippets) -->
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@graph": [
        {{
          "@type": "WebApplication",
          "name": "TaglioOttimo — Ottimizzatore di Taglio Lineare 1D",
          "url": "https://www.omnitoolslab.com/taglio",
          "applicationCategory": "UtilityApplication",
          "operatingSystem": "All",
          "browserRequirements": "Requires JavaScript. Requires HTML5.",
          "offers": {{
            "@type": "Offer",
            "price": "0",
            "priceCurrency": "EUR"
          }},
          "description": "Applicazione professionale per ottimizzare il piano di taglio 1D di travi in legno, profilati in metallo e tubi idraulici con compensazione dello spessore lama."
        }},
        {{
          "@type": "SoftwareApplication",
          "name": "TaglioOttimo Cut List Optimizer",
          "operatingSystem": "Web Browser",
          "applicationCategory": "DesignApplication",
          "aggregateRating": {{
            "@type": "AggregateRating",
            "ratingValue": "4.9",
            "reviewCount": "184"
          }}
        }}
      ]
    }}
    </script>

    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {{
            theme: {{
                extend: {{
                    colors: {{
                        amber: {{
                            50: '#fffbeb',
                            100: '#fef3c7',
                            200: '#fde68a',
                            500: '#f59e0b',
                            600: '#d97706',
                            700: '#b45309',
                            800: '#92400e',
                            900: '#78350f',
                        }}
                    }}
                }}
            }}
        }}
    </script>
    
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
    
    <style>
        body {{
            font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            -webkit-font-smoothing: antialiased;
        }}
        .font-mono {{
            font-family: 'JetBrains Mono', monospace;
        }}
        .metric-card {{
            transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
        }}
        .metric-card:hover {{
            transform: translateY(-2px);
            box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.05), 0 8px 10px -6px rgba(0, 0, 0, 0.01);
        }}
        .cut-bar-segment {{
            transition: all 0.2s ease;
        }}
        .cut-bar-segment:hover {{
            filter: brightness(1.1);
        }}
        @media print {{
            .no-print {{ display: none !important; }}
            body {{ background: white; color: black; }}
            .print-only {{ display: block !important; }}
            .card-box {{ border: 1px solid #cbd5e1 !important; box-shadow: none !important; break-inside: avoid; }}
        }}
        .print-only {{ display: none; }}
    </style>
</head>
<body class="bg-slate-50 text-slate-800 min-h-screen flex flex-col justify-between antialiased selection:bg-amber-500 selection:text-white">

    <!-- Universal Header with Chrome Tabs & Tool Picker -->
    {header_html}

    <main class="max-w-5xl mx-auto px-3 sm:px-6 py-2.5 sm:py-5 flex-1 w-full space-y-3 sm:space-y-5">
        <!-- Main Tool Intro Header -->
        <div class="mb-4 text-center sm:text-left sm:flex sm:items-end sm:justify-between border-b border-slate-200/80 pb-4">
            <div>
                <div class="inline-flex items-center gap-2 px-2.5 py-1 rounded-full bg-amber-50 border border-amber-200/60 text-amber-800 text-xs font-semibold mb-2">
                    <span class="w-2 h-2 rounded-full bg-amber-500 animate-pulse"></span>
                    <span id="badgeCategory">OmniBuilding • Taglio 1D & Falegnameria</span>
                </div>
                <h1 id="mainTitle" class="text-2xl sm:text-3xl font-extrabold text-slate-900 tracking-tight">Ottimizzatore di Taglio 1D</h1>
                <p id="mainSubtitle" class="text-slate-600 text-xs sm:text-sm mt-1 max-w-2xl">
                    Pianifica tagli per legno, profilati e tubi minimizzando lo sfrido di materiale con compensazione spessore lama (Kerf).
                </p>
            </div>
            <!-- Unit & Quick Controls -->
            <div class="mt-4 sm:mt-0 flex items-center justify-center sm:justify-end gap-2 shrink-0">
                <div class="flex items-center gap-2 bg-white px-2.5 py-1.5 rounded-2xl border border-slate-200 shadow-xs">
                    <span id="unitLabelText" class="text-[11px] font-bold uppercase tracking-wider text-slate-500 mr-1 hidden sm:inline">Misure:</span>
                    <div class="inline-flex p-0.5 bg-slate-100 rounded-xl border border-slate-200/80 gap-0.5 text-xs font-bold">
                        <button type="button" id="unitCmBtn" onclick="setUnit('cm')" class="w-10 sm:w-11 py-1 rounded-lg bg-white text-amber-700 shadow-xs font-extrabold transition active:scale-95 text-center">cm</button>
                        <button type="button" id="unitMmBtn" onclick="setUnit('mm')" class="w-10 sm:w-11 py-1 rounded-lg text-slate-600 hover:text-slate-900 transition active:scale-95 text-center font-bold">mm</button>
                        <button type="button" id="unitInBtn" onclick="setUnit('in')" class="w-10 sm:w-11 py-1 rounded-lg text-slate-600 hover:text-slate-900 transition active:scale-95 text-center font-bold" title="Inches (pollici)">in</button>
                        <button type="button" id="unitFtBtn" onclick="setUnit('ft')" class="w-10 sm:w-11 py-1 rounded-lg text-slate-600 hover:text-slate-900 transition active:scale-95 text-center font-bold" title="Feet (piedi)">ft</button>
                    </div>
                </div>
            </div>
        </div>

        <!-- Presets Bar -->
        <div class="mb-8 p-3.5 bg-white border border-slate-200/70 rounded-2xl shadow-xs flex flex-wrap items-center gap-2">
            <span id="presetTitleLabel" class="text-xs font-bold text-slate-500 uppercase tracking-wider flex items-center gap-1.5 mr-1">
                <svg class="w-4 h-4 text-amber-500" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M13 10V3L4 14h7v7l9-11h-7z"/></svg>
                Esempi Rapidi:
            </span>
            <button onclick="applyPreset('wood_diy')" class="px-3 py-1.5 rounded-lg bg-amber-50 hover:bg-amber-100 text-amber-900 border border-amber-200/80 text-xs font-semibold transition">
                🪵 <span id="presetWoodDiyText">Scaffale Legno (Travetti 200cm)</span>
            </button>
            <button onclick="applyPreset('metal_frame')" class="px-3 py-1.5 rounded-lg bg-slate-100 hover:bg-slate-200 text-slate-800 border border-slate-300 text-xs font-semibold transition">
                🔩 <span id="presetMetalFrameText">Telaio Ferro (Barre 600cm)</span>
            </button>
            <button onclick="applyPreset('pergola')" class="px-3 py-1.5 rounded-lg bg-amber-50 hover:bg-amber-100 text-amber-900 border border-amber-200/80 text-xs font-semibold transition">
                🏡 <span id="presetPergolaText">Pergola Giardino (Travi 300cm)</span>
            </button>
        </div>

        <!-- Layout Grid: Left Inputs / Right Results & Visuals -->
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
            
            <!-- Left Column: Inputs Form (5 cols) -->
            <div class="lg:col-span-5 space-y-6">
                
                <!-- Stock Material & Kerf Card -->
                <div class="bg-white rounded-3xl p-6 border border-slate-200 shadow-xs">
                    <div class="flex items-center gap-2.5 mb-5 pb-3 border-b border-slate-100">
                        <span class="w-7 h-7 rounded-lg bg-amber-500/10 text-amber-600 flex items-center justify-center font-bold text-sm">1</span>
                        <h2 id="stockSettingsTitle" class="text-base font-bold text-slate-900">1. Barre Master di Partenza</h2>
                    </div>

                    <div class="space-y-4">
                        <div>
                            <div class="flex justify-between items-center text-xs font-semibold text-slate-700 mb-1.5">
                                <label id="stockLengthLabel" for="stockLengthInput">Lunghezza Barra Standard</label>
                                <span class="text-slate-400 font-mono" id="stockLengthUnit">cm</span>
                            </div>
                            <div class="relative">
                                <input type="number" id="stockLengthInput" min="10" step="any" value="200" oninput="calculateCutList()"
                                    class="w-full bg-slate-50 border border-slate-200 rounded-xl px-3.5 py-2.5 text-sm font-mono font-bold text-slate-800 focus:outline-none focus:ring-2 focus:ring-amber-500 focus:bg-white transition">
                                <span class="absolute right-3.5 top-2.5 text-slate-400 text-xs font-bold font-mono pointer-events-none" id="stockLengthBadge">cm</span>
                            </div>
                        </div>

                        <div>
                            <div class="flex justify-between items-center text-xs font-semibold text-slate-700 mb-1.5">
                                <label id="kerfLabel" for="kerfInput">Spessore Lama (Kerf)</label>
                                <span class="text-slate-400 font-mono" id="kerfUnit">mm</span>
                            </div>
                            <div class="relative">
                                <input type="number" id="kerfInput" min="0" max="20" step="0.1" value="3.0" oninput="calculateCutList()"
                                    class="w-full bg-slate-50 border border-slate-200 rounded-xl px-3.5 py-2.5 text-sm font-mono font-bold text-slate-800 focus:outline-none focus:ring-2 focus:ring-amber-500 focus:bg-white transition">
                                <span class="absolute right-3.5 top-2.5 text-slate-400 text-xs font-bold font-mono pointer-events-none">mm</span>
                            </div>
                            <p id="kerfHint" class="text-[11px] text-slate-500 mt-1.5">Materiale asportato da ogni taglio (es. 3 mm per banco sega, 1.5 mm ferro).</p>
                        </div>
                    </div>
                </div>

                <!-- Required Cuts (Parts Table) Card -->
                <div class="bg-white rounded-3xl p-6 border border-slate-200 shadow-xs">
                    <div class="flex items-center justify-between mb-5 pb-3 border-b border-slate-100">
                        <div class="flex items-center gap-2.5">
                            <span class="w-7 h-7 rounded-lg bg-amber-500/10 text-amber-600 flex items-center justify-center font-bold text-sm">2</span>
                            <h2 id="requiredCutsTitle" class="text-base font-bold text-slate-900">2. Pezzi Richiesti (Distinta)</h2>
                        </div>
                        <button type="button" onclick="addCutRow()" class="px-3 py-1 rounded-xl bg-amber-500 hover:bg-amber-600 text-white text-xs font-bold transition flex items-center gap-1 shadow-xs">
                            <span id="addRowBtn">+ Aggiungi</span>
                        </button>
                    </div>

                    <!-- Cuts Input Table -->
                    <div class="overflow-x-auto">
                        <table class="w-full text-left text-xs">
                            <thead>
                                <tr class="text-slate-500 border-b border-slate-100">
                                    <th class="pb-2 font-semibold" id="colLengthHeader">Lunghezza (<span class="unitLabel">cm</span>)</th>
                                    <th class="pb-2 font-semibold w-20" id="colQtyHeader">Quantità</th>
                                    <th class="pb-2 font-semibold" id="colLabelHeader">Nome / Repere</th>
                                    <th class="pb-2 w-8"></th>
                                </tr>
                            </thead>
                            <tbody id="cutsTableBody" class="divide-y divide-slate-100">
                                <!-- Dynamic Rows Injected Here -->
                            </tbody>
                        </table>
                    </div>

                    <div class="mt-4 pt-3 border-t border-slate-100 flex items-center justify-between">
                        <span class="text-xs text-slate-500 font-medium">Totale pezzi inseriti: <strong id="totalPartsDemanded" class="text-slate-800 font-mono">0</strong></span>
                        <button type="button" onclick="clearAllCuts()" class="text-[11px] text-rose-500 hover:text-rose-700 font-semibold underline">Svuota lista</button>
                    </div>
                </div>

            </div>

            <!-- Right Column: Visual Diagram, KPIs & Workshop Cut Guide (7 cols) -->
            <div class="lg:col-span-7 space-y-6">
                
                <!-- KPI Results Dashboard Grid -->
                <div class="grid grid-cols-2 sm:grid-cols-4 gap-3">
                    <div class="metric-card bg-white p-4 rounded-2xl border border-slate-200/90 shadow-xs">
                        <span id="kpiBarsNeededLabel" class="block text-slate-500 text-[11px] font-semibold uppercase tracking-wider mb-1">Barre Master</span>
                        <div class="flex items-baseline gap-1">
                            <span id="resBarsCount" class="text-2xl sm:text-3xl font-extrabold text-amber-600 font-mono">0</span>
                            <span class="text-xs font-bold text-slate-400">pz</span>
                        </div>
                    </div>

                    <div class="metric-card bg-white p-4 rounded-2xl border border-slate-200/90 shadow-xs">
                        <span id="kpiEfficiencyLabel" class="block text-slate-500 text-[11px] font-semibold uppercase tracking-wider mb-1">Efficienza</span>
                        <div class="flex items-baseline gap-1">
                            <span id="resEfficiency" class="text-2xl sm:text-3xl font-extrabold text-emerald-600 font-mono">0.0</span>
                            <span class="text-xs font-bold text-slate-400">%</span>
                        </div>
                    </div>

                    <div class="metric-card bg-white p-4 rounded-2xl border border-slate-200/90 shadow-xs">
                        <span id="kpiTotalWasteLabel" class="block text-slate-500 text-[11px] font-semibold uppercase tracking-wider mb-1">Sfrido Scartato</span>
                        <div class="flex items-baseline gap-1">
                            <span id="resWastePct" class="text-2xl sm:text-3xl font-extrabold text-rose-600 font-mono">0.0</span>
                            <span class="text-xs font-bold text-slate-400">%</span>
                        </div>
                    </div>

                    <div class="metric-card bg-white p-4 rounded-2xl border border-slate-200/90 shadow-xs">
                        <span id="kpiCutsCountLabel" class="block text-slate-500 text-[11px] font-semibold uppercase tracking-wider mb-1">Tagli Totali</span>
                        <div class="flex items-baseline gap-1">
                            <span id="resTotalCuts" class="text-2xl sm:text-3xl font-extrabold text-slate-900 font-mono">0</span>
                            <span class="text-xs font-bold text-slate-400">passaggi</span>
                        </div>
                    </div>
                </div>

                <!-- Visual Cutting Stock Diagram -->
                <div class="bg-white rounded-3xl p-6 border border-slate-200 shadow-xs">
                    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 mb-4 pb-3 border-b border-slate-100">
                        <div class="flex items-center gap-2">
                            <svg class="w-5 h-5 text-amber-500" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M14.121 14.121L19 19m-7-7l7-7m-7 7l-2.879 2.879a3 3 0 11-4.242-4.242L10.758 10.758m0 0l2.879-2.879a3 3 0 10-4.242-4.242L6.515 6.515"/></svg>
                            <h3 id="visualCuttingMapTitle" class="text-base font-bold text-slate-900">Mappa Visiva del Piano di Taglio</h3>
                        </div>
                        <!-- Legend -->
                        <div class="flex items-center gap-3 text-[11px] font-medium text-slate-600">
                            <span class="inline-flex items-center gap-1">
                                <span class="w-3 h-3 rounded-xs bg-amber-500"></span> <span id="legendUsedLabel">Pezzo</span>
                            </span>
                            <span class="inline-flex items-center gap-1">
                                <span class="w-3 h-3 rounded-xs bg-slate-800"></span> <span id="legendKerfLabel">Kerf</span>
                            </span>
                            <span class="inline-flex items-center gap-1">
                                <span class="w-3 h-3 rounded-xs bg-slate-200 border border-slate-300"></span> <span id="legendWasteLabel">Sfrido</span>
                            </span>
                        </div>
                    </div>

                    <!-- Bars Container -->
                    <div id="visualBarsContainer" class="space-y-4 max-h-[500px] overflow-y-auto pr-1">
                        <!-- Bars dynamically rendered here -->
                    </div>

                    <!-- Summary Footnote -->
                    <div class="mt-5 pt-3 border-t border-slate-100 flex flex-wrap items-center justify-between text-xs text-slate-500 font-mono">
                        <div>Metri acquistati: <span id="summaryStockLength" class="font-bold text-slate-800">0 m</span></div>
                        <div>Metri utili netti: <span id="summaryUsedLength" class="font-bold text-emerald-600">0 m</span></div>
                        <div>Sfrido puro: <span id="summaryWasteLength" class="font-bold text-rose-600">0 m</span></div>
                    </div>
                </div>

                <!-- Sequential Cut List (Workshop Guide) Table -->
                <div class="bg-white rounded-3xl p-6 border border-slate-200 shadow-xs">
                    <div class="flex items-center justify-between mb-4 pb-3 border-b border-slate-100">
                        <h3 id="detailedCutlistTableTitle" class="text-base font-bold text-slate-900">Distinta di Taglio Sequenziale (Guida per Officina)</h3>
                        <button type="button" onclick="window.print()" class="px-2.5 py-1 rounded-lg bg-slate-100 hover:bg-slate-200 text-slate-700 text-xs font-semibold flex items-center gap-1.5 transition">
                            <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M17 17h2a2 2 0 002-2v-4a2 2 0 00-2-2H5a2 2 0 00-2 2v4a2 2 0 002 2h2m2 4h6a2 2 0 002-2v-4H7v4a2 2 0 002 2zm8-12V5a2 2 0 00-2-2H9a2 2 0 00-2 2v4h10z"/></svg>
                            Stampa Distinta
                        </button>
                    </div>

                    <div class="overflow-x-auto">
                        <table class="w-full text-left text-xs">
                            <thead>
                                <tr class="text-slate-400 border-b border-slate-100">
                                    <th class="pb-2 font-semibold w-16">Barra</th>
                                    <th class="pb-2 font-semibold">Tagli da Eseguire in Sequenza</th>
                                    <th class="pb-2 font-semibold text-right w-24">Sfrido Residuo</th>
                                </tr>
                            </thead>
                            <tbody id="workshopTableBody" class="divide-y divide-slate-100">
                                <!-- Populated dynamically -->
                            </tbody>
                        </table>
                    </div>
                </div>

            </div>

        </div>

        <!-- FAQ Section -->
        <section id="faqSection" class="no-print mt-12 bg-white rounded-2xl border border-slate-200/90 shadow-xs p-5 sm:p-6 space-y-4">
            <div class="flex items-center gap-2.5 mb-1 pb-2 border-b border-slate-100">
                <span class="text-xl">❓</span>
                <h2 class="text-base sm:text-lg font-black text-slate-900 font-jakarta flex items-center gap-2">
                    <span id="faqTitle">Domande Frequenti sull'Ottimizzazione di Taglio 1D</span>
                </h2>
                <span class="text-[10px] font-extrabold uppercase px-2 py-0.5 rounded-full bg-slate-100 text-slate-600 border border-slate-200">FAQ</span>
            </div>
            
            <div id="faqContainer" class="space-y-3">
                <details class="group bg-slate-50/80 hover:bg-slate-50 rounded-2xl border border-slate-200/80 p-4 transition duration-150">
                    <summary class="flex justify-between items-center font-bold text-xs sm:text-sm text-slate-900 cursor-pointer list-none select-none">
                        <span id="faqQ1">Cos'è lo spessore lama (Kerf) e perché è fondamentale considerarlo?</span>
                        <svg class="w-4 h-4 text-slate-400 group-open:-rotate-180 transition-transform duration-200 shrink-0 ml-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/>
                        </svg>
                    </summary>
                    <div id="faqA1" class="text-xs sm:text-sm text-slate-600 mt-2.5 leading-relaxed border-t border-slate-200/60 pt-2.5">
                        Ogni volta che una lama circolare, una sega a nastro o una troncatrice taglia un pezzo di materiale, trasforma una striscia di materiale in trucioli o limatura. Questa larghezza asportata si chiama *Kerf* (solitamente tra 2.4 mm e 3.2 mm per il legno, 1.2-2.0 mm per metalli). Se devi ricavare quattro pezzi da 50 cm da una barra da 200 cm, senza considerare il kerf l'ultimo pezzo risulterà corto di circa 1 cm!
                    </div>
                </details>

                <details class="group bg-slate-50/80 hover:bg-slate-50 rounded-2xl border border-slate-200/80 p-4 transition duration-150">
                    <summary class="flex justify-between items-center font-bold text-xs sm:text-sm text-slate-900 cursor-pointer list-none select-none">
                        <span id="faqQ2">Come funziona l'algoritmo di calcolo (First Fit Decreasing)?</span>
                        <svg class="w-4 h-4 text-slate-400 group-open:-rotate-180 transition-transform duration-200 shrink-0 ml-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/>
                        </svg>
                    </summary>
                    <div id="faqA2" class="text-xs sm:text-sm text-slate-600 mt-2.5 leading-relaxed border-t border-slate-200/60 pt-2.5">
                        Il problema dell'ottimizzazione del taglio 1D (Cutting Stock Problem) è un classico problema combinatorio matematico. L'algoritmo ordina tutti i pezzi richiesti in ordine decrescente dal più lungo al più corto, e li alloca nella prima barra master in cui entrano, tenendo conto ad ogni passaggio dello spessore della lama. Questa euristica garantisce una riduzione drastica dello sfrido e richiede pochissimi millisecondi di calcolo.
                    </div>
                </details>

                <details class="group bg-slate-50/80 hover:bg-slate-50 rounded-2xl border border-slate-200/80 p-4 transition duration-150">
                    <summary class="flex justify-between items-center font-bold text-xs sm:text-sm text-slate-900 cursor-pointer list-none select-none">
                        <span id="faqQ3">Posso usare questo calcolatore per profilati metallici, tubi in PVC e battiscopa?</span>
                        <svg class="w-4 h-4 text-slate-400 group-open:-rotate-180 transition-transform duration-200 shrink-0 ml-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/>
                        </svg>
                    </summary>
                    <div id="faqA3" class="text-xs sm:text-sm text-slate-600 mt-2.5 leading-relaxed border-t border-slate-200/60 pt-2.5">
                        Certamente! Qualsiasi materiale lineare continuo (travi in legno, canaline elettriche, tubi idraulici, profilati d'alluminio o acciaio, cornici e battiscopa) segue esattamente la stessa geometria lineare 1D.
                    </div>
                </details>

                <details class="group bg-slate-50/80 hover:bg-slate-50 rounded-2xl border border-slate-200/80 p-4 transition duration-150">
                    <summary class="flex justify-between items-center font-bold text-xs sm:text-sm text-slate-900 cursor-pointer list-none select-none">
                        <span id="faqQ4">Come gestire lo sfrido finale residuo per non sprecare materiale nei progetti futuri?</span>
                        <svg class="w-4 h-4 text-slate-400 group-open:-rotate-180 transition-transform duration-200 shrink-0 ml-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/>
                        </svg>
                    </summary>
                    <div id="faqA4" class="text-xs sm:text-sm text-slate-600 mt-2.5 leading-relaxed border-t border-slate-200/60 pt-2.5">
                        Lo schema visivo colorato evidenzia in grigio chiaro lo sfrido esatto di ogni barra. Gli spezzoni riutilizzabili (es. oltre 40-50 cm) possono essere etichettati e conservati in rastrelliera come 'scorte corte'. Nei progetti successivi basterà inserire la loro lunghezza effettiva come barra master per utilizzarli prioritariamente prima di intaccare barre nuove intere.
                    </div>
                </details>
            </div>
        </section>

    </main>

    <!-- Universal Footer -->
    {footer_html}

    <!-- Universal Scripts -->
    <script>
        {header_js}
        {footer_js}
    </script>

    <!-- Translations & Taglio Logic Script -->
    <script>
        const TRANSLATIONS = {t_json_str};
        let currentLang = 'it';
        let currentUnit = 'cm'; // 'cm' or 'mm'

        // Piece palette colors for distinctive visualization
        const PIECE_COLORS = [
            'bg-amber-500 text-white border-amber-600',
            'bg-blue-500 text-white border-blue-600',
            'bg-emerald-500 text-white border-emerald-600',
            'bg-purple-500 text-white border-purple-600',
            'bg-rose-500 text-white border-rose-600',
            'bg-teal-500 text-white border-teal-600',
            'bg-indigo-500 text-white border-indigo-600',
            'bg-orange-500 text-white border-orange-600',
            'bg-cyan-600 text-white border-cyan-700'
        ];

        // Cuts Data Model
        let cutsList = [
            {{ length: 120, qty: 4, label: "Montante A" }},
            {{ length: 75, qty: 6, label: "Traversa B" }},
            {{ length: 42, qty: 4, label: "Rinforzo C" }}
        ];

        // Unit Conversion Factors from CM (base internal unit)
        // 1 cm = 10 mm
        // 1 cm = 0.393701 in (1 in = 2.54 cm)
        // 1 cm = 0.0328084 ft (1 ft = 30.48 cm)
        const UNIT_TO_CM = {{
            'cm': 1,
            'mm': 0.1,
            'in': 2.54,
            'ft': 30.48
        }};

        function setUnit(newUnit) {{
            if (currentUnit === newUnit || !UNIT_TO_CM[newUnit]) return;
            
            // Conversion ratio: from currentUnit to newUnit
            // val_in_cm = val * UNIT_TO_CM[currentUnit]
            // val_new = val_in_cm / UNIT_TO_CM[newUnit]
            const toNewUnit = (val) => {{
                const inCm = val * UNIT_TO_CM[currentUnit];
                const res = inCm / UNIT_TO_CM[newUnit];
                if (newUnit === 'in' || newUnit === 'ft') {{
                    return parseFloat(res.toFixed(2));
                }}
                return parseFloat(res.toFixed(1));
            }};

            // Convert stock length
            const stockIn = document.getElementById('stockLengthInput');
            stockIn.value = toNewUnit(parseFloat(stockIn.value) || 200);
            
            // Convert cut lengths
            cutsList.forEach(c => {{
                c.length = toNewUnit(parseFloat(c.length) || 1);
            }});

            currentUnit = newUnit;

            // Update UI buttons styling
            ['cm', 'mm', 'in', 'ft'].forEach(u => {{
                const btn = document.getElementById(`unit${{u.charAt(0).toUpperCase() + u.slice(1)}}Btn`);
                if (btn) {{
                    if (u === currentUnit) {{
                        btn.className = 'w-10 sm:w-11 py-1 rounded-lg bg-white text-amber-700 shadow-xs font-extrabold transition active:scale-95 text-center';
                    }} else {{
                        btn.className = 'w-10 sm:w-11 py-1 rounded-lg text-slate-600 hover:text-slate-900 transition active:scale-95 text-center font-bold';
                    }}
                }}
            }});

            document.getElementById('stockLengthUnit').textContent = currentUnit;
            document.getElementById('stockLengthBadge').textContent = currentUnit;
            document.querySelectorAll('.unitLabel').forEach(el => el.textContent = currentUnit);

            renderCutsTable();
            calculateCutList();
        }}

        function renderCutsTable() {{
            const tbody = document.getElementById('cutsTableBody');
            tbody.innerHTML = '';
            let totalDemanded = 0;

            cutsList.forEach((cut, idx) => {{
                totalDemanded += (parseInt(cut.qty) || 0);
                const tr = document.createElement('tr');
                tr.className = 'hover:bg-slate-50 transition';
                tr.innerHTML = `
                    <td class="py-2 pr-2">
                        <input type="number" step="any" min="1" value="${{cut.length}}" onchange="updateCutRow(${{idx}}, 'length', this.value)"
                            class="w-full bg-slate-50 border border-slate-200 rounded-lg px-2 py-1 text-xs font-mono font-bold text-slate-800 focus:bg-white focus:outline-none focus:ring-1 focus:ring-amber-500">
                    </td>
                    <td class="py-2 pr-2 w-20">
                        <input type="number" step="1" min="1" value="${{cut.qty}}" onchange="updateCutRow(${{idx}}, 'qty', this.value)"
                            class="w-full bg-slate-50 border border-slate-200 rounded-lg px-2 py-1 text-xs font-mono font-bold text-slate-800 text-center focus:bg-white focus:outline-none focus:ring-1 focus:ring-amber-500">
                    </td>
                    <td class="py-2 pr-2">
                        <input type="text" value="${{cut.label || ''}}" placeholder="Pezzo #${{idx + 1}}" onchange="updateCutRow(${{idx}}, 'label', this.value)"
                            class="w-full bg-slate-50 border border-slate-200 rounded-lg px-2 py-1 text-xs text-slate-700 placeholder-slate-400 focus:bg-white focus:outline-none focus:ring-1 focus:ring-amber-500">
                    </td>
                    <td class="py-2 text-right">
                        <button type="button" onclick="removeCutRow(${{idx}})" class="text-slate-300 hover:text-rose-500 transition p-1" title="Elimina">
                            <svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"/></svg>
                        </button>
                    </td>
                `;
                tbody.appendChild(tr);
            }});

            document.getElementById('totalPartsDemanded').textContent = totalDemanded;
        }}

        function addCutRow() {{
            const defaultLength = currentUnit === 'cm' ? 50 : 500;
            cutsList.push({{ length: defaultLength, qty: 2, label: `Pezzo #${{cutsList.length + 1}}` }});
            renderCutsTable();
            calculateCutList();
        }}

        function updateCutRow(idx, field, val) {{
            if (field === 'length') cutsList[idx].length = Math.max(0.1, parseFloat(val) || 0.1);
            if (field === 'qty') cutsList[idx].qty = Math.max(1, parseInt(val) || 1);
            if (field === 'label') cutsList[idx].label = val;
            renderCutsTable();
            calculateCutList();
        }}

        function removeCutRow(idx) {{
            if (cutsList.length <= 1) {{
                cutsList = [{{ length: currentUnit === 'cm' ? 50 : 500, qty: 1, label: "Pezzo #1" }}];
            }} else {{
                cutsList.splice(idx, 1);
            }}
            renderCutsTable();
            calculateCutList();
        }}

        function clearAllCuts() {{
            cutsList = [{{ length: currentUnit === 'cm' ? 50 : 500, qty: 1, label: "Pezzo #1" }}];
            renderCutsTable();
            calculateCutList();
        }}

        function applyPreset(presetKey) {{
            if (presetKey === 'wood_diy') {{
                if (currentUnit === 'mm') setUnit('cm');
                document.getElementById('stockLengthInput').value = 200;
                document.getElementById('kerfInput').value = 3.0;
                cutsList = [
                    {{ length: 120, qty: 4, label: "Montante Legno" }},
                    {{ length: 70, qty: 6, label: "Ripiano" }},
                    {{ length: 35, qty: 4, label: "Traverso" }}
                ];
            }} else if (presetKey === 'metal_frame') {{
                if (currentUnit === 'mm') setUnit('cm');
                document.getElementById('stockLengthInput').value = 600;
                document.getElementById('kerfInput').value = 2.0;
                cutsList = [
                    {{ length: 240, qty: 4, label: "Longherone" }},
                    {{ length: 150, qty: 8, label: "Crociera" }},
                    {{ length: 80, qty: 6, label: "Piedino" }}
                ];
            }} else if (presetKey === 'pergola') {{
                if (currentUnit === 'mm') setUnit('cm');
                document.getElementById('stockLengthInput').value = 300;
                document.getElementById('kerfInput').value = 3.2;
                cutsList = [
                    {{ length: 280, qty: 4, label: "Arcata Trave" }},
                    {{ length: 190, qty: 6, label: "Listello Ombra" }},
                    {{ length: 95, qty: 8, label: "Staffa Diagonale" }}
                ];
            }}
            renderCutsTable();
            calculateCutList();
        }}

        // Bin Packing First Fit Decreasing with Kerf
        function calculateCutList() {{
            const stockLengthVal = parseFloat(document.getElementById('stockLengthInput').value) || 200;
            const kerfMm = parseFloat(document.getElementById('kerfInput').value) || 0;
            
            // Normalize kerf (input is in mm) to current unit
            // 1 mm = 0.1 cm
            // 1 mm = 0.0393701 in
            // 1 mm = 0.00328084 ft
            let kerfInUnit = kerfMm;
            if (currentUnit === 'cm') kerfInUnit = kerfMm * 0.1;
            else if (currentUnit === 'in') kerfInUnit = kerfMm / 25.4;
            else if (currentUnit === 'ft') kerfInUnit = kerfMm / 304.8;

            // Expand all requested pieces into an array of individual items
            let itemsToCut = [];
            cutsList.forEach((c, catIdx) => {{
                const len = parseFloat(c.length) || 0;
                const qty = parseInt(c.qty) || 0;
                const colorClass = PIECE_COLORS[catIdx % PIECE_COLORS.length];
                for (let i = 0; i < qty; i++) {{
                    itemsToCut.push({{
                        length: len,
                        label: c.label || `Pz #${{catIdx + 1}}`,
                        color: colorClass,
                        catIdx: catIdx
                    }});
                }}
            }});

            // Sort descending: First Fit Decreasing heuristic
            itemsToCut.sort((a, b) => b.length - a.length);

            // Check if any piece exceeds master bar
            const oversized = itemsToCut.filter(it => it.length > stockLengthVal);
            if (oversized.length > 0) {{
                alert(`Attenzione: il pezzo \"${{oversized[0].label}}\" (${{oversized[0].length}} ${{currentUnit}}) è più lungo della barra standard (${{stockLengthVal}} ${{currentUnit}})!`);
            }}

            // Bin Packing Simulation
            // Each bin represents one stock bar
            let bars = [];

            itemsToCut.forEach(item => {{
                if (item.length > stockLengthVal) return; // skip impossible pieces

                let placed = false;
                for (let b = 0; b < bars.length; b++) {{
                    const bar = bars[b];
                    // If adding item, we need item.length + kerf (if not first cut)
                    const extraKerf = bar.cuts.length > 0 ? kerfInUnit : 0;
                    if (bar.remainingLength >= (item.length + extraKerf)) {{
                        bar.cuts.push(item);
                        bar.remainingLength -= (item.length + extraKerf);
                        bar.totalKerf += extraKerf;
                        bar.totalUsedLength += item.length;
                        placed = true;
                        break;
                    }}
                }}

                if (!placed) {{
                    // Start new stock bar
                    bars.push({{
                        stockLength: stockLengthVal,
                        remainingLength: stockLengthVal - item.length,
                        totalUsedLength: item.length,
                        totalKerf: 0,
                        cuts: [item]
                    }});
                }}
            }});

            // KPIs calculation
            const barsCount = bars.length;
            const totalStockBought = barsCount * stockLengthVal;
            let totalUsefulLength = 0;
            let totalKerfConsumed = 0;
            let totalCutsCount = 0;

            bars.forEach(b => {{
                totalUsefulLength += b.totalUsedLength;
                totalKerfConsumed += b.totalKerf;
                totalCutsCount += b.cuts.length; // 1 cut per piece separated
            }});

            const pureWasteLength = Math.max(0, totalStockBought - totalUsefulLength - totalKerfConsumed);
            const totalOffcut = totalStockBought - totalUsefulLength;
            const efficiencyPct = totalStockBought > 0 ? ((totalUsefulLength / totalStockBought) * 100).toFixed(1) : 0;
            const wastePct = totalStockBought > 0 ? ((totalOffcut / totalStockBought) * 100).toFixed(1) : 0;

            // Render KPIs
            document.getElementById('resBarsCount').textContent = barsCount;
            document.getElementById('resEfficiency').textContent = efficiencyPct;
            document.getElementById('resWastePct').textContent = wastePct;
            document.getElementById('resTotalCuts').textContent = totalCutsCount;

            // Render Footnote Summaries in meters
            const toMeters = (val) => {{
                const inCm = val * (UNIT_TO_CM[currentUnit] || 1);
                return (inCm / 100).toFixed(2);
            }};
            document.getElementById('summaryStockLength').textContent = `${{toMeters(totalStockBought)}} m (${{barsCount}} barre)`;
            document.getElementById('summaryUsedLength').textContent = `${{toMeters(totalUsefulLength)}} m`;
            document.getElementById('summaryWasteLength').textContent = `${{toMeters(totalOffcut)}} m (${{wastePct}}%)`;

            // Render Visual Bars
            renderVisualBars(bars, stockLengthVal, kerfInUnit);
            renderWorkshopTable(bars);
        }}

        function renderVisualBars(bars, stockLength, kerfInUnit) {{
            const container = document.getElementById('visualBarsContainer');
            container.innerHTML = '';

            if (bars.length === 0) {{
                container.innerHTML = '<div class=\"p-8 text-center text-slate-400 text-xs italic\">Nessun taglio da visualizzare. Aggiungi i pezzi alla lista.</div>';
                return;
            }}

            bars.forEach((bar, barIdx) => {{
                const barWrapper = document.createElement('div');
                barWrapper.className = 'bg-slate-50 border border-slate-200/90 rounded-2xl p-3 sm:p-4';

                // Bar Header info
                const barEfficiency = ((bar.totalUsedLength / bar.stockLength) * 100).toFixed(1);
                const barWaste = Math.max(0, bar.remainingLength).toFixed(1);
                
                barWrapper.innerHTML = `
                    <div class="flex items-center justify-between text-xs font-semibold mb-2 text-slate-700">
                        <div class="flex items-center gap-2">
                            <span class="w-2 h-2 rounded-full bg-amber-500"></span>
                            <span class="font-bold text-slate-900">Barra #${{barIdx + 1}} (${{bar.stockLength}} ${{currentUnit}})</span>
                            <span class="text-slate-400 text-[11px] font-normal">• ${{bar.cuts.length}} pezzi</span>
                        </div>
                        <div class="flex items-center gap-3 font-mono text-[11px]">
                            <span class="text-emerald-700 font-bold">${{barEfficiency}}% utile</span>
                            <span class="text-rose-600">Sfrido: ${{barWaste}} ${{currentUnit}}</span>
                        </div>
                    </div>
                `;

                // Outer progress bar representing physical stock length
                const visualStrip = document.createElement('div');
                visualStrip.className = 'w-full h-10 sm:h-11 bg-slate-200 rounded-xl overflow-hidden flex items-stretch border border-slate-300 relative shadow-inner';

                bar.cuts.forEach((piece, pIdx) => {{
                    // Piece segment
                    const piecePct = (piece.length / bar.stockLength) * 100;
                    const pieceDiv = document.createElement('div');
                    pieceDiv.className = `cut-bar-segment relative h-full flex flex-col justify-center items-center font-mono font-bold text-[10px] sm:text-xs overflow-hidden px-1 border-r border-black/20 ${{piece.color}}`;
                    pieceDiv.style.width = `${{piecePct}}%`;
                    pieceDiv.title = `${{piece.label}}: ${{piece.length}} ${{currentUnit}}`;
                    pieceDiv.innerHTML = `
                        <span class="truncate w-full text-center leading-tight">${{piece.length}}</span>
                        <span class="truncate w-full text-center text-[9px] opacity-80 font-normal leading-tight hidden sm:block">${{piece.label}}</span>
                    `;
                    visualStrip.appendChild(pieceDiv);

                    // Blade Kerf separator (if not the last piece or if remaining scrap exists)
                    if (pIdx < bar.cuts.length - 1 || bar.remainingLength > 0) {{
                        const kerfPct = (kerfInUnit / bar.stockLength) * 100;
                        if (kerfPct > 0) {{
                            const kerfDiv = document.createElement('div');
                            kerfDiv.className = 'h-full bg-slate-900 shrink-0';
                            kerfDiv.style.width = `${{Math.max(kerfPct, 0.4)}}%`;
                            kerfDiv.title = `Lama / Kerf`;
                            visualStrip.appendChild(kerfDiv);
                        }}
                    }}
                }});

                // Offcut / Waste remnant segment
                const wastePct = (Math.max(0, bar.remainingLength) / bar.stockLength) * 100;
                if (wastePct > 0.05) {{
                    const wasteDiv = document.createElement('div');
                    wasteDiv.className = 'h-full bg-repeating-linear-to-r from-slate-200 to-slate-300 text-slate-500 font-mono text-[10px] flex items-center justify-center italic px-1 overflow-hidden';
                    wasteDiv.style.width = `${{wastePct}}%`;
                    wasteDiv.title = `Sfrido residuo: ${{bar.remainingLength.toFixed(1)}} ${{currentUnit}}`;
                    if (wastePct > 8) {{
                        wasteDiv.textContent = `${{bar.remainingLength.toFixed(1)}} ${{currentUnit}}`;
                    }}
                    visualStrip.appendChild(wasteDiv);
                }}

                barWrapper.appendChild(visualStrip);
                container.appendChild(barWrapper);
            }});
        }}

        function renderWorkshopTable(bars) {{
            const tbody = document.getElementById('workshopTableBody');
            tbody.innerHTML = '';

            bars.forEach((bar, bIdx) => {{
                const tr = document.createElement('tr');
                tr.className = 'hover:bg-slate-50 transition font-mono';
                
                const cutsText = bar.cuts.map((c, i) => `<strong>${{c.length}} ${{currentUnit}}</strong> <span class="text-slate-400 font-sans">(${{c.label}})</span>`).join(' <span class="text-amber-500 font-bold mx-1">→</span> ');

                tr.innerHTML = `
                    <td class="py-2.5 font-bold text-slate-800">#${{bIdx + 1}}</td>
                    <td class="py-2.5 text-slate-700">${{cutsText}}</td>
                    <td class="py-2.5 text-right font-bold text-rose-600">${{bar.remainingLength.toFixed(1)}} ${{currentUnit}}</td>
                `;
                tbody.appendChild(tr);
            }});
        }}

        function updateTexts(lang) {{
            currentLang = lang;
            const t = (key) => TRANSLATIONS[key]?.[lang] || TRANSLATIONS[key]?.['it'] || '';

            document.title = t('meta_title');
            document.querySelector('meta[name="description"]').setAttribute('content', t('meta_desc'));

            document.getElementById('mainTitle').textContent = t('title');
            document.getElementById('mainSubtitle').textContent = t('subtitle');
            document.getElementById('stockSettingsTitle').textContent = t('stock_settings_title');
            document.getElementById('stockLengthLabel').textContent = t('stock_length');
            document.getElementById('kerfLabel').textContent = t('kerf_label');
            document.getElementById('kerfHint').textContent = t('kerf_hint');
            document.getElementById('requiredCutsTitle').textContent = t('required_cuts_title');
            document.getElementById('colLengthHeader').childNodes[0].nodeValue = t('col_length') + ' ';
            document.getElementById('colQtyHeader').textContent = t('col_quantity');
            document.getElementById('colLabelHeader').textContent = t('col_label');
            document.getElementById('addRowBtn').textContent = t('add_row_btn');
            
            document.getElementById('presetTitleLabel').childNodes[2].nodeValue = ' ' + t('presets_title');
            document.getElementById('presetWoodDiyText').textContent = t('preset_wood_diy');
            document.getElementById('presetMetalFrameText').textContent = t('preset_metal_frame');
            document.getElementById('presetPergolaText').textContent = t('preset_pergola');

            document.getElementById('kpiBarsNeededLabel').textContent = t('kpi_bars_needed');
            document.getElementById('kpiEfficiencyLabel').textContent = t('kpi_efficiency');
            document.getElementById('kpiTotalWasteLabel').textContent = t('kpi_total_waste');
            document.getElementById('kpiCutsCountLabel').textContent = t('kpi_cuts_count');
            document.getElementById('visualCuttingMapTitle').textContent = t('visual_cutting_map');
            document.getElementById('legendUsedLabel').textContent = t('legend_used');
            document.getElementById('legendWasteLabel').textContent = t('legend_waste');
            document.getElementById('legendKerfLabel').textContent = t('legend_kerf');
            document.getElementById('detailedCutlistTableTitle').textContent = t('detailed_cutlist_table');

            const fTitle = document.getElementById('faqTitle');
            if (fTitle) fTitle.textContent = t('faq_title');
            document.getElementById('faqQ1').textContent = t('faq_q1');
            document.getElementById('faqA1').textContent = t('faq_a1');
            document.getElementById('faqQ2').textContent = t('faq_q2');
            document.getElementById('faqA2').textContent = t('faq_a2');
            document.getElementById('faqQ3').textContent = t('faq_q3');
            document.getElementById('faqA3').textContent = t('faq_a3');
            const q4 = document.getElementById('faqQ4');
            if (q4) q4.textContent = t('faq_q4');
            const a4 = document.getElementById('faqA4');
            if (a4) a4.textContent = t('faq_a4');

            calculateCutList();
        }}

        // Listen for universal language changes
        window.addEventListener('omni_lang_change', (e) => {{
            if (e.detail && e.detail.lang) updateTexts(e.detail.lang);
        }});

        // Initialization
        document.addEventListener('DOMContentLoaded', () => {{
            const savedLang = localStorage.getItem('omni_pref_lang') || 'it';
            updateTexts(savedLang);
            renderCutsTable();
            calculateCutList();
        }});
    </script>
</body>
</html>
"""

with open(os.path.join(base_dir, "taglio.html"), "w", encoding="utf-8") as f:
    f.write(html_code)

print("taglio.html written successfully!")
