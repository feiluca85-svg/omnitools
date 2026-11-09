from nav_header import render_suite_header, render_suite_header_js
from unified_footer import render_unified_footer, render_unified_footer_js
import json

with open('/Users/ilalu/Documents/Altenative Businnes/Calcolatore_Pendenza/translations_dpi.json', 'r', encoding='utf-8') as f:
    t_data = json.load(f)

t_json_str = json.dumps(t_data, ensure_ascii=False)

header_html = render_suite_header("dpi")
header_js = render_suite_header_js()
footer_html = render_unified_footer("dpi")
footer_js = render_unified_footer_js()

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
          }},
          {{
            "@type": "Question",
            "name": "Quanti megapixel servono per stampare una foto in formato A4 o A3 a 300 DPI?",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "Per un foglio A4 (21×29.7 cm) a 300 DPI servono 2480×3508 pixel (circa 8.7 Megapixel). Per un foglio A3 (29.7×42 cm) a 300 DPI occorrono 3508×4961 pixel (circa 17.4 Megapixel). Qualsiasi fotocamera recente o smartphone moderno scatta file ampiamente sufficienti per la stampa di qualità."
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
            }}
            body {{ 
                background: white !important; 
                color: #0f172a !important; 
                padding: 0 !important; 
                margin: 0 !important;
                font-size: 10pt !important; 
                line-height: 1.25 !important;
                -webkit-print-color-adjust: exact !important;
                print-color-adjust: exact !important;
            }}
            main {{ 
                max-width: 100% !important; 
                margin: 0 !important; 
                padding: 0 !important; 
            }}
            #resultsColumn {{
                width: 100% !important;
                max-width: 100% !important;
                display: block !important;
                margin: 0 !important;
                padding: 0 !important;
            }}
            .print-border {{ 
                border: 1px solid #cbd5e1 !important; 
                box-shadow: none !important;
            }}
        }}
        .print-only {{
            display: none;
        }}
    </style>
