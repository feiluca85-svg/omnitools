import json
import os
from nav_header import render_suite_header, render_suite_header_js

# Load barcode translations
with open('/Users/ilalu/Documents/Altenative Businnes/Calcolatore_Pendenza/translations_barcode.json', 'r', encoding='utf-8') as f:
    t_data = json.load(f)

t_json_str = json.dumps(t_data, ensure_ascii=False)

# Read jsbarcode library to embed directly for 100% offline resilience
with open('/Users/ilalu/Documents/Altenative Businnes/Calcolatore_Pendenza/jsbarcode.min.js', 'r', encoding='utf-8') as f:
    jsbarcode_code = f.read()

# Build HTML
header_html = render_suite_header("barcode")
header_js = render_suite_header_js()

it_t = t_data["it"]

html_code = f"""<!DOCTYPE html>
<html lang="it">
<head>
    <meta name="google-site-verification" content="MRdbDm9lLhokeD3I0FOpUSOhNaF_2WaveKvu52FxtG4">
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0">
    <title>Generatore Codici a Barre Online Vettoriale SVG & PDF — EAN-13, Tessera Sanitaria & Verifica GS1</title>
    <meta name="description" content="Generatore professionale di codici a barre vettoriali SVG e PDF ad alta risoluzione (EAN-13, UPC-A, Code 128, Code 39 per Tessera Sanitaria). Include simulatore contrasto laser 670 nm conforme alle specifiche ufficiali GS1.">
    
    <!-- Canonical & SEO Meta Tags -->
    <link rel="canonical" href="https://www.omnitoolslab.com/barcode">
    <meta name="robots" content="index, follow">
    <meta property="og:type" content="website">
    <meta property="og:title" content="OmniBarcode Studio — Generatore Codici a Barre Vettoriale SVG & Verifica GS1">
    <meta property="og:description" content="Genera codici a barre SVG vettoriali puri e PDF per packaging, editoria e sanità. Con simulatore laser GS1 a 670 nm e preset Tessera Sanitaria.">
    <meta property="og:url" content="https://www.omnitoolslab.com/barcode">
    <meta property="og:site_name" content="OmniTools Lab">
    <meta property="og:image" content="https://www.omnitoolslab.com/og-barcode.png">
    <meta property="og:image:width" content="1200">
    <meta property="og:image:height" content="630">
    <meta property="og:image:type" content="image/png">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:image" content="https://www.omnitoolslab.com/og-barcode.png">

    <!-- Schema.org JSON-LD Structured Data (Rich Snippets) -->
    <script type="application/ld+json">
    [
      {{
        "@context": "https://schema.org",
        "@type": "WebApplication",
        "name": "OmniBarcode Studio - Generatore Codici a Barre Vettoriale GS1",
        "url": "https://www.omnitoolslab.com/barcode",
        "applicationCategory": "DesignApplication",
        "operatingSystem": "All",
        "description": "Generatore vettoriale SVG/PDF di codici a barre EAN-13, UPC-A, Code 128 e Code 39 (Tessera Sanitaria) con verifica contrasto laser 670 nm conforme alle specifiche GS1.",
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
            "name": "OmniBarcode Studio",
            "item": "https://www.omnitoolslab.com/barcode"
          }}
        ]
      }},
      {{
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
          {{
            "@type": "Question",
            "name": "{it_t['faq_1_q']}",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "{it_t['faq_1_a'].replace('<strong>', '').replace('</strong>', '')}"
            }}
          }},
          {{
            "@type": "Question",
            "name": "{it_t['faq_2_q']}",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "{it_t['faq_2_a'].replace('<strong>', '').replace('</strong>', '').replace('<em>', '').replace('</em>', '')}"
            }}
          }},
          {{
            "@type": "Question",
            "name": "{it_t['faq_3_q']}",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "{it_t['faq_3_a'].replace('<strong>', '').replace('</strong>', '')}"
            }}
          }},
          {{
            "@type": "Question",
            "name": "{it_t['faq_4_q']}",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "{it_t['faq_4_a'].replace('<strong>', '').replace('</strong>', '')}"
            }}
          }}
        ]
      }}
    ]
    </script>
    <link rel="manifest" href="manifest-graph.json">
    <link rel="icon" type="image/svg+xml" href="favicon.svg?v=6">
    <link rel="alternate icon" type="image/png" href="favicon.png?v=6">
    <link rel="shortcut icon" href="favicon.svg?v=6">
    <meta name="theme-color" content="#4f46e5">
    <meta name="mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
    <meta name="apple-mobile-web-app-title" content="OmniBarcode">
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
                        sans: ['Plus Jakarta Sans', '-apple-system', 'BlinkMacSystemFont', 'Segoe UI', 'Roboto', 'sans-serif'],
                        mono: ['JetBrains Mono', 'monospace'],
                        jakarta: ['Plus Jakarta Sans', 'sans-serif']
                    }},
                    screens: {{
                        'xs': '480px'
                    }}
                }}
            }}
        }}
    </script>

    <!-- Embedded JsBarcode Library (100% Offline Resilience) -->
    <script>
    {jsbarcode_code}
    </script>

    <style>
        .custom-scrollbar::-webkit-scrollbar {{
            width: 5px;
            height: 5px;
        }}
        .custom-scrollbar::-webkit-scrollbar-track {{
            background: #f1f5f9;
        }}
        .custom-scrollbar::-webkit-scrollbar-thumb {{
            background: #cbd5e1;
            border-radius: 4px;
        }}
        
        .laser-line {{
            position: absolute;
            left: 0;
            right: 0;
            height: 2px;
            background: #ef4444;
            box-shadow: 0 0 8px #ef4444, 0 0 12px #f87171;
            pointer-events: none;
            animation: laserScan 2.5s ease-in-out infinite alternate;
        }}
        @keyframes laserScan {{
            0% {{ top: 15%; opacity: 0.6; }}
            50% {{ top: 50%; opacity: 0.95; }}
            100% {{ top: 85%; opacity: 0.6; }}
        }}

        @page {{
            size: A4 portrait;
            margin: 8mm 10mm 8mm 10mm;
        }}
        @media print {{
            header, footer, nav,
            .no-print,
            #faqSection, #normSection, #shareStrip,
            #installBanner, #iosModal,
            button, input, select {{ 
                display: none !important; 
            }}
            .print-only {{
                display: block !important;
            }}
        }}
    </style>
</head>
<body class="bg-slate-50 text-slate-800 font-sans antialiased min-h-screen flex flex-col justify-between selection:bg-indigo-500 selection:text-white">

{header_html}

    <!-- Main Content -->
    <main class="max-w-5xl mx-auto px-3 sm:px-6 py-2.5 sm:py-5 flex-1 w-full space-y-3 sm:space-y-5">
        
        <!-- Hero Header -->
        <div class="text-center space-y-1.5 sm:space-y-2">
            <div class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-purple-50 border border-purple-200/80 text-[11px] font-extrabold text-purple-800 tracking-wide uppercase">
                <span>🎯</span>
                <span id="heroBadge">OmniGraph · Packaging & Editoria</span>
            </div>
            <h1 id="heroTitle" class="text-2xl sm:text-3xl md:text-4xl font-extrabold font-jakarta text-slate-900 tracking-tight leading-tight">
                Generatore Codici a Barre Vettoriale & GS1
            </h1>
            <p id="heroDesc" class="text-xs sm:text-sm text-slate-600 max-w-2xl mx-auto leading-relaxed">
                Genera codici a barre SVG vettoriali puri e PDF per packaging, editoria e magazzino. Include preset per Tessera Sanitaria (Code 39) e simulatore contrasto laser 670 nm conforme alle specifiche ufficiali GS1.
            </p>
        </div>

        <!-- Presets Quick Bar -->
        <div class="bg-white rounded-2xl p-2.5 sm:p-3 border border-slate-200 shadow-2xs">
            <div class="text-[11px] font-extrabold uppercase tracking-wider text-slate-400 mb-2 px-1 flex items-center justify-between">
                <span>⚡ Preset Rapidi Standard</span>
                <span class="text-[10px] text-indigo-600 font-bold hidden sm:inline">1-Click Setup</span>
            </div>
            <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
                <button type="button" onclick="applyPreset('ts')" class="flex flex-col text-left p-2 rounded-xl bg-purple-50/70 hover:bg-purple-100/70 border border-purple-200 transition group">
                    <span class="text-xs font-bold text-purple-900 group-hover:text-purple-700 flex items-center gap-1">
                        <span>🏥</span> Tessera Sanitaria
                    </span>
                    <span class="text-[10px] text-purple-700">Code 39 • Codice Fiscale</span>
                </button>
                <button type="button" onclick="applyPreset('ean13')" class="flex flex-col text-left p-2 rounded-xl bg-blue-50/70 hover:bg-blue-100/70 border border-blue-200 transition group">
                    <span class="text-xs font-bold text-blue-900 group-hover:text-blue-700 flex items-center gap-1">
                        <span>🛒</span> EAN-13 Commercio
                    </span>
                    <span class="text-[10px] text-blue-700">13 Cifre GDO & Checksum</span>
                </button>
                <button type="button" onclick="applyPreset('code128')" class="flex flex-col text-left p-2 rounded-xl bg-indigo-50/70 hover:bg-indigo-100/70 border border-indigo-200 transition group">
                    <span class="text-xs font-bold text-indigo-900 group-hover:text-indigo-700 flex items-center gap-1">
                        <span>📦</span> Code 128 Pacchi
                    </span>
                    <span class="text-[10px] text-indigo-700">Logistica, Spedizioni, Hub</span>
                </button>
                <button type="button" onclick="applyPreset('upca')" class="flex flex-col text-left p-2 rounded-xl bg-emerald-50/70 hover:bg-emerald-100/70 border border-emerald-200 transition group">
                    <span class="text-xs font-bold text-emerald-900 group-hover:text-emerald-700 flex items-center gap-1">
                        <span>🇺🇸</span> UPC-A Retail USA
                    </span>
                    <span class="text-[10px] text-emerald-700">12 Cifre Nord America</span>
                </button>
            </div>
        </div>

        <!-- 2-Column Studio Layout -->
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-3 sm:gap-5">
            
            <!-- LEFT COLUMN: Controls & Parameters (7 Cols) -->
            <div class="lg:col-span-6 space-y-3 sm:space-y-4">
                
                <!-- Main Parameters Card -->
                <div class="bg-white rounded-2xl p-4 sm:p-5 border border-slate-200 shadow-2xs space-y-3.5">
                    
                    <!-- Symbology Selector -->
                    <div>
                        <label id="symbologyLabel" class="block text-xs font-bold text-slate-700 mb-1.5">
                            Simbologia / Standard Barcode
                        </label>
                        <select id="symbologySelect" onchange="onSymbologyChange()" class="w-full bg-slate-50 border border-slate-200 rounded-xl px-3 py-2 text-xs sm:text-sm font-bold text-slate-800 focus:outline-none focus:ring-2 focus:ring-indigo-500/20 focus:border-indigo-500 transition cursor-pointer">
                            <option value="EAN13">EAN-13 (Commercio & GDO Europa)</option>
                            <option value="UPC">UPC-A (Standard USA & Nord America)</option>
                            <option value="CODE128">Code 128 (Logistica, Magazzino & Pacchi)</option>
                            <option value="CODE39">Code 39 (Industria & Tessera Sanitaria)</option>
                        </select>
                    </div>

                    <!-- Input Code -->
                    <div>
                        <div class="flex items-center justify-between mb-1.5">
                            <label id="inputLabel" class="text-xs font-bold text-slate-700">
                                Codice / Dati da Codificare
                            </label>
                            <span id="checksumStatus" class="text-[10px] font-bold text-emerald-600 bg-emerald-50 px-2 py-0.5 rounded border border-emerald-200">
                                Check-digit auto
                            </span>
                        </div>
                        <div class="relative">
                            <input type="text" id="barcodeValue" value="801234567890" oninput="updateBarcode()" placeholder="Es. 801234567890" class="w-full bg-slate-50 border border-slate-200 rounded-xl px-3 py-2 text-xs sm:text-sm font-mono font-bold text-slate-800 focus:outline-none focus:ring-2 focus:ring-indigo-500/20 focus:border-indigo-500 transition">
                            <button type="button" onclick="randomizeCode()" class="absolute right-2 top-1.5 px-2 py-1 text-[10px] font-bold text-slate-500 hover:text-indigo-600 bg-white hover:bg-indigo-50 rounded-lg border border-slate-200 transition" title="Genera codice casuale">
                                🎲 Random
                            </button>
                        </div>
                        <p id="inputHelper" class="text-[10px] text-slate-500 mt-1">
                            Per EAN-13 inserisci 12 cifre: la 13ª cifra di controllo (checksum) viene calcolata automaticamente.
                        </p>
                    </div>

                    <!-- Settings: Display Value & Dimensions -->
                    <div class="pt-2 border-t border-slate-100 space-y-3">
                        <div class="flex items-center justify-between">
                            <label id="displayValueLabel" for="displayValueCheck" class="text-xs font-semibold text-slate-700 cursor-pointer">
                                Mostra Testo sotto le Barre (Human Readable)
                            </label>
                            <input type="checkbox" id="displayValueCheck" checked onchange="updateBarcode()" class="w-4 h-4 rounded text-indigo-600 focus:ring-indigo-500 cursor-pointer">
                        </div>

                        <!-- Sliders Grid -->
                        <div class="grid grid-cols-1 sm:grid-cols-3 gap-2.5 pt-1">
                            <div>
                                <div class="flex items-center justify-between text-[11px] font-bold text-slate-700 mb-1">
                                    <span id="barWidthLabel">Modulo</span>
                                    <span id="barWidthVal" class="font-mono text-indigo-600">2 px</span>
                                </div>
                                <input type="range" id="barWidth" min="1" max="4" step="0.5" value="2" oninput="updateBarcode()" class="w-full accent-indigo-600 cursor-pointer">
                            </div>
                            <div>
                                <div class="flex items-center justify-between text-[11px] font-bold text-slate-700 mb-1">
                                    <span id="barHeightLabel">Altezza</span>
                                    <span id="barHeightVal" class="font-mono text-indigo-600">60 px</span>
                                </div>
                                <input type="range" id="barHeight" min="30" max="120" step="5" value="60" oninput="updateBarcode()" class="w-full accent-indigo-600 cursor-pointer">
                            </div>
                            <div>
                                <div class="flex items-center justify-between text-[11px] font-bold text-slate-700 mb-1">
                                    <span id="quietZoneLabel">Quiet Zone</span>
                                    <span id="quietZoneVal" class="font-mono text-indigo-600">10 px</span>
                                </div>
                                <input type="range" id="quietZone" min="0" max="30" step="5" value="10" oninput="updateBarcode()" class="w-full accent-indigo-600 cursor-pointer">
                            </div>
                        </div>
                    </div>
                </div>

                <!-- GS1 Colors & Laser Contrast Engine Card -->
                <div class="bg-white rounded-2xl p-4 sm:p-5 border border-slate-200 shadow-2xs space-y-3">
                    <div class="flex items-center justify-between">
                        <h2 id="colorsTitle" class="text-xs font-bold text-slate-800 uppercase tracking-wide flex items-center gap-1.5">
                            <span>🎨</span> Colori & Verifica Contrasto Laser GS1 (670 nm)
                        </h2>
                        <span class="text-[9px] font-bold px-2 py-0.5 rounded-full bg-slate-100 text-slate-600">Norme GS1</span>
                    </div>

                    <!-- Color Pickers Row -->
                    <div class="grid grid-cols-2 gap-3">
                        <div class="p-2.5 rounded-xl bg-slate-50 border border-slate-200">
                            <label id="barColorLabel" class="block text-[11px] font-bold text-slate-700 mb-1.5">
                                Colore Barre
                            </label>
                            <div class="flex items-center gap-2">
                                <input type="color" id="barColor" value="#000000" onchange="updateBarcode()" class="w-8 h-8 rounded-lg border border-slate-300 cursor-pointer p-0 bg-transparent">
                                <input type="text" id="barColorText" value="#000000" oninput="syncColorText('bar')" class="w-full text-xs font-mono font-bold text-slate-700 bg-white border border-slate-200 rounded-lg px-2 py-1 uppercase">
                            </div>
                        </div>

                        <div class="p-2.5 rounded-xl bg-slate-50 border border-slate-200">
                            <label id="bgColorLabel" class="block text-[11px] font-bold text-slate-700 mb-1.5">
                                Colore Sfondo
                            </label>
                            <div class="flex items-center gap-2">
                                <input type="color" id="bgColor" value="#ffffff" onchange="updateBarcode()" class="w-8 h-8 rounded-lg border border-slate-300 cursor-pointer p-0 bg-transparent">
                                <input type="text" id="bgColorText" value="#ffffff" oninput="syncColorText('bg')" class="w-full text-xs font-mono font-bold text-slate-700 bg-white border border-slate-200 rounded-lg px-2 py-1 uppercase">
                            </div>
                        </div>
                    </div>

                    <!-- Official GS1 Presets (Tabella 1 & Tabella 2) -->
                    <div>
                        <div class="text-[10px] font-extrabold uppercase tracking-wider text-slate-400 mb-1.5">
                            Combinazioni Ufficiali GS1:
                        </div>
                        <div class="grid grid-cols-2 sm:grid-cols-3 gap-1.5">
                            <button type="button" onclick="setColorPair('#000000', '#ffffff')" class="text-left px-2 py-1.5 rounded-lg border border-slate-200 bg-white hover:bg-slate-50 text-[11px] font-bold text-slate-700 transition flex items-center gap-1.5">
                                <span class="w-3.5 h-3.5 rounded border border-slate-300 bg-black shrink-0"></span>
                                <span class="truncate">Nero su Bianco (GS1)</span>
                            </button>
                            <button type="button" onclick="setColorPair('#002060', '#ffffff')" class="text-left px-2 py-1.5 rounded-lg border border-slate-200 bg-white hover:bg-slate-50 text-[11px] font-bold text-slate-700 transition flex items-center gap-1.5">
                                <span class="w-3.5 h-3.5 rounded border border-slate-300 bg-[#002060] shrink-0"></span>
                                <span class="truncate">Blu Scuro su Bianco</span>
                            </button>
                            <button type="button" onclick="setColorPair('#006020', '#ffffff')" class="text-left px-2 py-1.5 rounded-lg border border-slate-200 bg-white hover:bg-slate-50 text-[11px] font-bold text-slate-700 transition flex items-center gap-1.5">
                                <span class="w-3.5 h-3.5 rounded border border-slate-300 bg-[#006020] shrink-0"></span>
                                <span class="truncate">Verde Scuro su Bianco</span>
                            </button>
                            <button type="button" onclick="setColorPair('#000000', '#facc15')" class="text-left px-2 py-1.5 rounded-lg border border-slate-200 bg-white hover:bg-slate-50 text-[11px] font-bold text-slate-700 transition flex items-center gap-1.5">
                                <span class="w-3.5 h-3.5 rounded border border-slate-300 bg-[#facc15] shrink-0"></span>
                                <span class="truncate">Nero su Giallo</span>
                            </button>
                            <button type="button" onclick="setColorPair('#000000', '#ef4444')" class="text-left px-2 py-1.5 rounded-lg border border-slate-200 bg-white hover:bg-slate-50 text-[11px] font-bold text-slate-700 transition flex items-center gap-1.5">
                                <span class="w-3.5 h-3.5 rounded border border-slate-300 bg-[#ef4444] shrink-0"></span>
                                <span class="truncate">Nero su Rosso (GS1)</span>
                            </button>
                            <button type="button" onclick="setColorPair('#ef4444', '#ffffff')" class="text-left px-2 py-1.5 rounded-lg border border-rose-200 bg-rose-50 hover:bg-rose-100 text-[11px] font-bold text-rose-700 transition flex items-center gap-1.5">
                                <span class="w-3.5 h-3.5 rounded border border-rose-300 bg-[#ef4444] shrink-0"></span>
                                <span class="truncate">⚠️ Barre Rosse (Errore)</span>
                            </button>
                        </div>
                    </div>
                </div>

            </div>

            <!-- RIGHT COLUMN: Live SVG Preview, GS1 Laser Simulator & Export (5 Cols) -->
            <div class="lg:col-span-6 space-y-3 sm:space-y-4">
                
                <!-- Vector Barcode Preview Card -->
                <div class="bg-white rounded-2xl p-4 sm:p-5 border border-slate-200 shadow-2xs space-y-3">
                    <div class="flex items-center justify-between">
                        <span class="text-xs font-bold text-slate-700 uppercase tracking-wide flex items-center gap-1.5">
                            <span>🔍</span> Anteprima Vettoriale SVG
                        </span>
                        <span id="barcodeSpecsBadge" class="text-[10px] font-mono font-bold px-2 py-0.5 rounded bg-slate-100 text-slate-600">
                            EAN-13 • 100% Vettoriale
                        </span>
                    </div>

                    <!-- Canvas / SVG Container -->
                    <div id="barcodePreviewBox" class="w-full min-h-[170px] rounded-xl border border-slate-200 flex items-center justify-center p-3 sm:p-4 overflow-x-auto custom-scrollbar transition-colors" style="background-color: #ffffff;">
                        <svg id="barcodeSvg" class="max-w-full"></svg>
                    </div>

                    <!-- Export Actions Grid -->
                    <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 pt-1">
                        <button type="button" onclick="exportSvg()" class="flex items-center justify-center gap-1.5 px-3 py-2.5 rounded-xl bg-indigo-600 hover:bg-indigo-700 text-white text-xs font-bold shadow-md shadow-indigo-600/20 active:scale-95 transition">
                            <span>⬇️</span>
                            <span id="exportSvgBtn">Scarica SVG Vettoriale</span>
                        </button>
                        <button type="button" onclick="exportPng()" class="flex items-center justify-center gap-1.5 px-3 py-2.5 rounded-xl bg-slate-800 hover:bg-slate-900 text-white text-xs font-bold shadow-md shadow-slate-800/20 active:scale-95 transition">
                            <span>🖼️</span>
                            <span id="exportPngBtn">Scarica PNG (300 DPI)</span>
                        </button>
                        <button type="button" onclick="copySvgCode()" class="flex items-center justify-center gap-1.5 px-3 py-2 rounded-xl bg-slate-100 hover:bg-slate-200 text-slate-700 text-xs font-bold border border-slate-200 active:scale-95 transition">
                            <span>📋</span>
                            <span id="copySvgBtn">Copia Codice SVG</span>
                        </button>
                        <button type="button" onclick="window.print()" class="flex items-center justify-center gap-1.5 px-3 py-2 rounded-xl bg-slate-100 hover:bg-slate-200 text-slate-700 text-xs font-bold border border-slate-200 active:scale-95 transition">
                            <span>🖨️</span>
                            <span id="printBtnSpec">Stampa Scheda Tecnica</span>
                        </button>
                    </div>
                </div>

                <!-- GS1 Laser Vision Simulator Card (670 nm) -->
                <div class="bg-slate-900 text-white rounded-2xl p-4 sm:p-5 border border-slate-800 shadow-xl space-y-3 relative overflow-hidden">
                    <div class="flex items-center justify-between">
                        <div class="flex items-center gap-1.5">
                            <span class="w-2.5 h-2.5 rounded-full bg-red-500 animate-ping"></span>
                            <span class="text-xs font-black uppercase tracking-wider text-rose-400">
                                👁️ Visore Laser GS1 (670 nm)
                            </span>
                        </div>
                        <span id="pcsBadge" class="text-[10px] font-mono font-black px-2 py-0.5 rounded bg-slate-800 text-emerald-400 border border-slate-700">
                            PCS: 100%
                        </span>
                    </div>

                    <p class="text-[11px] text-slate-300 leading-tight">
                        Simulazione ottica di come la fotocellula laser a raggio rosso (670 nm) percepisce il codice a barre:
                    </p>

                    <!-- Laser View Simulation Box -->
                    <div class="relative bg-black rounded-xl p-3 border border-slate-800 flex items-center justify-center overflow-hidden">
                        <div class="laser-line"></div>
                        <div id="laserSimBox" class="p-2 rounded flex items-center justify-center transition-all duration-300" style="background-color: #ffffff;">
                            <svg id="laserSimSvg" class="max-w-full opacity-95"></svg>
                        </div>
                    </div>

                    <!-- GS1 Verdict Banner -->
                    <div id="gs1VerdictBox" class="p-3 rounded-xl bg-emerald-950/80 border border-emerald-500/40 text-emerald-200 text-xs space-y-1">
                        <div id="gs1VerdictTitle" class="font-extrabold text-emerald-300 flex items-center gap-1.5">
                            🟢 CONFORME GS1 — PCS Ottimale (≥ 75%)
                        </div>
                        <div id="gs1VerdictDesc" class="text-[11px] text-emerald-200/90 leading-relaxed">
                            Contrasto spettrale perfetto. Il raggio laser a 670 nm distingue nettamente le barre dallo sfondo. Lettura istantanea garantita a tutte le casse.
                        </div>
                    </div>
                </div>

            </div>
        </div>

        <!-- Educational Rule Tip Box -->
        <div class="bg-indigo-50/70 border border-indigo-200/80 rounded-2xl p-3 sm:p-4 text-xs text-indigo-900 leading-relaxed shadow-2xs">
            <span id="ruleTipText">
                💡 <strong>La Fisica del Laser GS1 a 670 nm:</strong> Gli scanner da cassa e industriali emettono luce laser rossa (lunghezza d'onda ~670 nm). La luce rossa viene <em>riflessa</em> dai pigmenti caldi (rosso, arancio, giallo, oro) che quindi allo scanner appaiono <strong>BIANCHI</strong>. Viene invece <em>assorbita</em> dai pigmenti freddi e scuri (nero, blu scuro, verde scuro, marrone) che appaiono <strong>NERI</strong>. Ecco perché le barre rosse o gialle sono del tutto invisibili allo scanner!
            </span>
        </div>

        <!-- FAQ Section (Pre-rendered static HTML with JSON Schema) -->
        <section id="faqSection" class="bg-white rounded-2xl p-4 sm:p-6 border border-slate-200 shadow-2xs space-y-4">
            <div class="flex items-center gap-2 border-b border-slate-100 pb-3">
                <span class="text-xl">❓</span>
                <h2 id="faqTitle" class="text-base sm:text-lg font-bold text-slate-900">
                    Domande Frequenti su Codici a Barre, GS1 e Tessera Sanitaria
                </h2>
            </div>
            
            <div id="faqContainer" class="space-y-3">
                <details class="group bg-slate-50 rounded-xl p-3.5 border border-slate-200/80 transition" open>
                    <summary class="font-bold text-xs sm:text-sm text-slate-800 cursor-pointer list-none flex items-center justify-between">
                        <span id="faq1Q">{it_t['faq_1_q']}</span>
                        <span class="text-slate-400 group-open:rotate-180 transition-transform duration-200">▾</span>
                    </summary>
                    <div id="faq1A" class="text-xs text-slate-600 mt-2 leading-relaxed">
                        {it_t['faq_1_a']}
                    </div>
                </details>

                <details class="group bg-slate-50 rounded-xl p-3.5 border border-slate-200/80 transition">
                    <summary class="font-bold text-xs sm:text-sm text-slate-800 cursor-pointer list-none flex items-center justify-between">
                        <span id="faq2Q">{it_t['faq_2_q']}</span>
                        <span class="text-slate-400 group-open:rotate-180 transition-transform duration-200">▾</span>
                    </summary>
                    <div id="faq2A" class="text-xs text-slate-600 mt-2 leading-relaxed">
                        {it_t['faq_2_a']}
                    </div>
                </details>

                <details class="group bg-slate-50 rounded-xl p-3.5 border border-slate-200/80 transition">
                    <summary class="font-bold text-xs sm:text-sm text-slate-800 cursor-pointer list-none flex items-center justify-between">
                        <span id="faq3Q">{it_t['faq_3_q']}</span>
                        <span class="text-slate-400 group-open:rotate-180 transition-transform duration-200">▾</span>
                    </summary>
                    <div id="faq3A" class="text-xs text-slate-600 mt-2 leading-relaxed">
                        {it_t['faq_3_a']}
                    </div>
                </details>

                <details class="group bg-slate-50 rounded-xl p-3.5 border border-slate-200/80 transition">
                    <summary class="font-bold text-xs sm:text-sm text-slate-800 cursor-pointer list-none flex items-center justify-between">
                        <span id="faq4Q">{it_t['faq_4_q']}</span>
                        <span class="text-slate-400 group-open:rotate-180 transition-transform duration-200">▾</span>
                    </summary>
                    <div id="faq4A" class="text-xs text-slate-600 mt-2 leading-relaxed">
                        {it_t['faq_4_a']}
                    </div>
                </details>
            </div>
        </section>

        <!-- Technical Disclaimer -->
        <div class="text-[11px] text-slate-500 text-center leading-relaxed max-w-3xl mx-auto px-2">
            <span id="legalDisclaimer">
                {it_t['legal_disclaimer']}
            </span>
        </div>

    </main>

    <!-- Footer -->
    <footer class="bg-white border-t border-slate-200 py-6 mt-8">
        <div class="max-w-5xl mx-auto px-4 flex flex-col sm:flex-row items-center justify-between gap-4 text-xs text-slate-500">
            <div class="flex items-center gap-2">
                <span class="font-jakarta font-black text-slate-900">Omni<span class="text-blue-600">Tools</span></span>
                <span>© 2026 OmniTools Lab • Precision Utilities Suite</span>
            </div>
            <div class="flex items-center gap-3">
                <a href="/" class="hover:text-blue-600 transition">Tutti gli strumenti</a>
                <span>•</span>
                <a href="/partnership" class="hover:text-blue-600 transition">Partnership B2B</a>
                <span>•</span>
                <a href="/privacy" class="hover:text-blue-600 transition">Privacy</a>
            </div>
        </div>
    </footer>

    <!-- App Script Logic -->
    <script>
        const TRANSLATIONS = {t_json_str};
        let currentLang = 'it';

        {header_js}

        function calculateEan13CheckDigit(str) {{
            if (!str || str.length < 12) return null;
            let sum = 0;
            for (let i = 0; i < 12; i++) {{
                let n = parseInt(str[i], 10);
                if (isNaN(n)) return null;
                sum += (i % 2 === 0) ? n : n * 3;
            }}
            return (10 - (sum % 10)) % 10;
        }}

        function calculateUpcCheckDigit(str) {{
            if (!str || str.length < 11) return null;
            let sum = 0;
            for (let i = 0; i < 11; i++) {{
                let n = parseInt(str[i], 10);
                if (isNaN(n)) return null;
                sum += (i % 2 === 0) ? n * 3 : n;
            }}
            return (10 - (sum % 10)) % 10;
        }}

        function onSymbologyChange() {{
            const symb = document.getElementById('symbologySelect').value;
            const input = document.getElementById('barcodeValue');
            const helper = document.getElementById('inputHelper');
            const status = document.getElementById('checksumStatus');

            if (symb === 'EAN13') {{
                input.placeholder = 'Es. 801234567890 (12 o 13 cifre)';
                helper.innerText = 'Per EAN-13 inserisci 12 cifre: la 13ª cifra di controllo viene calcolata automaticamente.';
                if (!/^\d{{12,13}}$/.test(input.value)) {{
                    input.value = '801234567890';
                }}
            }} else if (symb === 'UPC') {{
                input.placeholder = 'Es. 01234567890 (11 o 12 cifre)';
                helper.innerText = 'Per UPC-A inserisci 11 cifre: la 12ª cifra di controllo viene calcolata automaticamente.';
                if (!/^\d{{11,12}}$/.test(input.value)) {{
                    input.value = '01234567890';
                }}
            }} else if (symb === 'CODE39') {{
                input.placeholder = 'Es. RSSMRA85M01H501Z (Alfanumerico TS)';
                helper.innerText = 'Code 39 supporta lettere maiuscole (A-Z), numeri (0-9) e simboli standard. Ideale per Tessera Sanitaria.';
            }} else {{
                input.placeholder = 'Es. PACK-2026-X7';
                helper.innerText = 'Code 128 supporta qualsiasi carattere alfanumerico ASCII ad alta densità.';
            }}
            updateBarcode();
        }}

        function applyPreset(type) {{
            const symb = document.getElementById('symbologySelect');
            const input = document.getElementById('barcodeValue');
            const height = document.getElementById('barHeight');
            const width = document.getElementById('barWidth');
            const displayCheck = document.getElementById('displayValueCheck');

            if (type === 'ts') {{
                symb.value = 'CODE39';
                input.value = 'RSSMRA85M01H501Z';
                height.value = 50;
                width.value = 1.5;
                displayCheck.checked = true;
                setColorPair('#000000', '#ffffff');
            }} else if (type === 'ean13') {{
                symb.value = 'EAN13';
                input.value = '801234567890';
                height.value = 60;
                width.value = 2;
                displayCheck.checked = true;
                setColorPair('#000000', '#ffffff');
            }} else if (type === 'code128') {{
                symb.value = 'CODE128';
                input.value = 'LOGIS-849204-IT';
                height.value = 65;
                width.value = 2;
                displayCheck.checked = true;
                setColorPair('#000000', '#ffffff');
            }} else if (type === 'upca') {{
                symb.value = 'UPC';
                input.value = '01234567890';
                height.value = 60;
                width.value = 2;
                displayCheck.checked = true;
                setColorPair('#000000', '#ffffff');
            }}
            onSymbologyChange();
        }}

        function randomizeCode() {{
            const symb = document.getElementById('symbologySelect').value;
            const input = document.getElementById('barcodeValue');
            if (symb === 'EAN13') {{
                let s = '80'; // Prefisso GS1 Italia
                for (let i = 0; i < 10; i++) {{
                    s += Math.floor(Math.random() * 10);
                }}
                input.value = s;
            }} else if (symb === 'UPC') {{
                let s = '0';
                for (let i = 0; i < 10; i++) {{
                    s += Math.floor(Math.random() * 10);
                }}
                input.value = s;
            }} else if (symb === 'CODE39') {{
                const chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';
                let s = '';
                for (let i = 0; i < 16; i++) {{
                    s += chars.charAt(Math.floor(Math.random() * chars.length));
                }}
                input.value = s;
            }} else {{
                input.value = 'OMNI-' + Math.floor(100000 + Math.random() * 900000);
            }}
            updateBarcode();
        }}

        function setColorPair(bar, bg) {{
            document.getElementById('barColor').value = bar;
            document.getElementById('barColorText').value = bar;
            document.getElementById('bgColor').value = bg;
            document.getElementById('bgColorText').value = bg;
            updateBarcode();
        }}

        function syncColorText(target) {{
            if (target === 'bar') {{
                const val = document.getElementById('barColorText').value;
                if (/^#[0-9A-Fa-f]{{6}}$/.test(val)) {{
                    document.getElementById('barColor').value = val;
                    updateBarcode();
                }}
            }} else {{
                const val = document.getElementById('bgColorText').value;
                if (/^#[0-9A-Fa-f]{{6}}$/.test(val)) {{
                    document.getElementById('bgColor').value = val;
                    updateBarcode();
                }}
            }}
        }}

        function hexToRgb(hex) {{
            hex = hex.replace('#', '');
            if (hex.length === 3) {{
                hex = hex.split('').map(c => c + c).join('');
            }}
            const num = parseInt(hex, 16);
            return {{
                r: (num >> 16) & 255,
                g: (num >> 8) & 255,
                b: num & 255
            }};
        }}

        // GS1 Laser Spectral Reflectance at 670 nm Calculation
        function calculateReflectance670(rgb) {{
            // Red light (670 nm) is primarily reflected by Red channel and slightly by warm pigments
            const rNorm = rgb.r / 255;
            const gNorm = rgb.g / 255;
            const bNorm = rgb.b / 255;
            // 670 nm spectral response model:
            let ref = (rNorm * 0.85) + (gNorm * 0.10) + (bNorm * 0.05);
            return Math.min(1.0, Math.max(0.0, ref));
        }}

        function updateBarcode() {{
            const symb = document.getElementById('symbologySelect').value;
            let rawValue = document.getElementById('barcodeValue').value.trim();
            const barWidth = parseFloat(document.getElementById('barWidth').value);
            const barHeight = parseInt(document.getElementById('barHeight').value, 10);
            const quietZone = parseInt(document.getElementById('quietZone').value, 10);
            const displayValue = document.getElementById('displayValueCheck').checked;
            const barColor = document.getElementById('barColor').value;
            const bgColor = document.getElementById('bgColor').value;

            document.getElementById('barWidthVal').innerText = barWidth + ' px';
            document.getElementById('barHeightVal').innerText = barHeight + ' px';
            document.getElementById('quietZoneVal').innerText = quietZone + ' px';
            document.getElementById('barColorText').value = barColor;
            document.getElementById('bgColorText').value = bgColor;
            document.getElementById('barcodePreviewBox').style.backgroundColor = bgColor;

            let finalValue = rawValue;
            const statusBadge = document.getElementById('checksumStatus');

            // Handle Checksum for EAN-13 & UPC
            if (symb === 'EAN13') {{
                const cleanDigits = rawValue.replace(/\\D/g, '');
                if (cleanDigits.length === 12) {{
                    const check = calculateEan13CheckDigit(cleanDigits);
                    finalValue = cleanDigits + check;
                    statusBadge.innerText = 'Check-digit auto: ' + check;
                    statusBadge.className = 'text-[10px] font-bold text-emerald-600 bg-emerald-50 px-2 py-0.5 rounded border border-emerald-200';
                }} else if (cleanDigits.length === 13) {{
                    const check = calculateEan13CheckDigit(cleanDigits.slice(0, 12));
                    if (parseInt(cleanDigits[12], 10) === check) {{
                        statusBadge.innerText = 'Check-digit valido (' + check + ')';
                        statusBadge.className = 'text-[10px] font-bold text-emerald-600 bg-emerald-50 px-2 py-0.5 rounded border border-emerald-200';
                    }} else {{
                        statusBadge.innerText = 'Check-digit errato (atteso ' + check + ')';
                        statusBadge.className = 'text-[10px] font-bold text-rose-600 bg-rose-50 px-2 py-0.5 rounded border border-rose-200';
                    }}
                    finalValue = cleanDigits;
                }} else {{
                    statusBadge.innerText = 'Richieste 12 o 13 cifre (' + cleanDigits.length + ')';
                    statusBadge.className = 'text-[10px] font-bold text-amber-600 bg-amber-50 px-2 py-0.5 rounded border border-amber-200';
                }}
            }} else if (symb === 'UPC') {{
                const cleanDigits = rawValue.replace(/\\D/g, '');
                if (cleanDigits.length === 11) {{
                    const check = calculateUpcCheckDigit(cleanDigits);
                    finalValue = cleanDigits + check;
                    statusBadge.innerText = 'Check-digit auto: ' + check;
                    statusBadge.className = 'text-[10px] font-bold text-emerald-600 bg-emerald-50 px-2 py-0.5 rounded border border-emerald-200';
                }} else if (cleanDigits.length === 12) {{
                    const check = calculateUpcCheckDigit(cleanDigits.slice(0, 11));
                    statusBadge.innerText = 'UPC 12 cifre';
                    statusBadge.className = 'text-[10px] font-bold text-emerald-600 bg-emerald-50 px-2 py-0.5 rounded border border-emerald-200';
                    finalValue = cleanDigits;
                }}
            }} else {{
                statusBadge.innerText = symb === 'CODE39' ? 'Code 39 Alfanumerico' : 'Code 128 Standard';
                statusBadge.className = 'text-[10px] font-bold text-slate-600 bg-slate-100 px-2 py-0.5 rounded border border-slate-200';
            }}

            // Render Barcode via JsBarcode
            try {{
                JsBarcode("#barcodeSvg", finalValue, {{
                    format: symb,
                    lineColor: barColor,
                    background: bgColor,
                    width: barWidth,
                    height: barHeight,
                    displayValue: displayValue,
                    font: "JetBrains Mono, monospace",
                    fontSize: 14,
                    textMargin: 4,
                    margin: quietZone
                }});
            }} catch (err) {{
                console.warn("JsBarcode render error:", err);
            }}

            // Render GS1 Laser 670nm Simulation
            renderLaserSimulation(barColor, bgColor, symb, finalValue, barWidth, barHeight, quietZone, displayValue);
        }}

        function renderLaserSimulation(barColor, bgColor, symb, value, barWidth, barHeight, quietZone, displayValue) {{
            const rgbBar = hexToRgb(barColor);
            const rgbBg = hexToRgb(bgColor);

            const rBar = calculateReflectance670(rgbBar); // 0.0 (dark) to 1.0 (light)
            const rBg = calculateReflectance670(rgbBg);

            // In laser vision, reflectance converts to brightness seen by sensor
            // High reflectance (red/orange/yellow/white) = bright / white
            // Low reflectance (black/dark blue/green) = dark / black
            const simBgGrey = Math.round(rBg * 255);
            const simBarGrey = Math.round(rBar * 255);

            const simBgColor = `rgb(${{simBgGrey}}, ${{simBgGrey}}, ${{simBgGrey}})`;
            const simBarColor = `rgb(${{simBarGrey}}, ${{simBarGrey}}, ${{simBarGrey}})`;

            document.getElementById('laserSimBox').style.backgroundColor = simBgColor;

            try {{
                JsBarcode("#laserSimSvg", value, {{
                    format: symb,
                    lineColor: simBarColor,
                    background: simBgColor,
                    width: barWidth,
                    height: barHeight,
                    displayValue: displayValue,
                    font: "JetBrains Mono, monospace",
                    fontSize: 14,
                    textMargin: 4,
                    margin: quietZone
                }});
            }} catch (e) {{}}

            // Calculate PCS (Print Contrast Signal) = (RL - RD) / RL
            let pcs = 0;
            if (rBg > 0.01) {{
                pcs = ((rBg - rBar) / rBg) * 100;
            }}

            const pcsBadge = document.getElementById('pcsBadge');
            const verdictBox = document.getElementById('gs1VerdictBox');
            const verdictTitle = document.getElementById('gs1VerdictTitle');
            const verdictDesc = document.getElementById('gs1VerdictDesc');

            pcsBadge.innerText = 'PCS: ' + Math.max(0, Math.round(pcs)) + '%';

            // Check if bars reflect red (e.g. red bars or yellow bars)
            const barsReflectRed = rgbBar.r > 160 && (rgbBar.g < 80 || (rgbBar.r > 200 && rgbBar.g > 180));
            const bgIsTooDark = rBg < 0.45;

            if (barsReflectRed) {{
                // Red or Yellow Bars Error!
                pcsBadge.className = 'text-[10px] font-mono font-black px-2 py-0.5 rounded bg-rose-950 text-rose-300 border border-rose-700';
                verdictBox.className = 'p-3 rounded-xl bg-rose-950/90 border border-rose-500/50 text-rose-200 text-xs space-y-1';
                verdictTitle.innerHTML = '🔴 RIFIUTO CASSA — Barre Invisibili al Laser (GS1)';
                verdictDesc.innerHTML = '<strong>Errore Critico:</strong> Il colore delle barre contiene pigmenti caldi che riflettono la luce rossa a 670 nm. Lo scanner laser della cassa "vede" sia lo sfondo che le barre come bianchi omogenei: il codice a barre scompare e la lettura fallisce al 100%.';
            }} else if (bgIsTooDark) {{
                // Background too dark (e.g. Black on Dark Blue / Black on Black)
                pcsBadge.className = 'text-[10px] font-mono font-black px-2 py-0.5 rounded bg-rose-950 text-rose-300 border border-rose-700';
                verdictBox.className = 'p-3 rounded-xl bg-rose-950/90 border border-rose-500/50 text-rose-200 text-xs space-y-1';
                verdictTitle.innerHTML = '🔴 RIFIUTO CASSA — Sfondo Troppo Scuro (Assorbe 670 nm)';
                verdictDesc.innerHTML = '<strong>Errore GS1:</strong> Lo sfondo assorbe il raggio laser rosso anziché rifletterlo. Senza un fondo riflettente chiaro, il sensore ottico non può rilevare i bordi delle barre.';
            }} else if (pcs >= 75) {{
                // Conforme GS1 Ottimale
                pcsBadge.className = 'text-[10px] font-mono font-black px-2 py-0.5 rounded bg-emerald-950 text-emerald-300 border border-emerald-700';
                verdictBox.className = 'p-3 rounded-xl bg-emerald-950/80 border border-emerald-500/40 text-emerald-200 text-xs space-y-1';
                verdictTitle.innerHTML = '🟢 CONFORME GS1 — PCS Ottimale (' + Math.round(pcs) + '%)';
                verdictDesc.innerHTML = 'Contrasto spettrale perfetto secondo gli standard ufficiali GS1. Il laser a 670 nm distingue le barre con la massima ampiezza di segnale. Lettura garantita su tutti gli scanner lineari e a cassa.';
            }} else if (pcs >= 60) {{
                // Warning
                pcsBadge.className = 'text-[10px] font-mono font-black px-2 py-0.5 rounded bg-amber-950 text-amber-300 border border-amber-700';
                verdictBox.className = 'p-3 rounded-xl bg-amber-950/80 border border-amber-500/40 text-amber-200 text-xs space-y-1';
                verdictTitle.innerHTML = '🟡 ATTENZIONE GS1 — Contrasto Limite (' + Math.round(pcs) + '%)';
                verdictDesc.innerHTML = 'Il contrasto PCS è al limite minimo consentito dalle specifiche industriali. Si consiglia una prova di stampa o di aumentare l\\\opacità delle barre prima della tiratura finale.';
            }} else {{
                // Danger
                pcsBadge.className = 'text-[10px] font-mono font-black px-2 py-0.5 rounded bg-rose-950 text-rose-300 border border-rose-700';
                verdictBox.className = 'p-3 rounded-xl bg-rose-950/90 border border-rose-500/50 text-rose-200 text-xs space-y-1';
                verdictTitle.innerHTML = '🔴 NON CONFORME GS1 — Contrasto Insufficiente (' + Math.round(pcs) + '%)';
                verdictDesc.innerHTML = 'Il contrasto tra barre e sfondo è inferiore al limite GS1. Rischio concreto di blocco della lettura alle casse automatiche e restituzione delle merci.';
            }}
        }}

        function exportSvg() {{
            const svg = document.getElementById('barcodeSvg');
            if (!svg) return;
            const svgData = new XMLSerializer().serializeToString(svg);
            const blob = new Blob([svgData], {{ type: "image/svg+xml;charset=utf-8" }});
            const url = URL.createObjectURL(blob);
            const a = document.createElement('a');
            const symb = document.getElementById('symbologySelect').value;
            const val = document.getElementById('barcodeValue').value.trim() || 'barcode';
            a.href = url;
            a.download = `OmniBarcode-${{symb}}-${{val}}.svg`;
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);
            URL.revokeObjectURL(url);
        }}

        function exportPng() {{
            const svg = document.getElementById('barcodeSvg');
            if (!svg) return;
            const svgData = new XMLSerializer().serializeToString(svg);
            const canvas = document.createElement("canvas");
            const ctx = canvas.getContext("2d");
            const img = new Image();
            
            // 300 DPI multiplier (3x or 4x scale)
            const scale = 3;
            const bbox = svg.getBoundingClientRect();
            canvas.width = bbox.width * scale;
            canvas.height = bbox.height * scale;

            img.onload = function() {{
                ctx.scale(scale, scale);
                ctx.drawImage(img, 0, 0);
                const pngUrl = canvas.toDataURL("image/png");
                const a = document.createElement('a');
                const symb = document.getElementById('symbologySelect').value;
                const val = document.getElementById('barcodeValue').value.trim() || 'barcode';
                a.href = pngUrl;
                a.download = `OmniBarcode-300DPI-${{symb}}-${{val}}.png`;
                document.body.appendChild(a);
                a.click();
                document.body.removeChild(a);
            }};
            img.src = "data:image/svg+xml;base64," + btoa(unescape(encodeURIComponent(svgData)));
        }}

        function copySvgCode() {{
            const svg = document.getElementById('barcodeSvg');
            if (!svg) return;
            const svgData = new XMLSerializer().serializeToString(svg);
            navigator.clipboard.writeText(svgData).then(() => {{
                const btn = document.getElementById('copySvgBtn');
                const old = btn.innerText;
                btn.innerText = '✅ Copiato!';
                setTimeout(() => {{
                    btn.innerText = old;
                }}, 2000);
            }}).catch(() => {{
                alert('Impossibile copiare il codice SVG negli appunti.');
            }});
        }}

        function changeLanguage(lang) {{
            if (!TRANSLATIONS[lang]) return;
            currentLang = lang;
            const t = TRANSLATIONS[lang];

            document.getElementById('heroTitle').innerHTML = t.hero_title;
            document.getElementById('heroDesc').innerHTML = t.hero_desc;
            document.getElementById('symbologyLabel').innerHTML = t.symbology_label;
            document.getElementById('inputLabel').innerHTML = t.input_label;
            document.getElementById('displayValueLabel').innerHTML = t.display_value_label;
            document.getElementById('barWidthLabel').innerHTML = t.bar_width_label.split(' ')[0];
            document.getElementById('barHeightLabel').innerHTML = t.bar_height_label.split(' ')[0];
            document.getElementById('quietZoneLabel').innerHTML = t.quiet_zone_label.split(' ')[0];
            document.getElementById('colorsTitle').innerHTML = '<span>🎨</span> ' + t.colors_title;
            document.getElementById('barColorLabel').innerHTML = t.bar_color_label;
            document.getElementById('bgColorLabel').innerHTML = t.bg_color_label;
            document.getElementById('exportSvgBtn').innerHTML = t.export_svg_btn;
            document.getElementById('exportPngBtn').innerHTML = t.export_png_btn;
            document.getElementById('copySvgBtn').innerHTML = t.copy_svg_btn;
            document.getElementById('ruleTipText').innerHTML = t.rule_tip;
            document.getElementById('legalDisclaimer').innerHTML = t.legal_disclaimer;
            document.getElementById('faqTitle').innerHTML = t.faq_title;

            // Update FAQs
            document.getElementById('faq1Q').innerHTML = t.faq_1_q;
            document.getElementById('faq1A').innerHTML = t.faq_1_a;
            document.getElementById('faq2Q').innerHTML = t.faq_2_q;
            document.getElementById('faq2A').innerHTML = t.faq_2_a;
            document.getElementById('faq3Q').innerHTML = t.faq_3_q;
            document.getElementById('faq3A').innerHTML = t.faq_3_a;
            document.getElementById('faq4Q').innerHTML = t.faq_4_q;
            document.getElementById('faq4A').innerHTML = t.faq_4_a;

            updateBarcode();
        }}

        // Initialize on load
        window.addEventListener('DOMContentLoaded', () => {{
            updateBarcode();
        }});
    </script>
</body>
</html>
"""

output_path = '/Users/ilalu/Documents/Altenative Businnes/Calcolatore_Pendenza/barcode.html'
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(html_code)

print("barcode.html compiled successfully! Size:", os.path.getsize(output_path))
