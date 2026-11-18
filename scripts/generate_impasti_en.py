#!/usr/bin/env python3
import os
import re

print("Generating BatchScaler Pro (EN)...")

with open('Calcolatore_Pendenza/shelflife.html', 'r', encoding='utf-8') as f:
    it_source = f.read()

with open('Calcolatore_Pendenza/en/shelf-life-calculator.html', 'r', encoding='utf-8') as f:
    en_source = f.read()

dark_styles_en = en_source[en_source.find('<style id="omniDarkStyles">'):en_source.find('</head>')]

def get_top_nav(html, mirror_url, tool_name):
    body_idx = html.find('<body')
    main_idx = html.find('<main')
    top = html[body_idx:main_idx]
    top = re.sub(r'data-mirror-url="[^"]*"', f'data-mirror-url="{mirror_url}"', top)
    top = re.sub(r'<span id="suiteCurrentToolName"[^>]*>[^<]*</span>', f'<span id="suiteCurrentToolName" class="truncate min-w-0">{tool_name}</span>', top)
    return top

top_en = get_top_nav(en_source, "/impasti", "BatchScaler Pro")

def get_bottom_nav(html):
    footer_idx = html.find('<footer')
    return html[footer_idx:]

bottom_en = get_bottom_nav(en_source)

# Head EN
head_en = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta name="google-site-verification" content="MRdbDm9lLhokeD3I0FOpUSOhNaF_2WaveKvu52FxtG4">
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0">
    <title>BatchScaler Pro: Baker's % &amp; Dough Batch Scaling Calculator | OmniTools Lab</title>
    <meta name="description" content="Commercial bakery batch scaler based on Baker's Percentage (Flour = 100%): scale recipes by target dough weight, piece count, or limiting ingredient with machine waste and bake loss.">

    <!-- Canonical & SEO Meta Tags -->
    <link rel="canonical" href="https://www.omnitoolslab.com/en/batch-scaler-calculator" />
    <link rel="alternate" hreflang="it" href="https://www.omnitoolslab.com/impasti" />
    <link rel="alternate" hreflang="en-US" href="https://www.omnitoolslab.com/en/batch-scaler-calculator" />
    <link rel="alternate" hreflang="en" href="https://www.omnitoolslab.com/en/batch-scaler-calculator" />
    <link rel="alternate" hreflang="x-default" href="https://www.omnitoolslab.com/en/batch-scaler-calculator" />
    
    <meta name="robots" content="index, follow">
    <meta property="og:type" content="website">
    <meta property="og:title" content="BatchScaler Pro: Commercial Dough Batch Scaler">
    <meta property="og:description" content="Scale bakery and pizza dough recipes accurately with Baker's Percentage, machine waste compensation, and printable bench production sheets.">
    <meta property="og:url" content="https://www.omnitoolslab.com/en/batch-scaler-calculator">
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
    "name": "BatchScaler Pro — Commercial Dough & Baker's Percentage Calculator",
    "url": "https://www.omnitoolslab.com/en/batch-scaler-calculator",
    "applicationCategory": "BusinessApplication",
    "operatingSystem": "All",
    "description": "Professional baking calculator based on Baker's Percentage (Flour = 100%) with machine bowl waste allowance, bake loss yield, and bench production sheets.",
    "offers": {
      "@type": "Offer",
      "price": "0",
      "priceCurrency": "USD"
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
        "item": "https://www.omnitoolslab.com/en/batch-scaler-calculator"
      }
    ]
  },
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "What is Baker's Percentage (Baker's Math)?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Baker's percentage is a standard mathematical notation where total flour weight always represents 100%. All other ingredients (water, salt, yeast, fats, sugars) are expressed as a percentage relative to the flour weight."
        }
      },
      {
        "@type": "Question",
        "name": "How is total flour calculated from a target dough batch weight?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The formula is: Total Flour = (Target Weight × (1 + Machine Waste% / 100)) / (Sum of all Baker's % / 100). Each ingredient quantity is then derived by multiplying total flour by its respective percentage."
        }
      },
      {
        "@type": "Question",
        "name": "What is mixer bowl waste allowance?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Mixer bowl waste is the portion of dough that clings to spiral hooks and bowl walls or is lost during dividing. In commercial baking, it typically ranges between 1% and 3%."
        }
      },
      {
        "@type": "Question",
        "name": "How does oven bake loss affect finished bread weight?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "During baking, water evaporation causes a 10% to 25% weight loss depending on loaf size, baking temperature, and crust type. To achieve a 500g baked loaf at 15% bake loss, dough pieces must be scaled to ~588g raw."
        }
      },
      {
        "@type": "Question",
        "name": "How does the Limiting Ingredient mode work?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "If stock is restricted for any single ingredient (such as only 450g butter or 1000g specialty flour remaining), the system automatically rescales the entire recipe preserving all ratios."
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
""" + dark_styles_en

# Main EN
main_en = """
    <!-- Main Container -->
    <main class="max-w-5xl mx-auto px-3 sm:px-6 py-2.5 sm:py-5 flex-1 w-full space-y-6 sm:space-y-8">

        <!-- PRINT ONLY: Professional Technical Header Cartiglio -->
        <div id="printHeader" class="hidden print:block border-b-2 border-slate-900 pb-3 mb-4">
            <div class="flex justify-between items-start gap-4">
                <div>
                    <div class="flex items-center gap-2 mb-1">
                        <span class="px-2 py-0.5 bg-orange-600 text-white font-bold text-[10px] rounded uppercase tracking-wider">OmniTools Lab — A4 TECHNICAL BENCH SHEET</span>
                        <span class="text-[11px] font-bold text-slate-600">OmniFood • Commercial Baking</span>
                    </div>
                    <h1 class="font-jakarta text-xl font-extrabold text-slate-900 leading-tight" id="printSheetTitle">Commercial Dough Batch Scaling &amp; Production Formula</h1>
                    <p class="text-[10px] text-slate-500 mt-0.5">Methodology: Baker's Percentage (Total Flour = 100%) • Machine Waste &amp; Bake Loss</p>
                </div>
                <div class="text-right text-[10px] text-slate-600 shrink-0">
                    <div class="font-bold text-slate-900 text-xs">omnitoolslab.com</div>
                    <div>Print Date: <span id="printTimestamp"></span></div>
                </div>
            </div>
            <div class="mt-2.5 pt-2 border-t border-slate-200 grid grid-cols-4 gap-2 text-[10px]" id="printInputsSummary"></div>
        </div>

        <!-- Hero Section -->
        <section class="text-center space-y-2 no-print">
            <div class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-orange-100 text-orange-800 text-xs font-bold shadow-2xs">
                <span>🥖</span> <span>Baker's % (Flour = 100%)</span> • <span>⚖️</span> <span>Machine Waste &amp; Bake Loss</span> • <span>📦</span> <span>A4 Production Sheet</span>
            </div>
            <h1 id="heroTitle" class="font-jakarta text-2xl sm:text-3xl lg:text-4xl font-black text-slate-900 tracking-tight">
                BatchScaler Pro
            </h1>
            <p id="heroSubtitle" class="text-slate-600 text-xs sm:text-sm max-w-2xl mx-auto leading-relaxed">
                Commercial dough scaling engine for bakeries and pizzerias: scale recipes by <strong>total batch weight</strong>, <strong>piece count</strong>, or <strong>limiting ingredient</strong> with CAD layered visual blueprints.
            </p>
        </section>

        <!-- Main Card: 2 Columns (Form Controls + CAD Layered Blueprint) -->
        <div class="bg-white rounded-3xl border border-slate-200 border-t-4 border-t-orange-600 shadow-sm p-4 sm:p-7 space-y-6">

            <!-- 3 Scaling Modes Tabs -->
            <div class="no-print">
                <label class="text-xs font-bold text-slate-700 uppercase tracking-wider block mb-2">Scaling Target Mode</label>
                <div class="grid grid-cols-3 gap-2 p-1.5 bg-slate-100 rounded-2xl border border-slate-200 text-xs font-bold">
                    <button type="button" id="tabModeDough" onclick="setScalerMode('dough')" class="py-2 px-3 rounded-xl transition bg-white text-orange-600 shadow-xs text-center cursor-pointer">
                        🎯 Total Dough
                    </button>
                    <button type="button" id="tabModePieces" onclick="setScalerMode('pieces')" class="py-2 px-3 rounded-xl transition text-slate-600 hover:text-slate-900 text-center cursor-pointer">
                        🔢 Pieces × Weight
                    </button>
                    <button type="button" id="tabModeLimit" onclick="setScalerMode('limit')" class="py-2 px-3 rounded-xl transition text-slate-600 hover:text-slate-900 text-center cursor-pointer">
                        📦 Limiting Ingredient
                    </button>
                </div>
            </div>

            <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 items-start">
                
                <!-- Left Column: Controls (lg:col-span-6) -->
                <div class="lg:col-span-6 space-y-5">
                    
                    <!-- Dynamic Scaling Target Input -->
                    <div class="p-4 bg-orange-50/60 rounded-2xl border border-orange-200/80 space-y-3">
                        <div id="targetDoughBox" class="space-y-1.5">
                            <label class="text-[11px] font-bold text-slate-700 block">Desired Net Dough Batch (kg)</label>
                            <div class="flex items-center">
                                <button type="button" onclick="stepVal('inpTargetDoughKg', -0.5, 0.1)" class="w-9 h-9 bg-slate-200 hover:bg-slate-300 font-bold rounded-l-lg text-slate-700">-</button>
                                <input type="number" id="inpTargetDoughKg" value="5.0" min="0.1" step="0.1" oninput="calculateBatchScaler()" class="w-full h-9 text-center text-xs font-mono font-bold border-y border-slate-200 focus:ring-0 bg-white">
                                <button type="button" onclick="stepVal('inpTargetDoughKg', 0.5, 0.1)" class="w-9 h-9 bg-slate-200 hover:bg-slate-300 font-bold rounded-r-lg text-slate-700">+</button>
                            </div>
                        </div>

                        <div id="targetPiecesBox" class="hidden grid grid-cols-2 gap-3">
                            <div>
                                <label class="text-[11px] font-bold text-slate-700 block">Number of Pieces (Count)</label>
                                <input type="number" id="inpNumPieces" value="10" min="1" step="1" oninput="calculateBatchScaler()" class="w-full mt-1 text-xs font-mono font-bold p-2 rounded-xl border border-slate-200 bg-white">
                            </div>
                            <div>
                                <label class="text-[11px] font-bold text-slate-700 block">Single Raw Piece Weight (g)</label>
                                <input type="number" id="inpPieceWeightRaw" value="550" min="10" step="10" oninput="calculateBatchScaler()" class="w-full mt-1 text-xs font-mono font-bold p-2 rounded-xl border border-slate-200 bg-white">
                            </div>
                        </div>

                        <div id="targetLimitBox" class="hidden grid grid-cols-2 gap-3">
                            <div>
                                <label class="text-[11px] font-bold text-slate-700 block">Limiting Available Ingredient</label>
                                <select id="selLimitIngredient" onchange="calculateBatchScaler()" class="w-full mt-1 text-xs font-bold p-2 rounded-xl border border-slate-200 bg-white">
                                    <option value="flour">Base Flour</option>
                                    <option value="water">Water</option>
                                    <option value="butter">Butter / Fats</option>
                                    <option value="sugar">Sugar</option>
                                </select>
                            </div>
                            <div>
                                <label class="text-[11px] font-bold text-slate-700 block">Quantity on Hand (g)</label>
                                <input type="number" id="inpLimitQtyGrams" value="1000" min="1" step="50" oninput="calculateBatchScaler()" class="w-full mt-1 text-xs font-mono font-bold p-2 rounded-xl border border-slate-200 bg-white">
                            </div>
                        </div>

                        <!-- Technical Machine Loss & Baking Loss -->
                        <div class="grid grid-cols-2 gap-3 pt-1 border-t border-orange-200/50">
                            <div>
                                <div class="flex justify-between items-center">
                                    <label class="text-[10px] font-bold text-slate-600 block">Machine Waste Allowance (%)</label>
                                    <span class="text-[9px] font-mono text-slate-400">1-3% typical</span>
                                </div>
                                <input type="number" id="inpMachineWastePct" value="2.0" min="0" max="15" step="0.5" oninput="calculateBatchScaler()" class="w-full mt-1 text-xs font-mono font-bold p-1.5 rounded-lg border border-slate-200 bg-white">
                            </div>
                            <div>
                                <div class="flex justify-between items-center">
                                    <label class="text-[10px] font-bold text-slate-600 block">Bake Loss / Evaporation (%)</label>
                                    <span class="text-[9px] font-mono text-slate-400">12-20% typical</span>
                                </div>
                                <input type="number" id="inpBakeLossPct" value="15.0" min="0" max="35" step="0.5" oninput="calculateBatchScaler()" class="w-full mt-1 text-xs font-mono font-bold p-1.5 rounded-lg border border-slate-200 bg-white">
                            </div>
                        </div>
                    </div>

                    <!-- Baker's % Recipe Formula Parameters -->
                    <div class="space-y-3">
                        <div class="flex items-center justify-between border-b border-slate-100 pb-2">
                            <span class="text-xs font-bold text-slate-800 uppercase tracking-wider flex items-center gap-1.5">
                                <span>🌾</span> <span>Baker's % Formula (Total Flour = 100%)</span>
                            </span>
                            <span class="text-[10px] font-mono font-bold text-orange-600 bg-orange-100 px-2 py-0.5 rounded-full">Bakery Standard</span>
                        </div>

                        <!-- Multi-Flour Blend -->
                        <div class="p-3 bg-slate-50/70 rounded-xl border border-slate-200/70 space-y-2">
                            <div class="text-[11px] font-bold text-slate-700 flex justify-between">
                                <span>Flour Blend (Flour 1 + Flour 2 = 100%)</span>
                                <span id="lblFlourBlendRatio" class="font-mono text-orange-600">70% / 30%</span>
                            </div>
                            <div class="grid grid-cols-2 gap-2">
                                <div>
                                    <label class="text-[10px] text-slate-500 block">Flour 1 (e.g. Bread Flour / T55) %</label>
                                    <input type="number" id="inpFlour1Pct" value="70" min="0" max="100" step="5" oninput="syncFlourBlend(1)" class="w-full mt-0.5 text-xs font-mono font-bold p-1.5 rounded-lg border border-slate-200 bg-white">
                                </div>
                                <div>
                                    <label class="text-[10px] text-slate-500 block">Flour 2 (e.g. Whole Wheat / Rye) %</label>
                                    <input type="number" id="inpFlour2Pct" value="30" min="0" max="100" step="5" oninput="syncFlourBlend(2)" class="w-full mt-0.5 text-xs font-mono font-bold p-1.5 rounded-lg border border-slate-200 bg-white">
                                </div>
                            </div>
                        </div>

                        <!-- Baker's Percentages Inputs -->
                        <div class="grid grid-cols-2 sm:grid-cols-3 gap-2.5">
                            <div>
                                <label class="text-[10px] font-bold text-blue-700 block truncate">Water (Hydration %)</label>
                                <input type="number" id="inpWaterPct" value="65.0" min="30" max="110" step="0.5" oninput="calculateBatchScaler()" class="w-full mt-1 text-xs font-mono font-bold p-2 rounded-xl border border-blue-200 bg-blue-50/30">
                            </div>
                            <div>
                                <label class="text-[10px] font-bold text-slate-700 block truncate">Salt (% on flour)</label>
                                <input type="number" id="inpSaltPct" value="2.2" min="0" max="5" step="0.1" oninput="calculateBatchScaler()" class="w-full mt-1 text-xs font-mono font-bold p-2 rounded-xl border border-slate-200">
                            </div>
                            <div>
                                <label class="text-[10px] font-bold text-amber-700 block truncate">Fresh Yeast (%)</label>
                                <input type="number" id="inpYeastPct" value="1.5" min="0.1" max="10" step="0.1" oninput="calculateBatchScaler()" class="w-full mt-1 text-xs font-mono font-bold p-2 rounded-xl border border-slate-200">
                            </div>
                            <div>
                                <label class="text-[10px] font-bold text-slate-700 block truncate">Oil / Butter / Fats (%)</label>
                                <input type="number" id="inpFatPct" value="3.0" min="0" max="80" step="0.5" oninput="calculateBatchScaler()" class="w-full mt-1 text-xs font-mono font-bold p-2 rounded-xl border border-slate-200">
                            </div>
                            <div>
                                <label class="text-[10px] font-bold text-slate-700 block truncate">Sugar / Malt (%)</label>
                                <input type="number" id="inpSugarPct" value="1.0" min="0" max="50" step="0.5" oninput="calculateBatchScaler()" class="w-full mt-1 text-xs font-mono font-bold p-2 rounded-xl border border-slate-200">
                            </div>
                            <div>
                                <label class="text-[10px] font-bold text-slate-700 block truncate">Inclusions / Seeds (%)</label>
                                <input type="number" id="inpInclusionsPct" value="0.0" min="0" max="50" step="1" oninput="calculateBatchScaler()" class="w-full mt-1 text-xs font-mono font-bold p-2 rounded-xl border border-slate-200">
                            </div>
                        </div>

                    </div>

                    <!-- Action Buttons -->
                    <div class="pt-2 flex flex-wrap gap-2.5 no-print">
                        <button type="button" onclick="copyBatchSpec()" id="btnCopyBatch" class="flex-1 py-2.5 px-4 bg-orange-600 hover:bg-orange-700 active:scale-95 text-white font-bold text-xs rounded-xl transition shadow-sm flex items-center justify-center gap-1.5 cursor-pointer">
                            <span>📋</span> <span>Copy Formula Sheet</span>
                        </button>
                        <button type="button" onclick="exportBatchCsv()" class="py-2.5 px-3.5 bg-slate-100 hover:bg-slate-200 active:scale-95 text-slate-700 font-bold text-xs rounded-xl transition flex items-center gap-1 cursor-pointer">
                            <span>📊</span> <span>Bench CSV</span>
                        </button>
                        <button type="button" onclick="window.print()" class="py-2.5 px-3.5 bg-slate-100 hover:bg-slate-200 active:scale-95 text-slate-700 font-bold text-xs rounded-xl transition flex items-center gap-1 cursor-pointer">
                            <span>🖨️</span> <span>Print A4</span>
                        </button>
                    </div>

                </div>

                <!-- Right Column: Visual Blueprint CAD & Distinta Banco (lg:col-span-6) -->
                <div class="lg:col-span-6 space-y-4">
                    <div class="flex items-center justify-between">
                        <span class="text-xs font-bold text-slate-700 uppercase tracking-wider flex items-center gap-1.5">
                            <span>📐</span> <span>CAD Layered Dough Blueprint</span>
                        </span>
                        <span id="lblSumBakerPct" class="text-[10px] font-mono font-bold text-orange-600 bg-orange-100 px-2 py-0.5 rounded-full">Total: 172.7%</span>
                    </div>

                    <!-- SVG Layered CAD Visual Blueprint -->
                    <div class="bg-slate-900 rounded-2xl p-4 border border-slate-800 shadow-md">
                        <svg class="svg-blueprint w-full h-44 sm:h-52" viewBox="0 0 500 200" role="img" aria-label="Layered Dough CAD Blueprint">
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
                            <text id="svgTxtFlour" x="150" y="70" fill="#ffffff" font-size="11" font-weight="bold" font-family="'JetBrains Mono', monospace" text-anchor="middle">FLOUR 100%</text>
                            <text id="svgTxtWater" x="350" y="70" fill="#ffffff" font-size="11" font-weight="bold" font-family="'JetBrains Mono', monospace" text-anchor="middle">WATER 65%</text>
                            <text id="svgTxtOther" x="450" y="70" fill="#ffffff" font-size="9" font-weight="bold" font-family="'JetBrains Mono', monospace" text-anchor="middle">+</text>

                            <!-- Bottom Dimensioning Line -->
                            <line x1="30" y1="100" x2="470" y2="100" stroke="#94a3b8" stroke-width="1.5" />
                            <line x1="30" y1="95" x2="30" y2="105" stroke="#94a3b8" stroke-width="1.5" />
                            <line x1="470" y1="95" x2="470" y2="105" stroke="#94a3b8" stroke-width="1.5" />
                            <text id="svgTxtTotalDough" x="250" y="118" fill="#38bdf8" font-size="11" font-weight="bold" font-family="'JetBrains Mono', monospace" text-anchor="middle">Mixer Batch: 5.10 kg (incl. 2% waste)</text>

                            <!-- Baking Loss Indicator -->
                            <rect x="30" y="135" width="374" height="20" rx="3" fill="#ea580c" opacity="0.8" />
                            <rect x="406" y="135" width="64" height="20" rx="3" fill="#64748b" opacity="0.5" stroke="#94a3b8" stroke-dasharray="2 2" />
                            <text id="svgTxtBakedYield" x="217" y="149" fill="#ffffff" font-size="10" font-weight="bold" font-family="'JetBrains Mono', monospace" text-anchor="middle">Baked Yield (-15% loss): 4.25 kg</text>
                            <text x="438" y="149" fill="#cbd5e1" font-size="9" font-family="'JetBrains Mono', monospace" text-anchor="middle">Loss</text>
                        </svg>
                    </div>

                    <!-- Production Formula Sheet (Table) -->
                    <div class="border border-slate-200 rounded-2xl overflow-hidden bg-white shadow-xs">
                        <div class="bg-slate-100/80 px-4 py-2 border-b border-slate-200 flex justify-between items-center text-xs font-bold text-slate-800">
                            <span>Bakery Bench Production Sheet</span>
                            <span class="text-[10px] font-mono text-slate-500">Net Batch: <strong id="lblNetDoughHeader" class="text-slate-900">5.00 kg</strong></span>
                        </div>
                        <div class="divide-y divide-slate-100 text-xs">
                            <div class="p-2.5 flex justify-between items-center bg-amber-50/40">
                                <div>
                                    <strong class="text-slate-900 block">Flour 1 (Base)</strong>
                                    <span id="subFlour1" class="text-[10px] text-slate-500">70% of flour blend</span>
                                </div>
                                <span id="resFlour1Grams" class="font-mono font-black text-slate-900 text-sm">2,067 g</span>
                            </div>
                            <div class="p-2.5 flex justify-between items-center bg-amber-50/40">
                                <div>
                                    <strong class="text-slate-900 block">Flour 2 (Blend)</strong>
                                    <span id="subFlour2" class="text-[10px] text-slate-500">30% of flour blend</span>
                                </div>
                                <span id="resFlour2Grams" class="font-mono font-black text-slate-900 text-sm">886 g</span>
                            </div>
                            <div class="p-2.5 flex justify-between items-center bg-blue-50/40">
                                <div>
                                    <strong class="text-blue-900 block">Water (Hydration)</strong>
                                    <span id="subWater" class="text-[10px] text-blue-600">65.0% on flour</span>
                                </div>
                                <span id="resWaterGrams" class="font-mono font-black text-blue-700 text-sm">1,920 g</span>
                            </div>
                            <div class="p-2 flex justify-between items-center">
                                <div>
                                    <span class="text-slate-800 block">Fine Sea Salt</span>
                                    <span id="subSalt" class="text-[10px] text-slate-500">2.2% on flour</span>
                                </div>
                                <span id="resSaltGrams" class="font-mono font-bold text-slate-800">65 g</span>
                            </div>
                            <div class="p-2 flex justify-between items-center">
                                <div>
                                    <span class="text-slate-800 block">Fresh Yeast</span>
                                    <span id="subYeast" class="text-[10px] text-slate-500">1.5% on flour</span>
                                </div>
                                <span id="resYeastGrams" class="font-mono font-bold text-slate-800">44 g</span>
                            </div>
                            <div id="rowFat" class="p-2 flex justify-between items-center">
                                <div>
                                    <span class="text-slate-800 block">Butter / Oil / Fats</span>
                                    <span id="subFat" class="text-[10px] text-slate-500">3.0% on flour</span>
                                </div>
                                <span id="resFatGrams" class="font-mono font-bold text-slate-800">89 g</span>
                            </div>
                            <div id="rowSugar" class="p-2 flex justify-between items-center">
                                <div>
                                    <span class="text-slate-800 block">Sugar / Malt</span>
                                    <span id="subSugar" class="text-[10px] text-slate-500">1.0% on flour</span>
                                </div>
                                <span id="resSugarGrams" class="font-mono font-bold text-slate-800">30 g</span>
                            </div>
                        </div>
                    </div>

                    <!-- Output KPI Grid -->
                    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 pt-1">
                        <div class="p-2.5 bg-slate-50 rounded-xl border border-slate-200 text-center">
                            <span class="text-[9px] uppercase font-bold text-slate-500 block">Total Flour</span>
                            <span id="kpiTotalFlour" class="text-sm font-mono font-black text-slate-900">2.95 kg</span>
                        </div>
                        <div class="p-2.5 bg-slate-50 rounded-xl border border-slate-200 text-center">
                            <span class="text-[9px] uppercase font-bold text-slate-500 block">Mixer Batch</span>
                            <span id="kpiTotalBatch" class="text-sm font-mono font-black text-orange-600">5.10 kg</span>
                        </div>
                        <div class="p-2.5 bg-slate-50 rounded-xl border border-slate-200 text-center">
                            <span class="text-[9px] uppercase font-bold text-slate-500 block">Baked Yield</span>
                            <span id="kpiBakedYield" class="text-sm font-mono font-black text-emerald-600">4.25 kg</span>
                        </div>
                        <div class="p-2.5 bg-slate-50 rounded-xl border border-slate-200 text-center">
                            <span class="text-[9px] uppercase font-bold text-slate-500 block">Estimated Pieces</span>
                            <span id="kpiEstimatedPieces" class="text-sm font-mono font-black text-slate-900">~9-10 pcs</span>
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
                    <span>Frequently Asked Questions — Baker's % &amp; Dough Batch Scaling</span>
                </h2>
                <span class="text-[10px] font-extrabold uppercase px-2 py-0.5 rounded-full bg-slate-100 text-slate-600 border border-slate-200">FAQ</span>
            </div>

            <div id="faqContainer" class="space-y-3">
                <details class="group bg-slate-50/80 hover:bg-slate-50 rounded-2xl border border-slate-200/80 p-4 transition duration-150">
                    <summary class="flex justify-between items-center font-bold text-xs sm:text-sm text-slate-900 cursor-pointer list-none select-none">
                        <span>What is Baker's Percentage (Baker's Math)?</span>
                        <span class="text-slate-400 group-open:rotate-180 transition-transform duration-200">▼</span>
                    </summary>
                    <p class="mt-2 text-xs text-slate-600 leading-relaxed">
                        Baker's percentage is a standard mathematical notation where total flour weight always represents 100%. All other ingredients (water, salt, yeast, fats, sugars) are expressed as a percentage relative to the flour weight.
                    </p>
                </details>

                <details class="group bg-slate-50/80 hover:bg-slate-50 rounded-2xl border border-slate-200/80 p-4 transition duration-150">
                    <summary class="flex justify-between items-center font-bold text-xs sm:text-sm text-slate-900 cursor-pointer list-none select-none">
                        <span>How is total flour calculated from a target dough batch weight?</span>
                        <span class="text-slate-400 group-open:rotate-180 transition-transform duration-200">▼</span>
                    </summary>
                    <p class="mt-2 text-xs text-slate-600 leading-relaxed">
                        The formula is: Total Flour = (Target Weight × (1 + Machine Waste% / 100)) / (Sum of all Baker's % / 100). Each ingredient quantity is then derived by multiplying total flour by its respective percentage.
                    </p>
                </details>

                <details class="group bg-slate-50/80 hover:bg-slate-50 rounded-2xl border border-slate-200/80 p-4 transition duration-150">
                    <summary class="flex justify-between items-center font-bold text-xs sm:text-sm text-slate-900 cursor-pointer list-none select-none">
                        <span>What is mixer bowl waste allowance?</span>
                        <span class="text-slate-400 group-open:rotate-180 transition-transform duration-200">▼</span>
                    </summary>
                    <p class="mt-2 text-xs text-slate-600 leading-relaxed">
                        Mixer bowl waste is the portion of dough that clings to spiral hooks and bowl walls or is lost during dividing. In commercial baking, it typically ranges between 1% and 3%.
                    </p>
                </details>

                <details class="group bg-slate-50/80 hover:bg-slate-50 rounded-2xl border border-slate-200/80 p-4 transition duration-150">
                    <summary class="flex justify-between items-center font-bold text-xs sm:text-sm text-slate-900 cursor-pointer list-none select-none">
                        <span>How does oven bake loss affect finished bread weight?</span>
                        <span class="text-slate-400 group-open:rotate-180 transition-transform duration-200">▼</span>
                    </summary>
                    <p class="mt-2 text-xs text-slate-600 leading-relaxed">
                        During baking, water evaporation causes a 10% to 25% weight loss depending on loaf size, baking temperature, and crust type. To achieve a 500g baked loaf at 15% bake loss, dough pieces must be scaled to ~588g raw.
                    </p>
                </details>

                <details class="group bg-slate-50/80 hover:bg-slate-50 rounded-2xl border border-slate-200/80 p-4 transition duration-150">
                    <summary class="flex justify-between items-center font-bold text-xs sm:text-sm text-slate-900 cursor-pointer list-none select-none">
                        <span>How does the Limiting Ingredient mode work?</span>
                        <span class="text-slate-400 group-open:rotate-180 transition-transform duration-200">▼</span>
                    </summary>
                    <p class="mt-2 text-xs text-slate-600 leading-relaxed">
                        If stock is restricted for any single ingredient (such as only 450g butter or 1000g specialty flour remaining), the system automatically rescales the entire recipe preserving all ratios.
                    </p>
                </details>
            </div>
        </section>

        <!-- Legal Disclaimer & Safe Harbor -->
        <section id="legalDisclaimerBox" class="bg-amber-50/60 rounded-3xl border border-amber-200/90 shadow-xs p-5 sm:p-6 text-[11px] sm:text-xs text-slate-700 leading-relaxed space-y-2">
            <div class="font-extrabold text-slate-900 uppercase tracking-wider text-[11px] flex items-center gap-1.5">
                <span>⚖️</span> <span>Bakery Craft Technical Notice &amp; Disclaimer</span>
            </div>
            <p>
                <strong>1. Estimation and Ambient Variances:</strong> Proportions provided are mathematical calculations. Actual bakery yields depend on specific flour absorption rates (W index, protein quality), ambient dough temperature, mixer type, and fermentation evaporation.
            </p>
            <p>
                <strong>2. Indemnity:</strong> OmniTools Lab and its developers provide this tool for craft optimization without liability for piece weight discrepancies or commercial bakery variances.
            </p>
        </section>

    </main>
"""

# Script EN
with open('Calcolatore_Pendenza/impasti.html', 'r', encoding='utf-8') as f:
    imp_it = f.read()

s_start = imp_it.find('<script>\n        let currentScalerMode')
s_end = imp_it.find('</script>', s_start) + 9
script_text = imp_it[s_start:s_end]

script_en = script_text.replace('new Date().toLocaleDateString(\'it-IT\')', 'new Date().toLocaleDateString(\'en-US\')')
script_en = script_en.replace('<span>Ricetta Copiata!</span>', '<span>Formula Copied!</span>')
script_en = script_en.replace('<div><span class="text-slate-400 block">Massa Netta:</span>', '<div><span class="text-slate-400 block">Net Batch:</span>')
script_en = script_en.replace('<div><span class="text-slate-400 block">Farina Base:</span>', '<div><span class="text-slate-400 block">Base Flour:</span>')
script_en = script_en.replace('<div><span class="text-slate-400 block">Idratazione:</span>', '<div><span class="text-slate-400 block">Hydration:</span>')
script_en = script_en.replace('<div><span class="text-slate-400 block">Resa Cotta:</span>', '<div><span class="text-slate-400 block">Baked Yield:</span>')
script_en = script_en.replace('FLOUR 100%', 'FLOUR 100%')
script_en = script_en.replace('Massa Totale Impasto:', 'Mixer Batch:')
script_en = script_en.replace('(incluso', '(incl.')
script_en = script_en.replace('Resa Cotta Stimata', 'Baked Yield')

full_en = head_en + "\n</head>\n" + top_en + "\n" + main_en + "\n" + script_en + "\n" + bottom_en

with open('Calcolatore_Pendenza/en/batch-scaler-calculator.html', 'w', encoding='utf-8') as f:
    f.write(full_en)

print(f"Generated Calcolatore_Pendenza/en/batch-scaler-calculator.html ({len(full_en)} bytes)")
