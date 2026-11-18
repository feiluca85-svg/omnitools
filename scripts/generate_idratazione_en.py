#!/usr/bin/env python3
import os
import re

print("Generating HygroBalance Lab (EN)...")

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

top_en = get_top_nav(en_source, "/idratazione", "HygroBalance Lab")

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
    <title>HygroBalance Lab: Real Dough Hydration &amp; Water Temperature Calculator | OmniTools Lab</title>
    <meta name="description" content="Thermodynamic real hydration calculator: uncover bound biological water in eggs, butter, milk, and sourdough, calculate mixer T-Base water temperature and flake ice dosage.">

    <!-- Canonical & SEO Meta Tags -->
    <link rel="canonical" href="https://www.omnitoolslab.com/en/hydration-balance-calculator" />
    <link rel="alternate" hreflang="it" href="https://www.omnitoolslab.com/idratazione" />
    <link rel="alternate" hreflang="en-US" href="https://www.omnitoolslab.com/en/hydration-balance-calculator" />
    <link rel="alternate" hreflang="en" href="https://www.omnitoolslab.com/en/hydration-balance-calculator" />
    <link rel="alternate" hreflang="x-default" href="https://www.omnitoolslab.com/en/hydration-balance-calculator" />
    
    <meta name="robots" content="index, follow">
    <meta property="og:type" content="website">
    <meta property="og:title" content="HygroBalance Lab: Real Hydration &amp; Water Temperature">
    <meta property="og:description" content="Calculate real vs apparent dough hydration, T-Base water temperature, and latent heat ice substitution to prevent overheating.">
    <meta property="og:url" content="https://www.omnitoolslab.com/en/hydration-balance-calculator">
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
    "name": "HygroBalance Lab — Real Dough Hydration & Water Temperature Calculator",
    "url": "https://www.omnitoolslab.com/en/hydration-balance-calculator",
    "applicationCategory": "BusinessApplication",
    "operatingSystem": "All",
    "description": "Scientific hydration calculator for artisan bakers and pizzaiolos: real vs apparent hydration (hidden water in dairy, eggs, levain), T-Base thermodynamic water temperature, and flake ice scaling.",
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
        "name": "HygroBalance Lab",
        "item": "https://www.omnitoolslab.com/en/hydration-balance-calculator"
      }
    ]
  },
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "What is the difference between apparent and real dough hydration?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Apparent hydration measures only added liquid water against flour weight (Water / Flour × 100). Real hydration accounts for all biological water bound inside ingredients (e.g. 75% in eggs, 16% in butter, 87.5% in milk) and factors in flour contributed by preferments or sourdough levain."
        }
      },
      {
        "@type": "Question",
        "name": "How is water temperature calculated using the T-Base rule?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The thermodynamic equation is: T_water = (3 × T_target_dough) - T_ambient - T_flour - ΔT_mixer_friction. Mechanical friction typically adds +9°C (+16°F) for spiral mixers, +4°C (+7°F) for diving arm mixers, +3°C (+5°F) for fork mixers, and +1°C (+2°F) for hand kneading."
        }
      },
      {
        "@type": "Question",
        "name": "When and why should water be substituted with flake ice?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "When the T-Base formula results in required water below +4°C (39°F)—which cannot be achieved with liquid tap water without freezing—flake ice is required. Utilizing the latent heat of fusion of ice (80 kcal/kg or 144 BTU/lb), ice absorbs friction heat rapidly without overhydrating the dough."
        }
      },
      {
        "@type": "Question",
        "name": "What is the exact calorimetry formula for ice substitution?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The calorimetry formula is: Ice (g) = [Total_water × (T_tap - T_calculated)] / (80 + T_tap). The calculated ice weight is subtracted from the liquid tap water poured into the mixer bowl."
        }
      },
      {
        "@type": "Question",
        "name": "How does sourdough levain affect hydration calculations?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Stiff sourdough (50% hydration) contains 33.3% water and 66.7% flour. Liquid levain (100% hydration) contains 50% water and 50% flour. The engine parses levain adding its moisture to total water and its dry matter to total flour."
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
                        <span class="text-[11px] font-bold text-slate-600">OmniFood • Dough Thermodynamics &amp; Hydration</span>
                    </div>
                    <h1 class="font-jakarta text-xl font-extrabold text-slate-900 leading-tight" id="printSheetTitle">Real Dough Hydration, T-Base &amp; Flake Ice Formulation</h1>
                    <p class="text-[10px] text-slate-500 mt-0.5">Biological Water Balancing • Latent Heat of Fusion of Ice (80 kcal/kg)</p>
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
                <span>💧</span> <span>Real vs Apparent Hydration</span> • <span>🌡️</span> <span>T-Base Rule</span> • <span>❄️</span> <span>Flake Ice Calculator</span>
            </div>
            <h1 id="heroTitle" class="font-jakarta text-2xl sm:text-3xl lg:text-4xl font-black text-slate-900 tracking-tight">
                HygroBalance Lab
            </h1>
            <p id="heroSubtitle" class="text-slate-600 text-xs sm:text-sm max-w-2xl mx-auto leading-relaxed">
                Scientific water balancing for bakeries and pizzerias: calculate <strong>real hydration</strong> (revealing hidden water in eggs, butter, milk) and exact <strong>water temperature</strong> with latent heat ice substitution to protect gluten structure.
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
                                <span>🌾</span> <span>Base Flour &amp; Free Liquid Water</span>
                            </span>
                            <span class="text-[10px] font-mono text-slate-500">Base Formula</span>
                        </div>

                        <div class="grid grid-cols-2 gap-3">
                            <div>
                                <label class="text-[11px] font-bold text-slate-700 block">Flour Added (g)</label>
                                <div class="flex items-center mt-1">
                                    <button type="button" onclick="stepVal('inpFlourGrams', -100, 100)" class="w-8 h-9 bg-slate-200 hover:bg-slate-300 font-bold rounded-l-lg text-slate-700">-</button>
                                    <input type="number" id="inpFlourGrams" value="1000" min="100" step="50" oninput="calculateHygroBalance()" class="w-full h-9 text-center text-xs font-mono font-bold border-y border-slate-200 focus:ring-0 bg-white">
                                    <button type="button" onclick="stepVal('inpFlourGrams', 100, 100)" class="w-8 h-9 bg-slate-200 hover:bg-slate-300 font-bold rounded-r-lg text-slate-700">+</button>
                                </div>
                            </div>
                            <div>
                                <label class="text-[11px] font-bold text-blue-700 block">Free Water Poured (g/ml)</label>
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
                                <span>🥚</span> <span>Moist Ingredients (Bound Water)</span>
                            </span>
                            <span class="text-[10px] font-mono text-orange-700 font-bold">Biological Water Coefficients</span>
                        </div>

                        <div class="grid grid-cols-2 sm:grid-cols-3 gap-2.5">
                            <div>
                                <label class="text-[10px] font-bold text-slate-700 block truncate">Whole Eggs (g) <span class="text-slate-400 font-normal">75% H2O</span></label>
                                <input type="number" id="inpHydroEggs" value="100" min="0" step="10" oninput="calculateHygroBalance()" class="w-full mt-0.5 text-xs font-mono font-bold p-1.5 rounded-lg border border-slate-200 bg-white">
                            </div>
                            <div>
                                <label class="text-[10px] font-bold text-slate-700 block truncate">Egg Yolks (g) <span class="text-slate-400 font-normal">50% H2O</span></label>
                                <input type="number" id="inpHydroYolk" value="0" min="0" step="10" oninput="calculateHygroBalance()" class="w-full mt-0.5 text-xs font-mono font-bold p-1.5 rounded-lg border border-slate-200 bg-white">
                            </div>
                            <div>
                                <label class="text-[10px] font-bold text-slate-700 block truncate">Butter (g) <span class="text-slate-400 font-normal">16% H2O</span></label>
                                <input type="number" id="inpHydroButter" value="80" min="0" step="10" oninput="calculateHygroBalance()" class="w-full mt-0.5 text-xs font-mono font-bold p-1.5 rounded-lg border border-slate-200 bg-white">
                            </div>
                            <div>
                                <label class="text-[10px] font-bold text-slate-700 block truncate">Whole Milk (g) <span class="text-slate-400 font-normal">87.5% H2O</span></label>
                                <input type="number" id="inpHydroMilk" value="0" min="0" step="20" oninput="calculateHygroBalance()" class="w-full mt-0.5 text-xs font-mono font-bold p-1.5 rounded-lg border border-slate-200 bg-white">
                            </div>
                            <div>
                                <label class="text-[10px] font-bold text-slate-700 block truncate">Heavy Cream (g) <span class="text-slate-400 font-normal">60% H2O</span></label>
                                <input type="number" id="inpHydroCream" value="0" min="0" step="20" oninput="calculateHygroBalance()" class="w-full mt-0.5 text-xs font-mono font-bold p-1.5 rounded-lg border border-slate-200 bg-white">
                            </div>
                            <div>
                                <label class="text-[10px] font-bold text-slate-700 block truncate">Honey (g) <span class="text-slate-400 font-normal">18% H2O</span></label>
                                <input type="number" id="inpHydroHoney" value="20" min="0" step="5" oninput="calculateHygroBalance()" class="w-full mt-0.5 text-xs font-mono font-bold p-1.5 rounded-lg border border-slate-200 bg-white">
                            </div>
                        </div>

                        <!-- Sourdough / Preferment -->
                        <div class="pt-2 border-t border-orange-200/40 grid grid-cols-2 gap-3">
                            <div>
                                <label class="text-[10px] font-bold text-slate-700 block">Sourdough / Levain Type</label>
                                <select id="selSourdoughType" onchange="calculateHygroBalance()" class="w-full mt-0.5 text-xs font-bold p-1.5 rounded-lg border border-slate-200 bg-white">
                                    <option value="none">None (Commercial yeast only)</option>
                                    <option value="solid">Stiff Levain 50% (33.3% H2O, 66.7% flour)</option>
                                    <option value="licoli">Liquid Levain 100% (50% H2O, 50% flour)</option>
                                </select>
                            </div>
                            <div>
                                <label class="text-[10px] font-bold text-slate-700 block">Levain Weight (g)</label>
                                <input type="number" id="inpHydroSourdoughGrams" value="0" min="0" step="25" oninput="calculateHygroBalance()" class="w-full mt-0.5 text-xs font-mono font-bold p-1.5 rounded-lg border border-slate-200 bg-white">
                            </div>
                        </div>
                    </div>

                    <!-- Section 3: Thermodynamic T-Base & Mixer Friction -->
                    <div class="p-4 bg-blue-50/50 rounded-2xl border border-blue-200/70 space-y-3">
                        <div class="flex items-center justify-between border-b border-blue-200/60 pb-1.5">
                            <span class="text-xs font-bold text-blue-900 uppercase tracking-wider flex items-center gap-1.5">
                                <span>🌡️</span> <span>Thermodynamic T-Base &amp; Ice Scaling</span>
                            </span>
                            <span class="text-[10px] font-mono font-bold text-blue-700">T_water = 3×T_target - T_amb - T_flour - ΔT</span>
                        </div>

                        <div class="grid grid-cols-3 gap-2">
                            <div>
                                <label class="text-[10px] font-bold text-slate-700 block truncate">Target Dough (°C)</label>
                                <input type="number" id="inpTempTarget" value="25.0" min="18" max="32" step="0.5" oninput="calculateHygroBalance()" class="w-full mt-0.5 text-xs font-mono font-bold p-1.5 rounded-lg border border-slate-200 bg-white">
                            </div>
                            <div>
                                <label class="text-[10px] font-bold text-slate-700 block truncate">Room Temp (°C)</label>
                                <input type="number" id="inpTempAmb" value="24.0" min="10" max="42" step="0.5" oninput="calculateHygroBalance()" class="w-full mt-0.5 text-xs font-mono font-bold p-1.5 rounded-lg border border-slate-200 bg-white">
                            </div>
                            <div>
                                <label class="text-[10px] font-bold text-slate-700 block truncate">Flour Temp (°C)</label>
                                <input type="number" id="inpTempFlour" value="23.0" min="10" max="35" step="0.5" oninput="calculateHygroBalance()" class="w-full mt-0.5 text-xs font-mono font-bold p-1.5 rounded-lg border border-slate-200 bg-white">
                            </div>
                        </div>

                        <div class="grid grid-cols-2 gap-3 pt-1">
                            <div>
                                <label class="text-[10px] font-bold text-slate-700 block">Mixer Type (Friction Heat)</label>
                                <select id="selMixerFriction" onchange="calculateHygroBalance()" class="w-full mt-0.5 text-xs font-bold p-1.5 rounded-lg border border-slate-200 bg-white">
                                    <option value="9">Spiral Mixer (+9°C / +16°F)</option>
                                    <option value="4">Diving Arms (+4°C / +7°F)</option>
                                    <option value="3">Fork Mixer (+3°C / +5°F)</option>
                                    <option value="6">Planetary Mixer (+6°C / +11°F)</option>
                                    <option value="1">Hand Kneading (+1°C / +2°F)</option>
                                </select>
                            </div>
                            <div>
                                <label class="text-[10px] font-bold text-slate-700 block">Tap Water Temp (°C)</label>
                                <input type="number" id="inpTempTap" value="18.0" min="4" max="30" step="1" oninput="calculateHygroBalance()" class="w-full mt-0.5 text-xs font-mono font-bold p-1.5 rounded-lg border border-slate-200 bg-white">
                            </div>
                        </div>
                    </div>

                    <!-- Action Buttons -->
                    <div class="pt-2 flex flex-wrap gap-2.5 no-print">
                        <button type="button" onclick="copyHygroSpec()" id="btnCopyHygro" class="flex-1 py-2.5 px-4 bg-orange-600 hover:bg-orange-700 active:scale-95 text-white font-bold text-xs rounded-xl transition shadow-sm flex items-center justify-center gap-1.5 cursor-pointer">
                            <span>📋</span> <span>Copy Hydration Spec</span>
                        </button>
                        <button type="button" onclick="exportHygroCsv()" class="py-2.5 px-3.5 bg-slate-100 hover:bg-slate-200 active:scale-95 text-slate-700 font-bold text-xs rounded-xl transition flex items-center gap-1 cursor-pointer">
                            <span>📊</span> <span>CSV</span>
                        </button>
                        <button type="button" onclick="window.print()" class="py-2.5 px-3.5 bg-slate-100 hover:bg-slate-200 active:scale-95 text-slate-700 font-bold text-xs rounded-xl transition flex items-center gap-1 cursor-pointer">
                            <span>🖨️</span> <span>Print A4</span>
                        </button>
                    </div>

                </div>

                <!-- Right Column: Visual Blueprint CAD Thermometer & Hydration Dial (lg:col-span-6) -->
                <div class="lg:col-span-6 space-y-4">
                    <div class="flex items-center justify-between">
                        <span class="text-xs font-bold text-slate-700 uppercase tracking-wider flex items-center gap-1.5">
                            <span>❄️</span> <span>Thermodynamic Thermometer &amp; Hydration Balance</span>
                        </span>
                        <span id="badgeIceAlert" class="hidden text-[10px] font-mono font-bold text-rose-700 bg-rose-100 px-2 py-0.5 rounded-full animate-pulse">ICE THRESHOLD ACTIVE</span>
                    </div>

                    <!-- Dual CAD Visual Blueprint SVG -->
                    <div class="bg-slate-900 rounded-2xl p-4 border border-slate-800 shadow-md">
                        <svg class="svg-blueprint w-full h-48 sm:h-56" viewBox="0 0 500 220" role="img" aria-label="Thermodynamic Water &amp; Hydration Blueprint">
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
                            <text x="80" y="143" fill="#38bdf8" font-size="9" font-weight="bold" font-family="'JetBrains Mono', monospace">4°C (Ice Threshold)</text>

                            <text id="svgTxtWaterTemp" x="46" y="210" fill="#38bdf8" font-size="12" font-weight="bold" font-family="'JetBrains Mono', monospace" text-anchor="middle">T: 19.0°C</text>

                            <!-- Balance Dial / Hydration Stack (Right 300px) -->
                            <rect x="180" y="30" width="300" height="34" rx="6" fill="#1e293b" stroke="#334155" />
                            <rect id="svgBarFreeWater" x="182" y="32" width="180" height="30" rx="4" fill="#0284c7" />
                            <rect id="svgBarBoundWater" x="364" y="32" width="60" height="30" rx="4" fill="#f59e0b" />
                            <text id="svgTxtHydrationSplit" x="330" y="52" fill="#ffffff" font-size="10" font-weight="bold" font-family="'JetBrains Mono', monospace" text-anchor="middle">Free: 600g | Bound: 102g</text>

                            <!-- Dual Hydration Badges -->
                            <rect x="180" y="75" width="145" height="50" rx="8" fill="#0f172a" stroke="#334155" />
                            <text x="252" y="93" fill="#94a3b8" font-size="9" font-weight="bold" text-anchor="middle">APPARENT HYDRATION</text>
                            <text id="svgTxtApparentPct" x="252" y="116" fill="#38bdf8" font-size="18" font-weight="bold" font-family="'JetBrains Mono', monospace" text-anchor="middle">60.0%</text>

                            <rect x="335" y="75" width="145" height="50" rx="8" fill="#0f172a" stroke="#ea580c" />
                            <text x="407" y="93" fill="#fb923c" font-size="9" font-weight="bold" text-anchor="middle">REAL HYDRATION</text>
                            <text id="svgTxtRealPct" x="407" y="116" fill="#f97316" font-size="18" font-weight="bold" font-family="'JetBrains Mono', monospace" text-anchor="middle">70.2%</text>

                            <!-- Ice Substitution Callout Banner -->
                            <rect id="svgIceBox" x="180" y="135" width="300" height="55" rx="8" fill="#1e293b" stroke="#0284c7" stroke-dasharray="3 3" />
                            <text id="svgTxtIceTitle" x="330" y="155" fill="#38bdf8" font-size="10" font-weight="bold" font-family="'JetBrains Mono', monospace" text-anchor="middle">Tap Water Dosage</text>
                            <text id="svgTxtIceDetails" x="330" y="175" fill="#ffffff" font-size="11" font-weight="bold" font-family="'JetBrains Mono', monospace" text-anchor="middle">No ice required (T &gt;= 4°C)</text>
                        </svg>
                    </div>

                    <!-- Water & Ice Production Breakdown Table -->
                    <div class="border border-slate-200 rounded-2xl overflow-hidden bg-white shadow-xs">
                        <div class="bg-slate-100/80 px-4 py-2 border-b border-slate-200 flex justify-between items-center text-xs font-bold text-slate-800">
                            <span>Mixer Liquid Dosage Formulation</span>
                            <span class="text-[10px] font-mono text-slate-500">T-Base Calculations</span>
                        </div>
                        <div class="divide-y divide-slate-100 text-xs">
                            <div class="p-2.5 flex justify-between items-center bg-blue-50/40">
                                <div>
                                    <strong class="text-blue-950 block">Liquid Tap Water to Measure</strong>
                                    <span id="subLiquidWater" class="text-[10px] text-blue-600">At ambient tap temperature</span>
                                </div>
                                <span id="resLiquidWaterGrams" class="font-mono font-black text-blue-700 text-sm">600 g</span>
                            </div>
                            <div id="rowIceResult" class="p-2.5 flex justify-between items-center bg-sky-50/40">
                                <div>
                                    <strong class="text-sky-950 block">Flake Ice (Substitution)</strong>
                                    <span id="subIce" class="text-[10px] text-sky-600">Latent heat of fusion 80 kcal/kg</span>
                                </div>
                                <span id="resIceGrams" class="font-mono font-black text-sky-700 text-sm">0 g</span>
                            </div>
                            <div class="p-2 flex justify-between items-center">
                                <div>
                                    <span class="text-slate-800 block">Biological Bound Water</span>
                                    <span id="subBoundWater" class="text-[10px] text-slate-500">From eggs, butter, milk, levain</span>
                                </div>
                                <span id="resBoundWaterGrams" class="font-mono font-bold text-orange-600">102 g</span>
                            </div>
                            <div class="p-2 flex justify-between items-center">
                                <div>
                                    <span class="text-slate-800 block">Total Real Water in Gluten Matrix</span>
                                    <span class="text-[10px] text-slate-500">Free Water + Bound Water</span>
                                </div>
                                <span id="resTotalWaterGrams" class="font-mono font-bold text-slate-900">702 g</span>
                            </div>
                        </div>
                    </div>

                    <!-- Output KPI Grid -->
                    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 pt-1">
                        <div class="p-2.5 bg-slate-50 rounded-xl border border-slate-200 text-center">
                            <span class="text-[9px] uppercase font-bold text-slate-500 block">Req. Water Temp</span>
                            <span id="kpiCalculatedTemp" class="text-sm font-mono font-black text-blue-600">19.0°C</span>
                        </div>
                        <div class="p-2.5 bg-slate-50 rounded-xl border border-slate-200 text-center">
                            <span class="text-[9px] uppercase font-bold text-slate-500 block">Real Hydration</span>
                            <span id="kpiRealHydration" class="text-sm font-mono font-black text-orange-600">70.2%</span>
                        </div>
                        <div class="p-2.5 bg-slate-50 rounded-xl border border-slate-200 text-center">
                            <span class="text-[9px] uppercase font-bold text-slate-500 block">Hidden Water</span>
                            <span id="kpiBoundWaterPct" class="text-sm font-mono font-black text-slate-800">+10.2%</span>
                        </div>
                        <div class="p-2.5 bg-slate-50 rounded-xl border border-slate-200 text-center">
                            <span class="text-[9px] uppercase font-bold text-slate-500 block">Flake Ice Needed</span>
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
                    <span>Frequently Asked Questions — Real Hydration &amp; T-Base Calculations</span>
                </h2>
                <span class="text-[10px] font-extrabold uppercase px-2 py-0.5 rounded-full bg-slate-100 text-slate-600 border border-slate-200">FAQ</span>
            </div>

            <div id="faqContainer" class="space-y-3">
                <details class="group bg-slate-50/80 hover:bg-slate-50 rounded-2xl border border-slate-200/80 p-4 transition duration-150">
                    <summary class="flex justify-between items-center font-bold text-xs sm:text-sm text-slate-900 cursor-pointer list-none select-none">
                        <span>What is the difference between apparent and real dough hydration?</span>
                        <span class="text-slate-400 group-open:rotate-180 transition-transform duration-200">▼</span>
                    </summary>
                    <p class="mt-2 text-xs text-slate-600 leading-relaxed">
                        Apparent hydration measures only added liquid water against flour weight (Water / Flour × 100). Real hydration accounts for all biological water bound inside ingredients (e.g. 75% in eggs, 16% in butter, 87.5% in milk) and factors in flour contributed by preferments or sourdough levain.
                    </p>
                </details>

                <details class="group bg-slate-50/80 hover:bg-slate-50 rounded-2xl border border-slate-200/80 p-4 transition duration-150">
                    <summary class="flex justify-between items-center font-bold text-xs sm:text-sm text-slate-900 cursor-pointer list-none select-none">
                        <span>How is water temperature calculated using the T-Base rule?</span>
                        <span class="text-slate-400 group-open:rotate-180 transition-transform duration-200">▼</span>
                    </summary>
                    <p class="mt-2 text-xs text-slate-600 leading-relaxed">
                        The thermodynamic equation is: T_water = (3 × T_target_dough) - T_ambient - T_flour - ΔT_mixer_friction. Mechanical friction typically adds +9°C (+16°F) for spiral mixers, +4°C (+7°F) for diving arm mixers, +3°C (+5°F) for fork mixers, and +1°C (+2°F) for hand kneading.
                    </p>
                </details>

                <details class="group bg-slate-50/80 hover:bg-slate-50 rounded-2xl border border-slate-200/80 p-4 transition duration-150">
                    <summary class="flex justify-between items-center font-bold text-xs sm:text-sm text-slate-900 cursor-pointer list-none select-none">
                        <span>When and why should water be substituted with flake ice?</span>
                        <span class="text-slate-400 group-open:rotate-180 transition-transform duration-200">▼</span>
                    </summary>
                    <p class="mt-2 text-xs text-slate-600 leading-relaxed">
                        When the T-Base formula results in required water below +4°C (39°F)—which cannot be achieved with liquid tap water without freezing—flake ice is required. Utilizing the latent heat of fusion of ice (80 kcal/kg or 144 BTU/lb), ice absorbs friction heat rapidly without overhydrating the dough.
                    </p>
                </details>

                <details class="group bg-slate-50/80 hover:bg-slate-50 rounded-2xl border border-slate-200/80 p-4 transition duration-150">
                    <summary class="flex justify-between items-center font-bold text-xs sm:text-sm text-slate-900 cursor-pointer list-none select-none">
                        <span>What is the exact calorimetry formula for ice substitution?</span>
                        <span class="text-slate-400 group-open:rotate-180 transition-transform duration-200">▼</span>
                    </summary>
                    <p class="mt-2 text-xs text-slate-600 leading-relaxed">
                        The calorimetry formula is: Ice (g) = [Total_water × (T_tap - T_calculated)] / (80 + T_tap). The calculated ice weight is subtracted from the liquid tap water poured into the mixer bowl.
                    </p>
                </details>

                <details class="group bg-slate-50/80 hover:bg-slate-50 rounded-2xl border border-slate-200/80 p-4 transition duration-150">
                    <summary class="flex justify-between items-center font-bold text-xs sm:text-sm text-slate-900 cursor-pointer list-none select-none">
                        <span>How does sourdough levain affect hydration calculations?</span>
                        <span class="text-slate-400 group-open:rotate-180 transition-transform duration-200">▼</span>
                    </summary>
                    <p class="mt-2 text-xs text-slate-600 leading-relaxed">
                        Stiff sourdough (50% hydration) contains 33.3% water and 66.7% flour. Liquid levain (100% hydration) contains 50% water and 50% flour. The engine parses levain adding its moisture to total water and its dry matter to total flour.
                    </p>
                </details>
            </div>
        </section>

        <!-- Legal Disclaimer & Safe Harbor -->
        <section id="legalDisclaimerBox" class="bg-amber-50/60 rounded-3xl border border-amber-200/90 shadow-xs p-5 sm:p-6 text-[11px] sm:text-xs text-slate-700 leading-relaxed space-y-2">
            <div class="font-extrabold text-slate-900 uppercase tracking-wider text-[11px] flex items-center gap-1.5">
                <span>⚖️</span> <span>Thermodynamic Physics Notice &amp; Bakery Indemnity</span>
            </div>
            <p>
                <strong>1. Theoretical Modeling &amp; Thermal Variances:</strong> Calorimetric formulas and biological moisture constants represent thermodynamic engineering models. Actual dough temperature varies according to mixing bowl load volume, motor heat dissipation, and room ambient fluctuations.
            </p>
            <p>
                <strong>2. Full Hold-Harmless:</strong> OmniTools Lab and its developers provide these calculations for artisanal precision reference without liability for dough degradation, gluten breakdown, or commercial bakery losses.
            </p>
        </section>

    </main>
"""

# Script EN
with open('Calcolatore_Pendenza/idratazione.html', 'r', encoding='utf-8') as f:
    idr_it = f.read()

s_start = idr_it.find('<script>\n        function stepVal')
s_end = idr_it.find('</script>', s_start) + 9
script_text = idr_it[s_start:s_end]

script_en = script_text.replace('new Date().toLocaleDateString(\'it-IT\')', 'new Date().toLocaleDateString(\'en-US\')')
script_en = script_en.replace('<span>Dati Copiati!</span>', '<span>Data Copied!</span>')
script_en = script_en.replace('<div><span class="text-slate-400 block">Farina Totale:</span>', '<div><span class="text-slate-400 block">Total Flour:</span>')
script_en = script_en.replace('<div><span class="text-slate-400 block">Idratazione Reale:</span>', '<div><span class="text-slate-400 block">Real Hydration:</span>')
script_en = script_en.replace('<div><span class="text-slate-400 block">T-Acqua Calcolata:</span>', '<div><span class="text-slate-400 block">Req. Water Temp:</span>')
script_en = script_en.replace('<div><span class="text-slate-400 block">Ghiaccio Richiesto:</span>', '<div><span class="text-slate-400 block">Flake Ice Needed:</span>')
script_en = script_en.replace('⚠️ Richiesto Ghiaccio a Scaglie:', '⚠️ Flake Ice Required:')
script_en = script_en.replace('Acqua Liquida:', 'Liquid Water:')
script_en = script_en.replace('Ghiaccio:', 'Ice:')
script_en = script_en.replace('Dosaggio Acqua di Rubinetto', 'Tap Water Dosage')
script_en = script_en.replace('Versare', 'Pour')
script_en = script_en.replace('(Nessun ghiaccio)', '(No ice needed)')
script_en = script_en.replace('Libera:', 'Free:')
script_en = script_en.replace('Nascosta:', 'Bound:')

full_en = head_en + "\n</head>\n" + top_en + "\n" + main_en + "\n" + script_en + "\n" + bottom_en

with open('Calcolatore_Pendenza/en/hydration-balance-calculator.html', 'w', encoding='utf-8') as f:
    f.write(full_en)

print(f"Generated Calcolatore_Pendenza/en/hydration-balance-calculator.html ({len(full_en)} bytes)")
