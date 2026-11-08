import json
import sys
import os

from nav_header import render_suite_header, render_suite_header_js
from unified_footer import render_unified_footer, render_unified_footer_js

cur_dir = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(cur_dir, "translations_tetto.json")
with open(json_path, "r", encoding="utf-8") as f:
    t_data = json.load(f)

t_json_str = json.dumps(t_data, ensure_ascii=False)

header_html = render_suite_header("tetto")
header_js = render_suite_header_js()
footer_html = render_unified_footer("tetto")
footer_js = render_unified_footer_js()

html_code = f"""<!DOCTYPE html>
<html lang="it">
<head>
    <meta name="google-site-verification" content="MRdbDm9lLhokeD3I0FOpUSOhNaF_2WaveKvu52FxtG4">
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0">
    <title>Calcolo Pendenza Tetto, Falda & Superficie Online — Gradi, Percentuale & Trave | TettoFacile</title>
    <meta name="description" content="Calcolatore professionale per pendenza tetto in gradi e percentuale (%). Calcola altezza del colmo, lunghezza reale della trave (incluso sporto di gronda) e metri quadri effettivi della falda per tegole, lamiere e coppi.">
    
    <!-- Canonical & SEO Meta Tags -->
    <link rel="canonical" href="https://www.omnitoolslab.com/tetto">
    <meta name="robots" content="index, follow">
    <meta property="og:type" content="website">
    <meta property="og:title" content="TettoFacile — Calcolo Pendenza Tetto, Falda & Superficie Online">
    <meta property="og:description" content="Calcola pendenza in gradi e %, altezza colmo, sviluppo reale della trave e superficie del tetto in mq.">
    <meta property="og:url" content="https://www.omnitoolslab.com/tetto">
    <meta property="og:site_name" content="OmniTools Lab">
    <meta property="og:image" content="https://www.omnitoolslab.com/og-tetto.png">
    <meta property="og:image:width" content="1200">
    <meta property="og:image:height" content="630">
    <meta property="og:image:type" content="image/png">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:image" content="https://www.omnitoolslab.com/og-tetto.png">

    <!-- Schema.org JSON-LD Structured Data (Rich Snippets) -->
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@graph": [
        {{
          "@type": "WebApplication",
          "name": "TettoFacile — Calcolo Pendenza Tetto & Sviluppo Falda",
          "url": "https://www.omnitoolslab.com/tetto",
          "applicationCategory": "UtilitiesApplication",
          "operatingSystem": "All",
          "browserRequirements": "Requires JavaScript",
          "offers": {{
            "@type": "Offer",
            "price": "0",
            "priceCurrency": "EUR"
          }},
          "description": "Strumento interattivo per il calcolo della pendenza di tetti, coperture e tettoie con conversione gradi/percentuale e sviluppo trave."
        }},
        {{
          "@type": "BreadcrumbList",
          "itemListElement": [
            {{
              "@type": "ListItem",
              "position": 1,
              "name": "OmniTools Lab",
              "item": "https://www.omnitoolslab.com/"
            }},
            {{
              "@type": "ListItem",
              "position": 2,
              "name": "TettoFacile",
              "item": "https://www.omnitoolslab.com/tetto"
            }}
          ]
        }},
        {{
          "@type": "FAQPage",
          "mainEntity": [
            {{
              "@type": "Question",
              "name": "Qual è la formula per convertire la pendenza del tetto da percentuale a gradi?",
              "acceptedAnswer": {{
                "@type": "Answer",
                "text": "La formula è: Gradi = arctan(Pendenza % / 100) × (180 / π). Ad esempio, una pendenza del 30% corrisponde a circa 16.7°."
              }}
            }},
            {{
              "@type": "Question",
              "name": "Qual è la pendenza minima consigliata per un tetto in tegole o coppi?",
              "acceptedAnswer": {{
                "@type": "Answer",
                "text": "Per tegole e coppi tradizionali la pendenza minima raccomandata è del 30-35% (circa 17°-19°). Per lamiere continue e pannelli sandwich si può scendere fino al 7-10% con opportuna impermeabilizzazione."
              }}
            }},
            {{
              "@type": "Question",
              "name": "Come si calcola la superficie effettiva della falda di un tetto?",
              "acceptedAnswer": {{
                "@type": "Answer",
                "text": "La superficie effettiva si ottiene moltiplicando la lunghezza reale della trave inclinata (incluso lo sporto di gronda) per la larghezza dell'edificio lungo la linea di gronda."
              }}
            }},
            {{
              "@type": "Question",
              "name": "Cos'è lo sporto di gronda e come influisce sulla lunghezza della trave?",
              "acceptedAnswer": {{
                "@type": "Answer",
                "text": "Lo sporto è la parte di copertura che sporge dai muri perimetrali per deviare l'acqua piovana. Va sommato all'ipotenusa del triangolo di falda per ricavare la lunghezza commerciale del legname."
              }}
            }}
          ]
        }}
      ]
    }}
    </script>

    <!-- PWA & Mobile Icons -->
    <link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
    <link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">
    <link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png">
    <link rel="manifest" href="/site.webmanifest">
    <meta name="theme-color" content="#f59e0b">

    <!-- Tailwind CSS (CDN) + Custom Font (Inter / Plus Jakarta Sans) -->
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@500;700&display=swap" rel="stylesheet">

    <style>
        body {{
            font-family: 'Plus Jakarta Sans', sans-serif;
        }}
        .font-mono {{
            font-family: 'JetBrains Mono', monospace;
        }}
        @media print {{
            .no-print {{
                display: none !important;
            }}
            body {{
                background: white !important;
                color: black !important;
            }}
        }}
    </style>
</head>
<body class="bg-slate-50 text-slate-900 min-h-screen flex flex-col antialiased selection:bg-amber-100 selection:text-amber-900">

    {header_html}

    <!-- MAIN APP CONTAINER -->
    <main class="max-w-5xl mx-auto px-3 sm:px-6 py-2.5 sm:py-5 flex-1 w-full space-y-3 sm:space-y-5">
        
        <!-- Hero Header -->
        <div id="heroContainer" class="text-center max-w-2xl mx-auto pt-1 sm:pt-2">
            <div class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-amber-50 border border-amber-200/80 text-[11px] font-extrabold text-amber-800 tracking-wide uppercase mb-2">
                <span>🏠</span>
                <span id="heroBadge">OmniBuilding · Geometria & Cantiere</span>
            </div>
            <h1 id="heroTitle" class="text-2xl sm:text-4xl font-extrabold text-slate-900 tracking-tight leading-tight mb-1.5 sm:mb-2">
                Calcolo Pendenza Tetto, Falda & Superficie
            </h1>
            <p id="heroDesc" class="text-slate-600 text-xs sm:text-base leading-relaxed px-2">
                Calcola all'istante l'inclinazione in gradi e percentuale, la quota del colmo, la lunghezza reale della trave e la superficie della falda.
            </p>
        </div>

        <!-- Mode Selector -->
        <div id="modeSelectorBar" class="no-print bg-slate-200/80 p-1 rounded-2xl flex max-w-sm sm:max-w-md mx-auto shadow-inner text-xs sm:text-sm font-bold">
            <button id="modeDirectBtn" onclick="switchMode('direct')" class="flex-1 py-1.5 sm:py-2 rounded-xl bg-white text-amber-700 shadow-sm transition active:scale-95 text-center">
                📐 Da Base & Colmo
            </button>
            <button id="modeReverseBtn" onclick="switchMode('reverse')" class="flex-1 py-1.5 sm:py-2 rounded-xl text-slate-600 hover:text-slate-900 transition active:scale-95 text-center">
                📏 Da Pendenza & Base
            </button>
        </div>

        <!-- Calculator Layout -->
        <div class="flex flex-col lg:grid lg:grid-cols-12 gap-3 sm:gap-6 items-start">
            
            <!-- RESULTS & VISUAL COLUMN (First on mobile) -->
            <div id="resultsColumn" class="w-full order-1 lg:order-2 lg:col-span-7 space-y-2.5 sm:space-y-4">
                
                <!-- Status Banner -->
                <div id="statusBanner" class="p-3 sm:p-4 rounded-2xl border transition-colors duration-200 flex items-start gap-3 bg-amber-50/80 border-amber-200 text-amber-900">
                    <span id="statusIcon" class="text-xl sm:text-2xl leading-none mt-0.5">🏠</span>
                    <div class="min-w-0 flex-1">
                        <div class="flex items-center justify-between gap-2 mb-0.5">
                            <h3 id="statusTitle" class="font-extrabold text-xs sm:text-sm leading-snug">Pendenza Standard Ottimale</h3>
                            <span id="statusTag" class="text-[9px] sm:text-[10px] font-bold px-2 py-0.5 rounded-full bg-amber-200/60 uppercase tracking-wide shrink-0">Ideale Tegole</span>
                        </div>
                        <p id="statusDesc" class="text-xs sm:text-xs leading-relaxed text-slate-600">
                            Inclinazione ideale per il deflusso rapido delle acque meteoriche con tegole tradizionali e coppi senza ristagni.
                        </p>
                    </div>
                </div>

                <!-- 4 Core Metric KPI Cards -->
                <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 sm:gap-2.5">
                    
                    <!-- Pendenza % -->
                    <div class="bg-white rounded-2xl p-3 sm:p-4 border border-slate-200 shadow-2xs flex flex-col justify-between">
                        <span id="colSlopeLabel" class="text-[10px] sm:text-xs font-bold text-slate-600 uppercase tracking-wide">Pendenza</span>
                        <div class="my-1">
                            <span id="valSlopePct" class="text-xl sm:text-2xl font-black font-mono text-amber-600 tracking-tight">30.0%</span>
                        </div>
                        <span id="valRatio" class="text-[10px] font-mono text-slate-600">Rapporto 1:3.3</span>
                    </div>

                    <!-- Inclinazione Gradi -->
                    <div class="bg-white rounded-2xl p-3 sm:p-4 border border-slate-200 shadow-2xs flex flex-col justify-between">
                        <span id="colAngleLabel" class="text-[10px] sm:text-xs font-bold text-slate-600 uppercase tracking-wide">Inclinazione</span>
                        <div class="my-1">
                            <span id="valAngleDeg" class="text-xl sm:text-2xl font-black font-mono text-slate-900 tracking-tight">16.7°</span>
                        </div>
                        <span class="text-[10px] font-mono text-slate-600">Angolo in gradi</span>
                    </div>

                    <!-- Lunghezza Trave -->
                    <div class="bg-white rounded-2xl p-3 sm:p-4 border border-slate-200 shadow-2xs flex flex-col justify-between">
                        <span id="colRafterLabel" class="text-[10px] sm:text-xs font-bold text-slate-600 uppercase tracking-wide">Lunghezza Trave</span>
                        <div class="my-1">
                            <span id="valRafterLength" class="text-xl sm:text-2xl font-black font-mono text-slate-900 tracking-tight">465.3 cm</span>
                        </div>
                        <span id="valOverhangNote" class="text-[10px] font-mono text-slate-600">Incluso sporto 50cm</span>
                    </div>

                    <!-- Superficie Reale -->
                    <div class="bg-white rounded-2xl p-3 sm:p-4 border border-slate-200 shadow-2xs flex flex-col justify-between">
                        <span id="colAreaLabel" class="text-[10px] sm:text-xs font-bold text-slate-600 uppercase tracking-wide">Superficie Falda</span>
                        <div class="my-1">
                            <span id="valRoofArea" class="text-xl sm:text-2xl font-black font-mono text-slate-900 tracking-tight">46.5 m²</span>
                        </div>
                        <span id="valLengthNote" class="text-[10px] font-mono text-slate-600">Su facciata 10.0 m</span>
                    </div>
                </div>

                <!-- Dynamic Vector Section Diagram -->
                <div class="bg-white rounded-2xl p-3.5 sm:p-5 border border-slate-200 shadow-2xs">
                    <div class="flex items-center justify-between mb-2">
                        <span id="schemaTitle" class="text-xs sm:text-sm font-extrabold text-slate-900">Schema Geometrico Sezione Falda</span>
                        <span id="schemaScale" class="text-[10px] font-mono font-bold text-slate-600 bg-slate-100 px-2 py-0.5 rounded-full">In scala interattiva</span>
                    </div>

                    <!-- Interactive SVG Canvas -->
                    <div class="w-full bg-slate-50/70 border border-slate-200 rounded-xl p-2 sm:p-4 flex items-center justify-center overflow-hidden">
                        <svg id="roofSvgCanvas" class="w-full h-44 sm:h-56 select-none" viewBox="0 0 500 240" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <!-- Injected dynamically via JS -->
                        </svg>
                    </div>

                    <!-- Quick Context Tip -->
                    <div class="mt-3 text-xs leading-relaxed text-slate-600 bg-amber-50/50 p-2.5 rounded-xl border border-amber-100">
                        <span id="ruleTip">💡 <strong>Regola Geometrica del Tetto:</strong> La pendenza percentuale esprime quanti centimetri si sale verticalmente ogni 100 cm di avanzamento orizzontale. La lunghezza della trave include l'ipotenusa del triangolo più lo sporto di gronda.</span>
                    </div>
                </div>

            </div>

            <!-- CONTROLS & INPUT COLUMN -->
            <div id="controlsColumn" class="w-full order-2 lg:order-1 lg:col-span-5 space-y-3 sm:space-y-4">
                
                <div class="bg-white rounded-2xl p-4 sm:p-5 border border-slate-200 shadow-2xs space-y-3.5">
                    
                    <!-- Unit Switcher -->
                    <div class="flex items-center justify-between">
                        <label id="unitLabel" class="text-xs font-extrabold uppercase tracking-wide text-slate-600">Unità di Misura</label>
                        <div class="inline-flex p-0.5 rounded-xl bg-slate-100 border border-slate-200 text-xs font-bold">
                            <button type="button" onclick="setUnit('cm')" id="unitBtnCm" class="px-2.5 py-1 rounded-lg bg-white shadow-2xs text-amber-700 transition">cm</button>
                            <button type="button" onclick="setUnit('m')" id="unitBtnM" class="px-2.5 py-1 rounded-lg text-slate-600 hover:text-slate-900 transition">m</button>
                        </div>
                    </div>

                    <!-- Input 1: Base / Run (L) -->
                    <div class="space-y-1.5">
                        <div class="flex items-center justify-between">
                            <label for="inputBase" id="baseLabel" class="text-xs font-extrabold text-slate-700 flex items-center gap-1.5">
                                <span class="w-2 h-2 rounded-full bg-amber-500"></span>
                                <span>Larghezza Base in Pianta (L)</span>
                            </label>
                            <span id="baseUnitTag" class="text-xs font-mono font-bold text-slate-600">cm</span>
                        </div>
                        <input type="number" id="inputBase" value="400" min="50" max="5000" step="1" oninput="calculateRoof()" class="w-full px-3.5 py-2.5 bg-slate-50 hover:bg-slate-100/70 focus:bg-white text-slate-900 font-mono font-bold text-base rounded-xl border border-slate-200 focus:border-amber-500 focus:outline-none transition">
                        <input type="range" id="sliderBase" min="100" max="1500" value="400" step="5" oninput="syncSlider('base', this.value)" class="w-full accent-amber-500 cursor-pointer">
                    </div>

                    <!-- Input 2: Dynamic (Height in Direct Mode, Slope% in Reverse Mode) -->
                    <div id="modeDirectGroup" class="space-y-1.5">
                        <div class="flex items-center justify-between">
                            <label for="inputHeight" id="heightLabel" class="text-xs font-extrabold text-slate-700 flex items-center gap-1.5">
                                <span class="w-2 h-2 rounded-full bg-amber-500"></span>
                                <span>Altezza Colmo / Dislivello (H)</span>
                            </label>
                            <span id="heightUnitTag" class="text-xs font-mono font-bold text-slate-600">cm</span>
                        </div>
                        <input type="number" id="inputHeight" value="120" min="10" max="3000" step="1" oninput="calculateRoof()" class="w-full px-3.5 py-2.5 bg-slate-50 hover:bg-slate-100/70 focus:bg-white text-slate-900 font-mono font-bold text-base rounded-xl border border-slate-200 focus:border-amber-500 focus:outline-none transition">
                        <input type="range" id="sliderHeight" min="20" max="800" value="120" step="5" oninput="syncSlider('height', this.value)" class="w-full accent-amber-500 cursor-pointer">
                    </div>

                    <div id="modeReverseGroup" class="space-y-1.5 hidden">
                        <div class="flex items-center justify-between">
                            <label for="inputSlopePct" id="slopePctLabel" class="text-xs font-extrabold text-slate-700 flex items-center gap-1.5">
                                <span class="w-2 h-2 rounded-full bg-amber-500"></span>
                                <span>Pendenza Desiderata (%)</span>
                            </label>
                            <span class="text-xs font-mono font-bold text-slate-600">%</span>
                        </div>
                        <input type="number" id="inputSlopePct" value="30" min="2" max="250" step="0.5" oninput="calculateRoof()" class="w-full px-3.5 py-2.5 bg-slate-50 hover:bg-slate-100/70 focus:bg-white text-slate-900 font-mono font-bold text-base rounded-xl border border-slate-200 focus:border-amber-500 focus:outline-none transition">
                        <input type="range" id="sliderSlopePct" min="5" max="120" value="30" step="1" oninput="syncSlider('slopePct', this.value)" class="w-full accent-amber-500 cursor-pointer">
                    </div>

                    <!-- Input 3: Sporto Gronda (cm) -->
                    <div class="space-y-1.5 pt-1 border-t border-slate-100">
                        <div class="flex items-center justify-between">
                            <label for="inputOverhang" id="overhangLabel" class="text-xs font-bold text-slate-600">Sporto Gronda Grondaia (cm)</label>
                            <span class="text-xs font-mono font-bold text-slate-600">cm</span>
                        </div>
                        <input type="number" id="inputOverhang" value="50" min="0" max="200" step="5" oninput="calculateRoof()" class="w-full px-3 py-2 bg-slate-50 hover:bg-slate-100/70 focus:bg-white text-slate-900 font-mono font-bold text-xs rounded-xl border border-slate-200 focus:border-amber-500 focus:outline-none transition">
                    </div>

                    <!-- Input 4: Lunghezza Fabbricato (m) -->
                    <div class="space-y-1.5">
                        <div class="flex items-center justify-between">
                            <label for="inputRoofLength" id="roofLengthLabel" class="text-xs font-bold text-slate-600">Lunghezza Edificio / Falda (m)</label>
                            <span class="text-xs font-mono font-bold text-slate-600">m</span>
                        </div>
                        <input type="number" id="inputRoofLength" value="10" min="1" max="100" step="0.5" oninput="calculateRoof()" class="w-full px-3 py-2 bg-slate-50 hover:bg-slate-100/70 focus:bg-white text-slate-900 font-mono font-bold text-xs rounded-xl border border-slate-200 focus:border-amber-500 focus:outline-none transition">
                    </div>

                    <!-- Presets Grid -->
                    <div class="pt-2 border-t border-slate-100">
                        <label id="presetsTitle" class="text-[11px] font-extrabold uppercase tracking-wide text-slate-600 block mb-2">Preset standard di pendenza tetto:</label>
                        <div class="grid grid-cols-2 gap-1.5 text-left">
                            <button type="button" onclick="applyPreset(8.7)" class="p-2 rounded-xl bg-slate-50 hover:bg-amber-50 border border-slate-200 hover:border-amber-300 transition text-left group">
                                <span id="preset1Title" class="text-xs font-bold text-slate-800 group-hover:text-amber-800 block">Tettoia (8.7% • 5°)</span>
                                <span id="preset1Sub" class="text-[10px] text-slate-600 block">Minimo scolo acqua</span>
                            </button>
                            <button type="button" onclick="applyPreset(30)" class="p-2 rounded-xl bg-slate-50 hover:bg-amber-50 border border-slate-200 hover:border-amber-300 transition text-left group">
                                <span id="preset2Title" class="text-xs font-bold text-slate-800 group-hover:text-amber-800 block">Tegole (30% • 16.7°)</span>
                                <span id="preset2Sub" class="text-[10px] text-slate-600 block">Standard coppi</span>
                            </button>
                            <button type="button" onclick="applyPreset(60)" class="p-2 rounded-xl bg-slate-50 hover:bg-amber-50 border border-slate-200 hover:border-amber-300 transition text-left group">
                                <span id="preset3Title" class="text-xs font-bold text-slate-800 group-hover:text-amber-800 block">Neve (60% • 31°)</span>
                                <span id="preset3Sub" class="text-[10px] text-slate-600 block">Zone montane</span>
                            </button>
                            <button type="button" onclick="applyPreset(100)" class="p-2 rounded-xl bg-slate-50 hover:bg-amber-50 border border-slate-200 hover:border-amber-300 transition text-left group">
                                <span id="preset4Title" class="text-xs font-bold text-slate-800 group-hover:text-amber-800 block">Alpino (100% • 45°)</span>
                                <span id="preset4Sub" class="text-[10px] text-slate-600 block">Ripido per neve</span>
                            </button>
                        </div>
                    </div>

                </div>

            </div>

        </div>

        <!-- FAQ Accordion Section -->
        <div class="mt-8 pt-6 border-t border-slate-200 space-y-3">
            <h2 id="faqTitle" class="text-base sm:text-lg font-extrabold text-slate-900 tracking-tight">Domande Frequenti su Pendenza Tetto, Falde e Calcolo Geometria</h2>
            
            <div class="space-y-2 text-xs sm:text-sm">
                <details class="bg-white rounded-2xl p-3.5 sm:p-4 border border-slate-200 group">
                    <summary id="faq1Q" class="font-bold text-slate-800 cursor-pointer list-none flex items-center justify-between">
                        <span>Qual è la formula per convertire la pendenza del tetto da percentuale a gradi?</span>
                        <span class="text-slate-600 group-open:rotate-180 transition-transform">▼</span>
                    </summary>
                    <p id="faq1A" class="mt-2 text-slate-600 leading-relaxed text-xs">
                        Per convertire la percentuale in gradi: <code>Gradi = arctan(Pendenza % / 100) × (180 / π)</code>. Ad esempio, una pendenza del 35% corrisponde a circa 19.3°.
                    </p>
                </details>

                <details class="bg-white rounded-2xl p-3.5 sm:p-4 border border-slate-200 group">
                    <summary id="faq2Q" class="font-bold text-slate-800 cursor-pointer list-none flex items-center justify-between">
                        <span>Qual è la pendenza minima consigliata per un tetto in tegole?</span>
                        <span class="text-slate-600 group-open:rotate-180 transition-transform">▼</span>
                    </summary>
                    <p id="faq2A" class="mt-2 text-slate-600 leading-relaxed text-xs">
                        Per tegole tradizionali (marsigliesi, portoghesi) la pendenza minima è solitamente compresa tra il <strong>30% e il 35%</strong> (circa 17°-19°). Per le lamiere grecate o pannelli coibentati si può scendere fino al <strong>7-10%</strong> con guaina idonea.
                    </p>
                </details>

                <details class="bg-white rounded-2xl p-3.5 sm:p-4 border border-slate-200 group">
                    <summary id="faq3Q" class="font-bold text-slate-800 cursor-pointer list-none flex items-center justify-between">
                        <span>Come si calcola la superficie effettiva di una falda?</span>
                        <span class="text-slate-600 group-open:rotate-180 transition-transform">▼</span>
                    </summary>
                    <p id="faq3A" class="mt-2 text-slate-600 leading-relaxed text-xs">
                        La superficie reale si calcola moltiplicando la <strong>lunghezza reale della trave inclinata</strong> (inclusi gli sporti di gronda) per la <strong>lunghezza del fabbricato lungo la linea di gronda</strong>.
                    </p>
                </details>

                <details class="bg-white rounded-2xl p-3.5 sm:p-4 border border-slate-200 group">
                    <summary id="faq4Q" class="font-bold text-slate-800 cursor-pointer list-none flex items-center justify-between">
                        <span>Cos'è lo sporto di gronda e come influisce sulla trave?</span>
                        <span class="text-slate-600 group-open:rotate-180 transition-transform">▼</span>
                    </summary>
                    <p id="faq4A" class="mt-2 text-slate-600 leading-relaxed text-xs">
                        Lo sporto di gronda è la porzione di tetto che sporge oltre il perimetro esterno dei muri per proteggere la facciata dall'acqua piovana. Va sommato alla lunghezza inclinata teorica della trave per determinare la lunghezza d'acquisto del legname.
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
        let currentMode = 'direct'; // 'direct' (Base + Height) or 'reverse' (Slope% + Base)
        let currentUnit = 'cm'; // 'cm' or 'm'

        function setUnit(u) {{
            if (currentUnit === u) return;
            const b = parseFloat(document.getElementById('inputBase').value) || 0;
            const h = parseFloat(document.getElementById('inputHeight').value) || 0;
            
            if (u === 'm') {{
                document.getElementById('inputBase').value = (b / 100).toFixed(2);
                document.getElementById('inputHeight').value = (h / 100).toFixed(2);
                document.getElementById('baseUnitTag').textContent = 'm';
                document.getElementById('heightUnitTag').textContent = 'm';
            }} else {{
                document.getElementById('inputBase').value = Math.round(b * 100);
                document.getElementById('inputHeight').value = Math.round(h * 100);
                document.getElementById('baseUnitTag').textContent = 'cm';
                document.getElementById('heightUnitTag').textContent = 'cm';
            }}

            currentUnit = u;
            document.getElementById('unitBtnCm').className = (u === 'cm') 
                ? 'px-2.5 py-1 rounded-lg bg-white shadow-2xs text-amber-700 transition' 
                : 'px-2.5 py-1 rounded-lg text-slate-600 hover:text-slate-900 transition';
            document.getElementById('unitBtnM').className = (u === 'm') 
                ? 'px-2.5 py-1 rounded-lg bg-white shadow-2xs text-amber-700 transition' 
                : 'px-2.5 py-1 rounded-lg text-slate-600 hover:text-slate-900 transition';

            calculateRoof();
        }}

        function switchMode(mode) {{
            currentMode = mode;
            const dirBtn = document.getElementById('modeDirectBtn');
            const revBtn = document.getElementById('modeReverseBtn');
            const dirGrp = document.getElementById('modeDirectGroup');
            const revGrp = document.getElementById('modeReverseGroup');

            if (mode === 'direct') {{
                dirBtn.className = 'flex-1 py-1.5 sm:py-2 rounded-xl bg-white text-amber-700 shadow-sm transition active:scale-95 text-center';
                revBtn.className = 'flex-1 py-1.5 sm:py-2 rounded-xl text-slate-600 hover:text-slate-900 transition active:scale-95 text-center';
                dirGrp.classList.remove('hidden');
                revGrp.classList.add('hidden');
            }} else {{
                revBtn.className = 'flex-1 py-1.5 sm:py-2 rounded-xl bg-white text-amber-700 shadow-sm transition active:scale-95 text-center';
                dirBtn.className = 'flex-1 py-1.5 sm:py-2 rounded-xl text-slate-600 hover:text-slate-900 transition active:scale-95 text-center';
                revGrp.classList.remove('hidden');
                dirGrp.classList.add('hidden');
            }}
            calculateRoof();
        }}

        function syncSlider(field, val) {{
            if (field === 'base') {{
                document.getElementById('inputBase').value = (currentUnit === 'm') ? (val / 100).toFixed(2) : val;
            }} else if (field === 'height') {{
                document.getElementById('inputHeight').value = (currentUnit === 'm') ? (val / 100).toFixed(2) : val;
            }} else if (field === 'slopePct') {{
                document.getElementById('inputSlopePct').value = val;
            }}
            calculateRoof();
        }}

        function applyPreset(targetSlopePct) {{
            if (currentMode !== 'reverse') {{
                switchMode('reverse');
            }}
            document.getElementById('inputSlopePct').value = targetSlopePct;
            document.getElementById('sliderSlopePct').value = Math.min(120, targetSlopePct);
            calculateRoof();
        }}

        function calculateRoof() {{
            let baseInput = parseFloat(document.getElementById('inputBase').value) || 0;
            // Convert to cm internally
            let baseCm = (currentUnit === 'm') ? baseInput * 100 : baseInput;
            if (baseCm <= 0) baseCm = 100;

            let slopePct = 0;
            let heightCm = 0;

            if (currentMode === 'direct') {{
                let heightInput = parseFloat(document.getElementById('inputHeight').value) || 0;
                heightCm = (currentUnit === 'm') ? heightInput * 100 : heightInput;
                slopePct = (heightCm / baseCm) * 100;
            }} else {{
                slopePct = parseFloat(document.getElementById('inputSlopePct').value) || 0;
                heightCm = (slopePct / 100) * baseCm;
                // Update direct height input for consistency
                document.getElementById('inputHeight').value = (currentUnit === 'm') ? (heightCm / 100).toFixed(2) : Math.round(heightCm);
            }}

            const angleRad = Math.atan(heightCm / baseCm);
            const angleDeg = angleRad * (180 / Math.PI);

            // Overhang in cm
            const overhangCm = parseFloat(document.getElementById('inputOverhang').value) || 0;
            // Building length in meters
            const roofLengthM = parseFloat(document.getElementById('inputRoofLength').value) || 10;

            // Rafter (hypotenuse) length
            const rafterTheoreticalCm = Math.sqrt((baseCm * baseCm) + (heightCm * heightCm));
            const rafterTotalCm = rafterTheoreticalCm + overhangCm;
            const rafterTotalM = rafterTotalCm / 100;

            // Total slope surface in m2
            const roofAreaM2 = rafterTotalM * roofLengthM;

            // Update KPI DOM
            document.getElementById('valSlopePct').textContent = slopePct.toFixed(1) + '%';
            document.getElementById('valRatio').textContent = `Rapporto 1:${{(100 / slopePct).toFixed(1)}}`;
            document.getElementById('valAngleDeg').textContent = angleDeg.toFixed(1) + '°';
            document.getElementById('valRafterLength').textContent = (rafterTotalCm >= 1000) 
                ? (rafterTotalCm / 100).toFixed(2) + ' m' 
                : rafterTotalCm.toFixed(1) + ' cm';
            document.getElementById('valOverhangNote').textContent = `Incluso sporto ${{overhangCm}} cm`;
            document.getElementById('valRoofArea').textContent = roofAreaM2.toFixed(1) + ' m²';
            document.getElementById('valLengthNote').textContent = `Su facciata ${{roofLengthM.toFixed(1)}} m`;

            // Update Status Badge
            updateRoofStatus(angleDeg, slopePct);

            // Render Section SVG
            renderRoofSvg(baseCm, heightCm, overhangCm, angleDeg, rafterTheoreticalCm);
        }}

        function updateRoofStatus(deg, pct) {{
            const t = TRANSLATIONS[currentLang] || TRANSLATIONS['it'];
            const banner = document.getElementById('statusBanner');
            const title = document.getElementById('statusTitle');
            const tag = document.getElementById('statusTag');
            const desc = document.getElementById('statusDesc');

            if (pct < 18) {{
                // Low pitch
                banner.className = 'p-3 sm:p-4 rounded-2xl border transition-colors duration-200 flex items-start gap-3 bg-blue-50/80 border-blue-200 text-blue-900';
                title.textContent = t.status_warn_title;
                tag.textContent = t.status_warn_tag;
                tag.className = 'text-[9px] sm:text-[10px] font-bold px-2 py-0.5 rounded-full bg-blue-200/60 uppercase tracking-wide shrink-0';
                desc.textContent = t.status_warn_desc;
            }} else if (pct > 50) {{
                // Steep alpine
                banner.className = 'p-3 sm:p-4 rounded-2xl border transition-colors duration-200 flex items-start gap-3 bg-indigo-50/80 border-indigo-200 text-indigo-900';
                title.textContent = t.status_high_title;
                tag.textContent = t.status_high_tag;
                tag.className = 'text-[9px] sm:text-[10px] font-bold px-2 py-0.5 rounded-full bg-indigo-200/60 uppercase tracking-wide shrink-0';
                desc.textContent = t.status_high_desc;
            }} else {{
                // Optimal tile
                banner.className = 'p-3 sm:p-4 rounded-2xl border transition-colors duration-200 flex items-start gap-3 bg-amber-50/80 border-amber-200 text-amber-900';
                title.textContent = t.status_opt_title;
                tag.textContent = t.status_opt_tag;
                tag.className = 'text-[9px] sm:text-[10px] font-bold px-2 py-0.5 rounded-full bg-amber-200/60 uppercase tracking-wide shrink-0';
                desc.textContent = t.status_opt_desc;
            }}
        }}

        function renderRoofSvg(baseCm, heightCm, overhangCm, angleDeg, rafterTheoreticalCm) {{
            const svg = document.getElementById('roofSvgCanvas');
            if (!svg) return;

            if (!rafterTheoreticalCm) {{
                rafterTheoreticalCm = Math.sqrt((baseCm * baseCm) + (heightCm * heightCm));
            }}

            // Coordinate space: 500w x 240h
            // Origin corner at bottom-left: x=60, y=190
            const ox = 70;
            const oy = 190;
            const maxW = 340;
            const maxH = 140;

            const scale = Math.min(maxW / baseCm, maxH / Math.max(heightCm, baseCm * 0.15));
            const drawBaseW = baseCm * scale;
            const drawH = heightCm * scale;
            const drawOverhang = overhangCm * scale;

            const xEave = ox - (drawOverhang * Math.cos(angleDeg * Math.PI / 180));
            const yEave = oy + (drawOverhang * Math.sin(angleDeg * Math.PI / 180));
            const xWall = ox;
            const yWall = oy;
            const xRidge = ox + drawBaseW;
            const yRidge = oy - drawH;

            svg.innerHTML = `
                <!-- Ground / Wall baseline -->
                <line x1="30" y1="${{oy}}" x2="470" y2="${{oy}}" stroke="#cbd5e1" stroke-width="1.5" stroke-dasharray="4 3" />
                
                <!-- Shaded Roof Slope Wedge -->
                <polygon points="${{xWall}},${{yWall}} ${{xRidge}},${{yRidge}} ${{xRidge}},${{yWall}}" fill="#fef3c7" fill-opacity="0.6" stroke="#f59e0b" stroke-width="1" />
                
                <!-- Main Rafter Timber (incl. Eave Overhang) -->
                <line x1="${{xEave}}" y1="${{yEave}}" x2="${{xRidge}}" y2="${{yRidge}}" stroke="#d97706" stroke-width="6" stroke-linecap="round" />
                
                <!-- Vertical Ridge Pillar (Height H) -->
                <line x1="${{xRidge}}" y1="${{yRidge}}" x2="${{xRidge}}" y2="${{yWall}}" stroke="#e11d48" stroke-width="2.5" stroke-linecap="round" />
                <circle cx="${{xRidge}}" cy="${{yRidge}}" r="4" fill="#e11d48" />

                <!-- Eave point marker -->
                <circle cx="${{xEave}}" cy="${{yEave}}" r="3.5" fill="#d97706" />

                <!-- Horizontal Base Dimension (Run L) -->
                <line x1="${{xWall}}" y1="${{oy + 18}}" x2="${{xRidge}}" y2="${{oy + 18}}" stroke="#475569" stroke-width="1.5" />
                <line x1="${{xWall}}" y1="${{oy + 12}}" x2="${{xWall}}" y2="${{oy + 24}}" stroke="#475569" stroke-width="1.5" />
                <line x1="${{xRidge}}" y1="${{oy + 12}}" x2="${{xRidge}}" y2="${{oy + 24}}" stroke="#475569" stroke-width="1.5" />
                <text x="${{(xWall + xRidge) / 2}}" y="${{oy + 32}}" fill="#334155" font-size="11" font-weight="bold" font-family="'JetBrains Mono', monospace" text-anchor="middle">L: ${{baseCm.toFixed(0)}} cm</text>

                <!-- Vertical Height Dimension (H) -->
                <text x="${{xRidge + 12}}" y="${{(yRidge + yWall) / 2 + 4}}" fill="#e11d48" font-size="11" font-weight="bold" font-family="'JetBrains Mono', monospace" text-anchor="start">H: ${{heightCm.toFixed(0)}} cm</text>

                <!-- Slope Incline Label on Rafter -->
                <text x="${{(xWall + xRidge) / 2 - 10}}" y="${{(yRidge + yWall) / 2 - 12}}" fill="#92400e" font-size="11" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle" transform="rotate(${{-angleDeg}}, ${{(xWall + xRidge) / 2}}, ${{(yRidge + yWall) / 2}})">Trave: ${{((rafterTheoreticalCm + overhangCm) >= 1000 ? ((rafterTheoreticalCm + overhangCm)/100).toFixed(2)+'m' : (rafterTheoreticalCm + overhangCm).toFixed(0)+'cm')}} (${{angleDeg.toFixed(1)}}°)</text>

                <!-- Angle Arc -->
                <path d="M ${{xWall + 32}} ${{yWall}} A 32 32 0 0 0 ${{xWall + 32 * Math.cos(angleDeg * Math.PI / 180)}} ${{yWall - 32 * Math.sin(angleDeg * Math.PI / 180)}}" fill="none" stroke="#f59e0b" stroke-width="2" />
            `;
        }}

        function changeLanguage(lang) {{
            currentLang = lang;
            const t = TRANSLATIONS[lang] || TRANSLATIONS['it'];
            if (!t) return;

            document.getElementById('heroBadge').textContent = `OmniBuilding · ${{t.badge || 'Geometria'}}`;
            document.getElementById('heroTitle').textContent = t.hero_title;
            document.getElementById('heroDesc').textContent = t.hero_desc;
            document.getElementById('modeDirectBtn').textContent = t.mode_direct;
            document.getElementById('modeReverseBtn').textContent = t.mode_reverse;
            document.getElementById('unitLabel').textContent = t.unit_label;
            document.getElementById('baseLabel').querySelector('span:last-child').textContent = t.base_label;
            document.getElementById('heightLabel').querySelector('span:last-child').textContent = t.height_label;
            document.getElementById('slopePctLabel').querySelector('span:last-child').textContent = t.slope_pct_label;
            document.getElementById('overhangLabel').textContent = t.overhang_label;
            document.getElementById('roofLengthLabel').textContent = t.roof_length_label;
            document.getElementById('presetsTitle').textContent = t.presets_title;

            document.getElementById('colSlopeLabel').textContent = t.col_slope;
            document.getElementById('colAngleLabel').textContent = t.col_angle;
            document.getElementById('colRafterLabel').textContent = t.col_rafter;
            document.getElementById('colAreaLabel').textContent = t.col_area;
            document.getElementById('schemaTitle').textContent = t.schema_title;
            document.getElementById('schemaScale').textContent = t.schema_scale;
            document.getElementById('ruleTip').innerHTML = t.rule_tip;
            document.getElementById('faqTitle').textContent = t.faq_title;

            calculateRoof();
        }}

        document.addEventListener('DOMContentLoaded', () => {{
            calculateRoof();
        }});
    </script>

    <!-- Header & Footer JS -->
    <script>
        {header_js}
        {footer_js}
    </script>

    <!-- OmniDesk Dock Suite Scripts -->
    <script src="/desk_dock.js" defer></script>
</body>
</html>
"""

out_path = os.path.join(cur_dir, "tetto.html")
with open(out_path, "w", encoding="utf-8") as f:
    f.write(html_code)

print("tetto.html built successfully!")
