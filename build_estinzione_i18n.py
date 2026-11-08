import json
import sys
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
if base_dir not in sys.path:
    sys.path.insert(0, base_dir)

from nav_header import render_suite_header, render_suite_header_js
from unified_footer import render_unified_footer, render_unified_footer_js

with open(os.path.join(base_dir, "translations_estinzione.json"), "r", encoding="utf-8") as f:
    t_data = json.load(f)

t_json_str = json.dumps(t_data, ensure_ascii=False)

header_html = render_suite_header("estinzione")
header_js = render_suite_header_js()
footer_html = render_unified_footer("estinzione")
footer_js = render_unified_footer_js()

html_code = f"""<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0">
    <meta name="google-site-verification" content="MRdbDm9lLhokeD3I0FOpUSOhNaF_2WaveKvu52FxtG4">
    <title>Calcolo Estinzione Anticipata Mutuo Online — Riduci Rata o Anni? | EstinzioneFacile</title>
    <meta name="description" content="Simulatore professionale gratuito per l'estinzione anticipata parziale del mutuo (Legge Bersani). Confronta subito: conviene abbassare la rata mensile o ridurre gli anni? Calcola il totale degli interessi bancari risparmiati ed esporta in CSV.">
    
    <!-- Canonical & SEO Meta Tags -->
    <link rel="canonical" href="https://www.omnitoolslab.com/estinzione">
    <meta name="robots" content="index, follow">
    <meta property="og:type" content="website">
    <meta property="og:title" content="EstinzioneFacile — Simulatore Estinzione Anticipata Mutuo (Rata vs Durata)">
    <meta property="og:description" content="Confronta istantaneamente le due opzioni di estinzione parziale del mutuo: risparmio rata mensile vs riduzione durata anni con zero penali.">
    <meta property="og:url" content="https://www.omnitoolslab.com/estinzione">
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
          "@id": "https://www.omnitoolslab.com/estinzione#app",
          "url": "https://www.omnitoolslab.com/estinzione",
          "name": "EstinzioneFacile — Simulatore Estinzione Anticipata Mutuo",
          "applicationCategory": "FinanceApplication",
          "operatingSystem": "All",
          "browserRequirements": "Requires JavaScript. Requires HTML5.",
          "offers": {{
            "@type": "Offer",
            "price": "0",
            "priceCurrency": "EUR"
          }},
          "description": "Simulatore di estinzione anticipata parziale del mutuo. Calcola se conviene abbassare la rata mensile o ridurre gli anni e il totale interessi risparmiati secondo la legge Bersani.",
          "inLanguage": ["it", "en", "es", "fr", "de", "pt"]
        }},
        {{
          "@type": "BreadcrumbList",
          "@id": "https://www.omnitoolslab.com/estinzione#breadcrumb",
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
              "name": "Estinzione Anticipata Mutuo",
              "item": "https://www.omnitoolslab.com/estinzione"
            }}
          ]
        }},
        {{
          "@type": "FAQPage",
          "@id": "https://www.omnitoolslab.com/estinzione#faq",
          "mainEntity": [
            {{
              "@type": "Question",
              "name": "L'estinzione anticipata parziale del mutuo prevede penali o costi bancari?",
              "acceptedAnswer": {{
                "@type": "Answer",
                "text": "No. In Italia, grazie al Decreto Bersani (Legge 40/2007), per tutti i mutui stipulati o rinegoziati per l'acquisto o la ristrutturazione di immobili adibiti ad abitazione o attività professionale, le penali di estinzione anticipata totale o parziale sono nulle per legge."
              }}
            }},
            {{
              "@type": "Question",
              "name": "Conviene di più abbassare la rata mensile o diminuire gli anni del mutuo?",
              "acceptedAnswer": {{
                "@type": "Answer",
                "text": "Dal punto di vista puramente economico e matematico, ridurre gli anni del mutuo (durata) genera un risparmio di interessi notevolmente più elevato rispetto alla riduzione della sola rata."
              }}
            }},
            {{
              "@type": "Question",
              "name": "Come viene ricalcolato l'ammortamento dopo un versamento anticipato?",
              "acceptedAnswer": {{
                "@type": "Answer",
                "text": "La somma versata abbatte direttamente il debito residuo in quota capitale. Da quel momento, gli interessi futuri vengono calcolati dalla banca esclusivamente sul nuovo debito ridotto."
              }}
            }},
            {{
              "@type": "Question",
              "name": "Esiste un importo minimo obbligatorio per l'estinzione parziale?",
              "acceptedAnswer": {{
                "@type": "Answer",
                "text": "La legge non impone una soglia minima, ma molti contratti bancari indicano un importo minimo per singola operazione (spesso 1.000 € o l'equivalente di una rata mensile)."
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
                        <span>⚡</span> <span id="heroBadge">OMNIFINANCE · ESTINZIONE ANTICIPATA</span>
                    </span>
                    <span class="text-xs font-bold text-slate-400">· Legge Bersani (Zero Penali)</span>
                </div>
                <h1 id="heroTitle" class="text-xl sm:text-2xl font-black text-slate-900 tracking-tight">Simulatore Estinzione Anticipata Mutuo</h1>
                <p id="heroDesc" class="text-xs sm:text-sm text-slate-600">
                    Confronta istantaneamente le due opzioni: conviene ridurre la rata mensile o accorciare la durata del mutuo in anni?
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
        <section aria-label="Formula Estinzione Anticipata Mutuo" class="no-print bg-gradient-to-r from-emerald-50 to-teal-50 border border-emerald-200/80 rounded-2xl p-3.5 sm:p-4 text-slate-800 shadow-xs mb-3">
            <div class="flex items-start gap-3">
                <span class="w-7 h-7 sm:w-8 sm:h-8 rounded-xl bg-emerald-600 text-white flex items-center justify-center font-bold text-xs sm:text-sm shrink-0 shadow-xs">fx</span>
                <div class="text-xs sm:text-sm space-y-1">
                    <p class="font-extrabold text-slate-900 tracking-tight text-xs sm:text-sm">
                        Regola Matematica dell'Estinzione Anticipata: <code class="bg-white px-2 py-0.5 rounded-md border border-emerald-200 text-emerald-800 font-mono font-black">Risparmio Durata (B) >> Risparmio Rata (A)</code>
                    </p>
                    <p class="text-slate-600 text-[11px] sm:text-xs leading-relaxed">
                        <strong>Esempio pratico:</strong> Con un debito residuo di <code class="font-bold">150.000 €</code> a <code class="font-bold">20 anni</code> al TAN del <code class="font-bold">3,50%</code> (rata 869,94 €), versando <code class="font-bold">20.000 €</code> di estinzione parziale: 
                        riducendo la rata risparmi <code class="font-mono text-emerald-800 font-bold">7.838 €</code> di interessi; accorciando invece la durata risparmi ben <code class="font-mono text-emerald-800 font-bold">17.797 €</code> di interessi ed estingui il mutuo <code class="font-bold">3 anni e mezzo prima</code>!
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
                        <span>⚙️</span> Dati del Tuo Mutuo Attuale
                    </span>
                    <button type="button" onclick="resetDefaults()" class="text-[11px] font-semibold text-slate-500 hover:text-slate-800">Reimposta</button>
                </div>

                <!-- Debito Residuo Attuale -->
                <div>
                    <div class="flex justify-between items-center mb-1">
                        <label class="text-xs font-bold text-slate-700">Capitale Residuo Attuale (<span class="currencySymbol">€</span>)</label>
                        <span id="badgeCurrentDebt" class="text-xs font-bold font-mono text-emerald-700 bg-emerald-50 px-2 py-0.5 rounded border border-emerald-200">150.000 €</span>
                    </div>
                    <div class="relative">
                        <input type="number" id="inputCurrentDebt" value="150000" min="5000" max="2000000" step="5000" oninput="syncFromInput('CurrentDebt')" class="w-full p-2.5 bg-slate-50 border border-slate-200 rounded-xl font-bold font-mono text-base text-slate-900 focus:outline-none focus:ring-2 focus:ring-emerald-500">
                    </div>
                    <input type="range" id="rangeCurrentDebt" min="10000" max="500000" step="5000" value="150000" oninput="syncFromRange('CurrentDebt')" class="w-full mt-2 accent-emerald-600 cursor-pointer">
                    <div class="grid grid-cols-4 gap-1 mt-1 text-[10px] font-bold no-print">
                        <button type="button" onclick="setVal('CurrentDebt', 80000)" class="py-1 bg-slate-100 hover:bg-slate-200 rounded-lg text-slate-700 transition">80k</button>
                        <button type="button" onclick="setVal('CurrentDebt', 120000)" class="py-1 bg-slate-100 hover:bg-slate-200 rounded-lg text-slate-700 transition">120k</button>
                        <button type="button" onclick="setVal('CurrentDebt', 180000)" class="py-1 bg-slate-100 hover:bg-slate-200 rounded-lg text-slate-700 transition">180k</button>
                        <button type="button" onclick="setVal('CurrentDebt', 250000)" class="py-1 bg-slate-100 hover:bg-slate-200 rounded-lg text-slate-700 transition">250k</button>
                    </div>
                </div>

                <!-- Anni Residui -->
                <div>
                    <div class="flex justify-between items-center mb-1">
                        <label class="text-xs font-bold text-slate-700">Anni di Ammortamento Residui</label>
                        <span id="badgeYearsLeft" class="text-xs font-bold font-mono text-slate-800 bg-slate-100 px-2 py-0.5 rounded border border-slate-200">20 anni (240 rate)</span>
                    </div>
                    <div class="relative">
                        <input type="number" id="inputYearsLeft" value="20" min="1" max="40" step="1" oninput="syncFromInput('YearsLeft')" class="w-full p-2.5 bg-slate-50 border border-slate-200 rounded-xl font-bold font-mono text-base text-slate-900 focus:outline-none focus:ring-2 focus:ring-emerald-500">
                    </div>
                    <input type="range" id="rangeYearsLeft" min="1" max="35" step="1" value="20" oninput="syncFromRange('YearsLeft')" class="w-full mt-2 accent-emerald-600 cursor-pointer">
                    <div class="grid grid-cols-4 gap-1 mt-1 text-[10px] font-bold no-print">
                        <button type="button" onclick="setVal('YearsLeft', 10)" class="py-1 bg-slate-100 hover:bg-slate-200 rounded-lg text-slate-700 transition">10a</button>
                        <button type="button" onclick="setVal('YearsLeft', 15)" class="py-1 bg-slate-100 hover:bg-slate-200 rounded-lg text-slate-700 transition">15a</button>
                        <button type="button" onclick="setVal('YearsLeft', 20)" class="py-1 bg-slate-100 hover:bg-slate-200 rounded-lg text-slate-700 transition">20a</button>
                        <button type="button" onclick="setVal('YearsLeft', 25)" class="py-1 bg-slate-100 hover:bg-slate-200 rounded-lg text-slate-700 transition">25a</button>
                    </div>
                </div>

                <!-- Tasso di Interesse TAN -->
                <div>
                    <div class="flex justify-between items-center mb-1">
                        <label class="text-xs font-bold text-slate-700">Tasso di Interesse Annuo (TAN %)</label>
                        <span id="badgeRate" class="text-xs font-bold font-mono text-emerald-700 bg-emerald-50 px-2 py-0.5 rounded border border-emerald-200">3.50 %</span>
                    </div>
                    <div class="relative">
                        <input type="number" id="inputRate" value="3.50" min="0.1" max="15.0" step="0.05" oninput="syncFromInput('Rate')" class="w-full p-2.5 bg-slate-50 border border-slate-200 rounded-xl font-bold font-mono text-base text-slate-900 focus:outline-none focus:ring-2 focus:ring-emerald-500">
                    </div>
                    <input type="range" id="rangeRate" min="0.5" max="8.0" step="0.05" value="3.50" oninput="syncFromRange('Rate')" class="w-full mt-2 accent-emerald-600 cursor-pointer">
                    <div class="grid grid-cols-4 gap-1 mt-1 text-[10px] font-bold no-print">
                        <button type="button" onclick="setVal('Rate', 2.50)" class="py-1 bg-slate-100 hover:bg-slate-200 rounded-lg text-slate-700 transition">2.5%</button>
                        <button type="button" onclick="setVal('Rate', 3.20)" class="py-1 bg-slate-100 hover:bg-slate-200 rounded-lg text-slate-700 transition">3.2%</button>
                        <button type="button" onclick="setVal('Rate', 3.80)" class="py-1 bg-slate-100 hover:bg-slate-200 rounded-lg text-slate-700 transition">3.8%</button>
                        <button type="button" onclick="setVal('Rate', 4.50)" class="py-1 bg-slate-100 hover:bg-slate-200 rounded-lg text-slate-700 transition">4.5%</button>
                    </div>
                </div>

                <!-- Somma da Versare per Estinzione Parziale -->
                <div class="pt-3 border-t-2 border-emerald-500/20 bg-emerald-50/40 -mx-4 -mb-4 p-4 rounded-b-2xl">
                    <div class="flex justify-between items-center mb-1">
                        <label class="text-xs font-black text-emerald-900 flex items-center gap-1">
                            <span>💰</span> Somma che Vuoi Versare (<span class="currencySymbol">€</span>)
                        </label>
                        <span id="badgePrepay" class="text-xs font-black font-mono text-white bg-emerald-700 px-2 py-0.5 rounded shadow-2xs">20.000 €</span>
                    </div>
                    <div class="relative">
                        <input type="number" id="inputPrepay" value="20000" min="1000" max="500000" step="1000" oninput="syncFromInput('Prepay')" class="w-full p-2.5 bg-white border-2 border-emerald-400 rounded-xl font-black font-mono text-base text-emerald-950 focus:outline-none focus:ring-2 focus:ring-emerald-600">
                    </div>
                    <input type="range" id="rangePrepay" min="1000" max="100000" step="1000" value="20000" oninput="syncFromRange('Prepay')" class="w-full mt-2 accent-emerald-700 cursor-pointer">
                    <div class="grid grid-cols-4 gap-1 mt-1 text-[10px] font-bold no-print">
                        <button type="button" onclick="setVal('Prepay', 5000)" class="py-1 bg-white hover:bg-emerald-100 border border-emerald-200 rounded-lg text-emerald-800 transition">5k</button>
                        <button type="button" onclick="setVal('Prepay', 10000)" class="py-1 bg-white hover:bg-emerald-100 border border-emerald-200 rounded-lg text-emerald-800 transition">10k</button>
                        <button type="button" onclick="setVal('Prepay', 20000)" class="py-1 bg-white hover:bg-emerald-100 border border-emerald-200 rounded-lg text-emerald-800 transition">20k</button>
                        <button type="button" onclick="setVal('Prepay', 40000)" class="py-1 bg-white hover:bg-emerald-100 border border-emerald-200 rounded-lg text-emerald-800 transition">40k</button>
                    </div>
                </div>

            </div>

            <!-- RESULTS & COMPARISON COLUMN (7 Cols) -->
            <div class="lg:col-span-7 space-y-4">
                
                <!-- Stato Attuale Pre-Estinzione -->
                <div class="bg-slate-900 text-white rounded-2xl p-4 shadow-lg border border-slate-800 flex flex-wrap items-center justify-between gap-3">
                    <div>
                        <span class="text-[10px] font-bold uppercase tracking-wider text-slate-400 block" id="labelCurRate">Rata Mensile Attuale</span>
                        <div class="text-2xl sm:text-3xl font-black font-mono tracking-tight text-white" id="valCurrentRate">869,94 €</div>
                        <span class="text-[11px] text-slate-400">su 240 mensilità residue</span>
                    </div>
                    <div class="text-right">
                        <span class="text-[10px] font-bold uppercase tracking-wider text-slate-400 block" id="labelCurInterest">Interessi Residui a Scadenza</span>
                        <div class="text-xl sm:text-2xl font-black font-mono text-rose-400" id="valCurrentInterest">58.785 €</div>
                        <span class="text-[11px] text-slate-400" id="valCurrentDebtSummary">Debito residuo: 150.000 €</span>
                    </div>
                </div>

                <!-- CONFRONTO DIRETTO A DUE CARDS (Opzione A vs Opzione B) -->
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                    
                    <!-- OPZIONE A: RIDUCI RATA -->
                    <div class="bg-white rounded-2xl p-4 sm:p-5 border-2 border-slate-200 shadow-xs space-y-3 relative overflow-hidden flex flex-col justify-between">
                        <div>
                            <div class="flex items-center justify-between pb-2 border-b border-slate-100">
                                <span class="text-xs font-black text-slate-900" id="optATitle">Opzione A: Riduci Rata</span>
                                <span class="text-[9px] uppercase font-extrabold px-1.5 py-0.5 rounded bg-blue-50 text-blue-700 border border-blue-200">Più Liquidità</span>
                            </div>
                            <p class="text-[11px] text-slate-500 mt-1" id="optASub">Mantiene la scadenza a 20 anni ma alleggerisce la spesa mensile.</p>
                            
                            <div class="mt-4 space-y-2">
                                <div>
                                    <span class="text-[10px] uppercase font-bold text-slate-400 block" id="optANewRateLabel">Nuova Rata Mensile</span>
                                    <span class="text-2xl font-black font-mono text-blue-700" id="valNewRateA">753,95 €</span>
                                </div>
                                <div class="p-2.5 rounded-xl bg-blue-50/70 border border-blue-100">
                                    <span class="text-[10px] font-bold text-blue-900 block" id="optAMonthSaveLabel">Risparmio Ogni Mese</span>
                                    <span class="text-base font-black font-mono text-blue-800" id="valMonthSavingA">+115,99 € / mese</span>
                                </div>
                            </div>
                        </div>

                        <div class="pt-3 border-t border-slate-100 mt-3">
                            <span class="text-[10px] uppercase font-bold text-slate-500 block" id="optATotSaveLabel">Interessi Totali Risparmiati</span>
                            <span class="text-xl font-black font-mono text-emerald-600" id="valTotSavingA">7.838 €</span>
                        </div>
                    </div>

                    <!-- OPZIONE B: RIDUCI DURATA -->
                    <div class="bg-white rounded-2xl p-4 sm:p-5 border-2 border-emerald-500 shadow-md space-y-3 relative overflow-hidden flex flex-col justify-between">
                        <div class="absolute top-0 right-0 bg-emerald-600 text-white text-[9px] font-black uppercase px-2 py-0.5 rounded-bl-lg tracking-wider">
                            Massimo Risparmio
                        </div>

                        <div>
                            <div class="flex items-center justify-between pb-2 border-b border-slate-100">
                                <span class="text-xs font-black text-emerald-950" id="optBTitle">Opzione B: Riduci Anni</span>
                            </div>
                            <p class="text-[11px] text-slate-500 mt-1" id="optBSub">Mantieni la rata a 869,94 € e cancelli il mutuo anni prima.</p>
                            
                            <div class="mt-4 space-y-2">
                                <div>
                                    <span class="text-[10px] uppercase font-bold text-slate-400 block" id="optBTimeSavedLabel">Tempo Risparmiato</span>
                                    <span class="text-2xl font-black font-mono text-emerald-700" id="valYearsSavedB">3 anni e 7 mesi</span>
                                </div>
                                <div class="p-2.5 rounded-xl bg-emerald-50/80 border border-emerald-200">
                                    <span class="text-[10px] font-bold text-emerald-900 block" id="optBNewDurLabel">Nuova Durata Residua</span>
                                    <span class="text-base font-black font-mono text-emerald-800" id="valNewDurationB">16 anni e 5 mesi</span>
                                </div>
                            </div>
                        </div>

                        <div class="pt-3 border-t border-slate-100 mt-3">
                            <span class="text-[10px] uppercase font-bold text-slate-500 block" id="optBTotSaveLabel">Interessi Totali Risparmiati</span>
                            <span class="text-2xl font-black font-mono text-emerald-600" id="valTotSavingB">17.797 €</span>
                        </div>
                    </div>

                </div>

                <!-- VERDETTO INTELLIGENTE & GRAFICO SVG -->
                <div class="bg-white rounded-2xl p-4 sm:p-5 border border-slate-200 shadow-xs space-y-3">
                    <h3 class="text-xs font-extrabold uppercase tracking-wide text-slate-700 flex items-center gap-1.5" id="verdictHeader">
                        <span>💡</span> <span id="verdictTitle">Quale opzione conviene di più?</span>
                    </h3>
                    <p class="text-xs sm:text-sm text-slate-600 leading-relaxed" id="verdictText">
                        L'<strong>Opzione B (Riduci Durata)</strong> ti fa risparmiare <strong><span id="diffSavings">9.959 €</span> di interessi in più</strong> rispetto all'Opzione A, perché abbatte gli anni di maturazione del capitale. Scegli l'<strong>Opzione A</strong> se il tuo obiettivo primario è avere <strong><span id="diffMonthly">116 €</span> al mese di liquidità extra</strong> in famiglia.
                    </p>

                    <!-- SVG Bar Chart Visualizer -->
                    <div class="mt-4 pt-3 border-t border-slate-100">
                        <span class="text-[10px] font-bold uppercase tracking-wider text-slate-400 block mb-2">Confronto Risparmio Interessi Totali</span>
                        <div class="space-y-2">
                            <div>
                                <div class="flex justify-between text-xs font-bold text-slate-700 mb-1">
                                    <span>Opzione A (Riduci Rata)</span>
                                    <span id="chartLabelA">7.838 €</span>
                                </div>
                                <div class="w-full bg-slate-100 rounded-full h-3.5 overflow-hidden">
                                    <div id="chartBarA" class="bg-blue-600 h-full rounded-full transition-all duration-500" style="width: 44%"></div>
                                </div>
                            </div>
                            <div>
                                <div class="flex justify-between text-xs font-bold text-emerald-800 mb-1">
                                    <span>Opzione B (Riduci Durata) — Top</span>
                                    <span id="chartLabelB">17.797 €</span>
                                </div>
                                <div class="w-full bg-slate-100 rounded-full h-3.5 overflow-hidden">
                                    <div id="chartBarB" class="bg-emerald-600 h-full rounded-full transition-all duration-500" style="width: 100%"></div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Export & Print Actions -->
                <div class="flex items-center justify-end gap-2 pt-1 no-print">
                    <button type="button" onclick="exportCsvComparison()" class="px-3 py-2 bg-emerald-50 hover:bg-emerald-100 text-emerald-800 border border-emerald-200 text-xs font-bold rounded-xl transition flex items-center gap-1.5 cursor-pointer">
                        <span>📊</span> <span id="btnCsvExport">Esporta Confronto CSV</span>
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
                    <span id="faqTitle">Domande Frequenti su Estinzione Anticipata Mutuo</span>
                </h2>
                <span class="text-[10px] font-extrabold uppercase px-2 py-0.5 rounded-full bg-slate-100 text-slate-600 border border-slate-200">FAQ</span>
            </div>
            
            <div id="faqContainer" class="space-y-3">
                <details class="group bg-slate-50/80 hover:bg-slate-50 rounded-xl border border-slate-200/80 p-4 transition duration-150">
                    <summary class="flex justify-between items-center font-bold text-xs sm:text-sm text-slate-900 cursor-pointer list-none select-none">
                        <span id="faq1Q">L'estinzione anticipata parziale del mutuo prevede penali o costi bancari?</span>
                        <svg class="w-4 h-4 text-slate-400 group-open:-rotate-180 transition-transform duration-200 shrink-0 ml-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/>
                        </svg>
                    </summary>
                    <div id="faq1A" class="text-xs sm:text-sm text-slate-600 mt-2.5 leading-relaxed border-t border-slate-200/60 pt-2.5">
                        No. In Italia, grazie al <strong>Decreto Bersani (Legge 40/2007)</strong>, per tutti i mutui stipulati o rinegoziati per l'acquisto o la ristrutturazione di immobili adibiti ad abitazione (prima casa o meno) o ad attività professionale, <strong>le penali di estinzione anticipata totale o parziale sono nulle per legge</strong>.
                    </div>
                </details>

                <details class="group bg-slate-50/80 hover:bg-slate-50 rounded-xl border border-slate-200/80 p-4 transition duration-150">
                    <summary class="flex justify-between items-center font-bold text-xs sm:text-sm text-slate-900 cursor-pointer list-none select-none">
                        <span id="faq2Q">Conviene di più abbassare la rata mensile o diminuire gli anni del mutuo?</span>
                        <svg class="w-4 h-4 text-slate-400 group-open:-rotate-180 transition-transform duration-200 shrink-0 ml-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/>
                        </svg>
                    </summary>
                    <div id="faq2A" class="text-xs sm:text-sm text-slate-600 mt-2.5 leading-relaxed border-t border-slate-200/60 pt-2.5">
                        Dal punto di vista puramente economico e matematico, <strong>ridurre gli anni del mutuo (durata) genera un risparmio di interessi molto più elevato</strong>. Tuttavia, se la famiglia desidera maggiore serenità mese per mese, ridurre la rata offre un beneficio immediato sulla liquidità mensile.
                    </div>
                </details>

                <details class="group bg-slate-50/80 hover:bg-slate-50 rounded-xl border border-slate-200/80 p-4 transition duration-150">
                    <summary class="flex justify-between items-center font-bold text-xs sm:text-sm text-slate-900 cursor-pointer list-none select-none">
                        <span id="faq3Q">Come viene ricalcolato l'ammortamento dopo un versamento anticipato?</span>
                        <svg class="w-4 h-4 text-slate-400 group-open:-rotate-180 transition-transform duration-200 shrink-0 ml-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/>
                        </svg>
                    </summary>
                    <div id="faq3A" class="text-xs sm:text-sm text-slate-600 mt-2.5 leading-relaxed border-t border-slate-200/60 pt-2.5">
                        La somma versata va ad abbattere direttamente il <strong>debito residuo in quota capitale</strong>. Da quel momento, gli interessi futuri verranno conteggiati dalla banca esclusivamente sul nuovo debito ridotto, ricalcolando la rata o la durata secondo la formula di ammortamento alla francese.
                    </div>
                </details>

                <details class="group bg-slate-50/80 hover:bg-slate-50 rounded-xl border border-slate-200/80 p-4 transition duration-150">
                    <summary class="flex justify-between items-center font-bold text-xs sm:text-sm text-slate-900 cursor-pointer list-none select-none">
                        <span id="faq4Q">Esiste un importo minimo obbligatorio per l'estinzione parziale?</span>
                        <svg class="w-4 h-4 text-slate-400 group-open:-rotate-180 transition-transform duration-200 shrink-0 ml-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/>
                        </svg>
                    </summary>
                    <div id="faq4A" class="text-xs sm:text-sm text-slate-600 mt-2.5 leading-relaxed border-t border-slate-200/60 pt-2.5">
                        La legge non impone una soglia minima, ma molti contratti di mutuo o regolamenti interni bancari indicano un importo minimo per singola richiesta (spesso 1.000 € o l'equivalente di una rata mensile). Non c'è limite al numero di versamenti anticipati eseguibili.
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
            setVal('CurrentDebt', 150000);
            setVal('YearsLeft', 20);
            setVal('Rate', 3.50);
            setVal('Prepay', 20000);
        }}

        function saveState() {{
            try {{
                const state = {{
                    debt: document.getElementById('inputCurrentDebt').value,
                    years: document.getElementById('inputYearsLeft').value,
                    rate: document.getElementById('inputRate').value,
                    prepay: document.getElementById('inputPrepay').value,
                    curr: currentCurrency
                }};
                localStorage.setItem('omni_estinzione_state', JSON.stringify(state));
            }} catch(e) {{}}
        }}

        function loadState() {{
            try {{
                const saved = localStorage.getItem('omni_estinzione_state');
                if (saved) {{
                    const s = JSON.parse(saved);
                    if (s.debt) setVal('CurrentDebt', s.debt);
                    if (s.years) setVal('YearsLeft', s.years);
                    if (s.rate) setVal('Rate', s.rate);
                    if (s.prepay) setVal('Prepay', s.prepay);
                    if (s.curr) setCurrency(s.curr);
                }}
            }} catch(e) {{}}
        }}

        function recalc() {{
            const C = parseFloat(document.getElementById('inputCurrentDebt').value) || 0;
            const yearsLeft = parseFloat(document.getElementById('inputYearsLeft').value) || 1;
            const tanAnnual = parseFloat(document.getElementById('inputRate').value) || 0.1;
            let E = parseFloat(document.getElementById('inputPrepay').value) || 0;

            if (E >= C) {{
                E = C - 1000;
                if (E < 0) E = 0;
                document.getElementById('inputPrepay').value = E;
                document.getElementById('rangePrepay').value = E;
            }}

            // Badges
            document.getElementById('badgeCurrentDebt').textContent = fmtCurr(C);
            const totalMonths = Math.round(yearsLeft * 12);
            document.getElementById('badgeYearsLeft').textContent = yearsLeft + ' anni (' + totalMonths + ' rate)';
            document.getElementById('badgeRate').textContent = tanAnnual.toFixed(2) + ' %';
            document.getElementById('badgePrepay').textContent = fmtCurr(E);

            const i = (tanAnnual / 100.0) / 12.0;
            const n = totalMonths;

            // Rata Attuale
            const R_cur = C * (i * Math.pow(1 + i, n)) / (Math.pow(1 + i, n) - 1);
            const totInterestCur = (R_cur * n) - C;

            const C_new = C - E;

            // Opzione A: Riduci Rata (stesso n)
            const R_new_A = C_new * (i * Math.pow(1 + i, n)) / (Math.pow(1 + i, n) - 1);
            const totInterest_A = (R_new_A * n) - C_new;
            const saving_A = totInterestCur - totInterest_A;
            const monthSaving_A = R_cur - R_new_A;

            // Opzione B: Riduci Durata (stesso R_cur)
            // n_new = -ln(1 - i*C_new / R_cur) / ln(1+i)
            let n_new = n;
            let val = 1 - (i * C_new / R_cur);
            if (val > 0) {{
                n_new = -Math.log(val) / Math.log(1 + i);
            }}
            const monthsSaved = Math.max(0, n - n_new);
            const yearsSaved = Math.floor(monthsSaved / 12);
            const remMonthsSaved = Math.round(monthsSaved % 12);
            
            const newYearsB = Math.floor(n_new / 12);
            const newMonthsB = Math.round(n_new % 12);

            const totInterest_B = (R_cur * n_new) - C_new;
            const saving_B = totInterestCur - totInterest_B;

            lastCalculation = {{
                C, yearsLeft, totalMonths, tanAnnual, E, C_new,
                R_cur, totInterestCur,
                R_new_A, totInterest_A, saving_A, monthSaving_A,
                n_new, monthsSaved, yearsSaved, remMonthsSaved,
                newYearsB, newMonthsB, totInterest_B, saving_B
            }};

            // Render current
            document.getElementById('valCurrentRate').textContent = fmtCurrDec(R_cur);
            document.getElementById('valCurrentInterest').textContent = fmtCurr(totInterestCur);
            document.getElementById('valCurrentDebtSummary').textContent = 'Debito residuo: ' + fmtCurr(C);

            // Render Opzione A
            document.getElementById('valNewRateA').textContent = fmtCurrDec(R_new_A);
            document.getElementById('valMonthSavingA').textContent = '+' + fmtCurrDec(monthSaving_A) + ' / mese';
            document.getElementById('valTotSavingA').textContent = fmtCurr(saving_A);

            // Render Opzione B
            let timeSavedStr = '';
            if (yearsSaved > 0) timeSavedStr += yearsSaved + ' anni ';
            if (remMonthsSaved > 0) timeSavedStr += 'e ' + remMonthsSaved + ' mesi';
            if (!timeSavedStr) timeSavedStr = 'Meno di 1 mese';
            document.getElementById('valYearsSavedB').textContent = timeSavedStr;

            let newDurStr = '';
            if (newYearsB > 0) newDurStr += newYearsB + ' anni ';
            if (newMonthsB > 0) newDurStr += 'e ' + newMonthsB + ' mesi';
            document.getElementById('valNewDurationB').textContent = newDurStr;

            document.getElementById('valTotSavingB').textContent = fmtCurr(saving_B);

            // Verdict & Differences
            const diffSave = Math.max(0, saving_B - saving_A);
            document.getElementById('diffSavings').textContent = fmtCurr(diffSave);
            document.getElementById('diffMonthly').textContent = fmtCurrDec(monthSaving_A);

            // Bar chart updates
            const maxSave = Math.max(saving_B, 1);
            const pctA = Math.max(5, Math.round((saving_A / maxSave) * 100));
            document.getElementById('chartLabelA').textContent = fmtCurr(saving_A);
            document.getElementById('chartBarA').style.width = pctA + '%';

            document.getElementById('chartLabelB').textContent = fmtCurr(saving_B);
            document.getElementById('chartBarB').style.width = '100%';
        }}

        function exportCsvComparison() {{
            if (!lastCalculation) return;
            const c = lastCalculation;
            let csv = "PARAMETRO;SITUAZIONE ATTUALE;OPZIONE A (RIDUCI RATA);OPZIONE B (RIDUCI ANNI)\\n";
            csv += `Debito Residuo;${{c.C.toFixed(2)}};${{c.C_new.toFixed(2)}};${{c.C_new.toFixed(2)}}\\n`;
            csv += `Quota Versata;0;${{c.E.toFixed(2)}};${{c.E.toFixed(2)}}\\n`;
            csv += `Rata Mensile;${{c.R_cur.toFixed(2)}};${{c.R_new_A.toFixed(2)}};${{c.R_cur.toFixed(2)}}\\n`;
            csv += `Durata Residua Mesi;${{c.totalMonths}};${{c.totalMonths}};${{Math.round(c.n_new)}}\\n`;
            csv += `Interessi Totali Futuri;${{c.totInterestCur.toFixed(2)}};${{c.totInterest_A.toFixed(2)}};${{c.totInterest_B.toFixed(2)}}\\n`;
            csv += `RISPARMIO INTERESSI NETTO;0;${{c.saving_A.toFixed(2)}};${{c.saving_B.toFixed(2)}}\\n`;

            const blob = new Blob([csv], {{ type: 'text/csv;charset=utf-8;' }});
            const url = URL.createObjectURL(blob);
            const link = document.createElement("a");
            link.setAttribute("href", url);
            link.setAttribute("download", `OmniTools_Estinzione_Mutuo_${{new Date().toISOString().slice(0,10)}}.csv`);
            document.body.appendChild(link);
            link.click();
            document.body.removeChild(link);
        }}

        function applyTranslations() {{
            const t = TRANSLATIONS[currentLang] || TRANSLATIONS['it'];
            document.getElementById('heroTitle').textContent = t.hero_title;
            document.getElementById('heroDesc').textContent = t.hero_desc;
            document.getElementById('labelCurRate').textContent = t.col_cur_rate;
            document.getElementById('labelCurInterest').textContent = t.col_interest_before;
            
            document.getElementById('optATitle').textContent = t.option_a_title;
            document.getElementById('optASub').textContent = t.option_a_subtitle;
            document.getElementById('optANewRateLabel').textContent = t.option_a_new_rate;
            document.getElementById('optAMonthSaveLabel').textContent = t.option_a_month_saving;
            document.getElementById('optATotSaveLabel').textContent = t.option_a_tot_saving;

            document.getElementById('optBTitle').textContent = t.option_b_title;
            document.getElementById('optBSub').textContent = t.option_b_subtitle;
            document.getElementById('optBTimeSavedLabel').textContent = t.option_b_time_saved;
            document.getElementById('optBNewDurLabel').textContent = t.option_b_new_duration;
            document.getElementById('optBTotSaveLabel').textContent = t.option_b_tot_saving;

            document.getElementById('verdictTitle').textContent = t.verdict_title;
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

        function switchLang(lang) {{
            if (!TRANSLATIONS[lang]) return;
            currentLang = lang;
            applyTranslations();
            recalc();
        }}

        document.addEventListener('DOMContentLoaded', () => {{
            loadState();
            recalc();
            applyTranslations();
        }});
    </script>
</body>
</html>
"""

out_path = os.path.join(base_dir, "estinzione.html")
with open(out_path, "w", encoding="utf-8") as f:
    f.write(html_code)

print(f"estinzione.html compiled successfully at: {out_path}")
