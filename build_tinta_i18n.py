from nav_header import render_suite_header, render_suite_header_js
from unified_footer import render_unified_footer, render_unified_footer_js
import json

with open('/Users/ilalu/Documents/Altenative Businnes/Calcolatore_Pendenza/translations_tinta.json', 'r', encoding='utf-8') as f:
    t_data = json.load(f)

t_json_str = json.dumps(t_data, ensure_ascii=False)

header_html = render_suite_header("tinta")
header_js = render_suite_header_js()
footer_html = render_unified_footer("tinta")
footer_js = render_unified_footer_js()

html_code = f"""<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0">
    <meta name="google-site-verification" content="MRdbDm9lLhokeD3I0FOpUSOhNaF_2WaveKvu52FxtG4">
    <title>TintaPerfetta — Matrice di Calibrazione Colore & Prova Stampa CMYK (Formati A4, A3, 33x48 e Bobina)</title>
    <meta name="description" content="Generatore professionale di matrici cromatiche di scarto CMYK su misura: A4, A3, SRA3 33x48 cm, formati personalizzati e strisce bobina su misura (25, 30, 33 cm).">
    
    <!-- Schema.org Structured Data (WebApplication + FAQPage) -->
    <script type="application/ld+json">
    [
      {{
        "@context": "https://schema.org",
        "@type": "WebApplication",
        "name": "TintaPerfetta — Matrice di Calibrazione CMYK",
        "url": "https://www.omnitoolslab.com/tinta",
        "applicationCategory": "DesignApplication",
        "operatingSystem": "All",
        "description": "Matrice di scarto cromatico CMYK su misura per rotative a bobina, stampanti digitali SRA3 e formati personalizzati con campionamento colore pipetta contagocce.",
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
            "name": "Perché il colore a video RGB non corrisponde mai al 100% alla stampa CMYK?",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "I monitor emettono luce RGB con un gamut più ampio, mentre la stampa sottrae luce tramite inchiostri CMYK. La finitura della carta e la macchina modificano il risultato reale."
            }}
          }},
          {{
            "@type": "Question",
            "name": "Come si usa la matrice di calibrazione TintaPerfetta?",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "Inserisci la ricetta colore stimata, stampa il file PDF vettoriale sul supporto reale con la tua macchina da stampa, confronta il tassello sotto luce D50 e imposta il codice vincente nel RIP."
            }}
          }},
          {{
            "@type": "Question",
            "name": "Cos'è il Total Area Coverage (TAC) e perché è importante?",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "Il TAC è la somma delle percentuali dei quattro canali CMYK. Per carte patinate non deve superare il 300-320%, per uso mano 260% per evitare sbavature o problemi di asciugatura."
            }}
          }}
        ]
      }}
    ]
    </script>

    <!-- Canonical & SEO Meta Tags -->
    <link rel="canonical" href="https://www.omnitoolslab.com/tinta">
    <meta name="robots" content="index, follow">
    <meta property="og:type" content="website">
    <meta property="og:title" content="TintaPerfetta — Matrice di Calibrazione Colore & Prova Stampa CMYK">
    <meta property="og:description" content="Azzeramento sprechi di avviamento su rotative a bobina e stampanti digitali a foglio. Matrice di scarto cromatico CMYK su qualsiasi formato.">
    <meta property="og:url" content="https://www.omnitoolslab.com/tinta">
    <meta property="og:site_name" content="OmniTools Lab">
    
    <!-- PWA & Mobile Icons -->
    <link rel="manifest" href="manifest-graph.json">
    <link rel="icon" type="image/svg+xml" href="favicon.svg?v=6">
    <link rel="apple-touch-icon" href="icon-graph-192.png">
    <meta name="theme-color" content="#9f1239">

    <!-- jsPDF Library for Custom Vector PDF Generation -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js"></script>

    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <script defer src="/_vercel/insights/script.js"></script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@500;700;800&display=swap" rel="stylesheet">
    
    <script>
        tailwind.config = {{
            theme: {{
                extend: {{
                    fontFamily: {{
                        sans: ['"Plus Jakarta Sans"', 'system-ui', '-apple-system', 'sans-serif'],
                        jakarta: ['"Plus Jakarta Sans"', 'sans-serif'],
                        mono: ['"JetBrains Mono"', 'monospace'],
                    }},
                    colors: {{
                        graph: {{
                            50: '#fff1f2',
                            100: '#ffe4e6',
                            200: '#fecdd3',
                            500: '#f43f5e',
                            600: '#e11d48',
                            700: '#be123c',
                            800: '#9f1239',
                            900: '#881337',
                        }}
                    }}
                }}
            }}
        }}
    </script>

    <!-- Dynamic CSS Page Style for Print -->
    <style id="dynamicPageStyle">
        @media print {{
            @page {{
                size: A4 portrait;
                margin: 5mm 6mm;
            }}
            body {{
                background: #ffffff !important;
                color: #000000 !important;
                font-size: 8.5pt !important;
                line-height: 1.15 !important;
                padding: 0 !important;
            }}
            .no-print {{
                display: none !important;
            }}
            .print-only {{
                display: block !important;
            }}
            .print-card {{
                box-shadow: none !important;
                border: 1px solid #cbd5e1 !important;
                break-inside: avoid !important;
                page-break-inside: avoid !important;
            }}
            .matrix-cell {{
                -webkit-print-color-adjust: exact !important;
                print-color-adjust: exact !important;
            }}
            #matrixContainer {{
                height: calc(100vh - 120px) !important;
                display: flex !important;
                flex-direction: column !important;
            }}
            #matrixContainer table {{
                height: 100% !important;
                width: 100% !important;
                table-layout: fixed !important;
            }}
            #matrixContainer td {{
                height: auto !important;
                padding: 2px !important;
            }}
            #matrixContainer .color-swatch-box {{
                height: 100% !important;
                min-height: 100% !important;
            }}
        }}
        .print-only {{
            display: none;
        }}
        .color-swatch-box {{
            transition: transform 0.1s ease, box-shadow 0.1s ease;
        }}
        .color-swatch-box:hover {{
            transform: scale(1.04);
            z-index: 10;
        }}
    </style>
</head>
<body class="bg-slate-50 text-slate-800 font-sans antialiased min-h-screen flex flex-col justify-between selection:bg-rose-900 selection:text-white">

    <!-- Header Navigation -->
    {header_html}

    <!-- Main Content Container -->
    <main class="max-w-5xl mx-auto px-3 sm:px-6 py-4 sm:py-6 flex-1 w-full space-y-4 sm:space-y-6">

        <!-- UNIFIED A4/CUSTOM PRINT HEADER (Shown only when printing) -->
        <div id="printHeader" class="hidden print:block mb-2 pb-2 border-b-2 border-slate-900">
            <div class="flex items-center justify-between">
                <div class="flex items-center gap-2.5">
                    <div class="w-10 h-10 rounded-xl bg-gradient-to-br from-rose-800 to-rose-950 flex items-center justify-center text-white shrink-0 p-1 shadow-sm" style="-webkit-print-color-adjust: exact; print-color-adjust: exact;">
                        <svg class="w-full h-full" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <circle cx="16" cy="16" r="13.2" stroke="#ffffff" stroke-width="2.8" />
                            <circle cx="16" cy="16" r="6" stroke="#ffffff" stroke-width="2" />
                            <line x1="16" y1="4.5" x2="16" y2="27.5" stroke="#ffffff" stroke-width="2" stroke-linecap="round" />
                            <line x1="4.5" y1="16" x2="27.5" y2="16" stroke="#ffffff" stroke-width="2" stroke-linecap="round" />
                            <circle cx="16" cy="16" r="2.2" fill="#fda4af" />
                        </svg>
                    </div>
                    <div>
                        <div class="flex items-center gap-1.5 leading-none">
                            <span class="text-base font-black tracking-tight text-slate-900 font-jakarta">Omni<span class="text-rose-800">Graph</span> Lab</span>
                            <span class="text-[9px] font-extrabold uppercase bg-slate-100 text-slate-800 px-1.5 py-0.5 rounded border border-slate-300">SCHEDA PROVA COLORE</span>
                        </div>
                        <h1 id="printSheetTitle" class="text-xs font-bold text-slate-700 mt-1">TintaPerfetta — Matrice di Calibrazione Cromatica & Compensazione Punto Macchina</h1>
                    </div>
                </div>
                <div class="text-right text-[10px] text-slate-600 font-mono leading-tight">
                    <div id="printReportDate" class="font-bold text-slate-900">Data: 04/11/2026</div>
                    <div>ISO 12647-2 • FOGRA39 / FOGRA51</div>
                    <div class="text-rose-800 font-bold">omnitoolslab.com/tinta</div>
                </div>
            </div>
            
            <!-- Metadata Strip for Press Operator -->
            <div class="mt-2 pt-1.5 border-t border-slate-200 flex items-center justify-between text-[10px] font-mono flex-wrap gap-2">
                <div><span class="font-bold text-slate-500">COMMESSA:</span> <span id="printJobName" class="font-extrabold text-slate-900">Lavoro Campione</span></div>
                <div><span class="font-bold text-slate-500">MACCHINA:</span> <span id="printPressName" class="font-extrabold text-slate-900">Rotativa a Bobina</span></div>
                <div><span class="font-bold text-slate-500">SUPPORTO:</span> <span id="printPaperName" class="font-extrabold text-slate-900">Patinata Lucida / Bobina</span></div>
                <div><span class="font-bold text-slate-500">FORMATO:</span> <span id="printFormatName" class="font-extrabold text-rose-800">33 x 48 cm</span></div>
                <div><span class="font-bold text-slate-500">PASSO:</span> <span id="printStepName" class="font-extrabold text-slate-900">±5% Standard</span></div>
            </div>
        </div>

        <!-- Hero Header -->
        <div id="heroContainer" class="no-print text-center max-w-2xl mx-auto space-y-1 sm:space-y-1.5">
            <div class="inline-flex items-center gap-1.5 px-3 py-0.5 rounded-full bg-rose-50 border border-rose-200 text-rose-800 text-xs font-bold shadow-2xs">
                <span>🎯</span> <span>Azzeramento Sprechi Carta & Avviamenti Macchina</span>
            </div>
            <h1 id="heroTitle" class="text-2xl sm:text-4xl font-extrabold text-slate-900 tracking-tight leading-tight">
                Matrice di Scarto CMYK & Prova Colore
            </h1>
            <p id="heroDesc" class="text-slate-600 text-xs sm:text-sm leading-relaxed px-2">
                Generatore di matrici cromatiche di scarto su misura. Imposta il formato esatto del foglio (A4, A3, 33x48 cm o personalizzato) o l'altezza della bobina (25, 30, 33 cm) ed esporta il file PDF pronto per il RIP.
            </p>
        </div>

        <!-- Main Workspace Grid: 2 Columns on Desktop -->
        <div class="flex flex-col lg:grid lg:grid-cols-12 gap-4 sm:gap-6 items-start">
            
            <!-- LEFT COLUMN: CONTROLS & COLOR PICKER (col-span-5) -->
            <div class="no-print w-full lg:col-span-5 space-y-4">
                
                <!-- Card 1: Baseline Target Color -->
                <div class="bg-white p-4 sm:p-5 rounded-3xl border border-slate-200/90 shadow-xs space-y-4">
                    <div class="flex items-center justify-between pb-2 border-b border-slate-100">
                        <div>
                            <h2 id="inputSectionTitle" class="font-black text-slate-900 text-sm sm:text-base">1. Colore Target di Partenza</h2>
                            <p id="inputSectionSub" class="text-[11px] text-slate-500">Inserisci i valori da ricreare o scegli un preset</p>
                        </div>
                        <div id="previewSwatch" class="w-10 h-10 rounded-2xl shadow-inner border-2 border-white ring-2 ring-slate-200 shrink-0" style="background-color: #d92638;"></div>
                    </div>

                    <!-- Presets Strip -->
                    <div>
                        <label id="presetLabel" class="text-[11px] font-bold text-slate-500 block mb-1.5">Campioni Rapidi di Riferimento</label>
                        <div class="grid grid-cols-6 gap-1.5 text-center">
                            <button type="button" onclick="setPreset(0, 100, 100, 0)" class="h-7 rounded-xl bg-[#e60000] hover:scale-105 transition shadow-2xs border border-white" title="Rosso Corsa (C0 M100 Y100 K0)"></button>
                            <button type="button" onclick="setPreset(100, 80, 10, 40)" class="h-7 rounded-xl bg-[#001f5c] hover:scale-105 transition shadow-2xs border border-white" title="Blu Notte (C100 M80 Y10 K40)"></button>
                            <button type="button" onclick="setPreset(15, 30, 95, 10)" class="h-7 rounded-xl bg-[#c99a24] hover:scale-105 transition shadow-2xs border border-white" title="Oro Caldo (C15 M30 Y95 K10)"></button>
                            <button type="button" onclick="setPreset(85, 20, 90, 40)" class="h-7 rounded-xl bg-[#12592b] hover:scale-105 transition shadow-2xs border border-white" title="Verde Bottiglia (C85 M20 Y90 K40)"></button>
                            <button type="button" onclick="setPreset(0, 65, 100, 0)" class="h-7 rounded-xl bg-[#ff6600] hover:scale-105 transition shadow-2xs border border-white" title="Arancio Reflex (C0 M65 Y100 K0)"></button>
                            <button type="button" onclick="setPreset(20, 25, 30, 15)" class="h-7 rounded-xl bg-[#9c968f] hover:scale-105 transition shadow-2xs border border-white" title="Grigio Neutro (C20 M25 Y30 K15)"></button>
                        </div>
                    </div>

                    <!-- Input Mode Toggle (3 Modes: CMYK, HEX, DROPPER) -->
                    <div class="bg-slate-100 p-1 rounded-xl grid grid-cols-3 gap-1 text-xs font-bold">
                        <button type="button" id="btnModeCmyk" onclick="switchInputMode('cmyk')" class="py-1.5 px-1 rounded-lg bg-white text-rose-900 shadow-2xs transition text-center truncate font-bold">CMYK</button>
                        <button type="button" id="btnModeHex" onclick="switchInputMode('hex')" class="py-1.5 px-1 rounded-lg text-slate-600 hover:text-slate-900 transition text-center truncate font-bold">HEX / RGB</button>
                        <button type="button" id="btnModeDropper" onclick="switchInputMode('dropper')" class="py-1.5 px-1 rounded-lg text-slate-600 hover:text-slate-900 transition text-center truncate font-bold inline-flex items-center justify-center gap-1">
                            <span>💧</span> <span id="labelModeDropper">Pipetta & Foto</span>
                        </button>
                    </div>
<!-- CMYK Sliders Group -->
                    <div id="cmykControlsGroup" class="space-y-2.5">
                        <!-- Cyan -->
                        <div>
                            <div class="flex justify-between text-xs font-bold mb-1">
                                <span class="text-cyan-700">Ciano (C)</span>
                                <span class="font-mono" id="cValText">0%</span>
                            </div>
                            <input type="range" id="cSlider" min="0" max="100" value="0" oninput="onCmykChange()" class="w-full h-2 bg-slate-200 rounded-lg appearance-none cursor-pointer accent-cyan-600">
                        </div>
                        <!-- Magenta -->
                        <div>
                            <div class="flex justify-between text-xs font-bold mb-1">
                                <span class="text-pink-600">Magenta (M)</span>
                                <span class="font-mono" id="mValText">90%</span>
                            </div>
                            <input type="range" id="mSlider" min="0" max="100" value="90" oninput="onCmykChange()" class="w-full h-2 bg-slate-200 rounded-lg appearance-none cursor-pointer accent-pink-600">
                        </div>
                        <!-- Yellow -->
                        <div>
                            <div class="flex justify-between text-xs font-bold mb-1">
                                <span class="text-amber-600">Giallo (Y)</span>
                                <span class="font-mono" id="yValText">90%</span>
                            </div>
                            <input type="range" id="ySlider" min="0" max="100" value="90" oninput="onCmykChange()" class="w-full h-2 bg-slate-200 rounded-lg appearance-none cursor-pointer accent-amber-500">
                        </div>
                        <!-- Black -->
                        <div>
                            <div class="flex justify-between text-xs font-bold mb-1">
                                <span class="text-slate-800">Nero (K)</span>
                                <span class="font-mono" id="kValText">0%</span>
                            </div>
                            <input type="range" id="kSlider" min="0" max="100" value="0" oninput="onCmykChange()" class="w-full h-2 bg-slate-200 rounded-lg appearance-none cursor-pointer accent-slate-800">
                        </div>
                    </div>

                    <!-- HEX Group (Hidden by default) -->
                    <div id="hexControlsGroup" class="hidden space-y-2">
                        <label id="hexLabel" class="text-xs font-bold text-slate-700 block">Codice Colore (HEX o RGB)</label>
                        <div class="flex items-center gap-2">
                            <input type="color" id="nativeColorPicker" value="#d92638" onchange="onColorPickerChange(this.value)" class="w-10 h-10 rounded-xl border border-slate-300 p-0.5 cursor-pointer shrink-0">
                            <input type="text" id="hexInput" value="#D92638" oninput="onHexInputChange(this.value)" class="flex-1 p-2 font-mono text-sm uppercase font-bold border border-slate-300 rounded-xl focus:border-rose-700 focus:outline-none">
                            <button type="button" onclick="triggerNativeEyeDropper()" class="p-2.5 rounded-xl bg-slate-100 hover:bg-rose-50 text-slate-700 hover:text-rose-800 border border-slate-300 transition shrink-0" title="Pipetta Schermo Intero">
                                💧
                            </button>
                        </div>
                    </div>

                    <!-- DROPPER & IMAGE CONTROLS GROUP (Hidden by default) -->
                    <div id="dropperControlsGroup" class="hidden space-y-3">
                        <!-- Native EyeDropper API Button (Screen/Desktop) -->
                        <div>
                            <button type="button" id="btnNativeEyeDropper" onclick="triggerNativeEyeDropper()" class="w-full py-2.5 px-3 bg-gradient-to-r from-rose-900 to-rose-800 hover:from-rose-950 hover:to-rose-900 text-white font-bold text-xs rounded-xl shadow-xs transition flex items-center justify-center gap-2 cursor-pointer active:scale-98">
                                <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                                    <path d="m14 2-8.5 8.5a2.12 2.12 0 0 0-.6 1.5V16l-3.5 3.5a1 1 0 0 0 1.4 1.4L6.3 17.4h3.9c.56 0 1.1-.22 1.5-.6L20.2 8.3a2.12 2.12 0 0 0 0-3L18.7 3.8a2.12 2.12 0 0 0-3 0z"/>
                                    <path d="m14 6 4 4"/>
                                </svg>
                                <span id="dropperBtnScreen">Pipetta Schermo Intero (Qualsiasi App)</span>
                            </button>
                            <p class="text-[10px] text-slate-500 mt-1 text-center">Campiona direttamente un pixel da qualsiasi finestra o foto aperta sullo schermo.</p>
                        </div>

                        <!-- Image Upload / Dropzone / Paste Area -->
                        <div class="relative">
                            <input type="file" id="imageFileInput" accept="image/*" class="hidden" onchange="handleImageFileUpload(event)">
                            <div id="imageDropzone" onclick="document.getElementById('imageFileInput').click()" class="border-2 border-dashed border-rose-300 hover:border-rose-500 bg-rose-50/50 hover:bg-rose-50 p-4 rounded-2xl text-center cursor-pointer transition flex flex-col items-center justify-center gap-1.5 group">
                                <div class="w-10 h-10 rounded-xl bg-white shadow-2xs border border-rose-200 flex items-center justify-center text-rose-800 group-hover:scale-105 transition">
                                    <svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                        <rect width="18" height="18" x="3" y="3" rx="2" ry="2"/>
                                        <circle cx="9" cy="9" r="2"/>
                                        <path d="m21 15-3.086-3.086a2 2 0 0 0-2.828 0L6 21"/>
                                    </svg>
                                </div>
                                <span id="dropperDropzoneTitle" class="text-xs font-bold text-slate-800">Trascina qui l'immagine o Incolla (Ctrl+V)</span>
                                <span id="dropperDropzoneSub" class="text-[10px] text-slate-500 max-w-xs">Carica foto cliente, catalogo o logo per estrarre la tinta esatta</span>
                            </div>
                        </div>

                        <!-- Interactive Image Canvas Area with Loupe Magnifier -->
                        <div id="imageSamplerArea" class="hidden space-y-2">
                            <div class="flex items-center justify-between text-[11px]">
                                <span id="dropperCanvasHint" class="font-bold text-slate-700">🔍 Clicca sull'immagine per campionare il colore</span>
                                <button type="button" onclick="clearLoadedImage()" class="text-rose-700 hover:underline font-bold text-[10px]">Rimuovi</button>
                            </div>
                            
                            <div class="relative overflow-hidden rounded-xl border border-slate-200 bg-slate-900/5 flex items-center justify-center max-h-60 select-none">
                                <canvas id="samplerCanvas" class="max-w-full max-h-60 object-contain cursor-crosshair"></canvas>
                                
                                <!-- Magnifier Loupe Floating Ring -->
                                <div id="magnifierLoupe" class="hidden absolute pointer-events-none w-20 h-20 rounded-full border-2 border-white shadow-2xl overflow-hidden ring-2 ring-slate-900/40 z-20" style="transform: translate(-50%, -50%);">
                                    <canvas id="loupeCanvas" width="80" height="80" class="w-full h-full"></canvas>
                                    <div class="absolute inset-0 flex items-center justify-center pointer-events-none">
                                        <div class="w-1.5 h-1.5 rounded-full bg-white ring-1 ring-black"></div>
                                    </div>
                                </div>
                            </div>

                            <!-- Live Hovered Pixel Info Strip -->
                            <div id="pixelHoverStrip" class="p-2 rounded-xl bg-slate-900 text-white flex items-center justify-between text-xs font-mono">
                                <div class="flex items-center gap-2">
                                    <div id="hoverColorBox" class="w-5 h-5 rounded-md border border-white/40 shrink-0" style="background-color: #d92638;"></div>
                                    <span id="hoverHexText" class="font-bold">#D92638</span>
                                </div>
                                <div id="hoverCmykText" class="text-[10px] text-slate-300">C:0 M:90 Y:90 K:0</div>
                            </div>
                        </div>

                        <!-- Picked Confirmation Toast -->
                        <div id="pickedToast" class="hidden p-2.5 rounded-xl bg-emerald-50 border border-emerald-200 text-emerald-800 text-xs font-bold flex items-center gap-2">
                            <span class="text-sm">✓</span> <span id="pickedToastText">Colore campionato con successo</span>
                        </div>
                    </div>
<!-- TAC (Total Area Coverage) indicator -->
                    <div class="p-2.5 rounded-xl bg-slate-50 border border-slate-200 flex items-center justify-between text-xs">
                        <div class="flex items-center gap-1.5">
                            <span class="font-bold text-slate-700">Somma Inchiostri (TAC):</span>
                            <span id="tacValue" class="font-mono font-black text-slate-900">180%</span>
                        </div>
                        <span id="tacStatusBadge" class="text-[10px] font-bold px-2 py-0.5 rounded-md bg-emerald-50 text-emerald-700 border border-emerald-200">Sicuro</span>
                    </div>
                </div>

                <!-- Card 2: Professional Media & Custom Size Dimensions -->
                <div class="bg-white p-4 sm:p-5 rounded-3xl border border-slate-200/90 shadow-xs space-y-4">
                    <div class="flex items-center justify-between pb-2 border-b border-slate-100">
                        <h2 id="configSectionTitle" class="font-black text-slate-900 text-sm sm:text-base">2. Formato Foglio & Bobina</h2>
                        <span id="liveSizeIndicator" class="text-[10px] font-extrabold px-2 py-0.5 rounded-md bg-rose-50 text-rose-800 border border-rose-200 font-mono">33.0 × 48.0 cm</span>
                    </div>

                    <!-- Feed Type Toggle (Sheet vs Continuous Web) -->
                    <div>
                        <label id="supportTypeLabel" class="text-xs font-bold text-slate-700 block mb-1.5">Tipo di Supporto Stampa</label>
                        <div class="grid grid-cols-2 gap-2 text-xs font-bold">
                            <button type="button" id="btnFeedSheet" onclick="switchFeedType('sheet')" class="py-2 px-2 rounded-xl bg-rose-900 text-white shadow-2xs transition">
                                📄 Foglio Singolo
                            </button>
                            <button type="button" id="btnFeedRoll" onclick="switchFeedType('roll')" class="py-2 px-2 rounded-xl bg-slate-100 hover:bg-slate-200 text-slate-700 border border-slate-200 transition">
                                🎞️ Nastro / Bobina
                            </button>
                        </div>
                    </div>

                    <!-- 1. SHEET CONTROLS (Active by default) -->
                    <div id="sheetOptionsGroup" class="space-y-3">
                        <div>
                            <label id="sheetFormatLabel" class="text-xs font-bold text-slate-700 block mb-1">Formato Foglio</label>
                            <select id="sheetPresetSelect" onchange="onSheetPresetChange()" class="w-full bg-slate-50 border border-slate-200 rounded-xl p-2 text-xs font-bold text-slate-800 cursor-pointer focus:outline-none focus:border-rose-700">
                                <option value="A4">A4 (21.0 × 29.7 cm)</option>
                                <option value="A3">A3 (29.7 × 42.0 cm)</option>
                                <option value="SRA3" selected>SRA3 / 33×48 (33.0 × 48.0 cm)</option>
                                <option value="CUSTOM">Personalizzato (cm)...</option>
                            </select>
                        </div>

                        <!-- Custom Sheet Dimensions Input (Shown when CUSTOM) -->
                        <div id="customSheetInputs" class="grid grid-cols-2 gap-2 text-xs">
                            <div>
                                <span id="widthCmLabel" class="font-bold text-slate-600 block mb-0.5">Base (cm)</span>
                                <input type="number" id="sheetWidthInput" value="33.0" step="0.5" min="10" max="200" oninput="onCustomDimensionsChange()" class="w-full p-2 bg-slate-50 border border-slate-200 rounded-xl font-mono font-bold text-slate-900 focus:outline-none focus:border-rose-700">
                            </div>
                            <div>
                                <span id="heightCmLabel" class="font-bold text-slate-600 block mb-0.5">Altezza (cm)</span>
                                <input type="number" id="sheetHeightInput" value="48.0" step="0.5" min="10" max="200" oninput="onCustomDimensionsChange()" class="w-full p-2 bg-slate-50 border border-slate-200 rounded-xl font-mono font-bold text-slate-900 focus:outline-none focus:border-rose-700">
                            </div>
                        </div>

                        <!-- Orientation -->
                        <div>
                            <label id="orientationLabel" class="text-xs font-bold text-slate-700 block mb-1">Orientamento</label>
                            <div class="grid grid-cols-2 gap-2 text-xs font-bold">
                                <button type="button" id="btnOrientP" onclick="setOrientation('portrait')" class="py-1.5 px-2 rounded-xl bg-rose-50 text-rose-900 border border-rose-200 transition">Verticale (Portrait)</button>
                                <button type="button" id="btnOrientL" onclick="setOrientation('landscape')" class="py-1.5 px-2 rounded-xl bg-slate-100 text-slate-700 border border-slate-200 transition">Orizzontale (Landscape)</button>
                            </div>
                        </div>
                    </div>

                    <!-- 2. CONTINUOUS ROLL CONTROLS (Hidden by default) -->
                    <div id="rollOptionsGroup" class="hidden space-y-3">
                        <div>
                            <label id="rollWidthLabel" class="text-xs font-bold text-slate-700 block mb-1">Larghezza Bobina (Passaggio Carta)</label>
                            <select id="rollWidthSelect" onchange="onRollPresetChange()" class="w-full bg-slate-50 border border-slate-200 rounded-xl p-2 text-xs font-bold text-slate-800 cursor-pointer focus:outline-none focus:border-rose-700">
                                <option value="25">25 cm (250 mm)</option>
                                <option value="30">30 cm (300 mm)</option>
                                <option value="33" selected>33 cm (330 mm)</option>
                                <option value="50">50 cm (500 mm)</option>
                                <option value="CUSTOM">Altra Larghezza Personalizzata...</option>
                            </select>
                        </div>

                        <!-- Custom Roll Width Input -->
                        <div id="customRollWidthInput" class="hidden text-xs">
                            <span class="font-bold text-slate-600 block mb-0.5">Larghezza Bobina Personalizzata (cm)</span>
                            <input type="number" id="rollCustomWidthVal" value="33.0" step="0.5" min="10" max="320" oninput="onCustomDimensionsChange()" class="w-full p-2 bg-slate-50 border border-slate-200 rounded-xl font-mono font-bold text-slate-900 focus:outline-none focus:border-rose-700">
                        </div>

                        <!-- Rows of Control Samples along Roll Feed -->
                        <div>
                            <div class="flex items-center justify-between mb-1">
                                <label id="rollRowsLabel" class="text-xs font-bold text-slate-700">Righe di Controllo (Avanzamento Bobina)</label>
                                <span id="rollAdvanceEstimate" class="text-[10px] font-mono font-bold text-rose-800 bg-rose-50 px-1.5 py-0.5 rounded border border-rose-200">36 campioni • 16.5 cm</span>
                            </div>
                            <select id="rollRowsSelect" onchange="onRollRowsChange()" class="w-full bg-slate-50 border border-slate-200 rounded-xl p-2 text-xs font-bold text-slate-800 cursor-pointer focus:outline-none focus:border-rose-700">
                                <option value="1">1 Riga (Campione Singolo in Linea — Avanzamento ~6 cm)</option>
                                <option value="2">2 Righe (18 Campioni — Avanzamento ~9.5 cm)</option>
                                <option value="3">3 Righe (27 Campioni — Avanzamento ~13.0 cm)</option>
                                <option value="4" selected>4 Righe (36 Campioni — Avanzamento ~16.5 cm • Consigliato)</option>
                                <option value="5">5 Righe (45 Campioni — Avanzamento ~20.0 cm)</option>
                                <option value="6">6 Righe (54 Campioni — Avanzamento ~23.5 cm • Ampio Spettro)</option>
                            </select>
                        </div>
                    </div>

                    <!-- Sensitivity Step -->
                    <div class="pt-1 border-t border-slate-100">
                        <label id="stepLabel" class="text-xs font-bold text-slate-700 block mb-1">Passo di Scarto (Sensibilità)</label>
                        <div class="grid grid-cols-3 gap-1.5 text-xs font-bold">
                            <button type="button" onclick="setStep(2)" id="step2Btn" class="py-1.5 px-2 rounded-xl bg-slate-100 hover:bg-slate-200 text-slate-700 border border-slate-200 transition">±2% Fine</button>
                            <button type="button" onclick="setStep(5)" id="step5Btn" class="py-1.5 px-2 rounded-xl bg-rose-900 text-white shadow-2xs transition">±5% Medio</button>
                            <button type="button" onclick="setStep(10)" id="step10Btn" class="py-1.5 px-2 rounded-xl bg-slate-100 hover:bg-slate-200 text-slate-700 border border-slate-200 transition">±10% Ampio</button>
                        </div>
                    </div>

                    <!-- Job Metadata Inputs -->
                    <div class="space-y-2 pt-1 border-t border-slate-100 text-xs">
                        <div>
                            <span id="jobNameLabel" class="font-bold text-slate-600 block mb-0.5">Cliente / Commessa</span>
                            <input type="text" id="jobInput" value="Test Colore Etichetta" oninput="updatePrintMetadata()" placeholder="Es. Olio Extravergine" class="w-full p-2 bg-slate-50 border border-slate-200 rounded-xl text-xs font-medium focus:outline-none focus:border-rose-700">
                        </div>
                        <div class="grid grid-cols-2 gap-2">
                            <div>
                                <span id="jobPressLabel" class="font-bold text-slate-600 block mb-0.5">Macchina Stampa</span>
                                <input type="text" id="pressInput" value="Rotativa a Bobina" oninput="updatePrintMetadata()" placeholder="Es. Macchina Stampa" class="w-full p-2 bg-slate-50 border border-slate-200 rounded-xl text-xs font-medium focus:outline-none focus:border-rose-700">
                            </div>
                            <div>
                                <span id="jobPaperLabel" class="font-bold text-slate-600 block mb-0.5">Supporto / Carta</span>
                                <input type="text" id="paperInput" value="PP Bianco Lucido" oninput="updatePrintMetadata()" placeholder="Es. Patinata / Bobina" class="w-full p-2 bg-slate-50 border border-slate-200 rounded-xl text-xs font-medium focus:outline-none focus:border-rose-700">
                            </div>
                        </div>
                    </div>

                </div>

            </div>

            <!-- RIGHT COLUMN: INTERACTIVE MATRIX & INSPECTOR (col-span-7) -->
            <div class="w-full lg:col-span-7 space-y-4">
                
                <!-- Main Calibration Matrix Card -->
                <div class="bg-white p-3.5 sm:p-5 rounded-3xl border border-slate-200/90 shadow-xs space-y-3.5 print-card">
                    <div class="flex items-center justify-between no-print flex-wrap gap-2">
                        <div>
                            <h2 id="gridTitle" class="font-black text-slate-900 text-sm sm:text-base">Matrice di Calibrazione Generata</h2>
                            <p id="gridSub" class="text-[11px] text-slate-500">Stampa o scarica il file vettoriale su misura reale con crocini</p>
                        </div>
                        
                        <!-- Dual Action Buttons: Download PDF + Print -->
                        <div class="flex items-center gap-2">
                            <button type="button" onclick="downloadVectorPdf()" class="px-3.5 py-2 bg-rose-900 hover:bg-rose-950 active:scale-95 text-white font-bold text-xs rounded-xl shadow-xs transition inline-flex items-center gap-1.5 cursor-pointer">
                                <span>📥</span> <span>Scarica PDF Vettoriale</span>
                            </button>
                            <button type="button" onclick="window.print()" class="px-3 py-2 bg-slate-100 hover:bg-slate-200 active:scale-95 text-slate-700 font-bold text-xs rounded-xl border border-slate-200 transition inline-flex items-center gap-1.5 cursor-pointer" title="Stampa Diretta">
                                <span>🖨️</span> <span id="btnPrintMatrix">Stampa</span>
                            </button>
                        </div>
                    </div>

                    <!-- Instructions Bar in Print -->
                    <div class="print-only mb-2 p-2 bg-slate-50 border border-slate-300 rounded-lg text-[9pt] leading-tight text-slate-700">
                        <strong class="text-slate-900">Istruzioni Operatore Macchina:</strong> 1) Stampa il presente file sul supporto effettivo di commessa; 2) Appoggia il campione originale alla luce standard D50; 3) Scegli il tassello coincidente ed imposta la ricetta CMYK nel RIP.
                    </div>

                    <!-- DYNAMIC MATRIX GRID CONTAINER -->
                    <div id="matrixContainer" class="overflow-x-auto pb-2">
                        <!-- Filled by JS -->
                    </div>

                    <!-- Legend / Center Swatch Notice -->
                    <div class="flex items-center justify-between text-[11px] text-slate-500 pt-2 border-t border-slate-100 flex-wrap gap-2">
                        <div class="flex items-center gap-2">
                            <span class="inline-block w-3.5 h-3.5 rounded border-2 border-amber-500 bg-amber-100 shrink-0"></span>
                            <span class="font-bold text-slate-700">Bordo Dorato: Colore Base di Partenza</span>
                        </div>
                        <div class="font-mono text-[10px]" id="matrixDimFooter">
                            Dimensioni: 33.0 × 48.0 cm • FOGRA39
                        </div>
                    </div>
                </div>

                <!-- Inspector / Selected Tile Details (no-print) -->
                <div id="inspectorCard" class="no-print bg-white p-4 sm:p-5 rounded-3xl border-2 border-rose-900/30 shadow-xs space-y-3">
                    <div class="flex items-center justify-between pb-2 border-b border-slate-100 flex-wrap gap-2">
                        <div class="flex items-center gap-2.5">
                            <div id="inspectorSwatch" class="w-9 h-9 rounded-xl shadow-inner border border-slate-300 shrink-0"></div>
                            <div>
                                <h3 id="inspectorTitle" class="font-black text-slate-900 text-sm">Tassello Selezionato: <span id="inspectorCoord" class="text-rose-800">C4 (Centro)</span></h3>
                                <span id="inspectorTac" class="text-[10px] font-bold text-slate-500 font-mono">TAC: 180%</span>
                            </div>
                        </div>
                        <div class="flex items-center gap-1.5">
                            <button type="button" onclick="recenterOnSelected()" id="btnRecenter" class="px-3 py-1.5 bg-rose-50 hover:bg-rose-100 text-rose-900 font-bold text-xs rounded-xl border border-rose-200 transition cursor-pointer" title="Ricalcola la matrice usando questo colore come centro">
                                🔍 <span id="btnRecenterText">Zoom su Questo</span>
                            </button>
                            <button type="button" onclick="copyRecipe()" class="px-3 py-1.5 bg-slate-900 hover:bg-slate-800 text-white font-bold text-xs rounded-xl transition cursor-pointer" title="Copia valori CMYK per il RIP">
                                📋 <span id="btnCopyText">Copia Ricetta</span>
                            </button>
                        </div>
                    </div>

                    <!-- Values Breakdown -->
                    <div class="grid grid-cols-4 gap-2 text-center text-xs">
                        <div class="p-2 rounded-xl bg-cyan-50 border border-cyan-200">
                            <span class="text-[10px] font-bold text-cyan-800 block">Ciano</span>
                            <span id="inspectC" class="font-mono font-black text-slate-900 text-sm">0%</span>
                        </div>
                        <div class="p-2 rounded-xl bg-pink-50 border border-pink-200">
                            <span class="text-[10px] font-bold text-pink-800 block">Magenta</span>
                            <span id="inspectM" class="font-mono font-black text-slate-900 text-sm">90%</span>
                        </div>
                        <div class="p-2 rounded-xl bg-amber-50 border border-amber-200">
                            <span class="text-[10px] font-bold text-amber-800 block">Giallo</span>
                            <span id="inspectY" class="font-mono font-black text-slate-900 text-sm">90%</span>
                        </div>
                        <div class="p-2 rounded-xl bg-slate-100 border border-slate-200">
                            <span class="text-[10px] font-bold text-slate-800 block">Nero</span>
                            <span id="inspectK" class="font-mono font-black text-slate-900 text-sm">0%</span>
                        </div>
                    </div>
                </div>

            </div>

        </div>

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
                        <span>Perché il colore a video RGB non corrisponde mai al 100% alla stampa CMYK?</span>
                        <svg class="w-4 h-4 text-slate-400 group-open:-rotate-180 transition-transform duration-200 shrink-0 ml-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/>
                        </svg>
                    </summary>
                    <div class="text-xs sm:text-sm text-slate-600 mt-2.5 leading-relaxed border-t border-slate-200/60 pt-2.5">
                        I monitor emettono luce additiva (RGB) con un gamut di colori molto più esteso, mentre la stampa sottrae luce tramite inchiostri fisici su carta (CMYK). Inoltre la porosità della carta, la laminazione (lucida/opaca) e il tipo di macchina da stampa modificano sensibilmente la resa finale.
                    </div>
                </details>
                <details class="group bg-slate-50/80 hover:bg-slate-50 rounded-2xl border border-slate-200/80 p-4 transition duration-150">
                    <summary class="flex justify-between items-center font-bold text-xs sm:text-sm text-slate-900 cursor-pointer list-none select-none">
                        <span>Come si usa la matrice di calibrazione TintaPerfetta?</span>
                        <svg class="w-4 h-4 text-slate-400 group-open:-rotate-180 transition-transform duration-200 shrink-0 ml-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/>
                        </svg>
                    </summary>
                    <div class="text-xs sm:text-sm text-slate-600 mt-2.5 leading-relaxed border-t border-slate-200/60 pt-2.5">
                        Inserisci la tua ricetta colore stimata (o campionala con la pipetta). Seleziona il formato del tuo supporto (foglio o nastro bobina) e stampa il file PDF vettoriale direttamente sulla macchina da stampa con la carta definitiva della commessa. Appoggia il campione originale alla luce naturale o cabina D50, trova il tassello perfetto e inserisci la ricetta corrispondente nel tuo RIP.
                    </div>
                </details>
                <details class="group bg-slate-50/80 hover:bg-slate-50 rounded-2xl border border-slate-200/80 p-4 transition duration-150">
                    <summary class="flex justify-between items-center font-bold text-xs sm:text-sm text-slate-900 cursor-pointer list-none select-none">
                        <span>Cosa significa passo di sensibilità ±2%, ±5% o ±10%?</span>
                        <svg class="w-4 h-4 text-slate-400 group-open:-rotate-180 transition-transform duration-200 shrink-0 ml-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/>
                        </svg>
                    </summary>
                    <div class="text-xs sm:text-sm text-slate-600 mt-2.5 leading-relaxed border-t border-slate-200/60 pt-2.5">
                        Rappresenta la variazione percentuale di inchiostro tra una casella e la successiva. ±10% serve per una sgrossatura rapida quando il colore è lontano; ±5% è il passo standard di precisione; ±2% è ideale per rifiniture micrometriche su tonalità critiche come incarnati o tinte istituzionali.
                    </div>
                </details>
                <details class="group bg-slate-50/80 hover:bg-slate-50 rounded-2xl border border-slate-200/80 p-4 transition duration-150">
                    <summary class="flex justify-between items-center font-bold text-xs sm:text-sm text-slate-900 cursor-pointer list-none select-none">
                        <span>Cos'è il Total Area Coverage (TAC) e perché è importante?</span>
                        <svg class="w-4 h-4 text-slate-400 group-open:-rotate-180 transition-transform duration-200 shrink-0 ml-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/>
                        </svg>
                    </summary>
                    <div class="text-xs sm:text-sm text-slate-600 mt-2.5 leading-relaxed border-t border-slate-200/60 pt-2.5">
                        Il TAC è la somma delle percentuali dei quattro canali CMYK (C+M+Y+K). Per carte patinate non dovrebbe superare il 300-320%, mentre per carte uso mano o giornale è raccomandato non superare il 260-280% per evitare sbavature, problemi di asciugatura e controstampa.
                    </div>
                </details>
            </div>
        </section>

        <!-- Social Share & Viral Strip -->
        <div class="no-print bg-white p-4 rounded-3xl border border-slate-200 shadow-xs flex flex-col sm:flex-row items-center justify-between gap-3.5 text-center sm:text-left mt-6">
            <div class="flex items-center gap-3">
                <span class="text-2xl">📢</span>
                <div>
                    <span id="shareTitleText" class="text-xs sm:text-sm font-bold text-slate-900 block">Ti è utile TintaPerfetta?</span>
                    <span id="shareSubText" class="text-[11px] text-slate-500 block">Condividilo con il tuo reparto stampa, tipografi o colleghi grafici</span>
                </div>
            </div>
            <div class="flex items-center gap-2 flex-wrap justify-center shrink-0">
                <button type="button" onclick="shareWhatsApp()" class="inline-flex items-center gap-1.5 px-3.5 py-2 bg-emerald-600 hover:bg-emerald-500 active:scale-95 text-white text-xs font-bold rounded-xl transition shadow-xs" title="Condividi su WhatsApp">
                    <span>💬</span> <span>WhatsApp</span>
                </button>
                <button type="button" onclick="shareLinkedIn()" class="inline-flex items-center gap-1.5 px-3.5 py-2 bg-[#0a66c2] hover:bg-[#004182] active:scale-95 text-white text-xs font-bold rounded-xl transition shadow-xs" title="Condividi su LinkedIn">
                    <span>💼</span> <span>LinkedIn</span>
                </button>
                <button type="button" onclick="copyCurrentUrl()" class="inline-flex items-center gap-1.5 px-3.5 py-2 bg-slate-100 hover:bg-slate-200 active:scale-95 text-slate-700 text-xs font-bold rounded-xl border border-slate-200 transition" title="Copia Link">
                    <span>🔗</span> <span id="shareCopyText">Copia Link</span>
                </button>
            </div>
        </div>

    </main>

    {footer_html}

    <script>
{footer_js}
        const TRANSLATIONS = {t_json_str};

        {header_js}


        function detectInitialLanguage() {{
            const saved = localStorage.getItem('omnitools_lang');
            if (saved && TRANSLATIONS[saved]) return saved;
            const langs = navigator.languages || [navigator.language || 'it'];
            for (const l of langs) {{
                const code = l.toLowerCase().split('-')[0];
                if (TRANSLATIONS[code]) return code;
            }}
            return 'en';
        }}

        let currentLang = detectInitialLanguage();

        // State
        let baseC = 0;
        let baseM = 90;
        let baseY = 90;
        let baseK = 0;
        let currentStep = 5; // ±5%
        let selectedCell = null; // {{ c, m, y, k, coord, tac, hex }}

        // Media & Dimension State
        let feedType = 'sheet'; // 'sheet' or 'roll'
        let sheetPreset = 'SRA3';
        let rollWidthPreset = '33';
        let stripHeightPreset = '8';
        let orientation = 'portrait'; // 'portrait' or 'landscape'

        // Physical dimensions in millimeters
        let currentWidthMm = 330;
        let currentHeightMm = 480;

        // Helpers: CMYK ⇄ RGB Approximation (Screen Simulation)
        function cmykToRgb(c, m, y, k) {{
            const r = Math.round(255 * (1 - c / 100) * (1 - k / 100));
            const g = Math.round(255 * (1 - m / 100) * (1 - k / 100));
            const b = Math.round(255 * (1 - y / 100) * (1 - k / 100));
            return {{ r: Math.max(0, Math.min(255, r)), g: Math.max(0, Math.min(255, g)), b: Math.max(0, Math.min(255, b)) }};
        }}

        function rgbToHex(r, g, b) {{
            return '#' + [r, g, b].map(x => {{
                const hex = x.toString(16);
                return hex.length === 1 ? '0' + hex : hex;
            }}).join('');
        }}

        function hexToRgb(hex) {{
            hex = hex.replace(/^#/, '');
            if (hex.length === 3) hex = hex.split('').map(x => x + x).join('');
            const num = parseInt(hex, 16);
            return {{ r: (num >> 16) & 255, g: (num >> 8) & 255, b: num & 255 }};
        }}

        function rgbToCmyk(r, g, b) {{
            const rPrime = r / 255;
            const gPrime = g / 255;
            const bPrime = b / 255;
            const k = 1 - Math.max(rPrime, gPrime, bPrime);
            if (k === 1) return {{ c: 0, m: 0, y: 0, k: 100 }};
            const c = Math.round(((1 - rPrime - k) / (1 - k)) * 100);
            const m = Math.round(((1 - gPrime - k) / (1 - k)) * 100);
            const y = Math.round(((1 - bPrime - k) / (1 - k)) * 100);
            return {{ c: Math.max(0, c), m: Math.max(0, m), y: Math.max(0, y), k: Math.round(k * 100) }};
        }}

        function clamp(val, min = 0, max = 100) {{
            return Math.max(min, Math.min(max, Math.round(val)));
        }}

        // Language Switcher
        function changeLanguage(lang) {{
            if (!TRANSLATIONS[lang]) lang = 'en';
            currentLang = lang;
            localStorage.setItem('omnitools_lang', lang);
            document.getElementById('langSelect').value = lang;
            document.documentElement.lang = lang;
            applyTranslations();
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
        function applyTranslations() {{
            renderFaqs();
            const t = TRANSLATIONS[currentLang] || TRANSLATIONS['it'];
            if (t.hero_title) if (document.getElementById('heroTitle')) document.getElementById('heroTitle').textContent = t.hero_title;
            if (t.hero_desc) if (document.getElementById('heroDesc')) document.getElementById('heroDesc').textContent = t.hero_desc;
            if (t.input_section_title) if (document.getElementById('inputSectionTitle')) document.getElementById('inputSectionTitle').textContent = t.input_section_title;
            if (t.input_section_sub) if (document.getElementById('inputSectionSub')) document.getElementById('inputSectionSub').textContent = t.input_section_sub;
            if (t.preset_label) if (document.getElementById('presetLabel')) document.getElementById('presetLabel').textContent = t.preset_label;
            if (t.config_section_title) if (document.getElementById('configSectionTitle')) document.getElementById('configSectionTitle').textContent = t.config_section_title;
            if (t.grid_title) if (document.getElementById('gridTitle')) document.getElementById('gridTitle').textContent = t.grid_title;
            if (t.grid_sub) if (document.getElementById('gridSub')) document.getElementById('gridSub').textContent = t.grid_sub;
            if (t.btn_print) if (document.getElementById('btnPrintMatrix')) document.getElementById('btnPrintMatrix').textContent = t.btn_print;
            if (t.share_title) if (document.getElementById('shareTitleText')) document.getElementById('shareTitleText').textContent = t.share_title;
            if (t.share_sub) if (document.getElementById('shareSubText')) document.getElementById('shareSubText').textContent = t.share_sub;
            if (t.share_copy) if (document.getElementById('shareCopyText')) document.getElementById('shareCopyText').textContent = t.share_copy;
            if (t.rights_reserved) if (document.getElementById('rightsText')) document.getElementById('rightsText').textContent = t.rights_reserved;
            if (t.legal_disclaimer) if (document.getElementById('legalDisclaimerText')) document.getElementById('legalDisclaimerText').innerHTML = t.legal_disclaimer;
            if (t.print_sheet_title) if (document.getElementById('printSheetTitle')) document.getElementById('printSheetTitle').textContent = t.print_sheet_title;

            const fqTitle = document.getElementById('faqTitle'); if (fqTitle && t.faq_title) fqTitle.textContent = t.faq_title;
            const f1q = document.getElementById('faq1Q'); if (f1q && t.faq_1_q) f1q.textContent = t.faq_1_q;
            const f1a = document.getElementById('faq1A'); if (f1a && t.faq_1_a) f1a.innerHTML = t.faq_1_a;
            const f2q = document.getElementById('faq2Q'); if (f2q && t.faq_2_q) f2q.textContent = t.faq_2_q;
            const f2a = document.getElementById('faq2A'); if (f2a && t.faq_2_a) f2a.innerHTML = t.faq_2_a;
            const f3q = document.getElementById('faq3Q'); if (f3q && t.faq_3_q) f3q.textContent = t.faq_3_q;
            const f3a = document.getElementById('faq3A'); if (f3a && t.faq_3_a) f3a.innerHTML = t.faq_3_a;
            const f4q = document.getElementById('faq4Q'); if (f4q && t.faq_4_q) f4q.textContent = t.faq_4_q;
            const f4a = document.getElementById('faq4A'); if (f4a && t.faq_4_a) f4a.innerHTML = t.faq_4_a;
        }}

        // Preset Selector
        function setPreset(c, m, y, k) {{
            baseC = c; baseM = m; baseY = y; baseK = k;
            updateInputsFromState();
            generateMatrix();
        }}

        // Mode Switch (CMYK vs HEX)
        function switchInputMode(mode) {{
            const btnCmyk = document.getElementById('btnModeCmyk');
            const btnHex = document.getElementById('btnModeHex');
            const btnDropper = document.getElementById('btnModeDropper');
            const cmykGroup = document.getElementById('cmykControlsGroup');
            const hexGroup = document.getElementById('hexControlsGroup');
            const dropperGroup = document.getElementById('dropperControlsGroup');

            [btnCmyk, btnHex, btnDropper].forEach(b => {{
                if (b) b.className = "py-1.5 px-1 rounded-lg text-slate-600 hover:text-slate-900 transition text-center truncate font-bold";
            }});
            cmykGroup.classList.add('hidden');
            hexGroup.classList.add('hidden');
            dropperGroup.classList.add('hidden');

            if (mode === 'cmyk') {{
                btnCmyk.className = "py-1.5 px-1 rounded-lg bg-white text-rose-900 shadow-2xs transition text-center truncate font-bold";
                cmykGroup.classList.remove('hidden');
            }} else if (mode === 'hex') {{
                btnHex.className = "py-1.5 px-1 rounded-lg bg-white text-rose-900 shadow-2xs transition text-center truncate font-bold";
                hexGroup.classList.remove('hidden');
            }} else if (mode === 'dropper') {{
                btnDropper.className = "py-1.5 px-1 rounded-lg bg-white text-rose-900 shadow-2xs transition text-center truncate font-bold inline-flex items-center justify-center gap-1";
                dropperGroup.classList.remove('hidden');
            }}
        }}

        // ==========================================
        // EYEDROPPER & IMAGE SAMPLER SYSTEM
        // ==========================================
        async function triggerNativeEyeDropper() {{
            if (!window.EyeDropper) {{
                switchInputMode('dropper');
                alert("La pipetta a schermo intero non è supportata da questo browser. Usa il box di caricamento immagine per campionare qualsiasi foto!");
                return;
            }}
            try {{
                const eyeDropper = new EyeDropper();
                const result = await eyeDropper.open();
                if (result && result.sRGBHex) {{
                    onHexInputChange(result.sRGBHex);
                    showPickedToast(`✓ Colore campionato: ${{result.sRGBHex.toUpperCase()}} (C:${{baseC}} M:${{baseM}} Y:${{baseY}} K:${{baseK}})`);
                }}
            }} catch (e) {{
                // Dismissed
            }}
        }}

        function showPickedToast(msg) {{
            const toast = document.getElementById('pickedToast');
            const text = document.getElementById('pickedToastText');
            if (toast && text) {{
                text.textContent = msg;
                toast.classList.remove('hidden');
                setTimeout(() => toast.classList.add('hidden'), 4000);
            }}
        }}

        function handleImageFileUpload(e) {{
            const file = e.target.files && e.target.files[0];
            if (file) loadImageFile(file);
        }}

        function loadImageFile(file) {{
            if (!file || !file.type.startsWith('image/')) return;
            const reader = new FileReader();
            reader.onload = function(evt) {{
                const img = new Image();
                img.onload = function() {{
                    renderImageOnCanvas(img);
                }};
                img.src = evt.target.result;
            }};
            reader.readAsDataURL(file);
        }}

        let loadedImageElement = null;

        function renderImageOnCanvas(img) {{
            loadedImageElement = img;
            const canvas = document.getElementById('samplerCanvas');
            const ctx = canvas.getContext('2d', {{ willReadFrequently: true }});

            const maxW = 500;
            const maxH = 260;
            let w = img.width;
            let h = img.height;

            if (w > maxW || h > maxH) {{
                const ratio = Math.min(maxW / w, maxH / h);
                w = Math.round(w * ratio);
                h = Math.round(h * ratio);
            }}

            canvas.width = w;
            canvas.height = h;
            ctx.drawImage(img, 0, 0, w, h);

            document.getElementById('imageDropzone').classList.add('hidden');
            document.getElementById('imageSamplerArea').classList.remove('hidden');

            canvas.onmousemove = onCanvasMouseMove;
            canvas.onmouseleave = onCanvasMouseLeave;
            canvas.onclick = onCanvasClick;
        }}

        function clearLoadedImage() {{
            loadedImageElement = null;
            document.getElementById('imageDropzone').classList.remove('hidden');
            document.getElementById('imageSamplerArea').classList.add('hidden');
            document.getElementById('magnifierLoupe').classList.add('hidden');
            const input = document.getElementById('imageFileInput');
            if (input) input.value = '';
        }}

        function onCanvasMouseMove(e) {{
            const canvas = document.getElementById('samplerCanvas');
            const rect = canvas.getBoundingClientRect();
            const scaleX = canvas.width / rect.width;
            const scaleY = canvas.height / rect.height;
            const x = Math.floor((e.clientX - rect.left) * scaleX);
            const y = Math.floor((e.clientY - rect.top) * scaleY);

            if (x < 0 || y < 0 || x >= canvas.width || y >= canvas.height) {{
                onCanvasMouseLeave();
                return;
            }}

            const ctx = canvas.getContext('2d', {{ willReadFrequently: true }});
            const pixel = ctx.getImageData(x, y, 1, 1).data;
            const r = pixel[0], g = pixel[1], b = pixel[2];
            const hex = rgbToHex(r, g, b);
            const cmyk = rgbToCmyk(r, g, b);

            document.getElementById('hoverColorBox').style.backgroundColor = hex;
            if (document.getElementById('hoverHexText')) document.getElementById('hoverHexText').textContent = hex;
            if (document.getElementById('hoverCmykText')) document.getElementById('hoverCmykText').textContent = `C:${{cmyk.c}}% M:${{cmyk.m}}% Y:${{cmyk.y}}% K:${{cmyk.k}}%`;

            const loupe = document.getElementById('magnifierLoupe');
            loupe.classList.remove('hidden');
            loupe.style.left = `${{e.clientX - rect.left}}px`;
            loupe.style.top = `${{e.clientY - rect.top}}px`;

            const loupeCanvas = document.getElementById('loupeCanvas');
            const lctx = loupeCanvas.getContext('2d');
            lctx.imageSmoothingEnabled = false;
            lctx.clearRect(0, 0, 80, 80);
            const sampleSize = 16;
            const half = Math.floor(sampleSize / 2);
            lctx.drawImage(canvas, x - half, y - half, sampleSize, sampleSize, 0, 0, 80, 80);
        }}

        function onCanvasMouseLeave() {{
            const loupe = document.getElementById('magnifierLoupe');
            if (loupe) loupe.classList.add('hidden');
        }}

        function onCanvasClick(e) {{
            const canvas = document.getElementById('samplerCanvas');
            const rect = canvas.getBoundingClientRect();
            const scaleX = canvas.width / rect.width;
            const scaleY = canvas.height / rect.height;
            const x = Math.floor((e.clientX - rect.left) * scaleX);
            const y = Math.floor((e.clientY - rect.top) * scaleY);

            const ctx = canvas.getContext('2d', {{ willReadFrequently: true }});
            const pixel = ctx.getImageData(x, y, 1, 1).data;
            const hex = rgbToHex(pixel[0], pixel[1], pixel[2]);

            onHexInputChange(hex);
            showPickedToast(`✓ Campionato dall'immagine: ${{hex}} (C:${{baseC}} M:${{baseM}} Y:${{baseY}} K:${{baseK}})`);
        }}

        function initImageSamplerListeners() {{
            const dropzone = document.getElementById('imageDropzone');
            if (dropzone) {{
                ['dragenter', 'dragover'].forEach(name => {{
                    dropzone.addEventListener(name, (e) => {{
                        e.preventDefault();
                        dropzone.classList.add('border-rose-600', 'bg-rose-100/50');
                    }});
                }});
                ['dragleave', 'drop'].forEach(name => {{
                    dropzone.addEventListener(name, (e) => {{
                        e.preventDefault();
                        dropzone.classList.remove('border-rose-600', 'bg-rose-100/50');
                    }});
                }});
                dropzone.addEventListener('drop', (e) => {{
                    e.preventDefault();
                    if (e.dataTransfer && e.dataTransfer.files && e.dataTransfer.files[0]) {{
                        loadImageFile(e.dataTransfer.files[0]);
                    }}
                }});
            }}

            window.addEventListener('paste', function(e) {{
                if (e.clipboardData && e.clipboardData.items) {{
                    for (let i = 0; i < e.clipboardData.items.length; i++) {{
                        const item = e.clipboardData.items[i];
                        if (item.type.indexOf('image') !== -1) {{
                            const file = item.getAsFile();
                            switchInputMode('dropper');
                            loadImageFile(file);
                            break;
                        }}
                    }}
                }}
            }});
        }}

        function switchFeedType(type) {{
            feedType = type;
            const btnSheet = document.getElementById('btnFeedSheet');
            const btnRoll = document.getElementById('btnFeedRoll');
            const sheetGroup = document.getElementById('sheetOptionsGroup');
            const rollGroup = document.getElementById('rollOptionsGroup');

            if (type === 'sheet') {{
                btnSheet.className = "py-2 px-2 rounded-xl bg-rose-900 text-white shadow-2xs transition font-bold";
                btnRoll.className = "py-2 px-2 rounded-xl bg-slate-100 hover:bg-slate-200 text-slate-700 border border-slate-200 transition font-bold";
                sheetGroup.classList.remove('hidden');
                rollGroup.classList.add('hidden');
            }} else {{
                btnRoll.className = "py-2 px-2 rounded-xl bg-rose-900 text-white shadow-2xs transition font-bold";
                btnSheet.className = "py-2 px-2 rounded-xl bg-slate-100 hover:bg-slate-200 text-slate-700 border border-slate-200 transition font-bold";
                rollGroup.classList.remove('hidden');
                sheetGroup.classList.add('hidden');
            }}
            recalculateDimensions();
        }}

        function onSheetPresetChange() {{
            const val = document.getElementById('sheetPresetSelect').value;
            sheetPreset = val;
            const customBox = document.getElementById('customSheetInputs');
            if (val === 'CUSTOM') {{
                customBox.classList.remove('hidden');
            }} else {{
                if (val === 'A4') {{
                    document.getElementById('sheetWidthInput').value = 21.0;
                    document.getElementById('sheetHeightInput').value = 29.7;
                }} else if (val === 'A3') {{
                    document.getElementById('sheetWidthInput').value = 29.7;
                    document.getElementById('sheetHeightInput').value = 42.0;
                }} else if (val === 'SRA3') {{
                    document.getElementById('sheetWidthInput').value = 33.0;
                    document.getElementById('sheetHeightInput').value = 48.0;
                }}
            }}
            recalculateDimensions();
        }}

        function setOrientation(orient) {{
            orientation = orient;
            const btnP = document.getElementById('btnOrientP');
            const btnL = document.getElementById('btnOrientL');
            if (orient === 'portrait') {{
                btnP.className = "py-1.5 px-2 rounded-xl bg-rose-50 text-rose-900 border border-rose-200 transition font-bold";
                btnL.className = "py-1.5 px-2 rounded-xl bg-slate-100 text-slate-700 border border-slate-200 transition font-bold";
            }} else {{
                btnL.className = "py-1.5 px-2 rounded-xl bg-rose-50 text-rose-900 border border-rose-200 transition font-bold";
                btnP.className = "py-1.5 px-2 rounded-xl bg-slate-100 text-slate-700 border border-slate-200 transition font-bold";
            }}
            recalculateDimensions();
        }}

        function onRollRowsChange() {{
            recalculateDimensions();
        }}

        function onRollPresetChange() {{
            const val = document.getElementById('rollWidthSelect').value;
            rollWidthPreset = val;
            const customBox = document.getElementById('customRollWidthInput');
            if (val === 'CUSTOM') {{
                customBox.classList.remove('hidden');
            }} else {{
                customBox.classList.add('hidden');
                document.getElementById('rollCustomWidthVal').value = parseFloat(val);
            }}
            recalculateDimensions();
        }}

        function onCustomDimensionsChange() {{
            recalculateDimensions();
        }}

        function recalculateDimensions() {{
            let wMm, hMm;

            if (feedType === 'sheet') {{
                let wCm = parseFloat(document.getElementById('sheetWidthInput').value) || 33.0;
                let hCm = parseFloat(document.getElementById('sheetHeightInput').value) || 48.0;

                if (orientation === 'landscape' && wCm < hCm) {{
                    const temp = wCm; wCm = hCm; hCm = temp;
                }} else if (orientation === 'portrait' && wCm > hCm) {{
                    const temp = wCm; wCm = hCm; hCm = temp;
                }}
                wMm = Math.round(wCm * 10);
                hMm = Math.round(hCm * 10);
            }} else {{
                // Roll Web Strip
                let wCm;
                if (rollWidthPreset === 'CUSTOM') {{
                    wCm = parseFloat(document.getElementById('rollCustomWidthVal').value) || 33.0;
                }} else {{
                    wCm = parseFloat(rollWidthPreset) || 33.0;
                }}
                const rollRows = parseInt(document.getElementById('rollRowsSelect')?.value, 10) || 4;
                const calculatedHeightCm = (rollRows * 3.5) + 2.5;
                wMm = Math.round(wCm * 10);
                hMm = Math.round(calculatedHeightCm * 10);

                const colsCount = wCm >= 45 ? 11 : (wCm >= 30 ? 9 : 7);
                const totalSamples = rollRows * colsCount;
                const estEl = document.getElementById('rollAdvanceEstimate');
                if (estEl) {{
                    estEl.textContent = `${{totalSamples}} campioni • ${{calculatedHeightCm.toFixed(1)}} cm`;
                }}
            }}

            currentWidthMm = wMm;
            currentHeightMm = hMm;

            const wCmStr = (wMm / 10).toFixed(1).replace('.0', '');
            const hCmStr = (hMm / 10).toFixed(1).replace('.0', '');
            const dimText = `${{wCmStr}} × ${{hCmStr}} cm`;

            if (document.getElementById('liveSizeIndicator')) document.getElementById('liveSizeIndicator').textContent = dimText;
            if (document.getElementById('printFormatName')) document.getElementById('printFormatName').textContent = dimText;
            if (document.getElementById('matrixDimFooter')) document.getElementById('matrixDimFooter').textContent = `Dimensioni Foglio: ${{dimText}} • FOGRA39`;
            const badgeEl = document.getElementById('badgeFormatIndicator');
            if (badgeEl) badgeEl.textContent = dimText;

            // Update Dynamic Print CSS rule
            const styleEl = document.getElementById('dynamicPageStyle');
            styleEl.textContent = `
                @media print {{
                    @page {{
                        size: ${{wMm}}mm ${{hMm}}mm;
                        margin: 5mm;
                    }}
                    body {{
                        background: #ffffff !important;
                        color: #000000 !important;
                        font-size: 8.5pt !important;
                        line-height: 1.15 !important;
                        padding: 0 !important;
                    }}
                    .no-print {{ display: none !important; }}
                    .print-only {{ display: block !important; }}
                    .print-card {{ box-shadow: none !important; border: 1px solid #cbd5e1 !important; break-inside: avoid !important; }}
                    .matrix-cell {{ -webkit-print-color-adjust: exact !important; print-color-adjust: exact !important; }}
                }}
                .print-only {{ display: none; }}
            `;

            generateMatrix();
        }}

        // Input Handlers
        function onCmykChange() {{
            baseC = parseInt(document.getElementById('cSlider').value, 10);
            baseM = parseInt(document.getElementById('mSlider').value, 10);
            baseY = parseInt(document.getElementById('ySlider').value, 10);
            baseK = parseInt(document.getElementById('kSlider').value, 10);
            updatePreviewAndTac();
            generateMatrix();
        }}

        function onColorPickerChange(hexVal) {{
            document.getElementById('hexInput').value = hexVal.toUpperCase();
            const rgb = hexToRgb(hexVal);
            const cmyk = rgbToCmyk(rgb.r, rgb.g, rgb.b);
            baseC = cmyk.c; baseM = cmyk.m; baseY = cmyk.y; baseK = cmyk.k;
            updateInputsFromState();
            generateMatrix();
        }}

        function onHexInputChange(hexVal) {{
            if (!hexVal.startsWith('#')) hexVal = '#' + hexVal;
            if (/^#[0-9A-F]{{6}}$/i.test(hexVal)) {{
                document.getElementById('nativeColorPicker').value = hexVal;
                const rgb = hexToRgb(hexVal);
                const cmyk = rgbToCmyk(rgb.r, rgb.g, rgb.b);
                baseC = cmyk.c; baseM = cmyk.m; baseY = cmyk.y; baseK = cmyk.k;
                updateInputsFromState();
                generateMatrix();
            }}
        }}

        function setStep(step) {{
            currentStep = step;
            ['step2Btn', 'step5Btn', 'step10Btn'].forEach(id => {{
                const el = document.getElementById(id);
                el.className = "py-1.5 px-2 rounded-xl bg-slate-100 hover:bg-slate-200 text-slate-700 border border-slate-200 transition font-bold";
            }});
            document.getElementById(`step${{step}}Btn`).className = "py-1.5 px-2 rounded-xl bg-rose-900 text-white shadow-2xs transition font-bold";
            if (document.getElementById('printStepName')) document.getElementById('printStepName').textContent = `±${{step}}%`;
            generateMatrix();
        }}

        function updateInputsFromState() {{
            document.getElementById('cSlider').value = baseC;
            document.getElementById('mSlider').value = baseM;
            document.getElementById('ySlider').value = baseY;
            document.getElementById('kSlider').value = baseK;

            if (document.getElementById('cValText')) document.getElementById('cValText').textContent = baseC + '%';
            if (document.getElementById('mValText')) document.getElementById('mValText').textContent = baseM + '%';
            if (document.getElementById('yValText')) document.getElementById('yValText').textContent = baseY + '%';
            if (document.getElementById('kValText')) document.getElementById('kValText').textContent = baseK + '%';

            updatePreviewAndTac();
        }}

        function updatePreviewAndTac() {{
            if (document.getElementById('cValText')) document.getElementById('cValText').textContent = baseC + '%';
            if (document.getElementById('mValText')) document.getElementById('mValText').textContent = baseM + '%';
            if (document.getElementById('yValText')) document.getElementById('yValText').textContent = baseY + '%';
            if (document.getElementById('kValText')) document.getElementById('kValText').textContent = baseK + '%';

            const rgb = cmykToRgb(baseC, baseM, baseY, baseK);
            const hex = rgbToHex(rgb.r, rgb.g, rgb.b);
            document.getElementById('previewSwatch').style.backgroundColor = hex;
            document.getElementById('nativeColorPicker').value = hex;
            document.getElementById('hexInput').value = hex.toUpperCase();

            const tac = baseC + baseM + baseY + baseK;
            if (document.getElementById('tacValue')) document.getElementById('tacValue').textContent = tac + '%';

            const badge = document.getElementById('tacStatusBadge');
            if (tac > 320) {{
                badge.className = "text-[10px] font-bold px-2 py-0.5 rounded-md bg-rose-50 text-rose-700 border border-rose-200";
                badge.textContent = "Alto (>320%)";
            }} else if (tac > 300) {{
                badge.className = "text-[10px] font-bold px-2 py-0.5 rounded-md bg-amber-50 text-amber-700 border border-amber-200";
                badge.textContent = "Limite (300%)";
            }} else {{
                badge.className = "text-[10px] font-bold px-2 py-0.5 rounded-md bg-emerald-50 text-emerald-700 border border-emerald-200";
                badge.textContent = "Sicuro (<300%)";
            }}
        }}

        function updatePrintMetadata() {{
            const job = document.getElementById('jobInput').value.trim() || 'Lavoro Campione';
            const press = document.getElementById('pressInput').value.trim() || 'Rotativa a Bobina';
            const paper = document.getElementById('paperInput').value.trim() || 'Patinata Lucida';

            if (document.getElementById('printJobName')) document.getElementById('printJobName').textContent = job;
            if (document.getElementById('printPressName')) document.getElementById('printPressName').textContent = press;
            if (document.getElementById('printPaperName')) document.getElementById('printPaperName').textContent = paper;
        }}

        // Matrix calculation cache for PDF download
        let currentGridCells = []; // array of cell objects

        // ==========================================
        // CHROMATIC BRACKETING MATRIX GENERATOR
        // ==========================================
        function generateMatrix() {{
            updatePreviewAndTac();
            updatePrintMetadata();

            const container = document.getElementById('matrixContainer');
            container.innerHTML = '';

            const step = currentStep;

            let cols = 5;
            let rows = 5;

            if (feedType === 'roll') {{
                const rollRows = parseInt(document.getElementById('rollRowsSelect')?.value, 10) || 4;
                rows = rollRows;
                const wCm = currentWidthMm / 10;
                cols = wCm >= 45 ? 11 : (wCm >= 30 ? 9 : 7);
            }} else {{
                // Sheet Mode
                if (currentWidthMm > currentHeightMm) {{
                    // Landscape
                    cols = 7;
                    rows = 5;
                }} else {{
                    // Portrait (A4, SRA3 33x48) -> 5 cols x 5 rows for MAXIMUM tile size
                    cols = 5;
                    rows = 5;
                }}
            }}

            const centerCol = Math.floor(cols / 2);
            const centerRow = Math.floor(rows / 2);

            const rowLetters = ['A', 'B', 'C', 'D', 'E', 'F', 'G'];

            currentGridCells = [];

            const table = document.createElement('table');
            table.className = "w-full border-collapse text-center select-none print-full-height";

            // Table Header: Column Indices
            const thead = document.createElement('thead');
            const trHead = document.createElement('tr');
            trHead.className = "border-b border-slate-200";
            
            const thCorner = document.createElement('th');
            thCorner.className = "p-1 text-slate-400 font-mono text-[9px] w-8";
            thCorner.textContent = "R/C";
            trHead.appendChild(thCorner);

            for (let c = 0; c < cols; c++) {{
                const th = document.createElement('th');
                th.className = "p-1 sm:p-1.5 text-slate-700 font-mono text-[11px] sm:text-xs font-black";
                const deltaCol = (c - centerCol) * step;
                th.innerHTML = `${{c + 1}}<br><span class=\"text-[9px] sm:text-[10px] font-bold text-slate-400\">${{deltaCol >= 0 ? '+' : ''}}${{deltaCol}}%</span>`;
                trHead.appendChild(th);
            }}
            thead.appendChild(trHead);
            table.appendChild(thead);

            const tbody = document.createElement('tbody');

            for (let r = 0; r < rows; r++) {{
                const tr = document.createElement('tr');
                tr.className = "border-b border-slate-100";

                const tdRowLabel = document.createElement('td');
                const deltaRow = (r - centerRow) * step;
                tdRowLabel.className = "p-1 sm:p-1.5 font-mono font-black text-slate-700 text-xs sm:text-sm w-8";
                tdRowLabel.innerHTML = `${{rowLetters[r]}}<br><span class=\"text-[9px] sm:text-[10px] font-bold text-slate-400\">${{deltaRow >= 0 ? '+' : ''}}${{deltaRow}}%</span>`;
                tr.appendChild(tdRowLabel);

                for (let c = 0; c < cols; c++) {{
                    const td = document.createElement('td');
                    td.className = "p-1 sm:p-1.5";

                    const dCol = (c - centerCol) * step;
                    const dRow = (r - centerRow) * step;

                    let tileC = baseC;
                    let tileM = baseM;
                    let tileY = baseY;
                    let tileK = baseK;

                    // Horizontal variation: Hue
                    if (dCol > 0) {{
                        tileM = clamp(tileM + dCol);
                        tileY = clamp(tileY + dCol);
                    }} else if (dCol < 0) {{
                        tileC = clamp(tileC - dCol);
                    }}

                    // Vertical variation: Density / K
                    if (dRow > 0) {{
                        tileK = clamp(tileK + dRow);
                        tileC = clamp(tileC + Math.round(dRow * 0.5));
                    }} else if (dRow < 0) {{
                        tileK = clamp(tileK + dRow);
                        tileM = clamp(tileM + Math.round(dRow * 0.5));
                        tileY = clamp(tileY + Math.round(dRow * 0.5));
                    }}

                    const tileTac = tileC + tileM + tileY + tileK;
                    const rgb = cmykToRgb(tileC, tileM, tileY, tileK);
                    const hex = rgbToHex(rgb.r, rgb.g, rgb.b);
                    const coordName = `${{rowLetters[r]}}${{c + 1}}`;
                    const isCenter = (c === centerCol && r === centerRow);

                    const cellData = {{
                        c: tileC, m: tileM, y: tileY, k: tileK,
                        col: c, row: r, coord: coordName, tac: tileTac,
                        rgb: rgb, hex: hex, isCenter: isCenter
                    }};
                    currentGridCells.push(cellData);

                    // Swatch Box Element:
                    // If roll mode: GIANT vertical rectangle (h-36 sm:h-48)
                    // If sheet mode: LARGE swatch (h-24 sm:h-28 md:h-32)
                    const heightClass = (feedType === 'roll') 
                        ? (rows <= 2 ? 'h-32 sm:h-44' : (rows <= 4 ? 'h-24 sm:h-32' : 'h-20 sm:h-24'))
                        : 'h-24 sm:h-28 md:h-32';

                    const swatchBtn = document.createElement('button');
                    swatchBtn.type = "button";
                    swatchBtn.className = `color-swatch-box matrix-cell w-full ${{heightClass}} rounded-2xl flex flex-col justify-between p-2 text-left relative cursor-pointer border ${{
                        isCenter ? 'border-3 border-amber-400 ring-4 ring-amber-400/40 shadow-lg' : 'border-black/15 shadow-xs'
                    }}`;
                    swatchBtn.style.backgroundColor = hex;

                    const isDark = (rgb.r * 0.299 + rgb.g * 0.587 + rgb.b * 0.114) < 140;
                    const textColor = isDark ? '#ffffff' : '#0f172a';

                    swatchBtn.innerHTML = `
                        <div class=\"flex items-center justify-between leading-none\" style=\"color: ${{textColor}}\">
                            <span class=\"font-mono font-black text-xs sm:text-sm tracking-wide\">${{coordName}}</span>
                            ${{isCenter ? '<span class=\"text-xs sm:text-sm font-black px-1.5 py-0.5 rounded bg-amber-400 text-slate-900 shadow-2xs\">★ BASE</span>' : ''}}
                        </div>
                        <div class=\"font-mono font-extrabold text-[10px] sm:text-xs leading-tight tracking-tight mt-auto\" style=\"color: ${{textColor}}\">
                            <div class=\"bg-black/30 backdrop-blur-xs px-1.5 py-1 rounded-lg inline-block w-full\">
                                C:${{tileC}} M:${{tileM}} Y:${{tileY}} K:${{tileK}}
                            </div>
                        </div>
                    `;

                    swatchBtn.onclick = () => selectSwatch(cellData);
                    td.appendChild(swatchBtn);
                    tr.appendChild(td);

                    if (isCenter && !selectedCell) {{
                        selectedCell = cellData;
                    }}
                }}

                tbody.appendChild(tr);
            }}

            table.appendChild(tbody);
            container.appendChild(table);

            if (selectedCell) {{
                updateInspector(selectedCell);
            }}
        }}

        function selectSwatch(cell) {{
            selectedCell = cell;
            updateInspector(cell);
        }}

        function updateInspector(cell) {{
            document.getElementById('inspectorSwatch').style.backgroundColor = cell.hex;
            if (document.getElementById('inspectorCoord')) document.getElementById('inspectorCoord').textContent = `${{cell.coord}} ${{cell.isCenter ? '(Centro)' : ''}}`;
            if (document.getElementById('inspectorTac')) document.getElementById('inspectorTac').textContent = `TAC: ${{cell.tac}}%`;

            if (document.getElementById('inspectC')) document.getElementById('inspectC').textContent = cell.c + '%';
            if (document.getElementById('inspectM')) document.getElementById('inspectM').textContent = cell.m + '%';
            if (document.getElementById('inspectY')) document.getElementById('inspectY').textContent = cell.y + '%';
            if (document.getElementById('inspectK')) document.getElementById('inspectK').textContent = cell.k + '%';
        }}

        function recenterOnSelected() {{
            if (!selectedCell) return;
            baseC = selectedCell.c;
            baseM = selectedCell.m;
            baseY = selectedCell.y;
            baseK = selectedCell.k;
            updateInputsFromState();
            selectedCell = null;
            generateMatrix();
        }}

        function copyRecipe() {{
            if (!selectedCell) return;
            const text = `C:${{selectedCell.c}} M:${{selectedCell.m}} Y:${{selectedCell.y}} K:${{selectedCell.k}} (TAC: ${{selectedCell.tac}}%) - Tassello ${{selectedCell.coord}}`;
            navigator.clipboard.writeText(text).then(() => {{
                const btn = document.getElementById('btnCopyText');
                const orig = btn.textContent;
                btn.textContent = 'Copiato! ✓';
                setTimeout(() => btn.textContent = orig, 1800);
            }});
        }}

        // ==========================================
        // CLIENT-SIDE VECTOR PDF GENERATOR (jsPDF)
        // ==========================================
        function downloadVectorPdf() {{
            const jsPDFClass = (window.jspdf && window.jspdf.jsPDF) || window.jsPDF;
            if (!jsPDFClass) {{
                // Fallback to print dialog if jsPDF CDN is blocked
                window.print();
                return;
            }}

            const wMm = currentWidthMm;
            const hMm = currentHeightMm;
            const orient = wMm > hMm ? 'l' : 'p';

            const doc = new jsPDFClass({{
                orientation: orient,
                unit: 'mm',
                format: [wMm, hMm]
            }});

            const job = document.getElementById('jobInput').value.trim() || 'Commessa';
            const press = document.getElementById('pressInput').value.trim() || 'Macchina';
            const paper = document.getElementById('paperInput').value.trim() || 'Supporto';
            const dateStr = new Date().toLocaleDateString('it-IT');

            // Margin & Layout calculation
            const margin = 10; // 10mm margin for print clamps & crop marks
            const contentW = wMm - (margin * 2);
            const contentH = hMm - (margin * 2);

            // 1. Draw Technical Crop Marks (Crocini di registro tipografici)
            doc.setDrawColor(30, 41, 59);
            doc.setLineWidth(0.2);
            // Top-left
            doc.line(margin - 4, margin, margin + 4, margin);
            doc.line(margin, margin - 4, margin, margin + 4);
            // Top-right
            doc.line(wMm - margin - 4, margin, wMm - margin + 4, margin);
            doc.line(wMm - margin, margin - 4, wMm - margin, margin + 4);
            // Bottom-left
            doc.line(margin - 4, hMm - margin, margin + 4, hMm - margin);
            doc.line(margin, hMm - margin - 4, margin, hMm - margin + 4);
            // Bottom-right
            doc.line(wMm - margin - 4, hMm - margin, wMm - margin + 4, hMm - margin);
            doc.line(wMm - margin, hMm - margin - 4, wMm - margin, hMm - margin + 4);

            // 2. Draw Technical Header Banner
            doc.setFont('helvetica', 'bold');
            doc.setFontSize(10);
            doc.setTextColor(159, 18, 57); // Rose 800
            doc.text('OmniGraph Lab — TintaPerfetta', margin + 2, margin + 5);

            doc.setFont('helvetica', 'normal');
            doc.setFontSize(7.5);
            doc.setTextColor(71, 85, 105);
            doc.text(`COMMESSA: ${{job}}   |   MACCHINA: ${{press}}   |   SUPPORTO: ${{paper}}   |   DATA: ${{dateStr}}   |   PASSO: ±${{currentStep}}%`, margin + 2, margin + 9);

            doc.setFont('helvetica', 'bold');
            doc.setFontSize(7);
            doc.setTextColor(100, 116, 139);
            doc.text(`MISURA REALE: ${{wMm / 10}} × ${{hMm / 10}} cm  (FOGRA39 / ISO 12647-2)`, wMm - margin - 2, margin + 5, {{ align: 'right' }});

            // Separator Line
            doc.setDrawColor(226, 232, 240);
            doc.line(margin + 2, margin + 11, wMm - margin - 2, margin + 11);

            // 3. Grid Calculation
            const gridStartY = margin + 14;
            const gridH = hMm - gridStartY - margin - 4;
            const gridW = contentW - 4;

            // Find rows and cols in current cells
            let maxCol = 0;
            let maxRow = 0;
            currentGridCells.forEach(cell => {{
                if (cell.col > maxCol) maxCol = cell.col;
                if (cell.row > maxRow) maxRow = cell.row;
            }});

            const totalCols = maxCol + 1;
            const totalRows = maxRow + 1;

            const gap = 1.5; // mm between cells
            const cellW = (gridW - (gap * (totalCols - 1))) / totalCols;
            // FULL HEIGHT UTILIZATION - fills entire page / strip without arbitrary cap
            const cellH = (gridH - (gap * (totalRows - 1))) / totalRows;

            // Draw Swatches
            currentGridCells.forEach(cell => {{
                const x = margin + 2 + (cell.col * (cellW + gap));
                const y = gridStartY + (cell.row * (cellH + gap));

                // Fill Color
                doc.setFillColor(cell.rgb.r, cell.rgb.g, cell.rgb.b);
                doc.roundedRect(x, y, cellW, cellH, 1.5, 1.5, 'F');

                // Border
                if (cell.isCenter) {{
                    doc.setDrawColor(245, 158, 11); // Amber-500
                    doc.setLineWidth(0.8);
                    doc.roundedRect(x, y, cellW, cellH, 1.5, 1.5, 'D');
                }} else {{
                    doc.setDrawColor(0, 0, 0, 0.2);
                    doc.setLineWidth(0.15);
                    doc.roundedRect(x, y, cellW, cellH, 1.5, 1.5, 'D');
                }}

                // Text Contrast
                const isDark = (cell.rgb.r * 0.299 + cell.rgb.g * 0.587 + cell.rgb.b * 0.114) < 140;
                doc.setTextColor(isDark ? 255 : 15, isDark ? 255 : 23, isDark ? 255 : 42);

                // Top coordinate label
                doc.setFont('helvetica', 'bold');
                doc.setFontSize(cellH > 35 ? 12 : (cellH > 18 ? 9 : 7));
                doc.text(cell.coord, x + 2.5, y + (cellH > 35 ? 7 : (cellH > 18 ? 5 : 3.5)));

                if (cell.isCenter) {{
                    doc.setFontSize(cellH > 35 ? 9 : 7);
                    doc.text('[★ BASE]', x + cellW - 2.5, y + (cellH > 35 ? 7 : (cellH > 18 ? 5 : 3.5)), {{ align: 'right' }});
                }}

                // Bottom Recipe label
                doc.setFont('helvetica', 'bold');
                doc.setFontSize(cellH > 35 ? 9.5 : (cellH > 18 ? 7.5 : 5.8));
                doc.text(`C:${{cell.c}} M:${{cell.m}} Y:${{cell.y}} K:${{cell.k}}`, x + 2.5, y + cellH - (cellH > 35 ? 3.5 : 2));
            }});
            // 4. Operator Legend at Bottom
            doc.setFont('helvetica', 'italic');
            doc.setFontSize(6.5);
            doc.setTextColor(148, 163, 184);
            doc.text('Istruzioni: 1) Stampa sul supporto effettivo; 2) Confronta con il campione alla luce neutra D50; 3) Riporta i valori del tassello nel RIP.', margin + 2, hMm - margin + 1);

            // Trigger Clean Download
            const cleanJob = job.replace(/[^a-z0-9]/gi, '_').toLowerCase();
            const fileName = `TintaPerfetta_${{wMm / 10}}x${{hMm / 10}}cm_${{cleanJob}}.pdf`;
            doc.save(fileName);
        }}

        // Viral Sharing
        function shareWhatsApp() {{
            const url = encodeURIComponent(window.location.href);
            const text = encodeURIComponent('TintaPerfetta: Matrice di Scarto CMYK per centrare il colore al primo colpo su qualsiasi formato foglio o bobina: ' + window.location.href);
            window.open(`https://api.whatsapp.com/send?text=${{text}}`, '_blank');
        }}

        function shareLinkedIn() {{
            const url = encodeURIComponent(window.location.href);
            window.open(`https://www.linkedin.com/sharing/share-offsite/?url=${{url}}`, '_blank');
        }}

        function copyCurrentUrl() {{
            navigator.clipboard.writeText(window.location.href).then(() => {{
                const btn = document.getElementById('shareCopyText');
                if (btn) {{
                    const orig = btn.textContent;
                    btn.textContent = 'Copiato! ✓';
                    setTimeout(() => btn.textContent = orig, 2000);
                }}
            }});
        }}

        // PWA Install
        let deferredPrompt;
        window.addEventListener('beforeinstallprompt', (e) => {{
            e.preventDefault();
            deferredPrompt = e;
        }});

        function triggerInstall() {{
            if (deferredPrompt) {{
                deferredPrompt.prompt();
                deferredPrompt.userChoice.then(() => {{
                    deferredPrompt = null;
                }});
            }}
        }}

        // Init
        document.addEventListener('DOMContentLoaded', () => {{
            applyTranslations();
            updateInputsFromState();
            recalculateDimensions();
        }});
    </script>
</body>
</html>
"""

with open("/Users/ilalu/Documents/Altenative Businnes/Calcolatore_Pendenza/tinta.html", "w", encoding="utf-8") as f:
    f.write(html_code)

print("tinta.html compiled with Custom Sheet & Roll Sizing and jsPDF Vector Engine successfully.")
