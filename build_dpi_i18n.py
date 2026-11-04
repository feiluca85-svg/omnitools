import json

with open('/Users/ilalu/Documents/Altenative Businnes/Calcolatore_Pendenza/translations_dpi.json', 'r', encoding='utf-8') as f:
    t_data = json.load(f)

t_json_str = json.dumps(t_data, ensure_ascii=False)

html_code = f"""<!DOCTYPE html>
<html lang="it">
<head>
    <meta name="google-site-verification" content="MRdbDm9lLhokeD3I0FOpUSOhNaF_2WaveKvu52FxtG4">
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0">
    <title>Convertitore Pixel Centimetri e DPI — Calcolo Risoluzione Stampa e Distanza Occhio</title>
    <meta name="description" content="Convertitore online tra Pixel, Centimetri e Risoluzione DPI/PPI per stampa tipografica, offset, digitale e grande formato (poster, manifesti). Include formula acuità visiva dell'occhio umano in base alla distanza di osservazione.">
    
    <!-- Canonical & SEO Meta Tags -->
    <link rel="canonical" href="https://www.omnitoolslab.com/dpi">
    <meta name="robots" content="index, follow">
    <meta property="og:type" content="website">
    <meta property="og:title" content="OmniTools - Calcolo Risoluzione Stampa, Pixel & DPI">
    <meta property="og:description" content="Converti all'istante Pixel, Centimetri e DPI per InDesign, Photoshop e stampa grande formato con calcolo dell'acuità visiva umana.">
    <meta property="og:url" content="https://www.omnitoolslab.com/dpi">
    <meta property="og:site_name" content="OmniTools Lab">
    <meta property="og:image" content="https://www.omnitoolslab.com/og-dpi.png">
    <meta property="og:image:width" content="1200">
    <meta property="og:image:height" content="630">
    <meta property="og:image:type" content="image/png">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:image" content="https://www.omnitoolslab.com/og-dpi.png">

    <!-- Schema.org JSON-LD Structured Data (Rich Snippets) -->
    <script type="application/ld+json">
    [
      {{
        "@context": "https://schema.org",
        "@type": "WebApplication",
        "name": "OmniTools - Calcolo Risoluzione Stampa, Pixel & DPI",
        "url": "https://www.omnitoolslab.com/dpi",
        "applicationCategory": "DesignApplication",
        "operatingSystem": "All",
        "description": "Calcolatore professionale per grafici, fotografi e tipografi per la conversione accurata tra pixel, cm di stampa e risoluzione DPI con distanza di visione.",
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
            "name": "RisoluzioneFacile",
            "item": "https://www.omnitoolslab.com/dpi"
          }}
        ]
      }},
      {{
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
          {{
            "@type": "Question",
            "name": "Qual è la differenza fondamentale tra DPI e PPI?",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "PPI (Pixels Per Inch) indica il numero di pixel digitali per pollice all'interno di un file raster o su uno schermo. DPI (Dots Per Inch) indica invece i punti fisici di inchiostro che la macchina da stampa o il plotter deposita sulla carta. Nel flusso di lavoro di prestampa grafica si usano come sinonimi, ma il calcolo matematico della dimensione del documento si basa rigorosamente sulla formula PPI."
            }}
          }},
          {{
            "@type": "Question",
            "name": "Servono davvero 300 DPI per stampare striscioni o cartelloni 6x3 metri?",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "No, è uno degli errori più diffusi che genera file da molti Gigabyte impossibili da gestire. La risoluzione necessaria dipende esclusivamente dalla distanza dell'osservatore (acuità visiva di 1 arcminuto). A 5 metri di distanza, un cartellone appare nitidissimo a soli 25-35 DPI, perché a quella distanza l'occhio umano non è fisicamente in grado di distinguere i singoli punti di stampa."
            }}
          }},
          {{
            "@type": "Question",
            "name": "Come si calcolano le dimensioni di stampa in cm conoscendo pixel e DPI?",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "La formula esatta è: Centimetri = (Pixel / DPI) × 2.54. Ad esempio, per un file di 3000 pixel di larghezza stampato a 300 DPI: (3000 / 300) × 2.54 = 25.4 cm."
            }}
          }}
        ]
      }}
    ]
    </script>
    <link rel="manifest" href="manifest.json">
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
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@500;700&display=swap" rel="stylesheet">
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
    <style>
        .blueprint-grid {{
            background-color: #0f172a;
            background-image: 
                linear-gradient(rgba(56, 189, 248, 0.08) 1px, transparent 1px),
                linear-gradient(90deg, rgba(56, 189, 248, 0.08) 1px, transparent 1px),
                linear-gradient(rgba(56, 189, 248, 0.03) 1px, transparent 1px),
                linear-gradient(90deg, rgba(56, 189, 248, 0.03) 1px, transparent 1px);
            background-size: 50px 50px, 50px 50px, 10px 10px, 10px 10px;
        }}
        input[type=number]::-webkit-inner-spin-button, 
        input[type=number]::-webkit-outer-spin-button {{ 
            -webkit-appearance: none; 
            margin: 0; 
        }}
        input[type=range] {{
            -webkit-appearance: none;
            width: 100%;
            height: 6px;
            background: #e2e8f0;
            border-radius: 9999px;
            outline: none;
        }}
        input[type=range]::-webkit-slider-thumb {{
            -webkit-appearance: none;
            appearance: none;
            width: 20px;
            height: 20px;
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
            margin: 10mm 12mm;
        }}
        @media print {{
            body {{
                background-color: #ffffff !important;
                color: #000000 !important;
                font-size: 10.5pt;
            }}
            .no-print {{
                display: none !important;
            }}
            .print-only {{
                display: block !important;
            }}
            .print-container {{
                max-width: 100% !important;
                padding: 0 !important;
                margin: 0 !important;
            }}
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
                <a href="/" class="w-[33px] h-[33px] sm:w-[36px] sm:h-[36px] rounded-xl bg-gradient-to-br from-blue-600 to-indigo-700 flex items-center justify-center text-white shadow-md shadow-blue-500/20 shrink-0 p-1 transition hover:opacity-95" title="OmniTools Home">
                    <svg class="w-full h-full" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <circle cx="16" cy="16" r="13.2" stroke="#ffffff" stroke-width="3.4" />
                        <path d="M 7.5 11.5 H 24.5 M 16 11.5 V 24.5" stroke="#ffffff" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round" />
                        <circle cx="16" cy="11.5" r="2.1" fill="#38bdf8" />
                    </svg>
                </a>

                <!-- Brand Name & Module Indicator (Zero Mobile Overlap) -->
                <div class="flex flex-col min-w-0">
                    <div class="flex items-center gap-1.5 leading-none">
                        <span class="font-jakarta font-black text-sm sm:text-base text-slate-900 tracking-tight leading-none">Omni<span class="text-blue-600">Tools</span></span>
                        <span class="text-[8px] sm:text-[9px] font-jakarta font-extrabold uppercase bg-blue-100 text-blue-800 px-1.5 py-0.5 rounded-full border border-blue-200/80 shrink-0">Lab</span>
                        <span class="h-3.5 w-px bg-slate-200 hidden sm:inline-block"></span>
                        <span id="brandTitle" class="font-bold text-xs text-slate-700 hidden sm:inline-block">RisoluzioneFacile</span>
                        <span id="brandBadge" class="px-1.5 py-0.5 text-[9px] font-bold bg-emerald-50 text-emerald-700 rounded-md border border-emerald-200 shrink-0 hidden sm:inline-block">OmniGraph</span>
                    </div>
                    <div class="sm:hidden flex items-center gap-1.5 leading-none mt-1">
                        <span id="brandTitleMobile" class="font-bold text-[11px] text-slate-700">RisoluzioneFacile</span>
                        <span id="brandBadgeMobile" class="px-1.5 py-0.2 text-[8px] font-bold bg-emerald-50 text-emerald-700 rounded border border-emerald-200">Pixel & DPI</span>
                    </div>
                </div>
            </div>
            
            <!-- Quick Actions: Switcher + Language Selector + App + Print -->
            <div class="flex items-center gap-1.5 sm:gap-2 shrink-0">
                <!-- Suite Quick Switcher (Rampe, Scale, Dorso) -->
                <a href="/rampe" class="no-print inline-flex items-center gap-1 px-2 py-1.5 text-xs font-bold text-slate-600 hover:text-blue-600 bg-slate-100 hover:bg-blue-50 rounded-xl border border-slate-200 transition" title="Calcolo Rampe">
                    <span>📐</span>
                    <span class="hidden md:inline">Rampe</span>
                </a>
                <a href="/scale" class="no-print inline-flex items-center gap-1 px-2 py-1.5 text-xs font-bold text-slate-600 hover:text-indigo-600 bg-slate-100 hover:bg-indigo-50 rounded-xl border border-slate-200 transition" title="Calcolo Scale">
                    <span>🪜</span>
                    <span class="hidden md:inline">Scale</span>
                </a>
                <a href="/dorso" class="no-print inline-flex items-center gap-1 px-2 py-1.5 text-xs font-bold text-slate-600 hover:text-purple-600 bg-slate-100 hover:bg-purple-50 rounded-xl border border-slate-200 transition" title="Calcolo Dorso Libro">
                    <span>🎨</span>
                    <span class="hidden md:inline">Dorso</span>
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

    <!-- Main Content Container -->
    <main class="max-w-5xl mx-auto px-3 sm:px-4 py-3 sm:py-5 flex-1 space-y-3 sm:space-y-4 print-container">
        
        <!-- Hero Title Banner (No Print) -->
        <div class="no-print text-center max-w-2xl mx-auto space-y-1">
            <h1 id="heroTitle" class="text-xl sm:text-2xl lg:text-3xl font-black text-slate-900 tracking-tight leading-tight">
                Calcolo Risoluzione Stampa, Pixel & DPI
            </h1>
            <p id="heroDesc" class="text-xs sm:text-sm text-slate-600 leading-snug">
                Converti istantaneamente tra Pixel, Centimetri e DPI per stampa offset, digitale e grande formato, con calcolo della distanza di visione ottimale dell'occhio umano.
            </p>
        </div>

        <!-- Mode Selector -->
        <div id="modeSelectorBar" class="no-print bg-slate-200/80 p-1 rounded-2xl flex max-w-sm sm:max-w-md mx-auto shadow-inner text-xs sm:text-sm font-bold">
            <button id="modeDirectBtn" onclick="switchMode('direct')" class="flex-1 py-1.5 sm:py-2 rounded-xl bg-white text-emerald-700 shadow-sm transition active:scale-95 text-center">
                🖼️ Da Pixel a Formato Stampa
            </button>
            <button id="modeReverseBtn" onclick="switchMode('reverse')" class="flex-1 py-1.5 sm:py-2 rounded-xl text-slate-600 hover:text-slate-900 transition active:scale-95 text-center">
                📐 Da Formato Stampa a Pixel
            </button>
        </div>

        <!-- Calculator Grid Layout -->
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-3 sm:gap-4 items-start">
            
            <!-- Controls Column (Inputs) -->
            <div class="no-print w-full order-2 lg:order-1 lg:col-span-5 bg-white p-3.5 sm:p-4 rounded-2xl sm:rounded-3xl shadow-sm border border-slate-200 space-y-3">
                
                <!-- Unit Switcher -->
                <div class="flex items-center justify-between pb-2 border-b border-slate-100">
                    <span id="unitLabelText" class="text-[11px] font-bold uppercase tracking-wider text-slate-700">Unità Stampa</span>
                    <div class="inline-flex p-0.5 bg-slate-100 rounded-xl border border-slate-200/80 gap-1 text-xs font-bold">
                        <button type="button" id="unitCm" onclick="setUnit('cm')" class="w-10 sm:w-11 py-1 rounded-lg bg-white text-emerald-700 shadow-xs font-extrabold transition active:scale-95 text-center">cm</button>
                        <button type="button" id="unitMm" onclick="setUnit('mm')" class="w-10 sm:w-11 py-1 rounded-lg text-slate-700 hover:text-slate-900 transition active:scale-95 text-center font-bold">mm</button>
                        <button type="button" id="unitIn" onclick="setUnit('in')" class="w-10 sm:w-11 py-1 rounded-lg text-slate-700 hover:text-slate-900 transition active:scale-95 text-center font-bold">in</button>
                    </div>
                </div>

                <!-- Input Set: Direct Mode (Pixel Inputs) -->
                <div id="directInputsGroup" class="space-y-3">
                    <div class="grid grid-cols-2 gap-2">
                        <div class="space-y-1">
                            <label id="pixelsWLabel" class="block text-xs font-bold text-slate-800">Larghezza (px)</label>
                            <input type="number" id="inputPxW" value="2480" min="10" max="100000" step="1" oninput="calculateResolution()" class="w-full bg-slate-50 border border-slate-200 rounded-xl px-3 py-2 text-sm font-mono font-bold text-slate-900 focus:bg-white focus:border-emerald-600 focus:ring-1 focus:ring-emerald-600 outline-none transition">
                        </div>
                        <div class="space-y-1">
                            <label id="pixelsHLabel" class="block text-xs font-bold text-slate-800">Altezza (px)</label>
                            <input type="number" id="inputPxH" value="3508" min="10" max="100000" step="1" oninput="calculateResolution()" class="w-full bg-slate-50 border border-slate-200 rounded-xl px-3 py-2 text-sm font-mono font-bold text-slate-900 focus:bg-white focus:border-emerald-600 focus:ring-1 focus:ring-emerald-600 outline-none transition">
                        </div>
                    </div>
                </div>

                <!-- Input Set: Reverse Mode (Print Size Inputs) -->
                <div id="reverseInputsGroup" class="space-y-3 hidden">
                    <div class="grid grid-cols-2 gap-2">
                        <div class="space-y-1">
                            <label id="printWLabel" class="block text-xs font-bold text-slate-800">Larghezza Stampa (<span class="unitBadge">cm</span>)</label>
                            <input type="number" id="inputPrintW" value="21.0" min="0.1" max="5000" step="0.1" oninput="calculateResolution()" class="w-full bg-slate-50 border border-slate-200 rounded-xl px-3 py-2 text-sm font-mono font-bold text-slate-900 focus:bg-white focus:border-emerald-600 focus:ring-1 focus:ring-emerald-600 outline-none transition">
                        </div>
                        <div class="space-y-1">
                            <label id="printHLabel" class="block text-xs font-bold text-slate-800">Altezza Stampa (<span class="unitBadge">cm</span>)</label>
                            <input type="number" id="inputPrintH" value="29.7" min="0.1" max="5000" step="0.1" oninput="calculateResolution()" class="w-full bg-slate-50 border border-slate-200 rounded-xl px-3 py-2 text-sm font-mono font-bold text-slate-900 focus:bg-white focus:border-emerald-600 focus:ring-1 focus:ring-emerald-600 outline-none transition">
                        </div>
                    </div>
                </div>

                <!-- DPI Setting + Quick DPI buttons -->
                <div class="space-y-1.5 pt-1">
                    <div class="flex items-center justify-between">
                        <label id="dpiTargetLabel" class="block text-xs font-bold text-slate-800">Risoluzione di Stampa (DPI / PPI)</label>
                        <span id="dpiBadge" class="text-xs font-mono font-black text-emerald-700 bg-emerald-50 px-2 py-0.5 rounded-md border border-emerald-200">300 DPI</span>
                    </div>
                    <input type="range" id="dpiRange" min="10" max="600" step="5" value="300" oninput="updateDpiFromRange(this.value)" class="w-full accent-emerald-600">
                    <div class="grid grid-cols-5 gap-1 pt-1">
                        <button type="button" onclick="setDpi(72)" class="py-1 text-[10px] font-bold bg-slate-100 hover:bg-emerald-50 hover:text-emerald-700 rounded-lg border border-slate-200 transition text-center">72 DPI</button>
                        <button type="button" onclick="setDpi(150)" class="py-1 text-[10px] font-bold bg-slate-100 hover:bg-emerald-50 hover:text-emerald-700 rounded-lg border border-slate-200 transition text-center">150 DPI</button>
                        <button type="button" onclick="setDpi(200)" class="py-1 text-[10px] font-bold bg-slate-100 hover:bg-emerald-50 hover:text-emerald-700 rounded-lg border border-slate-200 transition text-center">200 DPI</button>
                        <button type="button" onclick="setDpi(300)" class="py-1 text-[10px] font-extrabold bg-emerald-100 text-emerald-800 rounded-lg border border-emerald-300 transition text-center">300 DPI</button>
                        <button type="button" onclick="setDpi(600)" class="py-1 text-[10px] font-bold bg-slate-100 hover:bg-emerald-50 hover:text-emerald-700 rounded-lg border border-slate-200 transition text-center">600 DPI</button>
                    </div>
                </div>

                <!-- Viewing Distance Slider -->
                <div class="space-y-1.5 pt-2 border-t border-slate-100">
                    <div class="flex items-center justify-between">
                        <label id="viewDistLabel" class="block text-xs font-bold text-slate-800">Distanza di Visione Osservatore</label>
                        <span id="distBadge" class="text-xs font-mono font-bold text-slate-700 bg-slate-100 px-2 py-0.5 rounded-md border border-slate-200">40 cm</span>
                    </div>
                    <input type="range" id="distRange" min="20" max="800" step="10" value="40" oninput="updateDistFromRange(this.value)" class="w-full accent-blue-600">
                    <div class="flex justify-between text-[10px] text-slate-600 font-medium">
                        <span>30 cm (Libro)</span>
                        <span>1 m (Poster)</span>
                        <span>3 m (Stand)</span>
                        <span>6 m (Cartellone)</span>
                    </div>
                </div>

                <!-- Presets Grid -->
                <div class="space-y-1.5 pt-2 border-t border-slate-100">
                    <span id="presetsTitle" class="text-[11px] font-bold uppercase tracking-wider text-slate-700 block">Preset Standard:</span>
                    <div class="grid grid-cols-2 gap-1.5 text-left">
                        <button type="button" onclick="applyPreset(1)" class="p-2 rounded-xl bg-slate-50 hover:bg-emerald-50/70 border border-slate-200/90 hover:border-emerald-300 transition active:scale-95 text-left group">
                            <span id="preset1Title" class="text-[11px] font-bold text-slate-800 group-hover:text-emerald-700 block leading-tight">A4 Offset HD (300 DPI)</span>
                            <span id="preset1Sub" class="text-[9px] text-slate-600 block">21 × 29.7 cm • 2480 × 3508 px</span>
                        </button>
                        <button type="button" onclick="applyPreset(2)" class="p-2 rounded-xl bg-slate-50 hover:bg-emerald-50/70 border border-slate-200/90 hover:border-emerald-300 transition active:scale-95 text-left group">
                            <span id="preset2Title" class="text-[11px] font-bold text-slate-800 group-hover:text-emerald-700 block leading-tight">Manifesto 70×100 cm</span>
                            <span id="preset2Sub" class="text-[9px] text-slate-600 block">Distanza 1.5 m • 150 DPI</span>
                        </button>
                        <button type="button" onclick="applyPreset(3)" class="p-2 rounded-xl bg-slate-50 hover:bg-emerald-50/70 border border-slate-200/90 hover:border-emerald-300 transition active:scale-95 text-left group">
                            <span id="preset3Title" class="text-[11px] font-bold text-slate-800 group-hover:text-emerald-700 block leading-tight">Roll-up 85×200 cm</span>
                            <span id="preset3Sub" class="text-[9px] text-slate-600 block">Distanza 2 m • 100 DPI</span>
                        </button>
                        <button type="button" onclick="applyPreset(4)" class="p-2 rounded-xl bg-slate-50 hover:bg-emerald-50/70 border border-slate-200/90 hover:border-emerald-300 transition active:scale-95 text-left group">
                            <span id="preset4Title" class="text-[11px] font-bold text-slate-800 group-hover:text-emerald-700 block leading-tight">Cartellone 6×3 m</span>
                            <span id="preset4Sub" class="text-[9px] text-slate-600 block">Distanza 5 m • 30 DPI</span>
                        </button>
                    </div>
                </div>

            </div>

            <!-- Results & Technical Blueprint Column -->
            <div id="resultsColumn" class="w-full order-1 lg:order-2 lg:col-span-7 space-y-2.5 sm:space-y-4">
                
                <!-- DEDICATED PRINT-ONLY TECHNICAL SPEC HEADER -->
                <div id="printHeader" class="hidden print:block mb-3 pb-2.5 border-b-2 border-slate-900">
                    <div class="flex items-center justify-between">
                        <div class="flex items-center gap-2.5">
                            <div class="w-9 h-9 rounded-xl bg-emerald-700 text-white flex items-center justify-center font-black text-sm">
                                O/T
                            </div>
                            <div>
                                <h1 class="text-base font-black tracking-tight text-slate-900">OMNITOOLS — SCHEDA TECNICA DI RISOLUZIONE & PRE-STAMPA</h1>
                                <p class="text-[10px] text-slate-600 font-medium">Relazione Tecnica di Conversione Pixel, DPI & Distanza di Visione Ottica</p>
                            </div>
                        </div>
                        <div class="text-right text-[10px] text-slate-600 leading-tight">
                            <div id="printReportDate" class="font-bold text-slate-900">Data: 03/11/2026</div>
                            <div>Formula Acuità Visiva 1 Arcmin • Standard ISO 216</div>
                            <div class="text-[9px] text-slate-500">omnitoolslab.com/dpi</div>
                        </div>
                    </div>
                </div>

                <!-- Primary KPI Metrics Grid -->
                <div class="grid grid-cols-3 gap-2">
                    <div class="bg-white p-2.5 sm:p-3 rounded-2xl border border-slate-200 shadow-xs">
                        <span id="colDimLabel" class="text-[10px] font-bold uppercase tracking-wider text-slate-600 block">Formato Stampa</span>
                        <div id="valPrintDim" class="text-sm sm:text-base lg:text-lg font-black font-mono text-slate-900 leading-tight">21.0 × 29.7 cm</div>
                        <span id="valPrintDimIn" class="text-[10px] text-slate-600 font-mono block">8.27 × 11.69 in</span>
                    </div>
                    <div class="bg-white p-2.5 sm:p-3 rounded-2xl border border-slate-200 shadow-xs">
                        <span id="colPixLabel" class="text-[10px] font-bold uppercase tracking-wider text-slate-600 block">Risoluzione File</span>
                        <div id="valPixelDim" class="text-sm sm:text-base lg:text-lg font-black font-mono text-emerald-700 leading-tight">2480 × 3508 px</div>
                        <span id="valAspectRatio" class="text-[10px] text-slate-600 font-mono block">Ratio: 1:1.41 (A4)</span>
                    </div>
                    <div class="bg-white p-2.5 sm:p-3 rounded-2xl border border-slate-200 shadow-xs">
                        <span id="colMegaLabel" class="text-[10px] font-bold uppercase tracking-wider text-slate-600 block">Megapixel & Peso</span>
                        <div id="valMegapixels" class="text-sm sm:text-base lg:text-lg font-black font-mono text-slate-900 leading-tight">8.70 MP</div>
                        <span id="valFileSize" class="text-[10px] text-slate-600 font-mono block">RGB 24.9 MB • CMYK 33.2 MB</span>
                    </div>
                </div>

                <!-- Human Eye Acuity & Sharpness Verdict Box -->
                <div id="verdictBox" class="p-3 sm:p-4 rounded-2xl border bg-emerald-50/80 border-emerald-200 text-slate-800 transition shadow-xs space-y-1.5">
                    <div class="flex items-center justify-between gap-2">
                        <div class="flex items-center gap-2">
                            <span id="verdictIcon" class="text-lg">👁️</span>
                            <span id="verdictTitle" class="font-bold text-xs sm:text-sm text-emerald-900">Nitidezza Perfetta (Qualità Fotografica)</span>
                        </div>
                        <span id="verdictTag" class="px-2 py-0.5 rounded-full text-[10px] font-black uppercase bg-emerald-200 text-emerald-900 tracking-wider">Qualità Ottima</span>
                    </div>
                    <p id="verdictDesc" class="text-[11px] sm:text-xs text-slate-700 leading-relaxed">
                        A una distanza di 40 cm l'occhio umano richiede almeno 86 DPI. Con 300 DPI l'immagine risulta infinitamente definita, senza alcuna sgranatura o pixel visibile.
                    </p>
                    <div class="flex flex-wrap items-center justify-between pt-1 border-t border-emerald-200/60 text-[10px] font-mono text-slate-600">
                        <span>DPI Attuali: <strong id="curDpiMetric" class="text-emerald-800">300 DPI</strong></span>
                        <span>DPI Minimi Necessari: <strong id="minDpiMetric" class="text-slate-800">86 DPI</strong></span>
                    </div>
                </div>

                <!-- Interactive Aspect Ratio & Pixel Density Blueprint Canvas -->
                <div class="bg-slate-900 rounded-2xl sm:rounded-3xl p-3 sm:p-4 shadow-lg border border-slate-800 text-white space-y-2">
                    <div class="flex items-center justify-between">
                        <div class="flex items-center gap-2">
                            <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
                            <span id="schemaTitle" class="text-xs font-bold text-slate-200 font-jakarta">Rapporto di Forma & Densità Pixel</span>
                        </div>
                        <span id="schemaScaleText" class="text-[10px] font-mono text-slate-400 bg-slate-800 px-2 py-0.5 rounded-md border border-slate-700">In scala dinamica</span>
                    </div>

                    <!-- Blueprint SVG Area -->
                    <div class="blueprint-grid rounded-xl border border-slate-700/80 p-2 sm:p-3 overflow-hidden flex items-center justify-center min-h-[190px] sm:min-h-[220px]">
                        <svg id="blueprintSvg" class="w-full h-44 sm:h-52 transition-all duration-300" viewBox="0 0 460 220" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <!-- Injected dynamically by updateBlueprint() -->
                        </svg>
                    </div>

                    <!-- Quick Copy Specifications Button -->
                    <div class="flex items-center justify-between pt-1">
                        <span class="text-[10px] text-slate-400 hidden sm:inline">Pronto per Photoshop, InDesign e Illustrator</span>
                        <button type="button" onclick="copySpecs()" id="copySpecsBtn" class="w-full sm:w-auto px-3.5 py-1.5 bg-emerald-600 hover:bg-emerald-500 active:scale-95 text-white font-bold text-xs rounded-xl transition flex items-center justify-center gap-1.5 shadow-xs">
                            <span>📋</span>
                            <span id="copyBtnText">Copia Quote Photoshop/InDesign</span>
                        </button>
                    </div>
                </div>

                <!-- Technical Rule Tip Strip -->
                <div class="p-3 bg-amber-50/80 border border-amber-200 rounded-2xl text-[11px] text-amber-900 leading-snug">
                    <span id="ruleTipText">
                        💡 <strong>Regola dell'Acuità Visiva Umana:</strong> A una certa distanza, l'occhio umano non distingue più i singoli pixel. Formula di risoluzione ottica: <code>DPI Ottimale ≈ 3438 / Distanza (cm)</code>. Per libri e riviste a 30 cm bastano 300 DPI; per un cartellone a 5 metri bastano 25-35 DPI.
                    </span>
                </div>

            </div>

        </div>

        <!-- Reference Guide & Normative Tables (SEO Pillar) -->
        <section class="no-print bg-white rounded-2xl sm:rounded-3xl p-4 sm:p-6 border border-slate-200 shadow-xs space-y-4">
            <div class="flex items-center gap-2">
                <span class="text-xl">📋</span>
                <h2 class="text-sm sm:text-base font-bold text-slate-900 font-jakarta">Guida Tecnica: Risoluzione Ottica DPI Consigliata per Distanza di Visione</h2>
            </div>
            <div class="overflow-x-auto">
                <table class="w-full text-left text-xs border-collapse">
                    <thead>
                        <tr class="border-b border-slate-200 text-slate-700 bg-slate-50/80">
                            <th class="py-2.5 px-3 font-bold">Supporto di Stampa</th>
                            <th class="py-2.5 px-3 font-bold">Distanza Tipica</th>
                            <th class="py-2.5 px-3 font-bold">DPI Consigliati</th>
                            <th class="py-2.5 px-3 font-bold">Acuità Occhio Umano</th>
                            <th class="py-2.5 px-3 font-bold">Spazio Colore Tipico</th>
                        </tr>
                    </thead>
                    <tbody class="divide-y divide-slate-100 text-slate-700">
                        <tr class="hover:bg-slate-50/50">
                            <td class="py-2.5 px-3 font-bold text-slate-900">Libri, Riviste, Biglietti da Visita</td>
                            <td class="py-2.5 px-3">25 – 35 cm</td>
                            <td class="py-2.5 px-3 text-emerald-700 font-bold">300 DPI</td>
                            <td class="py-2.5 px-3 font-bold text-slate-800">100 – 130 DPI minimi</td>
                            <td class="py-2.5 px-3 font-mono text-[11px] text-emerald-700">CMYK Fogra 39 / 51</td>
                        </tr>
                        <tr class="hover:bg-slate-50/50">
                            <td class="py-2.5 px-3 font-bold text-slate-900">Fotografia Fine Art & Cataloghi Lusso</td>
                            <td class="py-2.5 px-3">20 – 30 cm</td>
                            <td class="py-2.5 px-3 text-emerald-700 font-bold">360 – 600 DPI</td>
                            <td class="py-2.5 px-3 font-bold text-slate-800">Nitidezza assoluta microscopica</td>
                            <td class="py-2.5 px-3 font-mono text-[11px] text-emerald-700">RGB ProPhoto / Adobe1998</td>
                        </tr>
                        <tr class="hover:bg-slate-50/50">
                            <td class="py-2.5 px-3 font-bold text-slate-900">Poster, Locandine, Manifesti 70×100</td>
                            <td class="py-2.5 px-3">1.0 – 1.5 metri</td>
                            <td class="py-2.5 px-3 text-emerald-700 font-bold">150 – 200 DPI</td>
                            <td class="py-2.5 px-3 font-bold text-slate-800">25 – 35 DPI minimi</td>
                            <td class="py-2.5 px-3 font-mono text-[11px] text-emerald-700">CMYK / RGB Plotter</td>
                        </tr>
                        <tr class="hover:bg-slate-50/50">
                            <td class="py-2.5 px-3 font-bold text-slate-900">Roll-up fieristici & Banner Forex</td>
                            <td class="py-2.5 px-3">1.5 – 2.5 metri</td>
                            <td class="py-2.5 px-3 text-slate-800 font-bold">100 – 120 DPI</td>
                            <td class="py-2.5 px-3 font-bold text-slate-800">15 – 25 DPI minimi</td>
                            <td class="py-2.5 px-3 font-mono text-[11px] text-slate-500">CMYK Digitale Grande Formato</td>
                        </tr>
                        <tr class="hover:bg-slate-50/50">
                            <td class="py-2.5 px-3 font-bold text-slate-900">Cartelloni Stradali 6×3 m & Maxiteli</td>
                            <td class="py-2.5 px-3">5.0 – 15 metri</td>
                            <td class="py-2.5 px-3 text-amber-700 font-bold">25 – 35 DPI</td>
                            <td class="py-2.5 px-3 font-bold text-slate-800">3 – 7 DPI minimi</td>
                            <td class="py-2.5 px-3 font-mono text-[11px] text-slate-500">CMYK (scala 1:1 o 1:10 a 300 DPI)</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </section>

        <!-- Localized FAQs Section (No Print) -->
        <section class="no-print bg-white rounded-2xl sm:rounded-3xl p-4 sm:p-6 border border-slate-200 shadow-xs space-y-3 mt-6">
            <h2 id="faqMainTitle" class="text-sm sm:text-base font-bold text-slate-900 flex items-center gap-2">
                <span>📚</span>
                <span>Domande Frequenti su DPI, Pixel e Risoluzione di Stampa</span>
            </h2>
            
            <div id="faqContainer" class="divide-y divide-slate-100 text-xs sm:text-sm">
                <!-- Localized FAQs injected via JS -->
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
                        <span id="shareSubText" class="text-[11px] text-slate-500 block">Condividilo con grafici, fotografi o colleghi di stampa</span>
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

            <!-- Suggestion Prompt Strip -->
            <div class="bg-gradient-to-r from-emerald-50 to-teal-50/70 border border-emerald-200/80 rounded-2xl p-3.5 sm:p-4 flex flex-col sm:flex-row items-center justify-between gap-3 text-center sm:text-left transition shadow-xs">
                <div class="flex items-center gap-2.5">
                    <span class="text-xl">💡</span>
                    <span id="suggestBannerText" class="text-xs sm:text-sm font-bold text-slate-800">
                        Hai un'idea per un nuovo calcolatore grafico o un miglioramento?
                    </span>
                </div>
                <button type="button" onclick="openSuggestModal()" class="px-3.5 py-1.5 bg-emerald-600 hover:bg-emerald-700 active:scale-95 text-white font-bold text-xs rounded-xl shadow-xs transition shrink-0 inline-flex items-center gap-1">
                    <span id="suggestBtnText">Suggerisci</span>
                    <span>→</span>
                </button>
            </div>

            <!-- OmniTools Network Ecosystem Bar (All Active Tools) -->
            <div class="bg-slate-900 text-white rounded-2xl p-4 sm:p-5 shadow-lg border border-slate-800">
                <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 pb-3 border-b border-slate-800">
                    <div class="flex items-center gap-2">
                        <div class="w-6 h-6 rounded-lg bg-blue-600 flex items-center justify-center text-white text-xs font-bold">
                            ⌘
                        </div>
                        <span class="font-black text-sm tracking-tight font-jakarta">OMNITOOLS <span class="text-blue-400">NETWORK</span></span>
                    </div>
                    <span class="text-[11px] text-slate-400 font-medium">Suite di Calcolatori & Utility di Precisione (Edilizia & Grafica)</span>
                </div>
                
                <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-5 gap-2 pt-3 text-[11px]">
<a href="/rampe" class="p-2 rounded-xl bg-slate-800/60 hover:bg-slate-800 border border-slate-700/60 flex items-center justify-between transition group">
                        <span class="font-bold text-slate-300 group-hover:text-white">📐 Rampe</span>
                        <span class="text-[9px] px-1.5 py-0.2 bg-blue-500/20 text-blue-400 font-bold rounded">Attivo</span>
                    </a>
                    <a href="/scale" class="p-2 rounded-xl bg-slate-800/60 hover:bg-slate-800 border border-slate-700/60 flex items-center justify-between transition group">
                        <span class="font-bold text-slate-300 group-hover:text-white">🪜 Scale</span>
                        <span class="text-[9px] px-1.5 py-0.2 bg-emerald-500/20 text-emerald-400 font-bold rounded">Attivo</span>
                    </a>
                    <a href="/dorso" class="p-2 rounded-xl bg-slate-800/60 hover:bg-slate-800 border border-slate-700/60 flex items-center justify-between transition group">
                        <span class="font-bold text-slate-300 group-hover:text-white">🎨 Dorso Libro</span>
                        <span class="text-[9px] px-1.5 py-0.2 bg-purple-500/20 text-purple-300 font-bold rounded">Attivo</span>
                    </a>
                    <a href="/dpi" class="p-2 rounded-xl bg-slate-800 border border-emerald-500/50 flex items-center justify-between transition">
                        <span class="font-bold text-white">🖼️ Risoluzione & DPI</span>
                        <span class="text-[9px] px-1.5 py-0.2 bg-emerald-500/20 text-emerald-300 font-bold rounded">Attivo</span>
                    </a>
                    <a href="/tubi" class="p-2 rounded-xl bg-slate-800/60 hover:bg-slate-800 border border-slate-700/60 flex items-center justify-between transition group">
                        <span class="font-bold text-slate-300 group-hover:text-white">🚰 ScaricoFacile</span>
                        <span class="text-[9px] px-1.5 py-0.2 bg-cyan-500/20 text-cyan-400 font-bold rounded">Attivo</span>
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
                    <strong>Note Tecniche di Prestampa:</strong> I calcoli di conversione pixel/cm si basano sullo standard internazionale 1 pollice = 2.54 cm. Il peso del file stimato fa riferimento a immagini raster non compresse (TIFF a 8-bit per canale in spazio colore RGB o CMYK). Verificare sempre le schede tecniche del fornitore di stampa o RIP per retini speciali o stampe Fine Art.
                </p>
            </div>
        </div>
    </footer>

    <!-- Smart Floating PWA Install Banner -->
    <div id="installBanner" class="no-print fixed bottom-3 left-3 right-3 sm:left-auto sm:right-6 sm:bottom-6 sm:max-w-sm bg-slate-900 text-white p-3.5 rounded-2xl shadow-2xl border border-slate-700/60 z-50 flex items-center justify-between gap-3 transition-all duration-300 transform translate-y-0">
        <div class="flex items-center gap-2.5 min-w-0">
            <div class="w-9 h-9 rounded-xl bg-emerald-600 flex items-center justify-center text-white shrink-0 font-bold shadow-md">
                📱
            </div>
            <div class="min-w-0">
                <span id="installBannerTitle" class="text-xs font-bold block text-white truncate">Installa OmniTools su Smartphone</span>
                <span id="installBannerSub" class="text-[10px] text-slate-300 block truncate">Utility di prestampa e grafica sempre offline</span>
            </div>
        </div>
        <div class="flex items-center gap-1.5 shrink-0">
            <button onclick="triggerInstall()" id="installBannerBtn" class="px-3 py-1.5 bg-emerald-600 hover:bg-emerald-500 text-white font-bold text-xs rounded-xl transition shadow-xs">
                Installa
            </button>
            <button onclick="dismissInstallBanner()" class="p-1.5 text-slate-400 hover:text-white rounded-lg transition" title="Chiudi">
                ✕
            </button>
        </div>
    </div>

    <!-- Suggestion Modal -->
    <div id="suggestModal" class="no-print fixed inset-0 bg-slate-900/60 backdrop-blur-xs z-50 hidden flex items-center justify-center p-4">
        <div class="bg-white rounded-3xl max-w-md w-full p-5 sm:p-6 shadow-2xl border border-slate-100 space-y-4">
            <div class="flex items-center justify-between">
                <div class="flex items-center gap-2">
                    <span class="text-xl">💡</span>
                    <h3 id="suggestModalTitle" class="text-sm sm:text-base font-bold text-slate-900">Suggerisci una Ferramenta o Calcolatore</h3>
                </div>
                <button onclick="closeSuggestModal()" class="text-slate-400 hover:text-slate-600 p-1 rounded-lg">✕</button>
            </div>
            <p id="suggestModalDesc" class="text-xs text-slate-600">
                Quale calcolatore grafico o funzione tecnica vorresti vedere in OmniTools?
            </p>
            <textarea id="suggestIdeaInput" rows="3" class="w-full bg-slate-50 border border-slate-200 rounded-xl p-3 text-xs text-slate-900 focus:bg-white focus:border-emerald-600 outline-none transition" placeholder="Es. Calcolo peso bancale carta, calcolo resa foglio macchina, etc."></textarea>
            <div class="flex items-center justify-between pt-1">
                <span class="text-[10px] text-slate-600">🔒 Invio 100% anonimo</span>
                <button type="button" onclick="sendSuggestion()" id="suggestSendBtn" class="px-4 py-2 bg-emerald-600 hover:bg-emerald-700 text-white text-xs font-bold rounded-xl transition shadow-xs">
                    Invia Suggerimento
                </button>
            </div>
            <div id="suggestFeedback" class="hidden text-xs font-bold text-emerald-700 bg-emerald-50 p-2.5 rounded-xl border border-emerald-200 text-center">
                🎉 Grazie mille! Il tuo suggerimento guiderà i prossimi sviluppi.
            </div>
        </div>
    </div>

    <!-- JAVASCRIPT CALCULATION & UI ENGINE -->
    <script>
        const TRANSLATIONS = {t_json_str};

        let currentLang = localStorage.getItem('omnitools_lang') || 'it';
        let currentUnit = 'cm';
        let currentMode = 'direct'; // 'direct' = da px a cm, 'reverse' = da cm a px
        let currentDpi = 300;
        let currentDist = 40; // in cm

        function changeLanguage(lang) {{
            if (!TRANSLATIONS[lang]) return;
            currentLang = lang;
            localStorage.setItem('omnitools_lang', lang);
            document.documentElement.lang = lang;
            document.getElementById('langSelect').value = lang;
            applyTranslations();
            calculateResolution();
        }}

        function applyTranslations() {{
            const t = TRANSLATIONS[currentLang];
            if (!t) return;

            document.getElementById('brandTitle').textContent = t.title;
            document.getElementById('brandTitleMobile').textContent = t.title;
            document.getElementById('heroTitle').textContent = t.hero_title;
            document.getElementById('heroDesc').textContent = t.hero_desc;
            document.getElementById('modeDirectBtn').textContent = t.mode_direct;
            document.getElementById('modeReverseBtn').textContent = t.mode_reverse;
            document.getElementById('unitLabelText').textContent = t.unit_label;
            document.getElementById('pixelsWLabel').textContent = t.pixels_w_label;
            document.getElementById('pixelsHLabel').textContent = t.pixels_h_label;
            document.getElementById('printWLabel').innerHTML = `${{t.print_w_label}} (<span class="unitBadge">${{currentUnit}}</span>)`;
            document.getElementById('printHLabel').innerHTML = `${{t.print_h_label}} (<span class="unitBadge">${{currentUnit}}</span>)`;
            document.getElementById('dpiTargetLabel').textContent = t.dpi_target_label;
            document.getElementById('viewDistLabel').textContent = t.view_dist_label;
            document.getElementById('presetsTitle').textContent = t.presets_title;
            document.getElementById('preset1Title').textContent = t.preset_1;
            document.getElementById('preset1Sub').textContent = t.preset_1_sub;
            document.getElementById('preset2Title').textContent = t.preset_2;
            document.getElementById('preset2Sub').textContent = t.preset_2_sub;
            document.getElementById('preset3Title').textContent = t.preset_3;
            document.getElementById('preset3Sub').textContent = t.preset_3_sub;
            document.getElementById('preset4Title').textContent = t.preset_4;
            document.getElementById('preset4Sub').textContent = t.preset_4_sub;
            document.getElementById('colDimLabel').textContent = t.col_dimensions;
            document.getElementById('colPixLabel').textContent = t.col_pixels;
            document.getElementById('colMegaLabel').textContent = t.col_megapixels;
            document.getElementById('schemaTitle').textContent = t.schema_title;
            document.getElementById('printBtnText').textContent = t.print_btn;
            document.getElementById('installBannerTitle').textContent = t.install_banner_title;
            document.getElementById('installBannerSub').textContent = t.install_banner_sub;
            document.getElementById('installBannerBtn').textContent = t.install_btn;
            document.getElementById('legalDisclaimerText').innerHTML = t.legal_disclaimer;
            document.getElementById('faqMainTitle').innerHTML = `<span>📚</span> <span>${{t.faq_title}}</span>`;
            document.getElementById('ruleTipText').innerHTML = t.rule_tip;
            document.getElementById('copyBtnText').textContent = t.copy_btn;

            // Update FAQs
            const faqContainer = document.getElementById('faqContainer');
            faqContainer.innerHTML = `
                <div class="py-2.5">
                    <h3 class="font-bold text-slate-900 mb-1">${{t.faq_1_q}}</h3>
                    <p class="text-slate-600 leading-relaxed text-xs">${{t.faq_1_a}}</p>
                </div>
                <div class="py-2.5">
                    <h3 class="font-bold text-slate-900 mb-1">${{t.faq_2_q}}</h3>
                    <p class="text-slate-600 leading-relaxed text-xs">${{t.faq_2_a}}</p>
                </div>
                <div class="py-2.5">
                    <h3 class="font-bold text-slate-900 mb-1">${{t.faq_3_q}}</h3>
                    <p class="text-slate-600 leading-relaxed text-xs">${{t.faq_3_a}}</p>
                </div>
            `;
        }}

        function switchMode(mode) {{
            currentMode = mode;
            const directGroup = document.getElementById('directInputsGroup');
            const reverseGroup = document.getElementById('reverseInputsGroup');
            const btnDirect = document.getElementById('modeDirectBtn');
            const btnReverse = document.getElementById('modeReverseBtn');

            if (mode === 'direct') {{
                directGroup.classList.remove('hidden');
                reverseGroup.classList.add('hidden');
                btnDirect.className = "flex-1 py-1.5 sm:py-2 rounded-xl bg-white text-emerald-700 shadow-sm transition active:scale-95 text-center font-bold";
                btnReverse.className = "flex-1 py-1.5 sm:py-2 rounded-xl text-slate-600 hover:text-slate-900 transition active:scale-95 text-center font-bold";
            }} else {{
                directGroup.classList.add('hidden');
                reverseGroup.classList.remove('hidden');
                btnReverse.className = "flex-1 py-1.5 sm:py-2 rounded-xl bg-white text-emerald-700 shadow-sm transition active:scale-95 text-center font-bold";
                btnDirect.className = "flex-1 py-1.5 sm:py-2 rounded-xl text-slate-600 hover:text-slate-900 transition active:scale-95 text-center font-bold";
            }}
            calculateResolution();
        }}

        function setUnit(u) {{
            currentUnit = u;
            ['cm', 'mm', 'in'].forEach(unit => {{
                const btn = document.getElementById('unit' + unit.charAt(0).toUpperCase() + unit.slice(1));
                if (unit === u) {{
                    btn.className = "w-10 sm:w-11 py-1 rounded-lg bg-white text-emerald-700 shadow-xs font-extrabold transition active:scale-95 text-center";
                }} else {{
                    btn.className = "w-10 sm:w-11 py-1 rounded-lg text-slate-700 hover:text-slate-900 transition active:scale-95 text-center font-bold";
                }}
            }});
            document.querySelectorAll('.unitBadge').forEach(el => el.textContent = u);
            calculateResolution();
        }}

        function updateDpiFromRange(val) {{
            currentDpi = parseInt(val) || 300;
            document.getElementById('dpiBadge').textContent = currentDpi + ' DPI';
            calculateResolution();
        }}

        function setDpi(dpi) {{
            currentDpi = dpi;
            document.getElementById('dpiRange').value = dpi;
            document.getElementById('dpiBadge').textContent = dpi + ' DPI';
            calculateResolution();
        }}

        function updateDistFromRange(val) {{
            currentDist = parseInt(val) || 40;
            document.getElementById('distBadge').textContent = currentDist + ' cm';
            calculateResolution();
        }}

        function applyPreset(num) {{
            if (num === 1) {{
                // A4 Offset HD 300 DPI
                setUnit('cm');
                setDpi(300);
                updateDistFromRange(35);
                document.getElementById('distRange').value = 35;
                document.getElementById('inputPxW').value = 2480;
                document.getElementById('inputPxH').value = 3508;
                document.getElementById('inputPrintW').value = 21.0;
                document.getElementById('inputPrintH').value = 29.7;
            }} else if (num === 2) {{
                // Manifesto 70x100 cm (150 DPI, dist 1.5 m)
                setUnit('cm');
                setDpi(150);
                updateDistFromRange(150);
                document.getElementById('distRange').value = 150;
                document.getElementById('inputPxW').value = 4134;
                document.getElementById('inputPxH').value = 5906;
                document.getElementById('inputPrintW').value = 70.0;
                document.getElementById('inputPrintH').value = 100.0;
            }} else if (num === 3) {{
                // Roll-up 85x200 cm (100 DPI, dist 2 m)
                setUnit('cm');
                setDpi(100);
                updateDistFromRange(200);
                document.getElementById('distRange').value = 200;
                document.getElementById('inputPxW').value = 3346;
                document.getElementById('inputPxH').value = 7874;
                document.getElementById('inputPrintW').value = 85.0;
                document.getElementById('inputPrintH').value = 200.0;
            }} else if (num === 4) {{
                // Cartellone 6x3 m (30 DPI, dist 5 m)
                setUnit('cm');
                setDpi(30);
                updateDistFromRange(500);
                document.getElementById('distRange').value = 500;
                document.getElementById('inputPxW').value = 7087;
                document.getElementById('inputPxH').value = 3543;
                document.getElementById('inputPrintW').value = 600.0;
                document.getElementById('inputPrintH').value = 300.0;
            }}
            calculateResolution();
        }}

        // Greatest Common Divisor for Aspect Ratio
        function gcd(a, b) {{
            return b ? gcd(b, a % b) : a;
        }}

        function getAspectRatioString(w, h) {{
            const r = w / h;
            if (Math.abs(r - 1.4142) < 0.05 || Math.abs(r - 0.7071) < 0.05) return "ISO A-Series (1:√2)";
            if (Math.abs(r - 1.7778) < 0.04 || Math.abs(r - 0.5625) < 0.04) return "16:9 Panoramico";
            if (Math.abs(r - 1.3333) < 0.04 || Math.abs(r - 0.75) < 0.04) return "4:3 Standard";
            if (Math.abs(r - 1.5) < 0.04 || Math.abs(r - 0.6667) < 0.04) return "3:2 Fotografico";
            if (Math.abs(r - 1.0) < 0.02) return "1:1 Quadrato";
            
            // Generic reduction
            const roundedW = Math.round(w / 10);
            const roundedH = Math.round(h / 10);
            const div = gcd(roundedW, roundedH);
            if (div > 1 && roundedW / div <= 32 && roundedH / div <= 32) {{
                return `${{roundedW / div}}:${{roundedH / div}}`;
            }}
            return `${{r.toFixed(2)}}:1`;
        }}

        function calculateResolution() {{
            let pxW = 0, pxH = 0;
            let printW_cm = 0, printH_cm = 0;
            const dpi = currentDpi;

            if (currentMode === 'direct') {{
                pxW = parseFloat(document.getElementById('inputPxW').value) || 0;
                pxH = parseFloat(document.getElementById('inputPxH').value) || 0;
                if (pxW <= 0 || pxH <= 0 || dpi <= 0) return;

                printW_cm = (pxW / dpi) * 2.54;
                printH_cm = (pxH / dpi) * 2.54;

                // Sync reverse inputs silently
                if (currentUnit === 'cm') {{
                    document.getElementById('inputPrintW').value = printW_cm.toFixed(1);
                    document.getElementById('inputPrintH').value = printH_cm.toFixed(1);
                }} else if (currentUnit === 'mm') {{
                    document.getElementById('inputPrintW').value = (printW_cm * 10).toFixed(0);
                    document.getElementById('inputPrintH').value = (printH_cm * 10).toFixed(0);
                }} else if (currentUnit === 'in') {{
                    document.getElementById('inputPrintW').value = (printW_cm / 2.54).toFixed(2);
                    document.getElementById('inputPrintH').value = (printH_cm / 2.54).toFixed(2);
                }}
            }} else {{
                let rawW = parseFloat(document.getElementById('inputPrintW').value) || 0;
                let rawH = parseFloat(document.getElementById('inputPrintH').value) || 0;
                if (rawW <= 0 || rawH <= 0 || dpi <= 0) return;

                if (currentUnit === 'cm') {{
                    printW_cm = rawW;
                    printH_cm = rawH;
                }} else if (currentUnit === 'mm') {{
                    printW_cm = rawW / 10;
                    printH_cm = rawH / 10;
                }} else if (currentUnit === 'in') {{
                    printW_cm = rawW * 2.54;
                    printH_cm = rawH * 2.54;
                }}

                pxW = Math.round((printW_cm / 2.54) * dpi);
                pxH = Math.round((printH_cm / 2.54) * dpi);

                // Sync direct inputs silently
                document.getElementById('inputPxW').value = pxW;
                document.getElementById('inputPxH').value = pxH;
            }}

            // Calculations
            const printW_in = printW_cm / 2.54;
            const printH_in = printH_cm / 2.54;
            const megapixels = (pxW * pxH) / 1000000;
            const rgbMB = (pxW * pxH * 3) / (1024 * 1024);
            const cmykMB = (pxW * pxH * 4) / (1024 * 1024);

            // Human Visual Acuity Formula: DPI_min = 3438 / Dist_cm
            const minAcuityDpi = Math.max(10, Math.round(3438 / currentDist));

            // Format unit output
            let displayW = printW_cm.toFixed(1) + ' cm';
            let displayH = printH_cm.toFixed(1) + ' cm';
            if (currentUnit === 'mm') {{
                displayW = (printW_cm * 10).toFixed(0) + ' mm';
                displayH = (printH_cm * 10).toFixed(0) + ' mm';
            }} else if (currentUnit === 'in') {{
                displayW = printW_in.toFixed(2) + ' in';
                displayH = printH_in.toFixed(2) + ' in';
            }}

            document.getElementById('valPrintDim').textContent = `${{displayW}} × ${{displayH}}`;
            document.getElementById('valPrintDimIn').textContent = `${{printW_in.toFixed(2)}} × ${{printH_in.toFixed(2)}} in (${{printW_cm.toFixed(1)}} × ${{printH_cm.toFixed(1)}} cm)`;
            document.getElementById('valPixelDim').textContent = `${{pxW}} × ${{pxH}} px`;
            
            const ratioStr = getAspectRatioString(pxW, pxH);
            document.getElementById('valAspectRatio').textContent = `Ratio: ${{ratioStr}}`;
            document.getElementById('valMegapixels').textContent = `${{megapixels.toFixed(2)}} MP`;
            document.getElementById('valFileSize').textContent = `RGB ${{rgbMB.toFixed(1)}} MB • CMYK ${{cmykMB.toFixed(1)}} MB`;

            // Update Acuity Metrics in Verdict
            document.getElementById('curDpiMetric').textContent = `${{dpi}} DPI`;
            document.getElementById('minDpiMetric').textContent = `${{minAcuityDpi}} DPI (${{currentDist}} cm)`;

            // Verdict State
            const verdictBox = document.getElementById('verdictBox');
            const verdictIcon = document.getElementById('verdictIcon');
            const verdictTitle = document.getElementById('verdictTitle');
            const verdictTag = document.getElementById('verdictTag');
            const verdictDesc = document.getElementById('verdictDesc');
            const t = TRANSLATIONS[currentLang];

            if (dpi >= minAcuityDpi * 0.9) {{
                // Ottima qualità
                verdictBox.className = "p-3 sm:p-4 rounded-2xl border bg-emerald-50/80 border-emerald-200 text-slate-800 transition shadow-xs space-y-1.5";
                verdictIcon.textContent = "👁️";
                verdictTitle.className = "font-bold text-xs sm:text-sm text-emerald-900";
                verdictTitle.textContent = t.status_opt_title;
                verdictTag.className = "px-2 py-0.5 rounded-full text-[10px] font-black uppercase bg-emerald-200 text-emerald-900 tracking-wider";
                verdictTag.textContent = t.status_opt_tag;
                verdictDesc.textContent = `A una distanza di ${{currentDist}} cm l'occhio umano richiede almeno ${{minAcuityDpi}} DPI. Con ${{dpi}} DPI l'immagine risulta infinitamente definita, senza alcuna sgranatura o pixel visibile.`;
            }} else if (dpi >= minAcuityDpi * 0.55) {{
                // Qualità Accettabile
                verdictBox.className = "p-3 sm:p-4 rounded-2xl border bg-amber-50/80 border-amber-200 text-slate-800 transition shadow-xs space-y-1.5";
                verdictIcon.textContent = "⚠️";
                verdictTitle.className = "font-bold text-xs sm:text-sm text-amber-900";
                verdictTitle.textContent = t.status_warn_title;
                verdictTag.className = "px-2 py-0.5 rounded-full text-[10px] font-black uppercase bg-amber-200 text-amber-900 tracking-wider";
                verdictTag.textContent = t.status_warn_tag;
                verdictDesc.textContent = `A ${{currentDist}} cm la risoluzione è accettabile per stampa digitale commerciale o affissioni. Per una nitidezza fotografica da vicino servirebbero almeno ${{minAcuityDpi}} DPI.`;
            }} else {{
                // Bassa Risoluzione
                verdictBox.className = "p-3 sm:p-4 rounded-2xl border bg-rose-50/80 border-rose-200 text-slate-800 transition shadow-xs space-y-1.5";
                verdictIcon.textContent = "🛑";
                verdictTitle.className = "font-bold text-xs sm:text-sm text-rose-900";
                verdictTitle.textContent = t.status_danger_title;
                verdictTag.className = "px-2 py-0.5 rounded-full text-[10px] font-black uppercase bg-rose-200 text-rose-900 tracking-wider";
                verdictTag.textContent = t.status_danger_tag;
                verdictDesc.textContent = `Attenzione: a ${{currentDist}} cm l'occhio distingue dettagli fini (${{minAcuityDpi}} DPI necessari). I ${{dpi}} DPI attuali causeranno sgranature o pixel evidenti.`;
            }}

            updateBlueprint(pxW, pxH, printW_cm, printH_cm, dpi, minAcuityDpi);
        }}

        function updateBlueprint(pxW, pxH, wCm, hCm, dpi, minDpi) {{
            const svg = document.getElementById('blueprintSvg');
            const maxSvgW = 440;
            const maxSvgH = 200;
            const padX = 50;
            const padY = 30;

            const availW = maxSvgW - (padX * 2);
            const availH = maxSvgH - (padY * 2);

            const ratio = pxW / pxH;
            let drawW = availW;
            let drawH = drawW / ratio;

            if (drawH > availH) {{
                drawH = availH;
                drawW = drawH * ratio;
            }}

            const startX = (maxSvgW - drawW) / 2;
            const startY = (maxSvgH - drawH) / 2;

            // Generate SVG Inner HTML
            let s = '';

            // Outer Dimensions Indicators
            s += `<line x1="${{startX}}" y1="${{startY - 12}}" x2="${{startX + drawW}}" y2="${{startY - 12}}" stroke="#38bdf8" stroke-width="1.5" />`;
            s += `<line x1="${{startX}}" y1="${{startY - 17}}" x2="${{startX}}" y2="${{startY - 7}}" stroke="#38bdf8" stroke-width="1.5" />`;
            s += `<line x1="${{startX + drawW}}" y1="${{startY - 17}}" x2="${{startX + drawW}}" y2="${{startY - 7}}" stroke="#38bdf8" stroke-width="1.5" />`;
            s += `<text x="${{startX + (drawW / 2)}}" y="${{startY - 16}}" fill="#38bdf8" font-size="10" font-family="'JetBrains Mono', monospace" font-weight="bold" text-anchor="middle">${{wCm.toFixed(1)}} cm (${{pxW}} px)</text>`;

            s += `<line x1="${{startX + drawW + 12}}" y1="${{startY}}" x2="${{startX + drawW + 12}}" y2="${{startY + drawH}}" stroke="#38bdf8" stroke-width="1.5" />`;
            s += `<line x1="${{startX + drawW + 7}}" y1="${{startY}}" x2="${{startX + drawW + 17}}" y2="${{startY}}" stroke="#38bdf8" stroke-width="1.5" />`;
            s += `<line x1="${{startX + drawW + 7}}" y1="${{startY + drawH}}" x2="${{startX + drawW + 17}}" y2="${{startY + drawH}}" stroke="#38bdf8" stroke-width="1.5" />`;
            s += `<text x="${{startX + drawW + 18}}" y="${{startY + (drawH / 2) + 3}}" fill="#38bdf8" font-size="10" font-family="'JetBrains Mono', monospace" font-weight="bold" text-anchor="start">${{hCm.toFixed(1)}} cm</text>`;

            // Artwork Box with Gradient
            s += `<defs>
                <linearGradient id="artGrad" x1="0%" y1="0%" x2="100%" y2="100%">
                    <stop offset="0%" stop-color="#059669" stop-opacity="0.35"/>
                    <stop offset="100%" stop-color="#10b981" stop-opacity="0.15"/>
                </linearGradient>
            </defs>`;
            s += `<rect x="${{startX}}" y="${{startY}}" width="${{drawW}}" height="${{drawH}}" rx="6" fill="url(#artGrad)" stroke="#10b981" stroke-width="2" />`;

            // Center Loupe / Pixel Density Indicator
            const centerX = startX + (drawW / 2);
            const centerY = startY + (drawH / 2);
            s += `<circle cx="${{centerX}}" cy="${{centerY}}" r="24" fill="#0f172a" fill-opacity="0.85" stroke="#38bdf8" stroke-width="1.5" />`;
            s += `<text x="${{centerX}}" y="${{centerY - 2}}" fill="#ffffff" font-size="10" font-family="'JetBrains Mono', monospace" font-weight="bold" text-anchor="middle">${{dpi}}</text>`;
            s += `<text x="${{centerX}}" y="${{centerY + 9}}" fill="#38bdf8" font-size="8" font-family="'Plus Jakarta Sans', sans-serif" font-weight="bold" text-anchor="middle">DPI</text>`;

            // Visual eye observer distance badge at bottom
            s += `<text x="${{startX + (drawW / 2)}}" y="${{startY + drawH + 18}}" fill="#94a3b8" font-size="9" font-family="'Plus Jakarta Sans', sans-serif" font-weight="bold" text-anchor="middle">👁️ Visione a ${{currentDist}} cm • Acuità visiva minima: ${{minDpi}} DPI</text>`;

            svg.innerHTML = s;
        }}

        function copySpecs() {{
            const pxW = document.getElementById('inputPxW').value;
            const pxH = document.getElementById('inputPxH').value;
            const dpi = currentDpi;
            const dim = document.getElementById('valPrintDim').textContent;
            const mp = document.getElementById('valMegapixels').textContent;

            const text = `Larghezza: ${{pxW}} px | Altezza: ${{pxH}} px | Risoluzione: ${{dpi}} DPI | Formato Stampa: ${{dim}} | Risoluzione Sensore: ${{mp}} (OmniTools RisoluzioneFacile)`;
            navigator.clipboard.writeText(text).then(() => {{
                const btn = document.getElementById('copySpecsBtn');
                const orig = btn.innerHTML;
                btn.innerHTML = `<span>✓</span> <span>${{TRANSLATIONS[currentLang].copied_text}}</span>`;
                btn.classList.add('bg-emerald-700');
                setTimeout(() => {{
                    btn.innerHTML = orig;
                    btn.classList.remove('bg-emerald-700');
                }}, 2500);
            }});
        }}

        // Feedback / Suggest Modal
        function openSuggestModal() {{
            document.getElementById('suggestModal').classList.remove('hidden');
        }}
        function closeSuggestModal() {{
            document.getElementById('suggestModal').classList.add('hidden');
            document.getElementById('suggestFeedback').classList.add('hidden');
        }}
        async function sendSuggestion() {{
            const input = document.getElementById('suggestIdeaInput');
            const val = input.value.trim();
            if (!val) return;
            const btn = document.getElementById('suggestSendBtn');
            btn.disabled = true;
            btn.textContent = '...';
            try {{
                await fetch('/api/suggest', {{
                    method: 'POST',
                    headers: {{ 'Content-Type': 'application/json' }},
                    body: JSON.stringify({{ idea: val, tool: 'RisoluzioneFacile', lang: currentLang }})
                }});
            }} catch(e) {{}}
            document.getElementById('suggestFeedback').classList.remove('hidden');
            input.value = '';
            setTimeout(() => closeSuggestModal(), 2000);
            btn.disabled = false;
            btn.textContent = 'Invia Suggerimento';
        }}

        // PWA Install Prompt
        let deferredPrompt;
        window.addEventListener('beforeinstallprompt', (e) => {{
            e.preventDefault();
            deferredPrompt = e;
            const banner = document.getElementById('installBanner');
            if (banner && !sessionStorage.getItem('omnitools_install_dismissed')) {{
                banner.classList.remove('hidden');
            }}
        }});
        function triggerInstall() {{
            if (deferredPrompt) {{
                deferredPrompt.prompt();
                deferredPrompt.userChoice.then(() => {{
                    deferredPrompt = null;
                    dismissInstallBanner();
                }});
            }}
        }}
        function dismissInstallBanner() {{
            document.getElementById('installBanner').classList.add('hidden');
            sessionStorage.setItem('omnitools_install_dismissed', '1');
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

        // Init
        document.addEventListener('DOMContentLoaded', () => {{
            applyTranslations();
            calculateResolution();
        }});
    </script>
</body>
</html>
"""

with open("/Users/ilalu/Documents/Altenative Businnes/Calcolatore_Pendenza/dpi.html", "w", encoding="utf-8") as f:
    f.write(html_code)

print("dpi.html compiled with OmniGraph brand successfully.")
