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
    <meta name="google-site-verification" content="MRdbDm9lLhokeD3I0FOpUSOhNaF_2WaveKvu52FxtG4">
    <title>Calcolo Margine di Profitto, Ricarico (Markup) e Prezzo di Vendita Online | MargineFacile</title>
    <meta name="description" content="Calcola il margine di profitto lordo, il ricarico percentuale (markup) e il prezzo di vendita ottimale da costo di produzione (COGS). Con scorporo e applicazione IVA.">
    
    <!-- Canonical & SEO -->
    <link rel="canonical" href="https://www.omnitoolslab.com/margine">
    <meta name="robots" content="index, follow">
    <meta property="og:type" content="website">
    <meta property="og:title" content="MargineFacile — Calcolo Margine di Profitto & Ricarico (Markup)">
    <meta property="og:description" content="Utility professionale per commercio ed e-commerce: calcolo prezzo di vendita da costo, margine percentuale vs ricarico e scorporo imposte.">
    <meta property="og:url" content="https://www.omnitoolslab.com/margine">
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
      "name": "MargineFacile",
      "url": "https://www.omnitoolslab.com/margine",
      "applicationCategory": "BusinessApplication",
      "operatingSystem": "All",
      "description": "Calcolatore gratuito di margine commerciale, ricarico percentuale (markup), utile lordo e prezzo di vendita.",
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
          "name": "Qual è la differenza sostanziale tra margine di profitto e ricarico (markup)?",
          "acceptedAnswer": {{
            "@type": "Answer",
            "text": "Il margine di profitto esprime la percentuale di utile calcolata sul prezzo di vendita finale (non può mai superare il 100%). Il ricarico (markup) indica invece di quale percentuale viene aumentato il costo di acquisto o produzione (COGS) per arrivare al prezzo di vendita (può superare abbondantemente il 100% o 500%)."
          }}
        }},
        {{
          "@type": "Question",
          "name": "Cosa include esattamente il costo del venduto (COGS)?",
          "acceptedAnswer": {{
            "@type": "Answer",
            "text": "Il COGS (Cost of Goods Sold) comprende esclusivamente i costi diretti imputabili al singolo bene o servizio venduto: prezzo di acquisto dal fornitore, imballaggio primario, spese di trasporto/doganali inbound e manodopera diretta di lavorazione. Non include costi fissi generali o marketing indiretto."
          }}
        }},
        {{
          "@type": "Question",
          "name": "Perché il margine di profitto non può mai raggiungere o superare il 100%?",
          "acceptedAnswer": {{
            "@type": "Answer",
            "text": "Poiché il margine è il rapporto tra utile e prezzo di vendita [Margine = (Utile / Prezzo) × 100], per raggiungere il 100% il costo del prodotto dovrebbe essere zero assoluto. Superare il 100% è matematicamente impossibile a meno che il costo non sia negativo. Il ricarico invece non ha alcun limite superiore teorico."
          }}
        }},
        {{
          "@type": "Question",
          "name": "Come si calcola lo scorporo dell'IVA dal prezzo lordo al consumatore?",
          "acceptedAnswer": {{
            "@type": "Answer",
            "text": "Per scorporare l'IVA da un prezzo lordo finale al dettaglio si applica la formula: Prezzo Netto = Prezzo Lordo / (1 + Aliquota IVA/100). Ad esempio, per un'IVA al 22%, si divide il prezzo lordo per 1,22. L'IVA non costituisce ricavo per l'azienda ma un debito verso l'Erario."
          }}
        }},
        {{
          "@type": "Question",
          "name": "Quali sono i margini di profitto medi di riferimento per settore?",
          "acceptedAnswer": {{
            "@type": "Answer",
            "text": "Nel retail e grande distribuzione alimentare i margini netti sono compressi (2%-5%), mentre i margini lordi si attestano sul 20%-30%. Nell'e-commerce e moda i margini lordi medi variano tra il 50% e il 70%. Nei software B2B e servizi SaaS il margine lordo supera frequentemente l'80%."
          }}
        }}
      ]
    }}
    </script>
