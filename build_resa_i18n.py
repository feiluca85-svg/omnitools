import json
import os
from nav_header import render_suite_header, render_suite_header_js
from unified_footer import render_unified_footer, render_unified_footer_js

# Load translations
with open('/Users/ilalu/Documents/Altenative Businnes/Calcolatore_Pendenza/translations_resa.json', 'r', encoding='utf-8') as f:
    t_data = json.load(f)

t_json_str = json.dumps(t_data, ensure_ascii=False)

header_html = render_suite_header("resa")
header_js = render_suite_header_js()

footer_html = render_unified_footer("resa", disclaimer_id="legalDisclaimerText", disclaimer_default=t_data["it"]["legal_disclaimer"])
footer_js = render_unified_footer_js()

it_t = t_data["it"]

html_code = f"""<!DOCTYPE html>
<html lang="it">
<head>
    <meta name="google-site-verification" content="MRdbDm9lLhokeD3I0FOpUSOhNaF_2WaveKvu52FxtG4">
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0">
    <title>Calcolo Resa Carta & Schema di Taglio Online | Imposizione Fogli Macchina</title>
    <meta name="description" content="Calcolatore professionale di resa carta tipografica. Ottimizza il taglio dei fogli macchina 70x100, 64x88, SRA3, calcola le pose, minimizza lo sfrido e verifica il senso di fibra.">
    
    <!-- Canonical & SEO Meta Tags -->
    <link rel="canonical" href="https://www.omnitoolslab.com/resa">
    <meta name="robots" content="index, follow">
    <meta property="og:type" content="website">
    <meta property="og:title" content="ResaCarta — Calcolo Resa Carta & Schema di Taglio Tipografico">
    <meta property="og:description" content="Ottimizza la resa dei fogli macchina, calcola il numero di pose con disposizione dritta o mista, azzera lo sfrido e verifica il senso di fibra per la piega.">
    <meta property="og:url" content="https://www.omnitoolslab.com/resa">
    <meta property="og:site_name" content="OmniTools Lab">
    <meta property="og:image" content="https://www.omnitoolslab.com/og-graph.png">
    <meta name="twitter:card" content="summary_large_image">

    <!-- Schema.org JSON-LD Structured Data (WebApplication + FAQPage) -->
    <script type="application/ld+json">
    [
      {{
        "@context": "https://schema.org",
        "@type": "WebApplication",
        "name": "ResaCarta — Ottimizzazione Taglio Fogli Macchina",
        "url": "https://www.omnitoolslab.com/resa",
        "applicationCategory": "DesignApplication",
        "operatingSystem": "All",
        "description": "Applicazione professionale per grafici, tipografi e preventivisti: calcolo della resa di taglio dai fogli macchina, disposizione con e senza rotazione, sfrido % e verifica senso fibra.",
        "offers": {{
          "@type": "Offer",
          "price": "0",
          "priceCurrency": "EUR"
        }}
      }},
      {{
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
          {{
            "@type": "Question",
            "name": "Come si calcola la resa di taglio di un foglio macchina?",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "La resa si calcola confrontando la disposizione dritta con la disposizione ruotata a 90 gradi e la combinazione mista, tenendo conto dei margini di pinza macchina e dei refili tra le pose."
            }}
          }},
          {{
            "@type": "Question",
            "name": "Perché il senso di fibra della carta è fondamentale per la piega?",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "Se la piega viene effettuata in controfibra (perpendicolare alle fibre di cellulosa), il cartoncino si spacca e i volumi resistono all'apertura piatta. La linea di piega deve essere parallela alla fibra."
            }}
          }},
          {{
            "@type": "Question",
            "name": "Quanto spazio bisogna riservare per la pinza macchina?",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "Nelle macchine offset tradizionali il margine di presa pinza è solitamente compreso tra 10 e 15 mm su un lato lungo. Nelle macchine digitali il bordo non stampabile è solitamente tra 3 e 5 mm."
            }}
          }},
          {{
            "@type": "Question",
            "name": "Come si calcola il peso della carta da ordinare?",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "Formula: Peso (kg) = (Base foglio in m × Altezza foglio in m × Grammatura in gsm × Totale fogli) / 1000."
            }}
          }}
        ]
      }}
    ]
    </script>

    <!-- PWA & Mobile Icons -->
    <link rel="manifest" href="manifest-graph.json">
    <link rel="icon" type="image/svg+xml" href="favicon.svg?v=6">
    <link rel="apple-touch-icon" href="icon-graph-192.png">
    <meta name="theme-color" content="#d97706">
    <meta name="mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
    <meta name="apple-mobile-web-app-title" content="ResaCarta">

    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <script defer src="/_vercel/insights/script.js"></script>

    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@500;700;800&display=swap" rel="stylesheet">

    <script>
        tailwind.config = {{
            theme: {{
                extend: {{
                    fontFamily: {{
                        sans: ['"Plus Jakarta Sans"', 'system-ui', 'sans-serif'],
                        jakarta: ['"Plus Jakarta Sans"', 'sans-serif'],
                        mono: ['"JetBrains Mono"', 'monospace']
                    }}
                }}
            }}
        }}
    </script>

    <style>
        @media print {{
            @page {{
                size: A4 portrait;
                margin: 7mm 7mm 7mm 7mm;
            }}
            body {{
                background: white !important;
                color: black !important;
                font-size: 8.5pt !important;
                line-height: 1.25 !important;
                -webkit-print-color-adjust: exact !important;
                print-color-adjust: exact !important;
            }}
            .no-print {{
                display: none !important;
            }}
            .print-only {{
                display: block !important;
            }}
            .page-container {{
                max-width: 100% !important;
                padding: 0 !important;
                margin: 0 !important;
            }}
            #mainGrid {{
                display: grid !important;
                grid-template-columns: repeat(12, minmax(0, 1fr)) !important;
                gap: 10px !important;
            }}
            #svgContainer {{
                max-height: 220px !important;
            }}
        }}
        .print-only {{
            display: none;
        }}
    </style>
</head>
<body class="bg-slate-50 text-slate-800 font-sans antialiased min-h-screen flex flex-col justify-between selection:bg-amber-500 selection:text-white">

{header_html}

    <!-- DEDICATED PRINT HEADER (Strict A4 Print Only) -->
    <div class="print-only mb-3 border-b-2 border-slate-800 pb-2">
        <div class="flex items-center justify-between">
            <div class="flex items-center gap-2">
                <span class="text-xl">📑</span>
                <div>
                    <h1 class="text-sm font-extrabold uppercase tracking-tight text-slate-900">OmniGraph • ResaCarta</h1>
                    <p class="text-[8pt] font-semibold text-slate-600">Scheda Tecnica di Taglio & Imposizione Fogli Macchina</p>
                </div>
            </div>
            <div class="text-right text-[8pt] text-slate-600 font-mono">
                <div>Data: <span id="printDate">--/--/----</span></div>
                <div class="font-bold text-amber-700">SPECIFICA DI TAGLIO GHIGLIOTTINA</div>
            </div>
        </div>
    </div>

    <!-- MAIN CONTAINER (Unified max-w-5xl, Centered Hero, Coherent Suite Padding) -->
    <main class="max-w-5xl mx-auto px-3 sm:px-6 py-2.5 sm:py-5 flex-1 w-full space-y-3 sm:space-y-5 page-container">
        
        <!-- Hero Header -->
        <div id="heroContainer" class="no-print text-center max-w-2xl mx-auto space-y-1.5 sm:space-y-2 pt-1 sm:pt-2">
            <div class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-amber-50 border border-amber-200/80 text-[11px] font-extrabold text-amber-800 tracking-wide uppercase">
                <span>📑</span>
                <span id="badgeText">OmniGraph · Prestampa & Tipografia</span>
            </div>
            <h1 id="heroTitle" class="text-2xl sm:text-3xl md:text-4xl font-extrabold font-jakarta text-slate-900 tracking-tight leading-tight">
                {it_t["hero_title"]}
            </h1>
            <p id="heroDesc" class="text-xs sm:text-sm text-slate-600 max-w-2xl mx-auto leading-relaxed">
                {it_t["hero_desc"]}
            </p>
            <div class="pt-1">
                <span id="privacyBadge" class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-[11px] font-bold bg-emerald-50 text-emerald-800 border border-emerald-200 shadow-2xs">
                    {it_t["privacy_badge"]}
                </span>
            </div>
        </div>

        <!-- MAIN INTERACTIVE GRID -->
        <div id="mainGrid" class="grid grid-cols-1 lg:grid-cols-12 gap-5 items-start">

            <!-- LEFT COLUMN: CONTROLS & SETTINGS (5 COLS) -->
            <div class="lg:col-span-5 flex flex-col gap-4">
                
                <!-- FORMAT PRESETS & SIZES -->
                <div class="bg-white rounded-2xl p-4 sm:p-5 border border-slate-200 shadow-xs space-y-4">
                    <div class="flex items-center justify-between pb-2 border-b border-slate-100">
                        <span class="text-xs font-bold uppercase tracking-wider text-slate-700 flex items-center gap-1.5">
                            <span>📐</span> Formati & Dimensioni
                        </span>
                        <!-- Unit Switcher -->
                        <div class="inline-flex p-0.5 bg-slate-100 rounded-xl border border-slate-200/80 gap-1 text-[11px] font-bold">
                            <button type="button" id="unitMm" onclick="setUnit('mm')" class="px-2 py-0.5 rounded-lg bg-white text-amber-800 shadow-xs font-extrabold transition active:scale-95 text-center">mm</button>
                            <button type="button" id="unitCm" onclick="setUnit('cm')" class="px-2 py-0.5 rounded-lg text-slate-600 hover:text-slate-900 transition active:scale-95 text-center font-bold">cm</button>
                            <button type="button" id="unitIn" onclick="setUnit('in')" class="px-2 py-0.5 rounded-lg text-slate-600 hover:text-slate-900 transition active:scale-95 text-center font-bold">in</button>
                        </div>
                    </div>

                    <!-- Sheet Format Selector -->
                    <div>
                        <label id="lblSheetFormat" class="block text-xs font-bold text-slate-700 mb-1">Formato Foglio Macchina (Grezzo)</label>
                        <select id="sheetPreset" onchange="applySheetPreset()" class="w-full p-2.5 bg-slate-50 border border-slate-200 rounded-xl text-xs sm:text-sm font-semibold text-slate-800 focus:outline-none focus:ring-2 focus:ring-amber-500 transition">
                            <option value="700x1000">70 × 100 cm (700 × 1000 mm) - Standard Offset</option>
                            <option value="640x880">64 × 88 cm (640 × 880 mm) - Editoria Libri</option>
                            <option value="500x700">50 × 70 cm (500 × 700 mm) - Mezzo Foglio</option>
                            <option value="320x450" selected>SRA3 (320 × 450 mm) - Digitale Pro</option>
                            <option value="330x487">SRA3+ (330 × 487 mm) - Digitale Xerox/Canon</option>
                            <option value="297x420">A3 Standard (297 × 420 mm)</option>
                            <option value="custom">Personalizzato...</option>
                        </select>
                    </div>

                    <!-- Custom Sheet Dimensions -->
                    <div id="sheetCustomBox" class="grid grid-cols-2 gap-2.5">
                        <div>
                            <label id="lblSheetW" class="block text-[11px] font-bold text-slate-600 mb-0.5">Base Foglio (<span class="unitBadge">mm</span>)</label>
                            <input type="number" id="sheetW" value="320" min="50" max="3000" oninput="calculateYield()" class="w-full p-2 bg-slate-50 border border-slate-200 rounded-xl text-xs sm:text-sm font-bold text-slate-900 focus:outline-none focus:ring-2 focus:ring-amber-500 font-mono">
                        </div>
                        <div>
                            <label id="lblSheetH" class="block text-[11px] font-bold text-slate-600 mb-0.5">Altezza Foglio (<span class="unitBadge">mm</span>)</label>
                            <input type="number" id="sheetH" value="450" min="50" max="3000" oninput="calculateYield()" class="w-full p-2 bg-slate-50 border border-slate-200 rounded-xl text-xs sm:text-sm font-bold text-slate-900 focus:outline-none focus:ring-2 focus:ring-amber-500 font-mono">
                        </div>
                    </div>

                    <!-- Cut Product Format Selector -->
                    <div>
                        <label id="lblCutFormat" class="block text-xs font-bold text-slate-700 mb-1">Formato Prodotto Finito (Rifilato)</label>
                        <select id="cutPreset" onchange="applyCutPreset()" class="w-full p-2.5 bg-slate-50 border border-slate-200 rounded-xl text-xs sm:text-sm font-semibold text-slate-800 focus:outline-none focus:ring-2 focus:ring-amber-500 transition">
                            <option value="85x55" selected>Biglietto da Visita (85 × 55 mm)</option>
                            <option value="105x148">Volantino A6 (105 × 148 mm)</option>
                            <option value="148x210">Volantino A5 (148 × 210 mm)</option>
                            <option value="210x297">Foglio / Scheda A4 (210 × 297 mm)</option>
                            <option value="100x210">Pieghevole 1/3 A4 (100 × 210 mm)</option>
                            <option value="100x150">Cartolina (100 × 150 mm)</option>
                            <option value="custom">Personalizzato...</option>
                        </select>
                    </div>

                    <!-- Custom Cut Dimensions -->
                    <div id="cutCustomBox" class="grid grid-cols-2 gap-2.5">
                        <div>
                            <label id="lblCutW" class="block text-[11px] font-bold text-slate-600 mb-0.5">Base Prodotto (<span class="unitBadge">mm</span>)</label>
                            <input type="number" id="cutW" value="85" min="10" max="2000" oninput="calculateYield()" class="w-full p-2 bg-slate-50 border border-slate-200 rounded-xl text-xs sm:text-sm font-bold text-slate-900 focus:outline-none focus:ring-2 focus:ring-amber-500 font-mono">
                        </div>
                        <div>
                            <label id="lblCutH" class="block text-[11px] font-bold text-slate-600 mb-0.5">Altezza Prodotto (<span class="unitBadge">mm</span>)</label>
                            <input type="number" id="cutH" value="55" min="10" max="2000" oninput="calculateYield()" class="w-full p-2 bg-slate-50 border border-slate-200 rounded-xl text-xs sm:text-sm font-bold text-slate-900 focus:outline-none focus:ring-2 focus:ring-amber-500 font-mono">
                        </div>
                    </div>
                </div>

                <!-- PRESS & FINISHING PARAMETERS -->
                <div class="bg-white rounded-2xl p-4 sm:p-5 border border-slate-200 shadow-xs space-y-3.5">
                    <span class="text-xs font-bold uppercase tracking-wider text-slate-700 flex items-center gap-1.5 pb-2 border-b border-slate-100">
                        <span>⚙️</span> Parametri Macchina & Carta
                    </span>

                    <div class="grid grid-cols-2 gap-2.5">
                        <div>
                            <label id="lblGripper" class="block text-[11px] font-bold text-slate-600 mb-0.5">Pinza Macchina (<span class="unitBadge">mm</span>)</label>
                            <input type="number" id="gripperMargin" value="10" min="0" max="50" oninput="calculateYield()" class="w-full p-2 bg-slate-50 border border-slate-200 rounded-xl text-xs sm:text-sm font-bold text-slate-900 focus:outline-none focus:ring-2 focus:ring-amber-500 font-mono">
                        </div>
                        <div>
                            <label id="lblBleed" class="block text-[11px] font-bold text-slate-600 mb-0.5">Refilo / Spazio Pose (<span class="unitBadge">mm</span>)</label>
                            <input type="number" id="cutBleed" value="2" min="0" max="20" oninput="calculateYield()" class="w-full p-2 bg-slate-50 border border-slate-200 rounded-xl text-xs sm:text-sm font-bold text-slate-900 focus:outline-none focus:ring-2 focus:ring-amber-500 font-mono">
                        </div>
                    </div>

                    <!-- Grain Direction Selector -->
                    <div>
                        <label id="lblGrain" class="block text-[11px] font-bold text-slate-600 mb-1">Senso di Fibra Foglio Madre</label>
                        <select id="grainDirection" onchange="calculateYield()" class="w-full p-2 bg-slate-50 border border-slate-200 rounded-xl text-xs font-semibold text-slate-800 focus:outline-none focus:ring-2 focus:ring-amber-500">
                            <option value="long" selected>Fibra Lunga (LG - parallela al lato lungo)</option>
                            <option value="short">Fibra Corta (SG - parallela al lato corto)</option>
                        </select>
                    </div>

                    <!-- Target Copies & Weight -->
                    <div class="grid grid-cols-3 gap-2 pt-1 border-t border-slate-100">
                        <div>
                            <label id="lblCopiesTarget" class="block text-[10px] font-bold text-slate-500 mb-0.5">Tiratura Copie</label>
                            <input type="number" id="targetCopies" value="1000" min="1" step="100" oninput="calculateYield()" class="w-full p-1.5 bg-slate-50 border border-slate-200 rounded-xl text-xs font-bold text-slate-900 font-mono">
                        </div>
                        <div>
                            <label id="lblPaperWeight" class="block text-[10px] font-bold text-slate-500 mb-0.5">Grammatura (g/m²)</label>
                            <input type="number" id="paperWeight" value="350" min="40" max="800" oninput="calculateYield()" class="w-full p-1.5 bg-slate-50 border border-slate-200 rounded-xl text-xs font-bold text-slate-900 font-mono">
                        </div>
                        <div>
                            <label id="lblWasteMargin" class="block text-[10px] font-bold text-slate-500 mb-0.5">Avviamento %</label>
                            <input type="number" id="wasteMargin" value="5" min="0" max="50" oninput="calculateYield()" class="w-full p-1.5 bg-slate-50 border border-slate-200 rounded-xl text-xs font-bold text-slate-900 font-mono">
                        </div>
                    </div>
                </div>

            </div>

            <!-- RIGHT COLUMN: RESULTS & INTERACTIVE 2D SVG PREVIEW (7 COLS) -->
            <div class="lg:col-span-7 flex flex-col gap-4">
                
                <!-- KEY METRICS CARDS -->
                <div class="grid grid-cols-2 sm:grid-cols-3 gap-2.5">
                    
                    <!-- Yield Card (Hero Metric) -->
                    <div class="p-3.5 bg-gradient-to-br from-amber-50 to-orange-50/80 rounded-2xl border border-amber-200 shadow-xs flex flex-col justify-between">
                        <span id="lblResBestYield" class="text-[11px] font-extrabold uppercase tracking-wider text-amber-900">Resa per Foglio</span>
                        <div class="my-1">
                            <span id="resYieldValue" class="text-3xl sm:text-4xl font-black text-amber-600 font-mono">24</span>
                            <span id="resYieldUnit" class="text-xs font-bold text-amber-800 ml-1">pose</span>
                        </div>
                        <span id="resLayoutMode" class="text-[10px] font-bold text-amber-800/80 truncate">Disposizione Dritta (4×6)</span>
                    </div>

                    <!-- Waste % Card -->
                    <div class="p-3.5 bg-white rounded-2xl border border-slate-200 shadow-xs flex flex-col justify-between">
                        <span id="lblResWastePct" class="text-[11px] font-bold uppercase tracking-wider text-slate-500">Sfrido / Scarto</span>
                        <div class="my-1">
                            <span id="resWasteValue" class="text-3xl sm:text-4xl font-black text-slate-800 font-mono">21.8</span>
                            <span class="text-xs font-bold text-slate-500 ml-0.5">%</span>
                        </div>
                        <span id="resUsableArea" class="text-[10px] font-semibold text-slate-500">78.2% superficie utile</span>
                    </div>

                    <!-- Sheets to Order Card -->
                    <div class="col-span-2 sm:col-span-1 p-3.5 bg-white rounded-2xl border border-slate-200 shadow-xs flex flex-col justify-between">
                        <span id="lblResSheetsOrder" class="text-[11px] font-bold uppercase tracking-wider text-slate-500">Fogli da Ordinare</span>
                        <div class="my-1">
                            <span id="resOrderSheetsValue" class="text-3xl sm:text-4xl font-black text-blue-600 font-mono">44</span>
                            <span class="text-xs font-bold text-slate-500 ml-0.5">fogli</span>
                        </div>
                        <span id="resTotalWeight" class="text-[10px] font-semibold text-slate-500 font-mono">Peso: 2.22 kg</span>
                    </div>
                </div>

                <!-- 2D SVG CUT IMPOSITION PREVIEW -->
                <div class="bg-white rounded-2xl p-4 sm:p-5 border border-slate-200 shadow-xs space-y-3">
                    <div class="flex items-center justify-between pb-2 border-b border-slate-100">
                        <div class="flex items-center gap-1.5">
                            <span class="text-sm">🖥️</span>
                            <span id="sheetPreviewTitle" class="text-xs font-bold uppercase tracking-wider text-slate-800">Schema di Taglio & Disposizione Pose</span>
                        </div>
                        <div class="flex items-center gap-2">
                            <span class="inline-flex items-center gap-1 text-[10px] font-bold text-slate-500">
                                <span class="w-2.5 h-2.5 bg-amber-500 rounded-xs inline-block"></span> Pose
                            </span>
                            <span class="inline-flex items-center gap-1 text-[10px] font-bold text-slate-500">
                                <span class="w-2.5 h-2.5 bg-slate-200 rounded-xs inline-block"></span> Sfrido
                            </span>
                            <span class="inline-flex items-center gap-1 text-[10px] font-bold text-orange-600">
                                <span class="w-2.5 h-2.5 border border-dashed border-orange-500 rounded-xs inline-block"></span> Pinza
                            </span>
                        </div>
                    </div>

                    <!-- Vector Canvas Viewport -->
                    <div id="svgContainer" class="w-full bg-slate-900 rounded-xl p-3 flex items-center justify-center overflow-hidden border border-slate-800" style="min-height: 280px;">
                        <svg id="sheetSvg" class="w-full max-h-[320px] transition-all duration-300 drop-shadow-md" viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg">
                            <!-- Injected by JavaScript -->
                        </svg>
                    </div>

                    <div class="flex items-center justify-between text-[11px] text-slate-500 pt-1">
                        <span id="cutSheetNote">Linea tratteggiata arancione: zona pinza macchina non stampabile.</span>
                        <span id="grainIndicatorBadge" class="px-2 py-0.5 rounded-md font-bold text-[10px] bg-emerald-50 text-emerald-700 border border-emerald-200">
                            ✓ Fibra Parallela al Taglio
                        </span>
                    </div>
                </div>

                <!-- GRAIN DIRECTION ADVISORY BANNER -->
                <div id="grainAlertBox" class="p-3.5 rounded-xl border transition-all bg-emerald-50 border-emerald-200 text-emerald-900 text-xs flex items-center gap-3">
                    <span class="text-2xl shrink-0">🧭</span>
                    <div>
                        <span id="grainAlertTitle" class="font-bold block">Senso di Fibra Ottimale</span>
                        <span id="grainAlertDesc" class="text-[11px] opacity-90">La fibra scorre parallela al lato lungo del prodotto finito: garanzia di piega pulita senza spaccature.</span>
                    </div>
                </div>

                <!-- TECHNICAL TIP BANNER -->
                <div class="p-3 bg-slate-100 rounded-xl text-xs text-slate-600 leading-relaxed border border-slate-200" id="ruleTipBox">
                    <span id="ruleTipText">{it_t["rule_tip"]}</span>
                </div>

            </div>
        </div>

        <!-- FAQ ACCORDION SECTION -->
        <section id="faqSection" class="no-print pt-4 border-t border-slate-200 space-y-3">
            <h2 id="faqTitle" class="text-base sm:text-lg font-bold text-slate-900 flex items-center gap-2">
                <span>❓</span> <span>{it_t["faq_title"]}</span>
            </h2>
            <div class="space-y-2">
                <details class="bg-white rounded-xl border border-slate-200 p-3 sm:p-4 group">
                    <summary class="font-bold text-xs sm:text-sm text-slate-800 cursor-pointer list-none flex justify-between items-center">
                        <span id="faq1Q">{it_t["faq_1_q"]}</span>
                        <span class="text-slate-400 group-open:rotate-180 transition-transform">▼</span>
                    </summary>
                    <p id="faq1A" class="text-xs text-slate-600 mt-2 leading-relaxed">{it_t["faq_1_a"]}</p>
                </details>
                <details class="bg-white rounded-xl border border-slate-200 p-3 sm:p-4 group">
                    <summary class="font-bold text-xs sm:text-sm text-slate-800 cursor-pointer list-none flex justify-between items-center">
                        <span id="faq2Q">{it_t["faq_2_q"]}</span>
                        <span class="text-slate-400 group-open:rotate-180 transition-transform">▼</span>
                    </summary>
                    <p id="faq2A" class="text-xs text-slate-600 mt-2 leading-relaxed">{it_t["faq_2_a"]}</p>
                </details>
                <details class="bg-white rounded-xl border border-slate-200 p-3 sm:p-4 group">
                    <summary class="font-bold text-xs sm:text-sm text-slate-800 cursor-pointer list-none flex justify-between items-center">
                        <span id="faq3Q">{it_t["faq_3_q"]}</span>
                        <span class="text-slate-400 group-open:rotate-180 transition-transform">▼</span>
                    </summary>
                    <p id="faq3A" class="text-xs text-slate-600 mt-2 leading-relaxed">{it_t["faq_3_a"]}</p>
                </details>
                <details class="bg-white rounded-xl border border-slate-200 p-3 sm:p-4 group">
                    <summary class="font-bold text-xs sm:text-sm text-slate-800 cursor-pointer list-none flex justify-between items-center">
                        <span id="faq4Q">{it_t["faq_4_q"]}</span>
                        <span class="text-slate-400 group-open:rotate-180 transition-transform">▼</span>
                    </summary>
                    <p id="faq4A" class="text-xs text-slate-600 mt-2 leading-relaxed">{it_t["faq_4_a"]}</p>
                </details>
            </div>
        </section>

    </main>

{footer_html}

    <!-- TRANSLATIONS DICTIONARY INJECTED FOR CLIENT-SIDE I18N -->
    <script>
        const I18N_DATA = {t_json_str};
        let currentLang = 'it';
    </script>

    <!-- CORE JAVASCRIPT LOGIC -->
    <script>
{header_js}
{footer_js}

        // Global Imposition State & Units
        let currentCalculation = null;
        let currentUnit = 'mm';

        const SHEET_PRESETS_DATA = [
            {{ id: '700x1000', w: 700, h: 1000, name: '70 × 100 cm', sub: 'Standard Offset' }},
            {{ id: '640x880', w: 640, h: 880, name: '64 × 88 cm', sub: 'Editoria Libri' }},
            {{ id: '500x700', w: 500, h: 700, name: '50 × 70 cm', sub: 'Mezzo Foglio' }},
            {{ id: '320x450', w: 320, h: 450, name: 'SRA3', sub: 'Digitale Pro' }},
            {{ id: '330x487', w: 330, h: 487, name: 'SRA3+', sub: 'Digitale Xerox/Canon' }},
            {{ id: '297x420', w: 297, h: 420, name: 'A3 Standard', sub: 'A3' }}
        ];

        const CUT_PRESETS_DATA = [
            {{ id: '85x55', w: 85, h: 55, name: 'Biglietto da Visita' }},
            {{ id: '105x148', w: 105, h: 148, name: 'Volantino A6' }},
            {{ id: '148x210', w: 148, h: 210, name: 'Volantino A5' }},
            {{ id: '210x297', w: 210, h: 297, name: 'Foglio / Scheda A4' }},
            {{ id: '100x210', w: 100, h: 210, name: 'Pieghevole 1/3 A4' }},
            {{ id: '100x150', w: 100, h: 150, name: 'Cartolina' }}
        ];

        function updateResaDropdowns() {{
            const u = currentUnit;
            const factor = (u === 'cm' ? 10.0 : (u === 'in' ? 25.4 : 1.0));
            const dec = (u === 'mm' ? 0 : (u === 'in' ? 2 : 1));

            const curSheet = document.getElementById('sheetPreset').value;
            document.getElementById('sheetPreset').innerHTML = SHEET_PRESETS_DATA.map(s => {{
                const dispW = (s.w / factor).toFixed(dec);
                const dispH = (s.h / factor).toFixed(dec);
                const sel = (s.id === curSheet) ? 'selected' : '';
                return `<option value="${{s.id}}" ${{sel}}>${{s.name}} (${{dispW}} × ${{dispH}} ${{u}}) - ${{s.sub}}</option>`;
            }}).join('') + `<option value="custom" ${{curSheet === 'custom' ? 'selected' : ''}}>Personalizzato...</option>`;

            const curCut = document.getElementById('cutPreset').value;
            document.getElementById('cutPreset').innerHTML = CUT_PRESETS_DATA.map(c => {{
                const dispW = (c.w / factor).toFixed(dec);
                const dispH = (c.h / factor).toFixed(dec);
                const sel = (c.id === curCut) ? 'selected' : '';
                return `<option value="${{c.id}}" ${{sel}}>${{c.name}} (${{dispW}} × ${{dispH}} ${{u}})</option>`;
            }}).join('') + `<option value="custom" ${{curCut === 'custom' ? 'selected' : ''}}>Personalizzato...</option>`;
        }}

        function setUnit(u) {{
            if (u === currentUnit) return;
            const prevUnit = currentUnit;
            currentUnit = u;

            ['mm', 'cm', 'in'].forEach(unit => {{
                const btn = document.getElementById('unit' + unit.charAt(0).toUpperCase() + unit.slice(1));
                if (btn) {{
                    if (unit === u) {{
                        btn.className = 'px-2 py-0.5 rounded-lg bg-white text-amber-800 shadow-xs font-extrabold transition active:scale-95 text-center';
                    }} else {{
                        btn.className = 'px-2 py-0.5 rounded-lg text-slate-600 hover:text-slate-900 transition active:scale-95 text-center font-bold';
                    }}
                }}
            }});

            document.querySelectorAll('.unitBadge').forEach(el => el.textContent = u);

            const convertVal = (val, from, to) => {{
                let mm = val;
                if (from === 'cm') mm = val * 10;
                else if (from === 'in') mm = val * 25.4;

                if (to === 'cm') return parseFloat((mm / 10).toFixed(2));
                if (to === 'in') return parseFloat((mm / 25.4).toFixed(3));
                return Math.round(mm);
            }};

            const fields = ['sheetW', 'sheetH', 'cutW', 'cutH', 'gripperMargin', 'cutBleed'];
            fields.forEach(id => {{
                const el = document.getElementById(id);
                if (el && el.value) {{
                    const parsed = parseFloat(el.value);
                    if (!isNaN(parsed)) {{
                        el.value = convertVal(parsed, prevUnit, u);
                    }}
                }}
            }});

            updateResaDropdowns();
            calculateYield();
        }}

        document.addEventListener('DOMContentLoaded', function() {{
            initLanguage();
            calculateYield();
            updatePrintDate();
        }});

        function updatePrintDate() {{
            const now = new Date();
            const el = document.getElementById('printDate');
            if (el) {{
                el.textContent = now.toLocaleDateString(currentLang === 'it' ? 'it-IT' : 'en-US', {{
                    year: 'numeric', month: '2-digit', day: '2-digit', hour: '2-digit', minute: '2-digit'
                }});
            }}
        }}

        // Preset Handlers
        function applySheetPreset() {{
            const val = document.getElementById('sheetPreset').value;
            if (val !== 'custom') {{
                let [w, h] = val.split('x').map(Number);
                if (currentUnit === 'cm') {{ w = (w/10).toFixed(1); h = (h/10).toFixed(1); }}
                else if (currentUnit === 'in') {{ w = (w/25.4).toFixed(2); h = (h/25.4).toFixed(2); }}
                document.getElementById('sheetW').value = w;
                document.getElementById('sheetH').value = h;
            }}
            calculateYield();
        }}

        function applyCutPreset() {{
            const val = document.getElementById('cutPreset').value;
            if (val !== 'custom') {{
                let [w, h] = val.split('x').map(Number);
                if (currentUnit === 'cm') {{ w = (w/10).toFixed(1); h = (h/10).toFixed(1); }}
                else if (currentUnit === 'in') {{ w = (w/25.4).toFixed(2); h = (h/25.4).toFixed(2); }}
                document.getElementById('cutW').value = w;
                document.getElementById('cutH').value = h;
            }}
            calculateYield();
        }}

        // Main Cutting Imposition Algorithm
        function calculateYield() {{
            const toMm = (val) => {{
                if (currentUnit === 'cm') return val * 10;
                if (currentUnit === 'in') return val * 25.4;
                return val;
            }};

            const sheetW = toMm(parseFloat(document.getElementById('sheetW').value) || 320);
            const sheetH = toMm(parseFloat(document.getElementById('sheetH').value) || 450);
            const cutW = toMm(parseFloat(document.getElementById('cutW').value) || 85);
            const cutH = toMm(parseFloat(document.getElementById('cutH').value) || 55);
            const gripper = toMm(parseFloat(document.getElementById('gripperMargin').value) || 0);
            const bleed = toMm(parseFloat(document.getElementById('cutBleed').value) || 0);
            const grain = document.getElementById('grainDirection').value || 'long';
            const targetCopies = parseInt(document.getElementById('targetCopies').value) || 1000;
            const weightGsm = parseFloat(document.getElementById('paperWeight').value) || 350;
            const wastePct = parseFloat(document.getElementById('wasteMargin').value) || 5;

            // Effective printable area on parent sheet
            // We assume gripper is on one of the dimensions (typically sheetH or sheetW)
            const usableW = Math.max(10, sheetW - bleed);
            const usableH = Math.max(10, sheetH - gripper - bleed);

            const effectiveCutW = cutW + bleed;
            const effectiveCutH = cutH + bleed;

            // 1. Straight Orientation (Dir 1)
            const cols1 = Math.floor(usableW / effectiveCutW);
            const rows1 = Math.floor(usableH / effectiveCutH);
            const count1 = cols1 * rows1;

            // 2. Rotated Orientation (Dir 2 - 90 deg)
            const cols2 = Math.floor(usableW / effectiveCutH);
            const rows2 = Math.floor(usableH / effectiveCutW);
            const count2 = cols2 * rows2;

            // 3. Mixed / Guillotine Combo Layout
            // Test placing main block straight, then filling remaining height with rotated items
            let count3 = 0;
            let comboRows1 = rows1;
            let comboCols1 = cols1;
            let comboRows2 = 0;
            let comboCols2 = 0;

            const remH = usableH - (rows1 * effectiveCutH);
            if (remH >= effectiveCutW) {{
                comboRows2 = Math.floor(remH / effectiveCutW);
                comboCols2 = Math.floor(usableW / effectiveCutH);
                count3 = count1 + (comboRows2 * comboCols2);
            }}

            // Select optimal arrangement
            let bestArrangement = 'straight';
            let bestCount = count1;
            let arrangementLabel = `Dritta (${{cols1}} × ${{rows1}})`;

            if (count2 > bestCount) {{
                bestCount = count2;
                bestArrangement = 'rotated';
                arrangementLabel = `Ruotata 90° (${{cols2}} × ${{rows2}})`;
            }}
            if (count3 > bestCount) {{
                bestCount = count3;
                bestArrangement = 'mixed';
                arrangementLabel = `Mista Ottimizzata (${{count1}} + ${{count3 - count1}})`;
            }}

            bestCount = Math.max(1, bestCount);

            // Waste & Areas
            const sheetAreaMm2 = sheetW * sheetH;
            const totalCutsAreaMm2 = bestCount * (cutW * cutH);
            const wastePercent = Math.max(0, ((sheetAreaMm2 - totalCutsAreaMm2) / sheetAreaMm2) * 100);
            const usablePercent = 100 - wastePercent;

            // Sheets needed for target run
            const netSheets = Math.ceil(targetCopies / bestCount);
            const grossSheets = Math.ceil(netSheets * (1 + (wastePct / 100)));

            // Weight calculation: Area (m²) * gsm * sheets / 1000
            const sheetAreaM2 = (sheetW / 1000) * (sheetH / 1000);
            const totalKg = (sheetAreaM2 * weightGsm * grossSheets) / 1000;

            // Grain Direction Check
            // Fold is typically parallel to the long edge of the finished piece
            let isGrainOk = true;
            if (grain === 'long') {{
                // Sheet long edge is parallel to grain. If piece is rotated, piece long edge may be cross-grain
                if (bestArrangement === 'rotated') isGrainOk = false;
            }} else {{
                // Sheet short edge is parallel to grain
                if (bestArrangement === 'straight') isGrainOk = false;
            }}

            // Update UI
            document.getElementById('resYieldValue').textContent = bestCount;
            document.getElementById('resLayoutMode').textContent = arrangementLabel;
            document.getElementById('resWasteValue').textContent = wastePercent.toFixed(1);
            document.getElementById('resUsableArea').textContent = `${{usablePercent.toFixed(1)}}% superficie utile`;
            document.getElementById('resOrderSheetsValue').textContent = grossSheets;
            document.getElementById('resTotalWeight').textContent = `Peso: ${{totalKg.toFixed(2)}} kg (${{netSheets}} netti)`;

            // Grain Alert UI
            const grainBox = document.getElementById('grainAlertBox');
            const grainTitle = document.getElementById('grainAlertTitle');
            const grainDesc = document.getElementById('grainAlertDesc');
            const grainBadge = document.getElementById('grainIndicatorBadge');

            if (isGrainOk) {{
                grainBox.className = 'p-3.5 rounded-xl border transition-all bg-emerald-50 border-emerald-200 text-emerald-900 text-xs flex items-center gap-3';
                grainTitle.textContent = 'Senso di Fibra Ottimale';
                grainDesc.textContent = 'Le fibre di cellulosa scorrono parallele al lato di piega: pieghe pulite e nessun rischio di spaccatura.';
                grainBadge.className = 'px-2 py-0.5 rounded-md font-bold text-[10px] bg-emerald-50 text-emerald-700 border border-emerald-200';
                grainBadge.textContent = '✓ Fibra Conforme';
            }} else {{
                grainBox.className = 'p-3.5 rounded-xl border transition-all bg-amber-50 border-amber-200 text-amber-900 text-xs flex items-center gap-3';
                grainTitle.textContent = 'Attenzione: Piega in Controfibra';
                grainDesc.textContent = 'La disposizione massima orienta le pose perpendicolari alla fibra. È fortemente raccomandata la cordonatura meccanica per evitare spaccature.';
                grainBadge.className = 'px-2 py-0.5 rounded-md font-bold text-[10px] bg-amber-50 text-amber-700 border border-amber-200';
                grainBadge.textContent = '⚠️ Possibile Controfibra';
            }}

            // Raw display values from inputs
            const dispSheetW = document.getElementById('sheetW').value;
            const dispSheetH = document.getElementById('sheetH').value;

            // Render 2D SVG
            renderSheetSvg({{
                sheetW, sheetH, cutW, cutH, gripper, bleed,
                dispSheetW, dispSheetH,
                bestArrangement, cols1, rows1, cols2, rows2,
                comboRows1, comboCols1, comboRows2, comboCols2
            }});
        }}

        // Render Vector 2D SVG
        function renderSheetSvg(p) {{
            const svg = document.getElementById('sheetSvg');
            const pad = 20;
            const maxW = 560;
            const maxH = 280;

            const scale = Math.min(maxW / p.sheetW, maxH / p.sheetH);
            const w = p.sheetW * scale;
            const h = p.sheetH * scale;

            svg.setAttribute('viewBox', `0 0 ${{w + (pad * 2)}} ${{h + (pad * 2)}}`);

            let svgContent = `
                <!-- Background Shadow & Paper Sheet -->
                <rect x="${{pad}}" y="${{pad}}" width="${{w}}" height="${{h}}" rx="4" fill="#1e293b" stroke="#475569" stroke-width="2"/>
            `;

            // Gripper margin zone (orange dashed)
            if (p.gripper > 0) {{
                const gripH = p.gripper * scale;
                svgContent += `
                    <rect x="${{pad}}" y="${{pad}}" width="${{w}}" height="${{gripH}}" fill="rgba(249, 115, 22, 0.15)" stroke="#f97316" stroke-dasharray="3 3" stroke-width="1.5"/>
                    <text x="${{pad + (w / 2)}}" y="${{pad + (gripH / 2) + 3}}" fill="#fb923c" font-size="9" font-family="monospace" font-weight="bold" text-anchor="middle">ZONA PINZA MACCHINA (${{document.getElementById('gripperMargin').value}} ${{currentUnit}})</text>
                `;
            }}

            // Draw individual cut pieces
            const gripOffset = p.gripper * scale;
            let pieceIndex = 1;

            if (p.bestArrangement === 'straight') {{
                const pw = p.cutW * scale;
                const ph = p.cutH * scale;
                const effW = (p.cutW + p.bleed) * scale;
                const effH = (p.cutH + p.bleed) * scale;

                for (let r = 0; r < p.rows1; r++) {{
                    for (let c = 0; c < p.cols1; c++) {{
                        const x = pad + (c * effW);
                        const y = pad + gripOffset + (r * effH);
                        svgContent += `
                            <g>
                                <rect x="${{x}}" y="${{y}}" width="${{pw}}" height="${{ph}}" rx="2" fill="#d97706" stroke="#fbbf24" stroke-width="1.2"/>
                                <text x="${{x + (pw / 2)}}" y="${{y + (ph / 2) + 3}}" fill="#ffffff" font-size="${{Math.max(7, Math.min(10, pw / 4))}}" font-family="sans-serif" font-weight="bold" text-anchor="middle">${{pieceIndex++}}</text>
                            </g>
                        `;
                    }}
                }}
            }} else if (p.bestArrangement === 'rotated') {{
                const pw = p.cutH * scale;
                const ph = p.cutW * scale;
                const effW = (p.cutH + p.bleed) * scale;
                const effH = (p.cutW + p.bleed) * scale;

                for (let r = 0; r < p.rows2; r++) {{
                    for (let c = 0; c < p.cols2; c++) {{
                        const x = pad + (c * effW);
                        const y = pad + gripOffset + (r * effH);
                        svgContent += `
                            <g>
                                <rect x="${{x}}" y="${{y}}" width="${{pw}}" height="${{ph}}" rx="2" fill="#b45309" stroke="#fcd34d" stroke-width="1.2"/>
                                <text x="${{x + (pw / 2)}}" y="${{y + (ph / 2) + 3}}" fill="#ffffff" font-size="${{Math.max(7, Math.min(10, pw / 4))}}" font-family="sans-serif" font-weight="bold" text-anchor="middle">${{pieceIndex++}}</text>
                            </g>
                        `;
                    }}
                }}
            }} else if (p.bestArrangement === 'mixed') {{
                // Main straight block
                const pw1 = p.cutW * scale;
                const ph1 = p.cutH * scale;
                const effW1 = (p.cutW + p.bleed) * scale;
                const effH1 = (p.cutH + p.bleed) * scale;

                for (let r = 0; r < p.rows1; r++) {{
                    for (let c = 0; c < p.cols1; c++) {{
                        const x = pad + (c * effW1);
                        const y = pad + gripOffset + (r * effH1);
                        svgContent += `
                            <g>
                                <rect x="${{x}}" y="${{y}}" width="${{pw1}}" height="${{ph1}}" rx="2" fill="#d97706" stroke="#fbbf24" stroke-width="1.2"/>
                                <text x="${{x + (pw1 / 2)}}" y="${{y + (ph1 / 2) + 3}}" fill="#ffffff" font-size="${{Math.max(7, Math.min(10, pw1 / 4))}}" font-family="sans-serif" font-weight="bold" text-anchor="middle">${{pieceIndex++}}</text>
                            </g>
                        `;
                    }}
                }}

                // Rotated extra block in remaining height
                const pw2 = p.cutH * scale;
                const ph2 = p.cutW * scale;
                const effW2 = (p.cutH + p.bleed) * scale;
                const effH2 = (p.cutW + p.bleed) * scale;
                const startY = pad + gripOffset + (p.rows1 * effH1);

                for (let r = 0; r < p.comboRows2; r++) {{
                    for (let c = 0; c < p.comboCols2; c++) {{
                        const x = pad + (c * effW2);
                        const y = startY + (r * effH2);
                        svgContent += `
                            <g>
                                <rect x="${{x}}" y="${{y}}" width="${{pw2}}" height="${{ph2}}" rx="2" fill="#b45309" stroke="#fcd34d" stroke-width="1.2"/>
                                <text x="${{x + (pw2 / 2)}}" y="${{y + (ph2 / 2) + 3}}" fill="#ffffff" font-size="${{Math.max(7, Math.min(10, pw2 / 4))}}" font-family="sans-serif" font-weight="bold" text-anchor="middle">${{pieceIndex++}}</text>
                            </g>
                        `;
                    }}
                }}
            }}

            // Dimension indicators
            svgContent += `
                <!-- Sheet Dimensions Callout -->
                <text x="${{pad + (w / 2)}}" y="${{pad - 6}}" fill="#94a3b8" font-size="10" font-family="monospace" font-weight="bold" text-anchor="middle">Base: ${{p.dispSheetW}} ${{currentUnit}}</text>
                <text x="${{pad + w + 8}}" y="${{pad + (h / 2)}}" fill="#94a3b8" font-size="10" font-family="monospace" font-weight="bold" dominant-baseline="middle">H: ${{p.dispSheetH}} ${{currentUnit}}</text>
            `;

            svg.innerHTML = svgContent;
        }}

        // Language & Localization Engine
        function initLanguage() {{
            const saved = localStorage.getItem('omnitools_lang');
            if (saved && I18N_DATA[saved]) {{
                currentLang = saved;
            }} else {{
                const userLangs = navigator.languages || [navigator.language || 'it'];
                for (let l of userLangs) {{
                    const prefix = l.split('-')[0].toLowerCase();
                    if (I18N_DATA[prefix]) {{
                        currentLang = prefix;
                        break;
                    }}
                }}
            }}
            const selectEl = document.getElementById('langSelect');
            if (selectEl) selectEl.value = currentLang;
            applyTranslations(currentLang);
        }}

        function changeLanguage(lang) {{
            if (I18N_DATA[lang]) {{
                currentLang = lang;
                localStorage.setItem('omnitools_lang', lang);
            try {{ window.dispatchEvent(new CustomEvent('omnitools_lang_changed', {{ detail: {{ lang: lang }} }})); }} catch(e) {{}}
                const selectEl = document.getElementById('langSelect');
                if (selectEl) selectEl.value = lang;
                applyTranslations(lang);
                calculateYield();
                updatePrintDate();
            }}
        }}
        window.changeLanguage = changeLanguage;

        function applyTranslations(lang) {{
            const t = I18N_DATA[lang] || I18N_DATA['it'];
            document.documentElement.lang = lang;

            document.getElementById('heroTitle').textContent = t.hero_title;
            document.getElementById('heroDesc').textContent = t.hero_desc;
            document.getElementById('privacyBadge').textContent = t.privacy_badge;

            document.getElementById('lblSheetFormat').textContent = t.sheet_format_label;
            document.getElementById('lblCutFormat').textContent = t.cut_format_label;
            document.getElementById('lblSheetW').innerHTML = `${{t.sheet_w_label}} (<span class="unitBadge">${{currentUnit}}</span>)`;
            document.getElementById('lblSheetH').innerHTML = `${{t.sheet_h_label}} (<span class="unitBadge">${{currentUnit}}</span>)`;
            document.getElementById('lblCutW').innerHTML = `${{t.cut_w_label}} (<span class="unitBadge">${{currentUnit}}</span>)`;
            document.getElementById('lblCutH').innerHTML = `${{t.cut_h_label}} (<span class="unitBadge">${{currentUnit}}</span>)`;
            document.getElementById('lblGripper').innerHTML = `${{t.gripper_label}} (<span class="unitBadge">${{currentUnit}}</span>)`;
            document.getElementById('lblBleed').innerHTML = `${{t.bleed_label}} (<span class="unitBadge">${{currentUnit}}</span>)`;
            document.getElementById('lblGrain').textContent = t.grain_label;
            document.getElementById('lblCopiesTarget').textContent = t.copies_target_label;
            document.getElementById('lblPaperWeight').textContent = t.paper_weight_label;
            document.getElementById('lblWasteMargin').textContent = t.waste_margin_label;

            document.getElementById('lblResBestYield').textContent = t.res_best_yield;
            document.getElementById('resYieldUnit').textContent = t.res_pieces_per_sheet;
            document.getElementById('lblResWastePct').textContent = t.res_waste_pct;
            document.getElementById('lblResSheetsOrder').textContent = t.res_sheets_order;

            document.getElementById('sheetPreviewTitle').textContent = t.sheet_preview_title;
            document.getElementById('cutSheetNote').textContent = t.cut_sheet_note;

            document.getElementById('ruleTipText').innerHTML = t.rule_tip;
            document.getElementById('legalDisclaimerText').innerHTML = t.legal_disclaimer;

            document.getElementById('faqTitle').children[1].textContent = t.faq_title;
            document.getElementById('faq1Q').textContent = t.faq_1_q;
            document.getElementById('faq1A').textContent = t.faq_1_a;
            document.getElementById('faq2Q').textContent = t.faq_2_q;
            document.getElementById('faq2A').textContent = t.faq_2_a;
            document.getElementById('faq3Q').textContent = t.faq_3_q;
            document.getElementById('faq3A').textContent = t.faq_3_a;
            document.getElementById('faq4Q').textContent = t.faq_4_q;
            document.getElementById('faq4A').textContent = t.faq_4_a;
        }}

        // PWA Install Prompt Handler
        let deferredPrompt = null;
        window.addEventListener('beforeinstallprompt', (e) => {{
            e.preventDefault();
            deferredPrompt = e;
            const btn = document.getElementById('headerInstallBtn');
            if (btn) btn.classList.remove('hidden');
        }});

        function triggerInstall() {{
            if (deferredPrompt) {{
                deferredPrompt.prompt();
                deferredPrompt.userChoice.then((choiceResult) => {{
                    deferredPrompt = null;
                }});
            }} else {{
                alert('Per installare l\\'app su iOS: tocca il tasto Condividi e seleziona "Aggiungi alla schermata Home". Su Android/Desktop: menu opzioni del browser -> "Installa applicazione".');
            }}
        }}
    </script>
</body>
</html>"""

with open('/Users/ilalu/Documents/Altenative Businnes/Calcolatore_Pendenza/resa.html', 'w', encoding='utf-8') as f:
    f.write(html_code)

print("resa.html built successfully!")
