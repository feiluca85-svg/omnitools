import json

with open('/Users/ilalu/Documents/Altenative Businnes/Calcolatore_Pendenza/translations_tubi.json', 'r', encoding='utf-8') as f:
    t_data = json.load(f)

t_json_str = json.dumps(t_data, ensure_ascii=False)

html_code = f"""<!DOCTYPE html>
<html lang="it">
<head>
    <meta name="google-site-verification" content="MRdbDm9lLhokeD3I0FOpUSOhNaF_2WaveKvu52FxtG4">
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0">
    <title>Calcolo Pendenza Tubi di Scarico e Fognatura — Dislivello e Autopulizia UNI EN 12056</title>
    <meta name="description" content="Calcolatore online per pendenza tubazioni di scarico fognario, caduta per metro lineare (cm/m), dislivello e dimensionamento diametri Ø 40-200 mm con verifica di autopulizia acque nere e grigie secondo UNI EN 12056 e UNI EN 752.">
    
    <!-- Canonical & SEO Meta Tags -->
    <link rel="canonical" href="https://www.omnitoolslab.com/tubi">
    <meta name="robots" content="index, follow">
    <meta property="og:type" content="website">
    <meta property="og:title" content="ScaricoFacile — Calcolo Pendenza Tubazioni e Scarichi Fognari">
    <meta property="og:description" content="Dimensionamento immediato del dislivello, caduta al metro e verifica autopulizia per tubazioni di scarico secondo UNI EN 12056.">
    <meta property="og:url" content="https://www.omnitoolslab.com/tubi">
    <meta property="og:site_name" content="OmniTools Lab">
    <meta property="og:image" content="https://www.omnitoolslab.com/og-tubi.png">
    <meta property="og:image:width" content="1200">
    <meta property="og:image:height" content="630">
    <meta property="og:image:type" content="image/png">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:image" content="https://www.omnitoolslab.com/og-tubi.png">

    <!-- Schema.org JSON-LD Structured Data (Rich Snippets) -->
    <script type="application/ld+json">
    [
      {{
        "@context": "https://schema.org",
        "@type": "WebApplication",
        "name": "ScaricoFacile — Calcolo Pendenza Tubazioni e Scarichi",
        "url": "https://www.omnitoolslab.com/tubi",
        "applicationCategory": "UtilitiesApplication",
        "operatingSystem": "All",
        "description": "Calcolatore tecnico professionale per il calcolo di pendenza, dislivello e caduta al metro lineare per reti di scarico a gravità e fognature.",
        "offers": {{
          "@type": "Offer",
          "price": "0",
          "priceCurrency": "EUR"
        }}
      }},
      {{
        "@context": "https://schema.org",
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
            "name": "OmniBuilding",
            "item": "https://www.omnitoolslab.com/#building"
          }},
          {{
            "@type": "ListItem",
            "position": 3,
            "name": "ScaricoFacile",
            "item": "https://www.omnitoolslab.com/tubi"
          }}
        ]
      }},
      {{
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
          {{
            "@type": "Question",
            "name": "Qual è la pendenza minima obbligatoria per un tubo di scarico fognario?",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "La pendenza minima raccomandata dalle norme tecniche europee (UNI EN 12056) è dell'1% (1 cm per ogni metro lineare) per garantire l'autopulizia ed evitare depositi solidi."
            }}
          }},
          {{
            "@type": "Question",
            "name": "Cosa succede se la pendenza dello scarico è troppo ripida?",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "Sopra il 3.5-4%, l'acqua scivola via velocemente lasciando fermi sul fondo del tubo i corpi solidi pesanti (separazione liquido-solido), provocando occlusioni."
            }}
          }},
          {{
            "@type": "Question",
            "name": "Come si calcola il dislivello tra punto di partenza e punto di arrivo?",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "Formula: Dislivello (cm) = Lunghezza (metri) × Pendenza (%). Ad esempio: 4 metri con pendenza 1.5% necessitano di 6 cm di caduta."
            }}
          }}
        ]
      }}
    ]
    </script>

    <!-- Favicon & PWA -->
    <link rel="icon" type="image/svg+xml" href="/favicon.svg">
    <link rel="icon" type="image/png" sizes="32x32" href="/favicon.png">
    <link rel="apple-touch-icon" href="/favicon.png">
    <link rel="manifest" href="/manifest.json">
    <meta name="theme-color" content="#2563eb">

    <!-- Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600;700&family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
    
    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {{
            theme: {{
                extend: {{
                    fontFamily: {{
                        sans: ['"Plus Jakarta Sans"', 'system-ui', '-apple-system', 'sans-serif'],
                        jakarta: ['"Plus Jakarta Sans"', 'sans-serif'],
                        mono: ['"JetBrains Mono"', 'monospace'],
                    }}
                }}
            }}
        }}
    </script>
    <script defer src="/_vercel/insights/script.js"></script>

    <style>
        @page {{
            size: A4 portrait;
            margin: 8mm 10mm 8mm 10mm;
        }}
        @media print {{
            header, footer, nav,
            .no-print,
            #faqSection, #normSection, #shareStrip,
            #presetsSection, #calcTabs, #langSelect, button, input[type=range],
            details, .faq-accordion {{
                display: none !important;
            }}
            body {{
                background-color: #ffffff !important;
                color: #0f172a !important;
                font-size: 10pt !important;
                line-height: 1.25 !important;
                padding: 0 !important;
                margin: 0 !important;
                -webkit-print-color-adjust: exact !important;
                print-color-adjust: exact !important;
            }}
            main {{
                max-width: 100% !important;
                margin: 0 !important;
                padding: 0 !important;
                width: 100% !important;
            }}
            .print-only {{
                display: block !important;
            }}
            .shadow-sm, .shadow-md, .shadow-lg, .shadow-2xs {{
                box-shadow: none !important;
            }}
            .border {{
                border-color: #cbd5e1 !important;
            }}
            .bg-slate-900 {{
                background-color: #ffffff !important;
                border: 1px solid #cbd5e1 !important;
            }}
            #pipeSvg {{
                max-height: 150px !important;
            }}
        }}
        .print-only {{
            display: none;
        }}
    </style>
</head>
<body class="bg-slate-50 text-slate-800 font-sans antialiased min-h-screen flex flex-col justify-between selection:bg-blue-500 selection:text-white">

    <!-- Header Navigation -->
    <header class="bg-white/95 border-b border-slate-200 sticky top-0 z-40 backdrop-blur-md shadow-2xs" style="padding-top: max(env(safe-area-inset-top), 8px); padding-bottom: 8px;">
        <div class="max-w-4xl mx-auto px-4 py-1 flex items-center justify-between gap-3">
            <a href="/" class="flex items-center gap-2.5 group">
                <div class="w-[34px] h-[34px] sm:w-[38px] sm:h-[38px] rounded-xl bg-gradient-to-br from-blue-600 to-indigo-700 flex items-center justify-center text-white shadow-md shadow-blue-500/20 shrink-0 p-1 transition group-hover:scale-105">
                    <svg class="w-full h-full" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <circle cx="16" cy="16" r="13.2" stroke="#ffffff" stroke-width="3.4" />
                        <path d="M 7.5 11.5 H 24.5 M 16 11.5 V 24.5" stroke="#ffffff" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round" />
                        <circle cx="16" cy="11.5" r="2.1" fill="#38bdf8" />
                    </svg>
                </div>
                <div class="flex flex-col">
                    <div class="flex items-center gap-1.5 leading-none">
                        <span class="font-jakarta font-black text-base sm:text-lg text-slate-900 tracking-tight leading-none">Omni<span class="text-blue-600">Tools</span></span>
                        <span class="text-[9px] font-jakarta font-extrabold uppercase bg-blue-100 text-blue-800 px-1.5 py-0.5 rounded-full border border-blue-200/80">Lab</span>
                    </div>
                    <span class="text-[10px] text-slate-500 font-medium hidden sm:inline leading-tight mt-0.5">ScaricoFacile — UNI EN 12056</span>
                </div>
            </a>

            <div class="flex items-center gap-2">
                <a href="/" class="text-xs font-bold text-slate-600 hover:text-blue-600 bg-slate-100 hover:bg-slate-200 px-3 py-1.5 rounded-xl border border-slate-200 transition">
                    ← Suite
                </a>
                <select id="langSelect" onchange="changeLanguage(this.value)" class="bg-slate-100 hover:bg-slate-200 text-slate-800 text-xs font-bold py-1.5 px-2 rounded-xl border border-slate-200 focus:outline-none cursor-pointer transition">
                    <option value="it">🇮🇹 IT</option>
                    <option value="en">🇬🇧 EN</option>
                    <option value="es">🇪🇸 ES</option>
                    <option value="fr">🇫🇷 FR</option>
                    <option value="de">🇩🇪 DE</option>
                    <option value="pt">🇵🇹 PT</option>
                </select>
            </div>
        </div>
    </header>

    <!-- Main Container -->
    <main class="max-w-4xl mx-auto px-4 py-6 sm:py-8 flex-1 w-full space-y-6 sm:space-y-8">

        <!-- UNIFIED A4 PRINT HEADER -->
        <div class="print-only mb-3 pb-2 border-b-2 border-slate-900">
            <div class="flex items-center justify-between">
                <div class="flex items-center gap-2.5">
                    <div class="w-10 h-10 rounded-xl bg-gradient-to-br from-blue-600 to-indigo-700 flex items-center justify-center text-white shrink-0 p-1 shadow-sm" style="-webkit-print-color-adjust: exact; print-color-adjust: exact;">
                    <svg class="w-full h-full" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <circle cx="16" cy="16" r="13.2" stroke="#ffffff" stroke-width="3.4" />
                        <path d="M 7.5 11.5 H 24.5 M 16 11.5 V 24.5" stroke="#ffffff" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round" />
                        <circle cx="16" cy="11.5" r="2.1" fill="#38bdf8" />
                    </svg>
                </div>
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

        <!-- Hero Section -->
        <section class="text-center space-y-2 no-print">
            <div class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-blue-50 border border-blue-200/80 text-blue-800 text-xs font-bold shadow-2xs">
                <span>🏗️</span> <span id="toolBadge">OmniBuilding</span> • <span class="font-mono">UNI EN 12056</span>
            </div>
            <h1 id="heroTitle" class="font-jakarta text-2xl sm:text-3xl lg:text-4xl font-black text-slate-900 tracking-tight">
                Calcolo Pendenza Tubazioni e Scarichi Fognari
            </h1>
            <p id="heroDesc" class="text-xs sm:text-sm text-slate-600 max-w-2xl mx-auto leading-relaxed">
                Dimensionamento immediato del dislivello, della caduta per metro lineare e verifica dell'autopulizia per acque nere, grigie e meteoriche secondo UNI EN 12056 e UNI EN 752.
            </p>
        </section>

        <!-- Calculation Card -->
        <div class="bg-white rounded-3xl border border-slate-200 shadow-sm p-4 sm:p-7 space-y-6">

            <!-- Calculation Mode Selector -->
            <div id="calcTabs" class="grid grid-cols-1 sm:grid-cols-2 gap-2 p-1.5 bg-slate-100/90 rounded-2xl border border-slate-200/70">
                <button type="button" onclick="setMode('bySlope')" id="tabModeBySlope" class="py-2.5 px-3 rounded-xl text-xs sm:text-sm font-bold transition shadow-xs bg-white text-blue-700 cursor-pointer">
                    📐 Calcola Dislivello da Pendenza Desiderata (%)
                </button>
                <button type="button" onclick="setMode('byDrop')" id="tabModeByDrop" class="py-2.5 px-3 rounded-xl text-xs sm:text-sm font-bold transition text-slate-600 hover:text-slate-900 cursor-pointer">
                    📏 Calcola Pendenza da Lunghezza e Dislivello
                </button>
            </div>

            <!-- Inputs Grid -->
            <div class="no-print grid grid-cols-1 sm:grid-cols-2 gap-5">
                
                <!-- Input: Pipe Length (L) -->
                <div class="space-y-2">
                    <div class="flex justify-between items-center">
                        <label class="text-xs font-bold text-slate-700 uppercase tracking-wider" id="lblPipeLength">Lunghezza Tratta Tubo (L)</label>
                        <div class="flex items-center gap-1">
                            <input type="number" id="numLength" min="0.5" max="100" step="0.1" value="4.0" class="w-20 px-2 py-1 text-right font-mono font-bold text-sm bg-slate-50 border border-slate-300 rounded-lg text-slate-900 focus:outline-none focus:border-blue-600">
                            <span class="text-xs font-bold text-slate-500">m</span>
                        </div>
                    </div>
                    <input type="range" id="rngLength" min="0.5" max="30" step="0.1" value="4.0" class="w-full accent-blue-600 cursor-pointer">
                </div>

                <!-- Input: Slope % (Mode 1) -->
                <div id="slopeInputBox" class="space-y-2">
                    <div class="flex justify-between items-center">
                        <label class="text-xs font-bold text-slate-700 uppercase tracking-wider" id="lblPipeSlope">Pendenza Desiderata (%)</label>
                        <div class="flex items-center gap-1">
                            <input type="number" id="numSlope" min="0.2" max="10" step="0.1" value="1.5" class="w-20 px-2 py-1 text-right font-mono font-bold text-sm bg-slate-50 border border-slate-300 rounded-lg text-slate-900 focus:outline-none focus:border-blue-600">
                            <span class="text-xs font-bold text-slate-500">%</span>
                        </div>
                    </div>
                    <input type="range" id="rngSlope" min="0.5" max="6.0" step="0.1" value="1.5" class="w-full accent-blue-600 cursor-pointer">
                </div>

                <!-- Input: Drop cm (Mode 2, hidden by default) -->
                <div id="dropInputBox" class="space-y-2 hidden">
                    <div class="flex justify-between items-center">
                        <label class="text-xs font-bold text-slate-700 uppercase tracking-wider" id="lblPipeDrop">Dislivello Totale Caduta (ΔH)</label>
                        <div class="flex items-center gap-1">
                            <input type="number" id="numDrop" min="0.5" max="200" step="0.5" value="6.0" class="w-20 px-2 py-1 text-right font-mono font-bold text-sm bg-slate-50 border border-slate-300 rounded-lg text-slate-900 focus:outline-none focus:border-blue-600">
                            <span class="text-xs font-bold text-slate-500">cm</span>
                        </div>
                    </div>
                    <input type="range" id="rngDrop" min="1" max="50" step="0.5" value="6.0" class="w-full accent-blue-600 cursor-pointer">
                </div>

                <!-- Input: Diameter Selector -->
                <div class="space-y-2 sm:col-span-2">
                    <label class="text-xs font-bold text-slate-700 uppercase tracking-wider block" id="lblPipeDiameter">Diametro Nominale Tubazione (Ø)</label>
                    <select id="selDiameter" onchange="calculate()" class="w-full px-3.5 py-2.5 rounded-xl border border-slate-300 bg-white text-slate-900 text-sm font-semibold focus:outline-none focus:border-blue-600 cursor-pointer shadow-2xs">
                        <option value="40" id="optD40">Ø 40 mm (Lavabo, Bidet, Vasca)</option>
                        <option value="50" id="optD50">Ø 50 mm (Lavello Cucina, Doccia, Lavastoviglie)</option>
                        <option value="90" id="optD90">Ø 90 mm (WC compatto / derivazione)</option>
                        <option value="110" id="optD110" selected>Ø 110 mm (WC standard, Colonna montante)</option>
                        <option value="125" id="optD125">Ø 125 mm (Collettore di piano / scarico esterno)</option>
                        <option value="160" id="optD160">Ø 160 mm (Collettore orizzontale fognario sotterraneo)</option>
                        <option value="200" id="optD200">Ø 200 mm (Condotta principale esterna)</option>
                    </select>
                </div>
            </div>

            <!-- Quick Presets -->
            <div id="presetsSection" class="pt-2 border-t border-slate-100">
                <span class="text-[11px] font-bold text-slate-500 uppercase tracking-wider block mb-2" id="presetsTitle">Preimpostazioni frequenti di cantiere:</span>
                <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
                    <button type="button" onclick="applyPreset(2.5, 1.5, 110)" class="p-2 rounded-xl border border-slate-200 bg-slate-50 hover:bg-blue-50 hover:border-blue-300 text-left transition cursor-pointer">
                        <div class="text-xs font-bold text-slate-800" id="p1Title">WC Civile Standard</div>
                        <div class="text-[10px] text-slate-500 font-mono" id="p1Sub">L=2.5m • Ø110 • 1.5%</div>
                    </button>
                    <button type="button" onclick="applyPreset(4.0, 2.0, 50)" class="p-2 rounded-xl border border-slate-200 bg-slate-50 hover:bg-blue-50 hover:border-blue-300 text-left transition cursor-pointer">
                        <div class="text-xs font-bold text-slate-800" id="p2Title">Cucina / Doccia</div>
                        <div class="text-[10px] text-slate-500 font-mono" id="p2Sub">L=4.0m • Ø50 • 2.0%</div>
                    </button>
                    <button type="button" onclick="applyPreset(15.0, 1.2, 160)" class="p-2 rounded-xl border border-slate-200 bg-slate-50 hover:bg-blue-50 hover:border-blue-300 text-left transition cursor-pointer">
                        <div class="text-xs font-bold text-slate-800" id="p3Title">Collettore Sotterraneo</div>
                        <div class="text-[10px] text-slate-500 font-mono" id="p3Sub">L=15m • Ø160 • 1.2%</div>
                    </button>
                    <button type="button" onclick="applyPreset(8.0, 1.0, 110)" class="p-2 rounded-xl border border-slate-200 bg-slate-50 hover:bg-blue-50 hover:border-blue-300 text-left transition cursor-pointer">
                        <div class="text-xs font-bold text-slate-800" id="p4Title">Scarico Acque Piovane</div>
                        <div class="text-[10px] text-slate-500 font-mono" id="p4Sub">L=8.0m • Ø110 • 1.0%</div>
                    </button>
                </div>
            </div>

            <!-- Key Results Metric Cards -->
            <div class="grid grid-cols-2 sm:grid-cols-4 gap-3 pt-4 border-t border-slate-100">
                <div class="bg-blue-50/70 border border-blue-200/80 rounded-2xl p-3.5 text-center">
                    <span class="text-[11px] font-bold text-blue-700 uppercase tracking-wider block" id="colSlope">Pendenza Calcolata</span>
                    <span class="text-2xl sm:text-3xl font-black font-mono text-blue-900 block mt-1" id="resSlope">1.5 %</span>
                    <span class="text-[10px] text-blue-600 font-semibold block mt-0.5" id="resRatio">1 : 67</span>
                </div>
                <div class="bg-slate-50 border border-slate-200 rounded-2xl p-3.5 text-center">
                    <span class="text-[11px] font-bold text-slate-600 uppercase tracking-wider block" id="colDrop">Dislivello Totale (ΔH)</span>
                    <span class="text-2xl sm:text-3xl font-black font-mono text-slate-900 block mt-1" id="resDrop">6.0 cm</span>
                    <span class="text-[10px] text-slate-500 font-mono block mt-0.5" id="resDropMm">60 mm</span>
                </div>
                <div class="bg-slate-50 border border-slate-200 rounded-2xl p-3.5 text-center">
                    <span class="text-[11px] font-bold text-slate-600 uppercase tracking-wider block" id="colDropPerMeter">Caduta per Metro</span>
                    <span class="text-2xl sm:text-3xl font-black font-mono text-slate-900 block mt-1" id="resDropMeter">1.5 cm/m</span>
                    <span class="text-[10px] text-slate-500 font-mono block mt-0.5" id="resDropMeterMm">15 mm al metro</span>
                </div>
                <div class="bg-slate-50 border border-slate-200 rounded-2xl p-3.5 text-center">
                    <span class="text-[11px] font-bold text-slate-600 uppercase tracking-wider block" id="colAngle">Inclinazione</span>
                    <span class="text-2xl sm:text-3xl font-black font-mono text-slate-900 block mt-1" id="resAngle">0.86 °</span>
                    <span class="text-[10px] text-slate-500 font-semibold block mt-0.5" id="resDiamBadge">Ø 110 mm</span>
                </div>
            </div>

            <!-- Dynamic Compliance & Self-Cleansing Status -->
            <div id="statusContainer" class="p-4 sm:p-5 rounded-2xl border transition-all">
                <div class="flex items-start gap-3">
                    <div id="statusIcon" class="text-2xl sm:text-3xl shrink-0 mt-0.5">🟢</div>
                    <div class="space-y-1">
                        <div class="flex items-center gap-2 flex-wrap">
                            <h3 id="statusTitle" class="text-sm sm:text-base font-bold text-slate-900">Pendenza Ottimale — Autopulente (1.0% - 2.0%)</h3>
                            <span id="statusTag" class="text-[10px] font-extrabold uppercase px-2 py-0.5 rounded-full bg-emerald-100 text-emerald-800 border border-emerald-300">Conforme UNI EN 12056</span>
                        </div>
                        <p id="statusDesc" class="text-xs sm:text-sm text-slate-600 leading-relaxed">
                            Velocità di scorrimento ideale (0.7 - 2.0 m/s). L'acqua trascina efficacemente i corpi solidi senza sedimentazione né svuotamento rapido.
                        </p>
                    </div>
                </div>
            </div>

            <!-- Blueprint SVG Technical Diagram -->
            <div class="space-y-2">
                <div class="flex justify-between items-center">
                    <span class="text-xs font-bold text-slate-700 uppercase tracking-wider" id="schemaTitle">Schema Tecnico Sezione Tubazione e Flusso Idraulico</span>
                    <span class="text-[10px] text-slate-500 font-mono">Scala interattiva 1:1</span>
                </div>

                <div class="bg-slate-900 rounded-2xl p-4 sm:p-6 overflow-hidden relative shadow-inner">
                    <svg id="pipeSvg" class="w-full h-44 sm:h-56" viewBox="0 0 600 220" xmlns="http://www.w3.org/2000/svg">
                        <defs>
                            <linearGradient id="pipeGrad" x1="0%" y1="0%" x2="100%" y2="100%">
                                <stop offset="0%" stop-color="#ea580c"/>
                                <stop offset="100%" stop-color="#c2410c"/>
                            </linearGradient>
                            <linearGradient id="waterGrad" x1="0%" y1="0%" x2="100%" y2="0%">
                                <stop offset="0%" stop-color="#38bdf8" stop-opacity="0.8"/>
                                <stop offset="100%" stop-color="#0284c7" stop-opacity="0.9"/>
                            </linearGradient>
                            <pattern id="gridPattern" width="20" height="20" patternUnits="userSpaceOnUse">
                                <path d="M 20 0 L 0 0 0 20" fill="none" stroke="#1e293b" stroke-width="0.8"/>
                            </pattern>
                        </defs>

                        <!-- Blueprint Grid -->
                        <rect width="600" height="220" fill="url(#gridPattern)"/>

                        <!-- Baseline level reference -->
                        <line x1="40" y1="180" x2="560" y2="180" stroke="#334155" stroke-dasharray="4 4" stroke-width="1.5"/>
                        <text x="45" y="195" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="10">Piano di Riferimento Orizzontale (Livella 0.0°)</text>

                        <!-- Dynamic Sloping Pipe -->
                        <g id="svgPipeGroup">
                            <!-- Pipe Body -->
                            <line id="svgPipeTop" x1="70" y1="80" x2="510" y2="130" stroke="#ea580c" stroke-width="28" stroke-linecap="round"/>
                            <line id="svgPipeInner" x1="70" y1="80" x2="510" y2="130" stroke="#1e293b" stroke-width="20" stroke-linecap="round"/>
                            <!-- Water flow layer -->
                            <line id="svgWater" x1="70" y1="86" x2="510" y2="136" stroke="url(#waterGrad)" stroke-width="8" stroke-linecap="round"/>

                            <!-- Direction arrows inside water -->
                            <path id="svgArrow1" d="M 240 100 L 255 104 L 240 108" fill="none" stroke="#ffffff" stroke-width="2" stroke-linecap="round"/>
                            <path id="svgArrow2" d="M 340 115 L 355 119 L 340 123" fill="none" stroke="#ffffff" stroke-width="2" stroke-linecap="round"/>

                            <!-- Inlet & Outlet Nodes -->
                            <circle id="svgInlet" cx="70" cy="80" r="16" fill="#3b82f6" fill-opacity="0.3" stroke="#60a5fa" stroke-width="2"/>
                            <text id="svgInletText" x="70" y="55" fill="#93c5fd" font-family="'Plus Jakarta Sans', sans-serif" font-weight="bold" font-size="11" text-anchor="middle">INGRESSO (Quota Alta)</text>

                            <circle id="svgOutlet" cx="510" cy="130" r="16" fill="#10b981" fill-opacity="0.3" stroke="#34d399" stroke-width="2"/>
                            <text id="svgOutletText" x="510" y="165" fill="#6ee7b7" font-family="'Plus Jakarta Sans', sans-serif" font-weight="bold" font-size="11" text-anchor="middle">SCARICO (Quota Bassa)</text>

                            <!-- Vertical Fall Delta H Line -->
                            <line id="svgDropLine" x1="535" y1="80" x2="535" y2="130" stroke="#f43f5e" stroke-width="2"/>
                            <line x1="527" y1="80" x2="543" y2="80" stroke="#f43f5e" stroke-width="1.5"/>
                            <line x1="527" y1="130" x2="543" y2="130" stroke="#f43f5e" stroke-width="1.5"/>
                            <text id="svgDropLabel" x="550" y="110" fill="#fda4af" font-family="'JetBrains Mono', monospace" font-weight="bold" font-size="11">ΔH = 6.0 cm</text>

                            <!-- Horizontal Length Dimension Line -->
                            <line x1="70" y1="30" x2="510" y2="30" stroke="#94a3b8" stroke-width="1.5"/>
                            <line x1="70" y1="24" x2="70" y2="36" stroke="#94a3b8" stroke-width="1.5"/>
                            <line x1="510" y1="24" x2="510" y2="36" stroke="#94a3b8" stroke-width="1.5"/>
                            <text id="svgLengthLabel" x="290" y="24" fill="#cbd5e1" font-family="'JetBrains Mono', monospace" font-weight="bold" font-size="11" text-anchor="middle">L = 4.0 m</text>
                            
                            <!-- Slope Callout in center -->
                            <rect x="235" y="145" width="110" height="26" rx="6" fill="#0f172a" stroke="#3b82f6" stroke-width="1.5"/>
                            <text id="svgSlopeCallout" x="290" y="162" fill="#38bdf8" font-family="'JetBrains Mono', monospace" font-weight="bold" font-size="12" text-anchor="middle">p = 1.5 %</text>
                        </g>
                    </svg>
                </div>
            </div>

                            <!-- DEDICATED PRINT-ONLY TECHNICAL NOTES & SIGNATURE BOX -->
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
                </div>

            <!-- Action Buttons: Print & Copy -->
            <div class="flex flex-col sm:flex-row gap-3 pt-2 no-print">
                <button type="button" onclick="window.print()" class="flex-1 py-3 px-4 rounded-xl bg-slate-900 hover:bg-slate-800 text-white font-bold text-xs sm:text-sm flex items-center justify-center gap-2 transition cursor-pointer shadow-sm">
                    <span>🖨️</span> <span id="btnPrint">Stampa Scheda Cantiere A4</span>
                </button>
                <button type="button" onclick="copyResults()" class="flex-1 py-3 px-4 rounded-xl bg-slate-100 hover:bg-slate-200 border border-slate-200 text-slate-800 font-bold text-xs sm:text-sm flex items-center justify-center gap-2 transition cursor-pointer">
                    <span id="copyIcon">📋</span> <span id="btnCopy">Copia Dati per Computo Metrico</span>
                </button>
            </div>
        </div>

        <!-- Social Share Strip -->
        <div id="shareStrip" class="bg-white rounded-2xl border border-slate-200/80 p-4 sm:p-5 flex flex-col sm:flex-row items-center justify-between gap-4 shadow-2xs no-print">
            <div class="text-center sm:text-left">
                <h3 class="text-xs sm:text-sm font-bold text-slate-900" id="shareTitle">Ti è utile questo calcolatore per scarichi?</h3>
                <p class="text-[11px] text-slate-500" id="shareSub">Condividi lo strumento con colleghi termoidraulici, geometri o installatori</p>
            </div>
            <div class="flex items-center gap-2 shrink-0">
                <a id="shareWa" href="#" target="_blank" rel="noopener noreferrer" class="p-2.5 rounded-xl bg-emerald-50 text-emerald-700 hover:bg-emerald-100 border border-emerald-200/80 text-xs font-bold transition flex items-center gap-1.5">
                    <span>💬 WhatsApp</span>
                </a>
                <a id="shareLi" href="#" target="_blank" rel="noopener noreferrer" class="p-2.5 rounded-xl bg-blue-50 text-blue-700 hover:bg-blue-100 border border-blue-200/80 text-xs font-bold transition flex items-center gap-1.5">
                    <span>💼 LinkedIn</span>
                </a>
                <button type="button" onclick="copyShareUrl()" class="p-2.5 rounded-xl bg-slate-100 text-slate-700 hover:bg-slate-200 border border-slate-200/80 text-xs font-bold transition flex items-center gap-1.5 cursor-pointer">
                    <span id="shareCopyText">🔗 Copia Link</span>
                </button>
            </div>
        </div>

        <!-- Technical Normative Guide & Reference Table -->
        <section id="normSection" class="no-print bg-white rounded-3xl border border-slate-200 shadow-sm p-5 sm:p-8 space-y-6">
            <div class="space-y-2">
                <h2 class="text-lg sm:text-xl font-black text-slate-900 font-jakarta" id="normTitle">Quadro Tecnico Normativo (UNI EN 12056 & UNI EN 752)</h2>
                <p class="text-xs sm:text-sm text-slate-600 leading-relaxed" id="normP1">
                    La norma <strong>UNI EN 12056-2</strong> disciplina i sistemi di scarico per gravità all'interno degli edifici. La regola cardine dell'ingegneria idraulica è garantire il fenomeno dell'<strong>autopulizia</strong>: una velocità compresa tra 0.7 m/s e 2.5 m/s ad almeno il 50% di riempimento del condotto.
                </p>
            </div>

            <div class="overflow-x-auto rounded-2xl border border-slate-200">
                <table class="w-full text-left text-xs sm:text-sm">
                    <thead class="bg-slate-100 text-slate-700 font-bold uppercase tracking-wider text-[11px]">
                        <tr>
                            <th class="py-3 px-4" id="thDest">Destinazione Scarico</th>
                            <th class="py-3 px-4" id="thDiam">Diametro Ø</th>
                            <th class="py-3 px-4" id="thSlope">Pendenza Consigliata</th>
                            <th class="py-3 px-4" id="thNote">Requisito di Progetto</th>
                        </tr>
                    </thead>
                    <tbody class="divide-y divide-slate-200 font-medium text-slate-700">
                        <tr class="hover:bg-slate-50">
                            <td class="py-3 px-4 font-bold text-slate-900" id="row1Dest">Scarichi singoli (lavabi, bidet)</td>
                            <td class="py-3 px-4 font-mono font-bold text-blue-700" id="row1Diam">Ø 40 - 50 mm</td>
                            <td class="py-3 px-4 font-mono font-bold text-emerald-700" id="row1Slope">1.5% - 2.5% (1.5 - 2.5 cm/m)</td>
                            <td class="py-3 px-4 text-slate-500" id="row1Note">Evitare gomiti a 90° secchi; preferire 2 curve a 45°</td>
                        </tr>
                        <tr class="hover:bg-slate-50">
                            <td class="py-3 px-4 font-bold text-slate-900" id="row2Dest">Scarichi WC (acque nere)</td>
                            <td class="py-3 px-4 font-mono font-bold text-blue-700" id="row2Diam">Ø 90 - 110 mm</td>
                            <td class="py-3 px-4 font-mono font-bold text-emerald-700" id="row2Slope">1.2% - 2.0% (1.2 - 2.0 cm/m)</td>
                            <td class="py-3 px-4 text-slate-500" id="row2Note">Pendenza minima tassativa 1.0% per non lasciare solidi</td>
                        </tr>
                        <tr class="hover:bg-slate-50">
                            <td class="py-3 px-4 font-bold text-slate-900" id="row3Dest">Collettori orizzontali interrati</td>
                            <td class="py-3 px-4 font-mono font-bold text-blue-700" id="row3Diam">Ø 125 - 160 mm</td>
                            <td class="py-3 px-4 font-mono font-bold text-emerald-700" id="row3Slope">1.0% - 1.5% (1.0 - 1.5 cm/m)</td>
                            <td class="py-3 px-4 text-slate-500" id="row3Note">Conforme a UNI EN 752 per fognature esterne</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </section>

        <!-- FAQ Accordion Section -->
        <section id="faqSection" class="no-print bg-white rounded-3xl border border-slate-200 shadow-sm p-5 sm:p-8 space-y-4">
            <h2 class="text-lg sm:text-xl font-black text-slate-900 font-jakarta mb-4" id="faqTitle">Domande Frequenti su Pendenze Tubi e Scarichi</h2>
            
            <div class="space-y-3">
                <details class="group bg-slate-50 rounded-2xl border border-slate-200/80 p-4 [&_svg]:open:-rotate-180 transition">
                    <summary class="flex justify-between items-center font-bold text-xs sm:text-sm text-slate-900 cursor-pointer list-none">
                        <span id="faq1Q">Qual è la pendenza minima obbligatoria per un tubo di scarico fognario?</span>
                        <svg class="w-4 h-4 text-slate-500 transition-transform duration-200" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/>
                        </svg>
                    </summary>
                    <p class="text-xs sm:text-sm text-slate-600 mt-3 leading-relaxed border-t border-slate-200/60 pt-3" id="faq1A">
                        La pendenza minima raccomandata dalle norme tecniche europee (UNI EN 12056) è dell'<strong>1% (1 cm per ogni metro lineare)</strong>. Al di sotto di questa soglia l'acqua non raggiunge la velocità di 0.7 m/s necessaria a trascinare carta e deiezioni, provocando depositi e cattivi odori.
                    </p>
                </details>

                <details class="group bg-slate-50 rounded-2xl border border-slate-200/80 p-4 [&_svg]:open:-rotate-180 transition">
                    <summary class="flex justify-between items-center font-bold text-xs sm:text-sm text-slate-900 cursor-pointer list-none">
                        <span id="faq2Q">Cosa succede se la pendenza dello scarico è troppo ripida (es. 5-10%)?</span>
                        <svg class="w-4 h-4 text-slate-500 transition-transform duration-200" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/>
                        </svg>
                    </summary>
                    <p class="text-xs sm:text-sm text-slate-600 mt-3 leading-relaxed border-t border-slate-200/60 pt-3" id="faq2A">
                        È un errore comune pensare che 'più pendenza c'è, meglio scorre'. Sopra il 3.5-4%, l'acqua scivola via a forte velocità mentre i solidi pesanti rimangono fermi sul fondo del tubo per attrito (separazione liquido-solido), creando intasamenti cronici.
                    </p>
                </details>

                <details class="group bg-slate-50 rounded-2xl border border-slate-200/80 p-4 [&_svg]:open:-rotate-180 transition">
                    <summary class="flex justify-between items-center font-bold text-xs sm:text-sm text-slate-900 cursor-pointer list-none">
                        <span id="faq3Q">Come si calcola il dislivello tra punto di partenza e punto di arrivo?</span>
                        <svg class="w-4 h-4 text-slate-500 transition-transform duration-200" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/>
                        </svg>
                    </summary>
                    <p class="text-xs sm:text-sm text-slate-600 mt-3 leading-relaxed border-t border-slate-200/60 pt-3" id="faq3A">
                        Formula: <code>Dislivello (cm) = Lunghezza (metri) × Pendenza (%)</code>. Ad esempio, per un tubo lungo 4 metri con pendenza 1.5%, la caduta necessaria è: 4 × 1.5 = 6 cm.
                    </p>
                </details>

                <details class="group bg-slate-50 rounded-2xl border border-slate-200/80 p-4 [&_svg]:open:-rotate-180 transition">
                    <summary class="flex justify-between items-center font-bold text-xs sm:text-sm text-slate-900 cursor-pointer list-none">
                        <span id="faq4Q">Che differenza c'è tra Ø nominale interno ed esterno nei tubi in PVC/PP?</span>
                        <svg class="w-4 h-4 text-slate-500 transition-transform duration-200" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/>
                        </svg>
                    </summary>
                    <p class="text-xs sm:text-sm text-slate-600 mt-3 leading-relaxed border-t border-slate-200/60 pt-3" id="faq4A">
                        I tubi plastici per edilizia (PVC arancione o PP insonorizzato) sono commercialmente identificati dal diametro esterno (DE). Il diametro interno utile dipende dallo spessore della parete (es. tubo Ø 110 spessore 3.2 mm ha diametro interno utile di 103.6 mm).
                    </p>
                </details>
            </div>
        </section>

    </main>

    <!-- Footer -->
    <footer class="bg-white border-t border-slate-200 py-8 px-4 text-center mt-12 no-print">
        <div class="max-w-4xl mx-auto space-y-4">
            <div class="flex items-center justify-center gap-4 text-xs font-bold text-slate-600 flex-wrap">
                <a href="/" class="hover:text-blue-600 transition">Suite Hub</a>
                <span>•</span>
                <a href="/rampe" class="hover:text-blue-600 transition">RampaFacile</a>
                <span>•</span>
                <a href="/scale" class="hover:text-blue-600 transition">ScalaFacile</a>
                <span>•</span>
                <a href="/tubi" class="text-blue-600">ScaricoFacile</a>
                <span>•</span>
                <a href="/dorso" class="hover:text-blue-600 transition">DorsoFacile</a>
                <span>•</span>
                <a href="/dpi" class="hover:text-blue-600 transition">RisoluzioneFacile</a>
                <span>•</span>
                <a href="/partnership" class="text-indigo-600 hover:underline">Diventa Partner / Sponsor</a>
            </div>
            <p id="legalDisclaimer" class="text-xs text-slate-400 max-w-2xl mx-auto leading-relaxed">
                <strong>Note Tecniche:</strong> Il presente calcolatore fornisce valori indicativi basati sulle norme UNI EN 12056 e UNI EN 752. La verifica esecutiva delle reti fognarie complesse richiede l'asseverazione del progettista idraulico o termotecnico abilitato.
            </p>
            <p id="rightsReserved" class="text-xs font-bold text-slate-600">
                © 2026 OmniTools Lab — Precision Utilities Suite. Tutti i diritti riservati.
            </p>
        </div>
    </footer>

    <!-- JavaScript Application Logic -->
    <script>
        const TRANSLATIONS = {t_json_str};
        let currentLang = 'it';
        let currentMode = 'bySlope'; // 'bySlope' or 'byDrop'

        const numLength = document.getElementById('numLength');
        const rngLength = document.getElementById('rngLength');
        const numSlope = document.getElementById('numSlope');
        const rngSlope = document.getElementById('rngSlope');
        const numDrop = document.getElementById('numDrop');
        const rngDrop = document.getElementById('rngDrop');
        const selDiameter = document.getElementById('selDiameter');

        // Sync inputs
        numLength.addEventListener('input', () => {{ rngLength.value = numLength.value; calculate(); }});
        rngLength.addEventListener('input', () => {{ numLength.value = rngLength.value; calculate(); }});
        
        numSlope.addEventListener('input', () => {{ rngSlope.value = numSlope.value; calculate(); }});
        rngSlope.addEventListener('input', () => {{ numSlope.value = rngSlope.value; calculate(); }});
        
        numDrop.addEventListener('input', () => {{ rngDrop.value = numDrop.value; calculate(); }});
        rngDrop.addEventListener('input', () => {{ numDrop.value = rngDrop.value; calculate(); }});

        function setMode(mode) {{
            currentMode = mode;
            const tabSlope = document.getElementById('tabModeBySlope');
            const tabDrop = document.getElementById('tabModeByDrop');
            const boxSlope = document.getElementById('slopeInputBox');
            const boxDrop = document.getElementById('dropInputBox');

            if (mode === 'bySlope') {{
                tabSlope.className = 'py-2.5 px-3 rounded-xl text-xs sm:text-sm font-bold transition shadow-xs bg-white text-blue-700 cursor-pointer';
                tabDrop.className = 'py-2.5 px-3 rounded-xl text-xs sm:text-sm font-bold transition text-slate-600 hover:text-slate-900 cursor-pointer';
                boxSlope.classList.remove('hidden');
                boxDrop.classList.add('hidden');
            }} else {{
                tabDrop.className = 'py-2.5 px-3 rounded-xl text-xs sm:text-sm font-bold transition shadow-xs bg-white text-blue-700 cursor-pointer';
                tabSlope.className = 'py-2.5 px-3 rounded-xl text-xs sm:text-sm font-bold transition text-slate-600 hover:text-slate-900 cursor-pointer';
                boxDrop.classList.remove('hidden');
                boxSlope.classList.add('hidden');
            }}
            calculate();
        }}

        function applyPreset(length, slope, diameter) {{
            numLength.value = length;
            rngLength.value = length;
            numSlope.value = slope;
            rngSlope.value = slope;
            selDiameter.value = diameter;
            if (currentMode !== 'bySlope') {{
                setMode('bySlope');
            }} else {{
                calculate();
            }}
        }}

        function calculate() {{
            const L = parseFloat(numLength.value) || 1.0; // meters
            let slopePercent = 1.5;
            let dropCm = 6.0;

            if (currentMode === 'bySlope') {{
                slopePercent = parseFloat(numSlope.value) || 1.5;
                dropCm = L * slopePercent;
                numDrop.value = dropCm.toFixed(1);
                rngDrop.value = Math.min(50, dropCm);
            }} else {{
                dropCm = parseFloat(numDrop.value) || 1.0;
                slopePercent = dropCm / L;
                numSlope.value = slopePercent.toFixed(2);
                rngSlope.value = Math.min(6, slopePercent);
            }}

            const dropMm = dropCm * 10;
            const dropPerMeterCm = slopePercent;
            const dropPerMeterMm = slopePercent * 10;
            const angleRad = Math.atan(slopePercent / 100);
            const angleDeg = angleRad * (180 / Math.PI);
            const ratio = slopePercent > 0 ? Math.round(100 / slopePercent) : 0;
            const diam = selDiameter.value;

            // Update UI metrics
            document.getElementById('resSlope').textContent = slopePercent.toFixed(2) + ' %';
            document.getElementById('resRatio').textContent = '1 : ' + ratio + ' (1 cm ogni ' + ratio + ' cm)';
            document.getElementById('resDrop').textContent = dropCm.toFixed(1) + ' cm';
            document.getElementById('resDropMm').textContent = Math.round(dropMm) + ' mm';
            document.getElementById('resDropMeter').textContent = dropPerMeterCm.toFixed(1) + ' cm/m';
            document.getElementById('resDropMeterMm').textContent = dropPerMeterMm.toFixed(0) + ' mm al metro';
            document.getElementById('resAngle').textContent = angleDeg.toFixed(2) + ' °';
            document.getElementById('resDiamBadge').textContent = 'Ø ' + diam + ' mm';

            // Update Compliance Status Banner
            updateStatus(slopePercent);

            // Update Interactive Blueprint SVG
            updateSvg(L, slopePercent, dropCm, diam);

            // Update Social Share URLs
            updateShareUrls(L, slopePercent, dropCm, diam);
        }}

        function updateStatus(slope) {{
            const container = document.getElementById('statusContainer');
            const icon = document.getElementById('statusIcon');
            const title = document.getElementById('statusTitle');
            const tag = document.getElementById('statusTag');
            const desc = document.getElementById('statusDesc');
            const t = TRANSLATIONS[currentLang];

            if (slope < 1.0) {{
                container.className = 'p-4 sm:p-5 rounded-2xl border transition-all bg-rose-50/90 border-rose-200 text-rose-900';
                icon.textContent = '🔴';
                title.textContent = t.status_low_title;
                tag.className = 'text-[10px] font-extrabold uppercase px-2 py-0.5 rounded-full bg-rose-200 text-rose-900 border border-rose-300';
                tag.textContent = t.status_low_tag;
                desc.textContent = t.status_low_desc;
            }} else if (slope >= 1.0 && slope <= 2.0) {{
                container.className = 'p-4 sm:p-5 rounded-2xl border transition-all bg-emerald-50/90 border-emerald-200 text-emerald-900';
                icon.textContent = '🟢';
                title.textContent = t.status_ideal_title;
                tag.className = 'text-[10px] font-extrabold uppercase px-2 py-0.5 rounded-full bg-emerald-200 text-emerald-900 border border-emerald-300';
                tag.textContent = t.status_ideal_tag;
                desc.textContent = t.status_ideal_desc;
            }} else if (slope > 2.0 && slope <= 3.5) {{
                container.className = 'p-4 sm:p-5 rounded-2xl border transition-all bg-amber-50/90 border-amber-200 text-amber-900';
                icon.textContent = '🟡';
                title.textContent = t.status_acc_title;
                tag.className = 'text-[10px] font-extrabold uppercase px-2 py-0.5 rounded-full bg-amber-200 text-amber-900 border border-amber-300';
                tag.textContent = t.status_acc_tag;
                desc.textContent = t.status_acc_desc;
            }} else {{
                container.className = 'p-4 sm:p-5 rounded-2xl border transition-all bg-rose-50/90 border-rose-200 text-rose-900';
                icon.textContent = '⚠️';
                title.textContent = t.status_high_title;
                tag.className = 'text-[10px] font-extrabold uppercase px-2 py-0.5 rounded-full bg-rose-200 text-rose-900 border border-rose-300';
                tag.textContent = t.status_high_tag;
                desc.textContent = t.status_high_desc;
            }}
        }}

        function updateSvg(L, slope, dropCm, diam) {{
            // SVG coordinate mapping
            const startX = 70;
            const endX = 510;
            const startY = 75;
            
            // Visual slope clamped for clear schematics
            const visualDrop = Math.min(70, Math.max(15, slope * 18));
            const endY = startY + visualDrop;

            const pipeTop = document.getElementById('svgPipeTop');
            const pipeInner = document.getElementById('svgPipeInner');
            const water = document.getElementById('svgWater');
            const inlet = document.getElementById('svgInlet');
            const outlet = document.getElementById('svgOutlet');
            const inletText = document.getElementById('svgInletText');
            const outletText = document.getElementById('svgOutletText');
            const dropLine = document.getElementById('svgDropLine');
            const dropLabel = document.getElementById('svgDropLabel');
            const lengthLabel = document.getElementById('svgLengthLabel');
            const slopeCallout = document.getElementById('svgSlopeCallout');

            pipeTop.setAttribute('y2', endY);
            pipeInner.setAttribute('y2', endY);
            water.setAttribute('y2', endY + 6);

            outlet.setAttribute('cy', endY);
            outletText.setAttribute('y', endY + 35);

            dropLine.setAttribute('y1', startY);
            dropLine.setAttribute('y2', endY);
            dropLabel.setAttribute('y', startY + visualDrop / 2 + 4);
            dropLabel.textContent = `ΔH = ${{dropCm.toFixed(1)}} cm`;

            lengthLabel.textContent = `L = ${{L.toFixed(1)}} m (Ø ${{diam}} mm)`;
            slopeCallout.textContent = `p = ${{slope.toFixed(1)}} %`;
        }}

        function copyResults() {{
            const L = numLength.value;
            const p = document.getElementById('resSlope').textContent;
            const drop = document.getElementById('resDrop').textContent;
            const dropMeter = document.getElementById('resDropMeter').textContent;
            const diam = selDiameter.value;

            const text = `Tubazione Ø ${{diam}} mm | Lunghezza: ${{L}} m | Pendenza: ${{p}} | Dislivello Totale: ${{drop}} | Caduta al metro: ${{dropMeter}} (OmniTools Lab ScaricoFacile)`;
            navigator.clipboard.writeText(text).then(() => {{
                const btn = document.getElementById('btnCopy');
                const orig = btn.textContent;
                btn.textContent = '✓ Valori Copiati!';
                setTimeout(() => {{ btn.textContent = orig; }}, 2000);
            }});
        }}

        function updateShareUrls(L, slope, dropCm, diam) {{
            const url = 'https://www.omnitoolslab.com/tubi';
            const msg = `ScaricoFacile: calcolo rapido pendenza tubi fognatura e scarichi. Lunghezza ${{L}}m, pendenza ${{slope.toFixed(1)}}%, caduta ${{dropCm.toFixed(1)}}cm: ${{url}}`;
            document.getElementById('shareWa').href = `https://api.whatsapp.com/send?text=${{encodeURIComponent(msg)}}`;
            document.getElementById('shareLi').href = `https://www.linkedin.com/sharing/share-offsite/?url=${{encodeURIComponent(url)}}`;
        }}

        function copyShareUrl() {{
            navigator.clipboard.writeText('https://www.omnitoolslab.com/tubi').then(() => {{
                const el = document.getElementById('shareCopyText');
                el.textContent = '✓ Copiato!';
                setTimeout(() => {{ el.textContent = '🔗 Copia Link'; }}, 2000);
            }});
        }}

        function changeLanguage(lang) {{
            if (!TRANSLATIONS[lang]) return;
            currentLang = lang;
            document.documentElement.lang = lang;
            const t = TRANSLATIONS[lang];

            document.title = t.title;
            document.getElementById('toolBadge').textContent = t.tool_badge;
            document.getElementById('heroTitle').textContent = t.hero_title;
            document.getElementById('heroDesc').textContent = t.hero_desc;
            document.getElementById('tabModeBySlope').textContent = t.mode_by_slope;
            document.getElementById('tabModeByDrop').textContent = t.mode_by_drop;
            document.getElementById('lblPipeLength').textContent = t.pipe_length_label;
            document.getElementById('lblPipeSlope').textContent = t.pipe_slope_label;
            document.getElementById('lblPipeDrop').textContent = t.pipe_drop_label;
            document.getElementById('lblPipeDiameter').textContent = t.pipe_diameter_label;

            document.getElementById('optD40').textContent = t.opt_d40;
            document.getElementById('optD50').textContent = t.opt_d50;
            document.getElementById('optD90').textContent = t.opt_d90;
            document.getElementById('optD110').textContent = t.opt_d110;
            document.getElementById('optD125').textContent = t.opt_d125;
            document.getElementById('optD160').textContent = t.opt_d160;
            document.getElementById('optD200').textContent = t.opt_d200;

            document.getElementById('presetsTitle').textContent = t.presets_title;
            document.getElementById('p1Title').textContent = t.preset_1;
            document.getElementById('p1Sub').textContent = t.preset_1_sub;
            document.getElementById('p2Title').textContent = t.preset_2;
            document.getElementById('p2Sub').textContent = t.preset_2_sub;
            document.getElementById('p3Title').textContent = t.preset_3;
            document.getElementById('p3Sub').textContent = t.preset_3_sub;
            document.getElementById('p4Title').textContent = t.preset_4;
            document.getElementById('p4Sub').textContent = t.preset_4_sub;

            document.getElementById('colSlope').textContent = t.col_slope;
            document.getElementById('colDrop').textContent = t.col_drop;
            document.getElementById('colDropPerMeter').textContent = t.col_drop_per_meter;
            document.getElementById('colAngle').textContent = t.col_angle;
            document.getElementById('schemaTitle').textContent = t.schema_title;

            document.getElementById('normTitle').textContent = t.norm_title;
            document.getElementById('normP1').innerHTML = t.norm_p1;
            document.getElementById('thDest').textContent = t.norm_table_th_dest;
            document.getElementById('thDiam').textContent = t.norm_table_th_diam;
            document.getElementById('thSlope').textContent = t.norm_table_th_slope;
            document.getElementById('thNote').textContent = t.norm_table_th_note;

            document.getElementById('row1Dest').textContent = t.norm_row1_dest;
            document.getElementById('row1Diam').textContent = t.norm_row1_diam;
            document.getElementById('row1Slope').textContent = t.norm_row1_slope;
            document.getElementById('row1Note').textContent = t.norm_row1_note;

            document.getElementById('row2Dest').textContent = t.norm_row2_dest;
            document.getElementById('row2Diam').textContent = t.norm_row2_diam;
            document.getElementById('row2Slope').textContent = t.norm_row2_slope;
            document.getElementById('row2Note').textContent = t.norm_row2_note;

            document.getElementById('row3Dest').textContent = t.norm_row3_dest;
            document.getElementById('row3Diam').textContent = t.norm_row3_diam;
            document.getElementById('row3Slope').textContent = t.norm_row3_slope;
            document.getElementById('row3Note').textContent = t.norm_row3_note;

            document.getElementById('faqTitle').textContent = t.faq_title;
            document.getElementById('faq1Q').textContent = t.faq_1_q;
            document.getElementById('faq1A').innerHTML = t.faq_1_a;
            document.getElementById('faq2Q').textContent = t.faq_2_q;
            document.getElementById('faq2A').innerHTML = t.faq_2_a;
            document.getElementById('faq3Q').textContent = t.faq_3_q;
            document.getElementById('faq3A').innerHTML = t.faq_3_a;
            document.getElementById('faq4Q').textContent = t.faq_4_q;
            document.getElementById('faq4A').innerHTML = t.faq_4_a;

            document.getElementById('printSheetTitle').textContent = t.print_sheet_title;
            document.getElementById('btnPrint').textContent = t.print_btn;
            document.getElementById('legalDisclaimer').innerHTML = t.legal_disclaimer;
            document.getElementById('rightsReserved').textContent = t.rights_reserved;
            document.getElementById('shareTitle').textContent = t.share_title;
            document.getElementById('shareSub').textContent = t.share_sub;

            document.getElementById('langSelect').value = lang;
            localStorage.setItem('omni_lang', lang);

            calculate();
        }}

        // Initialization
        document.addEventListener('DOMContentLoaded', () => {{
            const stored = localStorage.getItem('omni_lang');
            if (stored && TRANSLATIONS[stored]) {{
                changeLanguage(stored);
            }} else {{
                const navLang = (navigator.language || 'it').substring(0, 2).toLowerCase();
                if (TRANSLATIONS[navLang]) {{
                    changeLanguage(navLang);
                }} else {{
                    calculate();
                }}
            }}
        }});
    </script>
</body>
</html>
"""

with open('/Users/ilalu/Documents/Altenative Businnes/Calcolatore_Pendenza/tubi.html', 'w', encoding='utf-8') as f:
    f.write(html_code)

print("tubi.html compiled successfully!")
