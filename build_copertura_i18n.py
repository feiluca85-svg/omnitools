import json
import os
from nav_header import render_suite_header, render_suite_header_js
from unified_footer import render_unified_footer, render_unified_footer_js

# Load translations
with open('/Users/ilalu/Documents/Altenative Businnes/Calcolatore_Pendenza/translations_copertura.json', 'r', encoding='utf-8') as f:
    t_data = json.load(f)

t_json_str = json.dumps(t_data, ensure_ascii=False)

header_html = render_suite_header("copertura")
header_js = render_suite_header_js()

footer_html = render_unified_footer("copertura", disclaimer_id="legalDisclaimerText", disclaimer_default=t_data["it"]["legal_disclaimer"])
footer_js = render_unified_footer_js()

it_t = t_data["it"]

html_code = f"""<!DOCTYPE html>
<html lang="it">
<head>
    <meta name="google-site-verification" content="MRdbDm9lLhokeD3I0FOpUSOhNaF_2WaveKvu52FxtG4">
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0">
    <title>Calcolo Copertura Inchiostro CMYK Online & TAC — Preventivo Stampa & Costo Copia</title>
    <meta name="description" content="Analisi densitometrica gratuita dei canali CMYK e verifica del TAC (Total Area Coverage) in tempo reale. Calcola il consumo di inchiostro in grammi e il costo per copia per tirature offset e digitali. 100% riservato nel tuo browser.">
    
    <!-- Canonical & SEO Meta Tags -->
    <link rel="canonical" href="https://www.omnitoolslab.com/copertura">
    <meta name="robots" content="index, follow">
    <meta property="og:type" content="website">
    <meta property="og:title" content="CoperturaFacile — Calcolo Copertura Inchiostro CMYK & Costo Copia">
    <meta property="og:description" content="Misura la copertura percentuale C, M, Y, K, rileva picchi TAC critici e stima il costo inchiostro della tiratura. Zero upload: 100% client-side privacy.">
    <meta property="og:url" content="https://www.omnitoolslab.com/copertura">
    <meta property="og:site_name" content="OmniTools Lab">
    <meta property="og:image" content="https://www.omnitoolslab.com/og-graph.png">
    <meta name="twitter:card" content="summary_large_image">

    <!-- Schema.org JSON-LD Structured Data (WebApplication + FAQPage) -->
    <script type="application/ld+json">
    [
      {{
        "@context": "https://schema.org",
        "@type": "WebApplication",
        "name": "CoperturaFacile — Calcolo Copertura Inchiostro CMYK",
        "url": "https://www.omnitoolslab.com/copertura",
        "applicationCategory": "DesignApplication",
        "operatingSystem": "All",
        "description": "Strumento professionale di prestampa per misurare la copertura percentuale di inchiostro CMYK, mappare le aree TAC critiche e calcolare i costi di tiratura.",
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
            "name": "Come si calcola la copertura percentuale di inchiostro in una pagina?",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "La copertura di un singolo colore (C, M, Y o K) corrisponde alla media ponderata della densità di quel colore su tutti i pixel dell'area stampabile."
            }}
          }},
          {{
            "@type": "Question",
            "name": "Perché le tipografie e i centri stampa chiedono la percentuale di copertura?",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "I contratti di noleggio e toner si basano su una copertura standard del 5% per colore. Pagine con fondi pieni o fotografie consumano fino a 10 volte più inchiostro."
            }}
          }},
          {{
            "@type": "Question",
            "name": "Cosa indica la Mappa Termica TAC (Heatmap)?",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "Evidenzia in rosso le coordinate dove la somma degli inchiostri supera il 310%, segnalando il rischio di sbavature e fogli incollati."
            }}
          }},
          {{
            "@type": "Question",
            "name": "I file caricati vengono salvati o inviati a qualche server?",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "No. Il calcolo viene eseguito al 100% all'interno della memoria RAM del tuo browser tramite l'API Canvas di HTML5."
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
    <meta name="theme-color" content="#881337">

    <!-- PDF.js library for direct client-side PDF rendering -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.min.js"></script>
    <script>
        if (window['pdfjs-dist/build/pdf']) {{
            pdfjsLib.GlobalWorkerOptions.workerSrc = 'https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.worker.min.js';
        }}
    </script>

    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <script defer src="/_vercel/insights/script.js"></script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;700&display=swap" rel="stylesheet">

    <style>
        body {{
            font-family: 'Plus Jakarta Sans', sans-serif;
        }}
        .font-mono {{
            font-family: 'JetBrains Mono', monospace;
        }}
        .font-jakarta {{
            font-family: 'Plus Jakarta Sans', sans-serif;
        }}
        
        /* A4 Professional Print Standard (Strictly 1 Page) */
        @media print {{
            @page {{
                size: A4 portrait;
                margin: 5mm 8mm;
            }}
            body {{
                background: white !important;
                color: #0f172a !important;
                font-size: 7.5pt !important;
                line-height: 1.15 !important;
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
                box-shadow: none !important;
                border: none !important;
            }}
            .print-card {{
                border: 1px solid #cbd5e1 !important;
                box-shadow: none !important;
                padding: 8px 10px !important;
                margin-bottom: 6px !important;
                page-break-inside: avoid !important;
                border-radius: 6px !important;
            }}
            #mainCanvas {{
                max-height: 100px !important;
            }}
            .grid {{
                gap: 8px !important;
            }}
            h3 {{
                font-size: 8pt !important;
                margin-bottom: 2px !important;
            }}
            .mb-5, .mb-4, .mb-3 {{
                margin-bottom: 3px !important;
            }}
            .space-y-3\\.5 > :not([hidden]) ~ :not([hidden]) {{
                margin-top: 3px !important;
            }}
            .grid.grid-cols-1.lg\\:grid-cols-12 {{
                display: grid !important;
                grid-template-columns: 1fr 1fr !important;
                gap: 10px !important;
            }}
            .lg\\:col-span-7, .lg\\:col-span-5 {{
                width: 100% !important;
            }}
        }}
        
        @media screen {{
            .print-only {{
                display: none !important;
            }}
        }}

        .drag-active {{
            border-color: #be123c !important;
            background-color: #fff1f2 !important;
        }}
    </style>
</head>
<body class="bg-slate-50 text-slate-800 antialiased min-h-screen flex flex-col justify-between selection:bg-rose-500 selection:text-white">

    <!-- Suite Header with Global Navigation -->
    <div class="no-print w-full bg-white border-b border-slate-200 sticky top-0 z-50">
        {header_html}
    </div>

    <!-- PRINT HEADER (Strictly A4 Official Spec) -->
    <div class="print-only mb-3 pb-2 border-b-2 border-rose-900">
        <div class="flex items-center justify-between">
            <div class="flex items-center gap-3">
                <div class="w-10 h-10 bg-rose-900 text-white rounded-lg flex items-center justify-center font-bold text-lg">
                    OG
                </div>
                <div>
                    <h1 class="text-base font-extrabold uppercase tracking-tight text-slate-900">OmniGraph • CoperturaFacile</h1>
                    <p class="text-[9pt] font-semibold text-slate-600">Scheda Tecnica Densitometrica CMYK & Preventivo Tiratura</p>
                </div>
            </div>
            <div class="text-right">
                <span class="inline-block px-2 py-0.5 text-[8pt] font-extrabold tracking-wider bg-rose-100 text-rose-900 rounded border border-rose-300 uppercase">Documento Ufficiale</span>
                <p class="text-[7.5pt] text-slate-500 mt-0.5">Generato: <span id="printDateStamp"></span> | omnitoolslab.com</p>
            </div>
        </div>
    </div>

    <!-- MAIN CONTAINER -->
    <main class="max-w-5xl mx-auto px-3 sm:px-6 py-2.5 sm:py-5 flex-1 w-full space-y-3 sm:space-y-5 page-container">
        
        <!-- Hero Header -->
        <div id="heroContainer" class="no-print text-center max-w-2xl mx-auto space-y-1.5 sm:space-y-2 pt-1 sm:pt-2">
            <div class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-rose-50 border border-rose-200/80 text-[11px] font-extrabold text-rose-800 tracking-wide uppercase">
                <span>🖨️</span>
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
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-6">

            <!-- LEFT COLUMN: UPLOAD, PREVIEW & SETTINGS (7 COLS) -->
            <div class="lg:col-span-7 flex flex-col gap-5">
                
                <!-- UPLOAD DROPZONE -->
                <div class="no-print bg-white rounded-2xl p-5 border-2 border-dashed border-slate-300 hover:border-rose-400 transition-all cursor-pointer text-center relative group shadow-xs" id="dropArea">
                    <input type="file" id="fileInput" accept="image/png, image/jpeg, image/webp, application/pdf" class="hidden">
                    <div class="py-4">
                        <div class="w-14 h-14 mx-auto rounded-2xl bg-rose-50 text-rose-600 flex items-center justify-center text-2xl mb-3 group-hover:scale-105 transition">
                            📥
                        </div>
                        <h3 id="dropTitle" class="text-base font-bold text-slate-800">
                            {it_t["dropzone_title"]}
                        </h3>
                        <p id="dropSub" class="text-xs text-slate-500 mt-1">
                            {it_t["dropzone_sub"]}
                        </p>
                        <p class="text-[11px] text-slate-400 mt-2 font-mono">
                            Supporta PNG, JPG, WebP e PDF (Prima Pagina) • Max 50 MB
                        </p>
                    </div>
                </div>

                <!-- PRESET BUTTONS FOR QUICK TESTING -->
                <div class="no-print bg-white rounded-2xl p-4 border border-slate-200 shadow-xs">
                    <label id="presetLabel" class="block text-xs font-bold text-slate-500 uppercase tracking-wider mb-2.5">
                        {it_t["sample_presets_label"]}
                    </label>
                    <div class="grid grid-cols-1 sm:grid-cols-3 gap-2">
                        <button onclick="loadSamplePreset('flyer')" class="px-3 py-2 rounded-xl text-xs font-bold bg-rose-50 text-rose-800 border border-rose-200 hover:bg-rose-100 active:scale-95 transition text-left flex items-center gap-1.5">
                            <span>🎨</span>
                            <span id="btnSampleFlyer">{it_t["sample_flyer"]}</span>
                        </button>
                        <button onclick="loadSamplePreset('book')" class="px-3 py-2 rounded-xl text-xs font-bold bg-blue-50 text-blue-800 border border-blue-200 hover:bg-blue-100 active:scale-95 transition text-left flex items-center gap-1.5">
                            <span>📖</span>
                            <span id="btnSampleBook">{it_t["sample_book"]}</span>
                        </button>
                        <button onclick="loadSamplePreset('minimal')" class="px-3 py-2 rounded-xl text-xs font-bold bg-slate-100 text-slate-800 border border-slate-200 hover:bg-slate-200 active:scale-95 transition text-left flex items-center gap-1.5">
                            <span>🖋️</span>
                            <span id="btnSampleMinimal">{it_t["sample_minimal"]}</span>
                        </button>
                    </div>
                </div>

                <!-- VISUAL PREVIEW & HEATMAP SWITCH -->
                <div class="bg-white rounded-2xl p-4 sm:p-5 border border-slate-200 shadow-xs print-card">
                    <div class="flex items-center justify-between mb-3">
                        <div class="flex items-center gap-2">
                            <h3 class="text-sm font-extrabold text-slate-800 uppercase tracking-wider">Anteprima del Documento</h3>
                            <span id="fileBadge" class="text-[10px] font-bold px-2 py-0.5 rounded-full bg-slate-100 text-slate-600 font-mono">Volantino Campione</span>
                        </div>
                        
                        <!-- Heatmap Toggle -->
                        <div class="no-print flex items-center gap-2">
                            <label for="heatmapToggle" class="text-xs font-bold text-slate-700 cursor-pointer flex items-center gap-1.5">
                                <span>🔥</span>
                                <span id="heatmapToggleText">{it_t["heatmap_toggle"]}</span>
                            </label>
                            <input type="checkbox" id="heatmapToggle" onchange="toggleHeatmap(this.checked)" class="w-4 h-4 rounded text-rose-600 focus:ring-rose-500 cursor-pointer">
                        </div>
                    </div>

                    <!-- Canvas Stage -->
                    <div class="w-full bg-slate-100 rounded-xl overflow-hidden border border-slate-200 flex items-center justify-center p-2 relative min-h-[220px]">
                        <canvas id="mainCanvas" class="max-h-[340px] max-w-full rounded shadow-sm object-contain bg-white"></canvas>
                        <canvas id="heatmapCanvas" class="max-h-[340px] max-w-full rounded shadow-sm object-contain absolute top-2 left-1/2 -translate-x-1/2 pointer-events-none hidden"></canvas>
                    </div>

                    <div id="heatmapLegend" class="no-print hidden mt-2.5 p-2 rounded-lg bg-slate-50 border border-slate-200 text-[11px] text-slate-600 flex flex-wrap items-center justify-between gap-2">
                        <span class="font-bold text-slate-700">Mappa Termica TAC:</span>
                        <div class="flex items-center gap-3">
                            <span class="flex items-center gap-1"><span class="w-2.5 h-2.5 rounded-full bg-emerald-500 inline-block"></span> &lt; 260% Sicuro</span>
                            <span class="flex items-center gap-1"><span class="w-2.5 h-2.5 rounded-full bg-amber-500 inline-block"></span> 260-310% Attenzione</span>
                            <span class="flex items-center gap-1"><span class="w-2.5 h-2.5 rounded-full bg-red-600 inline-block"></span> &gt; 310% Eccessivo</span>
                        </div>
                    </div>
                </div>

                <!-- COMMODITY & MACHINE INPUT SETTINGS -->
                <div class="bg-white rounded-2xl p-5 border border-slate-200 shadow-xs print-card">
                    <h3 id="costSettingsTitle" class="text-sm font-extrabold text-slate-800 uppercase tracking-wider mb-4 flex items-center gap-2">
                        <span>⚙️</span>
                        <span>{it_t["cost_calculator_title"]}</span>
                    </h3>

                    <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                        <!-- Paper Format -->
                        <div>
                            <label id="lblPaperFormat" class="block text-xs font-bold text-slate-700 mb-1">{it_t["paper_format_label"]}</label>
                            <select id="paperFormat" onchange="onFormatChange()" class="w-full bg-slate-50 border border-slate-300 rounded-xl px-3 py-2 text-xs font-bold text-slate-800 focus:ring-2 focus:ring-rose-500 focus:outline-none">
                                <option value="a4" selected>A4 (210 × 297 mm)</option>
                                <option value="a3">A3 (297 × 420 mm)</option>
                                <option value="sra3">SRA3 (320 × 450 mm)</option>
                                <option value="70x100">70 × 100 cm (Foglio Offset)</option>
                                <option value="64x88">64 × 88 cm (Foglio Macchina)</option>
                                <option value="custom">Personalizzato (mm)</option>
                            </select>
                        </div>

                        <!-- Copies Run -->
                        <div>
                            <label id="lblCopies" class="block text-xs font-bold text-slate-700 mb-1">{it_t["copies_label"]}</label>
                            <input type="number" id="copiesCount" value="1000" min="1" step="50" oninput="calculateCosts()" class="w-full bg-slate-50 border border-slate-300 rounded-xl px-3 py-2 text-xs font-bold text-slate-800 font-mono focus:ring-2 focus:ring-rose-500 focus:outline-none">
                        </div>

                        <!-- Custom Dimensions (hidden by default) with Unit Switcher -->
                        <div id="customDimBox" class="sm:col-span-2 hidden p-3 bg-rose-50/50 rounded-xl border border-rose-200 space-y-2">
                            <div class="flex items-center justify-between pb-1 border-b border-rose-200/60">
                                <span class="text-[11px] font-bold text-rose-900 uppercase tracking-wide">Dimensioni Personalizzate</span>
                                <div class="inline-flex p-0.5 bg-white rounded-lg border border-rose-200 gap-1 text-[10px] font-bold">
                                    <button type="button" id="copUnitMm" onclick="setCopUnit('mm')" class="px-2 py-0.5 rounded bg-rose-100 text-rose-800 font-extrabold">mm</button>
                                    <button type="button" id="copUnitCm" onclick="setCopUnit('cm')" class="px-2 py-0.5 rounded text-slate-600 hover:text-slate-900">cm</button>
                                    <button type="button" id="copUnitIn" onclick="setCopUnit('in')" class="px-2 py-0.5 rounded text-slate-600 hover:text-slate-900">in</button>
                                </div>
                            </div>
                            <div class="grid grid-cols-2 gap-3">
                                <div>
                                    <label class="block text-[11px] font-bold text-slate-600 mb-1">Larghezza Foglio (<span class="copUnitBadge">mm</span>)</label>
                                    <input type="number" id="customWidth" value="210" min="1" max="3000" oninput="calculateCosts()" class="w-full bg-white border border-slate-300 rounded-lg px-2.5 py-1.5 text-xs font-bold font-mono">
                                </div>
                                <div>
                                    <label class="block text-[11px] font-bold text-slate-600 mb-1">Altezza Foglio (<span class="copUnitBadge">mm</span>)</label>
                                    <input type="number" id="customHeight" value="297" min="1" max="3000" oninput="calculateCosts()" class="w-full bg-white border border-slate-300 rounded-lg px-2.5 py-1.5 text-xs font-bold font-mono">
                                </div>
                            </div>
                        </div>

                        <!-- Print Technology Preset -->
                        <div>
                            <label id="lblTech" class="block text-xs font-bold text-slate-700 mb-1">{it_t["tech_label"]}</label>
                            <select id="techPreset" onchange="onTechChange()" class="w-full bg-slate-50 border border-slate-300 rounded-xl px-3 py-2 text-xs font-bold text-slate-800 focus:ring-2 focus:ring-rose-500 focus:outline-none">
                                <option value="laser" selected>Laser Digitale Toner (~1.2 g/m² @ 100%)</option>
                                <option value="inkjet">Plotter Inkjet Base Acqua (~1.8 g/m² @ 100%)</option>
                                <option value="offset">Offset a Foglio (~1.5 g/m² @ 100%)</option>
                                <option value="custom">Personalizzato</option>
                            </select>
                        </div>

                        <!-- Ink Price -->
                        <div>
                            <label id="lblInkPrice" class="block text-xs font-bold text-slate-700 mb-1">{it_t["ink_price_label"]}</label>
                            <div class="relative">
                                <span class="absolute left-3 top-2 text-xs font-bold text-slate-400">€</span>
                                <input type="number" id="inkPricePerKg" value="45.00" min="1" step="0.5" oninput="calculateCosts()" class="w-full bg-slate-50 border border-slate-300 rounded-xl pl-7 pr-3 py-2 text-xs font-bold text-slate-800 font-mono focus:ring-2 focus:ring-rose-500 focus:outline-none">
                            </div>
                        </div>
                    </div>
                </div>

            </div>

            <!-- RIGHT COLUMN: RESULTS, TAC GAUGE & COST SUMMARY (5 COLS) -->
            <div class="lg:col-span-5 flex flex-col gap-5">
                
                <!-- CMYK SEPARATIONS & COVERAGE RESULTS -->
                <div class="bg-white rounded-2xl p-5 border border-slate-200 shadow-xs print-card">
                    <h3 id="analysisTitle" class="text-sm font-extrabold text-slate-800 uppercase tracking-wider mb-4 flex items-center justify-between">
                        <span>{it_t["analysis_title"]}</span>
                        <span class="text-[11px] font-bold text-slate-400 font-mono">ISO 12647</span>
                    </h3>

                    <!-- 4 Process Ink Progress Bars -->
                    <div class="space-y-3.5 mb-5">
                        <!-- Cyan -->
                        <div>
                            <div class="flex items-center justify-between text-xs font-bold mb-1">
                                <span class="flex items-center gap-1.5 text-sky-700">
                                    <span class="w-3 h-3 rounded-full bg-cyan-400 inline-block border border-cyan-500"></span>
                                    <span id="lblC">{it_t["c_label"]}</span>
                                </span>
                                <span id="valC" class="font-mono text-sm text-slate-900 font-extrabold">0.0%</span>
                            </div>
                            <div class="w-full h-3 bg-slate-100 rounded-full overflow-hidden p-0.5 border border-slate-200">
                                <div id="barC" class="h-full bg-cyan-400 rounded-full transition-all duration-300" style="width: 0%"></div>
                            </div>
                        </div>

                        <!-- Magenta -->
                        <div>
                            <div class="flex items-center justify-between text-xs font-bold mb-1">
                                <span class="flex items-center gap-1.5 text-pink-700">
                                    <span class="w-3 h-3 rounded-full bg-pink-500 inline-block border border-pink-600"></span>
                                    <span id="lblM">{it_t["m_label"]}</span>
                                </span>
                                <span id="valM" class="font-mono text-sm text-slate-900 font-extrabold">0.0%</span>
                            </div>
                            <div class="w-full h-3 bg-slate-100 rounded-full overflow-hidden p-0.5 border border-slate-200">
                                <div id="barM" class="h-full bg-pink-500 rounded-full transition-all duration-300" style="width: 0%"></div>
                            </div>
                        </div>

                        <!-- Yellow -->
                        <div>
                            <div class="flex items-center justify-between text-xs font-bold mb-1">
                                <span class="flex items-center gap-1.5 text-amber-700">
                                    <span class="w-3 h-3 rounded-full bg-yellow-400 inline-block border border-yellow-500"></span>
                                    <span id="lblY">{it_t["y_label"]}</span>
                                </span>
                                <span id="valY" class="font-mono text-sm text-slate-900 font-extrabold">0.0%</span>
                            </div>
                            <div class="w-full h-3 bg-slate-100 rounded-full overflow-hidden p-0.5 border border-slate-200">
                                <div id="barY" class="h-full bg-yellow-400 rounded-full transition-all duration-300" style="width: 0%"></div>
                            </div>
                        </div>

                        <!-- Key Black -->
                        <div>
                            <div class="flex items-center justify-between text-xs font-bold mb-1">
                                <span class="flex items-center gap-1.5 text-slate-800">
                                    <span class="w-3 h-3 rounded-full bg-slate-900 inline-block border border-black"></span>
                                    <span id="lblK">{it_t["k_label"]}</span>
                                </span>
                                <span id="valK" class="font-mono text-sm text-slate-900 font-extrabold">0.0%</span>
                            </div>
                            <div class="w-full h-3 bg-slate-100 rounded-full overflow-hidden p-0.5 border border-slate-200">
                                <div id="barK" class="h-full bg-slate-900 rounded-full transition-all duration-300" style="width: 0%"></div>
                            </div>
                        </div>
                    </div>

                    <!-- TAC METRICS -->
                    <div class="grid grid-cols-2 gap-3 pt-3 border-t border-slate-100 mb-4">
                        <div class="p-3 bg-slate-50 rounded-xl border border-slate-200 text-center">
                            <span id="lblTacAvg" class="block text-[11px] font-bold text-slate-500 uppercase">{it_t["tac_avg_label"]}</span>
                            <span id="valTacAvg" class="text-xl font-extrabold text-slate-900 font-mono">0.0%</span>
                        </div>
                        <div class="p-3 bg-slate-50 rounded-xl border border-slate-200 text-center">
                            <span id="lblTacPeak" class="block text-[11px] font-bold text-slate-500 uppercase">{it_t["tac_peak_label"]}</span>
                            <span id="valTacPeak" class="text-xl font-extrabold text-slate-900 font-mono">0.0%</span>
                        </div>
                    </div>

                    <!-- TAC COMPLIANCE STATUS BOX -->
                    <div id="tacStatusBox" class="p-3.5 rounded-xl border transition-all bg-emerald-50 border-emerald-200 text-emerald-900">
                        <h4 id="tacStatusTitle" class="text-xs font-extrabold flex items-center gap-1.5 mb-1">
                            {it_t["tac_safe_title"]}
                        </h4>
                        <p id="tacStatusDesc" class="text-[11px] leading-relaxed">
                            {it_t["tac_safe_desc"]}
                        </p>
                    </div>
                </div>

                <!-- COST BREAKDOWN & ESTIMATE -->
                <div class="bg-white rounded-2xl p-5 border border-slate-200 shadow-xs print-card">
                    <h3 id="resSummaryTitle" class="text-sm font-extrabold text-slate-800 uppercase tracking-wider mb-4 flex items-center justify-between">
                        <span>{it_t["res_summary_title"]}</span>
                        <span id="summaryBadge" class="text-[10px] font-bold px-2 py-0.5 rounded bg-emerald-100 text-emerald-800 font-mono">1.000 copie</span>
                    </h3>

                    <!-- Big Highlights -->
                    <div class="grid grid-cols-2 gap-3 mb-4">
                        <div class="p-3.5 bg-rose-50/70 rounded-xl border border-rose-200">
                            <span id="lblCostPerCopy" class="block text-[11px] font-bold text-rose-900/70 uppercase">{it_t["res_cost_per_copy"]}</span>
                            <div class="flex items-baseline gap-1 mt-0.5">
                                <span class="text-xs font-bold text-rose-800">€</span>
                                <span id="valCostPerCopy" class="text-xl font-black text-rose-950 font-mono">0.000</span>
                            </div>
                        </div>

                        <div class="p-3.5 bg-slate-900 text-white rounded-xl shadow-xs">
                            <span id="lblTotalCost" class="block text-[11px] font-bold text-slate-300 uppercase">{it_t["res_total_cost"]}</span>
                            <div class="flex items-baseline gap-1 mt-0.5">
                                <span class="text-xs font-bold text-rose-400">€</span>
                                <span id="valTotalCost" class="text-xl font-black text-white font-mono">0.00</span>
                            </div>
                        </div>
                    </div>

                    <!-- Grams per Separation Table -->
                    <div class="bg-slate-50 rounded-xl border border-slate-200 p-3 space-y-2 mb-4 text-xs font-mono">
                        <div class="flex justify-between items-center text-slate-600 font-bold border-b border-slate-200 pb-1">
                            <span>Separazione Colore</span>
                            <span>Grammi Tiratura</span>
                        </div>
                        <div class="flex justify-between items-center text-slate-800">
                            <span class="flex items-center gap-1.5"><span class="w-2 h-2 rounded-full bg-cyan-400"></span> Ciano</span>
                            <span id="gramC" class="font-bold">0.0 g</span>
                        </div>
                        <div class="flex justify-between items-center text-slate-800">
                            <span class="flex items-center gap-1.5"><span class="w-2 h-2 rounded-full bg-pink-500"></span> Magenta</span>
                            <span id="gramM" class="font-bold">0.0 g</span>
                        </div>
                        <div class="flex justify-between items-center text-slate-800">
                            <span class="flex items-center gap-1.5"><span class="w-2 h-2 rounded-full bg-yellow-400"></span> Giallo</span>
                            <span id="gramY" class="font-bold">0.0 g</span>
                        </div>
                        <div class="flex justify-between items-center text-slate-800">
                            <span class="flex items-center gap-1.5"><span class="w-2 h-2 rounded-full bg-slate-900"></span> Nero (K)</span>
                            <span id="gramK" class="font-bold">0.0 g</span>
                        </div>
                        <div class="flex justify-between items-center text-slate-900 font-extrabold border-t border-slate-200 pt-1.5">
                            <span>Totale Inchiostro Stimato:</span>
                            <span id="gramTotal" class="text-rose-700">0.0 g</span>
                        </div>
                    </div>

                    <!-- Action Buttons -->
                    <div class="no-print flex items-center gap-2">
                        <button onclick="window.print()" class="w-full py-2.5 px-4 rounded-xl text-xs font-extrabold bg-rose-800 hover:bg-rose-900 active:scale-95 text-white transition flex items-center justify-center gap-2 shadow-sm">
                            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 17h2a2 2 0 002-2v-4a2 2 0 00-2-2H5a2 2 0 00-2 2v4a2 2 0 002 2h2m2 4h6a2 2 0 002-2v-4a2 2 0 00-2-2H9a2 2 0 00-2 2v4a2 2 0 002 2zm8-12V5a2 2 0 00-2-2H9a2 2 0 00-2 2v4h10z" />
                            </svg>
                            <span id="btnPrintText">{it_t["print_btn"]}</span>
                        </button>
                    </div>

                    <!-- PRINT ONLY: SIGNATURE & LAB NOTES (Strictly Single Page A4) -->
                    <div class="print-only mt-4 pt-3 border-t border-slate-300 text-[8pt]">
                        <div class="grid grid-cols-2 gap-4">
                            <div class="border border-slate-300 rounded p-2">
                                <p class="font-bold text-slate-700 uppercase mb-1">Note Operative / RIP:</p>
                                <p class="text-slate-500 italic">Verificare profilo colore FOGRA39 / ISO Coated v2 prima dell'invio in macchina.</p>
                            </div>
                            <div class="border border-slate-300 rounded p-2 text-center flex flex-col justify-between min-h-[55px]">
                                <p class="font-bold text-slate-700 uppercase">Timbro e Firma Tecnico / Operatore:</p>
                                <div class="border-b border-dashed border-slate-400 w-3/4 mx-auto my-1"></div>
                                <p class="text-[7pt] text-slate-400">Data Approvazione Commessa</p>
                            </div>
                        </div>
                    </div>
                </div>

            </div>

        </div>

        <!-- EDUCATIONAL RULE TIP BOX -->
        <div class="no-print bg-rose-50/70 border border-rose-200/80 rounded-2xl p-4 text-xs text-rose-950 leading-relaxed shadow-2xs flex items-start gap-3">
            <span class="text-xl shrink-0">💡</span>
            <div id="ruleTipText">
                {it_t["rule_tip"]}
            </div>
        </div>

        <!-- FAQ ACCORDION SECTION (Unified OmniTools Lab Standard) -->
        <section id="faqSection" class="no-print bg-white rounded-3xl border border-slate-200/90 shadow-xs p-5 sm:p-7 space-y-4">
            <div class="flex items-center justify-between border-b border-slate-100 pb-3">
                <div class="flex items-center gap-2.5">
                    <span class="text-xl">❓</span>
                    <h2 class="text-base sm:text-lg font-black text-slate-900 font-jakarta flex items-center gap-2" id="faqTitle">
                        <span>Domande Frequenti su Copertura CMYK e TAC</span>
                    </h2>
                </div>
                <span class="text-[10px] font-extrabold uppercase px-2 py-0.5 rounded-full bg-slate-100 text-slate-600 border border-slate-200">FAQ</span>
            </div>
            
            <div id="faqContainer" class="space-y-3">
                <details class="group bg-slate-50/80 hover:bg-slate-50 rounded-2xl border border-slate-200/80 p-4 transition duration-150" open>
                    <summary class="flex justify-between items-center font-bold text-xs sm:text-sm text-slate-900 cursor-pointer list-none select-none">
                        <span id="faq1Q">{it_t["faq_1_q"]}</span>
                        <svg class="w-4 h-4 text-slate-400 group-open:-rotate-180 transition-transform duration-200 shrink-0 ml-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/>
                        </svg>
                    </summary>
                    <div id="faq1A" class="text-xs sm:text-sm text-slate-600 mt-2.5 leading-relaxed border-t border-slate-200/60 pt-2.5">
                        {it_t["faq_1_a"]}
                    </div>
                </details>

                <details class="group bg-slate-50/80 hover:bg-slate-50 rounded-2xl border border-slate-200/80 p-4 transition duration-150">
                    <summary class="flex justify-between items-center font-bold text-xs sm:text-sm text-slate-900 cursor-pointer list-none select-none">
                        <span id="faq2Q">{it_t["faq_2_q"]}</span>
                        <svg class="w-4 h-4 text-slate-400 group-open:-rotate-180 transition-transform duration-200 shrink-0 ml-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/>
                        </svg>
                    </summary>
                    <div id="faq2A" class="text-xs sm:text-sm text-slate-600 mt-2.5 leading-relaxed border-t border-slate-200/60 pt-2.5">
                        {it_t["faq_2_a"]}
                    </div>
                </details>

                <details class="group bg-slate-50/80 hover:bg-slate-50 rounded-2xl border border-slate-200/80 p-4 transition duration-150">
                    <summary class="flex justify-between items-center font-bold text-xs sm:text-sm text-slate-900 cursor-pointer list-none select-none">
                        <span id="faq3Q">{it_t["faq_3_q"]}</span>
                        <svg class="w-4 h-4 text-slate-400 group-open:-rotate-180 transition-transform duration-200 shrink-0 ml-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/>
                        </svg>
                    </summary>
                    <div id="faq3A" class="text-xs sm:text-sm text-slate-600 mt-2.5 leading-relaxed border-t border-slate-200/60 pt-2.5">
                        {it_t["faq_3_a"]}
                    </div>
                </details>

                <details class="group bg-slate-50/80 hover:bg-slate-50 rounded-2xl border border-slate-200/80 p-4 transition duration-150">
                    <summary class="flex justify-between items-center font-bold text-xs sm:text-sm text-slate-900 cursor-pointer list-none select-none">
                        <span id="faq4Q">{it_t["faq_4_q"]}</span>
                        <svg class="w-4 h-4 text-slate-400 group-open:-rotate-180 transition-transform duration-200 shrink-0 ml-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/>
                        </svg>
                    </summary>
                    <div id="faq4A" class="text-xs sm:text-sm text-slate-600 mt-2.5 leading-relaxed border-t border-slate-200/60 pt-2.5">
                        {it_t["faq_4_a"]}
                    </div>
                </details>
            </div>
        </section>

    </main>

    {footer_html}

    <!-- EMBEDDED TRANSLATION DATA -->
    <script>
        const I18N_DATA = {t_json_str};
        let currentLang = 'it';
    </script>

    <!-- CORE JAVASCRIPT LOGIC -->
    <script>
{header_js}
{footer_js}

        // Global State & Units
        let currentImage = null;
        let copUnit = 'mm';

        function setCopUnit(u) {{
            if (u === copUnit) return;
            const prev = copUnit;
            copUnit = u;

            ['mm', 'cm', 'in'].forEach(unit => {{
                const btn = document.getElementById('copUnit' + unit.charAt(0).toUpperCase() + unit.slice(1));
                if (btn) {{
                    if (unit === u) {{
                        btn.className = 'px-2 py-0.5 rounded bg-rose-100 text-rose-800 font-extrabold';
                    }} else {{
                        btn.className = 'px-2 py-0.5 rounded text-slate-600 hover:text-slate-900';
                    }}
                }}
            }});

            document.querySelectorAll('.copUnitBadge').forEach(el => el.textContent = u);

            const convertVal = (val, from, to) => {{
                let mm = val;
                if (from === 'cm') mm = val * 10;
                else if (from === 'in') mm = val * 25.4;

                if (to === 'cm') return parseFloat((mm / 10).toFixed(2));
                if (to === 'in') return parseFloat((mm / 25.4).toFixed(3));
                return Math.round(mm);
            }};

            ['customWidth', 'customHeight'].forEach(id => {{
                const el = document.getElementById(id);
                if (el && el.value) {{
                    const parsed = parseFloat(el.value);
                    if (!isNaN(parsed)) el.value = convertVal(parsed, prev, u);
                }}
            }});

            calculateCosts();
        }}
        let cmykData = {{ c: 0, m: 0, y: 0, k: 0, tacAvg: 0, tacPeak: 0 }};
        let pixelMap = null;
        let isHeatmapActive = false;

        // Paper area lookup (in square meters m²)
        const PAPER_AREAS = {{
            'a4': 0.210 * 0.297,      // 0.06237 m²
            'a3': 0.297 * 0.420,      // 0.12474 m²
            'sra3': 0.320 * 0.450,    // 0.14400 m²
            '70x100': 0.700 * 1.000,  // 0.70000 m²
            '64x88': 0.640 * 0.880,   // 0.56320 m²
            'custom': 0.06237
        }};

        // Technology specific consumption rates: grams of ink per m² at 100% solid coverage
        const TECH_FACTORS = {{
            'laser': 1.2,   // toner secco standard
            'inkjet': 1.8,  // inkjet base acqua / solvente
            'offset': 1.5,  // inchiostro offset a foglio
            'custom': 1.5
        }};

        // Initialize on DOM load
        document.addEventListener('DOMContentLoaded', function() {{
            initLanguage();
            setupDropZone();
            loadSamplePreset('flyer');
            updatePrintDate();
        }});

        function updatePrintDate() {{
            const now = new Date();
            const el = document.getElementById('printDateStamp');
            if (el) {{
                el.textContent = now.toLocaleDateString(currentLang === 'it' ? 'it-IT' : 'en-US', {{
                    year: 'numeric', month: '2-digit', day: '2-digit', hour: '2-digit', minute: '2-digit'
                }});
            }}
        }}

        // Setup Drag & Drop Zone
        function setupDropZone() {{
            const dropArea = document.getElementById('dropArea');
            const fileInput = document.getElementById('fileInput');

            dropArea.addEventListener('click', () => fileInput.click());

            fileInput.addEventListener('change', function(e) {{
                if (this.files && this.files[0]) {{
                    handleFile(this.files[0]);
                }}
            }});

            ['dragenter', 'dragover'].forEach(eventName => {{
                dropArea.addEventListener(eventName, (e) => {{
                    e.preventDefault();
                    e.stopPropagation();
                    dropArea.classList.add('drag-active');
                }}, false);
            }});

            ['dragleave', 'drop'].forEach(eventName => {{
                dropArea.addEventListener(eventName, (e) => {{
                    e.preventDefault();
                    e.stopPropagation();
                    dropArea.classList.remove('drag-active');
                }}, false);
            }});

            dropArea.addEventListener('drop', function(e) {{
                const dt = e.dataTransfer;
                if (dt.files && dt.files[0]) {{
                    handleFile(dt.files[0]);
                }}
            }});
        }}

        // Handle uploaded File (Image or PDF)
        function handleFile(file) {{
            const badge = document.getElementById('fileBadge');
            if (badge) badge.textContent = file.name;

            if (file.type === 'application/pdf') {{
                renderPdfFile(file);
            }} else if (file.type.startsWith('image/')) {{
                const reader = new FileReader();
                reader.onload = function(e) {{
                    const img = new Image();
                    img.onload = function() {{
                        analyzeImage(img);
                    }};
                    img.src = e.target.result;
                }};
                reader.readAsDataURL(file);
            }} else {{
                alert('Formato non supportato. Trascina un\\'immagine (PNG, JPG, WebP) o un file PDF.');
            }}
        }}

        // Render PDF First Page client-side using pdf.js
        function renderPdfFile(file) {{
            const reader = new FileReader();
            reader.onload = function(e) {{
                const typedarray = new Uint8Array(e.target.result);
                if (window.pdfjsLib) {{
                    pdfjsLib.getDocument(typedarray).promise.then(function(pdf) {{
                        pdf.getPage(1).then(function(page) {{
                            const viewport = page.getViewport({{ scale: 1.5 }});
                            const tempCanvas = document.createElement('canvas');
                            const ctx = tempCanvas.getContext('2d');
                            tempCanvas.width = viewport.width;
                            tempCanvas.height = viewport.height;

                            const renderContext = {{
                                canvasContext: ctx,
                                viewport: viewport
                            }};
                            page.render(renderContext).promise.then(function() {{
                                const img = new Image();
                                img.onload = function() {{
                                    analyzeImage(img);
                                }};
                                img.src = tempCanvas.toDataURL();
                            }});
                        }});
                    }}).catch(function(err) {{
                        console.error('PDF render error:', err);
                        alert('Errore nel caricamento del PDF. Prova a convertire la pagina in JPG/PNG.');
                    }});
                }} else {{
                    alert('Il visualizzatore PDF locale non è al momento disponibile. Usa un formato immagine PNG o JPG.');
                }}
            }};
            reader.readAsArrayBuffer(file);
        }}

        // Generate Sample Presets via Synthetic Canvas
        function loadSamplePreset(type) {{
            const badge = document.getElementById('fileBadge');
            const offCanvas = document.createElement('canvas');
            offCanvas.width = 600;
            offCanvas.height = 800;
            const ctx = offCanvas.getContext('2d');

            if (type === 'flyer') {{
                if (badge) badge.textContent = 'Volantino Full Color (Test)';
                const grad = ctx.createLinearGradient(0, 0, 600, 800);
                grad.addColorStop(0, '#0047AB');
                grad.addColorStop(0.5, '#C70039');
                grad.addColorStop(1, '#1A1A1A');
                ctx.fillStyle = grad;
                ctx.fillRect(0, 0, 600, 800);

                ctx.fillStyle = '#FFC300';
                ctx.fillRect(50, 600, 500, 120);

                ctx.fillStyle = '#FFFFFF';
                ctx.font = 'bold 38px sans-serif';
                ctx.fillText('SUPER PROMO PRINT', 80, 180);
                ctx.font = '22px sans-serif';
                ctx.fillText('Esperienza & Qualità Tipografica', 80, 240);
            }} 
            else if (type === 'book') {{
                if (badge) badge.textContent = 'Pagina Catalogo Editoriale (Test)';
                ctx.fillStyle = '#FFFFFF';
                ctx.fillRect(0, 0, 600, 800);

                const photoGrad = ctx.createLinearGradient(60, 80, 540, 380);
                photoGrad.addColorStop(0, '#2E8B57');
                photoGrad.addColorStop(1, '#D2691E');
                ctx.fillStyle = photoGrad;
                ctx.fillRect(60, 80, 480, 280);

                ctx.fillStyle = '#111827';
                ctx.font = 'bold 28px serif';
                ctx.fillText('Architettura & Paesaggio Contemporaneo', 60, 410);

                ctx.fillStyle = '#374151';
                for (let y = 450; y < 740; y += 18) {{
                    ctx.fillRect(60, y, 220, 6);
                    ctx.fillRect(320, y, 220, 6);
                }}
            }} 
            else if (type === 'minimal') {{
                if (badge) badge.textContent = 'Modulo / Minimale K-Only (Test)';
                ctx.fillStyle = '#FFFFFF';
                ctx.fillRect(0, 0, 600, 800);

                ctx.fillStyle = '#000000';
                ctx.font = 'bold 24px sans-serif';
                ctx.fillText('STUDIO GRAFICO & PRESTAMPA', 70, 120);

                ctx.fillRect(70, 140, 460, 2);

                for (let y = 200; y < 700; y += 45) {{
                    ctx.fillRect(70, y, 320, 4);
                    ctx.fillRect(430, y, 100, 1.5);
                }}
            }}

            const img = new Image();
            img.onload = function() {{
                analyzeImage(img);
            }};
            img.src = offCanvas.toDataURL();
        }}

        // Core Densitometric Pixel Analysis Algorithm
        function analyzeImage(img) {{
            currentImage = img;
            const mainCanvas = document.getElementById('mainCanvas');
            const heatmapCanvas = document.getElementById('heatmapCanvas');

            let scale = Math.min(1, 700 / Math.max(img.width, img.height));
            const w = Math.round(img.width * scale);
            const h = Math.round(img.height * scale);

            mainCanvas.width = w;
            mainCanvas.height = h;
            heatmapCanvas.width = w;
            heatmapCanvas.height = h;

            const ctx = mainCanvas.getContext('2d');
            const heatCtx = heatmapCanvas.getContext('2d');

            ctx.drawImage(img, 0, 0, w, h);
            const imgData = ctx.getImageData(0, 0, w, h);
            const pixels = imgData.data;
            const totalPixels = w * h;

            let sumC = 0, sumM = 0, sumY = 0, sumK = 0;
            let sumTac = 0;
            let maxTac = 0;

            const heatImgData = heatCtx.createImageData(w, h);
            const heatPixels = heatImgData.data;

            for (let i = 0; i < pixels.length; i += 4) {{
                const r = pixels[i];
                const g = pixels[i + 1];
                const b = pixels[i + 2];
                const a = pixels[i + 3] / 255;

                let r_p = r / 255;
                let g_p = g / 255;
                let b_p = b / 255;

                let k = 1 - Math.max(r_p, g_p, b_p);
                let c = 0, m = 0, y = 0;

                if (k < 0.999) {{
                    c = (1 - r_p - k) / (1 - k);
                    m = (1 - g_p - k) / (1 - k);
                    y = (1 - b_p - k) / (1 - k);
                }}

                c *= a;
                m *= a;
                y *= a;
                k *= a;

                const tac = c + m + y + k;

                sumC += c;
                sumM += m;
                sumY += y;
                sumK += k;
                sumTac += tac;

                if (tac > maxTac) maxTac = tac;

                if (tac > 3.10) {{
                    heatPixels[i] = 239;
                    heatPixels[i + 1] = 68;
                    heatPixels[i + 2] = 68;
                    heatPixels[i + 3] = 190;
                }} else if (tac >= 2.60) {{
                    heatPixels[i] = 245;
                    heatPixels[i + 1] = 158;
                    heatPixels[i + 2] = 11;
                    heatPixels[i + 3] = 150;
                }} else {{
                    heatPixels[i] = 16;
                    heatPixels[i + 1] = 185;
                    heatPixels[i + 2] = 129;
                    heatPixels[i + 3] = 40;
                }}
            }}

            heatCtx.putImageData(heatImgData, 0, 0);

            cmykData = {{
                c: (sumC / totalPixels) * 100,
                m: (sumM / totalPixels) * 100,
                y: (sumY / totalPixels) * 100,
                k: (sumK / totalPixels) * 100,
                tacAvg: (sumTac / totalPixels) * 100,
                tacPeak: maxTac * 100
            }};

            updateDensitometricUI();
            calculateCosts();
        }}

        // Update Gauge Bars, Metrics & TAC Status
        function updateDensitometricUI() {{
            document.getElementById('valC').textContent = cmykData.c.toFixed(1) + '%';
            document.getElementById('barC').style.width = Math.min(100, cmykData.c).toFixed(1) + '%';

            document.getElementById('valM').textContent = cmykData.m.toFixed(1) + '%';
            document.getElementById('barM').style.width = Math.min(100, cmykData.m).toFixed(1) + '%';

            document.getElementById('valY').textContent = cmykData.y.toFixed(1) + '%';
            document.getElementById('barY').style.width = Math.min(100, cmykData.y).toFixed(1) + '%';

            document.getElementById('valK').textContent = cmykData.k.toFixed(1) + '%';
            document.getElementById('barK').style.width = Math.min(100, cmykData.k).toFixed(1) + '%';

            document.getElementById('valTacAvg').textContent = cmykData.tacAvg.toFixed(1) + '%';
            document.getElementById('valTacPeak').textContent = cmykData.tacPeak.toFixed(0) + '%';

            const t = I18N_DATA[currentLang] || I18N_DATA['it'];
            const statusBox = document.getElementById('tacStatusBox');
            const titleEl = document.getElementById('tacStatusTitle');
            const descEl = document.getElementById('tacStatusDesc');

            if (cmykData.tacPeak > 320) {{
                statusBox.className = 'p-3.5 rounded-xl border transition-all bg-red-50 border-red-200 text-red-900';
                titleEl.textContent = t.tac_danger_title;
                descEl.textContent = t.tac_danger_desc;
            }} else if (cmykData.tacPeak > 280) {{
                statusBox.className = 'p-3.5 rounded-xl border transition-all bg-amber-50 border-amber-200 text-amber-900';
                titleEl.textContent = t.tac_warn_title;
                descEl.textContent = t.tac_warn_desc;
            }} else {{
                statusBox.className = 'p-3.5 rounded-xl border transition-all bg-emerald-50 border-emerald-200 text-emerald-900';
                titleEl.textContent = t.tac_safe_title;
                descEl.textContent = t.tac_safe_desc;
            }}
        }}

        // Toggle Heatmap Overlay
        function toggleHeatmap(active) {{
            isHeatmapActive = active;
            const heatmapCanvas = document.getElementById('heatmapCanvas');
            const legend = document.getElementById('heatmapLegend');

            if (active) {{
                heatmapCanvas.classList.remove('hidden');
                legend.classList.remove('hidden');
            }} else {{
                heatmapCanvas.classList.add('hidden');
                legend.classList.add('hidden');
            }}
        }}

        // Format selector change handler
        function onFormatChange() {{
            const format = document.getElementById('paperFormat').value;
            const customBox = document.getElementById('customDimBox');
            if (format === 'custom') {{
                customBox.classList.remove('hidden');
            }} else {{
                customBox.classList.add('hidden');
            }}
            calculateCosts();
        }}

        // Technology preset selector change handler
        function onTechChange() {{
            calculateCosts();
        }}

        // Calculate Consumable Grams & Financial Cost
        function calculateCosts() {{
            const format = document.getElementById('paperFormat').value;
            let sheetAreaM2 = PAPER_AREAS[format] || PAPER_AREAS['a4'];

            if (format === 'custom') {{
                let wMm = parseFloat(document.getElementById('customWidth').value) || 210;
                let hMm = parseFloat(document.getElementById('customHeight').value) || 297;
                if (copUnit === 'cm') {{ wMm *= 10; hMm *= 10; }}
                else if (copUnit === 'in') {{ wMm *= 25.4; hMm *= 25.4; }}
                sheetAreaM2 = (wMm / 1000) * (hMm / 1000);
            }}

            const copies = parseInt(document.getElementById('copiesCount').value, 10) || 1;
            const tech = document.getElementById('techPreset').value;
            const factor = TECH_FACTORS[tech] || 1.5;
            const pricePerKg = parseFloat(document.getElementById('inkPricePerKg').value) || 45.00;

            const totalAreaM2 = sheetAreaM2 * copies;

            const gramC = totalAreaM2 * (cmykData.c / 100) * factor;
            const gramM = totalAreaM2 * (cmykData.m / 100) * factor;
            const gramY = totalAreaM2 * (cmykData.y / 100) * factor;
            const gramK = totalAreaM2 * (cmykData.k / 100) * factor;
            const gramTotal = gramC + gramM + gramY + gramK;

            const totalCost = (gramTotal / 1000) * pricePerKg;
            const costPerCopy = copies > 0 ? (totalCost / copies) : 0;

            document.getElementById('gramC').textContent = gramC.toFixed(1) + ' g';
            document.getElementById('gramM').textContent = gramM.toFixed(1) + ' g';
            document.getElementById('gramY').textContent = gramY.toFixed(1) + ' g';
            document.getElementById('gramK').textContent = gramK.toFixed(1) + ' g';
            document.getElementById('gramTotal').textContent = gramTotal >= 1000 ? (gramTotal / 1000).toFixed(2) + ' kg' : gramTotal.toFixed(1) + ' g';

            document.getElementById('valCostPerCopy').textContent = costPerCopy < 0.001 ? '< 0.001' : costPerCopy.toFixed(3);
            document.getElementById('valTotalCost').textContent = totalCost.toFixed(2);

            const badge = document.getElementById('summaryBadge');
            if (badge) badge.textContent = copies.toLocaleString() + ' copie';
        }}

        // Language Management
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
                applyTranslations(lang);
                updateDensitometricUI();
                updatePrintDate();
            }}
        }}

        function applyTranslations(lang) {{
            const t = I18N_DATA[lang] || I18N_DATA['it'];
            document.documentElement.lang = lang;

            document.getElementById('heroTitle').textContent = t.hero_title;
            document.getElementById('heroDesc').textContent = t.hero_desc;
            document.getElementById('privacyBadge').textContent = t.privacy_badge;

            document.getElementById('dropTitle').textContent = t.dropzone_title;
            document.getElementById('dropSub').textContent = t.dropzone_sub;
            document.getElementById('presetLabel').textContent = t.sample_presets_label;
            document.getElementById('btnSampleFlyer').textContent = t.sample_flyer;
            document.getElementById('btnSampleBook').textContent = t.sample_book;
            document.getElementById('btnSampleMinimal').textContent = t.sample_minimal;

            document.getElementById('heatmapToggleText').textContent = t.heatmap_toggle;
            document.getElementById('costSettingsTitle').children[1].textContent = t.cost_calculator_title;

            document.getElementById('lblPaperFormat').textContent = t.paper_format_label;
            document.getElementById('lblCopies').textContent = t.copies_label;
            document.getElementById('lblTech').textContent = t.tech_label;
            document.getElementById('lblInkPrice').textContent = t.ink_price_label;

            document.getElementById('analysisTitle').children[0].textContent = t.analysis_title;
            document.getElementById('lblC').textContent = t.c_label;
            document.getElementById('lblM').textContent = t.m_label;
            document.getElementById('lblY').textContent = t.y_label;
            document.getElementById('lblK').textContent = t.k_label;
            document.getElementById('lblTacAvg').textContent = t.tac_avg_label;
            document.getElementById('lblTacPeak').textContent = t.tac_peak_label;

            document.getElementById('resSummaryTitle').children[0].textContent = t.res_summary_title;
            document.getElementById('lblCostPerCopy').textContent = t.res_cost_per_copy;
            document.getElementById('lblTotalCost').textContent = t.res_total_cost;
            document.getElementById('btnPrintText').textContent = t.print_btn;

            document.getElementById('ruleTipText').innerHTML = t.rule_tip;
            document.getElementById('legalDisclaimerText').innerHTML = t.legal_disclaimer;

            document.getElementById('faqTitle').children[0].textContent = t.faq_title;
            document.getElementById('faq1Q').textContent = t.faq_1_q;
            document.getElementById('faq1A').textContent = t.faq_1_a;
            document.getElementById('faq2Q').textContent = t.faq_2_q;
            document.getElementById('faq2A').textContent = t.faq_2_a;
            document.getElementById('faq3Q').textContent = t.faq_3_q;
            document.getElementById('faq3A').textContent = t.faq_3_a;
            document.getElementById('faq4Q').textContent = t.faq_4_q;
            document.getElementById('faq4A').textContent = t.faq_4_a;

            // Footer, Share & Modals
            if (t.share_title && document.getElementById('shareTitleText')) document.getElementById('shareTitleText').textContent = t.share_title;
            if (t.share_sub && document.getElementById('shareSubText')) document.getElementById('shareSubText').textContent = t.share_sub;
            if (t.share_copy && document.getElementById('shareCopyText')) document.getElementById('shareCopyText').textContent = t.share_copy;
            if (t.suggest_banner && document.getElementById('suggestBannerText')) document.getElementById('suggestBannerText').textContent = t.suggest_banner;
            if (t.suggest_btn && document.getElementById('suggestBtnText')) document.getElementById('suggestBtnText').textContent = t.suggest_btn;
            if (t.suggest_modal_title && document.getElementById('modalSuggestTitle')) document.getElementById('modalSuggestTitle').textContent = t.suggest_modal_title;
            if (t.suggest_modal_desc && document.getElementById('modalSuggestDesc')) document.getElementById('modalSuggestDesc').textContent = t.suggest_modal_desc;
            if (t.suggest_placeholder && document.getElementById('suggestMessage')) document.getElementById('suggestMessage').placeholder = t.suggest_placeholder;
            if (t.suggest_privacy_note && document.getElementById('modalPrivacyNote')) document.getElementById('modalPrivacyNote').textContent = t.suggest_privacy_note;
            if (t.suggest_close && document.getElementById('modalCloseBtn')) document.getElementById('modalCloseBtn').textContent = t.suggest_close;
            if (t.suggest_send && document.getElementById('modalSubmitBtn')) document.getElementById('modalSubmitBtn').textContent = t.suggest_send;
            if (t.suggest_thanks && document.getElementById('modalSuccessText')) document.getElementById('modalSuccessText').textContent = t.suggest_thanks;
            if (t.install_banner_title && document.getElementById('installBannerTitle')) document.getElementById('installBannerTitle').textContent = t.install_banner_title;
            if (t.install_banner_sub && document.getElementById('installBannerSub')) document.getElementById('installBannerSub').textContent = t.install_banner_sub;
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

with open('/Users/ilalu/Documents/Altenative Businnes/Calcolatore_Pendenza/copertura.html', 'w', encoding='utf-8') as f:
    f.write(html_code)

print("copertura.html recompiled successfully with unified_footer.")
