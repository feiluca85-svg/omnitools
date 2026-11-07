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
    <title>InteresseComposto — Simulatore PAC & Rendita Passiva 4% | OmniTools Lab</title>
    <meta name="description" content="Simula l'interesse composto nel tempo con versamenti mensili (PAC). Calcola il montante finale, gli interessi reinvestiti e la rendita passiva mensile sostenibile (Regola del 4%).">
    
    <!-- Canonical & SEO -->
    <link rel="canonical" href="https://www.omnitoolslab.com/pac">
    <meta name="robots" content="index, follow">
    <meta property="og:type" content="website">
    <meta property="og:title" content="InteresseComposto — Simulatore PAC & Rendita Passiva | OmniTools Lab">
    <meta property="og:description" content="Calcola la crescita esponenziale del tuo capitale con versamenti periodici e la regola del 4% per la rendita da investimento.">
    <meta property="og:url" content="https://www.omnitoolslab.com/pac">
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
      "name": "InteresseComposto",
      "url": "https://www.omnitoolslab.com/pac",
      "applicationCategory": "FinanceApplication",
      "operatingSystem": "All",
      "description": "Simulatore di interesse composto, piano di accumulo del capitale (PAC) e calcolo rendita passiva al 4%.",
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
          "name": "Cos'è l'interesse composto e come funziona l'effetto valanga?",
          "acceptedAnswer": {{
            "@type": "Answer",
            "text": "L'interesse composto è il processo per cui gli interessi maturati su un capitale vengono reinvestiti, iniziando a generare a loro volta nuovi interessi nei periodi successivi. Nel lungo periodo questo meccanismo trasforma la crescita da lineare a esponenziale (effetto valanga)."
          }}
        }},
        {{
          "@type": "Question",
          "name": "Qual è il vantaggio di un PAC (Piano di Accumulo del Capitale) rispetto a un versamento unico?",
          "acceptedAnswer": {{
            "@type": "Answer",
            "text": "Il PAC si basa sulla strategia del Dollar Cost Averaging (DCA): investendo una somma costante a intervalli regolari (es. ogni mese), si acquistano più quote quando i mercati scendono e meno quote quando salgono, mediando il prezzo di carico ed eliminando lo stress del timing di mercato."
          }}
        }},
        {{
          "@type": "Question",
          "name": "Cos'è la regola del 4% (Trinity Study) per la rendita da capitale?",
          "acceptedAnswer": {{
            "@type": "Answer",
            "text": "La regola del 4% deriva dallo studio accademico dell'Università Trinity (Texas). Dimostra che, con un portafoglio bilanciato tra azioni e obbligazioni, è storicamente possibile prelevare il 4% del capitale il primo anno (adeguandolo poi all'inflazione) con una probabilità superiore al 95% di preservare il capitale per oltre 30 anni."
          }}
        }},
        {{
          "@type": "Question",
          "name": "Come vengono tassate le plusvalenze e i rendimenti finanziari in Italia?",
          "acceptedAnswer": {{
            "@type": "Answer",
            "text": "In Italia le plusvalenze derivanti da ETF azionari, azioni e fondi sono soggette all'imposta sostitutiva del 26%. Per i titoli di Stato italiani o della white list l'aliquota agevolata è del 12,5%. Inoltre sui dossier titoli grava l'imposta di bollo proporzionale dello 0,20% annuo."
          }}
        }},
        {{
          "@type": "Question",
          "name": "Quanto tempo occorre affinché l'interesse composto mostri la sua vera forza?",
          "acceptedAnswer": {{
            "@type": "Answer",
            "text": "L'effetto esponenziale dell'interesse composto richiede tempo: nei primi 5-7 anni la crescita è dominata dai versamenti effettivi effettuati. Dopo i 10-15 anni, la quota degli interessi reinvestiti supera i versamenti annuali, accelerando vertiginosamente la crescita del patrimonio."
          }}
        }}
      ]
    }}
    </script>
