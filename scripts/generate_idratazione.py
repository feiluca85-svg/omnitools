#!/usr/bin/env python3
import os
import re

print("Generating HygroBalance Lab (IT & EN)...")

with open('Calcolatore_Pendenza/shelflife.html', 'r', encoding='utf-8') as f:
    it_source = f.read()

with open('Calcolatore_Pendenza/en/shelf-life-calculator.html', 'r', encoding='utf-8') as f:
    en_source = f.read()

dark_styles_it = it_source[it_source.find('<style id="omniDarkStyles">'):it_source.find('</head>')]
dark_styles_en = en_source[en_source.find('<style id="omniDarkStyles">'):en_source.find('</head>')]

def get_top_nav(html, mirror_url, tool_name):
    body_idx = html.find('<body')
    main_idx = html.find('<main')
    top = html[body_idx:main_idx]
    top = re.sub(r'data-mirror-url="[^"]*"', f'data-mirror-url="{mirror_url}"', top)
    top = re.sub(r'<span id="suiteCurrentToolName"[^>]*>[^<]*</span>', f'<span id="suiteCurrentToolName" class="truncate min-w-0">{tool_name}</span>', top)
    return top

top_it = get_top_nav(it_source, "/en/hydration-balance-calculator", "HygroBalance Lab")
top_en = get_top_nav(en_source, "/idratazione", "HygroBalance Lab")

def get_bottom_nav(html):
    footer_idx = html.find('<footer')
    return html[footer_idx:]

bottom_it = get_bottom_nav(it_source)
bottom_en = get_bottom_nav(en_source)

# Head IT
head_it = """<!DOCTYPE html>
<html lang="it">
<head>
    <meta name="google-site-verification" content="MRdbDm9lLhokeD3I0FOpUSOhNaF_2WaveKvu52FxtG4">
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0">
    <title>HygroBalance Lab: Idratazione Reale Impasti &amp; Calcolo Temperatura Acqua T-Base | OmniTools Lab</title>
    <meta name="description" content="Calcolatore termodinamico di idratazione reale: svela l'acqua legata in uova, burro, latte, lievito madre e calcola la temperatura dell'acqua d'impasto (Regola della T-Base) e i grammi esatti di ghiaccio a scaglie.">

    <!-- Canonical & SEO Meta Tags -->
    <link rel="canonical" href="https://www.omnitoolslab.com/idratazione" />
    <link rel="alternate" hreflang="it" href="https://www.omnitoolslab.com/idratazione" />
    <link rel="alternate" hreflang="en-US" href="https://www.omnitoolslab.com/en/hydration-balance-calculator" />
    <link rel="alternate" hreflang="en" href="https://www.omnitoolslab.com/en/hydration-balance-calculator" />
    <link rel="alternate" hreflang="x-default" href="https://www.omnitoolslab.com/en/hydration-balance-calculator" />
    
    <meta name="robots" content="index, follow">
    <meta property="og:type" content="website">
    <meta property="og:title" content="HygroBalance Lab: Idratazione Reale Impasti &amp; Temperatura Acqua">
    <meta property="og:description" content="Bilancia l'acqua biologica nascosta negli ingredienti (uova, burro, latte) e calcola i grammi di ghiaccio per non surriscaldare l'impasto.">
    <meta property="og:url" content="https://www.omnitoolslab.com/idratazione">
    <meta property="og:site_name" content="OmniTools Lab">
    <meta property="og:image" content="https://www.omnitoolslab.com/og-shelflife.png">
    <meta property="og:image:width" content="1200">
    <meta property="og:image:height" content="630">
    <meta property="og:image:type" content="image/png">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:image" content="https://www.omnitoolslab.com/og-shelflife.png">

    <!-- Schema.org JSON-LD Structured Data -->
    <script type="application/ld+json">
[
  {
    "@context": "https://schema.org",
    "@type": "WebApplication",
    "name": "HygroBalance Lab — Idratazione Reale e Temperatura Acqua Impasto",
    "url": "https://www.omnitoolslab.com/idratazione",
    "applicationCategory": "BusinessApplication",
    "operatingSystem": "All",
    "description": "Calcolatore scientifico per panificatori e maestri pizzaioli: calcolo idratazione reale vs apparente (con coefficienti acqua biologica per uova, burro, latte, lieviti), regola termodinamica della T-Base e dosaggio ghiaccio a scaglie.",
    "offers": {
      "@type": "Offer",
      "price": "0",
      "priceCurrency": "EUR"
    },
    "isAccessibleForFree": true
  },
  {
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
      {
        "@type": "ListItem",
        "position": 1,
        "name": "OmniTools Lab",
        "item": "https://www.omnitoolslab.com/"
      },
      {
        "@type": "ListItem",
        "position": 2,
        "name": "OmniFood",
        "item": "https://www.omnitoolslab.com/#food"
      },
      {
        "@type": "ListItem",
        "position": 3,
        "name": "HygroBalance Lab",
        "item": "https://www.omnitoolslab.com/idratazione"
      }
    ]
  },
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "Qual è la differenza tra idratazione apparente e idratazione reale?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "L'idratazione apparente calcola solo l'acqua libera versata nella farina (Acqua / Farina × 100). L'idratazione reale include tutta l'acqua 'nascosta' biologicamente contenuta in altri ingredienti (es. 75% nelle uova, 16% nel burro, 87.5% nel latte) e corregge la farina totale considerando la farina apportata dal lievito madre."
        }
      },
      {
        "@type": "Question",
        "name": "Come si calcola la Temperatura dell'Acqua con la Regola della T-Base?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "La formula termodinamica classica è: T_acqua = (3 × T_target_impasto) - T_ambiente - T_farina - ΔT_attrito_impastatrice. Il ΔT attrito varia a seconda della meccanica: tipicamente +9°C per la spirale, +4°C per le braccia tuffanti, +3°C per la forcella e +1°C a mano."
        }
      },
      {
        "@type": "Question",
        "name": "Perché e quando occorre sostituire l'acqua con il ghiaccio a scaglie?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Quando la formula della T-Base restituisce una temperatura dell'acqua inferiore a +4°C (impossibile da ottenere con l'acqua liquida di rubinetto senza congelamento), è indispensabile usare ghiaccio a scaglie. Sfruttando l'entalpia di fusione latente del ghiaccio (80 kcal/kg), una frazione di ghiaccio abbassa rapidamente la temperatura della massa senza bagnarla in eccesso."
        }
      },
      {
        "@type": "Question",
        "name": "Qual è la formula esatta per calcolare i grammi di ghiaccio da usare?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "La formula calorimetrica è: Ghiaccio (g) = [Acqua_totale × (T_rubinetto - T_calcolata)] / (80 + T_rubinetto). La quantità risultante di ghiaccio viene sottratta all'acqua liquida da versare in vasca."
        }
      },
      {
        "@type": "Question",
        "name": "Come incide il lievito madre (pasta madre o Li.Co.Li.) sul conteggio dell'acqua?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "La pasta madre solida al 50% di idratazione apporta 1/3 di acqua e 2/3 di farina. Il lievito naturale liquido (Li.Co.Li. al 100%) apporta metà acqua e metà farina. Il nostro motore scompone matematicamente il lievito madre aggiungendo la frazione acquosa al totale liquidi e la frazione secca al denominatore delle farine."
        }
      }
    ]
  }
]
    </script>

    <!-- Favicon & PWA -->
    <link rel="icon" type="image/svg+xml" href="/favicon.svg">
    <link rel="icon" type="image/png" sizes="32x32" href="/favicon.png">
    <link rel="apple-touch-icon" href="/favicon.png">
    <link rel="manifest" href="manifest-building.json">
    <meta name="theme-color" content="#ea580c">

    <!-- Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600;700&family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
    
    <!-- Tailwind CSS -->
    <link rel="stylesheet" href="/css/omni.min.css">
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    fontFamily: {
                        sans: ['"Plus Jakarta Sans"', 'system-ui', '-apple-system', 'sans-serif'],
                        jakarta: ['"Plus Jakarta Sans"', 'sans-serif'],
                        mono: ['"JetBrains Mono"', 'monospace'],
                    }
                }
            }
        }
    </script>
    <script defer src="/_vercel/insights/script.js"></script>
    <style>
        html, body { overflow-x: clip; }
        @page {
            size: A4 portrait;
            margin: 8mm 10mm 8mm 10mm;
        }
        @media print {
            header, footer, nav,
            .no-print,
            #faqSection, #legalDisclaimerBox, #shareStrip,
            #langSelect, button, input[type=range],
            details, .faq-accordion {
                display: none !important;
            }
            body {
                background-color: #ffffff !important;
                color: #0f172a !important;
                font-size: 10pt !important;
            }
            main {
                max-width: 100% !important;
                padding: 0 !important;
                margin: 0 !important;
            }
            #printHeader {
                display: block !important;
            }
        }
        .tabular-nums {
            font-variant-numeric: tabular-nums;
        }
    </style>
""" + dark_styles_it

