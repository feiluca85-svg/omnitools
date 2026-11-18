#!/usr/bin/env python3
import os
import re

print("Generating NutriExport Converter (EN)...")

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

top_en = get_top_nav(en_source, "/nutriexport", "NutriExport Converter")

def get_bottom_nav(html):
    footer_idx = html.find('<footer')
    return html[footer_idx:]

bottom_en = get_bottom_nav(en_source)

head_en = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta name="google-site-verification" content="MRdbDm9lLhokeD3I0FOpUSOhNaF_2WaveKvu52FxtG4">
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0">
    <title>NutriExport Converter: EU 100g to US FDA Nutrition Facts &amp; CFIA | OmniTools Lab</title>
    <meta name="description" content="Professional nutrition label converter: convert EU Reg. 1169/2011 100g values into US FDA 21 CFR 101.9 Nutrition Facts serving sizes with RACC presets, Salt-to-Sodium conversion, legal rounding and Daily Value (% DV).">

    <!-- Canonical & SEO Meta Tags -->
    <link rel="canonical" href="https://www.omnitoolslab.com/en/nutri-export-converter" />
    <link rel="alternate" hreflang="it" href="https://www.omnitoolslab.com/nutriexport" />
    <link rel="alternate" hreflang="en-US" href="https://www.omnitoolslab.com/en/nutri-export-converter" />
    <link rel="alternate" hreflang="en" href="https://www.omnitoolslab.com/en/nutri-export-converter" />
    <link rel="alternate" hreflang="x-default" href="https://www.omnitoolslab.com/en/nutri-export-converter" />
    
    <meta name="robots" content="index, follow">
    <meta property="og:type" content="website">
    <meta property="og:title" content="NutriExport Converter: EU 100g to FDA Nutrition Facts">
    <meta property="og:description" content="Convert EU 100g lab nutritional tables to US FDA Nutrition Facts panels with RACC portion presets and legal rounding rules.">
    <meta property="og:url" content="https://www.omnitoolslab.com/en/nutri-export-converter">
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
    "name": "NutriExport Converter — EU 100g to FDA Nutrition Facts Label",
    "url": "https://www.omnitoolslab.com/en/nutri-export-converter",
    "applicationCategory": "BusinessApplication",
    "operatingSystem": "All",
    "description": "Professional nutrition converter from EU Reg. 1169/2011 100g values to US FDA 21 CFR 101.9 Nutrition Facts label with RACC serving presets, Salt/Sodium conversion, legal rounding and live SVG label preview.",
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
        "name": "NutriExport Converter",
        "item": "https://www.omnitoolslab.com/en/nutri-export-converter"
      }
    ]
  },
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "What is the key difference between EU nutrition declarations and US FDA labels?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "In the European Union (Reg. EU 1169/2011), nutrition declaration is legally mandated per 100g or 100ml. In the United States (FDA 21 CFR 101.9), Nutrition Facts must be stated per standard serving size based on official RACC (Reference Amounts Customarily Consumed) categories."
        }
      },
      {
        "@type": "Question",
        "name": "How do you convert European Salt (g) to American Sodium (mg)?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The stoichiometric formula is: Sodium (mg) = Salt (g) × 400. In reverse, Salt (g) = Sodium (mg) / 400."
        }
      },
      {
        "@type": "Question",
        "name": "What are FDA's official rounding rules for calories and nutrients?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "FDA 21 CFR 101.9 mandates specific rounding tiers: Calories below 5 kcal round to 0, up to 50 kcal round to nearest 5, and above 50 kcal round to nearest 10. Total fat under 0.5g rounds to 0g, between 0.5g and 5g rounds to nearest 0.5g, and 5g or above rounds to nearest 1g."
        }
      },
      {
        "@type": "Question",
        "name": "Which micronutrients are federally mandatory on US Nutrition Facts labels?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Under the updated FDA framework, quantitative amounts and % Daily Values are mandatory for Vitamin D (mcg), Calcium (mg), Iron (mg), and Potassium (mg). Vitamins A and C are now voluntary."
        }
      },
      {
        "@type": "Question",
        "name": "What does % Daily Value (% DV) signify?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The % Daily Value (% DV) indicates how much a nutrient in a serving contributes to a daily 2,000 calorie diet. As a general FDA benchmark: 5% DV or less is low, while 20% DV or more is high."
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
            .fda-label-box {
                box-shadow: none !important;
                border: 2px solid #000000 !important;
                break-inside: avoid !important;
                page-break-inside: avoid !important;
            }
        }
        .fda-label-box {
            font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
            background: #ffffff;
            color: #000000;
        }
        .tabular-nums {
            font-variant-numeric: tabular-nums;
        }
    </style>