</head>
<body class="bg-slate-50 text-slate-800 font-sans antialiased min-h-screen flex flex-col justify-between selection:bg-blue-500 selection:text-white">

    <!-- Top Navigation Header with safe area padding -->
    {header_html}

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
                <div id="printHeader" class="hidden print:block mb-3 pb-2 border-b-2 border-slate-900">
                    <div class="flex items-center justify-between">
                        <div class="flex items-center gap-2.5">
                            <div class="w-10 h-10 rounded-xl bg-gradient-to-br from-rose-800 to-rose-950 flex items-center justify-center text-white shrink-0 p-1 shadow-sm" style="-webkit-print-color-adjust: exact; print-color-adjust: exact;">
                    <svg class="w-full h-full" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <circle cx="16" cy="16" r="13.2" stroke="#ffffff" stroke-width="3" />
                        <circle cx="16" cy="16" r="7.5" stroke="#ffffff" stroke-width="2.2" />
                        <line x1="16" y1="4.5" x2="16" y2="27.5" stroke="#ffffff" stroke-width="2.6" stroke-linecap="round" />
                        <line x1="4.5" y1="16" x2="27.5" y2="16" stroke="#ffffff" stroke-width="2.6" stroke-linecap="round" />
                        <circle cx="16" cy="16" r="2.2" fill="#fda4af" />
                    </svg>
                </div>
                            <div>
                                <div class="flex items-center gap-1.5 leading-none">
                                    <span class="text-base font-black tracking-tight text-slate-900 font-jakarta">Omni<span class="text-blue-600">Tools</span> Lab</span>
                                    <span class="text-[9px] font-extrabold uppercase bg-slate-100 text-slate-800 px-1.5 py-0.5 rounded border border-slate-300">SCHEDA TECNICA A4</span>
                                </div>
                                <h1 class="text-xs font-bold text-slate-700 mt-1">RisoluzioneFacile — Scheda Tecnica di Risoluzione Stampa, Megapixel & DPI</h1>
                            </div>
                        </div>
                        <div class="text-right text-[10px] text-slate-600 font-mono leading-tight">
                            <div id="printReportDate" class="font-bold text-slate-900">Data: 04/11/2026</div>
                            <div>Offset • Digitale • Acuità Visiva</div>
                            <div class="text-blue-600 font-bold">omnitoolslab.com/dpi</div>
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

                <!-- DEDICATED PRINT-ONLY TECHNICAL NOTES & SIGNATURE BOX -->
                <div id="printFooterBox" class="hidden print:block mt-3 pt-2.5 border-t border-slate-300 text-xs">
                    <div class="grid grid-cols-2 gap-4">
                        <div>
                            <span class="font-bold text-slate-800 block mb-1 text-[9px] uppercase tracking-wider">Note di Prestampa & Linee Guida File:</span>
                            <div class="border border-dashed border-slate-400 h-14 rounded-lg p-1.5 text-[8.5px] text-slate-600 leading-tight">
                                • Verificare spazio colore CMYK (Fogra 39 / Fogra 51) prima dell'invio in macchina.<br>
                                • Per immagini bitmap al tratto utilizzare preferibilmente 1200 DPI a 1 bit.
                            </div>
                        </div>
                        <div>
                            <span class="font-bold text-slate-800 block mb-1 text-[9px] uppercase tracking-wider">Visto Si Stampi / Firma Tecnico:</span>
                            <div class="border border-slate-300 h-14 rounded-lg flex items-end justify-center pb-1 text-[8.5px] text-slate-400">
                                Data, Firma Operatore Prestampa
                            </div>
                        </div>
                    </div>
                    <div class="text-[8px] text-slate-400 text-center mt-2 pt-1 border-t border-slate-200">
                        Documento tecnico generato da <strong>OmniTools Lab</strong> (https://www.omnitoolslab.com) — Precision Utilities Suite.
                    </div>
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
                <!-- FAQ Accordion Section (Unified OmniTools Lab Standard) -->
        <section id="faqSection" class="no-print bg-white rounded-3xl border border-slate-200/90 shadow-xs p-5 sm:p-7 space-y-4">
            <div class="flex items-center gap-2.5 mb-1">
                <span class="text-xl">❓</span>
                <h2 class="text-base sm:text-lg font-black text-slate-900 font-jakarta flex items-center gap-2" id="faqTitle">
                    <span>Domande Frequenti</span>
                </h2>
                <span class="text-[10px] font-extrabold uppercase px-2 py-0.5 rounded-full bg-slate-100 text-slate-600 border border-slate-200">FAQ</span>
            </div>
            
            <div id="faqContainer" class="space-y-3">
                <details class="group bg-slate-50/80 hover:bg-slate-50 rounded-2xl border border-slate-200/80 p-4 transition duration-150">
                    <summary class="flex justify-between items-center font-bold text-xs sm:text-sm text-slate-900 cursor-pointer list-none select-none">
                        <span>Qual è la vera differenza tra DPI e PPI?</span>
                        <svg class="w-4 h-4 text-slate-400 group-open:-rotate-180 transition-transform duration-200 shrink-0 ml-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/>
                        </svg>
                    </summary>
                    <div class="text-xs sm:text-sm text-slate-600 mt-2.5 leading-relaxed border-t border-slate-200/60 pt-2.5">
                        PPI (Pixels Per Inch) indica il numero di pixel per pollice su un display o in un file digitale raster. DPI (Dots Per Inch) indica il numero di punti di inchiostro fisici che una macchina da stampa o una stampante deposita sul foglio. Nel parlato comune della grafica pubblicitaria vengono spesso usati come sinonimi, ma il calcolo matematico delle dimensioni del documento si basa rigorosamente sulla formula dei PPI.
                    </div>
                </details>
                <details class="group bg-slate-50/80 hover:bg-slate-50 rounded-2xl border border-slate-200/80 p-4 transition duration-150">
                    <summary class="flex justify-between items-center font-bold text-xs sm:text-sm text-slate-900 cursor-pointer list-none select-none">
                        <span>Serve davvero inviare file a 300 DPI per manifesti 6x3 metri o striscioni?</span>
                        <svg class="w-4 h-4 text-slate-400 group-open:-rotate-180 transition-transform duration-200 shrink-0 ml-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/>
                        </svg>
                    </summary>
                    <div class="text-xs sm:text-sm text-slate-600 mt-2.5 leading-relaxed border-t border-slate-200/60 pt-2.5">
                        No, è un errore classico che genera file enormi e ingestibili da svariati Gigabyte. Più il supporto è grande, maggiore è la distanza da cui viene guardato. Un manifesto 6x3 metri visto da 5-10 metri di distanza appare nitidissimo a soli 25-35 DPI, perché il potere risolutivo dell'angolo visivo umano a quella distanza rende invisibile la griglia di stampa.
                    </div>
                </details>
                <details class="group bg-slate-50/80 hover:bg-slate-50 rounded-2xl border border-slate-200/80 p-4 transition duration-150">
                    <summary class="flex justify-between items-center font-bold text-xs sm:text-sm text-slate-900 cursor-pointer list-none select-none">
                        <span>Come si calcola la dimensione in cm conoscendo pixel e DPI?</span>
                        <svg class="w-4 h-4 text-slate-400 group-open:-rotate-180 transition-transform duration-200 shrink-0 ml-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/>
                        </svg>
                    </summary>
                    <div class="text-xs sm:text-sm text-slate-600 mt-2.5 leading-relaxed border-t border-slate-200/60 pt-2.5">
                        La formula esatta è: <code>Centimetri = (Pixel / DPI) × 2.54</code>. Ad esempio, un'immagine di 3000 pixel di larghezza a 300 DPI misurerà: (3000 / 300) × 2.54 = 25.4 cm di larghezza stampata.
                    </div>
                </details>
                <details class="group bg-slate-50/80 hover:bg-slate-50 rounded-2xl border border-slate-200/80 p-4 transition duration-150">
                    <summary class="flex justify-between items-center font-bold text-xs sm:text-sm text-slate-900 cursor-pointer list-none select-none">
                        <span>Come varia il peso del file TIFF/PSD aumentando i DPI?</span>
                        <svg class="w-4 h-4 text-slate-400 group-open:-rotate-180 transition-transform duration-200 shrink-0 ml-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/>
                        </svg>
                    </summary>
                    <div class="text-xs sm:text-sm text-slate-600 mt-2.5 leading-relaxed border-t border-slate-200/60 pt-2.5">
                        Raddoppiando i DPI (es. da 150 a 300 DPI) la superficie in pixel quadruplica (2×2 = 4 volte). Un file da 50 MB passerà istantaneamente a 200 MB. Per questo per manifesti e roll-up è opportuno non eccedere i 100-150 DPI.
                    </div>
                </details>
            </div>
        </section>

    </main>

    {footer_html}

    <script>
        const TRANSLATIONS = {t_json_str};

        {header_js}
{footer_js}


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
        let currentMode = 'direct'; // 'direct' = da px a cm, 'reverse' = da cm a px
        let currentDpi = 300;
        let currentDist = 40; // in cm

        function changeLanguage(lang) {{
            if (!TRANSLATIONS[lang]) return;
            currentLang = lang;
            localStorage.setItem('omnitools_lang', lang);
            try {{ window.dispatchEvent(new CustomEvent('omnitools_lang_changed', {{ detail: {{ lang: lang }} }})); }} catch(e) {{}}
            document.documentElement.lang = lang;
            document.getElementById('langSelect').value = lang;
            applyTranslations();
            calculateResolution();
        }}

        function applyTranslations() {{
            const t = TRANSLATIONS[currentLang];
            if (!t) return;

            if (document.getElementById('brandTitle')) document.getElementById('brandTitle').textContent = t.title;
            if (document.getElementById('brandTitleMobile')) document.getElementById('brandTitleMobile').textContent = t.title;
            if (document.getElementById('heroTitle')) document.getElementById('heroTitle').textContent = t.hero_title;
            if (document.getElementById('heroDesc')) document.getElementById('heroDesc').textContent = t.hero_desc;
            if (document.getElementById('modeDirectBtn')) document.getElementById('modeDirectBtn').textContent = t.mode_direct;
            if (document.getElementById('modeReverseBtn')) document.getElementById('modeReverseBtn').textContent = t.mode_reverse;
            if (document.getElementById('unitLabelText')) document.getElementById('unitLabelText').textContent = t.unit_label;
            if (document.getElementById('pixelsWLabel')) document.getElementById('pixelsWLabel').textContent = t.pixels_w_label;
            if (document.getElementById('pixelsHLabel')) document.getElementById('pixelsHLabel').textContent = t.pixels_h_label;
            if (document.getElementById('printWLabel')) document.getElementById('printWLabel').innerHTML = `${{t.print_w_label}} (<span class="unitBadge">${{currentUnit}}</span>)`;
            if (document.getElementById('printHLabel')) document.getElementById('printHLabel').innerHTML = `${{t.print_h_label}} (<span class="unitBadge">${{currentUnit}}</span>)`;
            if (document.getElementById('dpiTargetLabel')) document.getElementById('dpiTargetLabel').textContent = t.dpi_target_label;
            if (document.getElementById('viewDistLabel')) document.getElementById('viewDistLabel').textContent = t.view_dist_label;
            if (document.getElementById('presetsTitle')) document.getElementById('presetsTitle').textContent = t.presets_title;
            if (document.getElementById('preset1Title')) document.getElementById('preset1Title').textContent = t.preset_1;
            if (document.getElementById('preset1Sub')) document.getElementById('preset1Sub').textContent = t.preset_1_sub;
            if (document.getElementById('preset2Title')) document.getElementById('preset2Title').textContent = t.preset_2;
            if (document.getElementById('preset2Sub')) document.getElementById('preset2Sub').textContent = t.preset_2_sub;
            if (document.getElementById('preset3Title')) document.getElementById('preset3Title').textContent = t.preset_3;
            if (document.getElementById('preset3Sub')) document.getElementById('preset3Sub').textContent = t.preset_3_sub;
            if (document.getElementById('preset4Title')) document.getElementById('preset4Title').textContent = t.preset_4;
            if (document.getElementById('preset4Sub')) document.getElementById('preset4Sub').textContent = t.preset_4_sub;
            if (document.getElementById('colDimLabel')) document.getElementById('colDimLabel').textContent = t.col_dimensions;
            if (document.getElementById('colPixLabel')) document.getElementById('colPixLabel').textContent = t.col_pixels;
            if (document.getElementById('colMegaLabel')) document.getElementById('colMegaLabel').textContent = t.col_megapixels;
            if (document.getElementById('schemaTitle')) document.getElementById('schemaTitle').textContent = t.schema_title;
            if (document.getElementById('printBtnText')) document.getElementById('printBtnText').textContent = t.print_btn;
            if (document.getElementById('installBannerTitle')) document.getElementById('installBannerTitle').textContent = t.install_banner_title;
            if (document.getElementById('installBannerSub')) document.getElementById('installBannerSub').textContent = t.install_banner_sub;
            if (document.getElementById('installBannerBtn')) document.getElementById('installBannerBtn').textContent = t.install_btn;
            if (document.getElementById('legalDisclaimerText')) document.getElementById('legalDisclaimerText').innerHTML = t.legal_disclaimer;
            const fmt = document.getElementById('faqTitle') || document.getElementById('faqMainTitle'); if (fmt && t.faq_title) fmt.innerHTML = `<span>${{t.faq_title}}</span>`;
            if (document.getElementById('ruleTipText')) document.getElementById('ruleTipText').innerHTML = t.rule_tip;
            if (document.getElementById('copyBtnText')) document.getElementById('copyBtnText').textContent = t.copy_btn;

            // Update FAQs
            renderFaqs();
        }}

                function renderFaqs() {{
            const container = document.getElementById('faqContainer');
            if (!container) return;
            const t = TRANSLATIONS[currentLang] || TRANSLATIONS['it'];
            const titleElem = document.getElementById('faqTitle');
            if (titleElem && t.faq_title) {{
                titleElem.innerHTML = `<span>${{t.faq_title}}</span>`;
            }}

            let html = '';
            for (let i = 1; i <= 4; i++) {{
                const q = t[`faq_${{i}}_q`];
                const a = t[`faq_${{i}}_a`];
                if (q && a) {{
                    html += `
                    <details class="group bg-slate-50/80 hover:bg-slate-50 rounded-2xl border border-slate-200/80 p-4 transition duration-150">
                        <summary class="flex justify-between items-center font-bold text-xs sm:text-sm text-slate-900 cursor-pointer list-none select-none">
                            <span>${{q}}</span>
                            <svg class="w-4 h-4 text-slate-400 group-open:-rotate-180 transition-transform duration-200 shrink-0 ml-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/>
                            </svg>
                        </summary>
                        <div class="text-xs sm:text-sm text-slate-600 mt-2.5 leading-relaxed border-t border-slate-200/60 pt-2.5">
                            ${{a}}
                        </div>
                    </details>`;
                }}
            }}
            container.innerHTML = html;
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
            if (document.getElementById('dpiBadge')) document.getElementById('dpiBadge').textContent = currentDpi + ' DPI';
            calculateResolution();
        }}

        function setDpi(dpi) {{
            currentDpi = dpi;
            document.getElementById('dpiRange').value = dpi;
            if (document.getElementById('dpiBadge')) document.getElementById('dpiBadge').textContent = dpi + ' DPI';
            calculateResolution();
        }}

        function updateDistFromRange(val) {{
            currentDist = parseInt(val) || 40;
            if (document.getElementById('distBadge')) document.getElementById('distBadge').textContent = currentDist + ' cm';
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

            if (document.getElementById('valPrintDim')) document.getElementById('valPrintDim').textContent = `${{displayW}} × ${{displayH}}`;
            if (document.getElementById('valPrintDimIn')) document.getElementById('valPrintDimIn').textContent = `${{printW_in.toFixed(2)}} × ${{printH_in.toFixed(2)}} in (${{printW_cm.toFixed(1)}} × ${{printH_cm.toFixed(1)}} cm)`;
            if (document.getElementById('valPixelDim')) document.getElementById('valPixelDim').textContent = `${{pxW}} × ${{pxH}} px`;
            
            const ratioStr = getAspectRatioString(pxW, pxH);
            if (document.getElementById('valAspectRatio')) document.getElementById('valAspectRatio').textContent = `Ratio: ${{ratioStr}}`;
            if (document.getElementById('valMegapixels')) document.getElementById('valMegapixels').textContent = `${{megapixels.toFixed(2)}} MP`;
            if (document.getElementById('valFileSize')) document.getElementById('valFileSize').textContent = `RGB ${{rgbMB.toFixed(1)}} MB • CMYK ${{cmykMB.toFixed(1)}} MB`;

            // Update Acuity Metrics in Verdict
            if (document.getElementById('curDpiMetric')) document.getElementById('curDpiMetric').textContent = `${{dpi}} DPI`;
            if (document.getElementById('minDpiMetric')) document.getElementById('minDpiMetric').textContent = `${{minAcuityDpi}} DPI (${{currentDist}} cm)`;

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
            document.getElementById('langSelect').value = currentLang;
            document.documentElement.lang = currentLang;
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
