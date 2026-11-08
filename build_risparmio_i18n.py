import json
import sys
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
if base_dir not in sys.path:
    sys.path.insert(0, base_dir)

from nav_header import render_suite_header, render_suite_header_js
from unified_footer import render_unified_footer, render_unified_footer_js

with open(os.path.join(base_dir, "translations_risparmio.json"), "r", encoding="utf-8") as f:
    t_data = json.load(f)

t_json_str = json.dumps(t_data, ensure_ascii=False)

header_html = render_suite_header("risparmio")
header_js = render_suite_header_js()
footer_html = render_unified_footer("risparmio")
footer_js = render_unified_footer_js()

html_code = f"""<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0">
    <meta name="google-site-verification" content="MRdbDm9lLhokeD3I0FOpUSOhNaF_2WaveKvu52FxtG4">
    <title>Calcolo Obiettivo di Risparmio & Sinking Fund Online — Quanto Risparmiare al Mese | ObiettivoRisparmio</title>
    <meta name="description" content="Calcolatore professionale per obiettivi di risparmio e Sinking Fund. Calcola la quota mensile esatta da accantonare per comprare casa, fondo emergenza o viaggi, con o senza rendimento composto. Esporta piano in CSV.">
    
    <!-- Canonical & SEO Meta Tags -->
    <link rel="canonical" href="https://www.omnitoolslab.com/risparmio">
    <meta name="robots" content="index, follow">
    <meta property="og:type" content="website">
    <meta property="og:title" content="ObiettivoRisparmio — Calcolatore Quota Mensile & Sinking Fund">
    <meta property="og:description" content="Pianifica i tuoi traguardi economici: scopri quanto mettere da parte ogni mese per raggiungere il tuo obiettivo finanziario.">
    <meta property="og:url" content="https://www.omnitoolslab.com/risparmio">
    <meta property="og:site_name" content="OmniTools Lab">
    
    <!-- Fonts & Styling -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {{
            theme: {{
                extend: {{
                    fontFamily: {{
                        sans: ['"Plus Jakarta Sans"', 'system-ui', '-apple-system', 'sans-serif'],
                        mono: ['"JetBrains Mono"', 'monospace'],
                    }}
                }}
            }}
        }}
    </script>
    <style>
        * {{ -webkit-tap-highlight-color: transparent; }}
        input[type="number"] {{ font-size: 16px !important; }}
        input[type=range] {{
            -webkit-appearance: none;
            height: 6px;
            background: #e2e8f0;
            border-radius: 9999px;
            outline: none;
        }}
        input[type=range]::-webkit-slider-thumb {{
            -webkit-appearance: none;
            height: 24px;
            width: 24px;
            border-radius: 50%;
            background: #059669;
            cursor: pointer;
            box-shadow: 0 2px 6px rgba(5,150,105,0.4);
            border: 2px solid #ffffff;
            transition: transform 0.1s ease;
        }}
        input[type=range]::-webkit-slider-thumb:active {{ transform: scale(1.15); }}
        @media print {{
            .no-print {{ display: none !important; }}
            body {{ background: white; color: black; }}
            .card-box {{ border: 1px solid #cbd5e1 !important; box-shadow: none !important; break-inside: avoid; }}
        }}
    </style>

    <!-- Schema.org JSON-LD Structured Data for Rich Snippets -->
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@graph": [
        {{
          "@type": "WebApplication",
          "@id": "https://www.omnitoolslab.com/risparmio#app",
          "url": "https://www.omnitoolslab.com/risparmio",
          "name": "ObiettivoRisparmio — Calcolatore Quota Risparmio Mensile & Sinking Fund",
          "applicationCategory": "FinanceApplication",
          "operatingSystem": "All",
          "browserRequirements": "Requires JavaScript. Requires HTML5.",
          "offers": {{
            "@type": "Offer",
            "price": "0",
            "priceCurrency": "EUR"
          }},
          "description": "Calcolatore gratuito di risparmio mensile per raggiungere obiettivi prefissati (anticipo casa, fondo emergenza, viaggi) con effetto interesse composto.",
          "inLanguage": ["it", "en", "es", "fr", "de", "pt"]
        }},
        {{
          "@type": "BreadcrumbList",
          "@id": "https://www.omnitoolslab.com/risparmio#breadcrumb",
          "itemListElement": [
            {{
              "@type": "ListItem",
              "position": 1,
              "name": "OmniTools Lab",
              "item": "https://www.omnitoolslab.com"
            }},
            {{
              "@type": "ListItem",
              "position": 2,
              "name": "OmniFinance",
              "item": "https://www.omnitoolslab.com/#sectionFinance"
            }},
            {{
              "@type": "ListItem",
              "position": 3,
              "name": "Obiettivo di Risparmio",
              "item": "https://www.omnitoolslab.com/risparmio"
            }}
          ]
        }},
        {{
          "@type": "FAQPage",
          "@id": "https://www.omnitoolslab.com/risparmio#faq",
          "mainEntity": [
            {{
              "@type": "Question",
              "name": "Cos'è un Sinking Fund (Fondo Spese Future)?",
              "acceptedAnswer": {{
                "@type": "Answer",
                "text": "Un Sinking Fund è una strategia di finanza personale che consiste nel mettere da parte una somma mensile fissa destinata a una spesa specifica futura nota, evitando di intaccare il fondo emergenza o ricorrere a prestiti bancari."
              }}
            }},
            {{
              "@type": "Question",
              "name": "Quanto dovrebbe essere grande un Fondo di Emergenza?",
              "acceptedAnswer": {{
                "@type": "Answer",
                "text": "La regola generale raccomanda di accantonare tra i 3 e i 6 mesi di spese vive essenziali (mutuo/affitto, bollette, spesa alimentare). Per lavoratori autonomi è consigliabile raggiungere 6-9 mesi."
              }}
            }},
            {{
              "@type": "Question",
              "name": "Conviene tenere i risparmi sul conto corrente o su un conto deposito?",
              "acceptedAnswer": {{
                "@type": "Answer",
                "text": "I soldi fermi sul conto corrente perdono potere d'acquisto a causa dell'inflazione. Per obiettivi a breve-medio termine (1-5 anni), strumenti sicuri come i conti deposito svincolabili permettono di maturare interessi senza rischi."
              }}
            }},
            {{
              "@type": "Question",
              "name": "Come calcolare la quota mensile corretta?",
              "acceptedAnswer": {{
                "@type": "Answer",
                "text": "La formula sottrae il capitale iniziale dall'obiettivo e divide per i mesi disponibili, riducendo l'importo necessario qualora i fondi vengano remunerati da un rendimento composto."
              }}
            }}
          ]
        }}
      ]
    }}
    </script>
</head>
<body class="bg-slate-50 text-slate-800 min-h-screen flex flex-col justify-between antialiased selection:bg-emerald-500 selection:text-white">

    {header_html}

    <main class="max-w-5xl mx-auto px-3 sm:px-6 py-2.5 sm:py-5 flex-1 w-full space-y-3 sm:space-y-5">
        
        <!-- Hero Header & Currency Bar -->
        <div class="flex flex-col md:flex-row items-center justify-between gap-4 no-print pb-2 border-b border-slate-200">
            <div class="text-left space-y-1">
                <div class="flex items-center gap-2">
                    <span class="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded-full bg-emerald-100 text-emerald-800 text-[11px] font-extrabold border border-emerald-200">
                        <span>🎯</span> <span id="heroBadge">OMNIFINANCE · OBIETTIVI & SINKING FUND</span>
                    </span>
                    <span class="text-xs font-bold text-slate-400">· Pianificazione Spese & Risparmio</span>
                </div>
                <h1 id="heroTitle" class="text-xl sm:text-2xl font-black text-slate-900 tracking-tight">Calcolatore Obiettivo di Risparmio</h1>
                <p id="heroDesc" class="text-xs sm:text-sm text-slate-600">
                    Quanto devi mettere da parte al mese per raggiungere il tuo traguardo economico? Pianifica anticipo casa o fondo emergenza.
                </p>
            </div>

            <!-- Currency Switcher -->
            <div class="flex items-center gap-1 bg-white p-1 rounded-2xl border border-slate-200 shadow-2xs text-xs font-bold shrink-0" id="currencySwitcher">
                <span class="text-[10px] text-slate-400 font-bold uppercase px-2 hidden sm:inline">Valuta:</span>
                <button type="button" onclick="setCurrency('EUR')" id="currEUR" class="curr-btn px-2.5 py-1 rounded-xl bg-emerald-700 text-white shadow-xs font-black transition">€ EUR</button>
                <button type="button" onclick="setCurrency('USD')" id="currUSD" class="curr-btn px-2.5 py-1 rounded-xl text-slate-600 hover:text-slate-900 transition font-bold">$ USD</button>
                <button type="button" onclick="setCurrency('GBP')" id="currGBP" class="curr-btn px-2.5 py-1 rounded-xl text-slate-600 hover:text-slate-900 transition font-bold">£ GBP</button>
                <button type="button" onclick="setCurrency('CHF')" id="currCHF" class="curr-btn px-2.5 py-1 rounded-xl text-slate-600 hover:text-slate-900 transition font-bold">CHF</button>
                <button type="button" onclick="setCurrency('JPY')" id="currJPY" class="curr-btn px-2.5 py-1 rounded-xl text-slate-600 hover:text-slate-900 transition font-bold">¥ JPY</button>
            </div>
        </div>

        <!-- Google Featured Snippet (Position 0) Callout Box -->
        <section aria-label="Formula Calcolo Risparmio Mensile" class="no-print bg-gradient-to-r from-emerald-50 to-teal-50 border border-emerald-200/80 rounded-2xl p-3.5 sm:p-4 text-slate-800 shadow-xs mb-3">
            <div class="flex items-start gap-3">
                <span class="w-7 h-7 sm:w-8 sm:h-8 rounded-xl bg-emerald-600 text-white flex items-center justify-center font-bold text-xs sm:text-sm shrink-0 shadow-xs">fx</span>
                <div class="text-xs sm:text-sm space-y-1">
                    <p class="font-extrabold text-slate-900 tracking-tight text-xs sm:text-sm">
                        Formula Quota Risparmio Mensile (Sinking Fund): <code class="bg-white px-2 py-0.5 rounded-md border border-emerald-200 text-emerald-800 font-mono font-black">Quota Mese = (Obiettivo - Anticipo × (1+i)ⁿ) × [ i / ((1+i)ⁿ - 1) ]</code>
                    </p>
                    <p class="text-slate-600 text-[11px] sm:text-xs leading-relaxed">
                        <strong>Esempio pratico:</strong> Per accumulare un anticipo casa di <code class="font-bold">30.000 €</code> in <code class="font-bold">3 anni (36 mesi)</code> partendo da <code class="font-bold">5.000 €</code> con un conto deposito al <code class="font-bold">2,5% annuo</code>:
                        devi accantonare esattamente <code class="font-mono text-emerald-800 font-bold">660,15 € al mese</code>. Gli interessi composti ti regalano ben <code class="font-mono text-emerald-800 font-bold">1.234 €</code>, riducendo i soldi che devi sborsare di tasca tua!
                    </p>
                </div>
            </div>
        </section>

        <!-- Main Interactive Grid -->
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 items-start">
            
            <!-- CONTROLS COLUMN (5 Cols) -->
            <div class="lg:col-span-5 bg-white rounded-2xl p-4 sm:p-5 border border-slate-200 shadow-xs space-y-4 card-box">
                <div class="pb-2 border-b border-slate-100 flex items-center justify-between">
                    <span class="text-xs font-bold uppercase tracking-wider text-slate-700 flex items-center gap-1.5">
                        <span>🎯</span> Imposta il Tuo Traguardo
                    </span>
                    <button type="button" onclick="resetDefaults()" class="text-[11px] font-semibold text-slate-500 hover:text-slate-800">Reimposta</button>
                </div>

                <!-- Obiettivo Finale -->
                <div>
                    <div class="flex justify-between items-center mb-1">
                        <label class="text-xs font-bold text-slate-700">Somma da Raggiungere (<span class="currencySymbol">€</span>)</label>
                        <span id="badgeTarget" class="text-xs font-bold font-mono text-emerald-700 bg-emerald-50 px-2 py-0.5 rounded border border-emerald-200">30.000 €</span>
                    </div>
                    <div class="relative">
                        <input type="number" id="inputTarget" value="30000" min="500" max="2000000" step="500" oninput="syncFromInput('Target')" class="w-full p-2.5 bg-slate-50 border border-slate-200 rounded-xl font-bold font-mono text-base text-slate-900 focus:outline-none focus:ring-2 focus:ring-emerald-500">
                    </div>
                    <input type="range" id="rangeTarget" min="1000" max="150000" step="1000" value="30000" oninput="syncFromRange('Target')" class="w-full mt-2 accent-emerald-600 cursor-pointer">
                    <div class="grid grid-cols-4 gap-1 mt-1 text-[10px] font-bold no-print">
                        <button type="button" onclick="setVal('Target', 10000)" class="py-1 bg-slate-100 hover:bg-slate-200 rounded-lg text-slate-700 transition">10k</button>
                        <button type="button" onclick="setVal('Target', 25000)" class="py-1 bg-slate-100 hover:bg-slate-200 rounded-lg text-slate-700 transition">25k</button>
                        <button type="button" onclick="setVal('Target', 50000)" class="py-1 bg-slate-100 hover:bg-slate-200 rounded-lg text-slate-700 transition">50k</button>
                        <button type="button" onclick="setVal('Target', 100000)" class="py-1 bg-slate-100 hover:bg-slate-200 rounded-lg text-slate-700 transition">100k</button>
                    </div>
                </div>

                <!-- Somma Già Posseduta -->
                <div>
                    <div class="flex justify-between items-center mb-1">
                        <label class="text-xs font-bold text-slate-700">Somma Già Disponibile Oggi (<span class="currencySymbol">€</span>)</label>
                        <span id="badgeInitial" class="text-xs font-bold font-mono text-slate-800 bg-slate-100 px-2 py-0.5 rounded border border-slate-200">5.000 €</span>
                    </div>
                    <div class="relative">
                        <input type="number" id="inputInitial" value="5000" min="0" max="1000000" step="500" oninput="syncFromInput('Initial')" class="w-full p-2.5 bg-slate-50 border border-slate-200 rounded-xl font-bold font-mono text-base text-slate-900 focus:outline-none focus:ring-2 focus:ring-emerald-500">
                    </div>
                    <input type="range" id="rangeInitial" min="0" max="50000" step="500" value="5000" oninput="syncFromRange('Initial')" class="w-full mt-2 accent-emerald-600 cursor-pointer">
                    <div class="grid grid-cols-4 gap-1 mt-1 text-[10px] font-bold no-print">
                        <button type="button" onclick="setVal('Initial', 0)" class="py-1 bg-slate-100 hover:bg-slate-200 rounded-lg text-slate-700 transition">0 €</button>
                        <button type="button" onclick="setVal('Initial', 2000)" class="py-1 bg-slate-100 hover:bg-slate-200 rounded-lg text-slate-700 transition">2k</button>
                        <button type="button" onclick="setVal('Initial', 5000)" class="py-1 bg-slate-100 hover:bg-slate-200 rounded-lg text-slate-700 transition">5k</button>
                        <button type="button" onclick="setVal('Initial', 10000)" class="py-1 bg-slate-100 hover:bg-slate-200 rounded-lg text-slate-700 transition">10k</button>
                    </div>
                </div>

                <!-- Tempo Disponibile (Anni o Mesi) -->
                <div>
                    <div class="flex justify-between items-center mb-1">
                        <label class="text-xs font-bold text-slate-700">Entro Quanto Tempo (Anni)</label>
                        <span id="badgeYears" class="text-xs font-bold font-mono text-slate-800 bg-slate-100 px-2 py-0.5 rounded border border-slate-200">3 anni (36 mesi)</span>
                    </div>
                    <div class="relative">
                        <input type="number" id="inputYears" value="3" min="0.5" max="30" step="0.5" oninput="syncFromInput('Years')" class="w-full p-2.5 bg-slate-50 border border-slate-200 rounded-xl font-bold font-mono text-base text-slate-900 focus:outline-none focus:ring-2 focus:ring-emerald-500">
                    </div>
                    <input type="range" id="rangeYears" min="1" max="15" step="0.5" value="3" oninput="syncFromRange('Years')" class="w-full mt-2 accent-emerald-600 cursor-pointer">
                    <div class="grid grid-cols-4 gap-1 mt-1 text-[10px] font-bold no-print">
                        <button type="button" onclick="setVal('Years', 1)" class="py-1 bg-slate-100 hover:bg-slate-200 rounded-lg text-slate-700 transition">1 anno</button>
                        <button type="button" onclick="setVal('Years', 2)" class="py-1 bg-slate-100 hover:bg-slate-200 rounded-lg text-slate-700 transition">2 anni</button>
                        <button type="button" onclick="setVal('Years', 3)" class="py-1 bg-slate-100 hover:bg-slate-200 rounded-lg text-slate-700 transition">3 anni</button>
                        <button type="button" onclick="setVal('Years', 5)" class="py-1 bg-slate-100 hover:bg-slate-200 rounded-lg text-slate-700 transition">5 anni</button>
                    </div>
                </div>

                <!-- Rendimento Annuo Stimato -->
                <div class="pt-3 border-t-2 border-emerald-500/20 bg-emerald-50/40 -mx-4 -mb-4 p-4 rounded-b-2xl">
                    <div class="flex justify-between items-center mb-1">
                        <label class="text-xs font-black text-emerald-950 flex items-center gap-1">
                            <span>📈</span> Rendimento Annuo Stimato (%)
                        </label>
                        <span id="badgeRate" class="text-xs font-black font-mono text-white bg-emerald-700 px-2 py-0.5 rounded shadow-2xs">2.50 %</span>
                    </div>
                    <div class="relative">
                        <input type="number" id="inputRate" value="2.50" min="0" max="15.0" step="0.25" oninput="syncFromInput('Rate')" class="w-full p-2.5 bg-white border-2 border-emerald-400 rounded-xl font-black font-mono text-base text-emerald-950 focus:outline-none focus:ring-2 focus:ring-emerald-600">
                    </div>
                    <input type="range" id="rangeRate" min="0" max="8.0" step="0.25" value="2.50" oninput="syncFromRange('Rate')" class="w-full mt-2 accent-emerald-700 cursor-pointer">
                    <div class="grid grid-cols-4 gap-1 mt-1 text-[10px] font-bold no-print">
                        <button type="button" onclick="setVal('Rate', 0)" class="py-1 bg-white hover:bg-emerald-100 border border-emerald-200 rounded-lg text-emerald-800 transition">0% (Conto)</button>
                        <button type="button" onclick="setVal('Rate', 2.0)" class="py-1 bg-white hover:bg-emerald-100 border border-emerald-200 rounded-lg text-emerald-800 transition">2.0% Deposito</button>
                        <button type="button" onclick="setVal('Rate', 3.5)" class="py-1 bg-white hover:bg-emerald-100 border border-emerald-200 rounded-lg text-emerald-800 transition">3.5% Bot/BTP</button>
                        <button type="button" onclick="setVal('Rate', 6.0)" class="py-1 bg-white hover:bg-emerald-100 border border-emerald-200 rounded-lg text-emerald-800 transition">6.0% ETF</button>
                    </div>
                </div>

            </div>

            <!-- RESULTS & VISUAL COLUMN (7 Cols) -->
            <div class="lg:col-span-7 space-y-4">
                
                <!-- KPI HERO CARD: QUOTA MENSILE RICHIESTA -->
                <div class="bg-gradient-to-br from-emerald-600 to-teal-800 text-white rounded-2xl p-5 shadow-lg border border-emerald-500/30 flex flex-col sm:flex-row sm:items-center justify-between gap-4">
                    <div>
                        <span class="text-xs font-bold uppercase tracking-wider text-emerald-100 block mb-1">
                            🎯 Quota Mensile da Accantonare
                        </span>
                        <div class="text-3xl sm:text-4xl font-black font-mono tracking-tight text-white" id="valMonthlyNeeded">
                            660,15 €
                        </div>
                        <span class="text-xs text-emerald-100/90 block mt-1" id="subMonthlyNeeded">
                            per 36 mesi consecutivi
                        </span>
                    </div>

                    <div class="sm:text-right border-t sm:border-t-0 sm:border-l border-emerald-400/40 pt-3 sm:pt-0 sm:pl-4">
                        <span class="text-[10px] font-bold uppercase tracking-wider text-emerald-100 block">Obiettivo Finale</span>
                        <div class="text-xl sm:text-2xl font-black font-mono text-white" id="valTargetSummary">30.000 €</div>
                        <span class="text-[11px] text-emerald-200" id="valTotalMonths">Tra 3 anni</span>
                    </div>
                </div>

                <!-- 3 CARDS DECOMPOSIZIONE (Capitale Iniziale, Risparmio Tuo, Interessi Guadagnati) -->
                <div class="grid grid-cols-3 gap-3">
                    <div class="bg-white p-3.5 rounded-2xl border border-slate-200 shadow-xs text-center">
                        <span class="text-[10px] font-bold text-slate-500 uppercase tracking-wider block mb-0.5">Hai Già</span>
                        <div class="text-base sm:text-lg font-black font-mono text-slate-800" id="valInitialCard">5.000 €</div>
                        <span class="text-[10px] text-slate-400" id="pctInitial">16.7%</span>
                    </div>
                    <div class="bg-white p-3.5 rounded-2xl border border-slate-200 shadow-xs text-center">
                        <span class="text-[10px] font-bold text-blue-600 uppercase tracking-wider block mb-0.5">Metterai Tu</span>
                        <div class="text-base sm:text-lg font-black font-mono text-blue-700" id="valTotalPutCard">23.765 €</div>
                        <span class="text-[10px] text-blue-500" id="pctPut">79.2%</span>
                    </div>
                    <div class="bg-white p-3.5 rounded-2xl border border-emerald-300 shadow-xs text-center bg-emerald-50/30">
                        <span class="text-[10px] font-bold text-emerald-700 uppercase tracking-wider block mb-0.5">Interessi Extra</span>
                        <div class="text-base sm:text-lg font-black font-mono text-emerald-600" id="valInterestCard">+1.235 €</div>
                        <span class="text-[10px] text-emerald-600 font-bold" id="pctInterest">+4.1%</span>
                    </div>
                </div>

                <!-- PROGRESS BAR & TIMELINE ACCUMULO -->
                <div class="bg-white rounded-2xl p-4 sm:p-5 border border-slate-200 shadow-xs space-y-3">
                    <div class="flex items-center justify-between text-xs font-bold text-slate-700">
                        <span class="flex items-center gap-1.5">
                            <span>📊</span> Composizione del Tuo Traguardo
                        </span>
                        <span id="progressBarLabel" class="text-emerald-700 font-mono font-black">100% Raggiunto</span>
                    </div>

                    <!-- Multi-segment progress bar -->
                    <div class="w-full bg-slate-100 rounded-full h-4 overflow-hidden flex shadow-inner">
                        <div id="barInitial" class="bg-slate-400 h-full transition-all duration-500" title="Capitale già posseduto" style="width: 17%"></div>
                        <div id="barPut" class="bg-blue-600 h-full transition-all duration-500" title="Nuovo risparmio versato" style="width: 79%"></div>
                        <div id="barInterest" class="bg-emerald-500 h-full transition-all duration-500" title="Interessi guadagnati" style="width: 4%"></div>
                    </div>

                    <div class="flex flex-wrap items-center justify-between text-[11px] text-slate-500 pt-1">
                        <div class="flex items-center gap-1.5">
                            <span class="w-2.5 h-2.5 rounded-full bg-slate-400 inline-block"></span>
                            <span>Capitale Iniziale</span>
                        </div>
                        <div class="flex items-center gap-1.5">
                            <span class="w-2.5 h-2.5 rounded-full bg-blue-600 inline-block"></span>
                            <span>Risparmio Mensile</span>
                        </div>
                        <div class="flex items-center gap-1.5">
                            <span class="w-2.5 h-2.5 rounded-full bg-emerald-500 inline-block"></span>
                            <span>Rendimento Composto</span>
                        </div>
                    </div>

                    <!-- Verdetto e Suggerimento -->
                    <div class="mt-4 pt-3 border-t border-slate-100 text-xs text-slate-600 leading-relaxed" id="verdictSummary">
                        Impostando un accantonamento automatico di <strong>660,15 €</strong> ogni mese all'arrivo dello stipendio, completerai l'obiettivo di <strong>30.000 €</strong> esattamente tra <strong>3 anni</strong>.
                    </div>
                </div>

                <!-- Export & Print Actions -->
                <div class="flex items-center justify-end gap-2 pt-1 no-print">
                    <button type="button" onclick="exportCsvPlan()" class="px-3 py-2 bg-emerald-50 hover:bg-emerald-100 text-emerald-800 border border-emerald-200 text-xs font-bold rounded-xl transition flex items-center gap-1.5 cursor-pointer">
                        <span>📊</span> <span id="btnCsvExport">Esporta Piano CSV</span>
                    </button>
                    <button type="button" onclick="window.print()" class="px-3 py-2 bg-slate-100 hover:bg-slate-200 text-slate-800 text-xs font-bold rounded-xl transition flex items-center gap-1.5 cursor-pointer">
                        <span>🖨️</span> <span id="btnPrint">Stampa Scheda A4</span>
                    </button>
                </div>

            </div>
        </div>

        <!-- FAQ SECTION (Standard OmniTools Accordion Style) -->
        <section id="faqSection" class="no-print mt-10 bg-white rounded-2xl border border-slate-200 shadow-xs p-5 sm:p-6 space-y-4">
            <div class="flex items-center gap-2.5 mb-1 pb-2 border-b border-slate-100">
                <span class="text-xl">❓</span>
                <h2 class="text-base sm:text-lg font-black text-slate-900 font-jakarta flex items-center gap-2">
                    <span id="faqTitle">Domande Frequenti su Obiettivi di Risparmio & Sinking Fund</span>
                </h2>
                <span class="text-[10px] font-extrabold uppercase px-2 py-0.5 rounded-full bg-slate-100 text-slate-600 border border-slate-200">FAQ</span>
            </div>
            
            <div id="faqContainer" class="space-y-3">
                <details class="group bg-slate-50/80 hover:bg-slate-50 rounded-xl border border-slate-200/80 p-4 transition duration-150">
                    <summary class="flex justify-between items-center font-bold text-xs sm:text-sm text-slate-900 cursor-pointer list-none select-none">
                        <span id="faq1Q">Cos'è un Sinking Fund (Fondo Spese Future)?</span>
                        <svg class="w-4 h-4 text-slate-400 group-open:-rotate-180 transition-transform duration-200 shrink-0 ml-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/>
                        </svg>
                    </summary>
                    <div id="faq1A" class="text-xs sm:text-sm text-slate-600 mt-2.5 leading-relaxed border-t border-slate-200/60 pt-2.5">
                        Un <strong>Sinking Fund</strong> è una strategia di finanza personale che consiste nel mettere da parte una somma mensile fissa destinata a una spesa specifica futura nota, evitando di intaccare il fondo emergenza o ricorrere a prestiti bancari.
                    </div>
                </details>

                <details class="group bg-slate-50/80 hover:bg-slate-50 rounded-xl border border-slate-200/80 p-4 transition duration-150">
                    <summary class="flex justify-between items-center font-bold text-xs sm:text-sm text-slate-900 cursor-pointer list-none select-none">
                        <span id="faq2Q">Quanto dovrebbe essere grande un Fondo di Emergenza?</span>
                        <svg class="w-4 h-4 text-slate-400 group-open:-rotate-180 transition-transform duration-200 shrink-0 ml-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/>
                        </svg>
                    </summary>
                    <div id="faq2A" class="text-xs sm:text-sm text-slate-600 mt-2.5 leading-relaxed border-t border-slate-200/60 pt-2.5">
                        La regola generale raccomanda di accantonare tra i <strong>3 e i 6 mesi di spese vive essenziali</strong> (mutuo/affitto, bollette, spesa alimentare). Per lavoratori autonomi è consigliabile raggiungere 6-9 mesi.
                    </div>
                </details>

                <details class="group bg-slate-50/80 hover:bg-slate-50 rounded-xl border border-slate-200/80 p-4 transition duration-150">
                    <summary class="flex justify-between items-center font-bold text-xs sm:text-sm text-slate-900 cursor-pointer list-none select-none">
                        <span id="faq3Q">Conviene tenere i risparmi sul conto corrente o su un conto deposito?</span>
                        <svg class="w-4 h-4 text-slate-400 group-open:-rotate-180 transition-transform duration-200 shrink-0 ml-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/>
                        </svg>
                    </summary>
                    <div id="faq3A" class="text-xs sm:text-sm text-slate-600 mt-2.5 leading-relaxed border-t border-slate-200/60 pt-2.5">
                        I soldi fermi sul conto corrente perdono potere d'acquisto a causa dell'inflazione. Per obiettivi a breve-medio termine (1-5 anni), strumenti sicuri come i conti deposito svincolabili permettono di maturare interessi senza rischi.
                    </div>
                </details>

                <details class="group bg-slate-50/80 hover:bg-slate-50 rounded-xl border border-slate-200/80 p-4 transition duration-150">
                    <summary class="flex justify-between items-center font-bold text-xs sm:text-sm text-slate-900 cursor-pointer list-none select-none">
                        <span id="faq4Q">Come calcolare la quota mensile corretta?</span>
                        <svg class="w-4 h-4 text-slate-400 group-open:-rotate-180 transition-transform duration-200 shrink-0 ml-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/>
                        </svg>
                    </summary>
                    <div id="faq4A" class="text-xs sm:text-sm text-slate-600 mt-2.5 leading-relaxed border-t border-slate-200/60 pt-2.5">
                        La formula sottrae il capitale iniziale dall'obiettivo e divide per i mesi disponibili, riducendo l'importo necessario qualora i fondi vengano remunerati da un rendimento composto.
                    </div>
                </details>
            </div>
        </section>

    </main>

    {footer_html}

    <script>
        {header_js}
        {footer_js}

        const TRANSLATIONS = {t_json_str};
        let currentLang = 'it';
        let currentCurrency = 'EUR';
        const CURRENCY_SYMBOLS = {{ 'EUR': '€', 'USD': '$', 'GBP': '£', 'CHF': 'CHF', 'JPY': '¥' }};

        // State variables declared at top
        let lastCalculation = null;

        function setCurrency(curr) {{
            currentCurrency = curr;
            document.querySelectorAll('.curr-btn').forEach(btn => {{
                btn.classList.remove('bg-emerald-700', 'text-white', 'font-black');
                btn.classList.add('text-slate-600', 'font-bold');
            }});
            const activeBtn = document.getElementById('curr' + curr);
            if (activeBtn) {{
                activeBtn.classList.add('bg-emerald-700', 'text-white', 'font-black');
                activeBtn.classList.remove('text-slate-600', 'font-bold');
            }}
            document.querySelectorAll('.currencySymbol').forEach(el => {{
                el.textContent = CURRENCY_SYMBOLS[curr];
            }});
            saveState();
            recalc();
        }}

        function fmtCurr(num) {{
            const sym = CURRENCY_SYMBOLS[currentCurrency];
            const formatted = Math.round(num).toLocaleString('it-IT');
            return currentCurrency === 'CHF' ? formatted + ' CHF' : (sym === '$' || sym === '£' || sym === '¥' ? sym + formatted : formatted + ' ' + sym);
        }}

        function fmtCurrDec(num) {{
            const sym = CURRENCY_SYMBOLS[currentCurrency];
            const formatted = num.toLocaleString('it-IT', {{ minimumFractionDigits: 2, maximumFractionDigits: 2 }});
            return currentCurrency === 'CHF' ? formatted + ' CHF' : (sym === '$' || sym === '£' || sym === '¥' ? sym + formatted : formatted + ' ' + sym);
        }}

        function syncFromInput(field) {{
            const val = parseFloat(document.getElementById('input' + field).value) || 0;
            document.getElementById('range' + field).value = val;
            saveState();
            recalc();
        }}

        function syncFromRange(field) {{
            const val = parseFloat(document.getElementById('range' + field).value) || 0;
            document.getElementById('input' + field).value = val;
            saveState();
            recalc();
        }}

        function setVal(field, val) {{
            document.getElementById('input' + field).value = val;
            document.getElementById('range' + field).value = val;
            saveState();
            recalc();
        }}

        function resetDefaults() {{
            setVal('Target', 30000);
            setVal('Initial', 5000);
            setVal('Years', 3);
            setVal('Rate', 2.50);
        }}

        function saveState() {{
            try {{
                const state = {{
                    target: document.getElementById('inputTarget').value,
                    initial: document.getElementById('inputInitial').value,
                    years: document.getElementById('inputYears').value,
                    rate: document.getElementById('inputRate').value,
                    curr: currentCurrency
                }};
                localStorage.setItem('omni_risparmio_state', JSON.stringify(state));
            }} catch(e) {{}}
        }}

        function loadState() {{
            try {{
                const saved = localStorage.getItem('omni_risparmio_state');
                if (saved) {{
                    const s = JSON.parse(saved);
                    if (s.target) setVal('Target', s.target);
                    if (s.initial !== undefined) setVal('Initial', s.initial);
                    if (s.years) setVal('Years', s.years);
                    if (s.rate !== undefined) setVal('Rate', s.rate);
                    if (s.curr) setCurrency(s.curr);
                }}
            }} catch(e) {{}}
        }}

        function recalc() {{
            const S_target = parseFloat(document.getElementById('inputTarget').value) || 1000;
            let S0 = parseFloat(document.getElementById('inputInitial').value) || 0;
            const years = parseFloat(document.getElementById('inputYears').value) || 1;
            const r_annual = parseFloat(document.getElementById('inputRate').value) || 0;

            if (S0 >= S_target) {{
                S0 = S_target;
                document.getElementById('inputInitial').value = S0;
                document.getElementById('rangeInitial').value = S0;
            }}

            const months = Math.max(1, Math.round(years * 12));
            const i = (r_annual / 100.0) / 12.0;

            // Badges
            document.getElementById('badgeTarget').textContent = fmtCurr(S_target);
            document.getElementById('badgeInitial').textContent = fmtCurr(S0);
            document.getElementById('badgeYears').textContent = years + ' anni (' + months + ' mesi)';
            document.getElementById('badgeRate').textContent = r_annual.toFixed(2) + ' %';

            let monthlyNeeded = 0;
            let finalInitialValue = S0;

            if (i > 0) {{
                finalInitialValue = S0 * Math.pow(1 + i, months);
                const S_rem = Math.max(0, S_target - finalInitialValue);
                monthlyNeeded = S_rem * (i / (Math.pow(1 + i, months) - 1));
            }} else {{
                finalInitialValue = S0;
                const S_rem = Math.max(0, S_target - S0);
                monthlyNeeded = S_rem / months;
            }}

            const totalPut = monthlyNeeded * months;
            const interestEarned = Math.max(0, S_target - (S0 + totalPut));

            lastCalculation = {{
                S_target, S0, years, months, r_annual, i,
                monthlyNeeded, totalPut, interestEarned, finalInitialValue
            }};

            // Render KPI
            document.getElementById('valMonthlyNeeded').textContent = fmtCurrDec(monthlyNeeded);
            document.getElementById('subMonthlyNeeded').textContent = `per ${{months}} mesi consecutivi`;
            document.getElementById('valTargetSummary').textContent = fmtCurr(S_target);
            document.getElementById('valTotalMonths').textContent = `Tra ${{years}} anni (${{months}} mesi)`;

            // Render 3 Cards
            document.getElementById('valInitialCard').textContent = fmtCurr(S0);
            const pctInitVal = ((S0 / S_target) * 100).toFixed(1);
            document.getElementById('pctInitial').textContent = pctInitVal + '%';

            document.getElementById('valTotalPutCard').textContent = fmtCurr(totalPut);
            const pctPutVal = ((totalPut / S_target) * 100).toFixed(1);
            document.getElementById('pctPut').textContent = pctPutVal + '%';

            document.getElementById('valInterestCard').textContent = '+' + fmtCurr(interestEarned);
            const pctIntVal = ((interestEarned / S_target) * 100).toFixed(1);
            document.getElementById('pctInterest').textContent = '+' + pctIntVal + '%';

            // Progress Bar Widths
            document.getElementById('barInitial').style.width = pctInitVal + '%';
            document.getElementById('barPut').style.width = pctPutVal + '%';
            document.getElementById('barInterest').style.width = pctIntVal + '%';

            // Summary text
            document.getElementById('verdictSummary').innerHTML = `
                Impostando un accantonamento automatico di <strong>${{fmtCurrDec(monthlyNeeded)}}</strong> ogni mese, 
                raggiungerai il tuo obiettivo di <strong>${{fmtCurr(S_target)}}</strong> esattamente tra <strong>${{years}} anni</strong>. 
                ${{interestEarned > 50 ? `Grazie all'interesse composto risparmierai <strong>${{fmtCurr(interestEarned)}}</strong> di versamenti!` : ''}}
            `;
        }}

        function exportCsvPlan() {{
            if (!lastCalculation) return;
            const c = lastCalculation;
            let csv = "MESE;QUOTA MENSILE;CAPITALE VERSATO TOTALE;INTERESSI MATURATI;TOTALE ACCUMULATO\\n";
            
            let curBal = c.S0;
            let totDeposited = c.S0;
            csv += `0 (Iniziale);0;${{c.S0.toFixed(2)}};0;${{c.S0.toFixed(2)}}\\n`;

            for (let m = 1; m <= c.months; m++) {{
                const interestMonth = curBal * c.i;
                curBal += interestMonth + c.monthlyNeeded;
                totDeposited += c.monthlyNeeded;
                const totInterest = curBal - totDeposited;
                csv += `${{m}};${{c.monthlyNeeded.toFixed(2)}};${{totDeposited.toFixed(2)}};${{totInterest.toFixed(2)}};${{curBal.toFixed(2)}}\\n`;
            }}

            const blob = new Blob([csv], {{ type: 'text/csv;charset=utf-8;' }});
            const url = URL.createObjectURL(blob);
            const link = document.createElement("a");
            link.setAttribute("href", url);
            link.setAttribute("download", `OmniTools_Piano_Risparmio_${{new Date().toISOString().slice(0,10)}}.csv`);
            document.body.appendChild(link);
            link.click();
            document.body.removeChild(link);
        }}

        function applyTranslations() {{
            const t = TRANSLATIONS[currentLang] || TRANSLATIONS['it'];
            document.getElementById('heroTitle').textContent = t.hero_title;
            document.getElementById('heroDesc').textContent = t.hero_desc;
            document.getElementById('btnCsvExport').textContent = t.csv_export_btn;
            document.getElementById('btnPrint').textContent = t.print_btn;
            document.getElementById('faqTitle').textContent = t.faq_title;

            document.getElementById('faq1Q').textContent = t.faq_1_q;
            document.getElementById('faq1A').innerHTML = t.faq_1_a;
            document.getElementById('faq2Q').textContent = t.faq_2_q;
            document.getElementById('faq2A').innerHTML = t.faq_2_a;
            document.getElementById('faq3Q').textContent = t.faq_3_q;
            document.getElementById('faq3A').innerHTML = t.faq_3_a;
            document.getElementById('faq4Q').textContent = t.faq_4_q;
            document.getElementById('faq4A').innerHTML = t.faq_4_a;
        }}

        function changeLanguage(lang) {{
            if (!TRANSLATIONS[lang]) return;
            currentLang = lang;
            localStorage.setItem('omnitools_lang', lang);
            const sel = document.getElementById('langSelect');
            if (sel) sel.value = lang;
            document.documentElement.lang = lang;
            applyTranslations();
            recalc();
        }}
        window.changeLanguage = changeLanguage;
        window.switchLang = changeLanguage;

        document.addEventListener('DOMContentLoaded', () => {{
            const savedLang = localStorage.getItem('omnitools_lang') || 'it';
            if (TRANSLATIONS[savedLang]) currentLang = savedLang;
            const sel = document.getElementById('langSelect');
            if (sel) sel.value = currentLang;
            loadState();
            recalc();
            applyTranslations();
        }});
    </script>
</body>
</html>
"""

out_path = os.path.join(base_dir, "risparmio.html")
with open(out_path, "w", encoding="utf-8") as f:
    f.write(html_code)

print(f"risparmio.html compiled successfully at: {out_path}")
