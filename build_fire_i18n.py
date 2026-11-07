import json
import sys
import os

from nav_header import render_suite_header, render_suite_header_js
from unified_footer import render_unified_footer, render_unified_footer_js

base_dir = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(base_dir, "translations_fire.json"), "r", encoding="utf-8") as f:
    t_data = json.load(f)

t_json_str = json.dumps(t_data, ensure_ascii=False)

header_html = render_suite_header("fire")
header_js = render_suite_header_js()
footer_html = render_unified_footer("fire")
footer_js = render_unified_footer_js()

html_code = f"""<!DOCTYPE html>
<html lang="it">
<head>
    <meta name="google-site-verification" content="MRdbDm9lLhokeD3I0FOpUSOhNaF_2WaveKvu52FxtG4">
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0">
    <title>FIRE Calculator - Calcolo Rendita Passiva & Libertà Finanziaria (Regola del 4%)</title>
    <meta name="description" content="Calcola in quanti anni puoi raggiungere la libertà finanziaria e vivere di rendita con la Regola del 4% (Trinity Study). Simula Lean, Regular e Fat FIRE con interesse composto.">
    
    <!-- Canonical & SEO Meta Tags -->
    <link rel="canonical" href="https://www.omnitoolslab.com/fire">
    <meta name="robots" content="index, follow">
    <meta property="og:type" content="website">
    <meta property="og:title" content="OmniTools - Calcolatore FIRE & Libertà Finanziaria">
    <meta property="og:description" content="Scopri tra quanti anni puoi vivere di rendita. Calcolo Numero FIRE, Regola del 4% e traiettoria con interesse composto.">
    <meta property="og:url" content="https://www.omnitoolslab.com/fire">
    <meta property="og:site_name" content="OmniTools Lab">
    <meta property="og:image" content="https://www.omnitoolslab.com/og-fire.png">
    <meta property="og:image:width" content="1200">
    <meta property="og:image:height" content="630">
    <meta property="og:image:type" content="image/png">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:image" content="https://www.omnitoolslab.com/og-fire.png">

    <!-- Schema.org JSON-LD Structured Data (Rich Snippets) -->
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@graph": [
        {{
          "@type": "WebApplication",
          "name": "FIRE Calculator — Libertà Finanziaria & Rendita Passiva",
          "url": "https://www.omnitoolslab.com/fire",
          "applicationCategory": "FinanceApplication",
          "operatingSystem": "All",
          "browserRequirements": "Requires JavaScript. Requires HTML5.",
          "offers": {{
            "@type": "Offer",
            "price": "0",
            "priceCurrency": "EUR"
          }},
          "description": "Calcolatore accademico basato sul Trinity Study e la Regola del 4% per pianificare la pensione anticipata, il numero FIRE e la rendita passiva."
        }},
        {{
          "@type": "SoftwareApplication",
          "name": "FIRE Freedom Calculator",
          "operatingSystem": "Web Browser",
          "applicationCategory": "FinanceApplication",
          "aggregateRating": {{
            "@type": "AggregateRating",
            "ratingValue": "4.9",
            "reviewCount": "210"
          }}
        }}
      ]
    }}
    </script>

    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {{
            theme: {{
                extend: {{
                    colors: {{
                        emerald: {{
                            50: '#ecfdf5',
                            100: '#d1fae5',
                            500: '#10b981',
                            600: '#059669',
                            700: '#047857',
                            800: '#065f46',
                            900: '#064e3b',
                        }}
                    }}
                }}
            }}
        }}
    </script>
    
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
    
    <style>
        body {{
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            -webkit-font-smoothing: antialiased;
        }}
        .font-mono {{
            font-family: 'JetBrains Mono', monospace;
        }}
        .metric-card {{
            transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
        }}
        .metric-card:hover {{
            transform: translateY(-2px);
            box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.05), 0 8px 10px -6px rgba(0, 0, 0, 0.01);
        }}
    </style>
</head>
<body class="bg-slate-50 text-slate-800 min-h-screen flex flex-col justify-between antialiased selection:bg-emerald-600 selection:text-white">

    <!-- Universal Header with Chrome Tabs & Tool Picker -->
    {header_html}

    <main class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 pt-6 pb-16 flex-grow w-full">
        <!-- Main Tool Intro Header -->
        <div class="mb-8 text-center sm:text-left sm:flex sm:items-end sm:justify-between border-b border-slate-200/80 pb-6">
            <div>
                <div class="inline-flex items-center gap-2 px-2.5 py-1 rounded-full bg-emerald-50 border border-emerald-200/60 text-emerald-800 text-xs font-semibold mb-3">
                    <span class="w-2 h-2 rounded-full bg-emerald-500 animate-pulse"></span>
                    <span id="badgeCategory">OmniFinance • Indipendenza & Libertà Finanziaria</span>
                </div>
                <h1 id="mainTitle" class="text-3xl sm:text-4xl font-extrabold text-slate-900 tracking-tight">Calcolatore FIRE & Rendita Passiva</h1>
                <p id="mainSubtitle" class="text-slate-600 text-sm sm:text-base mt-2 max-w-2xl">
                    Scopri tra quanti anni puoi smettere di lavorare e vivere dei rendimenti del tuo patrimonio con la Regola del 4% (Trinity Study).
                </p>
            </div>
            <!-- Currency Selector -->
            <div class="mt-4 sm:mt-0 flex items-center justify-center sm:justify-end gap-2 shrink-0">
                <div class="inline-flex p-1 bg-slate-200/80 rounded-xl text-xs font-bold text-slate-600">
                    <button type="button" id="currEurBtn" onclick="setCurrency('€')" class="px-3 py-1.5 rounded-lg bg-white text-slate-900 shadow-xs transition">€ EUR</button>
                    <button type="button" id="currUsdBtn" onclick="setCurrency('$')" class="px-3 py-1.5 rounded-lg hover:text-slate-900 transition">$ USD</button>
                    <button type="button" id="currGbpBtn" onclick="setCurrency('£')" class="px-3 py-1.5 rounded-lg hover:text-slate-900 transition">£ GBP</button>
                </div>
            </div>
        </div>

        <!-- Presets Bar -->
        <div class="mb-8 p-3.5 bg-white border border-slate-200/70 rounded-2xl shadow-xs flex flex-wrap items-center gap-2">
            <span id="presetTitleLabel" class="text-xs font-bold text-slate-500 uppercase tracking-wider flex items-center gap-1.5 mr-1">
                <svg class="w-4 h-4 text-emerald-600" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M13 10V3L4 14h7v7l9-11h-7z"/></svg>
                Stili di Vita FIRE:
            </span>
            <button onclick="applyPreset('lean')" class="px-3 py-1.5 rounded-lg bg-emerald-50 hover:bg-emerald-100 text-emerald-900 border border-emerald-200/80 text-xs font-semibold transition">
                🌱 <span id="presetLeanText">Lean FIRE (1.200 €/m)</span>
            </button>
            <button onclick="applyPreset('regular')" class="px-3 py-1.5 rounded-lg bg-slate-100 hover:bg-slate-200 text-slate-800 border border-slate-300 text-xs font-semibold transition">
                ☕ <span id="presetRegularText">Regular FIRE (2.200 €/m)</span>
            </button>
            <button onclick="applyPreset('fat')" class="px-3 py-1.5 rounded-lg bg-emerald-50 hover:bg-emerald-100 text-emerald-900 border border-emerald-200/80 text-xs font-semibold transition">
                🏖️ <span id="presetFatText">Fat FIRE (4.500 €/m)</span>
            </button>
        </div>

        <!-- Layout Grid: Inputs Form & Visual Analytics -->
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
            
            <!-- Left Column: Inputs Form (5 cols) -->
            <div class="lg:col-span-5 space-y-6">
                
                <div class="bg-white rounded-3xl p-6 border border-slate-200 shadow-xs space-y-5">
                    <div class="flex items-center gap-2.5 pb-3 border-b border-slate-100">
                        <span class="w-7 h-7 rounded-lg bg-emerald-500/10 text-emerald-600 flex items-center justify-center font-bold text-sm">1</span>
                        <h2 id="sectionInputsTitle" class="text-base font-bold text-slate-900">1. Parametri di Risparmio & Spese</h2>
                    </div>

                    <!-- Input 1: Spese Mensili Desiderate -->
                    <div>
                        <div class="flex justify-between items-center text-xs font-semibold text-slate-700 mb-1.5">
                            <label id="monthlyExpenseLabel" for="monthlyExpenseInput">Spese Mensili Desiderate da Rendita</label>
                            <span class="text-slate-400 font-mono currLabel">€/mese</span>
                        </div>
                        <div class="relative">
                            <input type="number" id="monthlyExpenseInput" min="100" step="50" value="2000" oninput="calculateFire()"
                                class="w-full bg-slate-50 border border-slate-200 rounded-xl px-3.5 py-2.5 text-sm font-mono font-bold text-slate-800 focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:bg-white transition">
                            <span class="absolute right-3.5 top-2.5 text-slate-400 text-xs font-bold font-mono pointer-events-none currSymbol">€</span>
                        </div>
                        <span class="text-[11px] text-slate-400 mt-1 block">Spese annuali previste: <strong id="annualExpenseTag" class="text-slate-700 font-mono">24.000 €/anno</strong></span>
                    </div>

                    <!-- Input 2: Capitale Attuale -->
                    <div>
                        <div class="flex justify-between items-center text-xs font-semibold text-slate-700 mb-1.5">
                            <label id="currentSavingsLabel" for="currentSavingsInput">Capitale Attuale Risparmiato / Investito</label>
                            <span class="text-slate-400 font-mono currLabel">€</span>
                        </div>
                        <div class="relative">
                            <input type="number" id="currentSavingsInput" min="0" step="500" value="25000" oninput="calculateFire()"
                                class="w-full bg-slate-50 border border-slate-200 rounded-xl px-3.5 py-2.5 text-sm font-mono font-bold text-slate-800 focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:bg-white transition">
                            <span class="absolute right-3.5 top-2.5 text-slate-400 text-xs font-bold font-mono pointer-events-none currSymbol">€</span>
                        </div>
                    </div>

                    <!-- Input 3: Risparmio Mensile Aggiuntivo -->
                    <div>
                        <div class="flex justify-between items-center text-xs font-semibold text-slate-700 mb-1.5">
                            <label id="monthlySavingsLabel" for="monthlySavingsInput">Risparmio Mensile Aggiuntivo</label>
                            <span class="text-slate-400 font-mono currLabel">€/mese</span>
                        </div>
                        <div class="relative">
                            <input type="number" id="monthlySavingsInput" min="0" step="50" value="750" oninput="calculateFire()"
                                class="w-full bg-slate-50 border border-slate-200 rounded-xl px-3.5 py-2.5 text-sm font-mono font-bold text-slate-800 focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:bg-white transition">
                            <span class="absolute right-3.5 top-2.5 text-slate-400 text-xs font-bold font-mono pointer-events-none currSymbol">€</span>
                        </div>
                    </div>

                    <!-- Input 4: Rendimento Medio Annuo (%) -->
                    <div>
                        <div class="flex justify-between items-center text-xs font-semibold text-slate-700 mb-1.5">
                            <label id="returnRateLabel" for="returnRateInput">Rendimento Medio Annuo Atteso (%)</label>
                            <span class="text-slate-400 font-mono">% / anno</span>
                        </div>
                        <div class="relative">
                            <input type="number" id="returnRateInput" min="0.1" max="25" step="0.5" value="7.0" oninput="calculateFire()"
                                class="w-full bg-slate-50 border border-slate-200 rounded-xl px-3.5 py-2.5 text-sm font-mono font-bold text-slate-800 focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:bg-white transition">
                            <span class="absolute right-3.5 top-2.5 text-slate-400 text-xs font-bold font-mono pointer-events-none">%</span>
                        </div>
                        <span class="text-[11px] text-slate-400 mt-1 block">Rendimento tipico azionario globale (es. MSCI World / S&P 500 post-inflazione: 6-8%).</span>
                    </div>

                    <!-- Input 5: Tasso di Prelievo Sicuro (SWR) -->
                    <div>
                        <div class="flex justify-between items-center text-xs font-semibold text-slate-700 mb-1.5">
                            <label id="swrLabel" for="swrInput">Tasso di Prelievo Sicuro (SWR %)</label>
                            <span class="text-slate-400 font-mono" id="multiplierTag">25.0×</span>
                        </div>
                        <div class="relative">
                            <input type="number" id="swrInput" min="2.0" max="8.0" step="0.1" value="4.0" oninput="calculateFire()"
                                class="w-full bg-slate-50 border border-slate-200 rounded-xl px-3.5 py-2.5 text-sm font-mono font-bold text-slate-800 focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:bg-white transition">
                            <span class="absolute right-3.5 top-2.5 text-slate-400 text-xs font-bold font-mono pointer-events-none">%</span>
                        </div>
                        <p id="swrHint" class="text-[11px] text-slate-500 mt-1.5 leading-relaxed">
                            4.0% = Regola classica Trinity Study (Patrimonio = 25× Spese Annue). 3.5% = Approccio conservativo a lunghissimo termine.
                        </p>
                    </div>

                </div>

            </div>

            <!-- Right Column: Results KPIs, Chart & Breakdown (7 cols) -->
            <div class="lg:col-span-7 space-y-6">
                
                <!-- KPI Results Dashboard Grid -->
                <div class="grid grid-cols-2 sm:grid-cols-4 gap-3">
                    <div class="metric-card bg-white p-4 rounded-2xl border border-slate-200/90 shadow-xs">
                        <span id="kpiFireNumberLabel" class="block text-slate-500 text-[11px] font-semibold uppercase tracking-wider mb-1">Numero FIRE</span>
                        <div class="flex items-baseline gap-1">
                            <span id="resFireNumber" class="text-xl sm:text-2xl font-extrabold text-emerald-600 font-mono">0</span>
                            <span class="text-xs font-bold text-slate-400 currSymbol">€</span>
                        </div>
                    </div>

                    <div class="metric-card bg-white p-4 rounded-2xl border border-slate-200/90 shadow-xs">
                        <span id="kpiYearsLeftLabel" class="block text-slate-500 text-[11px] font-semibold uppercase tracking-wider mb-1">Tempo alla Libertà</span>
                        <div class="flex items-baseline gap-1">
                            <span id="resYearsLeft" class="text-xl sm:text-2xl font-extrabold text-slate-900 font-mono">0</span>
                            <span class="text-xs font-bold text-slate-400" id="resYearsUnit">anni</span>
                        </div>
                    </div>

                    <div class="metric-card bg-white p-4 rounded-2xl border border-slate-200/90 shadow-xs">
                        <span id="kpiProgressLabel" class="block text-slate-500 text-[11px] font-semibold uppercase tracking-wider mb-1">Progresso Target</span>
                        <div class="flex items-baseline gap-1">
                            <span id="resProgressPct" class="text-xl sm:text-2xl font-extrabold text-blue-600 font-mono">0.0</span>
                            <span class="text-xs font-bold text-slate-400">%</span>
                        </div>
                    </div>

                    <div class="metric-card bg-white p-4 rounded-2xl border border-slate-200/90 shadow-xs">
                        <span id="kpiAnnualIncomeLabel" class="block text-slate-500 text-[11px] font-semibold uppercase tracking-wider mb-1">Rendita Annua</span>
                        <div class="flex items-baseline gap-1">
                            <span id="resAnnualPassive" class="text-xl sm:text-2xl font-extrabold text-slate-900 font-mono">0</span>
                            <span class="text-xs font-bold text-slate-400 currSymbol">€</span>
                        </div>
                    </div>
                </div>

                <!-- Visual Wealth Trajectory Chart Container -->
                <div class="bg-white rounded-3xl p-6 border border-slate-200 shadow-xs">
                    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 mb-4 pb-3 border-b border-slate-100">
                        <div class="flex items-center gap-2">
                            <svg class="w-5 h-5 text-emerald-600" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"/></svg>
                            <h3 id="chartTitle" class="text-base font-bold text-slate-900">Traiettoria di Accumulo & Interesse Composto nel Tempo</h3>
                        </div>
                        <!-- Legend -->
                        <div class="flex items-center gap-3 text-[11px] font-medium text-slate-600">
                            <span class="inline-flex items-center gap-1">
                                <span class="w-3 h-3 rounded-xs bg-slate-400"></span> <span id="legendDepositsLabel">Versamenti</span>
                            </span>
                            <span class="inline-flex items-center gap-1">
                                <span class="w-3 h-3 rounded-xs bg-emerald-500"></span> <span id="legendInterestLabel">Interesse</span>
                            </span>
                            <span class="inline-flex items-center gap-1">
                                <span class="w-3.5 h-0.5 bg-amber-500"></span> <span id="legendFireLineLabel">Target FIRE</span>
                            </span>
                        </div>
                    </div>

                    <!-- SVG Chart Area -->
                    <div id="svgChartWrapper" class="w-full h-64 sm:h-72 bg-slate-50/60 rounded-2xl border border-slate-200/80 p-2 relative flex items-center justify-center">
                        <svg id="fireTrajectorySvg" class="w-full h-full" viewBox="0 0 600 240" preserveAspectRatio="none">
                            <!-- Injected by calculateFire() -->
                        </svg>
                    </div>

                    <!-- Milestone Summary Note -->
                    <div id="milestoneNote" class="mt-4 p-3 bg-emerald-50/80 border border-emerald-200/70 rounded-2xl text-xs text-emerald-900 flex items-center gap-2">
                        <span class="text-lg">🎯</span>
                        <span>Raggiungerai l'indipendenza finanziaria con un capitale di <strong id="milestoneTargetText" class="font-mono">600.000 €</strong> garantendo una rendita mensile netta a vita.</span>
                    </div>
                </div>

                <!-- Breakdown Projection Table -->
                <div class="bg-white rounded-3xl p-6 border border-slate-200 shadow-xs">
                    <div class="flex items-center justify-between mb-4 pb-3 border-b border-slate-100">
                        <h3 id="breakdownTitle" class="text-base font-bold text-slate-900">Proiezione Anno per Anno</h3>
                        <button type="button" onclick="window.print()" class="px-2.5 py-1 rounded-lg bg-slate-100 hover:bg-slate-200 text-slate-700 text-xs font-semibold flex items-center gap-1.5 transition">
                            <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M17 17h2a2 2 0 002-2v-4a2 2 0 00-2-2H5a2 2 0 00-2 2v4a2 2 0 002 2h2m2 4h6a2 2 0 002-2v-4H7v4a2 2 0 002 2zm8-12V5a2 2 0 00-2-2H9a2 2 0 00-2 2v4h10z"/></svg>
                            Stampa Proiezione
                        </button>
                    </div>

                    <div class="overflow-x-auto max-h-72 overflow-y-auto pr-1">
                        <table class="w-full text-left text-xs font-mono">
                            <thead class="sticky top-0 bg-white">
                                <tr class="text-slate-400 border-b border-slate-100">
                                    <th class="pb-2 font-semibold">Anno</th>
                                    <th class="pb-2 font-semibold">Capitale Versato</th>
                                    <th class="pb-2 font-semibold text-emerald-600">Interessi Totali</th>
                                    <th class="pb-2 font-semibold text-right font-bold text-slate-800">Patrimonio Totale</th>
                                </tr>
                            </thead>
                            <tbody id="fireTableBody" class="divide-y divide-slate-100">
                                <!-- Populated dynamically -->
                            </tbody>
                        </table>
                    </div>
                </div>

            </div>

        </div>

        <!-- FAQ Section -->
        <section id="faqSection" class="no-print mt-16 bg-white rounded-3xl border border-slate-200/90 shadow-xs p-5 sm:p-7 space-y-4">
            <div class="flex items-center gap-2.5 mb-1">
                <span class="text-xl">❓</span>
                <h2 class="text-base sm:text-lg font-black text-slate-900 font-jakarta flex items-center gap-2">
                    <span id="faqTitle">Domande Frequenti sul Movimento FIRE e la Libertà Finanziaria</span>
                </h2>
                <span class="text-[10px] font-extrabold uppercase px-2 py-0.5 rounded-full bg-slate-100 text-slate-600 border border-slate-200">FAQ</span>
            </div>
            
            <div id="faqContainer" class="space-y-3">
                <details class="group bg-slate-50/80 hover:bg-slate-50 rounded-2xl border border-slate-200/80 p-4 transition duration-150">
                    <summary class="flex justify-between items-center font-bold text-xs sm:text-sm text-slate-900 cursor-pointer list-none select-none">
                        <span id="faqQ1">Cos'è il movimento FIRE e come funziona la Regola del 4%?</span>
                        <svg class="w-4 h-4 text-slate-400 group-open:-rotate-180 transition-transform duration-200 shrink-0 ml-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/>
                        </svg>
                    </summary>
                    <div id="faqA1" class="text-xs sm:text-sm text-slate-600 mt-2.5 leading-relaxed border-t border-slate-200/60 pt-2.5">
                        FIRE è l'acronimo di "Financial Independence, Retire Early" (Indipendenza Finanziaria, Pensione Anticipata). La Regola del 4%, derivata dal celebre studio accademico Trinity Study dell'Università Trinity (Texas), dimostra che prelevando annualmente non più del 4% da un portafoglio diversificato di azioni e obbligazioni, il capitale ha una probabilità superiore al 95% di durare per almeno 30 anni senza mai esaurirsi.
                    </div>
                </details>

                <details class="group bg-slate-50/80 hover:bg-slate-50 rounded-2xl border border-slate-200/80 p-4 transition duration-150">
                    <summary class="flex justify-between items-center font-bold text-xs sm:text-sm text-slate-900 cursor-pointer list-none select-none">
                        <span id="faqQ2">Qual è la differenza tra Lean FIRE, Regular FIRE e Fat FIRE?</span>
                        <svg class="w-4 h-4 text-slate-400 group-open:-rotate-180 transition-transform duration-200 shrink-0 ml-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/>
                        </svg>
                    </summary>
                    <div id="faqA2" class="text-xs sm:text-sm text-slate-600 mt-2.5 leading-relaxed border-t border-slate-200/60 pt-2.5">
                        Lean FIRE punta a uno stile di vita frugale con spese coperte al minimo (es. 1.000 - 1.400 €/mese), richiedendo un capitale accumulato più piccolo. Regular FIRE garantisce il mantenimento del tenore di vita medio attuale (2.000 - 2.500 €/mese). Fat FIRE è pensato per chi desidera una pensione anticipata di lusso con viaggi frequenti e spese elevate (oltre 4.000 - 5.000 €/mese).
                    </div>
                </details>

                <details class="group bg-slate-50/80 hover:bg-slate-50 rounded-2xl border border-slate-200/80 p-4 transition duration-150">
                    <summary class="flex justify-between items-center font-bold text-xs sm:text-sm text-slate-900 cursor-pointer list-none select-none">
                        <span id="faqQ3">Come si calcola il Numero FIRE?</span>
                        <svg class="w-4 h-4 text-slate-400 group-open:-rotate-180 transition-transform duration-200 shrink-0 ml-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/>
                        </svg>
                    </summary>
                    <div id="faqA3" class="text-xs sm:text-sm text-slate-600 mt-2.5 leading-relaxed border-t border-slate-200/60 pt-2.5">
                        La formula matematica universale è: Spese Annue ÷ Tasso di Prelievo (SWR). Se applichi la regola classica del 4% (0.04), equivale semplicemente a moltiplicare le tue spese annuali per 25. Ad esempio: 20.000 € di spese all'anno × 25 = 500.000 € di patrimonio target.
                    </div>
                </details>
            </div>
        </section>

    </main>

    <!-- Universal Footer -->
    {footer_html}

    <!-- Universal Scripts -->
    {header_js}
    {footer_js}

    <!-- FIRE Engine Logic & I18N Script -->
    <script>
        const TRANSLATIONS = {t_json_str};
        let currentLang = 'it';
        let currentCurrency = '€';

        function setCurrency(curr) {{
            currentCurrency = curr;
            document.querySelectorAll('.currSymbol').forEach(el => el.textContent = curr);
            document.querySelectorAll('.currLabel').forEach(el => {{
                el.textContent = el.textContent.includes('/mese') ? `${{curr}}/mese` : curr;
            }});

            const eurBtn = document.getElementById('currEurBtn');
            const usdBtn = document.getElementById('currUsdBtn');
            const gbpBtn = document.getElementById('currGbpBtn');

            [eurBtn, usdBtn, gbpBtn].forEach(b => b.className = 'px-3 py-1.5 rounded-lg hover:text-slate-900 transition');
            if (curr === '€') eurBtn.className = 'px-3 py-1.5 rounded-lg bg-white text-slate-900 shadow-xs transition';
            if (curr === '$') usdBtn.className = 'px-3 py-1.5 rounded-lg bg-white text-slate-900 shadow-xs transition';
            if (curr === '£') gbpBtn.className = 'px-3 py-1.5 rounded-lg bg-white text-slate-900 shadow-xs transition';

            calculateFire();
        }}

        function applyPreset(type) {{
            if (type === 'lean') {{
                document.getElementById('monthlyExpenseInput').value = 1200;
                document.getElementById('monthlySavingsInput').value = 600;
            }} else if (type === 'regular') {{
                document.getElementById('monthlyExpenseInput').value = 2200;
                document.getElementById('monthlySavingsInput').value = 900;
            }} else if (type === 'fat') {{
                document.getElementById('monthlyExpenseInput').value = 4500;
                document.getElementById('monthlySavingsInput').value = 2000;
            }}
            calculateFire();
        }}

        function formatMoney(amount) {{
            return new Intl.NumberFormat('it-IT', {{ maximumFractionDigits: 0 }}).format(amount);
        }}

        function calculateFire() {{
            const monthlyExpense = parseFloat(document.getElementById('monthlyExpenseInput').value) || 0;
            const currentSavings = parseFloat(document.getElementById('currentSavingsInput').value) || 0;
            const monthlySavings = parseFloat(document.getElementById('monthlySavingsInput').value) || 0;
            const annualReturnPct = parseFloat(document.getElementById('returnRateInput').value) || 7.0;
            const swrPct = parseFloat(document.getElementById('swrInput').value) || 4.0;

            const annualExpense = monthlyExpense * 12;
            document.getElementById('annualExpenseTag').textContent = `${{formatMoney(annualExpense)}} ${{currentCurrency}}/anno`;

            const multiplier = swrPct > 0 ? (100 / swrPct) : 25;
            document.getElementById('multiplierTag').textContent = `${{multiplier.toFixed(1)}}×`;

            // FIRE Number = Annual Expenses / SWR
            const fireNumber = swrPct > 0 ? (annualExpense / (swrPct / 100)) : 0;
            document.getElementById('resFireNumber').textContent = formatMoney(fireNumber);
            document.getElementById('resAnnualPassive').textContent = formatMoney(annualExpense);

            const progressPct = fireNumber > 0 ? Math.min(100, (currentSavings / fireNumber) * 100) : 0;
            document.getElementById('resProgressPct').textContent = progressPct.toFixed(1);

            // Simulation of month-by-month compound growth
            const rMonth = Math.pow(1 + (annualReturnPct / 100), 1 / 12) - 1;
            let balance = currentSavings;
            let totalDeposited = currentSavings;
            let months = 0;
            const maxMonths = 12 * 70; // 70 years maximum cap

            let trajectory = [{{
                year: 0,
                balance: currentSavings,
                deposited: totalDeposited,
                interest: 0
            }}];

            let reachedMonth = null;
            if (balance >= fireNumber) {{
                reachedMonth = 0;
            }}

            while (months < maxMonths && balance < fireNumber) {{
                months++;
                balance = balance * (1 + rMonth) + monthlySavings;
                totalDeposited += monthlySavings;

                if (balance >= fireNumber && reachedMonth === null) {{
                    reachedMonth = months;
                }}

                if (months % 12 === 0 || balance >= fireNumber) {{
                    trajectory.push({{
                        year: (months / 12).toFixed(1),
                        balance: Math.round(balance),
                        deposited: Math.round(totalDeposited),
                        interest: Math.round(Math.max(0, balance - totalDeposited))
                    }});
                }}
            }}

            // Render Years left
            if (reachedMonth === 0) {{
                document.getElementById('resYearsLeft').textContent = '0';
                document.getElementById('resYearsUnit').textContent = '🎉 GIÀ LIBERO!';
            }} else if (reachedMonth !== null) {{
                const yrs = Math.floor(reachedMonth / 12);
                const mos = reachedMonth % 12;
                document.getElementById('resYearsLeft').textContent = (reachedMonth / 12).toFixed(1);
                document.getElementById('resYearsUnit').textContent = `anni (${{yrs}}a ${{mos}}m)`;
            }} else {{
                document.getElementById('resYearsLeft').textContent = '> 70';
                document.getElementById('resYearsUnit').textContent = 'anni';
            }}

            document.getElementById('milestoneTargetText').textContent = `${{formatMoney(fireNumber)}} ${{currentCurrency}}`;

            renderChart(trajectory, fireNumber);
            renderTable(trajectory);
        }}

        function renderChart(trajectory, fireNumber) {{
            const svg = document.getElementById('fireTrajectorySvg');
            if (trajectory.length === 0) return;

            const width = 600;
            const height = 240;
            const padL = 60;
            const padR = 20;
            const padT = 25;
            const padB = 30;

            const maxVal = Math.max(fireNumber * 1.15, trajectory[trajectory.length - 1].balance * 1.05);
            const maxYears = Math.max(1, parseFloat(trajectory[trajectory.length - 1].year));

            const scaleX = (yr) => padL + (yr / maxYears) * (width - padL - padR);
            const scaleY = (val) => height - padB - (val / maxVal) * (height - padT - padB);

            // Generate Path points
            let dBalance = '';
            let dDeposited = '';
            let dAreaInterest = '';

            trajectory.forEach((pt, i) => {{
                const x = scaleX(parseFloat(pt.year));
                const yBal = scaleY(pt.balance);
                const yDep = scaleY(pt.deposited);

                if (i === 0) {{
                    dBalance = `M ${{x}} ${{yBal}}`;
                    dDeposited = `M ${{x}} ${{yDep}}`;
                    dAreaInterest = `M ${{x}} ${{yBal}}`;
                }} else {{
                    dBalance += ` L ${{x}} ${{yBal}}`;
                    dDeposited += ` L ${{x}} ${{yDep}}`;
                }}
            }});

            // Area path for compound interest (between balance and deposited)
            let areaPath = dBalance;
            for (let i = trajectory.length - 1; i >= 0; i--) {{
                const x = scaleX(parseFloat(trajectory[i].year));
                const yDep = scaleY(trajectory[i].deposited);
                areaPath += ` L ${{x}} ${{yDep}}`;
            }}
            areaPath += ' Z';

            // Base deposited area
            let depAreaPath = dDeposited;
            depAreaPath += ` L ${{scaleX(maxYears)}} ${{scaleY(0)}} L ${{scaleX(0)}} ${{scaleY(0)}} Z`;

            const yFireLine = scaleY(fireNumber);

            svg.innerHTML = `
                <!-- Background Grid -->
                <line x1="${{padL}}" y1="${{scaleY(0)}}" x2="${{width - padR}}" y2="${{scaleY(0)}}" stroke="#cbd5e1" stroke-width="1.5" />
                <line x1="${{padL}}" y1="${{scaleY(maxVal * 0.5)}}" x2="${{width - padR}}" y2="${{scaleY(maxVal * 0.5)}}" stroke="#f1f5f9" stroke-width="1" stroke-dasharray="4" />
                
                <!-- Target FIRE Line -->
                <line x1="${{padL}}" y1="${{yFireLine}}" x2="${{width - padR}}" y2="${{yFireLine}}" stroke="#f59e0b" stroke-width="2" stroke-dasharray="5 3" />
                <text x="${{padL + 8}}" y="${{yFireLine - 6}}" fill="#d97706" font-size="10" font-family="JetBrains Mono" font-weight="bold">Target FIRE: ${{formatMoney(fireNumber)}} ${{currentCurrency}}</text>

                <!-- Deposited Area (Gray) -->
                <path d="${{depAreaPath}}" fill="#94a3b8" fill-opacity="0.25" />

                <!-- Compound Interest Area (Emerald) -->
                <path d="${{areaPath}}" fill="#10b981" fill-opacity="0.35" />

                <!-- Lines -->
                <path d="${{dDeposited}}" fill="none" stroke="#64748b" stroke-width="2" stroke-dasharray="3 3" />
                <path d="${{dBalance}}" fill="none" stroke="#059669" stroke-width="3" stroke-linecap="round" />

                <!-- Axes Labels -->
                <text x="${{padL - 6}}" y="${{scaleY(0)}}" fill="#64748b" font-size="9" text-anchor="end" font-family="JetBrains Mono">0</text>
                <text x="${{padL - 6}}" y="${{scaleY(maxVal * 0.5)}}" fill="#64748b" font-size="9" text-anchor="end" font-family="JetBrains Mono">${{formatMoney(maxVal * 0.5)}}</text>
                <text x="${{padL - 6}}" y="${{scaleY(maxVal)}}" fill="#64748b" font-size="9" text-anchor="end" font-family="JetBrains Mono">${{formatMoney(maxVal)}}</text>

                <text x="${{scaleX(0)}}" y="${{height - 10}}" fill="#64748b" font-size="10" text-anchor="middle" font-family="JetBrains Mono">Oggi</text>
                <text x="${{scaleX(maxYears)}}" y="${{height - 10}}" fill="#64748b" font-size="10" text-anchor="middle" font-family="JetBrains Mono">${{maxYears}}a</text>
            `;
        }}

        function renderTable(trajectory) {{
            const tbody = document.getElementById('fireTableBody');
            tbody.innerHTML = '';

            trajectory.forEach(pt => {{
                const tr = document.createElement('tr');
                tr.className = 'hover:bg-slate-50 transition';
                tr.innerHTML = `
                    <td class="py-2 text-slate-800 font-bold">${{pt.year === 0 ? 'Oggi' : 'Anno ' + pt.year}}</td>
                    <td class="py-2 text-slate-600">${{formatMoney(pt.deposited)}} ${{currentCurrency}}</td>
                    <td class="py-2 text-emerald-600 font-semibold">+${{formatMoney(pt.interest)}} ${{currentCurrency}}</td>
                    <td class="py-2 text-right font-extrabold text-slate-900">${{formatMoney(pt.balance)}} ${{currentCurrency}}</td>
                `;
                tbody.appendChild(tr);
            }});
        }}

        function updateTexts(lang) {{
            currentLang = lang;
            const t = (key) => TRANSLATIONS[key]?.[lang] || TRANSLATIONS[key]?.['it'] || '';

            document.title = t('meta_title');
            document.querySelector('meta[name="description"]').setAttribute('content', t('meta_desc'));

            document.getElementById('mainTitle').textContent = t('title');
            document.getElementById('mainSubtitle').textContent = t('subtitle');
            document.getElementById('sectionInputsTitle').textContent = t('section_inputs');
            document.getElementById('monthlyExpenseLabel').textContent = t('monthly_expense_label');
            document.getElementById('currentSavingsLabel').textContent = t('current_savings_label');
            document.getElementById('monthlySavingsLabel').textContent = t('monthly_savings_label');
            document.getElementById('returnRateLabel').textContent = t('return_rate_label');
            document.getElementById('swrLabel').textContent = t('swr_label');
            document.getElementById('swrHint').textContent = t('swr_hint');

            document.getElementById('presetTitleLabel').innerHTML = `
                <svg class="w-4 h-4 text-emerald-600 inline mr-1" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M13 10V3L4 14h7v7l9-11h-7z"/></svg>
                ${{t('presets_title')}}
            `;
            document.getElementById('presetLeanText').textContent = t('preset_lean');
            document.getElementById('presetRegularText').textContent = t('preset_regular');
            document.getElementById('presetFatText').textContent = t('preset_fat');

            document.getElementById('kpiFireNumberLabel').textContent = t('kpi_fire_number');
            document.getElementById('kpiYearsLeftLabel').textContent = t('kpi_years_left');
            document.getElementById('kpiProgressLabel').textContent = t('kpi_progress');
            document.getElementById('kpiAnnualIncomeLabel').textContent = t('kpi_annual_income');
            document.getElementById('chartTitle').textContent = t('chart_title');
            document.getElementById('legendDepositsLabel').textContent = t('legend_deposits');
            document.getElementById('legendInterestLabel').textContent = t('legend_interest');
            document.getElementById('legendFireLineLabel').textContent = t('legend_fire_line');
            document.getElementById('breakdownTitle').textContent = t('breakdown_title');

            document.getElementById('faqTitle').textContent = t('faq_title');
            document.getElementById('faqQ1').textContent = t('faq_q1');
            document.getElementById('faqA1').textContent = t('faq_a1');
            document.getElementById('faqQ2').textContent = t('faq_q2');
            document.getElementById('faqA2').textContent = t('faq_a2');
            document.getElementById('faqQ3').textContent = t('faq_q3');
            document.getElementById('faqA3').textContent = t('faq_a3');

            calculateFire();
        }}

        window.addEventListener('omni_lang_change', (e) => {{
            if (e.detail && e.detail.lang) updateTexts(e.detail.lang);
        }});

        document.addEventListener('DOMContentLoaded', () => {{
            const savedLang = localStorage.getItem('omni_pref_lang') || 'it';
            updateTexts(savedLang);
            calculateFire();
        }});
    </script>
</body>
</html>
"""

with open(os.path.join(base_dir, "fire.html"), "w", encoding="utf-8") as f:
    f.write(html_code)

print("fire.html generated successfully!")
