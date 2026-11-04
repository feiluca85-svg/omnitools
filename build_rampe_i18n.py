import json

with open('/Users/ilalu/Documents/Altenative Businnes/Calcolatore_Pendenza/translations.json', 'r', encoding='utf-8') as f:
    t_data = json.load(f)

# Update install banner titles for OmniTools
for lang, tr in t_data.items():
    if lang == 'it':
        tr['install_banner_title'] = "Installa OmniTools come App"
        tr['install_banner_sub'] = "I tuoi calcolatori di cantiere pronti anche offline"
    elif lang == 'en':
        tr['install_banner_title'] = "Install OmniTools as App"
        tr['install_banner_sub'] = "Field & engineering calculators ready offline"
    elif lang == 'es':
        tr['install_banner_title'] = "Instala OmniTools como App"
        tr['install_banner_sub'] = "Tus herramientas de obra listas sin conexión"
    elif lang == 'fr':
        tr['install_banner_title'] = "Installer OmniTools sur Smartphone"
        tr['install_banner_sub'] = "Vos outils de chantier utilisables hors-ligne"
    elif lang == 'de':
        tr['install_banner_title'] = "OmniTools als App nutzen"
        tr['install_banner_sub'] = "Praktische Baurechner jederzeit auch offline"
    elif lang == 'pt':
        tr['install_banner_title'] = "Instale OmniTools no Telemóvel"
        tr['install_banner_sub'] = "Ferramentas de obra disponíveis sem internet"

with open('/Users/ilalu/Documents/Altenative Businnes/Calcolatore_Pendenza/translations.json', 'w', encoding='utf-8') as f:
    json.dump(t_data, f, ensure_ascii=False, indent=2)

t_json_str = json.dumps(t_data, ensure_ascii=False)

