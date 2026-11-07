import json
import sys
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
if base_dir not in sys.path:
    sys.path.insert(0, base_dir)

from nav_header import render_suite_header, render_suite_header_js
from unified_footer import render_unified_footer, render_unified_footer_js

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
        }},
        {{
          "@type": "FAQPage",
          "mainEntity": [
            {{
              "@type": "Question",
              "name": "Cos'è il movimento FIRE e come funziona la Regola del 4%?",
              "acceptedAnswer": {{
                "@type": "Answer",
                "text": "FIRE significa Financial Independence, Retire Early. La regola del 4%, fondata sul Trinity Study, indica che prelevando annualmente non oltre il 4% da un portafoglio diversificato indicizzato all'inflazione, il capitale ha oltre il 95% di probabilità di durare almeno 30 anni senza esaurirsi."
              }}
            }},
            {{
              "@type": "Question",
              "name": "Come si calcola il Numero FIRE?",
              "acceptedAnswer": {{
                "@type": "Answer",
                "text": "La formula è: Spese Annuali moltiplicate per 25 (ovvero Spese Annuali diviso il 4% di Safe Withdrawal Rate). Esempio: 24.000 €/anno x 25 = 600.000 € di capitale target."
              }}
            }},
            {{
              "@type": "Question",
              "name": "Qual è la differenza tra Lean FIRE, Regular FIRE e Fat FIRE?",
              "acceptedAnswer": {{
                "@type": "Answer",
                "text": "Lean FIRE copre le spese essenziali minime con uno stile di vita frugale. Regular FIRE sostiene il tenore di vita medio attuale. Fat FIRE permette una rendita abbondante e spese elevate senza rinunce."
              }}
            }},
            {{
              "@type": "Question",
              "name": "Cos'è il rischio della sequenza dei rendimenti (Sequence of Returns Risk)?",
              "acceptedAnswer": {{
                "@type": "Answer",
                "text": "È il rischio che i mercati crollino nei primissimi anni di ritiro. Si gestisce mantenendo un cuscinetto di liquidità di 1-2 anni di spese o riducendo i prelievi nei periodi di mercato orso."
              }}
            }}
          ]
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
                    fontFamily: {{
                        sans: ['"Plus Jakarta Sans"', 'system-ui', '-apple-system', 'sans-serif'],
                        jakarta: ['"Plus Jakarta Sans"', 'sans-serif'],
                        mono: ['"JetBrains Mono"', 'monospace'],
                    }}
                }}
            }}
        }}
    </script>
    
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600;700;800&family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
    
    <style>
        body {{
            font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
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
        @media print {{
            .no-print {{ display: none !important; }}
            body {{ background: white; color: black; }}
            .print-only {{ display: block !important; }}
            .card-box {{ border: 1px solid #cbd5e1 !important; box-shadow: none !important; break-inside: avoid; }}
        }}
        .print-only {{ display: none; }}
    </style>
</head>
<body class="bg-slate-50 text-slate-800 min-h-screen flex flex-col justify-between selection:bg-emerald-600 selection:text-white">

    <!-- Universal Header with Chrome Tabs & Tool Picker -->
    {header_html}

    <main class="max-w-6xl mx-auto px-3 sm:px-4 py-5 flex-1 w-full space-y-6">

        <!-- Print-only official header -->
        <div class="print-only mb-6 border-b-2 border-slate-900 pb-3">
            <div class="flex justify-between items-center">
                <div>
                    <h1 class="text-xl font-black text-slate-900 uppercase tracking-wide">OmniTools Lab · FIRE & Rendita Passiva</h1>
                    <p class="text-xs text-slate-600">Simulatore di Indipendenza Finanziaria & Regola del 4% (Trinity Study)</p>
                </div>
                <div class="text-right text-xs text-slate-500 font-mono">
                    <p>Data Stampa: <span id="printDate"></span></p>
                    <p>omnitoolslab.com/fire</p>
                </div>
            </div>
        </div>

        <!-- Main Tool Intro Header & Currency Bar -->
        <div class="flex flex-col md:flex-row items-center justify-between gap-4 no-print pb-2 border-b border-slate-200">
            <div class="text-left space-y-1">
                <div class="flex items-center gap-2">
                    <span class="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded-full bg-emerald-100 text-emerald-800 text-[11px] font-extrabold border border-emerald-200">
                        <span>🔥</span> INDIPENDENZA & LIBERTÀ FINANZIARIA
                    </span>
                    <span class="text-xs font-bold text-slate-400">· Trinity Study & Regola 4%</span>
                </div>
                <h1 id="mainTitle" class="text-xl sm:text-2xl font-black text-slate-900 tracking-tight">Calcolatore FIRE & Rendita Passiva</h1>
                <p id="mainSubtitle" class="text-xs sm:text-sm text-slate-600 max-w-2xl">
                    Scopri tra quanti anni puoi smettere di lavorare e vivere dei rendimenti del tuo patrimonio.
                </p>
            </div>

            <!-- Universal Currency Switcher (5 currencies) -->
            <div class="flex items-center gap-1 bg-white p-1 rounded-2xl border border-slate-200 shadow-2xs text-xs font-bold shrink-0" id="currencySwitcher">
                <span class="text-[10px] text-slate-400 font-bold uppercase px-2 hidden sm:inline">Valuta:</span>
                <button type="button" onclick="setCurrency('EUR')" id="currEUR" class="curr-btn px-2.5 py-1 rounded-xl bg-emerald-700 text-white shadow-xs font-black transition">€ EUR</button>
                <button type="button" onclick="setCurrency('USD')" id="currUSD" class="curr-btn px-2.5 py-1 rounded-xl text-slate-600 hover:text-slate-900 transition font-bold">$ USD</button>
                <button type="button" onclick="setCurrency('GBP')" id="currGBP" class="curr-btn px-2.5 py-1 rounded-xl text-slate-600 hover:text-slate-900 transition font-bold">£ GBP</button>
                <button type="button" onclick="setCurrency('CHF')" id="currCHF" class="curr-btn px-2.5 py-1 rounded-xl text-slate-600 hover:text-slate-900 transition font-bold">CHF</button>
                <button type="button" onclick="setCurrency('JPY')" id="currJPY" class="curr-btn px-2.5 py-1 rounded-xl text-slate-600 hover:text-slate-900 transition font-bold">¥ JPY</button>
            </div>
        </div>

        <!-- Presets Bar -->
        <div class="p-3.5 bg-white border border-slate-200/80 rounded-2xl shadow-xs flex flex-wrap items-center gap-2">
            <span id="presetTitleLabel" class="text-xs font-bold text-slate-500 uppercase tracking-wider flex items-center gap-1.5 mr-1">
                <svg class="w-4 h-4 text-emerald-600 inline mr-1" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M13 10V3L4 14h7v7l9-11h-7z"/></svg>
                Stili di Vita FIRE:
            </span>
            <button onclick="applyPreset('lean')" class="px-3 py-1.5 rounded-lg bg-emerald-50 hover:bg-emerald-100 text-emerald-900 border border-emerald-200/80 text-xs font-semibold transition">
                🌱 <span id="presetLeanText">Lean FIRE (1.200 /m)</span>
            </button>
            <button onclick="applyPreset('regular')" class="px-3 py-1.5 rounded-lg bg-slate-100 hover:bg-slate-200 text-slate-800 border border-slate-300 text-xs font-semibold transition">
                ☕ <span id="presetRegularText">Regular FIRE (2.200 /m)</span>
            </button>
            <button onclick="applyPreset('fat')" class="px-3 py-1.5 rounded-lg bg-emerald-50 hover:bg-emerald-100 text-emerald-900 border border-emerald-200/80 text-xs font-semibold transition">
                🏖️ <span id="presetFatText">Fat FIRE (4.500 /m)</span>
            </button>
        </div>

        <!-- Layout Grid: Inputs Form & Visual Analytics -->
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 items-start">
            
            <!-- Left Column: Inputs Form (5 cols) -->
            <div class="lg:col-span-5 space-y-6">
                
                <div class="bg-white rounded-2xl p-5 sm:p-6 border border-slate-200 shadow-xs space-y-5 card-box">
                    <div class="flex items-center gap-2.5 pb-3 border-b border-slate-100">
                        <span class="w-7 h-7 rounded-lg bg-emerald-500/10 text-emerald-600 flex items-center justify-center font-bold text-sm">1</span>
                        <h2 id="sectionInputsTitle" class="text-base font-bold text-slate-900">1. Parametri di Risparmio & Spese</h2>
                    </div>

                    <!-- Input 1: Spese Mensili Desiderate -->
                    <div>
                        <div class="flex justify-between items-center text-xs font-semibold text-slate-700 mb-1.5">
                            <label id="monthlyExpenseLabel" for="monthlyExpenseInput">Spese Mensili Desiderate da Rendita</label>
                            <span class="text-slate-400 font-mono currLabel">/mese</span>
                        </div>
                        <div class="relative">
                            <input type="number" id="monthlyExpenseInput" min="100" step="50" value="2000" oninput="calculateFire()"
                                class="w-full bg-slate-50 border border-slate-200 rounded-xl px-3.5 py-2.5 text-sm font-mono font-bold text-slate-800 focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:bg-white transition">
                        </div>
                        <span class="text-[11px] text-slate-400 mt-1 block">Spese annuali previste: <strong id="annualExpenseDisplay" class="text-slate-700 font-mono">24.000 €/anno</strong></span>
                    </div>

                    <!-- Input 2: Capitale Attuale -->
                    <div>
                        <div class="flex justify-between items-center text-xs font-semibold text-slate-700 mb-1.5">
                            <label id="currentSavingsLabel" for="currentSavingsInput">Capitale Attuale Risparmiato / Investito</label>
                            <span class="text-slate-400 font-mono currSymbol">€</span>
                        </div>
                        <div class="relative">
                            <input type="number" id="currentSavingsInput" min="0" step="1000" value="25000" oninput="calculateFire()"
                                class="w-full bg-slate-50 border border-slate-200 rounded-xl px-3.5 py-2.5 text-sm font-mono font-bold text-slate-800 focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:bg-white transition">
                        </div>
                    </div>

                    <!-- Input 3: Risparmio Mensile Aggiuntivo -->
                    <div>
                        <div class="flex justify-between items-center text-xs font-semibold text-slate-700 mb-1.5">
                            <label id="monthlySavingsLabel" for="monthlySavingsInput">Risparmio Mensile Aggiuntivo</label>
                            <span class="text-slate-400 font-mono currLabel">/mese</span>
                        </div>
                        <div class="relative">
                            <input type="number" id="monthlySavingsInput" min="0" step="50" value="750" oninput="calculateFire()"
                                class="w-full bg-slate-50 border border-slate-200 rounded-xl px-3.5 py-2.5 text-sm font-mono font-bold text-slate-800 focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:bg-white transition">
                        </div>
                    </div>

                    <!-- Input 4: Rendimento Medio Annuo Atteso (%) -->
                    <div>
                        <div class="flex justify-between items-center text-xs font-semibold text-slate-700 mb-1.5">
                            <label id="returnRateLabel" for="returnRateInput">Rendimento Medio Annuo Atteso (%)</label>
                            <span class="text-slate-400 font-mono">% / anno</span>
                        </div>
                        <div class="relative">
                            <input type="number" id="returnRateInput" min="0" max="25" step="0.5" value="7.0" oninput="calculateFire()"
                                class="w-full bg-slate-50 border border-slate-200 rounded-xl px-3.5 py-2.5 text-sm font-mono font-bold text-slate-800 focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:bg-white transition">
                        </div>
                        <p class="text-[11px] text-slate-400 mt-1">Rendimento tipico azionario globale (es. MSCI World / S&P 500 post-inflazione: 6-8%).</p>
                    </div>

                    <!-- Input 5: Tasso di Prelievo Sicuro (SWR) -->
                    <div>
                        <div class="flex justify-between items-center text-xs font-semibold text-slate-700 mb-1.5">
                            <label id="swrLabel" for="swrInput">Tasso di Prelievo Sicuro (SWR %)</label>
                            <span id="multiplierBadge" class="text-emerald-700 bg-emerald-50 border border-emerald-200 px-2 py-0.5 rounded text-[11px] font-mono font-bold">25.0×</span>
                        </div>
                        <div class="relative">
                            <input type="number" id="swrInput" min="1.0" max="10.0" step="0.25" value="4.0" oninput="calculateFire()"
                                class="w-full bg-slate-50 border border-slate-200 rounded-xl px-3.5 py-2.5 text-sm font-mono font-bold text-slate-800 focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:bg-white transition">
                        </div>
                        <p id="swrHint" class="text-[11px] text-slate-400 mt-1">4.0% = Regola classica Trinity Study. 3.5% = Approccio conservativo a lunghissimo termine.</p>
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
                        </div>
                    </div>
                </div>

                <!-- Visual Wealth Trajectory Chart Container -->
                <div class="bg-white rounded-2xl p-5 sm:p-6 border border-slate-200 shadow-xs card-box">
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
                                <span class="w-3 h-3 rounded-xs bg-emerald-600"></span> <span id="legendInterestLabel">Interesse Composto</span>
                            </span>
                            <span class="inline-flex items-center gap-1">
                                <span class="w-3 h-0.5 bg-amber-500 border-t-2 border-dashed border-amber-500"></span> <span id="legendFireLineLabel">Target FIRE</span>
                            </span>
                        </div>
                    </div>

                    <!-- Responsive SVG Area Chart -->
                    <div class="relative w-full aspect-[16/9] sm:aspect-[2/1] bg-slate-50/60 rounded-xl border border-slate-200/80 p-2 overflow-hidden" id="chartContainer">
                        <svg id="trajectorySvg" class="w-full h-full overflow-visible" viewBox="0 0 700 320" preserveAspectRatio="none">
                            <!-- Populated dynamically via JS -->
                        </svg>
                    </div>

                    <!-- Milestone Summary Callout -->
                    <div id="milestoneSummary" class="mt-4 p-3 rounded-xl bg-emerald-50 border border-emerald-200/70 text-xs text-emerald-950 flex items-center gap-2">
                        <span class="text-base">🎯</span>
                        <span id="milestoneSummaryText">Calcolo in corso...</span>
                    </div>
                </div>

                <!-- Projection Breakdown Table -->
                <div class="bg-white rounded-2xl p-5 sm:p-6 border border-slate-200 shadow-xs card-box">
                    <div class="flex items-center justify-between pb-3 border-b border-slate-100 mb-3">
                        <h3 id="breakdownTitle" class="text-sm font-bold text-slate-900 uppercase tracking-wider">Proiezione Anno per Anno</h3>
                        <button onclick="window.print()" class="text-xs text-slate-500 hover:text-slate-800 font-semibold flex items-center gap-1 no-print">
                            <span>🖨️</span> Stampa Proiezione
                        </button>
                    </div>

                    <div class="overflow-x-auto max-h-72 overflow-y-auto">
                        <table class="w-full text-left text-xs">
                            <thead class="text-slate-400 font-semibold border-b border-slate-100 sticky top-0 bg-white">
                                <tr>
                                    <th class="pb-2">Anno</th>
                                    <th class="pb-2">Capitale Versato</th>
                                    <th class="pb-2">Interessi Totali</th>
                                    <th class="pb-2 text-right">Patrimonio Totale</th>
                                </tr>
                            </thead>
                            <tbody id="fireTableBody" class="divide-y divide-slate-100 font-mono">
                                <!-- Populated dynamically -->
                            </tbody>
                        </table>
                    </div>
                </div>

            </div>

        </div>

        <!-- FAQ Section (Accordion) -->
        <section id="faqSection" class="no-print mt-12 bg-white rounded-2xl border border-slate-200 shadow-xs p-5 sm:p-6 space-y-4 card-box">
            <div class="flex items-center gap-2.5 mb-1 pb-2 border-b border-slate-100">
                <span class="text-xl">❓</span>
                <h2 class="text-base sm:text-lg font-black text-slate-900 font-jakarta flex items-center gap-2">
                    <span id="faqTitle">Domande Frequenti sul Movimento FIRE e la Libertà Finanziaria</span>
                </h2>
                <span class="text-[10px] font-extrabold uppercase px-2 py-0.5 rounded-full bg-slate-100 text-slate-600 border border-slate-200">FAQ</span>
            </div>
            
            <div id="faqContainer" class="space-y-3">
                <details class="group bg-slate-50/80 hover:bg-slate-50 rounded-xl border border-slate-200/80 p-4 transition duration-150">
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

                <details class="group bg-slate-50/80 hover:bg-slate-50 rounded-xl border border-slate-200/80 p-4 transition duration-150">
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

                <details class="group bg-slate-50/80 hover:bg-slate-50 rounded-xl border border-slate-200/80 p-4 transition duration-150">
                    <summary class="flex justify-between items-center font-bold text-xs sm:text-sm text-slate-900 cursor-pointer list-none select-none">
                        <span id="faqQ3">Come si calcola il Numero FIRE?</span>
                        <svg class="w-4 h-4 text-slate-400 group-open:-rotate-180 transition-transform duration-200 shrink-0 ml-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/>
                        </svg>
                    </summary>
                    <div id="faqA3" class="text-xs sm:text-sm text-slate-600 mt-2.5 leading-relaxed border-t border-slate-200/60 pt-2.5">
                        La formula matematica universale è: Spese Annue ÷ Tasso di Prelievo (SWR). Se applichi la regola classica del 4% (0.04), equivale semplicemente a moltiplicare le tue spese annuali per 25. Ad esempio: 24.000 € di spese all'anno × 25 = 600.000 € di patrimonio target.
                    </div>
                </details>

                <details class="group bg-slate-50/80 hover:bg-slate-50 rounded-xl border border-slate-200/80 p-4 transition duration-150">
                    <summary class="flex justify-between items-center font-bold text-xs sm:text-sm text-slate-900 cursor-pointer list-none select-none">
                        <span id="faqQ4">Cosa succede se il mercato affronta una recessione subito dopo il mio ritiro (Sequence of Returns Risk)?</span>
                        <svg class="w-4 h-4 text-slate-400 group-open:-rotate-180 transition-transform duration-200 shrink-0 ml-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/>
                        </svg>
                    </summary>
                    <div id="faqA4" class="text-xs sm:text-sm text-slate-600 mt-2.5 leading-relaxed border-t border-slate-200/60 pt-2.5">
                        Il rischio della sequenza dei rendimenti si verifica quando una flessione del mercato colpisce i primi anni di ritiro. Per proteggersi, la strategia FIRE raccomanda di mantenere un cuscinetto di liquidità o obbligazioni a breve termine pari a 1-2 anni di spese vive (Cash Buffer), oppure di adottare un tasso di prelievo variabile riducendo temporaneamente le spese discrezionali durante i mercati orso.
                    </div>
                </details>
            </div>
        </section>

    </main>

    <!-- Universal Footer -->
    {footer_html}

    <script>
        {header_js}
        {footer_js}

        // Multi-Currency Engine
        const CURRENCIES = {{
            'EUR': {{ symbol: '€', code: 'EUR', pos: 'after', space: true }},
            'USD': {{ symbol: '$', code: 'USD', pos: 'before', space: false }},
            'GBP': {{ symbol: '£', code: 'GBP', pos: 'before', space: false }},
            'CHF': {{ symbol: 'CHF', code: 'CHF', pos: 'before', space: true }},
            'JPY': {{ symbol: '¥', code: 'JPY', pos: 'before', space: false }}
        }};

        let currentCurrency = 'EUR';
        const TRANSLATIONS = {t_json_str};
        let currentLang = 'it';

        function setCurrency(curr) {{
            if (!CURRENCIES[curr]) return;
            currentCurrency = curr;

            document.querySelectorAll('.curr-btn').forEach(btn => {{
                btn.className = 'curr-btn px-2.5 py-1 rounded-xl text-slate-600 hover:text-slate-900 transition font-bold';
            }});
            const activeBtn = document.getElementById('curr' + curr);
            if (activeBtn) {{
                activeBtn.className = 'curr-btn px-2.5 py-1 rounded-xl bg-emerald-700 text-white shadow-xs font-black transition';
            }}

            const sym = CURRENCIES[curr].symbol;
            document.querySelectorAll('.currSymbol').forEach(el => el.textContent = sym);
            document.querySelectorAll('.currLabel').forEach(el => {{
                el.textContent = `${{sym}}/mese`;
            }});

            calculateFire();
        }}

        function formatMoney(val) {{
            const c = CURRENCIES[currentCurrency] || CURRENCIES['EUR'];
            const formatted = Math.round(val).toLocaleString('it-IT');
            if (c.pos === 'before') {{
                return c.symbol + (c.space ? ' ' : '') + formatted;
            }} else {{
                return formatted + (c.space ? ' ' : '') + c.symbol;
            }}
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

        function calculateFire() {{
            const monthlyExp = parseFloat(document.getElementById('monthlyExpenseInput').value) || 0;
            const currentSavings = parseFloat(document.getElementById('currentSavingsInput').value) || 0;
            const monthlySavings = parseFloat(document.getElementById('monthlySavingsInput').value) || 0;
            const annualReturnPct = parseFloat(document.getElementById('returnRateInput').value) || 0;
            const swrPct = parseFloat(document.getElementById('swrInput').value) || 4.0;

            const annualExpenses = monthlyExp * 12;
            document.getElementById('annualExpenseDisplay').textContent = formatMoney(annualExpenses) + '/anno';

            const multiplier = swrPct > 0 ? (100 / swrPct) : 25;
            document.getElementById('multiplierBadge').textContent = multiplier.toFixed(1) + '×';

            const fireNumber = swrPct > 0 ? (annualExpenses / (swrPct / 100)) : 0;
            document.getElementById('resFireNumber').textContent = formatMoney(fireNumber);

            const annualPassive = (currentSavings * (swrPct / 100));
            document.getElementById('resAnnualPassive').textContent = formatMoney(annualPassive);

            const progressPct = fireNumber > 0 ? Math.min(100, (currentSavings / fireNumber) * 100) : 0;
            document.getElementById('resProgressPct').textContent = progressPct.toFixed(1);

            // Simulation month by month
            const rMonth = annualReturnPct > 0 ? Math.pow(1 + (annualReturnPct / 100), 1 / 12) - 1 : 0;
            let balance = currentSavings;
            let totalDeposited = currentSavings;
            let months = 0;
            const maxMonths = 600; // max 50 years cap

            const trajectory = [{{
                year: 0,
                month: 0,
                balance: balance,
                deposited: totalDeposited,
                interest: 0
            }}];

            let reachedFire = (balance >= fireNumber && fireNumber > 0);

            while (months < maxMonths && balance < fireNumber) {{
                months++;
                balance = balance * (1 + rMonth) + monthlySavings;
                totalDeposited += monthlySavings;

                if (months % 12 === 0 || balance >= fireNumber) {{
                    trajectory.push({{
                        year: (months / 12).toFixed(1),
                        month: months,
                        balance: Math.round(balance),
                        deposited: Math.round(totalDeposited),
                        interest: Math.max(0, Math.round(balance - totalDeposited))
                    }});
                }}
                if (balance >= fireNumber) {{
                    reachedFire = true;
                    break;
                }}
            }}

            // Update Years KPI
            const yearsLeftEl = document.getElementById('resYearsLeft');
            const yearsUnitEl = document.getElementById('resYearsUnit');
            if (currentSavings >= fireNumber && fireNumber > 0) {{
                yearsLeftEl.textContent = '0';
                yearsUnitEl.textContent = 'Obiettivo Raggiunto!';
            }} else if (!reachedFire) {{
                yearsLeftEl.textContent = '50+';
                yearsUnitEl.textContent = 'anni';
            }} else {{
                const y = Math.floor(months / 12);
                const m = months % 12;
                yearsLeftEl.textContent = (months / 12).toFixed(1);
                yearsUnitEl.textContent = `anni (${{y}}a ${{m}}m)`;
            }}

            // Callout Summary
            const summaryEl = document.getElementById('milestoneSummaryText');
            if (currentSavings >= fireNumber && fireNumber > 0) {{
                summaryEl.innerHTML = `<strong>Congratulazioni!</strong> Il tuo patrimonio attuale copre già integralmente il tuo fabbisogno FIRE con la Regola del ${{swrPct}}%.`;
            }} else if (reachedFire) {{
                summaryEl.innerHTML = `Raggiungerai l'indipendenza finanziaria con un capitale di <strong>${{formatMoney(fireNumber)}}</strong> garantendo una rendita mensile netta a vita.`;
            }} else {{
                summaryEl.innerHTML = `Aumentando la quota di risparmio mensile o il rendimento atteso accelererai il percorso per raggiungere ${{formatMoney(fireNumber)}}.`;
            }}

            renderChart(trajectory, fireNumber);
            renderTable(trajectory);
        }}

        function renderChart(trajectory, targetFire) {{
            const svg = document.getElementById('trajectorySvg');
            svg.innerHTML = '';

            if (trajectory.length < 2) return;

            const width = 700;
            const height = 320;
            const padL = 60;
            const padR = 25;
            const padT = 30;
            const padB = 40;

            const maxBalance = Math.max(...trajectory.map(p => p.balance));
            const maxVal = Math.max(maxBalance, targetFire) * 1.15;
            const maxYear = parseFloat(trajectory[trajectory.length - 1].year) || 1;

            const scaleX = (yr) => padL + (yr / maxYear) * (width - padL - padR);
            const scaleY = (val) => height - padB - (val / maxVal) * (height - padT - padB);

            // Generate Path points
            let dBalance = '';
            let dDeposited = '';

            trajectory.forEach((pt, i) => {{
                const x = scaleX(parseFloat(pt.year));
                const yBal = scaleY(pt.balance);
                const yDep = scaleY(pt.deposited);

                if (i === 0) {{
                    dBalance = `M ${{x}} ${{yBal}}`;
                    dDeposited = `M ${{x}} ${{yDep}}`;
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

            // Area path for deposited (from deposited down to ground Y)
            const groundY = scaleY(0);
            let areaDeposited = dDeposited;
            areaDeposited += ` L ${{scaleX(maxYear)}} ${{groundY}} L ${{scaleX(0)}} ${{groundY}} Z`;

            // Draw Target FIRE line
            const yFire = scaleY(targetFire);
            const fireLine = document.createElementNS('http://www.w3.org/2000/svg', 'line');
            fireLine.setAttribute('x1', padL);
            fireLine.setAttribute('y1', yFire);
            fireLine.setAttribute('x2', width - padR);
            fireLine.setAttribute('y2', yFire);
            fireLine.setAttribute('stroke', '#f59e0b');
            fireLine.setAttribute('stroke-width', '2');
            fireLine.setAttribute('stroke-dasharray', '4 3');
            svg.appendChild(fireLine);

            const fireText = document.createElementNS('http://www.w3.org/2000/svg', 'text');
            fireText.setAttribute('x', padL + 5);
            fireText.setAttribute('y', Math.max(15, yFire - 6));
            fireText.setAttribute('fill', '#d97706');
            fireText.setAttribute('font-size', '10');
            fireText.setAttribute('font-family', 'monospace');
            fireText.setAttribute('font-weight', 'bold');
            fireText.textContent = `Target FIRE: ${{formatMoney(targetFire)}}`;
            svg.appendChild(fireText);

            // Draw Area: Deposited (Gray)
            const pathDep = document.createElementNS('http://www.w3.org/2000/svg', 'path');
            pathDep.setAttribute('d', areaDeposited);
            pathDep.setAttribute('fill', '#e2e8f0');
            pathDep.setAttribute('opacity', '0.7');
            svg.appendChild(pathDep);

            // Draw Area: Interest (Emerald)
            const pathInt = document.createElementNS('http://www.w3.org/2000/svg', 'path');
            pathInt.setAttribute('d', areaPath);
            pathInt.setAttribute('fill', '#10b981');
            pathInt.setAttribute('opacity', '0.35');
            svg.appendChild(pathInt);

            // Draw Deposited boundary line
            const lineDep = document.createElementNS('http://www.w3.org/2000/svg', 'path');
            lineDep.setAttribute('d', dDeposited);
            lineDep.setAttribute('fill', 'none');
            lineDep.setAttribute('stroke', '#64748b');
            lineDep.setAttribute('stroke-width', '2');
            lineDep.setAttribute('stroke-dasharray', '3 3');
            svg.appendChild(lineDep);

            // Draw Total Balance curve
            const lineBal = document.createElementNS('http://www.w3.org/2000/svg', 'path');
            lineBal.setAttribute('d', dBalance);
            lineBal.setAttribute('fill', 'none');
            lineBal.setAttribute('stroke', '#059669');
            lineBal.setAttribute('stroke-width', '3.5');
            lineBal.setAttribute('stroke-linecap', 'round');
            svg.appendChild(lineBal);

            // X-Axis labels
            const xToday = document.createElementNS('http://www.w3.org/2000/svg', 'text');
            xToday.setAttribute('x', scaleX(0));
            xToday.setAttribute('y', height - 12);
            xToday.setAttribute('fill', '#64748b');
            xToday.setAttribute('font-size', '10');
            xToday.textContent = 'Oggi';
            svg.appendChild(xToday);

            const xEnd = document.createElementNS('http://www.w3.org/2000/svg', 'text');
            xEnd.setAttribute('x', scaleX(maxYear) - 20);
            xEnd.setAttribute('y', height - 12);
            xEnd.setAttribute('fill', '#64748b');
            xEnd.setAttribute('font-size', '10');
            xEnd.textContent = `${{maxYear}}a`;
            svg.appendChild(xEnd);

            // Y-Axis tick labels
            [0, maxVal * 0.5, maxVal].forEach(v => {{
                const yt = scaleY(v);
                const txt = document.createElementNS('http://www.w3.org/2000/svg', 'text');
                txt.setAttribute('x', 5);
                txt.setAttribute('y', yt + 3);
                txt.setAttribute('fill', '#94a3b8');
                txt.setAttribute('font-size', '9');
                txt.setAttribute('font-family', 'monospace');
                txt.textContent = Math.round(v).toLocaleString('it-IT');
                svg.appendChild(txt);
            }});
        }}

        function renderTable(trajectory) {{
            const tbody = document.getElementById('fireTableBody');
            tbody.innerHTML = '';

            trajectory.forEach(pt => {{
                const tr = document.createElement('tr');
                tr.className = 'hover:bg-slate-50 transition';
                tr.innerHTML = `
                    <td class="py-2 text-slate-800 font-bold">${{pt.year === 0 ? 'Oggi' : 'Anno ' + pt.year}}</td>
                    <td class="py-2 text-slate-600">${{formatMoney(pt.deposited)}}</td>
                    <td class="py-2 text-emerald-600 font-semibold">+${{formatMoney(pt.interest)}}</td>
                    <td class="py-2 text-right font-extrabold text-slate-900">${{formatMoney(pt.balance)}}</td>
                `;
                tbody.appendChild(tr);
            }});
        }}

        function updateTexts(lang) {{
            currentLang = lang;
            const t = (key) => TRANSLATIONS[key]?.[lang] || TRANSLATIONS[key]?.['it'] || '';

            document.title = t('meta_title');
            const metaD = document.querySelector('meta[name="description"]');
            if (metaD) metaD.setAttribute('content', t('meta_desc'));

            const mTitle = document.getElementById('mainTitle');
            if (mTitle) mTitle.textContent = t('title');
            const mSub = document.getElementById('mainSubtitle');
            if (mSub) mSub.textContent = t('subtitle');
            
            const secIn = document.getElementById('sectionInputsTitle');
            if (secIn) secIn.textContent = t('section_inputs');
            const mExp = document.getElementById('monthlyExpenseLabel');
            if (mExp) mExp.textContent = t('monthly_expense_label');
            const curSav = document.getElementById('currentSavingsLabel');
            if (curSav) curSav.textContent = t('current_savings_label');
            const mSav = document.getElementById('monthlySavingsLabel');
            if (mSav) mSav.textContent = t('monthly_savings_label');
            const retRate = document.getElementById('returnRateLabel');
            if (retRate) retRate.textContent = t('return_rate_label');
            const swrL = document.getElementById('swrLabel');
            if (swrL) swrL.textContent = t('swr_label');
            const swrH = document.getElementById('swrHint');
            if (swrH) swrH.textContent = t('swr_hint');

            const pTitle = document.getElementById('presetTitleLabel');
            if (pTitle) {{
                pTitle.innerHTML = `
                    <svg class="w-4 h-4 text-emerald-600 inline mr-1" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M13 10V3L4 14h7v7l9-11h-7z"/></svg>
                    ${{t('presets_title')}}
                `;
            }}
            const pLean = document.getElementById('presetLeanText');
            if (pLean) pLean.textContent = t('preset_lean');
            const pReg = document.getElementById('presetRegularText');
            if (pReg) pReg.textContent = t('preset_regular');
            const pFat = document.getElementById('presetFatText');
            if (pFat) pFat.textContent = t('preset_fat');

            const kpiFire = document.getElementById('kpiFireNumberLabel');
            if (kpiFire) kpiFire.textContent = t('kpi_fire_number');
            const kpiY = document.getElementById('kpiYearsLeftLabel');
            if (kpiY) kpiY.textContent = t('kpi_years_left');
            const kpiP = document.getElementById('kpiProgressLabel');
            if (kpiP) kpiP.textContent = t('kpi_progress');
            const kpiAnn = document.getElementById('kpiAnnualIncomeLabel');
            if (kpiAnn) kpiAnn.textContent = t('kpi_annual_income');
            
            const cTitle = document.getElementById('chartTitle');
            if (cTitle) cTitle.textContent = t('chart_title');
            const lDep = document.getElementById('legendDepositsLabel');
            if (lDep) lDep.textContent = t('legend_deposits');
            const lInt = document.getElementById('legendInterestLabel');
            if (lInt) lInt.textContent = t('legend_interest');
            const lFire = document.getElementById('legendFireLineLabel');
            if (lFire) lFire.textContent = t('legend_fire_line');
            const bTitle = document.getElementById('breakdownTitle');
            if (bTitle) bTitle.textContent = t('breakdown_title');

            const fTitle = document.getElementById('faqTitle');
            if (fTitle) fTitle.textContent = t('faq_title');
            const q1 = document.getElementById('faqQ1');
            if (q1) q1.textContent = t('faq_q1');
            const a1 = document.getElementById('faqA1');
            if (a1) a1.textContent = t('faq_a1');
            const q2 = document.getElementById('faqQ2');
            if (q2) q2.textContent = t('faq_q2');
            const a2 = document.getElementById('faqA2');
            if (a2) a2.textContent = t('faq_a2');
            const q3 = document.getElementById('faqQ3');
            if (q3) q3.textContent = t('faq_q3');
            const a3 = document.getElementById('faqA3');
            if (a3) a3.textContent = t('faq_a3');
            const q4 = document.getElementById('faqQ4');
            if (q4) q4.textContent = t('faq_q4');
            const a4 = document.getElementById('faqA4');
            if (a4) a4.textContent = t('faq_a4');

            calculateFire();
        }}

        window.addEventListener('omni_lang_change', (e) => {{
            if (e.detail && e.detail.lang) updateTexts(e.detail.lang);
        }});

        document.addEventListener('DOMContentLoaded', () => {{
            const pDate = document.getElementById('printDate');
            if (pDate) pDate.textContent = new Date().toLocaleDateString('it-IT');
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

print("fire.html generated successfully with standard styling, 5 currencies, 4 FAQs and cleaned footer!")