""" + dark_styles_en

main_en = """
    <!-- Main Container -->
    <main class="max-w-5xl mx-auto px-3 sm:px-6 py-2.5 sm:py-5 flex-1 w-full space-y-6 sm:space-y-8">

        <!-- PRINT ONLY: Professional Technical Header Cartiglio -->
        <div id="printHeader" class="hidden print:block border-b-2 border-slate-900 pb-3 mb-4">
            <div class="flex justify-between items-start gap-4">
                <div>
                    <div class="flex items-center gap-2 mb-1">
                        <span class="px-2 py-0.5 bg-orange-600 text-white font-bold text-[10px] rounded uppercase tracking-wider">OmniTools Lab — A4 TECHNICAL SHEET</span>
                        <span class="text-[11px] font-bold text-slate-600">OmniFood • Export Compliance</span>
                    </div>
                    <h1 class="font-jakarta text-xl font-extrabold text-slate-900 leading-tight" id="printSheetTitle">US FDA 21 CFR 101.9 Nutrition Facts Label Specification</h1>
                    <p class="text-[10px] text-slate-500 mt-0.5">References: FDA 21 CFR 101.9 • EU Reg. 1169/2011 • Canada CFIA (SFCR)</p>
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
                <span>🇺🇸</span> <span>FDA 21 CFR 101.9</span> • <span>🇪🇺</span> <span>EU Reg. 1169/2011</span> • <span>🇨🇦</span> <span>CFIA RACC</span>
            </div>
            <h1 id="heroTitle" class="font-jakarta text-2xl sm:text-3xl lg:text-4xl font-black text-slate-900 tracking-tight">
                NutriExport Converter
            </h1>
            <p id="heroSubtitle" class="text-slate-600 text-xs sm:text-sm max-w-2xl mx-auto leading-relaxed">
                Export compliance converter: transform standard European <strong>100g</strong> nutrition data into official <strong>US FDA Nutrition Facts</strong> serving panels with legal rounding tiers and % DV.
            </p>
        </section>

        <!-- Main Card: 2 Columns (Form Controls + Live Blueprint FDA Label) -->
        <div class="bg-white rounded-3xl border border-slate-200 border-t-4 border-t-orange-600 shadow-sm p-4 sm:p-7 space-y-6">

            <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 items-start">
                
                <!-- Left Column: Controls (lg:col-span-6) -->
                <div class="lg:col-span-6 space-y-5">
                    
                    <!-- RACC Category & Serving Size -->
                    <div class="p-4 bg-slate-50/80 rounded-2xl border border-slate-200/80 space-y-3">
                        <div class="flex items-center justify-between">
                            <span class="text-xs font-bold text-slate-800 uppercase tracking-wider flex items-center gap-1.5">
                                <span>📐</span> <span>FDA Standard Serving Size (RACC)</span>
                            </span>
                            <span class="text-[10px] font-mono font-bold text-orange-600 bg-orange-100 px-2 py-0.5 rounded-full">21 CFR 101.12</span>
                        </div>

                        <div class="space-y-1.5">
                            <label class="text-[11px] font-bold text-slate-600 block">RACC Food Category Preset</label>
                            <select id="selRaccPreset" onchange="onRaccChange()" class="w-full text-xs font-bold p-2.5 rounded-xl border border-slate-200 bg-white text-slate-800 focus:ring-2 focus:ring-orange-500">
                                <option value="30|cookies|Cookies &amp; Biscuits (30g)">Cookies &amp; Biscuits (30g)</option>
                                <option value="50|bread|Bread &amp; Yeast Rolls (50g)">Bread &amp; Yeast Rolls (50g)</option>
                                <option value="56|pasta|Dry Pasta (56g) / Cooked (140g)">Dry Pasta (56g) / Cooked (140g)</option>
                                <option value="30|cheese|Hard &amp; Semi-hard Cheeses (30g)">Hard Cheeses (30g)</option>
                                <option value="15|oil|Olive Oil &amp; Dressings (15g - 1 tbsp)">Olive Oil (15g - 1 tbsp)</option>
                                <option value="240|beverages|Beverages &amp; Juices (240ml / 8 fl oz)">Beverages &amp; Juices (240ml / 8 fl oz)</option>
                                <option value="30|chocolate|Chocolate &amp; Confectionery (30g)">Chocolate &amp; Snacks (30g)</option>
                                <option value="custom|custom|Custom Serving Size">Custom Serving Size</option>
                            </select>
                        </div>

                        <div class="grid grid-cols-2 gap-3 pt-1">
                            <div>
                                <label class="text-[11px] font-bold text-slate-600 block">Serving Size (g/ml)</label>
                                <div class="flex items-center mt-1">
                                    <button type="button" onclick="stepVal('inpServingGrams', -1, 1)" class="w-8 h-9 bg-slate-200 hover:bg-slate-300 font-bold rounded-l-lg text-slate-700">-</button>
                                    <input type="number" id="inpServingGrams" value="30" min="1" step="0.5" oninput="calculateNutriExport()" class="w-full h-9 text-center text-xs font-mono font-bold border-y border-slate-200 focus:ring-0">
                                    <button type="button" onclick="stepVal('inpServingGrams', 1, 1)" class="w-8 h-9 bg-slate-200 hover:bg-slate-300 font-bold rounded-r-lg text-slate-700">+</button>
                                </div>
                            </div>
                            <div>
                                <label class="text-[11px] font-bold text-slate-600 block">Servings Per Container</label>
                                <div class="flex items-center mt-1">
                                    <button type="button" onclick="stepVal('inpServingsPerContainer', -1, 1)" class="w-8 h-9 bg-slate-200 hover:bg-slate-300 font-bold rounded-l-lg text-slate-700">-</button>
                                    <input type="number" id="inpServingsPerContainer" value="10" min="1" step="1" oninput="calculateNutriExport()" class="w-full h-9 text-center text-xs font-mono font-bold border-y border-slate-200 focus:ring-0">
                                    <button type="button" onclick="stepVal('inpServingsPerContainer', 1, 1)" class="w-8 h-9 bg-slate-200 hover:bg-slate-300 font-bold rounded-r-lg text-slate-700">+</button>
                                </div>
                            </div>
                        </div>

                        <div>
                            <label class="text-[11px] font-bold text-slate-600 block">Household Measure &amp; Unit</label>
                            <input type="text" id="inpHouseholdMeasure" value="2 cookies (30g)" oninput="calculateNutriExport()" placeholder="E.g. 2 cookies (30g), 1 tbsp (15ml)" class="w-full mt-1 text-xs p-2 rounded-xl border border-slate-200 bg-white font-medium">
                        </div>
                    </div>

                    <!-- EU 100g Values Form -->
                    <div class="space-y-3">
                        <div class="flex items-center justify-between border-b border-slate-100 pb-2">
                            <span class="text-xs font-bold text-slate-800 uppercase tracking-wider flex items-center gap-1.5">
                                <span>🧪</span> <span>Average Lab Values per 100g (EU Standard)</span>
                            </span>
                            <span class="text-[10px] font-mono text-slate-500">Reg. 1169/2011</span>
                        </div>

                        <div class="grid grid-cols-2 gap-3">
                            <div>
                                <label class="text-[11px] font-bold text-slate-700 block">Energy (kcal / 100g)</label>
                                <input type="number" id="inpKcal100" value="480" min="0" step="1" oninput="calculateNutriExport()" class="w-full mt-1 text-xs font-mono font-bold p-2 rounded-xl border border-slate-200 bg-slate-50/50">
                            </div>
                            <div>
                                <label class="text-[11px] font-bold text-slate-700 block">Energy (kJ / 100g)</label>
                                <input type="number" id="inpKj100" value="2010" min="0" step="1" oninput="calculateNutriExport()" class="w-full mt-1 text-xs font-mono font-bold p-2 rounded-xl border border-slate-200 bg-slate-50/50">
                            </div>
                        </div>

                        <!-- Fats -->
                        <div class="grid grid-cols-3 gap-2 pt-1">
                            <div>
                                <label class="text-[10px] font-bold text-slate-700 block truncate">Total Fat (g)</label>
                                <input type="number" id="inpFat100" value="22" min="0" step="0.1" oninput="calculateNutriExport()" class="w-full mt-1 text-xs font-mono font-bold p-2 rounded-xl border border-slate-200">
                            </div>
                            <div>
                                <label class="text-[10px] font-bold text-slate-700 block truncate">Saturated Fat (g)</label>
                                <input type="number" id="inpSatFat100" value="10" min="0" step="0.1" oninput="calculateNutriExport()" class="w-full mt-1 text-xs font-mono font-bold p-2 rounded-xl border border-slate-200">
                            </div>
                            <div>
                                <label class="text-[10px] font-bold text-slate-700 block truncate">Trans Fat (g)</label>
                                <input type="number" id="inpTransFat100" value="0.1" min="0" step="0.05" oninput="calculateNutriExport()" class="w-full mt-1 text-xs font-mono font-bold p-2 rounded-xl border border-slate-200">
                            </div>
                        </div>

                        <!-- Cholesterol & Sodium / Salt -->
                        <div class="grid grid-cols-3 gap-2">
                            <div>
                                <label class="text-[10px] font-bold text-slate-700 block truncate">Cholesterol (mg)</label>
                                <input type="number" id="inpCholesterol100" value="15" min="0" step="1" oninput="calculateNutriExport()" class="w-full mt-1 text-xs font-mono font-bold p-2 rounded-xl border border-slate-200">
                            </div>
                            <div>
                                <label class="text-[10px] font-bold text-orange-700 block truncate">EU Salt (g)</label>
                                <input type="number" id="inpSalt100" value="0.75" min="0" step="0.01" oninput="syncFromSalt()" class="w-full mt-1 text-xs font-mono font-bold p-2 rounded-xl border border-orange-300 bg-orange-50/40">
                            </div>
                            <div>
                                <label class="text-[10px] font-bold text-blue-700 block truncate">US Sodium (mg)</label>
                                <input type="number" id="inpSodium100" value="300" min="0" step="1" oninput="syncFromSodium()" class="w-full mt-1 text-xs font-mono font-bold p-2 rounded-xl border border-blue-300 bg-blue-50/40">
                            </div>
                        </div>

                        <!-- Carbs, Fibers, Sugars -->
                        <div class="grid grid-cols-4 gap-2">
                            <div>
                                <label class="text-[10px] font-bold text-slate-700 block truncate">Carbohydrate (g)</label>
                                <input type="number" id="inpCarb100" value="64" min="0" step="0.1" oninput="calculateNutriExport()" class="w-full mt-1 text-xs font-mono font-bold p-2 rounded-xl border border-slate-200">
                            </div>
                            <div>
                                <label class="text-[10px] font-bold text-slate-700 block truncate">Dietary Fiber (g)</label>
                                <input type="number" id="inpFiber100" value="3.5" min="0" step="0.1" oninput="calculateNutriExport()" class="w-full mt-1 text-xs font-mono font-bold p-2 rounded-xl border border-slate-200">
                            </div>
                            <div>
                                <label class="text-[10px] font-bold text-slate-700 block truncate">Total Sugars (g)</label>
                                <input type="number" id="inpSugar100" value="28" min="0" step="0.1" oninput="calculateNutriExport()" class="w-full mt-1 text-xs font-mono font-bold p-2 rounded-xl border border-slate-200">
                            </div>
                            <div>
                                <label class="text-[10px] font-bold text-slate-700 block truncate">Added Sugars (g)</label>
                                <input type="number" id="inpAddedSugar100" value="25" min="0" step="0.1" oninput="calculateNutriExport()" class="w-full mt-1 text-xs font-mono font-bold p-2 rounded-xl border border-slate-200">
                            </div>
                        </div>

                        <!-- Proteins & Mandatory Micronutrients -->
                        <div class="grid grid-cols-2 gap-3">
                            <div>
                                <label class="text-[11px] font-bold text-slate-700 block">Protein (g / 100g)</label>
                                <input type="number" id="inpProtein100" value="6.5" min="0" step="0.1" oninput="calculateNutriExport()" class="w-full mt-1 text-xs font-mono font-bold p-2 rounded-xl border border-slate-200">
                            </div>
                            <div>
                                <label class="text-[11px] font-bold text-slate-700 block">Vitamin D (mcg / 100g)</label>
                                <input type="number" id="inpVitD100" value="0" min="0" step="0.1" oninput="calculateNutriExport()" class="w-full mt-1 text-xs font-mono font-bold p-2 rounded-xl border border-slate-200">
                            </div>
                        </div>

                        <div class="grid grid-cols-3 gap-2">
                            <div>
                                <label class="text-[10px] font-bold text-slate-700 block truncate">Calcium (mg / 100g)</label>
                                <input type="number" id="inpCalcium100" value="85" min="0" step="1" oninput="calculateNutriExport()" class="w-full mt-1 text-xs font-mono font-bold p-2 rounded-xl border border-slate-200">
                            </div>
                            <div>
                                <label class="text-[10px] font-bold text-slate-700 block truncate">Iron (mg / 100g)</label>
                                <input type="number" id="inpIron100" value="2.1" min="0" step="0.1" oninput="calculateNutriExport()" class="w-full mt-1 text-xs font-mono font-bold p-2 rounded-xl border border-slate-200">
                            </div>
                            <div>
                                <label class="text-[10px] font-bold text-slate-700 block truncate">Potassium (mg / 100g)</label>
                                <input type="number" id="inpPotassium100" value="180" min="0" step="1" oninput="calculateNutriExport()" class="w-full mt-1 text-xs font-mono font-bold p-2 rounded-xl border border-slate-200">
                            </div>
                        </div>
                    </div>

                    <!-- Action Buttons -->
                    <div class="pt-2 flex flex-wrap gap-2.5 no-print">
                        <button type="button" onclick="copyNutritionSpecs()" id="btnCopySpec" class="flex-1 py-2.5 px-4 bg-orange-600 hover:bg-orange-700 active:scale-95 text-white font-bold text-xs rounded-xl transition shadow-sm flex items-center justify-center gap-1.5 cursor-pointer">
                            <span>📋</span> <span>Copy FDA Spec</span>
                        </button>
                        <button type="button" onclick="exportNutriCsv()" class="py-2.5 px-3.5 bg-slate-100 hover:bg-slate-200 active:scale-95 text-slate-700 font-bold text-xs rounded-xl transition flex items-center gap-1 cursor-pointer">
                            <span>📊</span> <span>CSV</span>
                        </button>
                        <button type="button" onclick="window.print()" class="py-2.5 px-3.5 bg-slate-100 hover:bg-slate-200 active:scale-95 text-slate-700 font-bold text-xs rounded-xl transition flex items-center gap-1 cursor-pointer">
                            <span>🖨️</span> <span>Print A4</span>
                        </button>
                    </div>

                </div>

                <!-- Right Column: Visual Blueprint FDA Nutrition Facts Label (lg:col-span-6) -->
                <div class="lg:col-span-6 space-y-4">
                    <div class="flex items-center justify-between">
                        <span class="text-xs font-bold text-slate-700 uppercase tracking-wider flex items-center gap-1.5">
                            <span>🏷️</span> <span>Official FDA Nutrition Facts Preview</span>
                        </span>
                        <span class="text-[10px] font-mono font-bold text-emerald-700 bg-emerald-100 px-2 py-0.5 rounded-full">2016/2026 Format</span>
                    </div>

                    <!-- FDA Vertical Box Container -->
                    <div class="fda-label-box p-4 rounded-xl border-2 border-black max-w-sm mx-auto shadow-md">
                        <h2 class="text-3xl font-black uppercase tracking-tight leading-none text-black border-b-8 border-black pb-1">
                            Nutrition Facts
                        </h2>
                        
                        <div class="text-xs font-semibold py-1 border-b border-black flex justify-between">
                            <span id="lblServingsContainer">10 servings per container</span>
                        </div>
                        
                        <div class="text-sm font-black py-1 border-b-8 border-black flex justify-between items-baseline">
                            <span>Serving size</span>
                            <span id="lblServingSizeVal" class="font-bold">2 cookies (30g)</span>
                        </div>

                        <div class="py-1 border-b-4 border-black">
                            <div class="text-[10px] font-extrabold uppercase">Amount per serving</div>
                            <div class="flex justify-between items-baseline">
                                <span class="text-2xl font-black">Calories</span>
                                <span id="lblCaloriesVal" class="text-4xl font-black font-mono">140</span>
                            </div>
                        </div>

                        <div class="text-[10px] text-right font-black border-b border-black py-0.5">
                            % Daily Value*
                        </div>

                        <!-- Nutrients Table -->
                        <div class="divide-y divide-black text-xs font-normal">
                            <div class="py-1 flex justify-between">
                                <span><strong>Total Fat</strong> <span id="valTotalFat">7g</span></span>
                                <strong id="dvTotalFat" class="font-mono">9%</strong>
                            </div>
                            <div class="py-1 pl-4 flex justify-between">
                                <span>Saturated Fat <span id="valSatFat">3g</span></span>
                                <strong id="dvSatFat" class="font-mono">15%</strong>
                            </div>
                            <div class="py-1 pl-4 flex justify-between">
                                <span><em>Trans</em> Fat <span id="valTransFat">0g</span></span>
                                <span></span>
                            </div>
                            <div class="py-1 flex justify-between">
                                <span><strong>Cholesterol</strong> <span id="valCholesterol">5mg</span></span>
                                <strong id="dvCholesterol" class="font-mono">2%</strong>
                            </div>
                            <div class="py-1 flex justify-between">
                                <span><strong>Sodium</strong> <span id="valSodium">90mg</span></span>
                                <strong id="dvSodium" class="font-mono">4%</strong>
                            </div>
                            <div class="py-1 flex justify-between">
                                <span><strong>Total Carbohydrate</strong> <span id="valTotalCarb">19g</span></span>
                                <strong id="dvTotalCarb" class="font-mono">7%</strong>
                            </div>
                            <div class="py-1 pl-4 flex justify-between">
                                <span>Dietary Fiber <span id="valFiber">1g</span></span>
                                <strong id="dvFiber" class="font-mono">4%</strong>
                            </div>
                            <div class="py-1 pl-4 flex justify-between">
                                <span>Total Sugars <span id="valTotalSugar">8g</span></span>
                                <span></span>
                            </div>
                            <div class="py-1 pl-8 flex justify-between">
                                <span>Includes <span id="valAddedSugar">8g</span> Added Sugars</span>
                                <strong id="dvAddedSugar" class="font-mono">16%</strong>
                            </div>
                            <div class="py-1 flex justify-between border-b-4 border-black">
                                <span><strong>Protein</strong> <span id="valProtein">2g</span></span>
                                <span></span>
                            </div>
                            <div class="py-1 flex justify-between">
                                <span>Vitamin D <span id="valVitD">0mcg</span></span>
                                <span id="dvVitD" class="font-mono font-bold">0%</span>
                            </div>
                            <div class="py-1 flex justify-between">
                                <span>Calcium <span id="valCalcium">25mg</span></span>
                                <span id="dvCalcium" class="font-mono font-bold">2%</span>
                            </div>
                            <div class="py-1 flex justify-between">
                                <span>Iron <span id="valIron">0.6mg</span></span>
                                <span id="dvIron" class="font-mono font-bold">4%</span>
                            </div>
                            <div class="py-1 flex justify-between">
                                <span>Potassium <span id="valPotassium">55mg</span></span>
                                <span id="dvPotassium" class="font-mono font-bold">2%</span>
                            </div>
                        </div>

                        <div class="pt-2 text-[8px] leading-tight text-slate-700 border-t-4 border-black mt-1">
                            * The % Daily Value (DV) tells you how much a nutrient in a serving of food contributes to a daily diet. 2,000 calories a day is used for general nutrition advice.
                        </div>
                    </div>

                    <!-- KPI Benchmarks -->
                    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 pt-2">
                        <div class="p-2.5 bg-slate-50 rounded-xl border border-slate-200 text-center">
                            <span class="text-[9px] uppercase font-bold text-slate-500 block">Serving Ratio</span>
                            <span id="kpiServingRatio" class="text-sm font-mono font-black text-slate-800">0.30x</span>
                        </div>
                        <div class="p-2.5 bg-slate-50 rounded-xl border border-slate-200 text-center">
                            <span class="text-[9px] uppercase font-bold text-slate-500 block">Sodium / Serving</span>
                            <span id="kpiSodiumPerServing" class="text-sm font-mono font-black text-orange-600">90 mg</span>
                        </div>
                        <div class="p-2.5 bg-slate-50 rounded-xl border border-slate-200 text-center">
                            <span class="text-[9px] uppercase font-bold text-slate-500 block">Caloric Density</span>
                            <span id="kpiCaloricDensity" class="text-sm font-mono font-black text-slate-800">4.8 kcal/g</span>
                        </div>
                        <div class="p-2.5 bg-slate-50 rounded-xl border border-slate-200 text-center">
                            <span class="text-[9px] uppercase font-bold text-slate-500 block">Sugar % Calories</span>
                            <span id="kpiSugarCaloriesPct" class="text-sm font-mono font-black text-blue-600">23%</span>
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
                    <span>Frequently Asked Questions — FDA Nutrition Facts &amp; 21 CFR</span>
                </h2>
                <span class="text-[10px] font-extrabold uppercase px-2 py-0.5 rounded-full bg-slate-100 text-slate-600 border border-slate-200">FAQ</span>
            </div>

            <div id="faqContainer" class="space-y-3">
                <details class="group bg-slate-50/80 hover:bg-slate-50 rounded-2xl border border-slate-200/80 p-4 transition duration-150">
                    <summary class="flex justify-between items-center font-bold text-xs sm:text-sm text-slate-900 cursor-pointer list-none select-none">
                        <span>What is the key difference between EU nutrition declarations and US FDA labels?</span>
                        <span class="text-slate-400 group-open:rotate-180 transition-transform duration-200">▼</span>
                    </summary>
                    <p class="mt-2 text-xs text-slate-600 leading-relaxed">
                        In the European Union (Reg. EU 1169/2011), nutrition declaration is legally mandated per 100g or 100ml. In the United States (FDA 21 CFR 101.9), Nutrition Facts must be stated per standard serving size based on official RACC (Reference Amounts Customarily Consumed) categories.
                    </p>
                </details>

                <details class="group bg-slate-50/80 hover:bg-slate-50 rounded-2xl border border-slate-200/80 p-4 transition duration-150">
                    <summary class="flex justify-between items-center font-bold text-xs sm:text-sm text-slate-900 cursor-pointer list-none select-none">
                        <span>How do you convert European Salt (g) to American Sodium (mg)?</span>
                        <span class="text-slate-400 group-open:rotate-180 transition-transform duration-200">▼</span>
                    </summary>
                    <p class="mt-2 text-xs text-slate-600 leading-relaxed">
                        The stoichiometric formula is: Sodium (mg) = Salt (g) × 400. In reverse, Salt (g) = Sodium (mg) / 400.
                    </p>
                </details>

                <details class="group bg-slate-50/80 hover:bg-slate-50 rounded-2xl border border-slate-200/80 p-4 transition duration-150">
                    <summary class="flex justify-between items-center font-bold text-xs sm:text-sm text-slate-900 cursor-pointer list-none select-none">
                        <span>What are FDA's official rounding rules for calories and nutrients?</span>
                        <span class="text-slate-400 group-open:rotate-180 transition-transform duration-200">▼</span>
                    </summary>
                    <p class="mt-2 text-xs text-slate-600 leading-relaxed">
                        FDA 21 CFR 101.9 mandates specific rounding tiers: Calories below 5 kcal round to 0, up to 50 kcal round to nearest 5, and above 50 kcal round to nearest 10. Total fat under 0.5g rounds to 0g, between 0.5g and 5g rounds to nearest 0.5g, and 5g or above rounds to nearest 1g.
                    </p>
                </details>

                <details class="group bg-slate-50/80 hover:bg-slate-50 rounded-2xl border border-slate-200/80 p-4 transition duration-150">
                    <summary class="flex justify-between items-center font-bold text-xs sm:text-sm text-slate-900 cursor-pointer list-none select-none">
                        <span>Which micronutrients are federally mandatory on US Nutrition Facts labels?</span>
                        <span class="text-slate-400 group-open:rotate-180 transition-transform duration-200">▼</span>
                    </summary>
                    <p class="mt-2 text-xs text-slate-600 leading-relaxed">
                        Under the updated FDA framework, quantitative amounts and % Daily Values are mandatory for Vitamin D (mcg), Calcium (mg), Iron (mg), and Potassium (mg). Vitamins A and C are now voluntary.
                    </p>
                </details>

                <details class="group bg-slate-50/80 hover:bg-slate-50 rounded-2xl border border-slate-200/80 p-4 transition duration-150">
                    <summary class="flex justify-between items-center font-bold text-xs sm:text-sm text-slate-900 cursor-pointer list-none select-none">
                        <span>What does % Daily Value (% DV) signify?</span>
                        <span class="text-slate-400 group-open:rotate-180 transition-transform duration-200">▼</span>
                    </summary>
                    <p class="mt-2 text-xs text-slate-600 leading-relaxed">
                        The % Daily Value (% DV) indicates how much a nutrient in a serving contributes to a daily 2,000 calorie diet. As a general FDA benchmark: 5% DV or less is low, while 20% DV or more is high.
                    </p>
                </details>
            </div>
        </section>

        <!-- Legal Disclaimer & Safe Harbor -->
        <section id="legalDisclaimerBox" class="bg-amber-50/60 rounded-3xl border border-amber-200/90 shadow-xs p-5 sm:p-6 text-[11px] sm:text-xs text-slate-700 leading-relaxed space-y-2">
            <div class="font-extrabold text-slate-900 uppercase tracking-wider text-[11px] flex items-center gap-1.5">
                <span>⚖️</span> <span>US Regulatory Notice, Safe Harbor Disclaimer &amp; Liability Indemnity</span>
            </div>
            <p>
                <strong>1. Educational &amp; Pre-formatting Reference Only:</strong> This online application provides mathematical conversions and algorithmic roundings based on US FDA 21 CFR 101.9 guidelines strictly for preliminary planning, estimation, and pre-formatting reference. It does not provide certified legal, food safety, or customs compliance clearance under US federal law.
            </p>
            <p>
                <strong>2. Mandatory Laboratory Analytical Validation:</strong> Under FDA Preventive Controls for Human Food (FSMA / 21 CFR Part 117), food business operators must validate actual nutritional data via accredited ISO 17025 laboratories and consult qualified labeling specialists prior to commercial packaging print runs.
            </p>
            <p>
                <strong>3. Full Hold-Harmless Indemnity:</strong> By using this tool, the user agrees to hold harmless OmniTools Lab and its developers against any customs seizures, border holds, FDA Warning Letters, administrative penalties, or commercial losses resulting from labeling, formatting, or date conversions.
            </p>
        </section>

    </main>