# Main IT
main_it = """
    <!-- Main Container -->
    <main class="max-w-5xl mx-auto px-3 sm:px-6 py-2.5 sm:py-5 flex-1 w-full space-y-6 sm:space-y-8">

        <!-- PRINT ONLY: Professional Technical Header Cartiglio -->
        <div id="printHeader" class="hidden print:block border-b-2 border-slate-900 pb-3 mb-4">
            <div class="flex justify-between items-start gap-4">
                <div>
                    <div class="flex items-center gap-2 mb-1">
                        <span class="px-2 py-0.5 bg-orange-600 text-white font-bold text-[10px] rounded uppercase tracking-wider">OmniTools Lab — SCHEDA TECNICA A4</span>
                        <span class="text-[11px] font-bold text-slate-600">OmniFood • Igrometria &amp; Termodinamica Impasti</span>
                    </div>
                    <h1 class="font-jakarta text-xl font-extrabold text-slate-900 leading-tight" id="printSheetTitle">Scheda Calcolo Idratazione Reale, Regola T-Base &amp; Ghiaccio</h1>
                    <p class="text-[10px] text-slate-500 mt-0.5">Bilanciamento Acqua Biologica Legata • Entalpia di Fusione Ghiaccio (80 kcal/kg)</p>
                </div>
                <div class="text-right text-[10px] text-slate-600 shrink-0">
                    <div class="font-bold text-slate-900 text-xs">omnitoolslab.com</div>
                    <div>Data stampa: <span id="printTimestamp"></span></div>
                </div>
            </div>
            <div class="mt-2.5 pt-2 border-t border-slate-200 grid grid-cols-4 gap-2 text-[10px]" id="printInputsSummary"></div>
        </div>

        <!-- Hero Section -->
        <section class="text-center space-y-2 no-print">
            <div class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-orange-100 text-orange-800 text-xs font-bold shadow-2xs">
                <span>💧</span> <span>Idratazione Reale vs Apparente</span> • <span>🌡️</span> <span>Regola T-Base</span> • <span>❄️</span> <span>Ghiaccio a Scaglie</span>
            </div>
            <h1 id="heroTitle" class="font-jakarta text-2xl sm:text-3xl lg:text-4xl font-black text-slate-900 tracking-tight">
                HygroBalance Lab
            </h1>
            <p id="heroSubtitle" class="text-slate-600 text-xs sm:text-sm max-w-2xl mx-auto leading-relaxed">
                Bilanciamento scientifico dell'acqua negli impasti: calcola l'<strong>idratazione reale</strong> (includendo l'acqua legata in uova, burro e latte) e la <strong>temperatura esatta dell'acqua</strong> con dosaggio del ghiaccio per evitare il surriscaldamento della maglia glutinica.
            </p>
        </section>

        <!-- Main Card: 2 Columns (Form Controls + Thermodynamic Blueprint) -->
        <div class="bg-white rounded-3xl border border-slate-200 border-t-4 border-t-orange-600 shadow-sm p-4 sm:p-7 space-y-6">

            <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 items-start">
                
                <!-- Left Column: Controls (lg:col-span-6) -->
                <div class="lg:col-span-6 space-y-5">
                    
                    <!-- Section 1: Flours & Free Water -->
                    <div class="p-4 bg-slate-50/80 rounded-2xl border border-slate-200/80 space-y-3">
                        <div class="flex items-center justify-between">
                            <span class="text-xs font-bold text-slate-800 uppercase tracking-wider flex items-center gap-1.5">
                                <span>🌾</span> <span>Base Farina &amp; Acqua Libera</span>
                            </span>
                            <span class="text-[10px] font-mono text-slate-500">Ricetta Base</span>
                        </div>

                        <div class="grid grid-cols-2 gap-3">
                            <div>
                                <label class="text-[11px] font-bold text-slate-700 block">Farina Pura Aggiunta (g)</label>
                                <div class="flex items-center mt-1">
                                    <button type="button" onclick="stepVal('inpFlourGrams', -100, 100)" class="w-8 h-9 bg-slate-200 hover:bg-slate-300 font-bold rounded-l-lg text-slate-700">-</button>
                                    <input type="number" id="inpFlourGrams" value="1000" min="100" step="50" oninput="calculateHygroBalance()" class="w-full h-9 text-center text-xs font-mono font-bold border-y border-slate-200 focus:ring-0 bg-white">
                                    <button type="button" onclick="stepVal('inpFlourGrams', 100, 100)" class="w-8 h-9 bg-slate-200 hover:bg-slate-300 font-bold rounded-r-lg text-slate-700">+</button>
                                </div>
                            </div>
                            <div>
                                <label class="text-[11px] font-bold text-blue-700 block">Acqua Libera Versata (g/ml)</label>
                                <div class="flex items-center mt-1">
                                    <button type="button" onclick="stepVal('inpFreeWaterGrams', -25, 0)" class="w-8 h-9 bg-slate-200 hover:bg-slate-300 font-bold rounded-l-lg text-slate-700">-</button>
                                    <input type="number" id="inpFreeWaterGrams" value="600" min="0" step="25" oninput="calculateHygroBalance()" class="w-full h-9 text-center text-xs font-mono font-bold border-y border-slate-200 focus:ring-0 bg-white">
                                    <button type="button" onclick="stepVal('inpFreeWaterGrams', 25, 0)" class="w-8 h-9 bg-slate-200 hover:bg-slate-300 font-bold rounded-r-lg text-slate-700">+</button>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- Section 2: Moist & Biological Ingredients (Hidden Water) -->
                    <div class="p-4 bg-orange-50/50 rounded-2xl border border-orange-200/70 space-y-3">
                        <div class="flex items-center justify-between border-b border-orange-200/60 pb-1.5">
                            <span class="text-xs font-bold text-orange-900 uppercase tracking-wider flex items-center gap-1.5">
                                <span>🥚</span> <span>Ingredienti Umidi (Acqua Nascosta)</span>
                            </span>
                            <span class="text-[10px] font-mono text-orange-700 font-bold">Coefficiente Biologico</span>
                        </div>

                        <div class="grid grid-cols-2 sm:grid-cols-3 gap-2.5">
                            <div>
                                <label class="text-[10px] font-bold text-slate-700 block truncate">Uova Intere (g) <span class="text-slate-400 font-normal">75% H2O</span></label>
                                <input type="number" id="inpHydroEggs" value="100" min="0" step="10" oninput="calculateHygroBalance()" class="w-full mt-0.5 text-xs font-mono font-bold p-1.5 rounded-lg border border-slate-200 bg-white">
                            </div>
                            <div>
                                <label class="text-[10px] font-bold text-slate-700 block truncate">Tuorli (g) <span class="text-slate-400 font-normal">50% H2O</span></label>
                                <input type="number" id="inpHydroYolk" value="0" min="0" step="10" oninput="calculateHygroBalance()" class="w-full mt-0.5 text-xs font-mono font-bold p-1.5 rounded-lg border border-slate-200 bg-white">
                            </div>
                            <div>
                                <label class="text-[10px] font-bold text-slate-700 block truncate">Burro (g) <span class="text-slate-400 font-normal">16% H2O</span></label>
                                <input type="number" id="inpHydroButter" value="80" min="0" step="10" oninput="calculateHygroBalance()" class="w-full mt-0.5 text-xs font-mono font-bold p-1.5 rounded-lg border border-slate-200 bg-white">
                            </div>
                            <div>
                                <label class="text-[10px] font-bold text-slate-700 block truncate">Latte Intero (g) <span class="text-slate-400 font-normal">87.5% H2O</span></label>
                                <input type="number" id="inpHydroMilk" value="0" min="0" step="20" oninput="calculateHygroBalance()" class="w-full mt-0.5 text-xs font-mono font-bold p-1.5 rounded-lg border border-slate-200 bg-white">
                            </div>
                            <div>
                                <label class="text-[10px] font-bold text-slate-700 block truncate">Panna Fresca (g) <span class="text-slate-400 font-normal">60% H2O</span></label>
                                <input type="number" id="inpHydroCream" value="0" min="0" step="20" oninput="calculateHygroBalance()" class="w-full mt-0.5 text-xs font-mono font-bold p-1.5 rounded-lg border border-slate-200 bg-white">
                            </div>
                            <div>
                                <label class="text-[10px] font-bold text-slate-700 block truncate">Miele (g) <span class="text-slate-400 font-normal">18% H2O</span></label>
                                <input type="number" id="inpHydroHoney" value="20" min="0" step="5" oninput="calculateHygroBalance()" class="w-full mt-0.5 text-xs font-mono font-bold p-1.5 rounded-lg border border-slate-200 bg-white">
                            </div>
                        </div>

                        <!-- Sourdough / Preferment -->
                        <div class="pt-2 border-t border-orange-200/40 grid grid-cols-2 gap-3">
                            <div>
                                <label class="text-[10px] font-bold text-slate-700 block">Tipo Lievito Naturale</label>
                                <select id="selSourdoughType" onchange="calculateHygroBalance()" class="w-full mt-0.5 text-xs font-bold p-1.5 rounded-lg border border-slate-200 bg-white">
                                    <option value="none">Nessuno (Solo lievito di birra)</option>
                                    <option value="solid">Pasta Madre Solida (50% idr - 33% H2O)</option>
                                    <option value="licoli">Li.Co.Li. Liquido (100% idr - 50% H2O)</option>
                                </select>
                            </div>
                            <div>
                                <label class="text-[10px] font-bold text-slate-700 block">Grammi Lievito Madre (g)</label>
                                <input type="number" id="inpHydroSourdoughGrams" value="0" min="0" step="25" oninput="calculateHygroBalance()" class="w-full mt-0.5 text-xs font-mono font-bold p-1.5 rounded-lg border border-slate-200 bg-white">
                            </div>
                        </div>
                    </div>

                    <!-- Section 3: Thermodynamic T-Base & Mixer Friction -->
                    <div class="p-4 bg-blue-50/50 rounded-2xl border border-blue-200/70 space-y-3">
                        <div class="flex items-center justify-between border-b border-blue-200/60 pb-1.5">
                            <span class="text-xs font-bold text-blue-900 uppercase tracking-wider flex items-center gap-1.5">
                                <span>🌡️</span> <span>Termodinamica T-Base &amp; Calcolo Ghiaccio</span>
                            </span>
                            <span class="text-[10px] font-mono font-bold text-blue-700">T_acqua = 3×T_target - T_amb - T_far - ΔT</span>
                        </div>

                        <div class="grid grid-cols-3 gap-2">
                            <div>
                                <label class="text-[10px] font-bold text-slate-700 block truncate">Target Impasto (°C)</label>
                                <input type="number" id="inpTempTarget" value="25.0" min="18" max="32" step="0.5" oninput="calculateHygroBalance()" class="w-full mt-0.5 text-xs font-mono font-bold p-1.5 rounded-lg border border-slate-200 bg-white">
                            </div>
                            <div>
                                <label class="text-[10px] font-bold text-slate-700 block truncate">Temp. Ambiente (°C)</label>
                                <input type="number" id="inpTempAmb" value="24.0" min="10" max="42" step="0.5" oninput="calculateHygroBalance()" class="w-full mt-0.5 text-xs font-mono font-bold p-1.5 rounded-lg border border-slate-200 bg-white">
                            </div>
                            <div>
                                <label class="text-[10px] font-bold text-slate-700 block truncate">Temp. Farina (°C)</label>
                                <input type="number" id="inpTempFlour" value="23.0" min="10" max="35" step="0.5" oninput="calculateHygroBalance()" class="w-full mt-0.5 text-xs font-mono font-bold p-1.5 rounded-lg border border-slate-200 bg-white">
                            </div>
                        </div>

                        <div class="grid grid-cols-2 gap-3 pt-1">
                            <div>
                                <label class="text-[10px] font-bold text-slate-700 block">Tipo Impastatrice (Attrito Meccanico)</label>
                                <select id="selMixerFriction" onchange="calculateHygroBalance()" class="w-full mt-0.5 text-xs font-bold p-1.5 rounded-lg border border-slate-200 bg-white">
                                    <option value="9">Spirale (+9°C)</option>
                                    <option value="4">Braccia Tuffanti (+4°C)</option>
                                    <option value="3">Forcella (+3°C)</option>
                                    <option value="6">Planetaria (+6°C)</option>
                                    <option value="1">Impasto a Mano (+1°C)</option>
                                </select>
                            </div>
                            <div>
                                <label class="text-[10px] font-bold text-slate-700 block">Temp. Acqua Rubinetto (°C)</label>
                                <input type="number" id="inpTempTap" value="18.0" min="4" max="30" step="1" oninput="calculateHygroBalance()" class="w-full mt-0.5 text-xs font-mono font-bold p-1.5 rounded-lg border border-slate-200 bg-white">
                            </div>
                        </div>
                    </div>

                    <!-- Action Buttons -->
                    <div class="pt-2 flex flex-wrap gap-2.5 no-print">
                        <button type="button" onclick="copyHygroSpec()" id="btnCopyHygro" class="flex-1 py-2.5 px-4 bg-orange-600 hover:bg-orange-700 active:scale-95 text-white font-bold text-xs rounded-xl transition shadow-sm flex items-center justify-center gap-1.5 cursor-pointer">
                            <span>📋</span> <span>Copia Specifica Igrometrica</span>
                        </button>
                        <button type="button" onclick="exportHygroCsv()" class="py-2.5 px-3.5 bg-slate-100 hover:bg-slate-200 active:scale-95 text-slate-700 font-bold text-xs rounded-xl transition flex items-center gap-1 cursor-pointer">
                            <span>📊</span> <span>CSV</span>
                        </button>
                        <button type="button" onclick="window.print()" class="py-2.5 px-3.5 bg-slate-100 hover:bg-slate-200 active:scale-95 text-slate-700 font-bold text-xs rounded-xl transition flex items-center gap-1 cursor-pointer">
                            <span>🖨️</span> <span>Stampa A4</span>
                        </button>
                    </div>

                </div>

                <!-- Right Column: Visual Blueprint CAD Thermometer & Hydration Dial (lg:col-span-6) -->
                <div class="lg:col-span-6 space-y-4">
                    <div class="flex items-center justify-between">
                        <span class="text-xs font-bold text-slate-700 uppercase tracking-wider flex items-center gap-1.5">
                            <span>❄️</span> <span>Termometro Termodinamico &amp; Bilancia Acqua</span>
                        </span>
                        <span id="badgeIceAlert" class="hidden text-[10px] font-mono font-bold text-rose-700 bg-rose-100 px-2 py-0.5 rounded-full animate-pulse">SOGLIA GHIACCIO ATTIVA</span>
                    </div>

                    <!-- Dual CAD Visual Blueprint SVG -->
                    <div class="bg-slate-900 rounded-2xl p-4 border border-slate-800 shadow-md">
                        <svg class="svg-blueprint w-full h-48 sm:h-56" viewBox="0 0 500 220" role="img" aria-label="Diagramma Termodinamico Acqua e Bilancia Idratazione">
                            <defs>
                                <linearGradient id="gradThermoWater" x1="0" y1="1" x2="0" y2="0">
                                    <stop offset="0%" stop-color="#38bdf8" />
                                    <stop offset="60%" stop-color="#0284c7" />
                                    <stop offset="100%" stop-color="#ef4444" />
                                </linearGradient>
                            </defs>
                            
                            <!-- Thermometer Housing (Left 160px) -->
                            <rect x="35" y="25" width="22" height="150" rx="11" fill="#1e293b" stroke="#475569" stroke-width="2" />
                            <circle cx="46" cy="175" r="18" fill="#0284c7" stroke="#475569" stroke-width="2" />
                            
                            <!-- Liquid Column -->
                            <rect id="svgThermoFluid" x="40" y="70" width="12" height="105" rx="6" fill="#38bdf8" />
                            
                            <!-- Scale Ticks -->
                            <line x1="62" y1="35" x2="72" y2="35" stroke="#94a3b8" stroke-width="1.5" />
                            <text x="76" y="38" fill="#94a3b8" font-size="9" font-family="'JetBrains Mono', monospace">30°C</text>
                            
                            <line x1="62" y1="75" x2="72" y2="75" stroke="#94a3b8" stroke-width="1.5" />
                            <text x="76" y="78" fill="#94a3b8" font-size="9" font-family="'JetBrains Mono', monospace">20°C</text>

                            <line x1="62" y1="115" x2="72" y2="115" stroke="#94a3b8" stroke-width="1.5" />
                            <text x="76" y="118" fill="#94a3b8" font-size="9" font-family="'JetBrains Mono', monospace">10°C</text>

                            <line x1="62" y1="140" x2="75" y2="140" stroke="#38bdf8" stroke-width="2" />
                            <text x="80" y="143" fill="#38bdf8" font-size="9" font-weight="bold" font-family="'JetBrains Mono', monospace">4°C (Soglia Ghiaccio)</text>

                            <text id="svgTxtWaterTemp" x="46" y="210" fill="#38bdf8" font-size="12" font-weight="bold" font-family="'JetBrains Mono', monospace" text-anchor="middle">T: 19.0°C</text>

                            <!-- Balance Dial / Hydration Stack (Right 300px) -->
                            <rect x="180" y="30" width="300" height="34" rx="6" fill="#1e293b" stroke="#334155" />
                            <rect id="svgBarFreeWater" x="182" y="32" width="180" height="30" rx="4" fill="#0284c7" />
                            <rect id="svgBarBoundWater" x="364" y="32" width="60" height="30" rx="4" fill="#f59e0b" />
                            <text id="svgTxtHydrationSplit" x="330" y="52" fill="#ffffff" font-size="10" font-weight="bold" font-family="'JetBrains Mono', monospace" text-anchor="middle">Libera: 600g | Legata: 102g</text>

                            <!-- Dual Hydration Badges -->
                            <rect x="180" y="75" width="145" height="50" rx="8" fill="#0f172a" stroke="#334155" />
                            <text x="252" y="93" fill="#94a3b8" font-size="9" font-weight="bold" text-anchor="middle">IDRATAZIONE APPARENTE</text>
                            <text id="svgTxtApparentPct" x="252" y="116" fill="#38bdf8" font-size="18" font-weight="bold" font-family="'JetBrains Mono', monospace" text-anchor="middle">60.0%</text>

                            <rect x="335" y="75" width="145" height="50" rx="8" fill="#0f172a" stroke="#ea580c" />
                            <text x="407" y="93" fill="#fb923c" font-size="9" font-weight="bold" text-anchor="middle">IDRATAZIONE REALE</text>
                            <text id="svgTxtRealPct" x="407" y="116" fill="#f97316" font-size="18" font-weight="bold" font-family="'JetBrains Mono', monospace" text-anchor="middle">70.2%</text>

                            <!-- Ice Substitution Callout Banner -->
                            <rect id="svgIceBox" x="180" y="135" width="300" height="55" rx="8" fill="#1e293b" stroke="#0284c7" stroke-dasharray="3 3" />
                            <text id="svgTxtIceTitle" x="330" y="155" fill="#38bdf8" font-size="10" font-weight="bold" font-family="'JetBrains Mono', monospace" text-anchor="middle">Dosaggio Acqua di Rubinetto</text>
                            <text id="svgTxtIceDetails" x="330" y="175" fill="#ffffff" font-size="11" font-weight="bold" font-family="'JetBrains Mono', monospace" text-anchor="middle">Nessun ghiaccio richiesto (T &gt;= 4°C)</text>
                        </svg>
                    </div>

                    <!-- Water & Ice Production Breakdown Table -->
                    <div class="border border-slate-200 rounded-2xl overflow-hidden bg-white shadow-xs">
                        <div class="bg-slate-100/80 px-4 py-2 border-b border-slate-200 flex justify-between items-center text-xs font-bold text-slate-800">
                            <span>Dosaggio Liquidi in Vasca</span>
                            <span class="text-[10px] font-mono text-slate-500">T-Base Impastatrice</span>
                        </div>
                        <div class="divide-y divide-slate-100 text-xs">
                            <div class="p-2.5 flex justify-between items-center bg-blue-50/40">
                                <div>
                                    <strong class="text-blue-950 block">Acqua Liquida da Versare</strong>
                                    <span id="subLiquidWater" class="text-[10px] text-blue-600">A temperatura di rubinetto</span>
                                </div>
                                <span id="resLiquidWaterGrams" class="font-mono font-black text-blue-700 text-sm">600 g</span>
                            </div>
                            <div id="rowIceResult" class="p-2.5 flex justify-between items-center bg-sky-50/40">
                                <div>
                                    <strong class="text-sky-950 block">Ghiaccio a Scaglie (Sostituzione)</strong>
                                    <span id="subIce" class="text-[10px] text-sky-600">Entalpia fusione latente 80 kcal/kg</span>
                                </div>
                                <span id="resIceGrams" class="font-mono font-black text-sky-700 text-sm">0 g</span>
                            </div>
                            <div class="p-2 flex justify-between items-center">
                                <div>
                                    <span class="text-slate-800 block">Acqua Biologica Nascosta</span>
                                    <span id="subBoundWater" class="text-[10px] text-slate-500">Apportata da uova, burro, miele</span>
                                </div>
                                <span id="resBoundWaterGrams" class="font-mono font-bold text-orange-600">102 g</span>
                            </div>
                            <div class="p-2 flex justify-between items-center">
                                <div>
                                    <span class="text-slate-800 block">Acqua Totale Reale nel Glutine</span>
                                    <span class="text-[10px] text-slate-500">Acqua Libera + Acqua Nascosta</span>
                                </div>
                                <span id="resTotalWaterGrams" class="font-mono font-bold text-slate-900">702 g</span>
                            </div>
                        </div>
                    </div>

                    <!-- Output KPI Grid -->
                    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 pt-1">
                        <div class="p-2.5 bg-slate-50 rounded-xl border border-slate-200 text-center">
                            <span class="text-[9px] uppercase font-bold text-slate-500 block">T-Acqua Calcolata</span>
                            <span id="kpiCalculatedTemp" class="text-sm font-mono font-black text-blue-600">19.0°C</span>
                        </div>
                        <div class="p-2.5 bg-slate-50 rounded-xl border border-slate-200 text-center">
                            <span class="text-[9px] uppercase font-bold text-slate-500 block">Idratazione Reale</span>
                            <span id="kpiRealHydration" class="text-sm font-mono font-black text-orange-600">70.2%</span>
                        </div>
                        <div class="p-2.5 bg-slate-50 rounded-xl border border-slate-200 text-center">
                            <span class="text-[9px] uppercase font-bold text-slate-500 block">Acqua Nascosta</span>
                            <span id="kpiBoundWaterPct" class="text-sm font-mono font-black text-slate-800">+10.2%</span>
                        </div>
                        <div class="p-2.5 bg-slate-50 rounded-xl border border-slate-200 text-center">
                            <span class="text-[9px] uppercase font-bold text-slate-500 block">Ghiaccio da Pesare</span>
                            <span id="kpiIceWeight" class="text-sm font-mono font-black text-sky-700">0 g</span>
                        </div>
                    </div>

                </div>

            </div>

        </div>

        <!-- FAQ Section: 5 Technical Expandable Details -->
        <section id="faqSection" class="no-print bg-white rounded-3xl border border-slate-200/90 shadow-xs p-5 sm:p-7 space-y-4">
            <div class="flex items-center gap-2.5 mb-1">
                <span class="text-xl">❓</span>
                <h2 class="text-base sm:text-lg font-black text-slate-900 font-jakarta flex items-center gap-2" id="faqTitle">
                    <span>Domande Frequenti su Idratazione Reale, Regola T-Base &amp; Ghiaccio</span>
                </h2>
                <span class="text-[10px] font-extrabold uppercase px-2 py-0.5 rounded-full bg-slate-100 text-slate-600 border border-slate-200">FAQ</span>
            </div>

            <div id="faqContainer" class="space-y-3">
                <details class="group bg-slate-50/80 hover:bg-slate-50 rounded-2xl border border-slate-200/80 p-4 transition duration-150">
                    <summary class="flex justify-between items-center font-bold text-xs sm:text-sm text-slate-900 cursor-pointer list-none select-none">
                        <span>Qual è la differenza tra idratazione apparente e idratazione reale?</span>
                        <span class="text-slate-400 group-open:rotate-180 transition-transform duration-200">▼</span>
                    </summary>
                    <p class="mt-2 text-xs text-slate-600 leading-relaxed">
                        L'idratazione apparente calcola solo l'acqua libera versata nella farina (Acqua / Farina × 100). L'idratazione reale include tutta l'acqua 'nascosta' biologicamente contenuta in altri ingredienti (es. 75% nelle uova, 16% nel burro, 87.5% nel latte) e corregge la farina totale considerando la farina apportata dal lievito madre.
                    </p>
                </details>

                <details class="group bg-slate-50/80 hover:bg-slate-50 rounded-2xl border border-slate-200/80 p-4 transition duration-150">
                    <summary class="flex justify-between items-center font-bold text-xs sm:text-sm text-slate-900 cursor-pointer list-none select-none">
                        <span>Come si calcola la Temperatura dell'Acqua con la Regola della T-Base?</span>
                        <span class="text-slate-400 group-open:rotate-180 transition-transform duration-200">▼</span>
                    </summary>
                    <p class="mt-2 text-xs text-slate-600 leading-relaxed">
                        La formula termodinamica classica è: T_acqua = (3 × T_target_impasto) - T_ambiente - T_farina - ΔT_attrito_impastatrice. Il ΔT attrito varia a seconda della meccanica: tipicamente +9°C per la spirale, +4°C per le braccia tuffanti, +3°C per la forcella e +1°C a mano.
                    </p>
                </details>

                <details class="group bg-slate-50/80 hover:bg-slate-50 rounded-2xl border border-slate-200/80 p-4 transition duration-150">
                    <summary class="flex justify-between items-center font-bold text-xs sm:text-sm text-slate-900 cursor-pointer list-none select-none">
                        <span>Perché e quando occorre sostituire l'acqua con il ghiaccio a scaglie?</span>
                        <span class="text-slate-400 group-open:rotate-180 transition-transform duration-200">▼</span>
                    </summary>
                    <p class="mt-2 text-xs text-slate-600 leading-relaxed">
                        Quando la formula della T-Base restituisce una temperatura dell'acqua inferiore a +4°C (impossibile da ottenere con l'acqua liquida di rubinetto senza congelamento), è indispensabile usare ghiaccio a scaglie. Sfruttando l'entalpia di fusione latente del ghiaccio (80 kcal/kg), una frazione di ghiaccio abbassa rapidamente la temperatura della massa senza bagnarla in eccesso.
                    </p>
                </details>

                <details class="group bg-slate-50/80 hover:bg-slate-50 rounded-2xl border border-slate-200/80 p-4 transition duration-150">
                    <summary class="flex justify-between items-center font-bold text-xs sm:text-sm text-slate-900 cursor-pointer list-none select-none">
                        <span>Qual è la formula esatta per calcolare i grammi di ghiaccio da usare?</span>
                        <span class="text-slate-400 group-open:rotate-180 transition-transform duration-200">▼</span>
                    </summary>
                    <p class="mt-2 text-xs text-slate-600 leading-relaxed">
                        La formula calorimetrica è: Ghiaccio (g) = [Acqua_totale × (T_rubinetto - T_calcolata)] / (80 + T_rubinetto). La quantità risultante di ghiaccio viene sottratta all'acqua liquida da versare in vasca.
                    </p>
                </details>

                <details class="group bg-slate-50/80 hover:bg-slate-50 rounded-2xl border border-slate-200/80 p-4 transition duration-150">
                    <summary class="flex justify-between items-center font-bold text-xs sm:text-sm text-slate-900 cursor-pointer list-none select-none">
                        <span>Come incide il lievito madre sul conteggio dell'acqua?</span>
                        <span class="text-slate-400 group-open:rotate-180 transition-transform duration-200">▼</span>
                    </summary>
                    <p class="mt-2 text-xs text-slate-600 leading-relaxed">
                        La pasta madre solida al 50% di idratazione apporta 1/3 di acqua e 2/3 di farina. Il lievito naturale liquido (Li.Co.Li. al 100%) apporta metà acqua e metà farina. Il nostro motore scompone matematicamente il lievito madre aggiungendo la frazione acquosa al totale liquidi e la frazione secca al denominatore delle farine.
                    </p>
                </details>
            </div>
        </section>

        <!-- Legal Disclaimer & Safe Harbor -->
        <section id="legalDisclaimerBox" class="bg-amber-50/60 rounded-3xl border border-amber-200/90 shadow-xs p-5 sm:p-6 text-[11px] sm:text-xs text-slate-700 leading-relaxed space-y-2">
            <div class="font-extrabold text-slate-900 uppercase tracking-wider text-[11px] flex items-center gap-1.5">
                <span>⚖️</span> <span>Avvertenza Termodinamica, Reologia Impasti &amp; Esclusione di Responsabilità</span>
            </div>
            <p>
                <strong>1. Modello teorico e tolleranze fisiche:</strong> Le formule calorimetriche e le costanti di umidità biologica costituiscono modelli ideali di fisica tecnica. La temperatura reale dell'impasto può subire variazioni in funzione della velocità dell'impastatrice, del tempo di lavorazione, del volume di carico della vasca e della temperatura del motore.
            </p>
            <p>
                <strong>2. Manleva:</strong> OmniTools Lab e i suoi autori declinano ogni responsabilità per difetti strutturali dell'impasto, denaturazione delle proteine glutiniche o perdite di produzione.
            </p>
        </section>

    </main>
"""

