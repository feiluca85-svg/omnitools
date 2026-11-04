import json

with open('/Users/ilalu/Documents/Altenative Businnes/Calcolatore_Pendenza/translations_tinta.json', 'r', encoding='utf-8') as f:
    t_data = json.load(f)

t_json_str = json.dumps(t_data, ensure_ascii=False)

html_code = f"""<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0">
    <title>TintaPerfetta — Matrice di Calibrazione Colore & Prova Stampa CMYK (Formati A4, A3, 33x48 e Bobina)</title>
    <meta name="description" content="Generatore professionale di matrici cromatiche di scarto CMYK su misura: A4, A3, SRA3 33x48 cm, formati personalizzati e strisce bobina su misura (25, 30, 33 cm).">
    
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
    <header class="no-print bg-white/95 border-b border-slate-200 sticky top-0 z-40 backdrop-blur-md shadow-2xs" style="padding-top: max(env(safe-area-inset-top), 8px); padding-bottom: 8px;">
        <div class="max-w-5xl mx-auto px-3 sm:px-4 py-1 flex items-center justify-between gap-2">
            
            <!-- Brand Identity -->
            <div class="flex items-center gap-2 sm:gap-2.5 min-w-0">
                <a href="/" class="w-[33px] h-[33px] sm:w-[36px] sm:h-[36px] rounded-xl bg-gradient-to-br from-rose-800 to-rose-950 flex items-center justify-center text-white shadow-md shadow-rose-900/20 shrink-0 p-1 transition hover:opacity-95" title="OmniTools Home">
                    <svg class="w-full h-full" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <circle cx="16" cy="16" r="13.2" stroke="#ffffff" stroke-width="2.8" />
                        <circle cx="16" cy="16" r="6" stroke="#ffffff" stroke-width="2" />
                        <line x1="16" y1="4.5" x2="16" y2="27.5" stroke="#ffffff" stroke-width="2" stroke-linecap="round" />
                        <line x1="4.5" y1="16" x2="27.5" y2="16" stroke="#ffffff" stroke-width="2" stroke-linecap="round" />
                        <circle cx="16" cy="16" r="2.2" fill="#fda4af" />
                    </svg>
                </a>
                <div class="flex flex-col min-w-0">
                    <div class="flex items-center gap-1.5 leading-none">
                        <a href="/" class="font-jakarta font-black text-sm sm:text-base text-slate-900 tracking-tight leading-none hover:text-rose-900 transition">Omni<span class="text-rose-800">Graph</span></a>
                        <span class="text-[8px] sm:text-[9px] font-jakarta font-extrabold uppercase bg-rose-100 text-rose-900 px-1.5 py-0.5 rounded-full border border-rose-300 shrink-0">Prestampa</span>
                        <span class="h-3.5 w-px bg-slate-200 hidden sm:inline-block"></span>
                        <span class="font-bold text-xs text-slate-700 hidden sm:inline-block">TintaPerfetta</span>
                        <span class="px-1.5 py-0.5 text-[9px] font-bold bg-rose-50 text-rose-800 rounded-md border border-rose-200 shrink-0 hidden sm:inline-block" id="badgeFormatIndicator">A4 / 33x48 / Bobina</span>
                    </div>
                    <div class="sm:hidden flex items-center gap-1.5 leading-none mt-1">
                        <span class="font-bold text-[11px] text-slate-700">TintaPerfetta</span>
                        <span class="px-1.5 py-0.2 text-[8px] font-bold bg-rose-50 text-rose-800 rounded border border-rose-200">CMYK Matrix</span>
                    </div>
                </div>
            </div>

            <!-- Quick Actions: Switcher + Language + App + Action Buttons -->
            <div class="flex items-center gap-1.5 sm:gap-2 shrink-0">
                <a href="/dorso" class="no-print inline-flex items-center gap-1 px-2 py-1.5 text-xs font-bold text-slate-600 hover:text-purple-600 bg-slate-100 hover:bg-purple-50 rounded-xl border border-slate-200 transition" title="Dorso Libro">
                    <span>📖</span>
                    <span class="hidden md:inline">Dorso</span>
                </a>
                <a href="/dpi" class="no-print inline-flex items-center gap-1 px-2 py-1.5 text-xs font-bold text-slate-600 hover:text-emerald-600 bg-slate-100 hover:bg-emerald-50 rounded-xl border border-slate-200 transition" title="Risoluzione & DPI">
                    <span>🖼️</span>
                    <span class="hidden md:inline">DPI</span>
                </a>

                <!-- Language Selector -->
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

                <button onclick="triggerInstall()" id="headerInstallBtn" class="no-print inline-flex items-center justify-center p-1.5 sm:px-2.5 sm:py-1.5 text-xs font-bold text-rose-800 bg-rose-50 hover:bg-rose-100 active:scale-95 rounded-xl border border-rose-200 transition" title="Installa come App">
                    <span>📲</span>
                    <span id="headerInstallText" class="hidden sm:inline">App</span>
                </button>

                <!-- PDF Direct Download Button -->
                <button onclick="downloadVectorPdf()" class="no-print inline-flex items-center justify-center p-1.5 sm:px-3 sm:py-1.5 text-xs font-bold text-white bg-rose-900 hover:bg-rose-950 active:scale-95 rounded-xl transition shadow-xs" title="Scarica file PDF vettoriale pronto per il RIP">
                    <span>📥</span>
                    <span class="hidden sm:inline ml-1 font-extrabold">PDF Pronto</span>
                </button>
            </div>
        </div>
    </header>

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

                    <!-- Input Mode Toggle -->
                    <div class="bg-slate-100 p-1 rounded-xl flex text-xs font-bold">
                        <button type="button" id="btnModeCmyk" onclick="switchInputMode('cmyk')" class="flex-1 py-1 rounded-lg bg-white text-rose-900 shadow-2xs transition">CMYK</button>
                        <button type="button" id="btnModeHex" onclick="switchInputMode('hex')" class="flex-1 py-1 rounded-lg text-slate-600 transition">HEX / RGB</button>
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

                        <!-- Strip Height (Waste along roll length) -->
                        <div>
                            <label id="stripHeightLabel" class="text-xs font-bold text-slate-700 block mb-1">Altezza Striscia (Consumo Lineare)</label>
                            <select id="stripHeightSelect" onchange="onCustomDimensionsChange()" class="w-full bg-slate-50 border border-slate-200 rounded-xl p-2 text-xs font-bold text-slate-800 cursor-pointer focus:outline-none focus:border-rose-700">
                                <option value="5">5 cm (Striscia Compatta 1 Riga — Minimo Spreco)</option>
                                <option value="8" selected>8 cm (Striscia Standard 2 Righe)</option>
                                <option value="12">12 cm (Striscia Estesa 3 Righe)</option>
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

    <!-- Footer -->
    <footer class="no-print bg-white border-t border-slate-200 pt-8 pb-10 text-xs text-slate-500">
        <div class="max-w-5xl mx-auto px-4 space-y-5">
            <!-- Suite Navigation -->
            <div class="flex items-center justify-center gap-3 text-xs font-bold text-slate-600 flex-wrap pb-1">
                <a href="/rampe" class="hover:text-blue-600 transition">RampaFacile</a>
                <span>•</span>
                <a href="/scale" class="hover:text-blue-600 transition">ScalaFacile</a>
                <span>•</span>
                <a href="/tubi" class="hover:text-blue-600 transition">ScaricoFacile</a>
                <span>•</span>
                <a href="/dorso" class="hover:text-blue-600 transition">DorsoFacile</a>
                <span>•</span>
                <a href="/dpi" class="hover:text-blue-600 transition">RisoluzioneFacile</a>
                <span>•</span>
                <a href="/tinta" class="text-rose-900 font-extrabold">TintaPerfetta</a>
                <span>•</span>
                <a href="/partnership" class="text-indigo-600 hover:underline">🤝 Diventa Partner / Sponsor</a>
            </div>

            <!-- Disclaimer and Rights -->
            <div class="text-center space-y-1.5">
                <p id="rightsText" class="font-bold text-slate-600">© 2026 OmniTools Lab — Divisione OmniGraph. Tutti i diritti riservati.</p>
                <p id="legalDisclaimerText" class="text-[10px] text-slate-500 leading-relaxed max-w-2xl mx-auto">
                    <strong>Note Tecniche di Laboratorio:</strong> La presente matrice genera valori percentuali CMYK matematici standard. La resa finale effettiva dipende dal profilo ICC di macchina, dalla calibrazione del RIP, dal punto termico e dalla porosità del supporto di stampa.
                </p>
            </div>
        </div>
    </footer>

    <!-- Logic Script -->
    <script>
        const TRANSLATIONS = {t_json_str};

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

        function applyTranslations() {{
            const t = TRANSLATIONS[currentLang] || TRANSLATIONS['it'];
            if (t.hero_title) document.getElementById('heroTitle').textContent = t.hero_title;
            if (t.hero_desc) document.getElementById('heroDesc').textContent = t.hero_desc;
            if (t.input_section_title) document.getElementById('inputSectionTitle').textContent = t.input_section_title;
            if (t.input_section_sub) document.getElementById('inputSectionSub').textContent = t.input_section_sub;
            if (t.preset_label) document.getElementById('presetLabel').textContent = t.preset_label;
            if (t.config_section_title) document.getElementById('configSectionTitle').textContent = t.config_section_title;
            if (t.grid_title) document.getElementById('gridTitle').textContent = t.grid_title;
            if (t.grid_sub) document.getElementById('gridSub').textContent = t.grid_sub;
            if (t.btn_print) document.getElementById('btnPrintMatrix').textContent = t.btn_print;
            if (t.share_title) document.getElementById('shareTitleText').textContent = t.share_title;
            if (t.share_sub) document.getElementById('shareSubText').textContent = t.share_sub;
            if (t.share_copy) document.getElementById('shareCopyText').textContent = t.share_copy;
            if (t.rights_reserved) document.getElementById('rightsText').textContent = t.rights_reserved;
            if (t.legal_disclaimer) document.getElementById('legalDisclaimerText').innerHTML = t.legal_disclaimer;
            if (t.print_sheet_title) document.getElementById('printSheetTitle').textContent = t.print_sheet_title;
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
            const cmykGroup = document.getElementById('cmykControlsGroup');
            const hexGroup = document.getElementById('hexControlsGroup');

            if (mode === 'cmyk') {{
                btnCmyk.className = "flex-1 py-1 rounded-lg bg-white text-rose-900 shadow-2xs transition font-bold";
                btnHex.className = "flex-1 py-1 rounded-lg text-slate-600 transition font-bold";
                cmykGroup.classList.remove('hidden');
                hexGroup.classList.add('hidden');
            }} else {{
                btnHex.className = "flex-1 py-1 rounded-lg bg-white text-rose-900 shadow-2xs transition font-bold";
                btnCmyk.className = "flex-1 py-1 rounded-lg text-slate-600 transition font-bold";
                hexGroup.classList.remove('hidden');
                cmykGroup.classList.add('hidden');
            }}
        }}

        // ==========================================
        // MEDIA FORMAT & DIMENSION LOGIC
        // ==========================================
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
                let stripHeightCm = parseFloat(document.getElementById('stripHeightSelect').value) || 8.0;
                wMm = Math.round(wCm * 10);
                hMm = Math.round(stripHeightCm * 10);
            }}

            currentWidthMm = wMm;
            currentHeightMm = hMm;

            const wCmStr = (wMm / 10).toFixed(1).replace('.0', '');
            const hCmStr = (hMm / 10).toFixed(1).replace('.0', '');
            const dimText = `${{wCmStr}} × ${{hCmStr}} cm`;

            document.getElementById('liveSizeIndicator').textContent = dimText;
            document.getElementById('printFormatName').textContent = dimText;
            document.getElementById('matrixDimFooter').textContent = `Dimensioni Foglio: ${{dimText}} • FOGRA39`;
            document.getElementById('badgeFormatIndicator').textContent = dimText;

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
            document.getElementById('printStepName').textContent = `±${{step}}%`;
            generateMatrix();
        }}

        function updateInputsFromState() {{
            document.getElementById('cSlider').value = baseC;
            document.getElementById('mSlider').value = baseM;
            document.getElementById('ySlider').value = baseY;
            document.getElementById('kSlider').value = baseK;

            document.getElementById('cValText').textContent = baseC + '%';
            document.getElementById('mValText').textContent = baseM + '%';
            document.getElementById('yValText').textContent = baseY + '%';
            document.getElementById('kValText').textContent = baseK + '%';

            updatePreviewAndTac();
        }}

        function updatePreviewAndTac() {{
            document.getElementById('cValText').textContent = baseC + '%';
            document.getElementById('mValText').textContent = baseM + '%';
            document.getElementById('yValText').textContent = baseY + '%';
            document.getElementById('kValText').textContent = baseK + '%';

            const rgb = cmykToRgb(baseC, baseM, baseY, baseK);
            const hex = rgbToHex(rgb.r, rgb.g, rgb.b);
            document.getElementById('previewSwatch').style.backgroundColor = hex;
            document.getElementById('nativeColorPicker').value = hex;
            document.getElementById('hexInput').value = hex.toUpperCase();

            const tac = baseC + baseM + baseY + baseK;
            document.getElementById('tacValue').textContent = tac + '%';

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

            document.getElementById('printJobName').textContent = job;
            document.getElementById('printPressName').textContent = press;
            document.getElementById('printPaperName').textContent = paper;
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

            // Dimensions and layout adaptation:
            // If roll mode:
            // 1 riga se altezza <= 6cm, 2 righe se 8cm, 3 righe se 12cm.
            // Colonne: da 7 a 11 a seconda della larghezza bobina!
            let cols = 7;
            let rows = 5;

            if (feedType === 'roll') {{
                const stripH = parseFloat(document.getElementById('stripHeightSelect').value) || 8;
                rows = stripH <= 5 ? 1 : (stripH <= 8 ? 2 : 3);
                const wCm = currentWidthMm / 10;
                cols = wCm >= 45 ? 11 : (wCm >= 30 ? 9 : 7);
            }} else {{
                // Sheet Mode
                if (currentWidthMm > currentHeightMm) {{
                    // Landscape
                    cols = 9;
                    rows = 5;
                }} else {{
                    cols = 7;
                    rows = 5;
                }}
            }}

            const centerCol = Math.floor(cols / 2);
            const centerRow = Math.floor(rows / 2);

            const rowLetters = ['A', 'B', 'C', 'D', 'E', 'F', 'G'];

            currentGridCells = [];

            const table = document.createElement('table');
            table.className = "w-full border-collapse text-center text-[10px] select-none";

            // Table Header: Column Indices
            const thead = document.createElement('thead');
            const trHead = document.createElement('tr');
            trHead.className = "border-b border-slate-200";
            
            const thCorner = document.createElement('th');
            thCorner.className = "p-1 text-slate-400 font-mono text-[9px]";
            thCorner.textContent = "R/C";
            trHead.appendChild(thCorner);

            for (let c = 0; c < cols; c++) {{
                const th = document.createElement('th');
                th.className = "p-1 text-slate-600 font-mono text-[10px] font-bold";
                const deltaCol = (c - centerCol) * step;
                th.innerHTML = `${{c + 1}}<br><span class=\"text-[8px] font-normal text-slate-400\">${{deltaCol >= 0 ? '+' : ''}}${{deltaCol}}%</span>`;
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
                tdRowLabel.className = "p-1 font-mono font-bold text-slate-600 text-xs";
                tdRowLabel.innerHTML = `${{rowLetters[r]}}<br><span class=\"text-[8px] font-normal text-slate-400\">${{deltaRow >= 0 ? '+' : ''}}${{deltaRow}}%</span>`;
                tr.appendChild(tdRowLabel);

                for (let c = 0; c < cols; c++) {{
                    const td = document.createElement('td');
                    td.className = "p-1";

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

                    // Swatch Box Element
                    const swatchBtn = document.createElement('button');
                    swatchBtn.type = "button";
                    swatchBtn.className = `color-swatch-box matrix-cell w-full h-14 sm:h-16 rounded-xl flex flex-col justify-between p-1 text-left relative cursor-pointer border ${{
                        isCenter ? 'border-2 border-amber-400 ring-2 ring-amber-400/50 shadow-md' : 'border-black/10 shadow-2xs'
                    }}`;
                    swatchBtn.style.backgroundColor = hex;

                    const isDark = (rgb.r * 0.299 + rgb.g * 0.587 + rgb.b * 0.114) < 140;
                    const textColor = isDark ? '#ffffff' : '#0f172a';

                    swatchBtn.innerHTML = `
                        <div class=\"flex items-center justify-between leading-none\" style=\"color: ${{textColor}}\">
                            <span class=\"font-mono font-black text-[9px] sm:text-[10px]\">${{coordName}}</span>
                            ${{isCenter ? '<span class=\"text-[9px]\">★</span>' : ''}}
                        </div>
                        <div class=\"font-mono font-bold text-[7.5px] sm:text-[8.5px] leading-tight\" style=\"color: ${{textColor}}\">
                            ${{tileC}}/${{tileM}}/${{tileY}}/${{tileK}}
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
            document.getElementById('inspectorCoord').textContent = `${{cell.coord}} ${{cell.isCenter ? '(Centro)' : ''}}`;
            document.getElementById('inspectorTac').textContent = `TAC: ${{cell.tac}}%`;

            document.getElementById('inspectC').textContent = cell.c + '%';
            document.getElementById('inspectM').textContent = cell.m + '%';
            document.getElementById('inspectY').textContent = cell.y + '%';
            document.getElementById('inspectK').textContent = cell.k + '%';
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
            const cellH = Math.min(22, (gridH - (gap * (totalRows - 1))) / totalRows);

            // Draw Swatches
            currentGridCells.forEach(cell => {{
                const x = margin + 2 + (cell.col * (cellW + gap));
                const y = gridStartY + (cell.row * (cellH + gap));

                // Fill Color
                doc.setFillColor(cell.rgb.r, cell.rgb.g, cell.rgb.b);
                doc.roundedRect(x, y, cellW, cellH, 1, 1, 'F');

                // Border
                if (cell.isCenter) {{
                    doc.setDrawColor(245, 158, 11); // Amber-500
                    doc.setLineWidth(0.6);
                    doc.roundedRect(x, y, cellW, cellH, 1, 1, 'D');
                }} else {{
                    doc.setDrawColor(0, 0, 0, 0.15);
                    doc.setLineWidth(0.1);
                    doc.roundedRect(x, y, cellW, cellH, 1, 1, 'D');
                }}

                // Text Contrast
                const isDark = (cell.rgb.r * 0.299 + cell.rgb.g * 0.587 + cell.rgb.b * 0.114) < 140;
                doc.setTextColor(isDark ? 255 : 15, isDark ? 255 : 23, isDark ? 255 : 42);

                // Coordinate label (Top Left)
                doc.setFont('helvetica', 'bold');
                doc.setFontSize(cellH > 15 ? 7 : 6);
                doc.text(cell.coord + (cell.isCenter ? ' *' : ''), x + 1.2, y + 3.2);

                // CMYK Formula (Bottom Left)
                doc.setFont('helvetica', 'bold');
                doc.setFontSize(cellH > 15 ? 6.5 : 5.5);
                doc.text(`${{cell.c}}/${{cell.m}}/${{cell.y}}/${{cell.k}}`, x + 1.2, y + cellH - 1.5);
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