"""

# EN calculation script
script_it = """<script>
        // FDA 2026 Daily Values (21 CFR 101.9)
        const FDA_DV = {
            fat: 78,
            satFat: 20,
            cholesterol: 300,
            sodium: 2300,
            carb: 275,
            fiber: 28,
            addedSugar: 50,
            vitD: 20,       // mcg
            calcium: 1300,  // mg
            iron: 18,       // mg
            potassium: 4700 // mg
        };

        function stepVal(id, delta, min) {
            const inp = document.getElementById(id);
            if (!inp) return;
            let v = parseFloat(inp.value) || 0;
            v = Math.max(min, v + delta);
            inp.value = v;
            calculateNutriExport();
        }

        function onRaccChange() {
            const sel = document.getElementById('selRaccPreset');
            const val = sel.value;
            if (val === 'custom') return;
            const parts = val.split('|');
            const grams = parseFloat(parts[0]) || 30;
            document.getElementById('inpServingGrams').value = grams;
            const measureInput = document.getElementById('inpHouseholdMeasure');
            if (measureInput) {
                if (parts[1] === 'biscotti') measureInput.value = `2 biscotti (${grams}g)`;
                else if (parts[1] === 'pane') measureInput.value = `1 fetta (${grams}g)`;
                else if (parts[1] === 'pasta') measureInput.value = `1 porzione secca (${grams}g)`;
                else if (parts[1] === 'formaggio') measureInput.value = `1 cubetto (${grams}g)`;
                else if (parts[1] === 'olio') measureInput.value = `1 cucchiaio (${grams}ml)`;
                else if (parts[1] === 'bevande') measureInput.value = `1 bicchiere (${grams}ml)`;
                else if (parts[1] === 'cioccolato') measureInput.value = `3 quadretti (${grams}g)`;
            }
            calculateNutriExport();
        }

        function syncFromSalt() {
            const salt = parseFloat(document.getElementById('inpSalt100').value) || 0;
            document.getElementById('inpSodium100').value = Math.round(salt * 400);
            calculateNutriExport();
        }

        function syncFromSodium() {
            const sodium = parseFloat(document.getElementById('inpSodium100').value) || 0;
            document.getElementById('inpSalt100').value = (sodium / 400).toFixed(2);
            calculateNutriExport();
        }

        // FDA Rounding Rules
        function roundCalories(c) {
            if (c < 5) return '0';
            if (c <= 50) return String(Math.round(c / 5) * 5);
            return String(Math.round(c / 10) * 10);
        }

        function roundFat(f) {
            if (f < 0.5) return '0g';
            if (f < 5) return (Math.round(f * 2) / 2).toFixed(1).replace('.0', '') + 'g';
            return String(Math.round(f)) + 'g';
        }

        function roundCholesterol(c) {
            if (c < 2) return '0mg';
            if (c <= 5) return '< 5mg';
            return String(Math.round(c / 5) * 5) + 'mg';
        }

        function roundSodium(s) {
            if (s < 5) return '0mg';
            if (s <= 140) return String(Math.round(s / 5) * 5) + 'mg';
            return String(Math.round(s / 10) * 10) + 'mg';
        }

        function roundCarbFiberSugar(c) {
            if (c < 0.5) return '0g';
            if (c < 1) return '< 1g';
            return String(Math.round(c)) + 'g';
        }

        function roundProtein(p) {
            if (p < 0.5) return '0g';
            if (p < 1) return '< 1g';
            return String(Math.round(p)) + 'g';
        }

        function calcDV(val, dvMax) {
            if (!val || val <= 0) return '0%';
            const pct = Math.round((val / dvMax) * 100);
            return pct + '%';
        }

        function calculateNutriExport() {
            const servingGrams = parseFloat(document.getElementById('inpServingGrams').value) || 30;
            const servingsPerContainer = parseFloat(document.getElementById('inpServingsPerContainer').value) || 1;
            const household = document.getElementById('inpHouseholdMeasure').value || `${servingGrams}g`;

            const ratio = servingGrams / 100.0;

            const kcal100 = parseFloat(document.getElementById('inpKcal100').value) || 0;
            const fat100 = parseFloat(document.getElementById('inpFat100').value) || 0;
            const satFat100 = parseFloat(document.getElementById('inpSatFat100').value) || 0;
            const transFat100 = parseFloat(document.getElementById('inpTransFat100').value) || 0;
            const chol100 = parseFloat(document.getElementById('inpCholesterol100').value) || 0;
            const sodium100 = parseFloat(document.getElementById('inpSodium100').value) || 0;
            const carb100 = parseFloat(document.getElementById('inpCarb100').value) || 0;
            const fiber100 = parseFloat(document.getElementById('inpFiber100').value) || 0;
            const sugar100 = parseFloat(document.getElementById('inpSugar100').value) || 0;
            const addedSugar100 = parseFloat(document.getElementById('inpAddedSugar100').value) || 0;
            const protein100 = parseFloat(document.getElementById('inpProtein100').value) || 0;
            const vitD100 = parseFloat(document.getElementById('inpVitD100').value) || 0;
            const calcium100 = parseFloat(document.getElementById('inpCalcium100').value) || 0;
            const iron100 = parseFloat(document.getElementById('inpIron100').value) || 0;
            const pot100 = parseFloat(document.getElementById('inpPotassium100').value) || 0;

            // Serving calculations
            const servKcal = kcal100 * ratio;
            const servFat = fat100 * ratio;
            const servSatFat = satFat100 * ratio;
            const servTransFat = transFat100 * ratio;
            const servChol = chol100 * ratio;
            const servSodium = sodium100 * ratio;
            const servCarb = carb100 * ratio;
            const servFiber = fiber100 * ratio;
            const servSugar = sugar100 * ratio;
            const servAddedSugar = addedSugar100 * ratio;
            const servProtein = protein100 * ratio;
            const servVitD = vitD100 * ratio;
            const servCalcium = calcium100 * ratio;
            const servIron = iron100 * ratio;
            const servPot = pot100 * ratio;

            // Update Label Headers
            document.getElementById('lblServingsContainer').textContent = `${servingsPerContainer} servings per container`;
            document.getElementById('lblServingSizeVal').textContent = household;
            document.getElementById('lblCaloriesVal').textContent = roundCalories(servKcal);

            // Update Macronutrients with Official Rounding & % DV
            document.getElementById('valTotalFat').textContent = roundFat(servFat);
            document.getElementById('dvTotalFat').textContent = calcDV(servFat, FDA_DV.fat);

            document.getElementById('valSatFat').textContent = roundFat(servSatFat);
            document.getElementById('dvSatFat').textContent = calcDV(servSatFat, FDA_DV.satFat);

            document.getElementById('valTransFat').textContent = roundFat(servTransFat);

            document.getElementById('valCholesterol').textContent = roundCholesterol(servChol);
            document.getElementById('dvCholesterol').textContent = calcDV(servChol, FDA_DV.cholesterol);

            document.getElementById('valSodium').textContent = roundSodium(servSodium);
            document.getElementById('dvSodium').textContent = calcDV(servSodium, FDA_DV.sodium);

            document.getElementById('valTotalCarb').textContent = roundCarbFiberSugar(servCarb);
            document.getElementById('dvTotalCarb').textContent = calcDV(servCarb, FDA_DV.carb);

            document.getElementById('valFiber').textContent = roundCarbFiberSugar(servFiber);
            document.getElementById('dvFiber').textContent = calcDV(servFiber, FDA_DV.fiber);

            document.getElementById('valTotalSugar').textContent = roundCarbFiberSugar(servSugar);
            document.getElementById('valAddedSugar').textContent = roundCarbFiberSugar(servAddedSugar);
            document.getElementById('dvAddedSugar').textContent = calcDV(servAddedSugar, FDA_DV.addedSugar);

            document.getElementById('valProtein').textContent = roundProtein(servProtein);

            // Micronutrients
            const vitDStr = servVitD < 0.1 ? '0mcg' : (servVitD.toFixed(1) + 'mcg');
            document.getElementById('valVitD').textContent = vitDStr;
            document.getElementById('dvVitD').textContent = calcDV(servVitD, FDA_DV.vitD);

            const calcStr = Math.round(servCalcium) + 'mg';
            document.getElementById('valCalcium').textContent = calcStr;
            document.getElementById('dvCalcium').textContent = calcDV(servCalcium, FDA_DV.calcium);

            const ironStr = servIron < 0.1 ? '0mg' : (servIron.toFixed(1) + 'mg');
            document.getElementById('valIron').textContent = ironStr;
            document.getElementById('dvIron').textContent = calcDV(servIron, FDA_DV.iron);

            const potStr = Math.round(servPot) + 'mg';
            document.getElementById('valPotassium').textContent = potStr;
            document.getElementById('dvPotassium').textContent = calcDV(servPot, FDA_DV.potassium);

            // KPI Benchmarks
            document.getElementById('kpiServingRatio').textContent = ratio.toFixed(2) + 'x';
            document.getElementById('kpiSodiumPerServing').textContent = roundSodium(servSodium);
            document.getElementById('kpiCaloricDensity').textContent = (kcal100 / 100).toFixed(1) + ' kcal/g';
            const sugarCalPct = servKcal > 0 ? Math.round(((servSugar * 4) / servKcal) * 100) : 0;
            document.getElementById('kpiSugarCaloriesPct').textContent = sugarCalPct + '%';

            // Print Summary
            const printSummary = document.getElementById('printInputsSummary');
            if (printSummary) {
                printSummary.innerHTML = `
                    <div><span class="text-slate-400 block">Porzione RACC:</span><strong>${household}</strong></div>
                    <div><span class="text-slate-400 block">Calorie FDA:</span><strong>${roundCalories(servKcal)} kcal</strong></div>
                    <div><span class="text-slate-400 block">Sodio / Porz:</span><strong>${roundSodium(servSodium)}</strong></div>
                    <div><span class="text-slate-400 block">Energia 100g:</span><strong>${kcal100} kcal</strong></div>
                `;
            }
            const printTs = document.getElementById('printTimestamp');
            if (printTs) printTs.textContent = new Date().toLocaleDateString('it-IT');
        }

        function copyNutritionSpecs() {
            const h = document.getElementById('inpHouseholdMeasure').value;
            const cal = document.getElementById('lblCaloriesVal').textContent;
            const fat = document.getElementById('valTotalFat').textContent;
            const sod = document.getElementById('valSodium').textContent;
            const carb = document.getElementById('valTotalCarb').textContent;
            const prot = document.getElementById('valProtein').textContent;
            const txt = `FDA Nutrition Facts (21 CFR 101.9): Serving: ${h} | Calories: ${cal} | Total Fat: ${fat} | Sodium: ${sod} | Total Carb: ${carb} | Protein: ${prot}`;
            navigator.clipboard.writeText(txt).then(() => {
                const btn = document.getElementById('btnCopySpec');
                const old = btn.innerHTML;
                btn.innerHTML = '<span>✓</span> <span>Copiato negli appunti!</span>';
                setTimeout(() => { btn.innerHTML = old; }, 2000);
            });
        }

        function exportNutriCsv() {
            const h = document.getElementById('inpHouseholdMeasure').value;
            const rows = [
                ['Nutriente FDA', 'Per Porzione Arrotondata', '% Daily Value', 'Valore UE per 100g'],
                ['Serving Size', h, '-', '100g'],
                ['Calories', document.getElementById('lblCaloriesVal').textContent + ' kcal', '-', document.getElementById('inpKcal100').value + ' kcal'],
                ['Total Fat', document.getElementById('valTotalFat').textContent, document.getElementById('dvTotalFat').textContent, document.getElementById('inpFat100').value + 'g'],
                ['Saturated Fat', document.getElementById('valSatFat').textContent, document.getElementById('dvSatFat').textContent, document.getElementById('inpSatFat100').value + 'g'],
                ['Trans Fat', document.getElementById('valTransFat').textContent, '-', document.getElementById('inpTransFat100').value + 'g'],
                ['Cholesterol', document.getElementById('valCholesterol').textContent, document.getElementById('dvCholesterol').textContent, document.getElementById('inpCholesterol100').value + 'mg'],
                ['Sodium', document.getElementById('valSodium').textContent, document.getElementById('dvSodium').textContent, document.getElementById('inpSodium100').value + 'mg'],
                ['Total Carbohydrate', document.getElementById('valTotalCarb').textContent, document.getElementById('dvTotalCarb').textContent, document.getElementById('inpCarb100').value + 'g'],
                ['Dietary Fiber', document.getElementById('valFiber').textContent, document.getElementById('dvFiber').textContent, document.getElementById('inpFiber100').value + 'g'],
                ['Total Sugars', document.getElementById('valTotalSugar').textContent, '-', document.getElementById('inpSugar100').value + 'g'],
                ['Added Sugars', document.getElementById('valAddedSugar').textContent, document.getElementById('dvAddedSugar').textContent, document.getElementById('inpAddedSugar100').value + 'g'],
                ['Protein', document.getElementById('valProtein').textContent, '-', document.getElementById('inpProtein100').value + 'g'],
                ['Vitamin D', document.getElementById('valVitD').textContent, document.getElementById('dvVitD').textContent, document.getElementById('inpVitD100').value + 'mcg'],
                ['Calcium', document.getElementById('valCalcium').textContent, document.getElementById('dvCalcium').textContent, document.getElementById('inpCalcium100').value + 'mg'],
                ['Iron', document.getElementById('valIron').textContent, document.getElementById('dvIron').textContent, document.getElementById('inpIron100').value + 'mg'],
                ['Potassium', document.getElementById('valPotassium').textContent, document.getElementById('dvPotassium').textContent, document.getElementById('inpPotassium100').value + 'mg']
            ];
            const csv = rows.map(r => r.map(v => `"${String(v).replace(/"/g, '""')}"`).join(',')).join('\n');
            const blob = new Blob([csv], { type: 'text/csv;charset=utf-8;' });
            const a = document.createElement('a');
            a.href = URL.createObjectURL(blob);
            a.download = 'omnitools_fda_nutrition_facts.csv';
            a.click();
        }

        document.addEventListener('DOMContentLoaded', () => {
            calculateNutriExport();
        });
    </script>"""
script_en = script_it.replace('new Date().toLocaleDateString(\'it-IT\')', 'new Date().toLocaleDateString(\'en-US\')')
script_en = script_en.replace('<span>Copiato negli appunti!</span>', '<span>Copied to clipboard!</span>')
script_en = script_en.replace('<div><span class="text-slate-400 block">Porzione RACC:</span>', '<div><span class="text-slate-400 block">RACC Serving:</span>')
script_en = script_en.replace('<div><span class="text-slate-400 block">Calorie FDA:</span>', '<div><span class="text-slate-400 block">FDA Calories:</span>')
script_en = script_en.replace('<div><span class="text-slate-400 block">Sodio / Porz:</span>', '<div><span class="text-slate-400 block">Sodium / Serv:</span>')
script_en = script_en.replace('<div><span class="text-slate-400 block">Energia 100g:</span>', '<div><span class="text-slate-400 block">Energy 100g:</span>')

full_en = head_en + "\n</head>\n" + top_en + "\n" + main_en + "\n" + script_en + "\n" + bottom_en

with open('Calcolatore_Pendenza/en/nutri-export-converter.html', 'w', encoding='utf-8') as f:
    f.write(full_en)

print(f"Generated Calcolatore_Pendenza/en/nutri-export-converter.html ({len(full_en)} bytes)")