# Script IT
script_it = """
    <script>
        function stepVal(id, delta, min) {
            const inp = document.getElementById(id);
            if (!inp) return;
            let v = parseFloat(inp.value) || 0;
            v = Math.max(min, v + delta);
            inp.value = v.toFixed(0);
            calculateHygroBalance();
        }

        function calculateHygroBalance() {
            const flourAdded = parseFloat(document.getElementById('inpFlourGrams').value) || 1000;
            const freeWater = parseFloat(document.getElementById('inpFreeWaterGrams').value) || 0;

            const eggs = parseFloat(document.getElementById('inpHydroEggs').value) || 0;
            const yolk = parseFloat(document.getElementById('inpHydroYolk').value) || 0;
            const butter = parseFloat(document.getElementById('inpHydroButter').value) || 0;
            const milk = parseFloat(document.getElementById('inpHydroMilk').value) || 0;
            const cream = parseFloat(document.getElementById('inpHydroCream').value) || 0;
            const honey = parseFloat(document.getElementById('inpHydroHoney').value) || 0;

            const sourdoughType = document.getElementById('selSourdoughType').value;
            const sourdoughGrams = parseFloat(document.getElementById('inpHydroSourdoughGrams').value) || 0;

            let sourdoughWater = 0;
            let sourdoughFlour = 0;
            if (sourdoughType === 'solid') {
                sourdoughWater = sourdoughGrams * (1.0 / 3.0);
                sourdoughFlour = sourdoughGrams * (2.0 / 3.0);
            } else if (sourdoughType === 'licoli') {
                sourdoughWater = sourdoughGrams * 0.5;
                sourdoughFlour = sourdoughGrams * 0.5;
            }

            // Bound water calculations
            const boundEggs = eggs * 0.75;
            const boundYolk = yolk * 0.50;
            const boundButter = butter * 0.16;
            const boundMilk = milk * 0.875;
            const boundCream = cream * 0.60;
            const boundHoney = honey * 0.18;

            const totalBoundWater = boundEggs + boundYolk + boundButter + boundMilk + boundCream + boundHoney + sourdoughWater;
            const totalWaterReal = freeWater + totalBoundWater;
            const totalFlourReal = flourAdded + sourdoughFlour;

            const apparentHydrationPct = (freeWater / flourAdded) * 100.0;
            const realHydrationPct = (totalWaterReal / totalFlourReal) * 100.0;

            // Thermodynamic T-Base
            const tTarget = parseFloat(document.getElementById('inpTempTarget').value) || 25;
            const tAmb = parseFloat(document.getElementById('inpTempAmb').value) || 24;
            const tFlour = parseFloat(document.getElementById('inpTempFlour').value) || 23;
            const deltaFriction = parseFloat(document.getElementById('selMixerFriction').value) || 9;
            const tTap = parseFloat(document.getElementById('inpTempTap').value) || 18;

            const tWaterReq = (3 * tTarget) - tAmb - tFlour - deltaFriction;

            // Ice calculation if tWaterReq < 4°C
            let iceGrams = 0;
            let liquidWaterGrams = freeWater;

            const badgeIce = document.getElementById('badgeIceAlert');
            const svgIceBox = document.getElementById('svgIceBox');
            const svgTxtIceTitle = document.getElementById('svgTxtIceTitle');
            const svgTxtIceDetails = document.getElementById('svgTxtIceDetails');

            if (tWaterReq < 4.0 && freeWater > 0) {
                // Calorimetry formula: M_ice = [M_water * (T_tap - T_calc)] / (80 + T_tap)
                iceGrams = Math.round((freeWater * (tTap - tWaterReq)) / (80.0 + tTap));
                iceGrams = Math.min(freeWater, Math.max(0, iceGrams));
                liquidWaterGrams = Math.round(freeWater - iceGrams);

                if (badgeIce) badgeIce.classList.remove('hidden');
                if (svgIceBox) {
                    svgIceBox.setAttribute('stroke', '#38bdf8');
                    svgIceBox.setAttribute('fill', 'rgba(2, 132, 199, 0.25)');
                }
                if (svgTxtIceTitle) svgTxtIceTitle.textContent = `⚠️ Richiesto Ghiaccio a Scaglie: ${iceGrams} g`;
                if (svgTxtIceDetails) svgTxtIceDetails.textContent = `Acqua Liquida: ${liquidWaterGrams}g | Ghiaccio: ${iceGrams}g`;
            } else {
                if (badgeIce) badgeIce.classList.add('hidden');
                if (svgIceBox) {
                    svgIceBox.setAttribute('stroke', '#334155');
                    svgIceBox.setAttribute('fill', '#1e293b');
                }
                if (svgTxtIceTitle) svgTxtIceTitle.textContent = `Dosaggio Acqua di Rubinetto`;
                if (svgTxtIceDetails) svgTxtIceDetails.textContent = `Versare ${freeWater}g a ${tWaterReq.toFixed(1)}°C (Nessun ghiaccio)`;
            }

            // Update UI Table
            document.getElementById('resLiquidWaterGrams').textContent = liquidWaterGrams + ' g';
            document.getElementById('resIceGrams').textContent = iceGrams + ' g';
            document.getElementById('resBoundWaterGrams').textContent = Math.round(totalBoundWater) + ' g';
            document.getElementById('resTotalWaterGrams').textContent = Math.round(totalWaterReal) + ' g';

            // KPI Grid
            document.getElementById('kpiCalculatedTemp').textContent = tWaterReq.toFixed(1) + '°C';
            document.getElementById('kpiRealHydration').textContent = realHydrationPct.toFixed(1) + '%';
            const diffPct = realHydrationPct - apparentHydrationPct;
            document.getElementById('kpiBoundWaterPct').textContent = (diffPct >= 0 ? '+' : '') + diffPct.toFixed(1) + '%';
            document.getElementById('kpiIceWeight').textContent = iceGrams + ' g';

            // SVG Updates
            document.getElementById('svgTxtApparentPct').textContent = apparentHydrationPct.toFixed(1) + '%';
            document.getElementById('svgTxtRealPct').textContent = realHydrationPct.toFixed(1) + '%';
            document.getElementById('svgTxtWaterTemp').textContent = `T: ${tWaterReq.toFixed(1)}°C`;
            document.getElementById('svgTxtHydrationSplit').textContent = `Libera: ${Math.round(freeWater)}g | Nascosta: ${Math.round(totalBoundWater)}g`;

            // Adjust thermometer fluid visual height
            const clampedTemp = Math.max(-5, Math.min(35, tWaterReq));
            const fluidHeight = Math.round(20 + ((clampedTemp + 5) / 40.0) * 120);
            const svgFluid = document.getElementById('svgThermoFluid');
            if (svgFluid) {
                svgFluid.setAttribute('height', fluidHeight);
                svgFluid.setAttribute('y', 175 - fluidHeight);
                if (tWaterReq < 4.0) {
                    svgFluid.setAttribute('fill', '#38bdf8');
                } else if (tWaterReq > 24.0) {
                    svgFluid.setAttribute('fill', '#ef4444');
                } else {
                    svgFluid.setAttribute('fill', '#10b981');
                }
            }

            // Adjust Bar Free vs Bound Water
            const totalWaterWidth = 296;
            const freeFrac = totalWaterReal > 0 ? (freeWater / totalWaterReal) : 1;
            const wFree = Math.round(totalWaterWidth * freeFrac);
            const wBound = Math.max(0, totalWaterWidth - wFree);

            const barFree = document.getElementById('svgBarFreeWater');
            const barBound = document.getElementById('svgBarBoundWater');
            if (barFree && barBound) {
                barFree.setAttribute('width', wFree);
                barBound.setAttribute('x', 182 + wFree);
                barBound.setAttribute('width', wBound);
            }

            // Print summary
            const printSummary = document.getElementById('printInputsSummary');
            if (printSummary) {
                printSummary.innerHTML = `
                    <div><span class="text-slate-400 block">Farina Totale:</span><strong>${Math.round(totalFlourReal)} g</strong></div>
                    <div><span class="text-slate-400 block">Idratazione Reale:</span><strong>${realHydrationPct.toFixed(1)}%</strong></div>
                    <div><span class="text-slate-400 block">T-Acqua Calcolata:</span><strong>${tWaterReq.toFixed(1)}°C</strong></div>
                    <div><span class="text-slate-400 block">Ghiaccio Richiesto:</span><strong>${iceGrams} g</strong></div>
                `;
            }
            const printTs = document.getElementById('printTimestamp');
            if (printTs) printTs.textContent = new Date().toLocaleDateString('it-IT');
        }

        function copyHygroSpec() {
            const app = document.getElementById('svgTxtApparentPct').textContent;
            const real = document.getElementById('svgTxtRealPct').textContent;
            const tw = document.getElementById('kpiCalculatedTemp').textContent;
            const ice = document.getElementById('kpiIceWeight').textContent;
            const txt = `HygroBalance Lab: Idratazione Apparente: ${app} | Idratazione Reale: ${real} | Temp. Acqua Impasto: ${tw} | Ghiaccio a Scaglie: ${ice}`;
            navigator.clipboard.writeText(txt).then(() => {
                const btn = document.getElementById('btnCopyHygro');
                const old = btn.innerHTML;
                btn.innerHTML = '<span>✓</span> <span>Dati Copiati!</span>';
                setTimeout(() => { btn.innerHTML = old; }, 2000);
            });
        }

        function exportHygroCsv() {
            const rows = [
                ['Parametro', 'Valore', 'Unità', 'Descrizione'],
                ['Farina Base Aggiunta', document.getElementById('inpFlourGrams').value, 'g', 'Farina pura'],
                ['Acqua Libera Versata', document.getElementById('inpFreeWaterGrams').value, 'g', 'Acqua liquida'],
                ['Acqua Nascosta (Uova, Burro, ecc.)', document.getElementById('resBoundWaterGrams').textContent, 'g', 'Acqua biologica legata'],
                ['Acqua Totale Reale', document.getElementById('resTotalWaterGrams').textContent, 'g', 'Totale idratazione reale'],
                ['Idratazione Apparente', document.getElementById('svgTxtApparentPct').textContent, '%', 'Solo acqua su farina'],
                ['Idratazione Reale', document.getElementById('svgTxtRealPct').textContent, '%', 'Totale acqua su totale farina'],
                ['Temperatura Target Impasto', document.getElementById('inpTempTarget').value, '°C', 'Temperatura ottimale'],
                ['Temperatura Acqua Calcolata', document.getElementById('kpiCalculatedTemp').textContent, '°C', 'Regola T-Base'],
                ['Ghiaccio a Scaglie Necessario', document.getElementById('kpiIceWeight').textContent, 'g', 'Entalpia 80 kcal/kg'],
                ['Acqua Liquida Effettiva', document.getElementById('resLiquidWaterGrams').textContent, 'g', 'Acqua di rubinetto da dosare']
            ];
            const csv = rows.map(r => r.map(v => `"${String(v).replace(/"/g, '""')}"`).join(',')).join('\\n');
            const blob = new Blob([csv], { type: 'text/csv;charset=utf-8;' });
            const a = document.createElement('a');
            a.href = URL.createObjectURL(blob);
            a.download = 'omnitools_idratazione_termodinamica.csv';
            a.click();
        }

        document.addEventListener('DOMContentLoaded', () => {
            calculateHygroBalance();
        });
    </script>
"""

full_it = head_it + "\n</head>\n" + top_it + "\n" + main_it + "\n" + script_it + "\n" + bottom_it

with open('Calcolatore_Pendenza/idratazione.html', 'w', encoding='utf-8') as f:
    f.write(full_it)

print(f"Generated Calcolatore_Pendenza/idratazione.html ({len(full_it)} bytes)")