</head>
<body class="bg-slate-50 text-slate-800 min-h-screen flex flex-col justify-between">

    {render_suite_header('margine')}

    <main class="max-w-5xl mx-auto px-3 sm:px-6 py-2.5 sm:py-5 flex-1 w-full space-y-3 sm:space-y-5">

        <!-- Print-only official header -->
        <div class="print-only mb-6 border-b-2 border-slate-900 pb-3">
            <div class="flex justify-between items-center">
                <div>
                    <h1 class="text-xl font-black text-slate-900 uppercase tracking-wide">OmniTools Lab · MargineFacile</h1>
                    <p class="text-xs text-slate-600">Scheda Analitica di Pricing, Margine di Contribuzione & Ricarico</p>
                </div>
                <div class="text-right text-xs text-slate-500 font-mono">
                    <p>Data Stampa: <span id="printDate"></span></p>
                    <p>omnitoolslab.com/margine</p>
                </div>
            </div>
        </div>

        <!-- Hero Title & Global Currency Bar -->
        <div class="flex flex-col md:flex-row items-center justify-between gap-4 no-print pb-2 border-b border-slate-200">
            <div class="text-left space-y-1">
                <div class="flex items-center gap-2">
                    <span class="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded-full bg-emerald-100 text-emerald-800 text-[11px] font-extrabold border border-emerald-200">
                        <span>🏷️</span> PRICING & REDDITIVITÀ COMMERCIALE
                    </span>
                    <span class="text-xs font-bold text-slate-400">· Risolvi la confusione Margine vs Markup</span>
                </div>
                <h1 class="text-xl sm:text-2xl font-black text-slate-900 tracking-tight">Calcolo Margine di Profitto, Ricarico (Markup) & Prezzo</h1>
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

        <!-- Mode Switcher: Calcolo da Costo + Margine VS Calcolo da Costo + Prezzo Effettivo -->
        <div class="max-w-md mx-auto p-1 bg-slate-200/80 rounded-2xl flex text-xs font-bold gap-1 no-print">
            <button type="button" id="tabModeMargin" onclick="setCalcMode('target_margin')" class="flex-1 py-2 rounded-xl bg-white text-emerald-800 shadow-xs font-extrabold transition">Fissa Margine Obiettivo</button>
            <button type="button" id="tabModePrice" onclick="setCalcMode('given_price')" class="flex-1 py-2 rounded-xl text-slate-700 hover:text-slate-900 transition">Analizza Prezzo Esistente</button>
        </div>

        <!-- Main Interactive Grid -->
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-6">

            <!-- Controls Column (5 cols) -->
            <div class="lg:col-span-5 bg-white rounded-2xl p-4 sm:p-5 border border-slate-200 shadow-xs space-y-4 card-box">
                <span class="text-xs font-bold uppercase tracking-wider text-slate-700 block pb-2 border-b border-slate-100 flex items-center justify-between">
                    <span class="flex items-center gap-1.5"><span>⚙️</span> Dati di Costo & Obiettivi</span>
                    <div class="flex items-center gap-2">
                        <button type="button" onclick="copyShareLink()" id="btnShare" title="Copia link con i parametri attuali" class="text-[11px] font-bold text-emerald-800 bg-emerald-50 hover:bg-emerald-100 px-2 py-0.5 rounded-lg border border-emerald-200 transition flex items-center gap-1 cursor-pointer">
                            <span>🔗</span> <span id="btnShareText">Condividi</span>
                        </button>
                        <button type="button" onclick="resetDefaults()" class="text-[11px] font-semibold text-slate-500 hover:text-slate-800">Reimposta</button>
                    </div>
                </span>

                <!-- Costo Unitario del Prodotto (COGS) -->
                <div>
                    <div class="flex justify-between items-center mb-1">
                        <label class="text-xs font-bold text-slate-700">Costo di Acquisto / Produzione (<span class="currencySymbol">€</span>)</label>
                        <span id="badgeCost" class="text-xs font-bold font-mono text-slate-800 bg-slate-100 px-2 py-0.5 rounded border border-slate-200">45,00 €</span>
                    </div>
                    <input type="number" id="inputCost" value="45" min="0.01" max="1000000" step="1" oninput="calculateMargin()" class="w-full p-2.5 bg-slate-50 border border-slate-200 rounded-xl font-bold font-mono text-base text-slate-900 focus:outline-none focus:ring-2 focus:ring-emerald-500">
                    <div class="grid grid-cols-4 gap-1 mt-1 text-[10px] font-bold no-print">
                        <button type="button" onclick="setCost(10)" class="py-1 bg-slate-100 hover:bg-slate-200 rounded-lg text-slate-700 transition">10</button>
                        <button type="button" onclick="setCost(25)" class="py-1 bg-slate-100 hover:bg-slate-200 rounded-lg text-slate-700 transition">25</button>
                        <button type="button" onclick="setCost(45)" class="py-1 bg-slate-100 hover:bg-slate-200 rounded-lg text-slate-700 transition">45</button>
                        <button type="button" onclick="setCost(100)" class="py-1 bg-slate-100 hover:bg-slate-200 rounded-lg text-slate-700 transition">100</button>
                    </div>
                </div>

                <!-- Campo Variabile in base al Modo: Margine Obiettivo vs Prezzo Effettivo -->
                <div id="boxTargetMargin">
                    <div class="flex justify-between items-center mb-1">
                        <label class="text-xs font-bold text-slate-700">Margine di Profitto Desiderato (%)</label>
                        <span id="badgeMargin" class="text-xs font-bold font-mono text-emerald-700 bg-emerald-50 px-2 py-0.5 rounded border border-emerald-200">35.0 %</span>
                    </div>
                    <input type="number" id="inputMargin" value="35" min="1" max="99" step="1" oninput="syncFromInput('Margin')" class="w-full p-2.5 bg-slate-50 border border-slate-200 rounded-xl font-bold font-mono text-base text-slate-900 focus:outline-none focus:ring-2 focus:ring-emerald-500">
                    <input type="range" id="rangeMargin" min="5" max="85" step="1" value="35" oninput="syncFromRange('Margin')" class="w-full mt-2 accent-emerald-600 cursor-pointer">
                    <div class="grid grid-cols-4 gap-1 mt-1 text-[10px] font-bold no-print">
                        <button type="button" onclick="setTargetMargin(20)" class="py-1 bg-slate-100 hover:bg-slate-200 rounded-lg text-slate-700 transition">20%</button>
                        <button type="button" onclick="setTargetMargin(30)" class="py-1 bg-slate-100 hover:bg-slate-200 rounded-lg text-slate-700 transition">30%</button>
                        <button type="button" onclick="setTargetMargin(40)" class="py-1 bg-slate-100 hover:bg-slate-200 rounded-lg text-slate-700 transition">40%</button>
                        <button type="button" onclick="setTargetMargin(50)" class="py-1 bg-slate-100 hover:bg-slate-200 rounded-lg text-slate-700 transition">50%</button>
                    </div>
                </div>

                <!-- Modo B: Inserimento Prezzo di Vendita (nascosto di default) -->
                <div id="boxSellingPrice" class="hidden">
                    <div class="flex justify-between items-center mb-1">
                        <label class="text-xs font-bold text-slate-700">Prezzo di Vendita Effettivo (<span class="currencySymbol">€</span>)</label>
                        <span id="badgeSellingPrice" class="text-xs font-bold font-mono text-emerald-700 bg-emerald-50 px-2 py-0.5 rounded border border-emerald-200">69,23 €</span>
                    </div>
                    <input type="number" id="inputSellingPrice" value="69.23" min="0.01" max="1000000" step="0.5" oninput="calculateMargin()" class="w-full p-2.5 bg-slate-50 border border-slate-200 rounded-xl font-bold font-mono text-base text-slate-900 focus:outline-none focus:ring-2 focus:ring-emerald-500">
                </div>

                <!-- Aliquota IVA / Sales Tax Opzionale -->
                <div class="pt-2 border-t border-slate-100">
                    <div class="flex justify-between items-center mb-1">
                        <label class="text-xs font-bold text-slate-700 flex items-center gap-1">
                            <span>🏛️</span> Imposta / IVA sul Prezzo
                        </label>
                    </div>
                    <select id="selVat" onchange="calculateMargin()" class="w-full p-2.5 bg-slate-50 border border-slate-200 rounded-xl font-bold text-xs text-slate-800 focus:outline-none focus:ring-2 focus:ring-emerald-500 cursor-pointer">
                        <option value="0">0% — Nessuna imposta / B2B Export / Esente</option>
                        <option value="4">4% — IVA Agevolata (Prima necessità / Libri)</option>
                        <option value="10">10% — IVA Ridotta (Turismo / Alimentari)</option>
                        <option value="22" selected>22% — IVA Ordinaria (Standard Italia)</option>
                    </select>
                </div>
            </div>

            <!-- Results & Visualization Column (7 cols) -->
            <div class="lg:col-span-7 space-y-4">

                <!-- Primary KPI Card: Prezzo Consigliato Netto & Lordo -->
                <div class="bg-gradient-to-br from-emerald-600 via-teal-700 to-slate-900 rounded-2xl p-5 text-white shadow-md relative overflow-hidden card-box">
                    <div class="relative z-10 flex flex-col sm:flex-row sm:items-center justify-between gap-4">
                        <div>
                            <span class="text-[11px] font-extrabold uppercase tracking-wider text-emerald-200 block">Prezzo di Vendita Suggerito (Netto)</span>
                            <div class="text-3xl sm:text-4xl font-black font-mono tracking-tight text-white mt-1" id="resSellingPrice">
                                69,23 €
                            </div>
                            <span class="text-xs text-emerald-100/90 mt-0.5 block" id="resPriceWithVat">84,46 € con IVA 22% inclusa</span>
                        </div>
                        <div class="bg-white/10 backdrop-blur-xs p-3 rounded-xl border border-white/20 text-right sm:text-right shrink-0">
                            <span class="text-[10px] uppercase font-bold text-emerald-200 block">Utile Lordo Unitario</span>
                            <div class="text-xl font-black font-mono text-white mt-0.5" id="resGrossProfit">+24,23 €</div>
                            <span class="text-[10px] font-semibold text-emerald-100" id="resMarginKpi">Margine: 35.0%</span>
                        </div>
                    </div>
                </div>

                <!-- Secondary KPI Metrics Grid (Margin vs Markup) -->
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
                    <div class="bg-white rounded-xl p-3.5 border border-slate-200 shadow-2xs card-box">
                        <div class="flex items-center justify-between">
                            <span class="text-[11px] font-bold text-slate-500 uppercase tracking-wider block">Ricarico Percentuale (Markup)</span>
                            <span class="text-[9px] px-1.5 py-0.5 bg-blue-100 text-blue-800 rounded font-bold">sul Costo</span>
                        </div>
                        <div class="text-xl font-black font-mono text-blue-700 mt-1" id="resMarkupPercent">53.8 %</div>
                        <span class="text-[10px] text-slate-500">Percentuale applicata sopra il costo di fornitura</span>
                    </div>

                    <div class="bg-white rounded-xl p-3.5 border border-slate-200 shadow-2xs card-box">
                        <div class="flex items-center justify-between">
                            <span class="text-[11px] font-bold text-slate-500 uppercase tracking-wider block">Margine di Profitto (Margin)</span>
                            <span class="text-[9px] px-1.5 py-0.5 bg-emerald-100 text-emerald-800 rounded font-bold">sul Prezzo</span>
                        </div>
                        <div class="text-xl font-black font-mono text-emerald-700 mt-1" id="txtExpMargin">35.0 %</div>
                        <span class="text-[10px] text-slate-500">Frazione dell'incasso finale che resta come profitto</span>
                    </div>
                </div>

                <!-- Price Decomposition Waterfall Bar -->
                <div class="bg-slate-900 text-white rounded-2xl p-4 shadow-sm space-y-3 card-box">
                    <div class="flex items-center justify-between text-xs">
                        <span class="font-bold flex items-center gap-1.5">
                            <span>📊</span> Decomposizione del Prezzo di Vendita al Pubblico
                        </span>
                    </div>

                    <!-- Progress Bar Waterfall -->
                    <div class="w-full h-8 bg-slate-800 rounded-xl overflow-hidden flex font-mono text-xs font-bold leading-8 text-center">
                        <div id="barCost" class="bg-slate-500 text-white truncate transition-all duration-300" style="width: 53%;">Costo 53%</div>
                        <div id="barProfit" class="bg-emerald-500 text-slate-950 truncate transition-all duration-300" style="width: 29%;">Utile 29%</div>
                        <div id="barVat" class="bg-amber-400 text-slate-950 truncate transition-all duration-300" style="width: 18%;">IVA 18%</div>
                    </div>
                    <div class="flex justify-between items-center text-[10px] text-slate-400 font-mono px-1">
                        <span class="flex items-center gap-1"><span class="w-2.5 h-2.5 bg-slate-500 rounded-xs"></span> Costo Acquisto (COGS)</span>
                        <span class="flex items-center gap-1"><span class="w-2.5 h-2.5 bg-emerald-500 rounded-xs"></span> Utile Lordo</span>
                        <span class="flex items-center gap-1"><span class="w-2.5 h-2.5 bg-amber-400 rounded-xs"></span> Imposta / IVA</span>
                    </div>
                </div>

                <!-- Breakdown Summary Table -->
                <div class="bg-white rounded-2xl border border-slate-200 shadow-2xs overflow-hidden card-box">
                    <div class="p-3.5 bg-slate-100/80 border-b border-slate-200 flex items-center justify-between">
                        <span class="text-xs font-bold text-slate-800 flex items-center gap-1.5">
                            <span>📋</span> Prospetto Contabile Unitario
                        </span>
                        <span class="text-[10px] font-mono text-slate-500">Valuta Selezionata</span>
                    </div>
                    <div class="divide-y divide-slate-100 text-xs">
                        <div class="p-2.5 flex justify-between items-center">
                            <span class="text-slate-600">Costo del Prodotto (COGS):</span>
                            <span class="font-mono font-bold text-slate-800" id="dtCost">45,00 €</span>
                        </div>
                        <div class="p-2.5 flex justify-between items-center bg-emerald-50/50">
                            <span class="text-emerald-900 font-medium">Utile Unitario di Contribuzione:</span>
                            <span class="font-mono font-black text-emerald-700" id="dtProfit">+24,23 €</span>
                        </div>
                        <div class="p-2.5 flex justify-between items-center font-bold">
                            <span class="text-slate-800">Prezzo Imponibile di Vendita:</span>
                            <span class="font-mono text-slate-900" id="dtNetPrice">69,23 €</span>
                        </div>
                        <div class="p-2.5 flex justify-between items-center bg-slate-50 font-bold">
                            <span class="text-slate-900">Prezzo Finale al Consumatore (Lordo):</span>
                            <span class="font-mono text-emerald-800" id="dtGrossPrice">84,46 €</span>
                        </div>
                    </div>
                </div>

            </div>
        </div>

        <!-- Educational Didactic Box: Margine vs Ricarico Explanation -->
        <div class="p-4 sm:p-5 bg-white rounded-2xl border border-slate-200 text-xs leading-relaxed text-slate-700 space-y-3 card-box">
            <h3 class="text-sm font-extrabold text-slate-900 flex items-center gap-2">
                <span>💡</span>
                <span>Qual è la differenza fondamentale tra Margine e Ricarico (Markup)?</span>
            </h3>
            <p>
                Molti imprenditori, artigiani e commercianti confondono <strong>Margine %</strong> e <strong>Ricarico %</strong>, rischiando di vendere sottocosto o erodere la propria marginalità.
            </p>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-3 pt-1">
                <div class="p-3 bg-slate-50 rounded-xl border border-slate-200 space-y-1">
                    <span class="font-bold text-emerald-800 text-xs block">Margine di Profitto (Gross Margin):</span>
                    <p class="text-[11px] text-slate-600">
                        È la percentuale di profitto <strong>calcolata sul prezzo di vendita finale</strong>. Indica quanti centesimi di utile restano per ogni euro incassato. Non può mai superare il 100%.
                    </p>
                    <div class="font-mono text-[10px] bg-white p-1.5 rounded border border-slate-200 text-slate-800 mt-1">
                        Margine % = (Utile / Prezzo Vendita) × 100
                    </div>
                </div>

                <div class="p-3 bg-slate-50 rounded-xl border border-slate-200 space-y-1">
                    <span class="font-bold text-blue-800 text-xs block">Ricarico (Markup):</span>
                    <p class="text-[11px] text-slate-600">
                        È la percentuale di profitto <strong>calcolata sul costo di acquisto/produzione</strong>. Indica di quanto devi aumentare il costo per ottenere il prezzo di vendita. Può superare il 100%, 200% o 500%.
                    </p>
                    <div class="font-mono text-[10px] bg-white p-1.5 rounded border border-slate-200 text-slate-800 mt-1">
                        Ricarico % = (Utile / Costo COGS) × 100
                    </div>
                </div>
            </div>
            <p class="text-[11px] text-slate-500">
                <strong>Regola pratica veloce:</strong> Un ricarico del <span class="font-bold text-blue-700" id="txtExpMarkup">53.8%</span> su un prodotto genera un margine effettivo del <span class="font-bold text-emerald-700">35.0%</span>.
            </p>
        </div>

        <!-- FAQ Section (Frequently Asked Questions) -->
        <section class="mt-8 bg-white rounded-3xl p-6 sm:p-8 border border-slate-200 shadow-2xs space-y-6">
            <div class="space-y-1">
                <span class="text-xs font-black uppercase tracking-wider text-emerald-800">Guida & Domande Frequenti</span>
                <h2 class="text-lg sm:text-xl font-black text-slate-900 tracking-tight">Tutto sul Calcolo dei Margini, Prezzo di Vendita e Ricarico</h2>
            </div>

            <div class="space-y-3">
                <details class="group bg-slate-50/80 hover:bg-slate-50 rounded-2xl border border-slate-200/80 p-4 transition duration-150" open>
                    <summary class="flex justify-between items-center font-bold text-xs sm:text-sm text-slate-900 cursor-pointer list-none select-none">
                        <span>Qual è la differenza sostanziale tra margine di profitto e ricarico (markup)?</span>
                        <svg class="w-4 h-4 text-slate-400 group-open:-rotate-180 transition-transform duration-200 shrink-0 ml-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/>
                        </svg>
                    </summary>
                    <div class="text-xs sm:text-sm text-slate-600 mt-2.5 leading-relaxed border-t border-slate-200/60 pt-2.5">
                        La differenza fondamentale risiede nella base imponibile del calcolo. Il <strong>margine di profitto lordo</strong> (Margin) misura la percentuale di utile rispetto al ricavo totale (prezzo di vendita finale): non può mai eccedere il 100%. Il <strong>ricarico</strong> (Markup) misura invece l'incremento percentuale applicato sopra il costo del prodotto: un ricarico del 100% raddoppia il prezzo e corrisponde a un margine del 50%.
                    </div>
                </details>

                <details class="group bg-slate-50/80 hover:bg-slate-50 rounded-2xl border border-slate-200/80 p-4 transition duration-150">
                    <summary class="flex justify-between items-center font-bold text-xs sm:text-sm text-slate-900 cursor-pointer list-none select-none">
                        <span>Cosa include esattamente il costo del venduto (COGS)?</span>
                        <svg class="w-4 h-4 text-slate-400 group-open:-rotate-180 transition-transform duration-200 shrink-0 ml-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/>
                        </svg>
                    </summary>
                    <div class="text-xs sm:text-sm text-slate-600 mt-2.5 leading-relaxed border-t border-slate-200/60 pt-2.5">
                        Il <strong>COGS</strong> (Cost of Goods Sold) raggruppa tutti i costi direttamente imputabili alla fabbricazione o all'acquisizione del prodotto finito: prezzo netto d'acquisto da fornitore o terzista, materie prime, manodopera diretta, packaging primario e oneri di spedizione o dogana sostenuti per l'approvvigionamento. Non comprende spese generali, affitti aziendali o costi promozionali indiretti.
                    </div>
                </details>

                <details class="group bg-slate-50/80 hover:bg-slate-50 rounded-2xl border border-slate-200/80 p-4 transition duration-150">
                    <summary class="flex justify-between items-center font-bold text-xs sm:text-sm text-slate-900 cursor-pointer list-none select-none">
                        <span>Perché il margine di profitto non può mai superare il 100%?</span>
                        <svg class="w-4 h-4 text-slate-400 group-open:-rotate-180 transition-transform duration-200 shrink-0 ml-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/>
                        </svg>
                    </summary>
                    <div class="text-xs sm:text-sm text-slate-600 mt-2.5 leading-relaxed border-t border-slate-200/60 pt-2.5">
                        Per definizione matematica, l'utile lordo è dato da <code>Prezzo di Vendita - Costo</code>. Dividendo l'utile per il prezzo di vendita, si ottiene un rapporto che raggiungerebbe il 100% solo se il costo fosse pari a zero. Superare il 100% significherebbe che il fornitore ti paga per ricevere il prodotto. Se desideri moltiplicare il costo per 3 o 4 volte, devi impostare un <em>ricarico (markup)</em> del 200% o 300%, non un margine.
                    </div>
                </details>

                <details class="group bg-slate-50/80 hover:bg-slate-50 rounded-2xl border border-slate-200/80 p-4 transition duration-150">
                    <summary class="flex justify-between items-center font-bold text-xs sm:text-sm text-slate-900 cursor-pointer list-none select-none">
                        <span>Come funziona lo scorporo dell'IVA dal prezzo al consumo?</span>
                        <svg class="w-4 h-4 text-slate-400 group-open:-rotate-180 transition-transform duration-200 shrink-0 ml-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/>
                        </svg>
                    </summary>
                    <div class="text-xs sm:text-sm text-slate-600 mt-2.5 leading-relaxed border-t border-slate-200/60 pt-2.5">
                        L'IVA (Imposta sul Valore Aggiunto) o Sales Tax è un'imposta di consumo riscossa dall'esercente per conto dello Stato. Per scorporare l'IVA da un prezzo lordo si divide per il coefficiente <code>1 + (Aliquota/100)</code>. Per esempio con IVA ordinaria italiana al 22%, un prodotto venduto a 122 € ha un imponibile netto di <code>122 / 1.22 = 100 €</code>. È su quest'ultimo imponibile netto che devono essere calcolati margine e markup.
                    </div>
                </details>

                <details class="group bg-slate-50/80 hover:bg-slate-50 rounded-2xl border border-slate-200/80 p-4 transition duration-150">
                    <summary class="flex justify-between items-center font-bold text-xs sm:text-sm text-slate-900 cursor-pointer list-none select-none">
                        <span>Quali sono i margini lordi medi nei diversi settori commerciali?</span>
                        <svg class="w-4 h-4 text-slate-400 group-open:-rotate-180 transition-transform duration-200 shrink-0 ml-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/>
                        </svg>
                    </summary>
                    <div class="text-xs sm:text-sm text-slate-600 mt-2.5 leading-relaxed border-t border-slate-200/60 pt-2.5">
                        I benchmark variano ampiamente: nella <strong>grande distribuzione e commercio alimentare</strong> i margini lordi oscillano tipicamente tra il 20% e il 30% a fronte di volumi enormi. Nel <strong>settore retail moda ed e-commerce</strong> il margine lordo ideale si situa tra il 50% e il 65% (ricarichi da 2x a 3x). Nei settori del <strong>software SaaS, consulenza e beni digitali</strong> i margini lordi superano stabilmente l'80%-90%.
                    </div>
                </details>
            </div>
        </section>

    </main>

    {render_unified_footer('margine')}

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
        let currentMode = 'target_margin'; // 'target_margin' or 'given_price'

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

            calculateMargin();
        }}

        function formatMoney(val) {{
            const c = CURRENCIES[currentCurrency];
            const formatted = val.toLocaleString('it-IT', {{ minimumFractionDigits: 2, maximumFractionDigits: 2 }});
            if (c.pos === 'before') {{
                return c.symbol + (c.space ? ' ' : '') + formatted;
            }} else {{
                return formatted + (c.space ? ' ' : '') + c.symbol;
            }}
        }}

        function setCalcMode(mode) {{
            currentMode = mode;
            const btnMargin = document.getElementById('tabModeMargin');
            const btnPrice = document.getElementById('tabModePrice');
            const boxMargin = document.getElementById('boxTargetMargin');
            const boxPrice = document.getElementById('boxSellingPrice');

            if (mode === 'target_margin') {{
                btnMargin.className = 'flex-1 py-2 rounded-xl bg-white text-emerald-800 shadow-xs font-extrabold transition';
                btnPrice.className = 'flex-1 py-2 rounded-xl text-slate-700 hover:text-slate-900 transition';
                boxMargin.classList.remove('hidden');
                boxPrice.classList.add('hidden');
            }} else {{
                btnPrice.className = 'flex-1 py-2 rounded-xl bg-white text-emerald-800 shadow-xs font-extrabold transition';
                btnMargin.className = 'flex-1 py-2 rounded-xl text-slate-700 hover:text-slate-900 transition';
                boxPrice.classList.remove('hidden');
                boxMargin.classList.add('hidden');
            }}
            calculateMargin();
        }}

        function setCost(c) {{
            document.getElementById('inputCost').value = c;
            calculateMargin();
        }}

        function setTargetMargin(m) {{
            document.getElementById('inputMargin').value = m;
            document.getElementById('rangeMargin').value = m;
            calculateMargin();
        }}

        function resetDefaults() {{
            setCalcMode('target_margin');
            setCost(45);
            setTargetMargin(35);
            document.getElementById('selVat').value = '22';
            calculateMargin();
        }}

        function syncFromInput(type) {{
            document.getElementById('range' + type).value = document.getElementById('input' + type).value;
            calculateMargin();
        }}

        function syncFromRange(type) {{
            document.getElementById('input' + type).value = document.getElementById('range' + type).value;
            calculateMargin();
        }}

        function calculateMargin() {{
            const cost = parseFloat(document.getElementById('inputCost').value) || 0;
            const vatRate = (parseFloat(document.getElementById('selVat').value) || 0) / 100;

            document.getElementById('badgeCost').textContent = formatMoney(cost);

            let sellingPrice = 0;
            let marginPercent = 0;
            let markupPercent = 0;
            let grossProfit = 0;

            if (currentMode === 'target_margin') {{
                marginPercent = parseFloat(document.getElementById('inputMargin').value) || 35;
                if (marginPercent >= 100) marginPercent = 99.9;
                document.getElementById('badgeMargin').textContent = marginPercent.toFixed(1) + ' %';

                // Formula: Prezzo di Vendita = Costo / (1 - (Margine / 100))
                sellingPrice = cost / (1 - (marginPercent / 100));
                grossProfit = sellingPrice - cost;
                markupPercent = cost > 0 ? (grossProfit / cost) * 100 : 0;
                document.getElementById('inputSellingPrice').value = sellingPrice.toFixed(2);
            }} else {{
                sellingPrice = parseFloat(document.getElementById('inputSellingPrice').value) || cost;
                document.getElementById('badgeSellingPrice').textContent = formatMoney(sellingPrice);
                grossProfit = sellingPrice - cost;
                marginPercent = sellingPrice > 0 ? (grossProfit / sellingPrice) * 100 : 0;
                markupPercent = cost > 0 ? (grossProfit / cost) * 100 : 0;
            }}

            const priceWithVat = sellingPrice * (1 + vatRate);
            const vatAmount = priceWithVat - sellingPrice;

            // Aggiorna KPI
            document.getElementById('resSellingPrice').textContent = formatMoney(sellingPrice);
            document.getElementById('resPriceWithVat').textContent = vatRate > 0 ? `${{formatMoney(priceWithVat)}} con imposta/IVA` : 'Nessuna imposta applicata';
            document.getElementById('resGrossProfit').textContent = `+${{formatMoney(grossProfit)}}`;
            document.getElementById('resMarkupPercent').textContent = markupPercent.toFixed(1) + ' %';
            document.getElementById('resMarginKpi').textContent = `Margine: ${{marginPercent.toFixed(1)}}%`;

            document.getElementById('txtExpMargin').textContent = marginPercent.toFixed(1) + '%';
            document.getElementById('txtExpMarkup').textContent = markupPercent.toFixed(1) + '%';

            document.getElementById('dtCost').textContent = formatMoney(cost);
            document.getElementById('dtProfit').textContent = formatMoney(grossProfit);
            document.getElementById('dtNetPrice').textContent = formatMoney(sellingPrice);
            document.getElementById('dtGrossPrice').textContent = formatMoney(priceWithVat);

            // Aggiorna Barre di decomposizione visiva
            const totalForBar = priceWithVat > 0 ? priceWithVat : (cost + grossProfit);
            const costShare = (cost / totalForBar) * 100;
            const profitShare = Math.max(0, (grossProfit / totalForBar) * 100);
            const vatShare = (vatAmount / totalForBar) * 100;

            const barCost = document.getElementById('barCost');
            const barProfit = document.getElementById('barProfit');
            const barVat = document.getElementById('barVat');

            barCost.style.width = Math.max(5, costShare) + '%';
            barCost.textContent = `Costo ${{costShare.toFixed(0)}}%`;

            barProfit.style.width = Math.max(5, profitShare) + '%';
            barProfit.textContent = `Utile ${{profitShare.toFixed(0)}}%`;

            if (vatRate > 0) {{
                barVat.style.display = 'block';
                barVat.style.width = Math.max(5, vatShare) + '%';
                barVat.textContent = `IVA ${{vatShare.toFixed(0)}}%`;
            }} else {{
                barVat.style.display = 'none';
            }}

            updateUrlParams();
        }}

        // Print date
        const pDate = document.getElementById('printDate');
        if (pDate) pDate.textContent = new Date().toLocaleDateString('it-IT');

        // Initial Run
        initFromUrl();
        calculateMargin();

        function updateUrlParams() {{
            try {{
                const params = new URLSearchParams();
                if (currentCurrency !== 'EUR') params.set('curr', currentCurrency);
                if (currentMode !== 'target_margin') params.set('mode', currentMode);
                const cost = document.getElementById('inputCost').value;
                if (cost && cost !== '45') params.set('cost', cost);
                if (currentMode === 'target_margin') {{
                    const margin = document.getElementById('inputMargin').value;
                    if (margin && margin !== '35') params.set('margin', margin);
                }} else {{
                    const price = document.getElementById('inputSellingPrice').value;
                    if (price) params.set('price', price);
                }}
                const vat = document.getElementById('selVat').value;
                if (vat !== '22') params.set('vat', vat);
                
                const query = params.toString();
                const newUrl = query ? (window.location.pathname + '?' + query) : window.location.pathname;
                window.history.replaceState({{}}, '', newUrl);
            }} catch(e) {{}}
        }}

        function initFromUrl() {{
            try {{
                const params = new URLSearchParams(window.location.search);
                if (params.has('curr')) setCurrency(params.get('curr'));
                if (params.has('mode')) setCalcMode(params.get('mode'));
                if (params.has('cost')) setCost(parseFloat(params.get('cost')));
                if (params.has('margin')) setTargetMargin(parseFloat(params.get('margin')));
                if (params.has('price')) {{
                    document.getElementById('inputSellingPrice').value = params.get('price');
                }}
                if (params.has('vat')) document.getElementById('selVat').value = params.get('vat');
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
            prompt('Copia questo link con i tuoi parametri salvati:', text);
        }}
    </script>
</body>
</html>
"""

out_path = os.path.join(current_dir, 'margine.html')
with open(out_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"margine.html successfully built at: {out_path}")