</head>
<body class="bg-slate-50 text-slate-800 min-h-screen flex flex-col justify-between">

    {render_suite_header('pac')}

    <main class="max-w-5xl mx-auto px-3 sm:px-6 py-2.5 sm:py-5 flex-1 w-full space-y-3 sm:space-y-5">

        <!-- Print-only official header -->
        <div class="print-only mb-6 border-b-2 border-slate-900 pb-3">
            <div class="flex justify-between items-center">
                <div>
                    <h1 class="text-xl font-black text-slate-900 uppercase tracking-wide">OmniTools Lab · InteresseComposto</h1>
                    <p class="text-xs text-slate-600">Prospetto Finanziario di Crescita PAC & Rendita Passiva da Capitale</p>
                </div>
                <div class="text-right text-xs text-slate-500 font-mono">
                    <p>Data Stampa: <span id="printDate"></span></p>
                    <p>omnitoolslab.com/pac</p>
                </div>
            </div>
        </div>

        <!-- Hero Title & Global Currency Bar -->
        <div class="flex flex-col md:flex-row items-center justify-between gap-4 no-print pb-2 border-b border-slate-200">
            <div class="text-left space-y-1">
                <div class="flex items-center gap-2">
                    <span class="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded-full bg-emerald-100 text-emerald-800 text-[11px] font-extrabold border border-emerald-200">
                        <span>📈</span> SIMULATORE RISPARMIO & PIANO ACCUMULO (PAC)
                    </span>
                    <span class="text-xs font-bold text-slate-400">· Crescita Esponenziale & FIRE</span>
                </div>
                <h1 class="text-xl sm:text-2xl font-black text-slate-900 tracking-tight">Calcolo Interesse Composto & Montante Futuro</h1>
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
                    <span class="flex items-center gap-1.5"><span>⚙️</span> Parametri del Piano di Accumulo</span>
                    <div class="flex items-center gap-2">
                        <button type="button" onclick="copyShareLink()" id="btnShare" title="Copia link con i parametri attuali" class="text-[11px] font-bold text-emerald-800 bg-emerald-50 hover:bg-emerald-100 px-2 py-0.5 rounded-lg border border-emerald-200 transition flex items-center gap-1 cursor-pointer">
                            <span>🔗</span> <span id="btnShareText">Condividi</span>
                        </button>
                        <button type="button" onclick="resetDefaults()" class="text-[11px] font-semibold text-slate-500 hover:text-slate-800">Reimposta</button>
                    </div>
                </span>

                <!-- Capitale Iniziale -->
                <div>
                    <div class="flex justify-between items-center mb-1">
                        <label class="text-xs font-bold text-slate-700">Capitale Iniziale (<span class="currencySymbol">€</span>)</label>
                        <span id="badgeInitial" class="text-xs font-bold font-mono text-emerald-700 bg-emerald-50 px-2 py-0.5 rounded border border-emerald-200">5.000 €</span>
                    </div>
                    <input type="number" id="inputInitial" value="5000" min="0" max="10000000" step="500" oninput="syncFromInput('Initial')" class="w-full p-2.5 bg-slate-50 border border-slate-200 rounded-xl font-bold font-mono text-base text-slate-900 focus:outline-none focus:ring-2 focus:ring-emerald-500">
                    <input type="range" id="rangeInitial" min="0" max="50000" step="500" value="5000" oninput="syncFromRange('Initial')" class="w-full mt-2 accent-emerald-600 cursor-pointer">
                    <div class="grid grid-cols-4 gap-1 mt-1 text-[10px] font-bold no-print">
                        <button type="button" onclick="setInitial(0)" class="py-1 bg-slate-100 hover:bg-slate-200 rounded-lg text-slate-700 transition">0</button>
                        <button type="button" onclick="setInitial(2000)" class="py-1 bg-slate-100 hover:bg-slate-200 rounded-lg text-slate-700 transition">2.000</button>
                        <button type="button" onclick="setInitial(5000)" class="py-1 bg-slate-100 hover:bg-slate-200 rounded-lg text-slate-700 transition">5.000</button>
                        <button type="button" onclick="setInitial(10000)" class="py-1 bg-slate-100 hover:bg-slate-200 rounded-lg text-slate-700 transition">10.000</button>
                    </div>
                </div>

                <!-- Versamento Mensile (PAC) -->
                <div>
                    <div class="flex justify-between items-center mb-1">
                        <label class="text-xs font-bold text-slate-700">Versamento Ricorrente Mensile (<span class="currencySymbol">€</span>)</label>
                        <span id="badgeMonthly" class="text-xs font-bold font-mono text-emerald-700 bg-emerald-50 px-2 py-0.5 rounded border border-emerald-200">250 € / mese</span>
                    </div>
                    <input type="number" id="inputMonthly" value="250" min="0" max="100000" step="50" oninput="syncFromInput('Monthly')" class="w-full p-2.5 bg-slate-50 border border-slate-200 rounded-xl font-bold font-mono text-base text-slate-900 focus:outline-none focus:ring-2 focus:ring-emerald-500">
                    <input type="range" id="rangeMonthly" min="0" max="2500" step="50" value="250" oninput="syncFromRange('Monthly')" class="w-full mt-2 accent-emerald-600 cursor-pointer">
                    <div class="grid grid-cols-4 gap-1 mt-1 text-[10px] font-bold no-print">
                        <button type="button" onclick="setMonthly(100)" class="py-1 bg-slate-100 hover:bg-slate-200 rounded-lg text-slate-700 transition">100</button>
                        <button type="button" onclick="setMonthly(250)" class="py-1 bg-slate-100 hover:bg-slate-200 rounded-lg text-slate-700 transition">250</button>
                        <button type="button" onclick="setMonthly(500)" class="py-1 bg-slate-100 hover:bg-slate-200 rounded-lg text-slate-700 transition">500</button>
                        <button type="button" onclick="setMonthly(1000)" class="py-1 bg-slate-100 hover:bg-slate-200 rounded-lg text-slate-700 transition">1.000</button>
                    </div>
                </div>

                <!-- Orizzonte Temporale Anni -->
                <div>
                    <div class="flex justify-between items-center mb-1">
                        <label class="text-xs font-bold text-slate-700">Orizzonte Temporale (Anni)</label>
                        <span id="badgeYears" class="text-xs font-bold font-mono text-slate-800 bg-slate-100 px-2 py-0.5 rounded border border-slate-200">20 anni</span>
                    </div>
                    <input type="number" id="inputYears" value="20" min="1" max="50" step="1" oninput="syncFromInput('Years')" class="w-full p-2.5 bg-slate-50 border border-slate-200 rounded-xl font-bold font-mono text-base text-slate-900 focus:outline-none focus:ring-2 focus:ring-emerald-500">
                    <input type="range" id="rangeYears" min="1" max="40" step="1" value="20" oninput="syncFromRange('Years')" class="w-full mt-2 accent-emerald-600 cursor-pointer">
                    <div class="grid grid-cols-4 gap-1 mt-1 text-[10px] font-bold no-print">
                        <button type="button" onclick="setYears(10)" class="py-1 bg-slate-100 hover:bg-slate-200 rounded-lg text-slate-700 transition">10a</button>
                        <button type="button" onclick="setYears(15)" class="py-1 bg-slate-100 hover:bg-slate-200 rounded-lg text-slate-700 transition">15a</button>
                        <button type="button" onclick="setYears(20)" class="py-1 bg-slate-100 hover:bg-slate-200 rounded-lg text-slate-700 transition">20a</button>
                        <button type="button" onclick="setYears(30)" class="py-1 bg-slate-100 hover:bg-slate-200 rounded-lg text-slate-700 transition">30a</button>
                    </div>
                </div>

                <!-- Rendimento Medio Annuo Stimato % -->
                <div>
                    <div class="flex justify-between items-center mb-1">
                        <label class="text-xs font-bold text-slate-700">Rendimento Medio Annuo Stimato (%)</label>
                        <span id="badgeReturn" class="text-xs font-bold font-mono text-emerald-700 bg-emerald-50 px-2 py-0.5 rounded border border-emerald-200">7.00 %</span>
                    </div>
                    <input type="number" id="inputReturn" value="7.00" min="0.1" max="25.0" step="0.25" oninput="syncFromInput('Return')" class="w-full p-2.5 bg-slate-50 border border-slate-200 rounded-xl font-bold font-mono text-base text-slate-900 focus:outline-none focus:ring-2 focus:ring-emerald-500">
                    <input type="range" id="rangeReturn" min="1.0" max="15.0" step="0.25" value="7.00" oninput="syncFromRange('Return')" class="w-full mt-2 accent-emerald-600 cursor-pointer">
                    <div class="grid grid-cols-4 gap-1 mt-1 text-[10px] font-bold no-print">
                        <button type="button" onclick="setReturn(4.0)" class="py-1 bg-slate-100 hover:bg-slate-200 rounded-lg text-slate-700 transition">4% (Prud.)</button>
                        <button type="button" onclick="setReturn(6.0)" class="py-1 bg-slate-100 hover:bg-slate-200 rounded-lg text-slate-700 transition">6% (Bil.)</button>
                        <button type="button" onclick="setReturn(8.0)" class="py-1 bg-slate-100 hover:bg-slate-200 rounded-lg text-slate-700 transition">8% (Azion.)</button>
                        <button type="button" onclick="setReturn(10.0)" class="py-1 bg-slate-100 hover:bg-slate-200 rounded-lg text-slate-700 transition">10% (S&P)</button>
                    </div>
                </div>
            </div>

            <!-- Results & Visualization Column (7 cols) -->
            <div class="lg:col-span-7 space-y-4">

                <!-- Primary KPI: Montante Finale Stimato -->
                <div class="bg-gradient-to-br from-emerald-600 via-teal-700 to-slate-900 rounded-2xl p-5 text-white shadow-md relative overflow-hidden card-box">
                    <div class="relative z-10 flex flex-col sm:flex-row sm:items-center justify-between gap-4">
                        <div>
                            <span class="text-[11px] font-extrabold uppercase tracking-wider text-emerald-200 block">Capitale Finale Accumulato</span>
                            <div class="text-3xl sm:text-4xl font-black font-mono tracking-tight text-white mt-1" id="resFinalAmount">
                                151.785 €
                            </div>
                            <span class="text-xs text-emerald-100/90 mt-0.5 block" id="resGrowthMultiplier">2.3x il capitale versato</span>
                        </div>
                        <div class="bg-white/10 backdrop-blur-xs p-3 rounded-xl border border-white/20 text-right sm:text-right shrink-0">
                            <span class="text-[10px] uppercase font-bold text-emerald-200 block">Rendita Perpetua (Regola 4%)</span>
                            <div class="text-xl font-black font-mono text-white mt-0.5" id="resPassiveIncome">506 € / mese</div>
                            <span class="text-[10px] font-semibold text-emerald-100">Prelievo sicuro annuo</span>
                        </div>
                    </div>
                </div>

                <!-- Secondary Metrics Grid -->
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
                    <div class="bg-white rounded-xl p-3.5 border border-slate-200 shadow-2xs card-box">
                        <span class="text-[11px] font-bold text-slate-500 uppercase tracking-wider block">Capitale Versato da Te</span>
                        <div class="text-lg font-black font-mono text-slate-900 mt-1" id="resTotalDeposits">65.000 €</div>
                        <span class="text-[10px] text-slate-500" id="resInitialVsPac">5k iniziale + 60k versamenti</span>
                    </div>

                    <div class="bg-white rounded-xl p-3.5 border border-slate-200 shadow-2xs card-box">
                        <span class="text-[11px] font-bold text-emerald-700 uppercase tracking-wider block">Interessi Guadagnati (Compound)</span>
                        <div class="text-lg font-black font-mono text-emerald-700 mt-1" id="resTotalGains">+86.785 €</div>
                        <span class="text-[10px] text-slate-500" id="resGainsShare">57.2% del patrimonio finale</span>
                    </div>
                </div>

                <!-- SVG Exponential Growth Curve Chart -->
                <div class="bg-slate-900 text-white rounded-2xl p-4 shadow-sm space-y-3 card-box">
                    <div class="flex items-center justify-between text-xs">
                        <span class="font-bold flex items-center gap-1.5">
                            <span>📈</span> Curva di Crescita (Capitale Versato vs Interesse Composto)
                        </span>
                        <div class="flex items-center gap-3 text-[10px] font-mono">
                            <span class="flex items-center gap-1"><span class="w-2.5 h-2.5 bg-slate-400 rounded-xs"></span> Versamenti</span>
                            <span class="flex items-center gap-1"><span class="w-2.5 h-2.5 bg-emerald-500 rounded-xs"></span> Montante Totale</span>
                        </div>
                    </div>

                    <div class="w-full overflow-hidden">
                        <svg id="compoundSvg" class="w-full h-44" viewBox="0 0 520 200" preserveAspectRatio="none"></svg>
                    </div>
                    <p class="text-[10px] text-slate-400 text-center font-mono">
                        L'area verde rappresenta la ricchezza creata esclusivamente dagli interessi reinvestiti che generano a loro volta nuovi interessi (effetto valanga).
                    </p>
                </div>

                <!-- Yearly Breakdown Table -->
                <div class="bg-white rounded-2xl border border-slate-200 shadow-2xs overflow-hidden card-box">
                    <div class="p-3.5 bg-slate-100/80 border-b border-slate-200 flex items-center justify-between">
                        <span class="text-xs font-bold text-slate-800 flex items-center gap-1.5">
                            <span>📅</span> Tabella di Crescita Annuale
                        </span>
                        <span class="text-[10px] font-mono text-slate-500">Versato Cumulativo / Interessi Annuali / Valore Portafoglio</span>
                    </div>
                    <div class="max-h-56 overflow-y-auto">
                        <table class="w-full text-xs text-left">
                            <thead class="bg-slate-50 text-[10px] font-bold text-slate-500 uppercase sticky top-0 border-b border-slate-200">
                                <tr>
                                    <th class="p-2">Anno</th>
                                    <th class="p-2 text-right">Versato</th>
                                    <th class="p-2 text-right">Interessi Anno</th>
                                    <th class="p-2 text-right">Patrimonio</th>
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
        <div class="p-4 bg-slate-100 rounded-2xl border border-slate-200 text-[11px] leading-relaxed text-slate-600 space-y-1.5">
            <div class="flex items-center gap-1.5 font-bold text-slate-800">
                <span>⚖️</span>
                <span>Nota Tecnica & Disclaimer Legale (OmniFinance):</span>
            </div>
            <p>
                La formula utilizzata per il montante futuro con versamenti mensili costanti a capitalizzazione composta è:
                <span class="font-mono bg-white px-1.5 py-0.5 rounded border border-slate-200">M = C × (1 + r)^n + PMT × [((1 + r)^n - 1) / r]</span>.
            </p>
            <p>
                I risultati visualizzati sono puramente teorici, didattici ed estimativi. <strong>Non costituiscono in alcun modo consulenza finanziaria, raccomandazione d'investimento personalizzata o offerta di servizi finanziari</strong> ai sensi del D.Lgs. 58/1998 (TUF) e del regolamento intermediari Consob. I rendimenti passati dei mercati finanziari non sono garanzia di rendimenti futuri. Il simulatore assume un rendimento costante annuo non volatile; nella realtà i mercati azionari e obbligazionari subiscono fluttuazioni, drawdown e perdite di capitale. La simulazione non tiene conto di imposte sulle plusvalenze (capital gain al 26% o 12,5% sui titoli di stato), imposta di bollo sul dossier titoli (0,20% annuo), costi di gestione degli strumenti (TER/ETF) o impatto dell'inflazione sul potere d'acquisto reale.
            </p>
        </div>

        <!-- FAQ Section (Frequenty Asked Questions) -->
        <section class="mt-8 bg-white rounded-3xl p-6 sm:p-8 border border-slate-200 shadow-2xs space-y-6">
            <div class="space-y-1">
                <span class="text-xs font-black uppercase tracking-wider text-emerald-800">Guida & Domande Frequenti</span>
                <h2 class="text-lg sm:text-xl font-black text-slate-900 tracking-tight">Tutto quello che devi sapere su Interesse Composto e PAC</h2>
            </div>

            <div class="space-y-3">
                <details class="group bg-slate-50/80 hover:bg-slate-50 rounded-2xl border border-slate-200/80 p-4 transition duration-150" open>
                    <summary class="flex justify-between items-center font-bold text-xs sm:text-sm text-slate-900 cursor-pointer list-none select-none">
                        <span>Cos'è l'interesse composto e come funziona l'effetto valanga?</span>
                        <svg class="w-4 h-4 text-slate-400 group-open:-rotate-180 transition-transform duration-200 shrink-0 ml-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/>
                        </svg>
                    </summary>
                    <div class="text-xs sm:text-sm text-slate-600 mt-2.5 leading-relaxed border-t border-slate-200/60 pt-2.5">
                        A differenza dell'interesse semplice (in cui il rendimento viene calcolato unicamente sulla quota originaria depositata), con l'<strong>interesse composto</strong> i guadagni generati da ciascun periodo vengono automaticamente ri-sommati al capitale iniziale. Nei periodi successivi, tali interessi producono a loro volta altri interessi: si innesca così il cosiddetto <em>effetto valanga esponenziale</em>, descritto da Albert Einstein come la "forza più potente dell'universo".
                    </div>
                </details>

                <details class="group bg-slate-50/80 hover:bg-slate-50 rounded-2xl border border-slate-200/80 p-4 transition duration-150">
                    <summary class="flex justify-between items-center font-bold text-xs sm:text-sm text-slate-900 cursor-pointer list-none select-none">
                        <span>Qual è il vantaggio di un PAC (Piano di Accumulo) rispetto al versamento unico (PIC)?</span>
                        <svg class="w-4 h-4 text-slate-400 group-open:-rotate-180 transition-transform duration-200 shrink-0 ml-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/>
                        </svg>
                    </summary>
                    <div class="text-xs sm:text-sm text-slate-600 mt-2.5 leading-relaxed border-t border-slate-200/60 pt-2.5">
                        Il PAC sfrutta la celebre metodologia del <strong>Dollar-Cost Averaging (DCA)</strong>. Investire una somma fissa e costante ogni mese abbatte il rischio di <em>market timing</em> (ovvero la paura di investire al picco massimo di mercato): quando i corsi azionari calano, la rata mensile compra un numero maggiore di quote a sconto; quando salgono compra meno quote, mediando efficacemente il prezzo medio di carico nel tempo con disciplina psicologica.
                    </div>
                </details>

                <details class="group bg-slate-50/80 hover:bg-slate-50 rounded-2xl border border-slate-200/80 p-4 transition duration-150">
                    <summary class="flex justify-between items-center font-bold text-xs sm:text-sm text-slate-900 cursor-pointer list-none select-none">
                        <span>Cos'è la regola del 4% (Trinity Study) per la rendita da capitale?</span>
                        <svg class="w-4 h-4 text-slate-400 group-open:-rotate-180 transition-transform duration-200 shrink-0 ml-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/>
                        </svg>
                    </summary>
                    <div class="text-xs sm:text-sm text-slate-600 mt-2.5 leading-relaxed border-t border-slate-200/60 pt-2.5">
                        La <strong>Regola del 4%</strong> (Safe Withdrawal Rate - SWR) è il pilastro del movimento FIRE (Financial Independence, Retire Early), derivata da un rigoroso studio scientifico condotto dall'Università Trinity (Texas). Dimostra che, con un portafoglio diversificato tra azioni globali e obbligazioni, prelevando il 4% del capitale accumulato durante il primo anno di pensione anticipata (e adeguando il prelievo all'inflazione gli anni successivi), il capitale ha una probabilità superiore al <strong>95% di non estinguersi</strong> nell'arco di un orizzonte trentennale.
                    </div>
                </details>

                <details class="group bg-slate-50/80 hover:bg-slate-50 rounded-2xl border border-slate-200/80 p-4 transition duration-150">
                    <summary class="flex justify-between items-center font-bold text-xs sm:text-sm text-slate-900 cursor-pointer list-none select-none">
                        <span>Come vengono tassate le plusvalenze e i rendimenti finanziari in Italia?</span>
                        <svg class="w-4 h-4 text-slate-400 group-open:-rotate-180 transition-transform duration-200 shrink-0 ml-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/>
                        </svg>
                    </summary>
                    <div class="text-xs sm:text-sm text-slate-600 mt-2.5 leading-relaxed border-t border-slate-200/60 pt-2.5">
                        In Italia il capital gain (plusvalenza da vendita di azioni, ETF o dividendi) è assoggettato a un'imposta sostitutiva ordinaria del <strong>26%</strong>. Fanno eccezione i Titoli di Stato italiani e i titoli sovranazionali inseriti nella "White List", che godono dell'aliquota agevolata del <strong>12,50%</strong>. Inoltre, su base annua, grava sui patrimoni investiti l'imposta di bollo proporzionale dello <strong>0,20%</strong> sul controvalore del dossier titoli (art. 19 D.L. 201/2011).
                    </div>
                </details>

                <details class="group bg-slate-50/80 hover:bg-slate-50 rounded-2xl border border-slate-200/80 p-4 transition duration-150">
                    <summary class="flex justify-between items-center font-bold text-xs sm:text-sm text-slate-900 cursor-pointer list-none select-none">
                        <span>Quanto tempo occorre affinché l'interesse composto mostri la sua vera forza?</span>
                        <svg class="w-4 h-4 text-slate-400 group-open:-rotate-180 transition-transform duration-200 shrink-0 ml-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/>
                        </svg>
                    </summary>
                    <div class="text-xs sm:text-sm text-slate-600 mt-2.5 leading-relaxed border-t border-slate-200/60 pt-2.5">
                        La variabile fondamentale dell'equazione dell'interesse composto è l'<strong>esponente tempo</strong> (gli anni di investimento). Nei primi 5-8 anni, oltre l'80% del valore del conto è costituito semplicemente dai risparmi versati di tasca propria. Tra il decimo e il ventesimo anno si verifica il sorpasso: i guadagni generati dagli interessi reinvestiti superano il valore totale dei versamenti mensili, provocando una vera e propria impennata parabolica del conto.
                    </div>
                </details>
            </div>
        </section>

    </main>

    {render_unified_footer('pac')}

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

            calculateCompound();
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

        function setInitial(v) {{
            document.getElementById('inputInitial').value = v;
            document.getElementById('rangeInitial').value = v;
            calculateCompound();
        }}

        function setMonthly(v) {{
            document.getElementById('inputMonthly').value = v;
            document.getElementById('rangeMonthly').value = v;
            calculateCompound();
        }}

        function setYears(v) {{
            document.getElementById('inputYears').value = v;
            document.getElementById('rangeYears').value = v;
            calculateCompound();
        }}

        function setReturn(v) {{
            document.getElementById('inputReturn').value = v.toFixed(2);
            document.getElementById('rangeReturn').value = v.toFixed(2);
            calculateCompound();
        }}

        function resetDefaults() {{
            setInitial(5000);
            setMonthly(250);
            setYears(20);
            setReturn(7.00);
            calculateCompound();
        }}

        function syncFromInput(type) {{
            const val = document.getElementById('input' + type).value;
            document.getElementById('range' + type).value = val;
            calculateCompound();
        }}

        function syncFromRange(type) {{
            const val = document.getElementById('range' + type).value;
            document.getElementById('input' + type).value = val;
            calculateCompound();
        }}

        function calculateCompound() {{
            const initial = parseFloat(document.getElementById('inputInitial').value) || 0;
            const monthly = parseFloat(document.getElementById('inputMonthly').value) || 0;
            const years = parseInt(document.getElementById('inputYears').value) || 1;
            const annualReturnPercent = parseFloat(document.getElementById('inputReturn').value) || 0;

            const rMonthly = Math.pow(1 + (annualReturnPercent / 100), 1 / 12) - 1; // Tasso equivalente mensile composto

            // Update Badges
            document.getElementById('badgeInitial').textContent = formatMoney(initial);
            document.getElementById('badgeMonthly').textContent = formatMoney(monthly) + ' / mese';
            document.getElementById('badgeYears').textContent = `${{years}} anni`;
            document.getElementById('badgeReturn').textContent = `${{annualReturnPercent.toFixed(2)}} %`;

            let currentTotal = initial;
            let currentDeposited = initial;
            let tableData = [];

            for (let y = 1; y <= years; y++) {{
                let startYearTotal = currentTotal;
                for (let m = 1; m <= 12; m++) {{
                    currentTotal = (currentTotal + monthly) * (1 + rMonthly);
                    currentDeposited += monthly;
                }}
                let yearInterest = currentTotal - startYearTotal - (monthly * 12);

                tableData.push({{
                    year: y,
                    deposited: currentDeposited,
                    interest: Math.max(0, yearInterest),
                    total: currentTotal
                }});
            }}

            const finalAmount = currentTotal;
            const totalDeposited = currentDeposited;
            const gains = finalAmount - totalDeposited;
            const multiplier = totalDeposited > 0 ? (finalAmount / totalDeposited) : 1;
            const gainsShare = finalAmount > 0 ? (gains / finalAmount) * 100 : 0;
            const monthlyPassive = (finalAmount * 0.04) / 12; // 4% Trinity Rule

            // Aggiorna KPI
            document.getElementById('resFinalAmount').textContent = formatMoney(finalAmount);
            document.getElementById('resGrowthMultiplier').textContent = `${{multiplier.toFixed(1)}}x il capitale totale versato`;
            document.getElementById('resTotalDeposits').textContent = formatMoney(totalDeposited);
            document.getElementById('resInitialVsPac').textContent = `${{Math.round(initial/1000)}}k iniziale + ${{Math.round((totalDeposited - initial)/1000)}}k PAC`;
            document.getElementById('resTotalGains').textContent = `+${{formatMoney(gains)}}`;
            document.getElementById('resGainsShare').textContent = `${{gainsShare.toFixed(1)}}% del portafoglio totale`;
            document.getElementById('resPassiveIncome').textContent = formatMoney(monthlyPassive) + ' / mese';

            // Popola Tabella
            let tableHtml = '';
            tableData.forEach(d => {{
                tableHtml += `
                    <tr class="hover:bg-slate-50/80">
                        <td class="p-2 font-bold">${{d.year}}° Anno</td>
                        <td class="p-2 text-right text-slate-600">${{formatMoney(d.deposited)}}</td>
                        <td class="p-2 text-right text-teal-600 font-semibold">+${{formatMoney(d.interest)}}</td>
                        <td class="p-2 text-right font-black text-emerald-700">${{formatMoney(d.total)}}</td>
                    </tr>
                `;
            }});
            document.getElementById('tableBody').innerHTML = tableHtml;

            // Render SVG Exponential Curve
            renderSvgCurve(tableData, years);
        }}

        function renderSvgCurve(data, years) {{
            const svg = document.getElementById('compoundSvg');
            const W = 520;
            const H = 200;
            const padL = 40;
            const padR = 25;
            const padB = 30;
            const padT = 20;

            const maxVal = data[data.length - 1].total;
            const usableW = W - padL - padR;
            const usableH = H - padB - padT;

            const getX = (y) => padL + ((y / years) * usableW);
            const getY = (val) => (H - padB) - ((val / maxVal) * usableH);

            let depPoints = [`${{padL}},${{getY(data[0].deposited)}}`];
            let totPoints = [`${{padL}},${{getY(data[0].total)}}`];

            data.forEach(d => {{
                depPoints.push(`${{getX(d.year)}},${{getY(d.deposited)}}`);
                totPoints.push(`${{getX(d.year)}},${{getY(d.total)}}`);
            }});

            let svgContent = `
                <!-- Background Grid -->
                <line x1="${{padL}}" y1="${{padT}}" x2="${{W - padR}}" y2="${{padT}}" stroke="#334155" stroke-width="1" stroke-dasharray="2 2" />
                <line x1="${{padL}}" y1="${{padT + usableH / 2}}" x2="${{W - padR}}" y2="${{padT + usableH / 2}}" stroke="#334155" stroke-width="1" stroke-dasharray="2 2" />
                <line x1="${{H - padB}}" y1="${{H - padB}}" x2="${{W - padR}}" y2="${{H - padB}}" stroke="#64748b" stroke-width="1.5" />

                <!-- Filled Area between Deposited and Total (The Compound Interest Area) -->
                <polygon points="${{totPoints.join(' ')}} ${{getX(years)}},${{H - padB}} ${{padL}},${{H - padB}}" fill="rgba(16, 185, 129, 0.18)" />
                <polygon points="${{depPoints.join(' ')}} ${{getX(years)}},${{H - padB}} ${{padL}},${{H - padB}}" fill="rgba(148, 163, 184, 0.22)" />

                <!-- Lines -->
                <polyline points="${{depPoints.join(' ')}}" fill="none" stroke="#94a3b8" stroke-width="2.2" stroke-dasharray="4 2" />
                <polyline points="${{totPoints.join(' ')}}" fill="none" stroke="#10b981" stroke-width="3" />
            `;

            // Data Points on end
            const lastD = data[data.length - 1];
            svgContent += `
                <circle cx="${{getX(years)}}" cy="${{getY(lastD.total)}}" r="4.5" fill="#10b981" stroke="#ffffff" stroke-width="2" />
                <circle cx="${{getX(years)}}" cy="${{getY(lastD.deposited)}}" r="4" fill="#94a3b8" stroke="#ffffff" stroke-width="1.5" />
            `;

            // X Axis Labels
            for (let y = 0; y <= years; y += Math.max(5, Math.round(years / 5))) {{
                svgContent += `
                    <text x="${{getX(y)}}" y="${{H - padB + 14}}" fill="#94a3b8" font-size="9" font-family="monospace" text-anchor="middle">${{y}}a</text>
                `;
            }}

            svg.innerHTML = svgContent;

            updateUrlParams();
        }}

        // Print date
        const pDate = document.getElementById('printDate');
        if (pDate) pDate.textContent = new Date().toLocaleDateString('it-IT');

        // Initial Run
        initFromUrl();
        calculateCompound();

        function updateUrlParams() {{
            try {{
                const params = new URLSearchParams();
                if (currentCurrency !== 'EUR') params.set('curr', currentCurrency);
                const initial = document.getElementById('inputInitial').value;
                if (initial && initial !== '5000') params.set('initial', initial);
                const monthly = document.getElementById('inputMonthly').value;
                if (monthly && monthly !== '250') params.set('monthly', monthly);
                const years = document.getElementById('inputYears').value;
                if (years && years !== '20') params.set('years', years);
                const ret = document.getElementById('inputReturn').value;
                if (ret && ret !== '7.00') params.set('return', ret);

                const query = params.toString();
                const newUrl = query ? (window.location.pathname + '?' + query) : window.location.pathname;
                window.history.replaceState({{}}, '', newUrl);
            }} catch(e) {{}}
        }}

        function initFromUrl() {{
            try {{
                const params = new URLSearchParams(window.location.search);
                if (params.has('curr')) setCurrency(params.get('curr'));
                if (params.has('initial')) setInitial(parseFloat(params.get('initial')));
                if (params.has('monthly')) setMonthly(parseFloat(params.get('monthly')));
                if (params.has('years')) setYears(parseInt(params.get('years')));
                if (params.has('return')) setReturn(parseFloat(params.get('return')));
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
            prompt('Copia questo link con la tua proiezione PAC:', text);
        }}
    </script>
</body>
</html>
"""

out_path = os.path.join(current_dir, 'pac.html')
with open(out_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"pac.html successfully built at: {out_path}")
