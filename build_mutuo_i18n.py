import os
import sys

# Ensure current dir is in path for imports
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

from nav_header import render_suite_header, render_suite_header_js
from unified_footer import render_unified_footer, render_unified_footer_js

html_content = f"""<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0">
    <title>MutuoFacile — Calcolo Rata Mutuo & Piano di Ammortamento Francese | OmniTools Lab</title>
    <meta name="description" content="Calcola la rata mensile del mutuo, il piano di ammortamento alla francese rata per rata, il totale interessi bancari e la sostenibilità rata/reddito al 33%.">
    
    <!-- Canonical & SEO -->
    <link rel="canonical" href="https://www.omnitoolslab.com/mutuo">
    <meta name="robots" content="index, follow">
    <meta property="og:type" content="website">
    <meta property="og:title" content="MutuoFacile — Calcolo Rata Mutuo & Ammortamento Francese | OmniTools">
    <meta property="og:description" content="Simulatore professionale gratuito di ammortamento mutuo, quota capitale/interessi e rapporto di sostenibilità reddituale.">
    <meta property="og:url" content="https://www.omnitoolslab.com/mutuo">
    <meta property="og:site_name" content="OmniTools Lab">
    
    <!-- Fonts & Styling -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600;700;800&family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        body {{ font-family: 'Plus Jakarta Sans', sans-serif; }}
        .font-mono {{ font-family: 'JetBrains Mono', monospace; }}
        @media print {{
            .no-print {{ display: none !important; }}
            body {{ background: white; color: black; }}
            .print-only {{ display: block !important; }}
            .card-box {{ border: 1px solid #cbd5e1 !important; box-shadow: none !important; break-inside: avoid; }}
        }}
        .print-only {{ display: none; }}
    </style>

    <!-- Schema.org WebApplication -->
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "WebApplication",
      "name": "MutuoFacile",
      "url": "https://www.omnitoolslab.com/mutuo",
      "applicationCategory": "FinanceApplication",
      "operatingSystem": "All",
      "description": "Calcolatore gratuito di rata mutuo, piano di ammortamento francese e sostenibilità rata/reddito.",
      "offers": {{
        "@type": "Offer",
        "price": "0",
        "priceCurrency": "EUR"
      }}
    }}
    </script>

    <!-- Schema.org FAQPage -->
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "FAQPage",
      "mainEntity": [
        {{
          "@type": "Question",
          "name": "Come funziona l'ammortamento progressivo alla francese?",
          "acceptedAnswer": {{
            "@type": "Answer",
            "text": "L'ammortamento alla francese prevede una rata periodica costante per tutta la durata del mutuo. Ogni rata è suddivisa in quota interessi (sul debito residuo) e quota capitale. All'inizio del piano prevale la quota interessi; col tempo la quota capitale aumenta e gli interessi si riducono progressivamente."
          }}
        }},
        {{
          "@type": "Question",
          "name": "Cos'è la regola del 33% (rapporto rata/reddito) utilizzata dalle banche?",
          "acceptedAnswer": {{
            "@type": "Answer",
            "text": "È il parametro prudenziale cardine valutato dagli istituti bancari. Di norma, la rata mensile complessiva del mutuo non dovrebbe superare il 30%-35% del reddito netto mensile dei richiedenti, garantendo la disponibilità per le spese ordinarie."
          }}
        }},
        {{
          "@type": "Question",
          "name": "Qual è la differenza fondamentale tra TAN e TAEG?",
          "acceptedAnswer": {{
            "@type": "Answer",
            "text": "Il TAN misura il tasso di interesse puro applicato al prestito. Il TAEG esprime il costo totale effettivo del mutuo, includendo per legge tutte le spese accessorie: imposta sostitutiva, istruttoria, perizia, assicurazione incendio/scoppio obbligatoria e incasso rata."
          }}
        }},
        {{
          "@type": "Question",
          "name": "Conviene scegliere un mutuo a tasso fisso o a tasso variabile?",
          "acceptedAnswer": {{
            "@type": "Answer",
            "text": "Il tasso fisso blocca la rata per l'intera durata offrendo certezza assoluta di bilancio. Il tasso variabile oscilla secondo l'Euribor: può offrire tassi di ingresso più bassi, ma espone al rischio di futuri rialzi della rata."
          }}
        }},
        {{
          "@type": "Question",
          "name": "L'estinzione anticipata o la surroga del mutuo comportano penali?",
          "acceptedAnswer": {{
            "@type": "Answer",
            "text": "No. In virtù della Legge Bersani (Legge 40/2007), per i mutui prima casa non sono ammesse penali di estinzione anticipata. La surroga consente inoltre di trasferire il mutuo verso una nuova banca a costo zero."
          }}
        }}
      ]
    }}
    </script>
</head>
<body class="bg-slate-50 text-slate-800 min-h-screen flex flex-col justify-between">

    {render_suite_header('mutuo')}

    <main class="max-w-6xl mx-auto px-3 sm:px-4 py-5 flex-1 w-full space-y-6">

        <!-- Print-only official header -->
        <div class="print-only mb-6 border-b-2 border-slate-900 pb-3">
            <div class="flex justify-between items-center">
                <div>
                    <h1 class="text-xl font-black text-slate-900 uppercase tracking-wide">OmniTools Lab · MutuoFacile</h1>
                    <p class="text-xs text-slate-600">Prospetto Finanziario di Ammortamento Francese & Sostenibilità Reddituale</p>
                </div>
                <div class="text-right text-xs text-slate-500 font-mono">
                    <p>Data Stampa: <span id="printDate"></span></p>
                    <p>omnitoolslab.com/mutuo</p>
                </div>
            </div>
        </div>

        <!-- Hero Title & Global Currency Bar -->
        <div class="flex flex-col md:flex-row items-center justify-between gap-4 no-print pb-2 border-b border-slate-200">
            <div class="text-left space-y-1">
                <div class="flex items-center gap-2">
                    <span class="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded-full bg-emerald-100 text-emerald-800 text-[11px] font-extrabold border border-emerald-200">
                        <span>🏦</span> SIMULATORE MUTUO & AMMORTAMENTO
                    </span>
                    <span class="text-xs font-bold text-slate-400">· Formula Francese Rata Costante</span>
                </div>
                <h1 class="text-xl sm:text-2xl font-black text-slate-900 tracking-tight">Calcolo Rata Mutuo & Sostenibilità Bancaria</h1>
            </div>

            <!-- Universal Currency Switcher -->
            <div class="flex items-center gap-1 bg-white p-1 rounded-2xl border border-slate-200 shadow-2xs text-xs font-bold shrink-0" id="currencySwitcher">
                <span class="text-[10px] text-slate-400 font-bold uppercase px-2 hidden sm:inline">Valuta:</span>
                <button type="button" onclick="setCurrency('EUR')" id="currEUR" class="curr-btn px-2.5 py-1 rounded-xl bg-emerald-700 text-white shadow-xs font-black transition">€ EUR</button>
                <button type="button" onclick="setCurrency('USD')" id="currUSD" class="curr-btn px-2.5 py-1 rounded-xl text-slate-600 hover:text-slate-900 transition font-bold">$ USD</button>
                <button type="button" onclick="setCurrency('GBP')" id="currGBP" class="curr-btn px-2.5 py-1 rounded-xl text-slate-600 hover:text-slate-900 transition font-bold">£ GBP</button>
                <button type="button" onclick="setCurrency('CHF')" id="currCHF" class="curr-btn px-2.5 py-1 rounded-xl text-slate-600 hover:text-slate-900 transition font-bold">CHF</button>
                <button type="button" onclick="setCurrency('JPY')" id="currJPY" class="curr-btn px-2.5 py-1 rounded-xl text-slate-600 hover:text-slate-900 transition font-bold">¥ JPY</button>
            </div>
        </div>

        <!-- Main Interactive Grid -->
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-6">

            <!-- Controls Column (5 cols) -->
            <div class="lg:col-span-5 bg-white rounded-2xl p-4 sm:p-5 border border-slate-200 shadow-xs space-y-4 card-box">
                <span class="text-xs font-bold uppercase tracking-wider text-slate-700 block pb-2 border-b border-slate-100 flex items-center justify-between">
                    <span class="flex items-center gap-1.5"><span>⚙️</span> Parametri del Finanziamento</span>
                    <div class="flex items-center gap-2">
                        <button type="button" onclick="copyShareLink()" id="btnShare" title="Copia link con i parametri attuali" class="text-[11px] font-bold text-emerald-800 bg-emerald-50 hover:bg-emerald-100 px-2 py-0.5 rounded-lg border border-emerald-200 transition flex items-center gap-1 cursor-pointer">
                            <span>🔗</span> <span id="btnShareText">Condividi</span>
                        </button>
                        <button type="button" onclick="resetDefaults()" class="text-[11px] font-semibold text-slate-500 hover:text-slate-800">Reimposta</button>
                    </div>
                </span>

                <!-- Importo Mutuo -->
                <div>
                    <div class="flex justify-between items-center mb-1">
                        <label class="text-xs font-bold text-slate-700">Importo Richiesto (<span class="currencySymbol">€</span>)</label>
                        <span id="badgeAmount" class="text-xs font-bold font-mono text-emerald-700 bg-emerald-50 px-2 py-0.5 rounded border border-emerald-200">180.000 €</span>
                    </div>
                    <div class="relative">
                        <input type="number" id="inputAmount" value="180000" min="5000" max="20000000" step="5000" oninput="syncFromInput('Amount')" class="w-full p-2.5 bg-slate-50 border border-slate-200 rounded-xl font-bold font-mono text-base text-slate-900 focus:outline-none focus:ring-2 focus:ring-emerald-500">
                    </div>
                    <input type="range" id="rangeAmount" min="30000" max="600000" step="5000" value="180000" oninput="syncFromRange('Amount')" class="w-full mt-2 accent-emerald-600 cursor-pointer">
                    <div class="grid grid-cols-4 gap-1 mt-1 text-[10px] font-bold no-print">
                        <button type="button" onclick="setAmount(100000)" class="py-1 bg-slate-100 hover:bg-slate-200 rounded-lg text-slate-700 transition">100k</button>
                        <button type="button" onclick="setAmount(180000)" class="py-1 bg-slate-100 hover:bg-slate-200 rounded-lg text-slate-700 transition">180k</button>
                        <button type="button" onclick="setAmount(250000)" class="py-1 bg-slate-100 hover:bg-slate-200 rounded-lg text-slate-700 transition">250k</button>
                        <button type="button" onclick="setAmount(350000)" class="py-1 bg-slate-100 hover:bg-slate-200 rounded-lg text-slate-700 transition">350k</button>
                    </div>
                </div>

                <!-- Durata Anni -->
                <div>
                    <div class="flex justify-between items-center mb-1">
                        <label class="text-xs font-bold text-slate-700">Durata Mutuo (Anni)</label>
                        <span id="badgeYears" class="text-xs font-bold font-mono text-slate-800 bg-slate-100 px-2 py-0.5 rounded border border-slate-200">25 anni (300 rate)</span>
                    </div>
                    <input type="number" id="inputYears" value="25" min="5" max="40" step="1" oninput="syncFromInput('Years')" class="w-full p-2.5 bg-slate-50 border border-slate-200 rounded-xl font-bold font-mono text-base text-slate-900 focus:outline-none focus:ring-2 focus:ring-emerald-500">
                    <input type="range" id="rangeYears" min="5" max="40" step="1" value="25" oninput="syncFromRange('Years')" class="w-full mt-2 accent-emerald-600 cursor-pointer">
                    <div class="grid grid-cols-4 gap-1 mt-1 text-[10px] font-bold no-print">
                        <button type="button" onclick="setYears(15)" class="py-1 bg-slate-100 hover:bg-slate-200 rounded-lg text-slate-700 transition">15a</button>
                        <button type="button" onclick="setYears(20)" class="py-1 bg-slate-100 hover:bg-slate-200 rounded-lg text-slate-700 transition">20a</button>
                        <button type="button" onclick="setYears(25)" class="py-1 bg-slate-100 hover:bg-slate-200 rounded-lg text-slate-700 transition">25a</button>
                        <button type="button" onclick="setYears(30)" class="py-1 bg-slate-100 hover:bg-slate-200 rounded-lg text-slate-700 transition">30a</button>
                    </div>
                </div>

                <!-- Tasso di Interesse Annuo (TAN) -->
                <div>
                    <div class="flex justify-between items-center mb-1">
                        <label class="text-xs font-bold text-slate-700">Tasso di Interesse Annuo (TAN %)</label>
                        <span id="badgeRate" class="text-xs font-bold font-mono text-emerald-700 bg-emerald-50 px-2 py-0.5 rounded border border-emerald-200">3.20 %</span>
                    </div>
                    <input type="number" id="inputRate" value="3.20" min="0.05" max="18.00" step="0.05" oninput="syncFromInput('Rate')" class="w-full p-2.5 bg-slate-50 border border-slate-200 rounded-xl font-bold font-mono text-base text-slate-900 focus:outline-none focus:ring-2 focus:ring-emerald-500">
                    <input type="range" id="rangeRate" min="0.5" max="8.0" step="0.05" value="3.20" oninput="syncFromRange('Rate')" class="w-full mt-2 accent-emerald-600 cursor-pointer">
                    <div class="grid grid-cols-4 gap-1 mt-1 text-[10px] font-bold no-print">
                        <button type="button" onclick="setRate(2.5)" class="py-1 bg-slate-100 hover:bg-slate-200 rounded-lg text-slate-700 transition">2.5%</button>
                        <button type="button" onclick="setRate(3.0)" class="py-1 bg-slate-100 hover:bg-slate-200 rounded-lg text-slate-700 transition">3.0%</button>
                        <button type="button" onclick="setRate(3.5)" class="py-1 bg-slate-100 hover:bg-slate-200 rounded-lg text-slate-700 transition">3.5%</button>
                        <button type="button" onclick="setRate(4.0)" class="py-1 bg-slate-100 hover:bg-slate-200 rounded-lg text-slate-700 transition">4.0%</button>
                    </div>
                </div>

                <!-- Reddito Netto Mensile (Per Sostenibilità Rata/Reddito 33%) -->
                <div class="pt-2 border-t border-slate-100">
                    <div class="flex justify-between items-center mb-1">
                        <label class="text-xs font-bold text-slate-700 flex items-center gap-1">
                            <span>🛡️</span> Reddito Netto Mensile (<span class="currencySymbol">€</span>)
                        </label>
                        <span id="badgeIncome" class="text-xs font-bold font-mono text-slate-800 bg-slate-100 px-2 py-0.5 rounded border border-slate-200">2.600 €</span>
                    </div>
                    <input type="number" id="inputIncome" value="2600" min="500" max="50000" step="50" oninput="calculateMortgage()" class="w-full p-2.5 bg-slate-50 border border-slate-200 rounded-xl font-bold font-mono text-base text-slate-900 focus:outline-none focus:ring-2 focus:ring-emerald-500">
                    <p class="text-[10px] text-slate-500 mt-1">Utilizzato dalle banche per verificare il limite massimo del 33% di indebitamento.</p>
                </div>
            </div>

            <!-- Results & Visualization Column (7 cols) -->
            <div class="lg:col-span-7 space-y-4">

                <!-- Big Primary KPI Card -->
                <div class="bg-gradient-to-br from-emerald-600 via-teal-700 to-slate-900 rounded-2xl p-5 text-white shadow-md relative overflow-hidden card-box">
                    <div class="relative z-10 flex flex-col sm:flex-row sm:items-center justify-between gap-4">
                        <div>
                            <span class="text-[11px] font-extrabold uppercase tracking-wider text-emerald-200 block">Rata Mensile Costante</span>
                            <div class="text-3xl sm:text-4xl font-black font-mono tracking-tight text-white mt-1" id="resMonthlyPayment">
                                872,75 €
                            </div>
                            <span class="text-xs text-emerald-100/90 mt-0.5 block">per <span id="resTotalInstallments" class="font-bold">300</span> mensilità</span>
                        </div>
                        <div class="bg-white/10 backdrop-blur-xs p-3 rounded-xl border border-white/20 text-right sm:text-right shrink-0">
                            <span class="text-[10px] uppercase font-bold text-emerald-200 block">Incidenza su Reddito</span>
                            <div class="text-xl font-black font-mono text-white mt-0.5" id="resDebtToIncome">33.5%</div>
                            <span class="text-[10px] font-semibold text-emerald-100" id="resDebtToIncomeTag">In Linea (≤ 35%)</span>
                        </div>
                    </div>
                </div>

                <!-- Secondary KPI Metrics Grid -->
                <div class="grid grid-cols-1 sm:grid-cols-3 gap-3">
                    <div class="bg-white rounded-xl p-3.5 border border-slate-200 shadow-2xs card-box">
                        <span class="text-[11px] font-bold text-slate-500 uppercase tracking-wider block">Capitale Richiesto</span>
                        <div class="text-lg font-black font-mono text-slate-900 mt-1" id="resPrincipal">180.000 €</div>
                        <span class="text-[10px] text-slate-500">100% finanziato</span>
                    </div>

                    <div class="bg-white rounded-xl p-3.5 border border-slate-200 shadow-2xs card-box">
                        <span class="text-[11px] font-bold text-rose-600 uppercase tracking-wider block">Totale Interessi</span>
                        <div class="text-lg font-black font-mono text-rose-600 mt-1" id="resTotalInterest">81.826 €</div>
                        <span class="text-[10px] text-slate-500" id="resInterestRatio">+45.5% sul prestito</span>
                    </div>

                    <div class="bg-white rounded-xl p-3.5 border border-slate-200 shadow-2xs card-box">
                        <span class="text-[11px] font-bold text-slate-700 uppercase tracking-wider block">Costo Totale Mutuo</span>
                        <div class="text-lg font-black font-mono text-slate-900 mt-1" id="resTotalCost">261.826 €</div>
                        <span class="text-[10px] text-slate-500">Capitale + Interessi</span>
                    </div>
                </div>

                <!-- Bank Feasibility Analysis Card -->
                <div class="bg-white rounded-xl p-4 border border-slate-200 shadow-2xs space-y-2 card-box" id="affordabilityCard">
                    <div class="flex items-center justify-between">
                        <span class="text-xs font-bold text-slate-800 flex items-center gap-1.5">
                            <span>🏛️</span> Valutazione Bancaria di Fattibilità (Regola del Terzo)
                        </span>
                        <span id="affordTag" class="text-[10px] font-extrabold uppercase px-2 py-0.5 bg-emerald-100 text-emerald-800 rounded border border-emerald-300">
                            Fattibile (33%)
                        </span>
                    </div>
                    <p class="text-xs text-slate-600 leading-relaxed" id="affordDesc">
                        La rata assorbe il 33.5% del tuo reddito netto mensile. Rientra nella soglia canonica di sostenibilità bancaria (massimo 30-35%).
                    </p>
                </div>

                <!-- SVG Visualization of Yearly Amortization (Capital vs Interest) -->
                <div class="bg-slate-900 text-white rounded-2xl p-4 shadow-sm space-y-3 card-box">
                    <div class="flex items-center justify-between text-xs">
                        <span class="font-bold flex items-center gap-1.5">
                            <span>📊</span> Decomposizione Rata Annuale (Interessi vs Capitale)
                        </span>
                        <div class="flex items-center gap-3 text-[10px] font-mono">
                            <span class="flex items-center gap-1"><span class="w-2.5 h-2.5 bg-emerald-500 rounded-xs"></span> Capitale</span>
                            <span class="flex items-center gap-1"><span class="w-2.5 h-2.5 bg-rose-500 rounded-xs"></span> Interessi</span>
                        </div>
                    </div>

                    <!-- SVG Chart Container -->
                    <div class="w-full overflow-hidden">
                        <svg id="mortgageSvg" class="w-full h-44" viewBox="0 0 520 200" preserveAspectRatio="none"></svg>
                    </div>
                    <p class="text-[10px] text-slate-400 text-center font-mono">
                        Ammortamento alla Francese: le prime rate hanno una quota interessi elevata, mentre con il passare degli anni la quota capitale diventa prevalente.
                    </p>
                </div>

                <!-- Amortization Schedule Table Accordion -->
                <div class="bg-white rounded-2xl border border-slate-200 shadow-2xs overflow-hidden card-box">
                    <div class="p-3.5 bg-slate-100/80 border-b border-slate-200 flex items-center justify-between">
                        <span class="text-xs font-bold text-slate-800 flex items-center gap-1.5">
                            <span>📅</span> Prospetto di Ammortamento Sintetico (Anno per Anno)
                        </span>
                        <span class="text-[10px] font-mono text-slate-500">Quota Capitale / Quota Interessi / Debito Residuo</span>
                    </div>
                    <div class="max-h-60 overflow-y-auto">
                        <table class="w-full text-xs text-left">
                            <thead class="bg-slate-50 text-[10px] font-bold text-slate-500 uppercase sticky top-0 border-b border-slate-200">
                                <tr>
                                    <th class="p-2">Anno</th>
                                    <th class="p-2 text-right">Quota Capitale</th>
                                    <th class="p-2 text-right">Quota Interessi</th>
                                    <th class="p-2 text-right">Debito Residuo</th>
                                </tr>
                            </thead>
                            <tbody id="tableBody" class="divide-y divide-slate-100 font-mono text-[11px]">
                                <!-- Generato via JS -->
                            </tbody>
                        </table>
                    </div>
                </div>

            </div>
        </div>

        <!-- Technical Legal Disclaimer Box (TUF / D.Lgs. 58/1998) -->
        <div class="p-4 bg-slate-100 rounded-2xl border border-slate-200 text-[11px] leading-relaxed text-slate-600 space-y-1.5 card-box">
            <div class="flex items-center gap-1.5 font-bold text-slate-800">
                <span>⚖️</span>
                <span>Nota Tecnica & Disclaimer Legale (OmniFinance):</span>
            </div>
            <p>
                Questo simulatore calcola la rata e il piano di ammortamento progressivo alla francese (rata costante con quota capitale crescente e quota interessi decrescente) mediante la formula matematica standard: 
                <span class="font-mono bg-white px-1.5 py-0.5 rounded border border-slate-200">R = C × [r / (1 - (1 + r)^(-n))]</span>.
            </p>
            <p>
                I risultati hanno scopo puramente informativo ed educativo e <strong>non costituiscono proposta contrattuale, preventivo vincolante né sollecitazione al credito</strong>. Il calcolo non include spese accessorie quali: imposta sostitutiva di legge (0,25% prima casa, 2% seconda casa), costi di perizia tecnica e istruttoria bancaria, polizze incendio e scoppio obbligatorie o opzionali (CPI), commissioni di incasso rata o oscillazioni dei tassi variabili (Euribor). Rivolgersi sempre all'istituto di credito per il prospetto informativo europeo standardizzato (PIES).
            </p>
        </div>

        <!-- FAQ Section -->
        <section class="bg-white rounded-3xl p-5 sm:p-7 border border-slate-200 shadow-xs space-y-4 no-print card-box">
            <div class="flex items-center justify-between pb-3 border-b border-slate-100">
                <div class="flex items-center gap-2.5">
                    <div class="w-8 h-8 rounded-xl bg-emerald-100 text-emerald-800 flex items-center justify-center font-bold text-sm">
                        ❓
                    </div>
                    <h2 class="text-base sm:text-lg font-black text-slate-900 font-jakarta flex items-center gap-2">
                        <span>Domande Frequenti su Rata Mutuo & Ammortamento</span>
                    </h2>
                </div>
                <span class="text-[10px] font-extrabold uppercase px-2 py-0.5 rounded-full bg-slate-100 text-slate-600 border border-slate-200">FAQ</span>
            </div>
            
            <div class="space-y-2.5">
                <details class="group bg-slate-50/80 hover:bg-slate-50 rounded-2xl border border-slate-200/80 p-4 transition duration-150" open>
                    <summary class="flex justify-between items-center font-bold text-xs sm:text-sm text-slate-900 cursor-pointer list-none select-none">
                        <span>Come funziona l'ammortamento progressivo alla francese?</span>
                        <svg class="w-4 h-4 text-slate-400 group-open:-rotate-180 transition-transform duration-200 shrink-0 ml-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/>
                        </svg>
                    </summary>
                    <div class="text-xs sm:text-sm text-slate-600 mt-2.5 leading-relaxed border-t border-slate-200/60 pt-2.5">
                        L'ammortamento alla francese è il piano più diffuso in Italia ed Europa. Prevede una <strong>rata periodica costante</strong> per tutta la durata del finanziamento. Ogni rata è suddivisa in <em>quota interessi</em> (calcolata sul debito residuo) e <em>quota capitale</em>. Nei primi anni, poiché il debito residuo è elevato, la rata è composta prevalentemente da interessi; col passare del tempo il capitale viene via via rimborsato, riducendo gli interessi e aumentando progressivamente la quota di capitale restituita ogni mese.
                    </div>
                </details>

                <details class="group bg-slate-50/80 hover:bg-slate-50 rounded-2xl border border-slate-200/80 p-4 transition duration-150">
                    <summary class="flex justify-between items-center font-bold text-xs sm:text-sm text-slate-900 cursor-pointer list-none select-none">
                        <span>Cos'è la regola bancaria del 33% (rapporto rata/reddito)?</span>
                        <svg class="w-4 h-4 text-slate-400 group-open:-rotate-180 transition-transform duration-200 shrink-0 ml-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/>
                        </svg>
                    </summary>
                    <div class="text-xs sm:text-sm text-slate-600 mt-2.5 leading-relaxed border-t border-slate-200/60 pt-2.5">
                        È il parametro prudenziale cardine (Debt-to-Income / DTI) utilizzato dagli istituti bancari per valutare il merito creditizio. Di norma, l'importo della rata mensile non deve superare un terzo (<strong>30% - 35%</strong>) del reddito netto mensile complessivo dei richiedenti (al netto di altri prestiti personali o finanziamenti auto già in essere), garantendo una soglia minima di sussistenza per le spese correnti e imprevisti.
                    </div>
                </details>

                <details class="group bg-slate-50/80 hover:bg-slate-50 rounded-2xl border border-slate-200/80 p-4 transition duration-150">
                    <summary class="flex justify-between items-center font-bold text-xs sm:text-sm text-slate-900 cursor-pointer list-none select-none">
                        <span>Qual è la differenza tra TAN e TAEG nel calcolo del mutuo?</span>
                        <svg class="w-4 h-4 text-slate-400 group-open:-rotate-180 transition-transform duration-200 shrink-0 ml-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/>
                        </svg>
                    </summary>
                    <div class="text-xs sm:text-sm text-slate-600 mt-2.5 leading-relaxed border-t border-slate-200/60 pt-2.5">
                        Il <strong>TAN</strong> (Tasso Annuo Nominale) misura il tasso di interesse puro applicato al prestito. Il <strong>TAEG</strong> (Tasso Annuo Effettivo Globale) è invece l'indicatore reale del costo complessivo del finanziamento: include obbligatoriamente per legge tutte le spese accessorie, tra cui imposta sostitutiva statale, spese di istruttoria, perizia dell'immobile, polizza assicurativa incendio e scoppio obbligatoria e spese di incasso rata. È il TAEG il valore da confrontare tra diverse banche.
                    </div>
                </details>

                <details class="group bg-slate-50/80 hover:bg-slate-50 rounded-2xl border border-slate-200/80 p-4 transition duration-150">
                    <summary class="flex justify-between items-center font-bold text-xs sm:text-sm text-slate-900 cursor-pointer list-none select-none">
                        <span>Conviene scegliere un mutuo a tasso fisso o a tasso variabile?</span>
                        <svg class="w-4 h-4 text-slate-400 group-open:-rotate-180 transition-transform duration-200 shrink-0 ml-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/>
                        </svg>
                    </summary>
                    <div class="text-xs sm:text-sm text-slate-600 mt-2.5 leading-relaxed border-t border-slate-200/60 pt-2.5">
                        Il <strong>tasso fisso</strong> (Eurirs + spread) blocca la rata per l'intera durata, offrendo certezza assoluta e protezione contro i rincari dell'inflazione e del costo del denaro. Il <strong>tasso variabile</strong> (Euribor + spread) varia periodicamente in base all'andamento dei mercati interbancari: può offrire condizioni di ingresso più convenienti o ribassi nei periodi di politica monetaria espansiva, ma espone al rischio di rialzi imprevedibili della rata mensile.
                    </div>
                </details>

                <details class="group bg-slate-50/80 hover:bg-slate-50 rounded-2xl border border-slate-200/80 p-4 transition duration-150">
                    <summary class="flex justify-between items-center font-bold text-xs sm:text-sm text-slate-900 cursor-pointer list-none select-none">
                        <span>L'estinzione anticipata o la surroga del mutuo comportano penali?</span>
                        <svg class="w-4 h-4 text-slate-400 group-open:-rotate-180 transition-transform duration-200 shrink-0 ml-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/>
                        </svg>
                    </summary>
                    <div class="text-xs sm:text-sm text-slate-600 mt-2.5 leading-relaxed border-t border-slate-200/60 pt-2.5">
                        <strong>No.</strong> In virtù della Legge Bersani (D.L. 7/2007, Legge 40/2007), per i mutui stipulati da persone fisiche per l'acquisto o ristrutturazione della prima casa è <em>vietata qualsiasi penale o costo di estinzione anticipata</em> (sia parziale che totale). Inoltre, con la portabilità o surroga gratuita, è possibile trasferire il debito residuo a un nuovo istituto di credito a costo zero (spese di atto notarile e perizia a carico della nuova banca subentrante).
                    </div>
                </details>
            </div>
        </section>

    </main>

    {render_unified_footer('mutuo')}

    <script>
        {render_suite_header_js()}
        {render_unified_footer_js()}

        // Universal Multi-Currency Handler
        const CURRENCIES = {{
            'EUR': {{ symbol: '€', code: 'EUR', pos: 'after', space: true }},
            'USD': {{ symbol: '$', code: 'USD', pos: 'before', space: false }},
            'GBP': {{ symbol: '£', code: 'GBP', pos: 'before', space: false }},
            'CHF': {{ symbol: 'CHF', code: 'CHF', pos: 'before', space: true }},
            'JPY': {{ symbol: '¥', code: 'JPY', pos: 'before', space: false }}
        }};

        let currentCurrency = 'EUR';

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
            document.querySelectorAll('.currencySymbol').forEach(el => el.textContent = sym);

            calculateMortgage();
        }}

        function formatMoney(val) {{
            const c = CURRENCIES[currentCurrency];
            const formatted = Math.round(val).toLocaleString('it-IT');
            if (c.pos === 'before') {{
                return c.symbol + (c.space ? ' ' : '') + formatted;
            }} else {{
                return formatted + (c.space ? ' ' : '') + c.symbol;
            }}
        }}

        function formatMoneyExact(val) {{
            const c = CURRENCIES[currentCurrency];
            const formatted = val.toLocaleString('it-IT', {{ minimumFractionDigits: 2, maximumFractionDigits: 2 }});
            if (c.pos === 'before') {{
                return c.symbol + (c.space ? ' ' : '') + formatted;
            }} else {{
                return formatted + (c.space ? ' ' : '') + c.symbol;
            }}
        }}

        function setAmount(v) {{
            document.getElementById('inputAmount').value = v;
            document.getElementById('rangeAmount').value = v;
            calculateMortgage();
        }}

        function setYears(v) {{
            document.getElementById('inputYears').value = v;
            document.getElementById('rangeYears').value = v;
            calculateMortgage();
        }}

        function setRate(v) {{
            document.getElementById('inputRate').value = v.toFixed(2);
            document.getElementById('rangeRate').value = v.toFixed(2);
            calculateMortgage();
        }}

        function resetDefaults() {{
            setAmount(180000);
            setYears(25);
            setRate(3.20);
            document.getElementById('inputIncome').value = 2600;
            calculateMortgage();
        }}

        function syncFromInput(type) {{
            const val = document.getElementById('input' + type).value;
            document.getElementById('range' + type).value = val;
            calculateMortgage();
        }}

        function syncFromRange(type) {{
            const val = document.getElementById('range' + type).value;
            document.getElementById('input' + type).value = val;
            calculateMortgage();
        }}

        function calculateMortgage() {{
            const principal = parseFloat(document.getElementById('inputAmount').value) || 0;
            const years = parseInt(document.getElementById('inputYears').value) || 1;
            const annualRatePercent = parseFloat(document.getElementById('inputRate').value) || 0;
            const monthlyIncome = parseFloat(document.getElementById('inputIncome').value) || 1;

            const n = years * 12; // Numero totale di rate mensili
            const monthlyRate = (annualRatePercent / 100) / 12; // Tasso mensile

            // Update Badges
            document.getElementById('badgeAmount').textContent = formatMoney(principal);
            document.getElementById('badgeYears').textContent = `${{years}} anni (${{n}} rate)`;
            document.getElementById('badgeRate').textContent = `${{annualRatePercent.toFixed(2)}} %`;
            document.getElementById('badgeIncome').textContent = formatMoney(monthlyIncome);

            // Formula Francese: Rata = C * [ r / (1 - (1+r)^-n) ]
            let monthlyPayment = 0;
            if (monthlyRate > 0) {{
                monthlyPayment = principal * (monthlyRate / (1 - Math.pow(1 + monthlyRate, -n)));
            }} else {{
                monthlyPayment = principal / n;
            }}

            const totalCost = monthlyPayment * n;
            const totalInterest = totalCost - principal;
            const interestRatio = principal > 0 ? (totalInterest / principal) * 100 : 0;
            const debtToIncomeRatio = monthlyIncome > 0 ? (monthlyPayment / monthlyIncome) * 100 : 0;

            // Aggiorna KPI Numerici
            document.getElementById('resMonthlyPayment').textContent = formatMoneyExact(monthlyPayment);
            document.getElementById('resTotalInstallments').textContent = n;
            document.getElementById('resPrincipal').textContent = formatMoney(principal);
            document.getElementById('resTotalInterest').textContent = formatMoney(totalInterest);
            document.getElementById('resInterestRatio').textContent = `+${{interestRatio.toFixed(1)}}% sul capitale`;
            document.getElementById('resTotalCost').textContent = formatMoney(totalCost);

            // Sostenibilità Rata/Reddito
            const dtiEl = document.getElementById('resDebtToIncome');
            const dtiTag = document.getElementById('resDebtToIncomeTag');
            const affordTag = document.getElementById('affordTag');
            const affordDesc = document.getElementById('affordDesc');

            dtiEl.textContent = `${{debtToIncomeRatio.toFixed(1)}}%`;

            if (debtToIncomeRatio <= 33.3) {{
                dtiTag.textContent = 'Ottimale (≤ 33%)';
                dtiTag.className = 'text-[10px] font-semibold text-emerald-100';
                affordTag.className = 'text-[10px] font-extrabold uppercase px-2 py-0.5 bg-emerald-100 text-emerald-800 rounded border border-emerald-300';
                affordTag.textContent = 'Fattibile (Sotto il 33%)';
                affordDesc.textContent = `La rata assorbe il ${{debtToIncomeRatio.toFixed(1)}}% del reddito netto mensile. È ampiamente entro la soglia standard del 33% raccomandata dal sistema bancario.`;
            }} else if (debtToIncomeRatio <= 40) {{
                dtiTag.textContent = 'Al Limite (33-40%)';
                dtiTag.className = 'text-[10px] font-semibold text-amber-200';
                affordTag.className = 'text-[10px] font-extrabold uppercase px-2 py-0.5 bg-amber-100 text-amber-800 rounded border border-amber-300';
                affordTag.textContent = 'Attenzione (33% - 40%)';
                affordDesc.textContent = `La rata assorbe il ${{debtToIncomeRatio.toFixed(1)}}% del reddito. Alcune banche potrebbero richiedere garanzie aggiuntive, un co-intestatario o un garante.`;
            }} else {{
                dtiTag.textContent = 'Critico (> 40%)';
                dtiTag.className = 'text-[10px] font-semibold text-rose-200';
                affordTag.className = 'text-[10px] font-extrabold uppercase px-2 py-0.5 bg-rose-100 text-rose-800 rounded border border-rose-300';
                affordTag.textContent = 'Rischio Diniego (> 40%)';
                affordDesc.textContent = `Rapporto rata/reddito troppo elevato (${{debtToIncomeRatio.toFixed(1)}}%). Consigliato allungare la durata del mutuo o ridurre il capitale richiesto per evitare il diniego bancario.`;
            }}

            // Popola Tabella Ammortamento & SVG
            renderYearlyTableAndSvg(principal, monthlyRate, monthlyPayment, years);
        }}

        function renderYearlyTableAndSvg(principal, r, payment, years) {{
            let balance = principal;
            let tableHtml = '';
            let yearData = [];

            for (let y = 1; y <= years; y++) {{
                let yearInterest = 0;
                let yearPrincipal = 0;

                for (let m = 1; m <= 12; m++) {{
                    let interest = balance * r;
                    let principalPart = payment - interest;
                    if (principalPart > balance) principalPart = balance;
                    balance -= principalPart;
                    yearInterest += interest;
                    yearPrincipal += principalPart;
                }}

                yearData.push({{
                    year: y,
                    principalPart: yearPrincipal,
                    interestPart: yearInterest,
                    remaining: Math.max(0, balance)
                }});

                tableHtml += `
                    <tr class="hover:bg-slate-50/80">
                        <td class="p-2 font-bold">${{y}}° Anno</td>
                        <td class="p-2 text-right text-emerald-700">${{formatMoney(yearPrincipal)}}</td>
                        <td class="p-2 text-right text-rose-600">${{formatMoney(yearInterest)}}</td>
                        <td class="p-2 text-right font-bold">${{formatMoney(balance)}}</td>
                    </tr>
                `;
            }}

            document.getElementById('tableBody').innerHTML = tableHtml;

            // Render SVG Stacked Bar Chart
            const svg = document.getElementById('mortgageSvg');
            const W = 520;
            const H = 200;
            const padL = 30;
            const padR = 20;
            const padB = 30;
            const padT = 20;

            const usableW = W - padL - padR;
            const usableH = H - padB - padT;
            const barW = Math.max(4, (usableW / years) - 3);

            let svgContent = `
                <!-- Background Grid Lines -->
                <line x1="${{padL}}" y1="${{padT}}" x2="${{W - padR}}" y2="${{padT}}" stroke="#334155" stroke-width="1" stroke-dasharray="2 2" />
                <line x1="${{padL}}" y1="${{padT + usableH / 2}}" x2="${{W - padR}}" y2="${{padT + usableH / 2}}" stroke="#334155" stroke-width="1" stroke-dasharray="2 2" />
                <line x1="${{padL}}" y1="${{H - padB}}" x2="${{W - padR}}" y2="${{H - padB}}" stroke="#64748b" stroke-width="1.5" />
            `;

            yearData.forEach((d, idx) => {{
                let x = padL + (idx * (usableW / years)) + 1;
                let totalH = usableH;
                let intRatio = d.interestPart / (d.principalPart + d.interestPart);
                let intH = totalH * intRatio;
                let princH = totalH - intH;

                let intY = (H - padB) - totalH;
                let princY = intY + intH;

                svgContent += `
                    <!-- Interest Bar (Top - Red) -->
                    <rect x="${{x}}" y="${{intY}}" width="${{barW}}" height="${{intH}}" fill="#f43f5e" rx="1" />
                    <!-- Principal Bar (Bottom - Green) -->
                    <rect x="${{x}}" y="${{princY}}" width="${{barW}}" height="${{princH}}" fill="#059669" rx="1" />
                `;

                // X Axis Labels (ogni 5 anni)
                if (d.year === 1 || d.year % 5 === 0 || d.year === years) {{
                    svgContent += `
                        <text x="${{x + (barW/2)}}" y="${{H - padB + 14}}" fill="#94a3b8" font-size="9" font-family="monospace" text-anchor="middle">${{d.year}}a</text>
                    `;
                }}
            }});

            svgContent += `
                <text x="${{padL}}" y="${{padT - 6}}" fill="#94a3b8" font-size="9" font-family="monospace">Rata Annuale Costante (Interessi in calo / Capitale in crescita)</text>
            `;

            svg.innerHTML = svgContent;

            updateUrlParams();
        }}

        // Print date
        const pDate = document.getElementById('printDate');
        if (pDate) pDate.textContent = new Date().toLocaleDateString('it-IT');

        // Initial Run
        initFromUrl();
        calculateMortgage();

        function updateUrlParams() {{
            try {{
                const params = new URLSearchParams();
                if (currentCurrency !== 'EUR') params.set('curr', currentCurrency);
                const amount = document.getElementById('inputAmount').value;
                if (amount && amount !== '180000') params.set('loan', amount);
                const years = document.getElementById('inputYears').value;
                if (years && years !== '25') params.set('years', years);
                const rate = document.getElementById('inputRate').value;
                if (rate && rate !== '3.20') params.set('rate', rate);
                const income = document.getElementById('inputIncome').value;
                if (income && income !== '2600') params.set('income', income);

                const query = params.toString();
                const newUrl = query ? (window.location.pathname + '?' + query) : window.location.pathname;
                window.history.replaceState({{}}, '', newUrl);
            }} catch(e) {{}}
        }}

        function initFromUrl() {{
            try {{
                const params = new URLSearchParams(window.location.search);
                if (params.has('curr')) setCurrency(params.get('curr'));
                if (params.has('loan')) setAmount(parseFloat(params.get('loan')));
                if (params.has('years')) setYears(parseInt(params.get('years')));
                if (params.has('rate')) setRate(parseFloat(params.get('rate')));
                if (params.has('income')) {{
                    document.getElementById('inputIncome').value = params.get('income');
                }}
            }} catch(e) {{}}
        }}

        function copyShareLink() {{
            updateUrlParams();
            const url = window.location.href;
            if (navigator.clipboard && navigator.clipboard.writeText) {{
                navigator.clipboard.writeText(url).then(() => {{
                    showCopiedFeedback();
                }}).catch(() => {{
                    fallbackCopy(url);
                }});
            }} else {{
                fallbackCopy(url);
            }}
        }}

        function showCopiedFeedback() {{
            const btnText = document.getElementById('btnShareText');
            if (btnText) {{
                const orig = btnText.textContent;
                btnText.textContent = 'Copiato!';
                setTimeout(() => {{ btnText.textContent = orig; }}, 2000);
            }}
        }}

        function fallbackCopy(text) {{
            prompt('Copia questo link con il tuo preventivo mutuo:', text);
        }}
    </script>
</body>
</html>
"""

out_path = os.path.join(current_dir, 'mutuo.html')
with open(out_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"mutuo.html successfully built with FAQ at: {out_path}")