html_code = f"""<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0">
    <title>Calcolo Pendenza Rampa Disabili e Garage Online — Formula DM 236/89 & ADA</title>
    <meta name="description" content="Calcolatore professionale per pendenza rampe in percentuale (%) e gradi, dislivello e sviluppo a terra. Verifica immediata conformità per disabili e carrozzine (DM 236/89, ADA) e rampe carrabili autorimesse.">
    
    <!-- Google Search Console Verification -->
    <meta name="google-site-verification" content="MRdbDm9lLhokeD3I0FOpUSOhNaF_2WaveKvu52FxtG4">

    <!-- Canonical & SEO Meta Tags -->
    <link rel="canonical" href="https://www.omnitoolslab.com/rampe">
    <meta name="robots" content="index, follow">
    <meta property="og:type" content="website">
    <meta property="og:title" content="OmniTools - Calcolo Pendenza Rampa & Dislivello">
    <meta property="og:description" content="Calcolatore professionale di pendenza rampa e dislivello con verifica conformità DM 236/89 e ADA in 6 lingue.">
    <meta property="og:url" content="https://www.omnitoolslab.com/rampe">
    <meta property="og:site_name" content="OmniTools Lab">
    <meta property="og:image" content="https://www.omnitoolslab.com/og-rampe.png">
    <meta property="og:image:width" content="1200">
    <meta property="og:image:height" content="630">
    <meta property="og:image:type" content="image/png">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:image" content="https://www.omnitoolslab.com/og-rampe.png">

    <!-- Schema.org JSON-LD Structured Data for Googlebot (Rich Snippets) -->
    <script type="application/ld+json">
    [
      {{
        "@context": "https://schema.org",
        "@type": "WebApplication",
        "name": "OmniTools - Calcolo Pendenza Rampa & Dislivello",
        "url": "https://www.omnitoolslab.com/rampe",
        "applicationCategory": "UtilitiesApplication",
        "operatingSystem": "All",
        "description": "Calcolatore professionale di pendenza rampa con verifica conformità disabili (DM 236/89, ADA, CTE, PMR, DIN) e veicoli in 6 lingue.",
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
            "name": "RampaFacile",
            "item": "https://www.omnitoolslab.com/rampe"
          }}
        ]
      }},
      {{
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
          {{
            "@type": "Question",
            "name": "Qual è la pendenza massima di una rampa per disabili secondo la legge (DM 236/89)?",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "In Italia, ai sensi dell'art. 8.1.11 del DM 236/89, la pendenza massima ammessa per rampe pedonali accessibili su sedia a rotelle è dell'8%. La pendenza raccomandata è del 5%, che non richiede pianerottoli intermedi fino a 15 metri. Se la pendenza è tra il 5% e l'8%, è obbligatorio inserire un pianerottolo orizzontale ogni 10 metri lineari."
            }}
          }},
          {{
            "@type": "Question",
            "name": "Qual è la pendenza massima per una rampa di garage o autorimessa?",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "Ai sensi del D.M. 01/02/1986, la pendenza massima consentita per le rampe carrabili rettilinee è del 20%. Per le rampe a curva o elicoidali, la pendenza massima non può superare il 15%."
            }}
          }},
          {{
            "@type": "Question",
            "name": "Come si calcola la pendenza percentuale di una rampa?",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "La formula matematica è: Pendenza % = (Dislivello / Lunghezza orizzontale a terra) × 100. Ad esempio, per superare 40 cm di dislivello con 500 cm di spazio orizzontale: (40 / 500) × 100 = 8%."
            }}
          }}
        ]
      }}
    ]
    </script>
    <link rel="manifest" href="manifest-building.json">
    <link rel="icon" type="image/svg+xml" href="favicon.svg?v=6">
    <link rel="alternate icon" type="image/png" href="favicon.png?v=6">
    <link rel="shortcut icon" href="favicon.svg?v=6">
    <meta name="theme-color" content="#2563eb">
    <meta name="mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
    <meta name="apple-mobile-web-app-title" content="OmniTools">
    <link rel="apple-touch-icon" href="icon-192.png?v=6">

    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <script defer src="/_vercel/insights/script.js"></script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
    <script>
        tailwind.config = {{
            theme: {{
                extend: {{
                    fontFamily: {{
                        sans: ['"Plus Jakarta Sans"', 'system-ui', '-apple-system', 'sans-serif'],
                    }}
                }}
            }}
        }}
    </script>
    <style>
        * {{ -webkit-tap-highlight-color: transparent; }}
        input[type="number"] {{ font-size: 17px !important; }}
        input[type=range] {{
            -webkit-appearance: none;
            height: 7px;
            background: #e2e8f0;
            border-radius: 9999px;
            outline: none;
        }}
        input[type=range]::-webkit-slider-thumb {{
            -webkit-appearance: none;
            height: 26px;
            width: 26px;
            border-radius: 50%;
            background: #2563eb;
            cursor: pointer;
            box-shadow: 0 3px 8px rgba(37,99,235,0.45);
            border: 2px solid #ffffff;
            transition: transform 0.1s ease;
        }}
        input[type=range]::-webkit-slider-thumb:active {{ transform: scale(1.15); }}
        
        @page {{
            size: A4 portrait;
            margin: 8mm 10mm 8mm 10mm;
        }}
        @media print {{
            header, footer, nav,
            .no-print,
            #faqSection, #faqContainer, #normSection, #shareStrip,
            #suggestModal, #installBanner, #iosModal, #suggestBanner,
            #heroContainer, #modeSelectorBar, #controlsColumn,
            button, input[type=range], details, .faq-accordion {{ 
                display: none !important; 
            }}        .print-only {{
            display: none;
        }}
    </style>
</head>
<body class="bg-slate-50 text-slate-800 font-sans antialiased min-h-screen flex flex-col justify-between selection:bg-blue-500 selection:text-white">

    <!-- Top Navigation Header with safe area padding -->
    <header class="bg-white border-b border-slate-200 sticky top-0 z-30 shadow-xs backdrop-blur-md bg-white/95" style="padding-top: max(env(safe-area-inset-top), 8px); padding-bottom: 8px;">
        <div class="max-w-5xl mx-auto px-3 sm:px-4 py-1 flex items-center justify-between gap-2">
            
            <!-- OmniTools Master Brand + Tool Indicator -->
            <div class="flex items-center gap-2 sm:gap-2.5 min-w-0">
                <!-- Calibrated Logo (Version 3.4 Golden Ratio) -->
                <a href="/" class="w-[33px] h-[33px] sm:w-[36px] sm:h-[36px] rounded-xl bg-gradient-to-br from-amber-500 to-amber-700 flex items-center justify-center text-white shadow-md shadow-amber-500/20 shrink-0 p-1 transition hover:opacity-95" title="OmniTools Home">
                    <svg class="w-full h-full" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <circle cx="16" cy="16" r="13.2" stroke="#ffffff" stroke-width="3" />
                        <path d="M 9.5 8.5 V 23.5 H 24.5" stroke="#ffffff" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round" />
                        <line x1="9.5" y1="23.5" x2="22.5" y2="10.5" stroke="#ffffff" stroke-width="2" stroke-dasharray="2.5 2" />
                        <circle cx="9.5" cy="23.5" r="2.2" fill="#fde047" />
                    </svg>
                </a>

                <!-- Brand Name & Module Indicator (Zero Mobile Overlap) -->
                <div class="flex flex-col min-w-0">
                    <div class="flex items-center gap-1.5 leading-none">
                        <span class="font-jakarta font-black text-sm sm:text-base text-slate-900 tracking-tight leading-none">Omni<span class="text-blue-600">Tools</span></span>
                        <span class="text-[8px] sm:text-[9px] font-jakarta font-extrabold uppercase bg-blue-100 text-blue-800 px-1.5 py-0.5 rounded-full border border-blue-200/80 shrink-0">Lab</span>
                        <span class="h-3.5 w-px bg-slate-200 hidden sm:inline-block"></span>
                        <span id="brandTitle" class="font-bold text-xs text-slate-600 hidden sm:inline-block">RampaFacile</span>
                        <span id="brandBadge" class="px-1.5 py-0.5 text-[9px] font-bold bg-blue-50 text-blue-700 rounded-md border border-blue-200 shrink-0 hidden sm:inline-block">DM 236/89</span>
                    </div>
                    <!-- Row 2 on mobile: Tool Name + Standard Badge -->
                    <div class="sm:hidden flex items-center gap-1.5 leading-none mt-1">
                        <span id="brandTitleMobile" class="font-bold text-[11px] text-slate-600">RampaFacile</span>
                        <span id="brandBadgeMobile" class="px-1.5 py-0.2 text-[8px] font-bold bg-blue-50 text-blue-700 rounded border border-blue-200">DM 236/89</span>
                    </div>
                </div>
            </div>
            
            <!-- Quick Actions: Language Selector + App + Print (Clean icon buttons on mobile) -->
            <div class="flex items-center gap-1.5 sm:gap-2 shrink-0">
                <!-- Suite Quick Switcher (Scale, Dorso, DPI) -->
                <a href="/scale" class="no-print inline-flex items-center gap-1 px-2 py-1.5 text-xs font-bold text-slate-600 hover:text-indigo-600 bg-slate-100 hover:bg-indigo-50 rounded-xl border border-slate-200 transition" title="Calcolo Scale & Gradini">
                    <span>🪜</span>
                    <span class="hidden md:inline">Scale</span>
                </a>
                <a href="/dorso" class="no-print inline-flex items-center gap-1 px-2 py-1.5 text-xs font-bold text-slate-600 hover:text-purple-600 bg-slate-100 hover:bg-purple-50 rounded-xl border border-slate-200 transition" title="Dorso & Copertina Libro">
                    <span>🎨</span>
                    <span class="hidden md:inline">Dorso</span>
                </a>
                <a href="/dpi" class="no-print inline-flex items-center gap-1 px-2 py-1.5 text-xs font-bold text-slate-600 hover:text-emerald-600 bg-slate-100 hover:bg-emerald-50 rounded-xl border border-slate-200 transition" title="Calcolo Risoluzione & DPI">
                    <span>🖼️</span>
                    <span class="hidden md:inline">DPI</span>
                </a>

                <!-- Language Selector Dropdown -->
                <div class="relative inline-block text-left">
                    <select id="langSelect" onchange="changeLanguage(this.value)" class="bg-slate-100 hover:bg-slate-200 text-slate-800 text-xs font-bold py-1.5 px-1.5 sm:px-2 rounded-xl border border-slate-200 focus:outline-none cursor-pointer transition">
                        <option value="it">🇮🇹 IT</option>
                        <option value="en">🇬🇧 EN</option>
                        <option value="es">🇪🇸 ES</option>
                        <option value="fr">🇫🇷 FR</option>
                        <option value="de">🇩🇪 DE</option>
                        <option value="pt">🇵🇹 PT</option>
                    </select>
                </div>

                <button onclick="triggerInstall()" id="headerInstallBtn" class="no-print inline-flex items-center justify-center p-1.5 sm:px-2.5 sm:py-1.5 text-xs font-bold text-blue-700 bg-blue-50 hover:bg-blue-100 active:scale-95 rounded-xl border border-blue-200 transition" title="Installa come App">
                    <span>📲</span>
                    <span id="headerInstallText" class="hidden sm:inline">App</span>
                </button>
                <button onclick="window.print()" class="no-print inline-flex items-center justify-center p-1.5 sm:px-2.5 sm:py-1.5 text-xs font-bold text-slate-700 bg-slate-100 hover:bg-slate-200 active:scale-95 rounded-xl transition shadow-2xs" title="Stampa Scheda Tecnica">
                    <svg class="w-4 h-4 text-slate-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 17h2a2 2 0 002-2v-4a2 2 0 00-2-2H5a2 2 0 00-2 2v4a2 2 0 002 2h2m2 4h6a2 2 0 002-2v-4a2 2 0 00-2-2H9a2 2 0 00-2 2v4a2 2 0 002 2zm8-12V5a2 2 0 00-2-2H9a2 2 0 00-2 2v4h10z" />
                    </svg>
                    <span id="printBtnText" class="hidden sm:inline ml-1">Stampa</span>
                </button>
            </div>
        </div>
    </header>

    <!-- Main Content -->
    <main class="max-w-5xl mx-auto px-3 sm:px-6 py-2.5 sm:py-5 flex-1 w-full space-y-3 sm:space-y-5">
        
        <!-- Hero Header -->
        <div id="heroContainer" class="text-center max-w-2xl mx-auto pt-1 sm:pt-2">
            <h1 id="heroTitle" class="text-2xl sm:text-4xl font-extrabold text-slate-900 tracking-tight leading-tight mb-1.5 sm:mb-2">
                Calcolo Pendenza Rampa & Dislivello
            </h1>
            <p id="heroDesc" class="text-slate-600 text-xs sm:text-base leading-relaxed px-2">
                Calcola istantaneamente pendenza percentuale, gradi e spazio necessario a terra con verifica conformità normativa barriere architettoniche.
            </p>
        </div>

        <!-- Mode Selector -->
        <div id="modeSelectorBar" class="no-print bg-slate-200/80 p-1 rounded-2xl flex max-w-sm sm:max-w-md mx-auto shadow-inner text-xs sm:text-sm font-bold">
            <button id="modeDirectBtn" onclick="switchMode('direct')" class="flex-1 py-1.5 sm:py-2 rounded-xl bg-white text-blue-600 shadow-sm transition active:scale-95 text-center">
                📏 Calcola Pendenza
            </button>
            <button id="modeReverseBtn" onclick="switchMode('reverse')" class="flex-1 py-1.5 sm:py-2 rounded-xl text-slate-600 hover:text-slate-900 transition active:scale-95 text-center">
                📐 Calcola Spazio
            </button>
        </div>

        <!-- Calculator Layout -->
        <div class="flex flex-col lg:grid lg:grid-cols-12 gap-3 sm:gap-6 items-start">
            
            <!-- RESULTS & VISUAL COLUMN (IN CIMA SU MOBILE) -->
            <div id="resultsColumn" class="w-full order-1 lg:order-2 lg:col-span-7 space-y-2.5 sm:space-y-4">
                
                <!-- DEDICATED PRINT-ONLY TECHNICAL SPEC HEADER -->
                <div id="printHeader" class="hidden print:block mb-3 pb-2 border-b-2 border-slate-900">
                    <div class="flex items-center justify-between">
                        <div class="flex items-center gap-2.5">
                            <div class="w-10 h-10 rounded-xl bg-gradient-to-br from-amber-500 to-amber-700 flex items-center justify-center text-white shrink-0 p-1 shadow-sm" style="-webkit-print-color-adjust: exact; print-color-adjust: exact;">
                    <svg class="w-full h-full" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <circle cx="16" cy="16" r="13.2" stroke="#ffffff" stroke-width="3" />
                        <path d="M 9.5 8.5 V 23.5 H 24.5" stroke="#ffffff" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round" />
                        <line x1="9.5" y1="23.5" x2="22.5" y2="10.5" stroke="#ffffff" stroke-width="2" stroke-dasharray="2.5 2" />
                        <circle cx="9.5" cy="23.5" r="2.2" fill="#fde047" />
                    </svg>
                </div>
                            <div>
                                <div class="flex items-center gap-1.5 leading-none">
                                    <span class="text-base font-black tracking-tight text-slate-900 font-jakarta">Omni<span class="text-blue-600">Tools</span> Lab</span>
                                    <span class="text-[9px] font-extrabold uppercase bg-slate-100 text-slate-800 px-1.5 py-0.5 rounded border border-slate-300">SCHEDA TECNICA A4</span>
                                </div>
                                <h1 class="text-xs font-bold text-slate-700 mt-1">RampaFacile — Verifica Conformità Pendenza Rampa & Barriere Architettoniche</h1>
                            </div>
                        </div>
                        <div class="text-right text-[10px] text-slate-600 font-mono leading-tight">
                            <div id="printReportDate" class="font-bold text-slate-900">Data: 04/11/2026</div>
                            <div>DM 236/89 • ADA • CTE • DIN</div>
                            <div class="text-blue-600 font-bold">omnitoolslab.com/rampe</div>
                        </div>
                    </div>
                </div>

                <!-- DEDICATED PRINT-ONLY INPUT SUMMARY -->
                <div id="printInputsSummary" class="hidden print:block mb-2 p-2.5 bg-slate-50 border border-slate-300 rounded-xl text-xs">
                    <div class="grid grid-cols-3 gap-2">
                        <div>
                            <span class="text-[9px] text-slate-500 uppercase font-bold block">Dislivello (h):</span>
                            <span id="printHeightVal" class="text-xs font-extrabold text-slate-900">30 cm</span>
                        </div>
                        <div>
                            <span class="text-[9px] text-slate-500 uppercase font-bold block">Spazio a terra (L):</span>
                            <span id="printLengthVal" class="text-xs font-extrabold text-slate-900">500 cm</span>
                        </div>
                        <div>
                            <span class="text-[9px] text-slate-500 uppercase font-bold block">Tipo di Verifica:</span>
                            <span id="printModeVal" class="text-xs font-extrabold text-slate-900">Verifica Pendenza da Quota</span>
                        </div>
                    </div>
                </div>
                
                <!-- Compliance Badge (Semaforo Normativa) -->
                <div id="complianceCard" class="p-3 sm:p-4 rounded-2xl border transition-all duration-300 shadow-xs print-border">
                    <div class="flex items-start gap-2.5 sm:gap-3">
                        <div id="statusIcon" class="w-8 h-8 sm:w-11 sm:h-11 rounded-xl flex items-center justify-center shrink-0 text-base sm:text-xl font-bold">
                            ✓
                        </div>
                        <div class="flex-1 min-w-0">
                            <div class="flex flex-wrap items-center justify-between gap-1">
                                <h3 id="statusTitle" class="font-bold text-sm sm:text-base tracking-tight">Pendenza a Norma</h3>
                                <span id="statusTag" class="text-[9px] sm:text-[10px] px-2 py-0.5 rounded-full font-bold uppercase tracking-wider">Accessibile</span>
                            </div>
                            <p id="statusDesc" class="text-[11px] sm:text-xs mt-0.5 leading-snug">
                                Conforme per disabili e carrozzine secondo le linee guida.
                            </p>
                        </div>
                    </div>
                </div>

                <!-- 3 Numerical Output Cards -->
                <div class="grid grid-cols-3 gap-2 sm:gap-3">
                    <div class="bg-white p-2.5 sm:p-4 rounded-2xl border border-slate-200 shadow-xs text-center print-border">
                        <span id="colSlopeLabel" class="text-[10px] sm:text-xs font-bold text-slate-700 uppercase tracking-wider block mb-0.5">Pendenza</span>
                        <div id="slopePercent" class="text-xl sm:text-3xl font-extrabold text-blue-600 tracking-tight">6.0%</div>
                        <span id="slopeRatio" class="text-[10px] sm:text-xs font-semibold text-slate-700 block mt-0.5">1 : 16.7</span>
                    </div>

                    <div class="bg-white p-2.5 sm:p-4 rounded-2xl border border-slate-200 shadow-xs text-center print-border">
                        <span id="colAngleLabel" class="text-[10px] sm:text-xs font-bold text-slate-700 uppercase tracking-wider block mb-0.5">Angolo</span>
                        <div id="slopeDegrees" class="text-xl sm:text-3xl font-extrabold text-slate-800 tracking-tight">3.4°</div>
                        <span id="colAngleSubLabel" class="text-[10px] sm:text-xs font-semibold text-slate-700 block mt-0.5">Inclinazione</span>
                    </div>

                    <div class="bg-white p-2.5 sm:p-4 rounded-2xl border border-slate-200 shadow-xs text-center print-border">
                        <span id="lengthLabel" class="text-[10px] sm:text-xs font-bold text-slate-700 uppercase tracking-wider block mb-0.5">Lunghezza</span>
                        <div id="rampLength" class="text-xl sm:text-3xl font-extrabold text-slate-800 tracking-tight">500.9 cm</div>
                        <span id="lengthSubLabel" class="text-[10px] sm:text-xs font-semibold text-slate-700 block mt-0.5">Piano inclinato</span>
                    </div>
                </div>

                <!-- DYNAMIC SVG DIAGRAM -->
                <div class="bg-white p-3 sm:p-4 rounded-2xl border border-slate-200 shadow-xs print-border">
                    <div class="flex items-center justify-between mb-2">
                        <span id="schemaTitle" class="text-[11px] font-bold text-slate-700 uppercase tracking-wider">Schema Visivo Dinamico</span>
                        <span id="schemaScaleText" class="text-[10px] text-blue-600 font-bold flex items-center gap-1">
                            <span class="w-1.5 h-1.5 rounded-full bg-blue-500 animate-pulse"></span> In scala
                        </span>
                    </div>

                    <div class="bg-slate-50/80 rounded-xl p-2 sm:p-4 border border-slate-100 flex items-center justify-center overflow-hidden">
                        <svg id="rampSvg" class="w-full h-36 sm:h-48 transition-all duration-200" viewBox="0 0 520 220">
                            <defs>
                                <linearGradient id="rampGrad" x1="0%" y1="0%" x2="100%" y2="0%">
                                    <stop offset="0%" stop-color="#93c5fd" stop-opacity="0.3" />
                                    <stop offset="100%" stop-color="#3b82f6" stop-opacity="0.65" />
                                </linearGradient>
                                <filter id="textGlow" x="-20%" y="-20%" width="140%" height="140%">
                                    <feFlood flood-color="#ffffff" result="glowColor"/>
                                    <feMorphology in="SourceAlpha" operator="dilate" radius="2" result="dilated"/>
                                    <feComposite in="glowColor" in2="dilated" operator="in" result="glow"/>
                                    <feMerge>
                                        <feMergeNode in="glow"/>
                                        <feMergeNode in="SourceGraphic"/>
                                    </feMerge>
                                </filter>
                            </defs>
                            
                            <!-- Ground Base Line -->
                            <line x1="30" y1="165" x2="490" y2="165" stroke="#94a3b8" stroke-width="2" stroke-dasharray="4 4" />
                            
                            <!-- The Ramp Triangle -->
                            <polygon id="rampPolygon" points="40,165 430,165 430,65" fill="url(#rampGrad)" stroke="#2563eb" stroke-width="3.5" stroke-linejoin="round" />
                            
                            <!-- Height Dimension Line & Bold Label -->
                            <line id="heightDim" x1="445" y1="165" x2="445" y2="65" stroke="#dc2626" stroke-width="2.5" />
                            <text id="heightText" x="452" y="115" fill="#dc2626" font-size="14" font-weight="800" font-family="system-ui, sans-serif">h: 30 cm</text>
                            
                            <!-- Length Dimension Line & Bold Label -->
                            <line id="lengthDim" x1="40" y1="185" x2="430" y2="185" stroke="#334155" stroke-width="2.5" />
                            <text id="lengthText" x="200" y="202" fill="#334155" font-size="14" font-weight="800" font-family="system-ui, sans-serif">L: 500 cm</text>
                            
                            <!-- Hypotenuse / Ramp Length Tag -->
                            <text id="hypotenuseText" x="190" y="105" fill="#1e3a8a" font-size="15" font-weight="900" filter="url(#textGlow)" font-family="system-ui, sans-serif" transform="rotate(-14 235 115)">Rampa: 500.9 cm (6%)</text>
                        </svg>
                    </div>

                    <!-- Rule tip banner -->
                    <div class="mt-2 flex items-center text-[11px] sm:text-xs text-slate-700 bg-slate-50 p-2 sm:p-2.5 rounded-lg border border-slate-100">
                        <span id="ruleTip">💡 <strong>Regola del cantiere:</strong> ogni 10 cm di gradino richiedono almeno 125 cm a terra per non superare l'8%.</span>
                    </div>
                </div>

                <!-- DEDICATED PRINT-ONLY TECHNICAL NOTES & SIGNATURE BOX -->
                <div id="printFooterBox" class="hidden print:block mt-4 pt-3 border-t border-slate-300 text-xs">
                    <div class="grid grid-cols-2 gap-4">
                        <div>
                            <span class="font-bold text-slate-800 block mb-1 text-[10px] uppercase tracking-wider">Note di Cantiere / Prescrizioni:</span>
                            <div class="border border-dashed border-slate-400 h-16 rounded-lg p-2 text-[9px] text-slate-600 leading-tight">
                                • Verificare la presenza di pianerottolo orizzontale (min. 150×150 cm) ogni 10m.<br>
                                • Prevedere cordolo di protezione laterale h ≥ 10 cm e superficie antisdrucciolo.
                            </div>
                        </div>
                        <div>
                            <span class="font-bold text-slate-800 block mb-1 text-[10px] uppercase tracking-wider">Timbro e Firma del Progettista / Tecnico:</span>
                            <div class="border border-slate-300 h-16 rounded-lg flex items-end justify-center pb-1 text-[9px] text-slate-400">
                                Data e Firma Professionale
                            </div>
                        </div>
                    </div>
                    <div class="text-[8px] text-slate-400 text-center mt-3 pt-1.5 border-t border-slate-200">
                        Documento tecnico generato da <strong>OmniTools</strong> (https://www.omnitoolslab.com) — Valori a scopo matematico ed orientativo.
                    </div>
                </div>

            </div>

            <!-- CONTROLS COLUMN (INPUT E SLIDER) -->
            <div id="controlsColumn" class="no-print w-full order-2 lg:order-1 lg:col-span-5 bg-white rounded-2xl p-4 sm:p-5 shadow-sm border border-slate-200 space-y-3 sm:space-y-4">
                
                <!-- Unit Switcher (Metric + Imperial for USA/UK) -->
                <div class="flex items-center justify-between pb-2.5 border-b border-slate-100">
                    <span id="unitLabelText" class="text-[11px] font-bold uppercase tracking-wider text-slate-700">Imposta Misure</span>
                    <div class="inline-flex p-0.5 bg-slate-100 rounded-xl border border-slate-200/80 gap-1 text-xs font-bold">
                        <button type="button" id="unitCm" onclick="setUnit('cm')" class="w-10 sm:w-11 py-1 rounded-lg bg-white text-blue-600 shadow-xs font-extrabold transition active:scale-95 text-center">cm</button>
                        <button type="button" id="unitM" onclick="setUnit('m')" class="w-10 sm:w-11 py-1 rounded-lg text-slate-700 hover:text-slate-900 transition active:scale-95 text-center font-bold">m</button>
                        <button type="button" id="unitIn" onclick="setUnit('in')" class="w-10 sm:w-11 py-1 rounded-lg text-slate-700 hover:text-slate-900 transition active:scale-95 text-center font-bold" title="Inches (pollici)">in</button>
                        <button type="button" id="unitFt" onclick="setUnit('ft')" class="w-10 sm:w-11 py-1 rounded-lg text-slate-700 hover:text-slate-900 transition active:scale-95 text-center font-bold" title="Feet (piedi)">ft</button>
                    </div>
                </div>

                <!-- Input: Dislivello (Altezza) -->
                <div>
                    <div class="flex justify-between items-center mb-1">
                        <label for="heightInput" id="heightLabel" class="text-xs font-bold text-slate-700 flex items-center gap-1.5">
                            <span class="w-2 h-2 rounded-full bg-blue-600 inline-block"></span>
                            Dislivello da superare (h)
                        </label>
                        <span id="heightUnitBadge" class="text-[10px] font-bold px-1.5 py-0.5 bg-slate-100 text-slate-700 rounded">cm</span>
                    </div>
                    <div class="relative">
                        <input type="number" id="heightInput" value="30" min="1" max="1000" step="any"
                            class="w-full px-3 py-2 bg-slate-50 border border-slate-200 rounded-xl font-extrabold text-lg text-slate-900 focus:bg-white focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition">
                    </div>
                    <div class="pt-1.5 px-0.5">
                        <input type="range" id="heightRange" min="5" max="200" value="30" class="w-full">
                    </div>
                </div>

                <!-- FIELD A: Spazio a terra (Attivo in modalità Diretta) -->
                <div id="lengthContainer">
                    <div class="flex justify-between items-center mb-1">
                        <label for="lengthInput" id="lengthLabelInput" class="text-xs font-bold text-slate-700 flex items-center gap-1.5">
                            <span class="w-2 h-2 rounded-full bg-slate-800 inline-block"></span>
                            Spazio a terra disponibile (L)
                        </label>
                        <span id="lengthUnitBadge" class="text-[10px] font-bold px-1.5 py-0.5 bg-slate-100 text-slate-700 rounded">cm</span>
                    </div>
                    <div class="relative">
                        <input type="number" id="lengthInput" value="500" min="1" max="5000" step="any"
                            class="w-full px-3 py-2 bg-slate-50 border border-slate-200 rounded-xl font-extrabold text-lg text-slate-900 focus:bg-white focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition">
                    </div>
                    <div class="pt-1.5 px-0.5">
                        <input type="range" id="lengthRange" min="50" max="1500" value="500" class="w-full">
                    </div>
                </div>

                <!-- FIELD B: Pendenza desiderata (Attivo in modalità Inversa) -->
                <div id="targetSlopeContainer" class="hidden">
                    <div class="flex justify-between items-center mb-1">
                        <label for="targetSlopeInput" id="targetSlopeLabel" class="text-xs font-bold text-slate-700 flex items-center gap-1.5">
                            <span class="w-2 h-2 rounded-full bg-purple-600 inline-block"></span>
                            Pendenza richiesta (%)
                        </label>
                        <span class="text-[10px] font-bold px-1.5 py-0.5 bg-purple-50 text-purple-700 rounded">%</span>
                    </div>
                    <div class="relative">
                        <input type="number" id="targetSlopeInput" value="8" min="1" max="30" step="0.5"
                            class="w-full px-3 py-2 bg-slate-50 border border-slate-200 rounded-xl font-extrabold text-lg text-slate-900 focus:bg-white focus:outline-none focus:ring-2 focus:ring-purple-500 focus:border-transparent transition">
                    </div>
                    
                    <div class="grid grid-cols-3 gap-1.5 mt-2">
                        <button type="button" id="targetBtn5" onclick="setTargetSlope(5)" class="py-1 px-1.5 bg-emerald-50 text-emerald-800 border border-emerald-200 rounded-lg text-[11px] font-bold active:scale-95 transition">5% Ideale</button>
                        <button type="button" id="targetBtn8" onclick="setTargetSlope(8)" class="py-1 px-1.5 bg-amber-50 text-amber-800 border border-amber-200 rounded-lg text-[11px] font-bold active:scale-95 transition">8% Limite DM</button>
                        <button type="button" id="targetBtn20" onclick="setTargetSlope(20)" class="py-1 px-1.5 bg-blue-50 text-blue-800 border border-blue-200 rounded-lg text-[11px] font-bold active:scale-95 transition">20% Garage</button>
                    </div>
                </div>

                <!-- Quick Presets -->
                <div class="pt-2 border-t border-slate-100 no-print">
                    <span id="presetsTitleText" class="text-[10px] font-bold text-slate-700 uppercase tracking-wider block mb-1.5">Preset rapidi:</span>
                    <div class="grid grid-cols-2 gap-1.5 text-xs">
                        <button onclick="applyPreset(15, 250)" class="p-2 border border-slate-200 rounded-xl text-left bg-slate-50/70 hover:bg-blue-50 hover:border-blue-200 active:scale-95 transition">
                            <span id="preset1Title" class="font-bold text-slate-800 block text-[11px]">1 Gradino (15 cm)</span>
                            <span id="preset1Sub" class="text-[10px] text-slate-700">Disabili max 6%</span>
                        </button>
                        <button onclick="applyPreset(45, 600)" class="p-2 border border-slate-200 rounded-xl text-left bg-slate-50/70 hover:bg-blue-50 hover:border-blue-200 active:scale-95 transition">
                            <span id="preset2Title" class="font-bold text-slate-800 block text-[11px]">3 Gradini (45 cm)</span>
                            <span id="preset2Sub" class="text-[10px] text-slate-700">Ingresso a norma</span>
                        </button>
                        <button onclick="applyPreset(120, 1500)" class="p-2 border border-slate-200 rounded-xl text-left bg-slate-50/70 hover:bg-blue-50 hover:border-blue-200 active:scale-95 transition">
                            <span id="preset3Title" class="font-bold text-slate-800 block text-[11px]">Mezzo piano (120 cm)</span>
                            <span id="preset3Sub" class="text-[10px] text-slate-700">Con sosta</span>
                        </button>
                        <button onclick="applyPreset(250, 1500)" class="p-2 border border-slate-200 rounded-xl text-left bg-slate-50/70 hover:bg-blue-50 hover:border-blue-200 active:scale-95 transition">
                            <span id="preset4Title" class="font-bold text-slate-800 block text-[11px]">Garage Auto (250 cm)</span>
                            <span id="preset4Sub" class="text-[10px] text-slate-700">Carrabile 20%</span>
                        </button>
                    </div>
                </div>

            </div>

        </div>

        <!-- Reference Guide & Normative Tables (SEO Pillar) -->
        <section class="no-print bg-white rounded-2xl sm:rounded-3xl p-4 sm:p-6 border border-slate-200 shadow-xs space-y-4">
            <div class="flex items-center gap-2">
                <span class="text-xl">📋</span>
                <h2 class="text-sm sm:text-base font-bold text-slate-900">Tabella Normativa Pendenze Massime Consentite per Legge</h2>
            </div>
            <div class="overflow-x-auto">
                <table class="w-full text-left text-xs border-collapse">
                    <thead>
                        <tr class="border-b border-slate-200 text-slate-700 bg-slate-50/80">
                            <th class="py-2.5 px-3 font-bold">Destinazione d'Uso</th>
                            <th class="py-2.5 px-3 font-bold">Normativa di Riferimento</th>
                            <th class="py-2.5 px-3 font-bold">Pendenza Consigliata</th>
                            <th class="py-2.5 px-3 font-bold">Pendenza Massima</th>
                            <th class="py-2.5 px-3 font-bold">Obbligo Pianerottolo</th>
                        </tr>
                    </thead>
                    <tbody class="divide-y divide-slate-100 text-slate-700">
                        <tr class="hover:bg-slate-50/50">
                            <td class="py-2.5 px-3 font-bold text-slate-900">Rampa Disabili (Accessibilità)</td>
                            <td class="py-2.5 px-3 font-mono text-[11px] text-blue-600">D.M. 236/89 art. 8.1.11</td>
                            <td class="py-2.5 px-3 text-emerald-700 font-bold">4.0% – 5.0%</td>
                            <td class="py-2.5 px-3 font-bold text-amber-700">8.0% (max 10 m)</td>
                            <td class="py-2.5 px-3">Ogni 10 m lineari (min 150×150 cm)</td>
                        </tr>
                        <tr class="hover:bg-slate-50/50">
                            <td class="py-2.5 px-3 font-bold text-slate-900">Adeguamento Edifici Esistenti</td>
                            <td class="py-2.5 px-3 font-mono text-[11px] text-blue-600">D.M. 236/89 art. 8.1.11</td>
                            <td class="py-2.5 px-3 text-slate-600">≤ 8.0%</td>
                            <td class="py-2.5 px-3 font-bold text-rose-700">12.0% (tratti ≤ 3 m)</td>
                            <td class="py-2.5 px-3">All'inizio e al termine del tratto</td>
                        </tr>
                        <tr class="hover:bg-slate-50/50">
                            <td class="py-2.5 px-3 font-bold text-slate-900">Garage e Autorimesse Rettilinee</td>
                            <td class="py-2.5 px-3 font-mono text-[11px] text-blue-600">D.M. 01/02/1986 art. 3.7.2</td>
                            <td class="py-2.5 px-3 text-emerald-700 font-bold">12.0% – 16.0%</td>
                            <td class="py-2.5 px-3 font-bold text-rose-700">20.0%</td>
                            <td class="py-2.5 px-3">Raccordo a monte e a valle (min 3 m)</td>
                        </tr>
                        <tr class="hover:bg-slate-50/50">
                            <td class="py-2.5 px-3 font-bold text-slate-900">Garage e Autorimesse Curvilinee</td>
                            <td class="py-2.5 px-3 font-mono text-[11px] text-blue-600">D.M. 01/02/1986 art. 3.7.2</td>
                            <td class="py-2.5 px-3 text-emerald-700 font-bold">10.0% – 12.0%</td>
                            <td class="py-2.5 px-3 font-bold text-amber-700">15.0% (su mezzadria)</td>
                            <td class="py-2.5 px-3">Raggio min. curvatura 7.00 m</td>
                        </tr>
                        <tr class="hover:bg-slate-50/50">
                            <td class="py-2.5 px-3 font-bold text-slate-900">Standard USA / Internazionale ADA</td>
                            <td class="py-2.5 px-3 font-mono text-[11px] text-slate-500">ADA Standards Sec. 405</td>
                            <td class="py-2.5 px-3 text-emerald-700 font-bold">1:16 (6.25%)</td>
                            <td class="py-2.5 px-3 font-bold text-amber-700">1:12 (8.33%)</td>
                            <td class="py-2.5 px-3">Ogni 9 metri lineari (30 ft)</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </section>

        <!-- FAQ Section -->
        <section id="faqSection" class="no-print bg-white rounded-2xl border border-slate-200 p-4 sm:p-7 shadow-xs">
            <h2 id="faqTitle" class="text-lg sm:text-xl font-bold text-slate-900 mb-3 tracking-tight flex items-center gap-2">
                <span>Domande Frequenti sulle Rampe</span>
                <span class="text-[10px] px-2 py-0.5 bg-slate-100 text-slate-600 rounded-full font-bold">FAQ</span>
            </h2>
            
            <div id="faqContainer" class="divide-y divide-slate-100 text-xs sm:text-sm">
                <!-- Localized FAQs -->
            </div>
        </section>

    </main>

    <!-- Footer with OmniTools Suite & Ironclad Legal Disclaimer -->
    <footer class="no-print bg-white border-t border-slate-200 pt-8 pb-10 mt-8 text-xs text-slate-500">
        <div class="max-w-4xl mx-auto px-4 space-y-6">
            
            <!-- Share & Viral Action Strip -->
            <div class="bg-white p-3.5 sm:p-4 rounded-2xl border border-slate-200/90 shadow-xs flex flex-col sm:flex-row items-center justify-between gap-3 text-center sm:text-left">
                <div class="flex items-center gap-2.5">
                    <span class="text-xl">📢</span>
                    <div>
                        <span id="shareTitleText" class="text-xs sm:text-sm font-bold text-slate-800 block">Ti è stato utile questo calcolatore?</span>
                        <span id="shareSubText" class="text-[11px] text-slate-500 block">Condividilo con colleghi, collaboratori o sui canali di settore</span>
                    </div>
                </div>
                <div class="flex items-center gap-1.5 flex-wrap justify-center shrink-0">
                    <button type="button" onclick="shareWhatsApp()" class="inline-flex items-center gap-1.5 px-3 py-1.5 bg-emerald-600 hover:bg-emerald-500 active:scale-95 text-white text-xs font-bold rounded-xl transition shadow-xs" title="Condividi su WhatsApp">
                        <span>💬</span> <span>WhatsApp</span>
                    </button>
                    <button type="button" onclick="shareLinkedIn()" class="inline-flex items-center gap-1.5 px-3 py-1.5 bg-[#0a66c2] hover:bg-[#004182] active:scale-95 text-white text-xs font-bold rounded-xl transition shadow-xs" title="Condividi su LinkedIn">
                        <span>💼</span> <span>LinkedIn</span>
                    </button>
                    <button type="button" onclick="copyCurrentUrl()" class="inline-flex items-center gap-1.5 px-3 py-1.5 bg-slate-100 hover:bg-slate-200 active:scale-95 text-slate-700 text-xs font-bold rounded-xl border border-slate-200 transition" title="Copia Link">
                        <span>🔗</span> <span id="shareCopyText">Copia Link</span>
                    </button>
                    <button type="button" onclick="nativeShare()" class="inline-flex sm:hidden items-center gap-1.5 px-3 py-1.5 bg-blue-600 hover:bg-blue-500 active:scale-95 text-white text-xs font-bold rounded-xl transition shadow-xs" title="Altre opzioni di condivisione">
                        <span>📤</span> <span>Condividi</span>
                    </button>
                </div>
            </div>

            <!-- Suggestion Prompt Strip (Zero Distraction / High Utility) -->
            <div class="bg-gradient-to-r from-blue-50 to-indigo-50/70 border border-blue-200/80 rounded-2xl p-3.5 sm:p-4 flex flex-col sm:flex-row items-center justify-between gap-3 text-center sm:text-left transition shadow-xs">
                <div class="flex items-center gap-2.5">
                    <span class="text-xl">💡</span>
                    <span id="suggestBannerText" class="text-xs sm:text-sm font-bold text-slate-800">
                        Hai un'idea per un nuovo calcolatore o un miglioramento?
                    </span>
                </div>
                <button type="button" onclick="openSuggestModal()" class="px-3.5 py-1.5 bg-blue-600 hover:bg-blue-700 active:scale-95 text-white font-bold text-xs rounded-xl shadow-xs transition shrink-0 inline-flex items-center gap-1">
                    <span id="suggestBtnText">Suggerisci</span>
                    <span>→</span>
                </button>
            </div>

            <!-- OmniTools Network Ecosystem Bar -->
            <div class="bg-slate-900 text-white rounded-2xl p-4 sm:p-5 shadow-lg border border-slate-800">
                <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 pb-3 border-b border-slate-800">
                    <div class="flex items-center gap-2">
                        <div class="w-6 h-6 rounded-lg bg-blue-600 flex items-center justify-center text-white text-xs font-bold">
                            ⌘
                        </div>
                        <span class="font-black text-sm tracking-tight">OMNITOOLS <span class="text-blue-400">NETWORK</span></span>
                    </div>
                    <span class="text-[11px] text-slate-400 font-medium">Suite di Calcolatori & Utility di Cantiere ad Alta Precisione</span>
                </div>
                
                <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-6 gap-2 pt-3 text-[11px]">
<div class="p-2 rounded-xl bg-slate-800/80 border border-blue-500/30 flex items-center justify-between">
                        <span class="font-bold text-white">📐 Rampe & Pendenze</span>
                        <span class="text-[9px] px-1.5 py-0.2 bg-emerald-500/20 text-emerald-400 font-bold rounded">Attivo</span>
                    </div>
                    <a href="/scale" class="p-2 rounded-xl bg-slate-800/60 hover:bg-slate-800 border border-indigo-500/30 flex items-center justify-between transition group">
                        <span class="font-bold text-slate-300 group-hover:text-white">🪜 Scale & Blondel</span>
                        <span class="text-[9px] px-1.5 py-0.2 bg-emerald-500/20 text-emerald-400 font-bold rounded">Attivo</span>
                    </a>
                    <a href="/dorso" class="p-2 rounded-xl bg-slate-800/60 hover:bg-slate-800 border border-purple-500/30 flex items-center justify-between transition group">
                        <span class="font-bold text-slate-300 group-hover:text-white">🎨 Dorso Libro</span>
                        <span class="text-[9px] px-1.5 py-0.2 bg-purple-500/20 text-purple-300 font-bold rounded">Attivo</span>
                    </a>
                    <a href="/dpi" class="p-2 rounded-xl bg-slate-800/60 hover:bg-slate-800 border border-emerald-500/30 flex items-center justify-between transition group">
                        <span class="font-bold text-slate-300 group-hover:text-white">🖼️ Risoluzione & DPI</span>
                        <span class="text-[9px] px-1.5 py-0.2 bg-emerald-500/20 text-emerald-400 font-bold rounded">Attivo</span>
                    </a>
                    <a href="/tubi" class="p-2 rounded-xl bg-slate-800/60 hover:bg-slate-800 border border-slate-700/60 flex items-center justify-between transition group">
                        <span class="font-bold text-slate-300 group-hover:text-white">🚰 ScaricoFacile</span>
                        <span class="text-[9px] px-1.5 py-0.2 bg-cyan-500/20 text-cyan-400 font-bold rounded">Attivo</span>
                    </a>
                    <a href="/tinta" class="p-2 rounded-xl bg-slate-800/60 hover:bg-slate-800 border border-rose-500/30 flex items-center justify-between transition group">
                        <span class="font-bold text-slate-300 group-hover:text-white">🎯 Tinta & CMYK</span>
                        <span class="text-[9px] px-1.5 py-0.2 bg-rose-500/20 text-rose-300 font-bold rounded">Attivo</span>
                    </a>
                </div>
                <div class="pt-2.5 text-center">
                    <a href="/partnership" class="inline-flex items-center gap-1.5 text-xs font-bold text-indigo-400 hover:text-indigo-300 transition">
                        <span>🤝</span> <span>Diventa Partner Ufficiale o Sponsor della Suite OmniTools</span>
                    </a>
                </div>
            </div>

            <!-- Disclaimer and Copyright -->
            <div class="text-center space-y-2">
                <p class="font-bold text-slate-700">© 2026 OmniTools Network — Tutti i diritti riservati.</p>
                <p id="legalDisclaimerText" class="text-[10px] text-slate-500 leading-relaxed text-justify sm:text-center">
                    <strong>Disclaimer di Manleva e Limitazione di Responsabilità:</strong> I calcoli, i grafici e i riferimenti normativi (DM 236/89, D.M. 01/02/1986, ADA, CTE, PMR, DIN 18040, NBR 9050) forniti da questo strumento online hanno finalità puramente didattica, matematica ed orientativa. Non costituiscono progetto esecutivo, perizia tecnica, asseverazione o consulenza professionale ai sensi di legge (D.P.R. 380/2001 e standard esteri). Lo sviluppatore e il gestore della piattaforma declinano espressamente ogni responsabilità per errori, inesattezze o per qualunque danno diretto o indiretto derivante dall'esecuzione materiale di opere senza la direzione e firma di un tecnico abilitato.
                </p>
            </div>
        </div>
    </footer>

    <!-- Smart Floating PWA Install Banner -->
    <div id="installBanner" class="no-print fixed bottom-3 left-3 right-3 sm:left-auto sm:right-6 sm:bottom-6 sm:max-w-sm bg-slate-900 text-white p-3.5 rounded-2xl shadow-2xl border border-slate-700/60 z-50 flex items-center justify-between gap-3 transition-all duration-300 transform translate-y-0">
        <div class="flex items-center gap-2.5 min-w-0">
            <div class="w-9 h-9 rounded-xl bg-blue-600 flex items-center justify-center text-white shrink-0 font-bold shadow-md">
                📱
            </div>
            <div class="min-w-0">
                <span id="installBannerTitle" class="text-xs font-bold block text-white truncate">Installa OmniTools come App</span>
                <span id="installBannerSub" class="text-[10px] text-slate-300 block truncate">Sempre pronta in cantiere anche offline</span>
            </div>
        </div>
        <div class="flex items-center gap-1.5 shrink-0">
            <button id="installBannerBtn" onclick="triggerInstall()" class="px-3 py-1.5 bg-blue-600 hover:bg-blue-500 text-white rounded-xl text-xs font-bold transition active:scale-95 shadow-sm">
                Installa
            </button>
            <button onclick="dismissInstallBanner()" class="p-1 text-slate-400 hover:text-white rounded-lg text-xs" title="Chiudi">
                ✕
            </button>
        </div>
    </div>

    <!-- iOS Install Helper Modal -->
    <div id="iosModal" class="hidden no-print fixed inset-0 bg-black/60 z-50 flex items-end sm:items-center justify-center p-3 backdrop-blur-xs">
        <div class="bg-white rounded-2xl p-5 max-w-sm w-full text-slate-800 shadow-2xl space-y-3">
            <div class="flex justify-between items-center">
                <h4 class="font-extrabold text-base text-slate-900">Come installare su iPhone:</h4>
                <button onclick="closeIosModal()" class="text-slate-400 hover:text-slate-700 text-lg font-bold">✕</button>
            </div>
            <ol class="text-xs space-y-2 text-slate-600 list-decimal list-inside leading-relaxed">
                <li>Tocca l'icona di <strong>Condivisione</strong> in basso su Safari (il quadrato con la freccia ⎋).</li>
                <li>Scorri il menu e tocca <strong>"Aggiungi alla schermata Home"</strong> ➕.</li>
                <li>Conferma premendo <strong>"Aggiungi"</strong> in alto a destra.</li>
            </ol>
            <button onclick="closeIosModal()" class="w-full py-2 bg-blue-600 text-white rounded-xl text-xs font-bold">Ho capito</button>
        </div>
    </div>

    <!-- Suggestion Modal Pop-up -->
    <div id="suggestModal" class="hidden no-print fixed inset-0 bg-slate-900/60 z-50 flex items-center justify-center p-3 sm:p-4 backdrop-blur-xs">
        <div class="bg-white rounded-3xl p-5 sm:p-6 max-w-md w-full text-slate-800 shadow-2xl border border-slate-100 space-y-3.5 animate-in fade-in zoom-in-95 duration-150">
            <div class="flex justify-between items-start">
                <div class="flex items-center gap-2.5">
                    <div class="w-9 h-9 rounded-xl bg-blue-50 text-blue-600 border border-blue-100 flex items-center justify-center text-lg font-bold">
                        💡
                    </div>
                    <div>
                        <h4 id="modalSuggestTitle" class="font-extrabold text-base text-slate-900 leading-tight">Suggerisci uno Strumento</h4>
                        <span class="text-[10px] text-slate-700 font-medium">OmniTools User Feedback</span>
                    </div>
                </div>
                <button onclick="closeSuggestModal()" class="text-slate-400 hover:text-slate-700 text-xl font-bold p-1 rounded-lg transition">✕</button>
            </div>
            
            <p id="modalSuggestDesc" class="text-xs text-slate-700 leading-relaxed">
                Quale nuovo calcolatore, formula o funzione vorresti vedere su OmniTools?
            </p>

            <div id="suggestFormContainer" class="space-y-3">
                <textarea id="suggestMessage" rows="3" class="w-full p-3 bg-slate-50 border border-slate-200 rounded-xl text-xs sm:text-sm text-slate-900 focus:bg-white focus:outline-none focus:ring-2 focus:ring-blue-500 transition resize-none" placeholder="Scrivi qui la tua idea..."></textarea>
                
                <div class="flex items-center justify-between text-[10px] text-slate-700">
                    <span id="modalPrivacyNote">🔒 Invio 100% anonimo. Non serve registrarsi.</span>
                </div>

                <div class="flex gap-2 pt-1">
                    <button type="button" onclick="closeSuggestModal()" id="modalCloseBtn" class="flex-1 py-2 rounded-xl border border-slate-200 text-xs font-bold text-slate-700 hover:bg-slate-50 transition active:scale-95">
                        Annulla
                    </button>
                    <button type="button" onclick="submitSuggestion()" id="modalSubmitBtn" class="flex-1 py-2 rounded-xl bg-blue-600 hover:bg-blue-700 text-white text-xs font-bold shadow-md shadow-blue-500/20 active:scale-95 transition">
                        Invia
                    </button>
                </div>
            </div>

            <!-- Success State -->
            <div id="suggestSuccessContainer" class="hidden text-center py-4 space-y-3">
                <div class="w-12 h-12 mx-auto rounded-2xl bg-emerald-100 text-emerald-600 flex items-center justify-center text-2xl font-bold">
                    ✓
                </div>
                <p id="modalSuccessText" class="text-xs sm:text-sm font-bold text-slate-800 leading-relaxed px-2">
                    Grazie mille! La tua idea è stata registrata e guiderà i prossimi strumenti di OmniTools.
                </p>
                <button type="button" onclick="closeSuggestModal()" class="px-5 py-2 rounded-xl bg-slate-900 text-white text-xs font-bold hover:bg-slate-800 transition">
                    Fatto
                </button>
            </div>
        </div>
    </div>

    <!-- Script & Multi-Language Logic -->
    <script>
        const TRANSLATIONS = {t_json_str};

        function detectInitialLanguage() {{
            const stored = localStorage.getItem('omnitools_lang');
            if (stored && TRANSLATIONS[stored]) return stored;
            const candidates = navigator.languages || [navigator.language || navigator.userLanguage || ''];
            for (let l of candidates) {{
                if (!l) continue;
                const code = l.toLowerCase().split('-')[0].split('_')[0];
                if (TRANSLATIONS[code]) return code;
            }}
            return 'en';
        }}

        let currentLang = detectInitialLanguage();
        let currentUnit = 'cm';
        let currentMode = 'direct';

        const heightInput = document.getElementById('heightInput');
        const heightRange = document.getElementById('heightRange');
        const lengthInput = document.getElementById('lengthInput');
        const lengthRange = document.getElementById('lengthRange');
        const targetSlopeInput = document.getElementById('targetSlopeInput');

        const lengthContainer = document.getElementById('lengthContainer');
        const targetSlopeContainer = document.getElementById('targetSlopeContainer');
        const modeDirectBtn = document.getElementById('modeDirectBtn');
        const modeReverseBtn = document.getElementById('modeReverseBtn');

        const slopePercentElem = document.getElementById('slopePercent');
        const slopeRatioElem = document.getElementById('slopeRatio');
        const slopeDegreesElem = document.getElementById('slopeDegrees');
        const rampLengthElem = document.getElementById('rampLength');
        const lengthLabel = document.getElementById('lengthLabel');
        const lengthSubLabel = document.getElementById('lengthSubLabel');

        const complianceCard = document.getElementById('complianceCard');
        const statusIcon = document.getElementById('statusIcon');
        const statusTitle = document.getElementById('statusTitle');
        const statusTag = document.getElementById('statusTag');
        const statusDesc = document.getElementById('statusDesc');

        const rampPolygon = document.getElementById('rampPolygon');
        const heightDim = document.getElementById('heightDim');
        const heightText = document.getElementById('heightText');
        const lengthText = document.getElementById('lengthText');
        const hypotenuseText = document.getElementById('hypotenuseText');
        const ruleTip = document.getElementById('ruleTip');

        function changeLanguage(lang) {{
            if (!TRANSLATIONS[lang]) return;
            currentLang = lang;
            localStorage.setItem('omnitools_lang', lang);
            document.getElementById('langSelect').value = lang;
            document.documentElement.lang = lang;
            applyTranslations();
            updateCalculations();
        }}

        function applyTranslations() {{
            const t = TRANSLATIONS[currentLang];
            document.getElementById('brandTitle').textContent = t.title;
            const btm = document.getElementById('brandTitleMobile');
            if (btm) btm.textContent = t.title;
            document.getElementById('brandBadge').textContent = t.badge;
            const bbm = document.getElementById('brandBadgeMobile');
            if (bbm) bbm.textContent = t.badge;
            document.getElementById('heroTitle').textContent = t.hero_title;
            document.getElementById('heroDesc').textContent = t.hero_desc;
            document.getElementById('modeDirectBtn').textContent = t.mode_direct;
            document.getElementById('modeReverseBtn').textContent = t.mode_reverse;
            document.getElementById('unitLabelText').textContent = t.unit_label;
            document.getElementById('heightLabel').innerHTML = `<span class="w-2 h-2 rounded-full bg-blue-600 inline-block"></span> ${{t.height_label}}`;
            document.getElementById('lengthLabelInput').innerHTML = `<span class="w-2 h-2 rounded-full bg-slate-800 inline-block"></span> ${{t.length_label}}`;
            document.getElementById('targetSlopeLabel').innerHTML = `<span class="w-2 h-2 rounded-full bg-purple-600 inline-block"></span> ${{t.target_slope_label}}`;
            document.getElementById('targetBtn5').textContent = t.target_5;
            document.getElementById('targetBtn8').textContent = t.target_8;
            document.getElementById('targetBtn20').textContent = t.target_20;
            document.getElementById('presetsTitleText').textContent = t.presets_title;
            document.getElementById('preset1Title').textContent = t.preset_1;
            document.getElementById('preset1Sub').textContent = t.preset_1_sub;
            document.getElementById('preset2Title').textContent = t.preset_2;
            document.getElementById('preset2Sub').textContent = t.preset_2_sub;
            document.getElementById('preset3Title').textContent = t.preset_3;
            document.getElementById('preset3Sub').textContent = t.preset_3_sub;
            document.getElementById('preset4Title').textContent = t.preset_4;
            document.getElementById('preset4Sub').textContent = t.preset_4_sub;
            document.getElementById('colSlopeLabel').textContent = t.col_slope;
            document.getElementById('colAngleLabel').textContent = t.col_angle;
            document.getElementById('colAngleSubLabel').textContent = t.col_angle_sub;
            document.getElementById('schemaTitle').textContent = t.schema_title;
            document.getElementById('schemaScaleText').innerHTML = `<span class="w-1.5 h-1.5 rounded-full bg-blue-500 animate-pulse"></span> ${{t.schema_scale}}`;
            document.getElementById('printBtnText').textContent = t.print_btn;
            document.getElementById('installBannerTitle').textContent = t.install_banner_title;
            document.getElementById('installBannerSub').textContent = t.install_banner_sub;
            document.getElementById('installBannerBtn').textContent = t.install_btn;
            document.getElementById('legalDisclaimerText').innerHTML = t.legal_disclaimer;
            document.getElementById('faqTitle').firstElementChild.textContent = t.faq_title;

            // Suggestion text bindings
            if (document.getElementById('suggestBannerText')) {{
                document.getElementById('suggestBannerText').textContent = t.suggest_banner;
                document.getElementById('suggestBtnText').textContent = t.suggest_btn;
                document.getElementById('modalSuggestTitle').textContent = t.suggest_modal_title;
                document.getElementById('modalSuggestDesc').textContent = t.suggest_modal_desc;
                document.getElementById('suggestMessage').placeholder = t.suggest_placeholder;
                document.getElementById('modalPrivacyNote').textContent = t.suggest_privacy_note;
                document.getElementById('modalSubmitBtn').textContent = t.suggest_send;
                document.getElementById('modalCloseBtn').textContent = t.suggest_close;
                document.getElementById('modalSuccessText').textContent = t.suggest_thanks;
            }}

            renderFaqs();
        }}

        function renderFaqs() {{
            const container = document.getElementById('faqContainer');
            const faqs = {{
                'it': [
                    ['Qual è la pendenza massima per legge di una rampa per disabili?', 'In Italia, secondo il DM 236/1989, la pendenza consigliata è fino al 5%. Il limite massimo consentito per brevi tratti è dell\\'8%, con obbligo di pianerottolo ogni 10 metri.'],
                    ['Come calcolo lo spazio a terra conoscendo l\\'altezza del gradino?', 'Usa il Calcolo Spazio di OmniTools: dividi il dislivello per la pendenza desiderata. Esempio per 45 cm all\\'8%: 45 / 0.08 = 562.5 cm (circa 5.6 metri).'],
                    ['Quando è obbligatorio il pianerottolo di sosta?', 'Il pianerottolo orizzontale (minimo 150 × 150 cm) è obbligatorio per legge ogni 10 metri di rampa e davanti a porte o cambi di direzione.']
                ],
                'en': [
                    ['What is the maximum ADA compliant ramp slope?', 'Under the Americans with Disabilities Act (ADA) and UK Part M regulations, the maximum slope for commercial ramps is 1:12 (8.33%). The recommended slope for easier unassisted access is 1:20 (5%).'],
                    ['How much horizontal space do I need for a ramp?', 'For an 8.3% slope (1:12), every 1 inch (or cm) of rise requires 12 inches (or cm) of ramp run. A 40 cm rise requires at least 480 cm of horizontal space.'],
                    ['Are landing platforms required?', 'Yes, level rest landings (at least 150 x 150 cm / 5 x 5 ft) are required at the top and bottom of ramps and every 9 meters (30 feet) of horizontal run.']
                ],
                'es': [
                    ['¿Cuál es la pendiente máxima accesible según el CTE?', 'En España, según el CTE DB-SUA, la pendiente máxima es del 10% para tramos menores de 3m, 8% para tramos de hasta 6m y 6% para el resto. La óptima recomendada es del 5%.'],
                    ['¿Cuánto espacio en suelo se necesita para una rampa?', 'Divida la altura entre la pendiente: para salvar 40 cm al 8%, se requieren 40 / 0.08 = 500 cm (5 metros) de longitud en el suelo.']
                ],
                'fr': [
                    ['Quelle est la pente maximale pour une rampe PMR ?', 'En France, la norme d\\'accessibilité PMR impose une pente de 5% maximum. Des tolérances existent : jusqu\\'à 8% sur 2 mètres et 10% sur 0,5 mètre.'],
                    ['Comment calculer la longueur nécessaire pour une rampe ?', 'Pour une pente de 5%, il faut multiplier la hauteur par 20. Pour franchir 20 cm, il faut donc 20 × 20 = 400 cm (4 mètres) de rampe.']
                ],
                'de': [
                    ['Welche Neigung gilt nach DIN 18040 als barrierefrei?', 'Nach DIN 18040 darf die Neigung einer barrierefreien Rampe maximal 6% betragen. Quergefälle sind unzulässig.'],
                    ['Wann sind Zwischenpodeste vorgeschrieben?', 'Nach jeweils 600 cm Rampenlänge ist ein Zwischenpodest mit einer Mindestlänge von 150 cm erforderlich.']
                ],
                'pt': [
                    ['Qual a inclinação máxima de rampa segundo a NBR 9050?', 'A norma NBR 9050 recomenda inclinações entre 5% e 6,25% para total autonomia. A inclinação máxima admissível para reformas é de 8,33% (1:12).'],
                    ['Como calcular o espaço necessário?', 'Para desnível de 40 cm a 8,33%, divida 40 por 0,0833 = 480 cm (4,8 metros) de comprimento no piso.']
                ]
            }};

            const list = faqs[currentLang] || faqs['it'];
            container.innerHTML = list.map(item => `
                <details class="py-3 group cursor-pointer">
                    <summary class="font-bold text-slate-800 flex justify-between items-center list-none select-none">
                        <span>${{item[0]}}</span>
                        <span class="transition group-open:rotate-180 text-blue-600">▼</span>
                    </summary>
                    <p class="mt-1.5 text-slate-600 leading-relaxed pl-1">${{item[1]}}</p>
                </details>
            `).join('');
        }}

        function switchMode(mode) {{
            currentMode = mode;
            const t = TRANSLATIONS[currentLang];
            if (mode === 'direct') {{
                modeDirectBtn.className = "flex-1 py-1.5 sm:py-2 rounded-xl bg-white text-blue-600 shadow-sm transition active:scale-95 text-center";
                modeReverseBtn.className = "flex-1 py-1.5 sm:py-2 rounded-xl text-slate-600 hover:text-slate-900 transition active:scale-95 text-center";
                lengthContainer.classList.remove('hidden');
                targetSlopeContainer.classList.add('hidden');
                lengthLabel.textContent = t.col_length;
                lengthSubLabel.textContent = t.col_length_sub;
            }} else {{
                modeReverseBtn.className = "flex-1 py-1.5 sm:py-2 rounded-xl bg-white text-purple-600 shadow-sm transition active:scale-95 text-center";
                modeDirectBtn.className = "flex-1 py-1.5 sm:py-2 rounded-xl text-slate-600 hover:text-slate-900 transition active:scale-95 text-center";
                lengthContainer.classList.add('hidden');
                targetSlopeContainer.classList.remove('hidden');
                lengthLabel.textContent = t.col_space_min;
                lengthSubLabel.textContent = t.col_space_min_sub;
            }}
            updateCalculations();
        }}

        function setTargetSlope(val) {{
            targetSlopeInput.value = val;
            updateCalculations();
        }}

        const UNIT_FACTORS_CM = {{
            'cm': 1.0,
            'm': 100.0,
            'in': 2.54,
            'ft': 30.48
        }};

        function setUnit(newUnit) {{
            if (newUnit === currentUnit) return;
            const prevUnit = currentUnit;
            currentUnit = newUnit;

            let h = parseFloat(heightInput.value) || 0;
            let l = parseFloat(lengthInput.value) || 0;

            let h_cm = h * (UNIT_FACTORS_CM[prevUnit] || 1.0);
            let l_cm = l * (UNIT_FACTORS_CM[prevUnit] || 1.0);

            let h_new = h_cm / (UNIT_FACTORS_CM[newUnit] || 1.0);
            let l_new = l_cm / (UNIT_FACTORS_CM[newUnit] || 1.0);

            ['cm', 'm', 'in', 'ft'].forEach(u => {{
                const btn = document.getElementById('unit' + u.charAt(0).toUpperCase() + u.slice(1));
                if (btn) {{
                    if (u === newUnit) {{
                        btn.className = "w-10 sm:w-11 py-1 rounded-lg bg-white text-blue-600 shadow-xs font-extrabold transition active:scale-95 text-center";
                    }} else {{
                        btn.className = "w-10 sm:w-11 py-1 rounded-lg text-slate-700 hover:text-slate-900 transition active:scale-95 text-center font-bold";
                    }}
                }}
            }});

            document.getElementById('heightUnitBadge').textContent = newUnit;
            document.getElementById('lengthUnitBadge').textContent = newUnit;

            if (newUnit === 'cm') {{
                heightInput.value = Math.round(h_new);
                lengthInput.value = Math.round(l_new);
                heightRange.min = 5; heightRange.max = 200; heightRange.step = 1;
                lengthRange.min = 50; lengthRange.max = 1500; lengthRange.step = 5;
            }} else if (newUnit === 'm') {{
                heightInput.value = h_new.toFixed(2);
                lengthInput.value = l_new.toFixed(2);
                heightRange.min = 0.05; heightRange.max = 2.0; heightRange.step = 0.01;
                lengthRange.min = 0.5; lengthRange.max = 15.0; lengthRange.step = 0.05;
            }} else if (newUnit === 'in') {{
                heightInput.value = h_new.toFixed(1);
                lengthInput.value = l_new.toFixed(1);
                heightRange.min = 2; heightRange.max = 80; heightRange.step = 0.5;
                lengthRange.min = 20; lengthRange.max = 600; lengthRange.step = 1;
            }} else if (newUnit === 'ft') {{
                heightInput.value = h_new.toFixed(2);
                lengthInput.value = l_new.toFixed(2);
                heightRange.min = 0.2; heightRange.max = 7.0; heightRange.step = 0.05;
                lengthRange.min = 2.0; lengthRange.max = 50.0; lengthRange.step = 0.2;
            }}

            syncSliderWithInput(heightRange, heightInput);
            syncSliderWithInput(lengthRange, lengthInput);
            updateCalculations();
        }}

        function syncSliderWithInput(slider, input) {{ slider.value = input.value; }}
        function syncInputWithSlider(input, slider) {{ input.value = slider.value; }}

        heightInput.addEventListener('input', () => {{ syncSliderWithInput(heightRange, heightInput); updateCalculations(); }});
        heightRange.addEventListener('input', () => {{ syncInputWithSlider(heightInput, heightRange); updateCalculations(); }});
        lengthInput.addEventListener('input', () => {{ syncSliderWithInput(lengthRange, lengthInput); updateCalculations(); }});
        lengthRange.addEventListener('input', () => {{ syncInputWithSlider(lengthInput, lengthRange); updateCalculations(); }});
        targetSlopeInput.addEventListener('input', updateCalculations);

        function applyPreset(hCm, lCm) {{
            if (currentMode === 'reverse') {{
                switchMode('direct');
            }}
            const factor = UNIT_FACTORS_CM[currentUnit] || 1.0;
            const hVal = hCm / factor;
            const lVal = lCm / factor;

            if (currentUnit === 'cm') {{
                heightInput.value = Math.round(hVal);
                lengthInput.value = Math.round(lVal);
            }} else if (currentUnit === 'in') {{
                heightInput.value = hVal.toFixed(1);
                lengthInput.value = lVal.toFixed(1);
            }} else {{
                heightInput.value = hVal.toFixed(2);
                lengthInput.value = lVal.toFixed(2);
            }}
            syncSliderWithInput(heightRange, heightInput);
            syncSliderWithInput(lengthRange, lengthInput);
            updateCalculations();
        }}

        function updateCalculations() {{
            const t = TRANSLATIONS[currentLang];
            let h = parseFloat(heightInput.value);
            
            if (isNaN(h) || h <= 0) return;

            let l, slope, hypotenuse, angleDeg;

            if (currentMode === 'direct') {{
                l = parseFloat(lengthInput.value);
                if (isNaN(l) || l <= 0) return;

                slope = (h / l) * 100;
                hypotenuse = Math.sqrt((h * h) + (l * l));
                angleDeg = Math.atan(h / l) * (180 / Math.PI);
            }} else {{
                let targetSlope = parseFloat(targetSlopeInput.value);
                if (isNaN(targetSlope) || targetSlope <= 0) return;

                slope = targetSlope;
                l = h / (slope / 100);
                hypotenuse = Math.sqrt((h * h) + (l * l));
                angleDeg = Math.atan(slope / 100) * (180 / Math.PI);
            }}

            slopePercentElem.textContent = slope.toFixed(1) + '%';
            
            if (slope > 0) {{
                const ratio = (100 / slope).toFixed(1);
                slopeRatioElem.textContent = `1 : ${{ratio}}`;
            }} else {{
                slopeRatioElem.textContent = '-';
            }}

            slopeDegreesElem.textContent = angleDeg.toFixed(1) + '°';

            const u = currentUnit;
            const hFmt = (u === 'cm' ? h.toFixed(0) : (u === 'in' ? h.toFixed(1) : h.toFixed(2)));
            const lFmt = (u === 'cm' ? l.toFixed(0) : (u === 'in' ? l.toFixed(1) : l.toFixed(2)));
            const hypFmt = (u === 'cm' || u === 'in' ? hypotenuse.toFixed(1) : hypotenuse.toFixed(2));

            if (currentMode === 'direct') {{
                rampLengthElem.textContent = `${{hypFmt}} ${{u}}`;
                ruleTip.innerHTML = t.rule_tip_direct;
            }} else {{
                rampLengthElem.textContent = `${{lFmt}} ${{u}}`;
                let tip = t.rule_tip_reverse
                    .replace('{{h}}', hFmt)
                    .replace('{{s}}', slope.toFixed(1))
                    .replace('{{l}}', lFmt)
                    .replace('{{hyp}}', hypFmt)
                    .replace(/{{u}}/g, u);
                ruleTip.innerHTML = tip;
            }}

            // Sync Print-only technical report summary
            const printHeightVal = document.getElementById('printHeightVal');
            const printLengthVal = document.getElementById('printLengthVal');
            const printModeVal = document.getElementById('printModeVal');
            if (printHeightVal) printHeightVal.textContent = `${{hFmt}} ${{u}}`;
            if (printLengthVal) printLengthVal.textContent = `${{lFmt}} ${{u}}`;
            if (printModeVal) printModeVal.textContent = (currentMode === 'direct') ? 'Verifica Pendenza da Quota' : `Progetto Sviluppo al ${{slope.toFixed(1)}}%`;

            updateCompliance(slope, t);
            updateSvgDiagram(h, l, slope, hypotenuse, u);
        }}

        function updateCompliance(slope, t) {{
            complianceCard.className = "p-3 sm:p-4 rounded-2xl border transition-all duration-300 shadow-xs print-border ";
            statusTag.className = "text-[9px] sm:text-[10px] px-2 py-0.5 rounded-full font-bold uppercase tracking-wider ";

            // Germany has a rigid 6% max threshold under DIN 18040
            const optThreshold = (currentLang === 'de') ? 5.0 : 5.0;
            const maxDisabilityLimit = (currentLang === 'de') ? 6.0 : (currentLang === 'en' || currentLang === 'pt' ? 8.33 : 8.0);

            if (slope <= optThreshold) {{
                complianceCard.classList.add('bg-emerald-50/90', 'border-emerald-200');
                statusIcon.className = "w-8 h-8 sm:w-11 sm:h-11 rounded-xl flex items-center justify-center shrink-0 text-base sm:text-xl font-bold bg-emerald-600 text-white shadow-md shadow-emerald-600/20";
                statusIcon.textContent = "✓";
                statusTitle.className = "font-bold text-sm sm:text-base tracking-tight text-emerald-950";
                statusTitle.textContent = t.status_opt_title;
                statusTag.classList.add('bg-emerald-100', 'text-emerald-800');
                statusTag.textContent = t.status_opt_tag;
                statusDesc.className = "text-[11px] sm:text-xs mt-0.5 leading-snug text-emerald-800";
                statusDesc.textContent = t.status_opt_desc;
            }} else if (slope <= maxDisabilityLimit) {{
                complianceCard.classList.add('bg-amber-50/90', 'border-amber-200');
                statusIcon.className = "w-8 h-8 sm:w-11 sm:h-11 rounded-xl flex items-center justify-center shrink-0 text-base sm:text-xl font-bold bg-amber-500 text-white shadow-md shadow-amber-500/20";
                statusIcon.textContent = "!";
                statusTitle.className = "font-bold text-sm sm:text-base tracking-tight text-amber-950";
                statusTitle.textContent = t.status_warn_title;
                statusTag.classList.add('bg-amber-100', 'text-amber-800');
                statusTag.textContent = t.status_warn_tag;
                statusDesc.className = "text-[11px] sm:text-xs mt-0.5 leading-snug text-amber-800";
                statusDesc.textContent = t.status_warn_desc;
            }} else if (slope <= 20.0) {{
                complianceCard.classList.add('bg-blue-50/90', 'border-blue-200');
                statusIcon.className = "w-8 h-8 sm:w-11 sm:h-11 rounded-xl flex items-center justify-center shrink-0 text-base sm:text-xl font-bold bg-blue-600 text-white shadow-md shadow-blue-600/20";
                statusIcon.textContent = "🚗";
                statusTitle.className = "font-bold text-sm sm:text-base tracking-tight text-blue-950";
                statusTitle.textContent = t.status_car_title;
                statusTag.classList.add('bg-blue-100', 'text-blue-800');
                statusTag.textContent = t.status_car_tag;
                statusDesc.className = "text-[11px] sm:text-xs mt-0.5 leading-snug text-blue-800";
                statusDesc.textContent = t.status_car_desc;
            }} else {{
                complianceCard.classList.add('bg-rose-50/90', 'border-rose-200');
                statusIcon.className = "w-8 h-8 sm:w-11 sm:h-11 rounded-xl flex items-center justify-center shrink-0 text-base sm:text-xl font-bold bg-rose-600 text-white shadow-md shadow-rose-600/20";
                statusIcon.textContent = "✕";
                statusTitle.className = "font-bold text-sm sm:text-base tracking-tight text-rose-950";
                statusTitle.textContent = t.status_danger_title;
                statusTag.classList.add('bg-rose-100', 'text-rose-800');
                statusTag.textContent = t.status_danger_tag;
                statusDesc.className = "text-[11px] sm:text-xs mt-0.5 leading-snug text-rose-800";
                statusDesc.textContent = t.status_danger_desc;
            }}
        }}

        function updateSvgDiagram(h, l, slope, hypotenuse, u) {{
            const groundY = 165;
            const startX = 50;
            const maxX = 450;
            const availableW = maxX - startX;

            const ratio = h / l;
            const visualHeight = Math.min(Math.max(ratio * availableW * 2.5, 20), 125);
            const endY = groundY - visualHeight;

            rampPolygon.setAttribute('points', `${{startX}},${{groundY}} ${{maxX}},${{groundY}} ${{maxX}},${{endY}}`);
            heightDim.setAttribute('x1', maxX + 15);
            heightDim.setAttribute('x2', maxX + 15);
            heightDim.setAttribute('y1', groundY);
            heightDim.setAttribute('y2', endY);

            const hFmt = (u === 'cm' ? h.toFixed(0) : (u === 'in' ? h.toFixed(1) : h.toFixed(2)));
            const lFmt = (u === 'cm' ? l.toFixed(0) : (u === 'in' ? l.toFixed(1) : l.toFixed(2)));
            const hypFmt = (u === 'cm' || u === 'in' ? hypotenuse.toFixed(1) : hypotenuse.toFixed(2));

            heightText.setAttribute('x', maxX + 22);
            heightText.setAttribute('y', endY + (visualHeight / 2) + 5);
            heightText.textContent = `h: ${{hFmt}} ${{u}}`;

            lengthDim.setAttribute('x1', startX);
            lengthDim.setAttribute('x2', maxX);
            lengthText.setAttribute('x', startX + (availableW / 2) - 40);
            lengthText.textContent = `L: ${{lFmt}} ${{u}}`;

            const hypMidX = startX + (availableW / 2) - 20;
            const hypMidY = groundY - (visualHeight / 2) - 14;
            const angleDeg = Math.atan(visualHeight / availableW) * (180 / Math.PI);
            
            hypotenuseText.setAttribute('x', hypMidX);
            hypotenuseText.setAttribute('y', hypMidY);
            hypotenuseText.setAttribute('transform', `rotate(${{-angleDeg}} ${{hypMidX}} ${{hypMidY}})`);
            hypotenuseText.textContent = `Rampa: ${{hypFmt}} ${{u}} (${{slope.toFixed(1)}}%)`;
        }}

        // PWA Install Prompt Logic
        let deferredPrompt = null;
        window.addEventListener('beforeinstallprompt', (e) => {{
            e.preventDefault();
            deferredPrompt = e;
            if (!localStorage.getItem('omnitools_install_dismissed')) {{
                document.getElementById('installBanner').classList.remove('hidden');
            }}
        }});

        function triggerInstall() {{
            const isIos = /iPad|iPhone|iPod/.test(navigator.userAgent) && !window.MSStream;
            if (isIos) {{
                document.getElementById('iosModal').classList.remove('hidden');
                return;
            }}
            if (deferredPrompt) {{
                deferredPrompt.prompt();
                deferredPrompt.userChoice.then((choiceResult) => {{
                    if (choiceResult.outcome === 'accepted') {{
                        dismissInstallBanner();
                    }}
                    deferredPrompt = null;
                }});
            }} else {{
                alert("Per installare: apri le impostazioni del browser ⋮ e tocca 'Aggiungi a schermata Home'");
            }}
        }}

        function dismissInstallBanner() {{
            document.getElementById('installBanner').classList.add('hidden');
            localStorage.setItem('omnitools_install_dismissed', 'true');
        }}

        function closeIosModal() {{
            document.getElementById('iosModal').classList.add('hidden');
        }}

        // Suggestion Popup Logic
        function openSuggestModal() {{
            document.getElementById('suggestModal').classList.remove('hidden');
            document.getElementById('suggestFormContainer').classList.remove('hidden');
            document.getElementById('suggestSuccessContainer').classList.add('hidden');
            document.getElementById('suggestMessage').value = '';
        }}

        function closeSuggestModal() {{
            document.getElementById('suggestModal').classList.add('hidden');
        }}

        async function submitSuggestion() {{
            const msg = document.getElementById('suggestMessage').value.trim();
            if (!msg) return;
            const btn = document.getElementById('modalSubmitBtn');
            const t = TRANSLATIONS[currentLang];
            btn.textContent = t.suggest_sending || "Invio...";
            btn.disabled = true;

            try {{
                await fetch('/api/suggest', {{
                    method: 'POST',
                    headers: {{ 'Content-Type': 'application/json' }},
                    body: JSON.stringify({{ message: msg, lang: currentLang }})
                }});
            }} catch (e) {{
                console.log("Feedback logged", e);
            }}

            btn.textContent = t.suggest_send || "Invia";
            btn.disabled = false;
            document.getElementById('suggestFormContainer').classList.add('hidden');
            document.getElementById('suggestSuccessContainer').classList.remove('hidden');
        }}

        if (window.matchMedia('(display-mode: standalone)').matches || window.navigator.standalone === true) {{
            const banner = document.getElementById('installBanner');
            if (banner) banner.classList.add('hidden');
            const hBtn = document.getElementById('headerInstallBtn');
            if (hBtn) hBtn.classList.add('hidden');
        }}

        // Initialize Service Worker
        if ('serviceWorker' in navigator) {{
            window.addEventListener('load', () => {{
                navigator.serviceWorker.register('sw.js?v=2').then(reg => {{
                    reg.update();
                }}).catch(() => {{}});
            }});
        }}

        // Social Sharing Functions
        function shareWhatsApp() {{
            const url = encodeURIComponent(window.location.href);
            const text = encodeURIComponent(document.title);
            window.open(`https://api.whatsapp.com/send?text=${{text}}%20${{url}}`, '_blank');
        }}
        function shareLinkedIn() {{
            const url = encodeURIComponent(window.location.href);
            window.open(`https://www.linkedin.com/sharing/share-offsite/?url=${{url}}`, '_blank');
        }}
        function copyCurrentUrl() {{
            navigator.clipboard.writeText(window.location.href).then(() => {{
                const el = document.getElementById('shareCopyText');
                if (el) {{
                    const orig = el.textContent;
                    el.textContent = 'Copiato! ✓';
                    setTimeout(() => {{ el.textContent = orig; }}, 2000);
                }}
            }});
        }}
        function nativeShare() {{
            if (navigator.share) {{
                navigator.share({{
                    title: document.title,
                    url: window.location.href
                }}).catch(() => {{}});
            }} else {{
                copyCurrentUrl();
            }}
        }}

        // Initial setup
        const prd = document.getElementById('printReportDate');
        if (prd) {{
            const now = new Date();
            const dStr = String(now.getDate()).padStart(2, '0') + '/' + String(now.getMonth() + 1).padStart(2, '0') + '/' + now.getFullYear();
            prd.textContent = 'Data: ' + dStr;
        }}
        document.getElementById('langSelect').value = currentLang;
        document.documentElement.lang = currentLang;
        applyTranslations();
        updateCalculations();
    </script>
</body>
</html>
"""

with open('/Users/ilalu/Documents/Altenative Businnes/Calcolatore_Pendenza/rampe.html', 'w', encoding='utf-8') as f:
    f.write(html_code)

print("rampe.html compiled with OmniTools brand and dynamic logo successfully.")
