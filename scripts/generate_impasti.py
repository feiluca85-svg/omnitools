#!/usr/bin/env python3
import os
import re

print("Generating BatchScaler Pro (IT & EN)...")

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

top_it = get_top_nav(it_source, "/en/batch-scaler-calculator", "BatchScaler Pro")
top_en = get_top_nav(en_source, "/impasti", "BatchScaler Pro")

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
    <title>BatchScaler Pro: Baker's % &amp; Scalatore Lotti Impasti Laboratorio | OmniTools Lab</title>
    <meta name="description" content="Calcolatore professionale di impasti e panificazione basato su Baker's Percentage (Farina 100%): scalatura lotti per peso target, numero pezzi crudo/cotto o ingrediente limitante, con gestione sfrido e calo peso cottura.">

    <!-- Canonical & SEO Meta Tags -->
    <link rel="canonical" href="https://www.omnitoolslab.com/impasti" />
    <link rel="alternate" hreflang="it" href="https://www.omnitoolslab.com/impasti" />
    <link rel="alternate" hreflang="en-US" href="https://www.omnitoolslab.com/en/batch-scaler-calculator" />
    <link rel="alternate" hreflang="en" href="https://www.omnitoolslab.com/en/batch-scaler-calculator" />
    <link rel="alternate" hreflang="x-default" href="https://www.omnitoolslab.com/en/batch-scaler-calculator" />
    
    <meta name="robots" content="index, follow">
    <meta property="og:type" content="website">
    <meta property="og:title" content="BatchScaler Pro: Calcolatore Impasti &amp; Baker's Percentage">
    <meta property="og:description" content="Scala qualsiasi ricetta professionale di panificazione, pizzeria e pasticceria con percentuali del panificatore, calo cottura e distinta di produzione banco.">
    <meta property="og:url" content="https://www.omnitoolslab.com/impasti">
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
    "name": "BatchScaler Pro — Calcolatore Impasti e Baker's Percentage",
    "url": "https://www.omnitoolslab.com/impasti",
    "applicationCategory": "BusinessApplication",
    "operatingSystem": "All",
    "description": "Software di calcolo professionale per forni, pizzerie e laboratori alimentari basato sulla percentuale del panificatore (Baker's %), gestione sfrido macchina, calo peso in cottura e distinta di produzione esportabile.",
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
        "name": "BatchScaler Pro",
        "item": "https://www.omnitoolslab.com/impasti"
      }
    ]
  },
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "Cos'è la Percentuale del Panificatore (Baker's Percentage)?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "La Percentuale del Panificatore è il sistema di notazione internazionale usato nell'arte bianca in cui il peso totale della farina rappresenta sempre il 100%. Tutti gli altri ingredienti (acqua, sale, lievito, grassi, zuccheri) sono espressi come frazione percentuale rispetto alla farina."
        }
      },
      {
        "@type": "Question",
        "name": "Come si calcola la farina totale partendo dal peso desiderato dell'impasto?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "La formula esatta è: Farina Totale = (Peso Desiderato × (1 + Sfrido% / 100)) / (Somma di tutte le Baker's % / 100). Una volta nota la farina base, si moltiplica ciascuna percentuale per determinare i grammi di ciascun ingrediente."
        }
      },
      {
        "@type": "Question",
        "name": "Cos'è lo sfrido di impasto dell'impastatrice?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Lo sfrido è la quota fisiologica di pasta che resta adesa alle pareti della vasca, alla spirale o che si perde durante lo staglio e la spezzatura. In ambito artigianale varia tipicamente tra l'1% e il 3%."
        }
      },
      {
        "@type": "Question",
        "name": "Come incide il calo peso in cottura sul pane finito?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Durante la cottura, l'evaporazione dell'acqua determina una perdita di peso tra il 10% e il 25% a seconda della pezzatura, della temperatura del forno e del tipo di crosta. Per ottenere una pagnotta cotta da 500g con un calo del 15%, la pastella cruda deve pesare circa 588g."
        }
      },
      {
        "@type": "Question",
        "name": "Come funziona la modalità Ingrediente Limitante?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Se in magazzino disponi di una quantità limitata di un ingrediente (ad esempio solo 450g di burro o 1200g di farina speciale), il sistema ricalcola l'intera ricetta mantenendo rigorosamente costanti tutte le proporzioni percentuali."
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
                        <span class="text-[11px] font-bold text-slate-600">OmniFood • Laboratorio Arte Bianca</span>
                    </div>
                    <h1 class="font-jakarta text-xl font-extrabold text-slate-900 leading-tight" id="printSheetTitle">Distinta Base di Produzione Impasto &amp; Scalatura Lotto</h1>
                    <p class="text-[10px] text-slate-500 mt-0.5">Metodologia: Baker's Percentage (Totale Farine = 100%) • Sfrido &amp; Calo Cottura</p>
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
                <span>🥖</span> <span>Baker's % (Farina = 100%)</span> • <span>⚖️</span> <span>Sfrido &amp; Calo Cottura</span> • <span>📦</span> <span>Scheda Banco A4</span>
            </div>
            <h1 id="heroTitle" class="font-jakarta text-2xl sm:text-3xl lg:text-4xl font-black text-slate-900 tracking-tight">
                BatchScaler Pro
            </h1>
            <p id="heroSubtitle" class="text-slate-600 text-xs sm:text-sm max-w-2xl mx-auto leading-relaxed">
                Scalatore professionale per panificazione, pizzeria e pasticceria: scala la ricetta partendo da <strong>massa totale</strong>, <strong>numero pezzi</strong> o <strong>ingrediente limitante</strong> con ripartizione grafica CAD.
            </p>
        </section>

        <!-- Main Card: 2 Columns (Form Controls + CAD Layered Blueprint) -->
        <div class="bg-white rounded-3xl border border-slate-200 border-t-4 border-t-orange-600 shadow-sm p-4 sm:p-7 space-y-6">

            <!-- 3 Scaling Modes Tabs -->
            <div class="no-print">
                <label class="text-xs font-bold text-slate-700 uppercase tracking-wider block mb-2">Modalità di Calcolo Scalatura</label>
                <div class="grid grid-cols-3 gap-2 p-1.5 bg-slate-100 rounded-2xl border border-slate-200 text-xs font-bold">
                    <button type="button" id="tabModeDough" onclick="setScalerMode('dough')" class="py-2 px-3 rounded-xl transition bg-white text-orange-600 shadow-xs text-center cursor-pointer">
                        🎯 Massa Totale
                    </button>
                    <button type="button" id="tabModePieces" onclick="setScalerMode('pieces')" class="py-2 px-3 rounded-xl transition text-slate-600 hover:text-slate-900 text-center cursor-pointer">
                        🔢 Pezzatura × N°
                    </button>
                    <button type="button" id="tabModeLimit" onclick="setScalerMode('limit')" class="py-2 px-3 rounded-xl transition text-slate-600 hover:text-slate-900 text-center cursor-pointer">
                        📦 Ingrediente Limite
                    </button>
                </div>
            </div>

            <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 items-start">
                
                <!-- Left Column: Controls (lg:col-span-6) -->
                <div class="lg:col-span-6 space-y-5">
                    
                    <!-- Dynamic Scaling Target Input -->
                    <div class="p-4 bg-orange-50/60 rounded-2xl border border-orange-200/80 space-y-3">
                        <div id="targetDoughBox" class="space-y-1.5">
                            <label class="text-[11px] font-bold text-slate-700 block">Massa Totale Impasto Desiderata (kg)</label>
                            <div class="flex items-center">
                                <button type="button" onclick="stepVal('inpTargetDoughKg', -0.5, 0.1)" class="w-9 h-9 bg-slate-200 hover:bg-slate-300 font-bold rounded-l-lg text-slate-700">-</button>
                                <input type="number" id="inpTargetDoughKg" value="5.0" min="0.1" step="0.1" oninput="calculateBatchScaler()" class="w-full h-9 text-center text-xs font-mono font-bold border-y border-slate-200 focus:ring-0 bg-white">
                                <button type="button" onclick="stepVal('inpTargetDoughKg', 0.5, 0.1)" class="w-9 h-9 bg-slate-200 hover:bg-slate-300 font-bold rounded-r-lg text-slate-700">+</button>
                            </div>
                        </div>

                        <div id="targetPiecesBox" class="hidden grid grid-cols-2 gap-3">
                            <div>
                                <label class="text-[11px] font-bold text-slate-700 block">Numero Pezzi (Pz)</label>
                                <input type="number" id="inpNumPieces" value="10" min="1" step="1" oninput="calculateBatchScaler()" class="w-full mt-1 text-xs font-mono font-bold p-2 rounded-xl border border-slate-200 bg-white">
                            </div>
                            <div>
                                <label class="text-[11px] font-bold text-slate-700 block">Peso Crudo Singolo (g)</label>
                                <input type="number" id="inpPieceWeightRaw" value="550" min="10" step="10" oninput="calculateBatchScaler()" class="w-full mt-1 text-xs font-mono font-bold p-2 rounded-xl border border-slate-200 bg-white">
                            </div>
                        </div>

                        <div id="targetLimitBox" class="hidden grid grid-cols-2 gap-3">
                            <div>
                                <label class="text-[11px] font-bold text-slate-700 block">Ingrediente Limitante</label>
                                <select id="selLimitIngredient" onchange="calculateBatchScaler()" class="w-full mt-1 text-xs font-bold p-2 rounded-xl border border-slate-200 bg-white">
                                    <option value="flour">Farina Base</option>
                                    <option value="water">Acqua</option>
                                    <option value="butter">Grassi / Burro</option>
                                    <option value="sugar">Zucchero</option>
                                </select>
                            </div>
                            <div>
                                <label class="text-[11px] font-bold text-slate-700 block">Quantità Disponibile (g)</label>
                                <input type="number" id="inpLimitQtyGrams" value="1000" min="1" step="50" oninput="calculateBatchScaler()" class="w-full mt-1 text-xs font-mono font-bold p-2 rounded-xl border border-slate-200 bg-white">
                            </div>
                        </div>

                        <!-- Technical Machine Loss & Baking Loss -->
                        <div class="grid grid-cols-2 gap-3 pt-1 border-t border-orange-200/50">
                            <div>
                                <div class="flex justify-between items-center">
                                    <label class="text-[10px] font-bold text-slate-600 block">Sfrido Macchina (%)</label>
                                    <span class="text-[9px] font-mono text-slate-400">1-3% tipico</span>
                                </div>
                                <input type="number" id="inpMachineWastePct" value="2.0" min="0" max="15" step="0.5" oninput="calculateBatchScaler()" class="w-full mt-1 text-xs font-mono font-bold p-1.5 rounded-lg border border-slate-200 bg-white">
                            </div>
                            <div>
                                <div class="flex justify-between items-center">
                                    <label class="text-[10px] font-bold text-slate-600 block">Calo Peso Cottura (%)</label>
                                    <span class="text-[9px] font-mono text-slate-400">12-20% tipico</span>
                                </div>
                                <input type="number" id="inpBakeLossPct" value="15.0" min="0" max="35" step="0.5" oninput="calculateBatchScaler()" class="w-full mt-1 text-xs font-mono font-bold p-1.5 rounded-lg border border-slate-200 bg-white">
                            </div>
                        </div>
                    </div>

                    <!-- Baker's % Recipe Formula Parameters -->
                    <div class="space-y-3">
                        <div class="flex items-center justify-between border-b border-slate-100 pb-2">
                            <span class="text-xs font-bold text-slate-800 uppercase tracking-wider flex items-center gap-1.5">
                                <span>🌾</span> <span>Formula Baker's % (Farina Totale = 100%)</span>
                            </span>
                            <span class="text-[10px] font-mono font-bold text-orange-600 bg-orange-100 px-2 py-0.5 rounded-full">Standard Arte Bianca</span>
                        </div>

                        <!-- Multi-Flour Blend -->
                        <div class="p-3 bg-slate-50/70 rounded-xl border border-slate-200/70 space-y-2">
                            <div class="text-[11px] font-bold text-slate-700 flex justify-between">
                                <span>Blend Farine (Farina 1 + Farina 2 = 100%)</span>
                                <span id="lblFlourBlendRatio" class="font-mono text-orange-600">70% / 30%</span>
                            </div>
                            <div class="grid grid-cols-2 gap-2">
                                <div>
                                    <label class="text-[10px] text-slate-500 block">Farina 1 (es. Tipo 0 / W 300) %</label>
                                    <input type="number" id="inpFlour1Pct" value="70" min="0" max="100" step="5" oninput="syncFlourBlend(1)" class="w-full mt-0.5 text-xs font-mono font-bold p-1.5 rounded-lg border border-slate-200 bg-white">
                                </div>
                                <div>
                                    <label class="text-[10px] text-slate-500 block">Farina 2 (es. Integrale / Farro) %</label>
                                    <input type="number" id="inpFlour2Pct" value="30" min="0" max="100" step="5" oninput="syncFlourBlend(2)" class="w-full mt-0.5 text-xs font-mono font-bold p-1.5 rounded-lg border border-slate-200 bg-white">
                                </div>
                            </div>
                        </div>

                        <!-- Baker's Percentages Inputs -->
                        <div class="grid grid-cols-2 sm:grid-cols-3 gap-2.5">
                            <div>
                                <label class="text-[10px] font-bold text-blue-700 block truncate">Acqua (Idratazione %)</label>
                                <input type="number" id="inpWaterPct" value="65.0" min="30" max="110" step="0.5" oninput="calculateBatchScaler()" class="w-full mt-1 text-xs font-mono font-bold p-2 rounded-xl border border-blue-200 bg-blue-50/30">
                            </div>
                            <div>
                                <label class="text-[10px] font-bold text-slate-700 block truncate">Sale (% su farina)</label>
                                <input type="number" id="inpSaltPct" value="2.2" min="0" max="5" step="0.1" oninput="calculateBatchScaler()" class="w-full mt-1 text-xs font-mono font-bold p-2 rounded-xl border border-slate-200">
                            </div>
                            <div>
                                <label class="text-[10px] font-bold text-amber-700 block truncate">Lievito Fresco (%)</label>
                                <input type="number" id="inpYeastPct" value="1.5" min="0.1" max="10" step="0.1" oninput="calculateBatchScaler()" class="w-full mt-1 text-xs font-mono font-bold p-2 rounded-xl border border-slate-200">
                            </div>
                            <div>
                                <label class="text-[10px] font-bold text-slate-700 block truncate">Olio / Burro / Grassi (%)</label>
                                <input type="number" id="inpFatPct" value="3.0" min="0" max="80" step="0.5" oninput="calculateBatchScaler()" class="w-full mt-1 text-xs font-mono font-bold p-2 rounded-xl border border-slate-200">
                            </div>
                            <div>
                                <label class="text-[10px] font-bold text-slate-700 block truncate">Zucchero / Malto (%)</label>
                                <input type="number" id="inpSugarPct" value="1.0" min="0" max="50" step="0.5" oninput="calculateBatchScaler()" class="w-full mt-1 text-xs font-mono font-bold p-2 rounded-xl border border-slate-200">
                            </div>
                            <div>
                                <label class="text-[10px] font-bold text-slate-700 block truncate">Inclusioni / Semi (%)</label>
                                <input type="number" id="inpInclusionsPct" value="0.0" min="0" max="50" step="1" oninput="calculateBatchScaler()" class="w-full mt-1 text-xs font-mono font-bold p-2 rounded-xl border border-slate-200">
                            </div>
                        </div>

                    </div>

                    <!-- Action Buttons -->
                    <div class="pt-2 flex flex-wrap gap-2.5 no-print">
                        <button type="button" onclick="copyBatchSpec()" id="btnCopyBatch" class="flex-1 py-2.5 px-4 bg-orange-600 hover:bg-orange-700 active:scale-95 text-white font-bold text-xs rounded-xl transition shadow-sm flex items-center justify-center gap-1.5 cursor-pointer">
                            <span>📋</span> <span>Copia Scheda Ricetta</span>
                        </button>
                        <button type="button" onclick="exportBatchCsv()" class="py-2.5 px-3.5 bg-slate-100 hover:bg-slate-200 active:scale-95 text-slate-700 font-bold text-xs rounded-xl transition flex items-center gap-1 cursor-pointer">
                            <span>📊</span> <span>CSV Banco</span>
                        </button>
                        <button type="button" onclick="window.print()" class="py-2.5 px-3.5 bg-slate-100 hover:bg-slate-200 active:scale-95 text-slate-700 font-bold text-xs rounded-xl transition flex items-center gap-1 cursor-pointer">
                            <span>🖨️</span> <span>Stampa A4</span>
                        </button>
                    </div>

                </div>

                <!-- Right Column: Visual Blueprint CAD & Distinta Banco (lg:col-span-6) -->
                <div class="lg:col-span-6 space-y-4">
                    <div class="flex items-center justify-between">
                        <span class="text-xs font-bold text-slate-700 uppercase tracking-wider flex items-center gap-1.5">
                            <span>📐</span> <span>Blueprint Tecnico Stratificato Impasto</span>
                        </span>
                        <span id="lblSumBakerPct" class="text-[10px] font-mono font-bold text-orange-600 bg-orange-100 px-2 py-0.5 rounded-full">Tot: 172.7%</span>
                    </div>

                    <!-- SVG Layered CAD Visual Blueprint -->
                    <div class="bg-slate-900 rounded-2xl p-4 border border-slate-800 shadow-md">
                        <svg class="svg-blueprint w-full h-44 sm:h-52" viewBox="0 0 500 200" role="img" aria-label="Diagramma Stratificato Massa e Idratazione">
                            <defs>
                                <linearGradient id="gradFlour" x1="0" y1="0" x2="1" y2="0">
                                    <stop offset="0%" stop-color="#f59e0b" stop-opacity="0.9" />
                                    <stop offset="100%" stop-color="#d97706" stop-opacity="0.9" />
                                </linearGradient>
                                <linearGradient id="gradWater" x1="0" y1="0" x2="1" y2="0">
                                    <stop offset="0%" stop-color="#38bdf8" stop-opacity="0.9" />
                                    <stop offset="100%" stop-color="#0284c7" stop-opacity="0.9" />
                                </linearGradient>
                                <linearGradient id="gradOther" x1="0" y1="0" x2="1" y2="0">
                                    <stop offset="0%" stop-color="#10b981" stop-opacity="0.9" />
                                    <stop offset="100%" stop-color="#059669" stop-opacity="0.9" />
                                </linearGradient>
                            </defs>
                            
                            <!-- Background Grid -->
                            <line x1="20" y1="30" x2="480" y2="30" stroke="#334155" stroke-dasharray="2 2" stroke-width="1" />
                            <line x1="20" y1="110" x2="480" y2="110" stroke="#334155" stroke-dasharray="2 2" stroke-width="1" />
                            <line x1="20" y1="160" x2="480" y2="160" stroke="#334155" stroke-dasharray="2 2" stroke-width="1" />

                            <!-- Segmented Bar 1: Flour vs Water vs Other -->
                            <rect id="svgBarFlour" x="30" y="45" width="240" height="40" rx="4" fill="url(#gradFlour)" />
                            <rect id="svgBarWater" x="272" y="45" width="156" height="40" rx="4" fill="url(#gradWater)" />
                            <rect id="svgBarOther" x="430" y="45" width="40" height="40" rx="4" fill="url(#gradOther)" />

                            <!-- Bar Text Labels -->
                            <text id="svgTxtFlour" x="150" y="70" fill="#ffffff" font-size="11" font-weight="bold" font-family="'JetBrains Mono', monospace" text-anchor="middle">FARINA 100%</text>
                            <text id="svgTxtWater" x="350" y="70" fill="#ffffff" font-size="11" font-weight="bold" font-family="'JetBrains Mono', monospace" text-anchor="middle">ACQUA 65%</text>
                            <text id="svgTxtOther" x="450" y="70" fill="#ffffff" font-size="9" font-weight="bold" font-family="'JetBrains Mono', monospace" text-anchor="middle">+</text>

                            <!-- Bottom Dimensioning Line -->
                            <line x1="30" y1="100" x2="470" y2="100" stroke="#94a3b8" stroke-width="1.5" />
                            <line x1="30" y1="95" x2="30" y2="105" stroke="#94a3b8" stroke-width="1.5" />
                            <line x1="470" y1="95" x2="470" y2="105" stroke="#94a3b8" stroke-width="1.5" />
                            <text id="svgTxtTotalDough" x="250" y="118" fill="#38bdf8" font-size="11" font-weight="bold" font-family="'JetBrains Mono', monospace" text-anchor="middle">Massa Totale Impastatrice: 5.10 kg (con 2% sfrido)</text>

                            <!-- Baking Loss Indicator -->
                            <rect x="30" y="135" width="374" height="20" rx="3" fill="#ea580c" opacity="0.8" />
                            <rect x="406" y="135" width="64" height="20" rx="3" fill="#64748b" opacity="0.5" stroke="#94a3b8" stroke-dasharray="2 2" />
                            <text id="svgTxtBakedYield" x="217" y="149" fill="#ffffff" font-size="10" font-weight="bold" font-family="'JetBrains Mono', monospace" text-anchor="middle">Resa Cotta Stimata (-15% calo): 4.25 kg</text>
                            <text x="438" y="149" fill="#cbd5e1" font-size="9" font-family="'JetBrains Mono', monospace" text-anchor="middle">Calo</text>
                        </svg>
                    </div>

                    <!-- Distinta Base di Produzione (Tabella Banco) -->
                    <div class="border border-slate-200 rounded-2xl overflow-hidden bg-white shadow-xs">
                        <div class="bg-slate-100/80 px-4 py-2 border-b border-slate-200 flex justify-between items-center text-xs font-bold text-slate-800">
                            <span>Distinta Ingredienti per il Banco</span>
                            <span class="text-[10px] font-mono text-slate-500">Massa Netta: <strong id="lblNetDoughHeader" class="text-slate-900">5.00 kg</strong></span>
                        </div>
                        <div class="divide-y divide-slate-100 text-xs">
                            <div class="p-2.5 flex justify-between items-center bg-amber-50/40">
                                <div>
                                    <strong class="text-slate-900 block">Farina 1 (Base)</strong>
                                    <span id="subFlour1" class="text-[10px] text-slate-500">70% del blend farine</span>
                                </div>
                                <span id="resFlour1Grams" class="font-mono font-black text-slate-900 text-sm">2,067 g</span>
                            </div>
                            <div class="p-2.5 flex justify-between items-center bg-amber-50/40">
                                <div>
                                    <strong class="text-slate-900 block">Farina 2 (Blend)</strong>
                                    <span id="subFlour2" class="text-[10px] text-slate-500">30% del blend farine</span>
                                </div>
                                <span id="resFlour2Grams" class="font-mono font-black text-slate-900 text-sm">886 g</span>
                            </div>
                            <div class="p-2.5 flex justify-between items-center bg-blue-50/40">
                                <div>
                                    <strong class="text-blue-900 block">Acqua (Totale Idratazione)</strong>
                                    <span id="subWater" class="text-[10px] text-blue-600">65.0% su farina</span>
                                </div>
                                <span id="resWaterGrams" class="font-mono font-black text-blue-700 text-sm">1,920 g</span>
                            </div>
                            <div class="p-2 flex justify-between items-center">
                                <div>
                                    <span class="text-slate-800 block">Sale Marino Fine</span>
                                    <span id="subSalt" class="text-[10px] text-slate-500">2.2% su farina</span>
                                </div>
                                <span id="resSaltGrams" class="font-mono font-bold text-slate-800">65 g</span>
                            </div>
                            <div class="p-2 flex justify-between items-center">
                                <div>
                                    <span class="text-slate-800 block">Lievito Fresco</span>
                                    <span id="subYeast" class="text-[10px] text-slate-500">1.5% su farina</span>
                                </div>
                                <span id="resYeastGrams" class="font-mono font-bold text-slate-800">44 g</span>
                            </div>
                            <div id="rowFat" class="p-2 flex justify-between items-center">
                                <div>
                                    <span class="text-slate-800 block">Grassi / Olio / Burro</span>
                                    <span id="subFat" class="text-[10px] text-slate-500">3.0% su farina</span>
                                </div>
                                <span id="resFatGrams" class="font-mono font-bold text-slate-800">89 g</span>
                            </div>
                            <div id="rowSugar" class="p-2 flex justify-between items-center">
                                <div>
                                    <span class="text-slate-800 block">Zucchero / Malto</span>
                                    <span id="subSugar" class="text-[10px] text-slate-500">1.0% su farina</span>
                                </div>
                                <span id="resSugarGrams" class="font-mono font-bold text-slate-800">30 g</span>
                            </div>
                        </div>
                    </div>

                    <!-- Output KPI Grid -->
                    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 pt-1">
                        <div class="p-2.5 bg-slate-50 rounded-xl border border-slate-200 text-center">
                            <span class="text-[9px] uppercase font-bold text-slate-500 block">Farina Totale</span>
                            <span id="kpiTotalFlour" class="text-sm font-mono font-black text-slate-900">2.95 kg</span>
                        </div>
                        <div class="p-2.5 bg-slate-50 rounded-xl border border-slate-200 text-center">
                            <span class="text-[9px] uppercase font-bold text-slate-500 block">Massa Vasca</span>
                            <span id="kpiTotalBatch" class="text-sm font-mono font-black text-orange-600">5.10 kg</span>
                        </div>
                        <div class="p-2.5 bg-slate-50 rounded-xl border border-slate-200 text-center">
                            <span class="text-[9px] uppercase font-bold text-slate-500 block">Resa Cotta</span>
                            <span id="kpiBakedYield" class="text-sm font-mono font-black text-emerald-600">4.25 kg</span>
                        </div>
                        <div class="p-2.5 bg-slate-50 rounded-xl border border-slate-200 text-center">
                            <span class="text-[9px] uppercase font-bold text-slate-500 block">Pezzi Stimati</span>
                            <span id="kpiEstimatedPieces" class="text-sm font-mono font-black text-slate-900">~9-10 pz</span>
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
                    <span>Domande Frequenti su Baker's Percentage &amp; Scalatura Lotti</span>
                </h2>
                <span class="text-[10px] font-extrabold uppercase px-2 py-0.5 rounded-full bg-slate-100 text-slate-600 border border-slate-200">FAQ</span>
            </div>

            <div id="faqContainer" class="space-y-3">
                <details class="group bg-slate-50/80 hover:bg-slate-50 rounded-2xl border border-slate-200/80 p-4 transition duration-150">
                    <summary class="flex justify-between items-center font-bold text-xs sm:text-sm text-slate-900 cursor-pointer list-none select-none">
                        <span>Cos'è la Percentuale del Panificatore (Baker's Percentage)?</span>
                        <span class="text-slate-400 group-open:rotate-180 transition-transform duration-200">▼</span>
                    </summary>
                    <p class="mt-2 text-xs text-slate-600 leading-relaxed">
                        La Percentuale del Panificatore è il sistema di notazione internazionale usato nell'arte bianca in cui il peso totale della farina rappresenta sempre il 100%. Tutti gli altri ingredienti (acqua, sale, lievito, grassi, zuccheri) sono espressi come frazione percentuale rispetto alla farina.
                    </p>
                </details>

                <details class="group bg-slate-50/80 hover:bg-slate-50 rounded-2xl border border-slate-200/80 p-4 transition duration-150">
                    <summary class="flex justify-between items-center font-bold text-xs sm:text-sm text-slate-900 cursor-pointer list-none select-none">
                        <span>Come si calcola la farina totale partendo dal peso desiderato dell'impasto?</span>
                        <span class="text-slate-400 group-open:rotate-180 transition-transform duration-200">▼</span>
                    </summary>
                    <p class="mt-2 text-xs text-slate-600 leading-relaxed">
                        La formula esatta è: Farina Totale = (Peso Desiderato × (1 + Sfrido% / 100)) / (Somma di tutte le Baker's % / 100). Una volta nota la farina base, si moltiplica ciascuna percentuale per determinare i grammi di ciascun ingrediente.
                    </p>
                </details>

                <details class="group bg-slate-50/80 hover:bg-slate-50 rounded-2xl border border-slate-200/80 p-4 transition duration-150">
                    <summary class="flex justify-between items-center font-bold text-xs sm:text-sm text-slate-900 cursor-pointer list-none select-none">
                        <span>Cos'è lo sfrido di impasto dell'impastatrice?</span>
                        <span class="text-slate-400 group-open:rotate-180 transition-transform duration-200">▼</span>
                    </summary>
                    <p class="mt-2 text-xs text-slate-600 leading-relaxed">
                        Lo sfrido è la quota fisiologica di pasta che resta adesa alle pareti della vasca, alla spirale o che si perde durante lo staglio e la spezzatura. In ambito artigianale varia tipicamente tra l'1% e il 3%.
                    </p>
                </details>

                <details class="group bg-slate-50/80 hover:bg-slate-50 rounded-2xl border border-slate-200/80 p-4 transition duration-150">
                    <summary class="flex justify-between items-center font-bold text-xs sm:text-sm text-slate-900 cursor-pointer list-none select-none">
                        <span>Come incide il calo peso in cottura sul pane finito?</span>
                        <span class="text-slate-400 group-open:rotate-180 transition-transform duration-200">▼</span>
                    </summary>
                    <p class="mt-2 text-xs text-slate-600 leading-relaxed">
                        Durante la cottura, l'evaporazione dell'acqua determina una perdita di peso tra il 10% e il 25% a seconda della pezzatura, della temperatura del forno e del tipo di crosta. Per ottenere una pagnotta cotta da 500g con un calo del 15%, la pastella cruda deve pesare circa 588g.
                    </p>
                </details>

                <details class="group bg-slate-50/80 hover:bg-slate-50 rounded-2xl border border-slate-200/80 p-4 transition duration-150">
                    <summary class="flex justify-between items-center font-bold text-xs sm:text-sm text-slate-900 cursor-pointer list-none select-none">
                        <span>Come funziona la modalità Ingrediente Limitante?</span>
                        <span class="text-slate-400 group-open:rotate-180 transition-transform duration-200">▼</span>
                    </summary>
                    <p class="mt-2 text-xs text-slate-600 leading-relaxed">
                        Se in magazzino disponi di una quantità limitata di un ingrediente (ad esempio solo 450g di burro o 1200g di farina speciale), il sistema ricalcola l'intera ricetta mantenendo rigorosamente costanti tutte le proporzioni percentuali.
                    </p>
                </details>
            </div>
        </section>

        <!-- Legal Disclaimer & Safe Harbor -->
        <section id="legalDisclaimerBox" class="bg-amber-50/60 rounded-3xl border border-amber-200/90 shadow-xs p-5 sm:p-6 text-[11px] sm:text-xs text-slate-700 leading-relaxed space-y-2">
            <div class="font-extrabold text-slate-900 uppercase tracking-wider text-[11px] flex items-center gap-1.5">
                <span>⚖️</span> <span>Avvertenza Tecnica, Tolleranze di Laboratorio &amp; Esclusione di Responsabilità</span>
            </div>
            <p>
                <strong>1. Accuratezza delle stime e taratura strumenti:</strong> Le proporzioni fornite sono puramente matematiche. Le rese reali dipendono dalla capacità di assorbimento della specifica farina (W, P/L, Falling Number), dall'umidità ambientale, dal tipo di impastatrice e dalle perdite di evaporazione durante la fermentazione e la cottura.
            </p>
            <p>
                <strong>2. Manleva:</strong> OmniTools Lab non risponde di eventuali scostamenti di pezzatura, difetti di lievitazione o perdite commerciali di lavorazione.
            </p>
        </section>

    </main>
"""

# Script IT
script_it = """
    <script>
        let currentScalerMode = 'dough'; // 'dough', 'pieces', 'limit'

        function stepVal(id, delta, min) {
            const inp = document.getElementById(id);
            if (!inp) return;
            let v = parseFloat(inp.value) || 0;
            v = Math.max(min, v + delta);
            inp.value = v.toFixed(1).replace('.0', '');
            calculateBatchScaler();
        }

        function setScalerMode(mode) {
            currentScalerMode = mode;
            const btnDough = document.getElementById('tabModeDough');
            const btnPieces = document.getElementById('tabModePieces');
            const btnLimit = document.getElementById('tabModeLimit');

            const boxDough = document.getElementById('targetDoughBox');
            const boxPieces = document.getElementById('targetPiecesBox');
            const boxLimit = document.getElementById('targetLimitBox');

            [btnDough, btnPieces, btnLimit].forEach(b => {
                b.className = 'py-2 px-3 rounded-xl transition text-slate-600 hover:text-slate-900 text-center cursor-pointer';
            });
            [boxDough, boxPieces, boxLimit].forEach(bx => bx.classList.add('hidden'));

            if (mode === 'dough') {
                btnDough.className = 'py-2 px-3 rounded-xl transition bg-white text-orange-600 shadow-xs text-center cursor-pointer';
                boxDough.classList.remove('hidden');
            } else if (mode === 'pieces') {
                btnPieces.className = 'py-2 px-3 rounded-xl transition bg-white text-orange-600 shadow-xs text-center cursor-pointer';
                boxPieces.classList.remove('hidden');
            } else if (mode === 'limit') {
                btnLimit.className = 'py-2 px-3 rounded-xl transition bg-white text-orange-600 shadow-xs text-center cursor-pointer';
                boxLimit.classList.remove('hidden');
            }
            calculateBatchScaler();
        }

        function syncFlourBlend(changed) {
            if (changed === 1) {
                let v = parseFloat(document.getElementById('inpFlour1Pct').value) || 0;
                v = Math.max(0, Math.min(100, v));
                document.getElementById('inpFlour2Pct').value = (100 - v).toFixed(0);
            } else {
                let v = parseFloat(document.getElementById('inpFlour2Pct').value) || 0;
                v = Math.max(0, Math.min(100, v));
                document.getElementById('inpFlour1Pct').value = (100 - v).toFixed(0);
            }
            const f1 = document.getElementById('inpFlour1Pct').value;
            const f2 = document.getElementById('inpFlour2Pct').value;
            document.getElementById('lblFlourBlendRatio').textContent = `${f1}% / ${f2}%`;
            calculateBatchScaler();
        }

        function calculateBatchScaler() {
            const flour1Pct = parseFloat(document.getElementById('inpFlour1Pct').value) || 70;
            const flour2Pct = parseFloat(document.getElementById('inpFlour2Pct').value) || 30;

            const waterPct = parseFloat(document.getElementById('inpWaterPct').value) || 65;
            const saltPct = parseFloat(document.getElementById('inpSaltPct').value) || 2.2;
            const yeastPct = parseFloat(document.getElementById('inpYeastPct').value) || 1.5;
            const fatPct = parseFloat(document.getElementById('inpFatPct').value) || 0;
            const sugarPct = parseFloat(document.getElementById('inpSugarPct').value) || 0;
            const inclPct = parseFloat(document.getElementById('inpInclusionsPct').value) || 0;

            const wastePct = parseFloat(document.getElementById('inpMachineWastePct').value) || 0;
            const bakeLossPct = parseFloat(document.getElementById('inpBakeLossPct').value) || 0;

            const sumBakerPct = 100 + waterPct + saltPct + yeastPct + fatPct + sugarPct + inclPct;
            document.getElementById('lblSumBakerPct').textContent = `Tot: ${sumBakerPct.toFixed(1)}%`;

            let netDoughKg = 5.0;

            if (currentScalerMode === 'dough') {
                netDoughKg = parseFloat(document.getElementById('inpTargetDoughKg').value) || 5.0;
            } else if (currentScalerMode === 'pieces') {
                const pieces = parseFloat(document.getElementById('inpNumPieces').value) || 1;
                const rawGrams = parseFloat(document.getElementById('inpPieceWeightRaw').value) || 500;
                netDoughKg = (pieces * rawGrams) / 1000.0;
            } else if (currentScalerMode === 'limit') {
                const limitIng = document.getElementById('selLimitIngredient').value;
                const limitGrams = parseFloat(document.getElementById('inpLimitQtyGrams').value) || 1000;
                let refPct = 100;
                if (limitIng === 'flour') refPct = 100;
                else if (limitIng === 'water') refPct = waterPct;
                else if (limitIng === 'butter') refPct = fatPct || 1;
                else if (limitIng === 'sugar') refPct = sugarPct || 1;

                const flourTotalFromLimit = (limitGrams / refPct) * 100.0;
                netDoughKg = (flourTotalFromLimit * (sumBakerPct / 100.0)) / 1000.0;
            }

            // Total batch with machine waste
            const batchInBowlKg = netDoughKg * (1 + (wastePct / 100.0));
            const totalFlourGrams = (batchInBowlKg * 1000.0) / (sumBakerPct / 100.0);

            // Grams for each ingredient
            const gFlour1 = Math.round(totalFlourGrams * (flour1Pct / 100.0));
            const gFlour2 = Math.round(totalFlourGrams * (flour2Pct / 100.0));
            const gWater = Math.round(totalFlourGrams * (waterPct / 100.0));
            const gSalt = Math.round(totalFlourGrams * (saltPct / 100.0));
            const gYeast = Math.round(totalFlourGrams * (yeastPct / 100.0));
            const gFat = Math.round(totalFlourGrams * (fatPct / 100.0));
            const gSugar = Math.round(totalFlourGrams * (sugarPct / 100.0));

            // Update Distinta Banco Table
            document.getElementById('lblNetDoughHeader').textContent = `${netDoughKg.toFixed(2)} kg`;
            document.getElementById('resFlour1Grams').textContent = gFlour1.toLocaleString('it-IT') + ' g';
            document.getElementById('subFlour1').textContent = `${flour1Pct}% del blend farine`;

            document.getElementById('resFlour2Grams').textContent = gFlour2.toLocaleString('it-IT') + ' g';
            document.getElementById('subFlour2').textContent = `${flour2Pct}% del blend farine`;

            document.getElementById('resWaterGrams').textContent = gWater.toLocaleString('it-IT') + ' g';
            document.getElementById('subWater').textContent = `${waterPct.toFixed(1)}% su farina`;

            document.getElementById('resSaltGrams').textContent = gSalt.toLocaleString('it-IT') + ' g';
            document.getElementById('subSalt').textContent = `${saltPct.toFixed(1)}% su farina`;

            document.getElementById('resYeastGrams').textContent = gYeast.toLocaleString('it-IT') + ' g';
            document.getElementById('subYeast').textContent = `${yeastPct.toFixed(1)}% su farina`;

            document.getElementById('resFatGrams').textContent = gFat.toLocaleString('it-IT') + ' g';
            document.getElementById('subFat').textContent = `${fatPct.toFixed(1)}% su farina`;

            document.getElementById('resSugarGrams').textContent = gSugar.toLocaleString('it-IT') + ' g';
            document.getElementById('subSugar').textContent = `${sugarPct.toFixed(1)}% su farina`;

            // KPI Grid
            document.getElementById('kpiTotalFlour').textContent = (totalFlourGrams / 1000.0).toFixed(2) + ' kg';
            document.getElementById('kpiTotalBatch').textContent = batchInBowlKg.toFixed(2) + ' kg';
            const bakedYieldKg = netDoughKg * (1 - (bakeLossPct / 100.0));
            document.getElementById('kpiBakedYield').textContent = bakedYieldKg.toFixed(2) + ' kg';

            let estPieces = Math.round((netDoughKg * 1000.0) / 500.0);
            if (currentScalerMode === 'pieces') {
                estPieces = document.getElementById('inpNumPieces').value;
            }
            document.getElementById('kpiEstimatedPieces').textContent = `~${estPieces} pz`;

            // SVG CAD Layered Update
            const totalWidth = 440;
            const flourFraction = 100.0 / sumBakerPct;
            const waterFraction = waterPct / sumBakerPct;
            const otherFraction = (sumBakerPct - 100 - waterPct) / sumBakerPct;

            const wFlour = Math.round(totalWidth * flourFraction);
            const wWater = Math.round(totalWidth * waterFraction);
            const wOther = Math.max(10, totalWidth - wFlour - wWater);

            const barFlour = document.getElementById('svgBarFlour');
            const barWater = document.getElementById('svgBarWater');
            const barOther = document.getElementById('svgBarOther');

            if (barFlour && barWater && barOther) {
                barFlour.setAttribute('width', wFlour);
                barWater.setAttribute('x', 30 + wFlour + 2);
                barWater.setAttribute('width', wWater);
                barOther.setAttribute('x', 30 + wFlour + wWater + 4);
                barOther.setAttribute('width', wOther);

                document.getElementById('svgTxtFlour').setAttribute('x', 30 + (wFlour / 2));
                document.getElementById('svgTxtFlour').textContent = `FARINA (${(totalFlourGrams/1000).toFixed(2)}kg)`;

                document.getElementById('svgTxtWater').setAttribute('x', 30 + wFlour + 2 + (wWater / 2));
                document.getElementById('svgTxtWater').textContent = `ACQUA (${waterPct}%)`;

                document.getElementById('svgTxtOther').setAttribute('x', 30 + wFlour + wWater + 4 + (wOther / 2));
            }

            document.getElementById('svgTxtTotalDough').textContent = `Massa Totale Impasto: ${batchInBowlKg.toFixed(2)} kg (incluso ${wastePct}% sfrido)`;
            document.getElementById('svgTxtBakedYield').textContent = `Resa Cotta Stimata (-${bakeLossPct}% calo): ${bakedYieldKg.toFixed(2)} kg`;

            // Print summary update
            const printSummary = document.getElementById('printInputsSummary');
            if (printSummary) {
                printSummary.innerHTML = `
                    <div><span class="text-slate-400 block">Massa Netta:</span><strong>${netDoughKg.toFixed(2)} kg</strong></div>
                    <div><span class="text-slate-400 block">Farina Base:</span><strong>${(totalFlourGrams/1000).toFixed(2)} kg</strong></div>
                    <div><span class="text-slate-400 block">Idratazione:</span><strong>${waterPct}%</strong></div>
                    <div><span class="text-slate-400 block">Resa Cotta:</span><strong>${bakedYieldKg.toFixed(2)} kg</strong></div>
                `;
            }
            const printTs = document.getElementById('printTimestamp');
            if (printTs) printTs.textContent = new Date().toLocaleDateString('it-IT');
        }

        function copyBatchSpec() {
            const totFlour = document.getElementById('kpiTotalFlour').textContent;
            const totBatch = document.getElementById('kpiTotalBatch').textContent;
            const w1 = document.getElementById('resFlour1Grams').textContent;
            const w2 = document.getElementById('resFlour2Grams').textContent;
            const aq = document.getElementById('resWaterGrams').textContent;
            const sl = document.getElementById('resSaltGrams').textContent;
            const lv = document.getElementById('resYeastGrams').textContent;
            const txt = `BatchScaler Pro: Farina Tot: ${totFlour} (F1: ${w1}, F2: ${w2}) | Acqua: ${aq} | Sale: ${sl} | Lievito: ${lv} | Impasto Totale: ${totBatch}`;
            navigator.clipboard.writeText(txt).then(() => {
                const btn = document.getElementById('btnCopyBatch');
                const old = btn.innerHTML;
                btn.innerHTML = '<span>✓</span> <span>Ricetta Copiata!</span>';
                setTimeout(() => { btn.innerHTML = old; }, 2000);
            });
        }

        function exportBatchCsv() {
            const rows = [
                ['Ingrediente', 'Baker %', 'Peso in Grammi', 'Note Impasto'],
                ['Farina 1 (Base)', document.getElementById('inpFlour1Pct').value + '% blend', document.getElementById('resFlour1Grams').textContent, 'Farina principale'],
                ['Farina 2 (Blend)', document.getElementById('inpFlour2Pct').value + '% blend', document.getElementById('resFlour2Grams').textContent, 'Farina secondaria'],
                ['Acqua Totale', document.getElementById('inpWaterPct').value + '%', document.getElementById('resWaterGrams').textContent, 'Idratazione impasto'],
                ['Sale Marino', document.getElementById('inpSaltPct').value + '%', document.getElementById('resSaltGrams').textContent, 'Sale fine'],
                ['Lievito Fresco', document.getElementById('inpYeastPct').value + '%', document.getElementById('resYeastGrams').textContent, 'Lievito compresso'],
                ['Grassi / Burro', document.getElementById('inpFatPct').value + '%', document.getElementById('resFatGrams').textContent, 'Materia grassa'],
                ['Zucchero / Malto', document.getElementById('inpSugarPct').value + '%', document.getElementById('resSugarGrams').textContent, 'Zuccheri fermentescibili'],
                ['MASSA TOTALE VASCA', document.getElementById('lblSumBakerPct').textContent, document.getElementById('kpiTotalBatch').textContent, 'Incluso sfrido macchina'],
                ['RESA COTTA STIMATA', '-', document.getElementById('kpiBakedYield').textContent, 'Dopo calo peso cottura']
            ];
            const csv = rows.map(r => r.map(v => `"${String(v).replace(/"/g, '""')}"`).join(',')).join('\\n');
            const blob = new Blob([csv], { type: 'text/csv;charset=utf-8;' });
            const a = document.createElement('a');
            a.href = URL.createObjectURL(blob);
            a.download = 'omnitools_distinta_impasto_banco.csv';
            a.click();
        }

        document.addEventListener('DOMContentLoaded', () => {
            calculateBatchScaler();
        });
    </script>
"""

full_it = head_it + "\n</head>\n" + top_it + "\n" + main_it + "\n" + script_it + "\n" + bottom_it

with open('Calcolatore_Pendenza/impasti.html', 'w', encoding='utf-8') as f:
    f.write(full_it)

print(f"Generated Calcolatore_Pendenza/impasti.html ({len(full_it)} bytes)")
