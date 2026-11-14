// OmniTools Lab Universal Help Drawer (Desktop Slide-over & Mobile Bottom Sheet)
(function() {
    // Determine tool identifier from URL
    const pathname = window.location.pathname.toLowerCase();
    let toolId = 'rampe';
    if (pathname.includes('scale') || pathname.includes('stair')) toolId = 'scale';
    else if (pathname.includes('tubi')) toolId = 'tubi';
    else if (pathname.includes('tetto')) toolId = 'tetto';
    else if (pathname.includes('taglio')) toolId = 'taglio';
    else if (pathname.includes('piastrelle')) toolId = 'piastrelle';
    else if (pathname.includes('dorso')) toolId = 'dorso';
    else if (pathname.includes('dpi')) toolId = 'dpi';
    else if (pathname.includes('tinta')) toolId = 'tinta';
    else if (pathname.includes('barcode')) toolId = 'barcode';
    else if (pathname.includes('copertura')) toolId = 'copertura';
    else if (pathname.includes('resa')) toolId = 'resa';
    else if (pathname.includes('mutuo')) toolId = 'mutuo';
    else if (pathname.includes('pac') || pathname.includes('compound')) toolId = 'pac';
    else if (pathname.includes('margine')) toolId = 'margine';
    else if (pathname.includes('estinzione')) toolId = 'estinzione';
    else if (pathname.includes('risparmio')) toolId = 'risparmio';
    else if (pathname.includes('fire')) toolId = 'fire';
    else if (pathname.includes('rampe')) toolId = 'rampe';

    const HELP_DATABASE = {
        rampe: {
            themeColor: 'amber',
            it: {
                btn: 'Guida',
                title: 'Guida Rapida — RampaFacile',
                subtitle: 'Formule, pendenze e norme disabili',
                faqBtn: '↓ Vai alle FAQ complete',
                closeBtn: 'Chiudi',
                html: `
                    <div class="space-y-2">
                        <h3 class="text-xs font-black uppercase tracking-wider text-amber-700">1. Come si usa in 3 passi</h3>
                        <ol class="list-decimal pl-4 space-y-1.5">
                            <li><strong>Scegli la modalità:</strong> <em>Calcola Pendenza</em> (conosci dislivello e spazio a terra) oppure <em>Calcola Spazio</em> (vuoi sapere quanti metri occorrono per una certa % di pendenza).</li>
                            <li><strong>Inserisci le misure:</strong> usa i cursori o digita i valori numerici.</li>
                            <li><strong>Leggi il verdetto:</strong> verifica la conformità automatica per disabili (D.M. 236/89) o carrabili.</li>
                        </ol>
                    </div>
                    <div class="p-3.5 rounded-2xl bg-amber-50 border border-amber-200 space-y-2">
                        <h3 class="text-xs font-black uppercase tracking-wider text-amber-900">2. Formule Matematiche</h3>
                        <div class="font-mono text-[11px] space-y-1 text-amber-950">
                            <div><strong>Pendenza %</strong> = (Dislivello / Spazio a Terra) × 100</div>
                            <div><strong>Angolo (°)</strong> = arctan(Dislivello / Spazio a Terra) × (180 / π)</div>
                            <div><strong>Lunghezza Rampa</strong> = √(Dislivello² + Spazio²)</div>
                        </div>
                    </div>
                    <div class="space-y-2">
                        <h3 class="text-xs font-black uppercase tracking-wider text-slate-900">3. Limiti Normativi (D.M. 236/89)</h3>
                        <ul class="space-y-1.5">
                            <li class="p-2.5 rounded-xl bg-emerald-50 border border-emerald-200 text-emerald-950">
                                <strong>♿ Disabili / Carrozzine:</strong> max <strong>8%</strong> (consigliato <strong>5% – 6%</strong>). Pianerottolo orizzontale ogni 10 metri.
                            </li>
                            <li class="p-2.5 rounded-xl bg-slate-50 border border-slate-200 text-slate-800">
                                <strong>🚗 Rampe Garage:</strong> standard <strong>15% – 20%</strong> con raccordi dolci.
                            </li>
                        </ul>
                    </div>
                `
            },
            en: {
                btn: 'Guide',
                title: 'Quick Guide — RampCalc',
                subtitle: 'Formulas, grades & ADA standards',
                faqBtn: '↓ Jump to full FAQ',
                closeBtn: 'Close',
                html: `
                    <div class="space-y-2">
                        <h3 class="text-xs font-black uppercase tracking-wider text-amber-700">1. How to use in 3 steps</h3>
                        <ol class="list-decimal pl-4 space-y-1.5">
                            <li><strong>Choose mode:</strong> <em>Calculate Slope</em> (from rise &amp; run) or <em>Calculate Run</em> (from rise &amp; target slope %).</li>
                            <li><strong>Enter dimensions:</strong> use sliders or type exact values in cm, m, inches, feet.</li>
                            <li><strong>Review compliance:</strong> check wheelchair / ADA and vehicle ramp standards instantly.</li>
                        </ol>
                    </div>
                    <div class="p-3.5 rounded-2xl bg-amber-50 border border-amber-200 space-y-2">
                        <h3 class="text-xs font-black uppercase tracking-wider text-amber-900">2. Core Formulas</h3>
                        <div class="font-mono text-[11px] space-y-1 text-amber-950">
                            <div><strong>Grade %</strong> = (Rise / Run) × 100</div>
                            <div><strong>Angle (°)</strong> = arctan(Rise / Run) × (180 / π)</div>
                            <div><strong>Ramp Length</strong> = √(Rise² + Run²)</div>
                        </div>
                    </div>
                    <div class="space-y-2">
                        <h3 class="text-xs font-black uppercase tracking-wider text-slate-900">3. Standard Limits</h3>
                        <ul class="space-y-1.5">
                            <li class="p-2.5 rounded-xl bg-emerald-50 border border-emerald-200 text-emerald-950">
                                <strong>♿ Wheelchair / ADA &amp; EU:</strong> max <strong>8.33%</strong> (1:12 slope); <strong>5% – 6%</strong> recommended.
                            </li>
                            <li class="p-2.5 rounded-xl bg-slate-50 border border-slate-200 text-slate-800">
                                <strong>🚗 Driveways:</strong> typical grade <strong>15% – 20%</strong> with smooth transitions.
                            </li>
                        </ul>
                    </div>
                `
            }
        },
        scale: {
            themeColor: 'amber',
            it: {
                btn: 'Guida',
                title: 'Guida Rapida — ScalaFacile',
                subtitle: 'Formula di Blondel & Ergonomia',
                faqBtn: '↓ Vai alle FAQ complete',
                closeBtn: 'Chiudi',
                html: `
                    <div class="space-y-2">
                        <h3 class="text-xs font-black uppercase tracking-wider text-amber-700">1. Come calcolare la scala</h3>
                        <ol class="list-decimal pl-4 space-y-1.5">
                            <li><strong>Inserisci il dislivello totale:</strong> misura dal pavimento finito inferiore a quello superiore.</li>
                            <li><strong>Scegli l\'alzata ideale:</strong> l\'algoritmo calcola in automatico il numero intero esatto di gradini.</li>
                            <li><strong>Verifica la pedata:</strong> applica la Legge di Blondel per garantire il passo naturale perfetto.</li>
                        </ol>
                    </div>
                    <div class="p-3.5 rounded-2xl bg-amber-50 border border-amber-200 space-y-2">
                        <h3 class="text-xs font-black uppercase tracking-wider text-amber-900">2. Legge di Blondel (Comfort Ergonomico)</h3>
                        <div class="font-mono text-[11px] space-y-1 text-amber-950">
                            <div><strong>2 Alzate (a) + 1 Pedata (p) = 62 ÷ 64 cm</strong></div>
                            <div>Rapporto ideale ottimale: <strong>63 cm</strong></div>
                            <div>Numero Gradini = Dislivello Totale / Alzata Desiderata</div>
                        </div>
                    </div>
                    <div class="space-y-2">
                        <h3 class="text-xs font-black uppercase tracking-wider text-slate-900">3. Standard Residenziali</h3>
                        <ul class="space-y-1.5">
                            <li class="p-2.5 rounded-xl bg-emerald-50 border border-emerald-200 text-emerald-950">
                                <strong>Alzata consigliata:</strong> tra <strong>16 e 17.5 cm</strong> (max 18 cm).
                            </li>
                            <li class="p-2.5 rounded-xl bg-slate-50 border border-slate-200 text-slate-800">
                                <strong>Pedata minima:</strong> non inferiore a <strong>28 cm</strong> (minimo di legge 25-26 cm).
                            </li>
                        </ul>
                    </div>
                `
            },
            en: {
                btn: 'Guide',
                title: 'Quick Guide — StairCalc',
                subtitle: 'Blondel\'s Law & Ergonomics',
                faqBtn: '↓ Jump to full FAQ',
                closeBtn: 'Close',
                html: `
                    <div class="space-y-2">
                        <h3 class="text-xs font-black uppercase tracking-wider text-amber-700">1. Step-by-step layout</h3>
                        <ol class="list-decimal pl-4 space-y-1.5">
                            <li><strong>Enter total rise:</strong> measure finished floor to finished upper floor.</li>
                            <li><strong>Target riser height:</strong> algorithm automatically determines the exact integer count of steps.</li>
                            <li><strong>Calculate tread run:</strong> uses Blondel's formula to guarantee effortless natural climbing.</li>
                        </ol>
                    </div>
                    <div class="p-3.5 rounded-2xl bg-amber-50 border border-amber-200 space-y-2">
                        <h3 class="text-xs font-black uppercase tracking-wider text-amber-900">2. Blondel\'s Ergonomic Law</h3>
                        <div class="font-mono text-[11px] space-y-1 text-amber-950">
                            <div><strong>2 × Riser + 1 × Tread = 62 to 64 cm (24.4 to 25.2 in)</strong></div>
                            <div>Optimal target: <strong>63 cm (24.8 in)</strong></div>
                            <div>Step Count = Total Rise / Target Riser Height</div>
                        </div>
                    </div>
                    <div class="space-y-2">
                        <h3 class="text-xs font-black uppercase tracking-wider text-slate-900">3. Standard Dimensions</h3>
                        <ul class="space-y-1.5">
                            <li class="p-2.5 rounded-xl bg-emerald-50 border border-emerald-200 text-emerald-950">
                                <strong>Riser height:</strong> <strong>16 to 17.5 cm (6.3 - 6.9 in)</strong> (max 7.75 in IRC code).
                            </li>
                            <li class="p-2.5 rounded-xl bg-slate-50 border border-slate-200 text-slate-800">
                                <strong>Tread run:</strong> recommended <strong>28 to 30 cm (11 in)</strong> (minimum 10 in).
                            </li>
                        </ul>
                    </div>
                `
            }
        },
        tubi: {
            themeColor: 'amber',
            it: {
                btn: 'Guida',
                title: 'Guida Rapida — ScaricoFacile',
                subtitle: 'Pendenze e Autopulizia UNI EN 12056',
                faqBtn: '↓ Vai alle FAQ complete',
                closeBtn: 'Chiudi',
                html: `
                    <div class="space-y-2">
                        <h3 class="text-xs font-black uppercase tracking-wider text-amber-700">1. Dimensionamento scarichi</h3>
                        <ol class="list-decimal pl-4 space-y-1.5">
                            <li><strong>Scegli diametro e tipo:</strong> acque nere, saponose o pluviali.</li>
                            <li><strong>Imposta la lunghezza della tratta:</strong> calcola pendenza minima e dislivello.</li>
                            <li><strong>Regola dell'autopulizia:</strong> velocità dell'acqua compresa tra 0.7 e 2.0 m/s.</li>
                        </ol>
                    </div>
                    <div class="p-3.5 rounded-2xl bg-amber-50 border border-amber-200 space-y-2">
                        <h3 class="text-xs font-black uppercase tracking-wider text-amber-900">2. Regola Pratica delle Pendenze</h3>
                        <div class="font-mono text-[11px] space-y-1 text-amber-950">
                            <div><strong>Pendenza consigliata:</strong> <strong>1.0% ÷ 2.0%</strong> (1 ÷ 2 cm per metro)</div>
                            <div>Sotto l'1%: rischio ristagno e sedimentazione solidi.</div>
                            <div>Sopra il 3%: l'acqua scorre troppo veloce lasciando indietro i solidi.</div>
                        </div>
                    </div>
                `
            },
            en: {
                btn: 'Guide',
                title: 'Quick Guide — PipeSlope',
                subtitle: 'Drainage Slope & Self-Cleansing Standards',
                faqBtn: '↓ Jump to full FAQ',
                closeBtn: 'Close',
                html: `
                    <div class="space-y-2">
                        <h3 class="text-xs font-black uppercase tracking-wider text-amber-700">1. Pipe Sizing</h3>
                        <ol class="list-decimal pl-4 space-y-1.5">
                            <li><strong>Select pipe diameter:</strong> wastewater, greywater, or stormwater.</li>
                            <li><strong>Set run length:</strong> calculate necessary elevation drop and grade.</li>
                            <li><strong>Self-cleansing velocity:</strong> keep flow speed between 0.7 and 2.0 m/s.</li>
                        </ol>
                    </div>
                    <div class="p-3.5 rounded-2xl bg-amber-50 border border-amber-200 space-y-2">
                        <h3 class="text-xs font-black uppercase tracking-wider text-amber-900">2. Recommended Slope Rules</h3>
                        <div class="font-mono text-[11px] space-y-1 text-amber-950">
                            <div><strong>Ideal Grade:</strong> <strong>1.0% to 2.0%</strong> (1/8 to 1/4 in per foot)</div>
                            <div>Under 1%: solid sedimentation risk and clogs.</div>
                            <div>Over 3%: liquid runs too fast separating from solids.</div>
                        </div>
                    </div>
                `
            }
        },
        tetto: {
            themeColor: 'amber',
            it: {
                btn: 'Guida',
                title: 'Guida Rapida — TettoFacile',
                subtitle: 'Pendenza Falda & Sviluppo Travi',
                faqBtn: '↓ Vai alle FAQ complete',
                closeBtn: 'Chiudi',
                html: `
                    <div class="space-y-2">
                        <h3 class="text-xs font-black uppercase tracking-wider text-amber-700">1. Calcolo Falda del Tetto</h3>
                        <ol class="list-decimal pl-4 space-y-1.5">
                            <li><strong>Inserisci larghezza base e altezza colmo</strong> oppure base e inclinazione desiderata in gradi / %.</li>
                            <li><strong>Verifica il manto:</strong> tegole marsigliesi (min 30%), coppi (min 35%), lamiere (min 10%).</li>
                            <li><strong>Calcola superficie reale:</strong> include l'inclinazione per computare guaine e isolanti.</li>
                        </ol>
                    </div>
                    <div class="p-3.5 rounded-2xl bg-amber-50 border border-amber-200 space-y-2">
                        <h3 class="text-xs font-black uppercase tracking-wider text-amber-900">2. Formule Geometria Falda</h3>
                        <div class="font-mono text-[11px] space-y-1 text-amber-950">
                            <div><strong>Pendenza %</strong> = (Altezza Colmo / Base) × 100</div>
                            <div><strong>Lunghezza Trave</strong> = √(Base² + Altezza²)</div>
                        </div>
                    </div>
                `
            },
            en: {
                btn: 'Guide',
                title: 'Quick Guide — RoofPitch',
                subtitle: 'Roof Pitch & Rafter Length',
                faqBtn: '↓ Jump to full FAQ',
                closeBtn: 'Close',
                html: `
                    <div class="space-y-2">
                        <h3 class="text-xs font-black uppercase tracking-wider text-amber-700">1. Pitch Calculation</h3>
                        <ol class="list-decimal pl-4 space-y-1.5">
                            <li><strong>Enter horizontal run and ridge rise</strong> or pitch ratio.</li>
                            <li><strong>Check material minimums:</strong> clay tile (30%+), shingles, metal roofing (10%+).</li>
                            <li><strong>True surface area:</strong> accounts for pitch angle to calculate underlayment accurately.</li>
                        </ol>
                    </div>
                    <div class="p-3.5 rounded-2xl bg-amber-50 border border-amber-200 space-y-2">
                        <h3 class="text-xs font-black uppercase tracking-wider text-amber-900">2. Roof Pitch Formulas</h3>
                        <div class="font-mono text-[11px] space-y-1 text-amber-950">
                            <div><strong>Slope %</strong> = (Rise / Run) × 100</div>
                            <div><strong>Rafter Length</strong> = √(Run² + Rise²)</div>
                        </div>
                    </div>
                `
            }
        },
        taglio: {
            themeColor: 'amber',
            it: {
                btn: 'Guida',
                title: 'Guida Rapida — TaglioOttimo',
                subtitle: 'Ottimizzatore Taglio Lineare 1D',
                faqBtn: '↓ Vai alle FAQ complete',
                closeBtn: 'Chiudi',
                html: `
                    <div class="space-y-2">
                        <h3 class="text-xs font-black uppercase tracking-wider text-amber-700">1. Ridurre lo sfrido a zero</h3>
                        <ol class="list-decimal pl-4 space-y-1.5">
                            <li><strong>Imposta la barra grezza:</strong> ad es. 600 cm o 1200 cm commerciale.</li>
                            <li><strong>Imposta spessore lama (kerf):</strong> 2-4 mm per considerare il materiale asportato dal disco.</li>
                            <li><strong>Aggiungi la distinta pezzi:</strong> l\'algoritmo bin-packing trova la combinazione a minimo scarto.</li>
                        </ol>
                    </div>
                `
            },
            en: {
                btn: 'Guide',
                title: 'Quick Guide — CutOptimizer',
                subtitle: '1D Linear Cut Optimization',
                faqBtn: '↓ Jump to full FAQ',
                closeBtn: 'Close',
                html: `
                    <div class="space-y-2">
                        <h3 class="text-xs font-black uppercase tracking-wider text-amber-700">1. Waste Reduction</h3>
                        <ol class="list-decimal pl-4 space-y-1.5">
                            <li><strong>Set stock bar length:</strong> e.g. 6000 mm or 20 ft standard bars.</li>
                            <li><strong>Set kerf blade width:</strong> 2 to 4 mm material loss per cut.</li>
                            <li><strong>Enter cut list:</strong> bin-packing algorithm computes optimal nesting pattern.</li>
                        </ol>
                    </div>
                `
            }
        },
        piastrelle: {
            themeColor: 'amber',
            it: {
                btn: 'Guida',
                title: 'Guida Rapida — PiastrellaFacile',
                subtitle: 'Calcolo Piastrelle, Colla e Fuga',
                faqBtn: '↓ Vai alle FAQ complete',
                closeBtn: 'Chiudi',
                html: `
                    <div class="space-y-2">
                        <h3 class="text-xs font-black uppercase tracking-wider text-amber-700">1. Computo Posa Pavimenti</h3>
                        <ol class="list-decimal pl-4 space-y-1.5">
                            <li><strong>Superficie e formato:</strong> misura la stanza e inserisci le dimensioni piastrella.</li>
                            <li><strong>Percentuale di sfrido:</strong> +10% per posa dritta, +15% per posa diagonale o sfalsata.</li>
                            <li><strong>Sacchi colla e stucco:</strong> calcolo automatico dei kg necessari in base alla larghezza fuga.</li>
                        </ol>
                    </div>
                `
            },
            en: {
                btn: 'Guide',
                title: 'Quick Guide — TileCalc',
                subtitle: 'Tile Area, Adhesive & Grout Estimator',
                faqBtn: '↓ Jump to full FAQ',
                closeBtn: 'Close',
                html: `
                    <div class="space-y-2">
                        <h3 class="text-xs font-black uppercase tracking-wider text-amber-700">1. Tile Flooring Estimation</h3>
                        <ol class="list-decimal pl-4 space-y-1.5">
                            <li><strong>Room Area & Format:</strong> measure dimensions and tile width/length.</li>
                            <li><strong>Waste Allowance:</strong> +10% for straight layout, +15% for diagonal or herringbone patterns.</li>
                            <li><strong>Mortar & Grout Bags:</strong> automatic consumption in kg based on joint width.</li>
                        </ol>
                    </div>
                `
            }
        },
        dorso: {
            themeColor: 'rose',
            it: {
                btn: 'Guida',
                title: 'Guida Rapida — DorsoFacile',
                subtitle: 'Calcolo Spessore Dorso Brossura',
                faqBtn: '↓ Vai alle FAQ complete',
                closeBtn: 'Chiudi',
                html: `
                    <div class="space-y-2">
                        <h3 class="text-xs font-black uppercase tracking-wider text-rose-700">1. Dimensionamento Copertina Libro</h3>
                        <ol class="list-decimal pl-4 space-y-1.5">
                            <li><strong>Pagine totali (facciate):</strong> inserisci il totale pagine del blocco libro.</li>
                            <li><strong>Grammatura e mano carta:</strong> spessore tipico carta usomano o patinata.</li>
                            <li><strong>Formula spessore:</strong> <code>Spessore = (Pagine / 2) × (Grammatura / 1000) × Mano</code>.</li>
                        </ol>
                    </div>
                `
            },
            en: {
                btn: 'Guide',
                title: 'Quick Guide — SpineCalc',
                subtitle: 'Book Spine Thickness Calculator',
                faqBtn: '↓ Jump to full FAQ',
                closeBtn: 'Close',
                html: `
                    <div class="space-y-2">
                        <h3 class="text-xs font-black uppercase tracking-wider text-rose-700">1. Perfect Binding Setup</h3>
                        <ol class="list-decimal pl-4 space-y-1.5">
                            <li><strong>Total page count:</strong> enter number of pages in text block.</li>
                            <li><strong>Paper weight & bulk:</strong> coated or uncoated paper stock thickness.</li>
                            <li><strong>Spine formula:</strong> <code>Thickness = (Pages / 2) × (GSM / 1000) × Bulk</code>.</li>
                        </ol>
                    </div>
                `
            }
        },
        dpi: {
            themeColor: 'rose',
            it: {
                btn: 'Guida',
                title: 'Guida Rapida — RisoluzioneFacile',
                subtitle: 'DPI, Pixel e Distanza di Visione',
                faqBtn: '↓ Vai alle FAQ complete',
                closeBtn: 'Chiudi',
                html: `
                    <div class="space-y-2">
                        <h3 class="text-xs font-black uppercase tracking-wider text-rose-700">1. Pixel e Risoluzione Stampa</h3>
                        <ol class="list-decimal pl-4 space-y-1.5">
                            <li><strong>Stampa ravvicinata (libri, volantini):</strong> standard <strong>300 DPI</strong>.</li>
                            <li><strong>Poster da parete (distanza 1 metro):</strong> bastano <strong>150 DPI</strong>.</li>
                            <li><strong>Manifesti e billboard (distanza 5+ metri):</strong> bastano <strong>30 ÷ 50 DPI</strong>.</li>
                        </ol>
                    </div>
                `
            },
            en: {
                btn: 'Guide',
                title: 'Quick Guide — ResolutionCalc',
                subtitle: 'DPI, Pixels & Visual Distance',
                faqBtn: '↓ Jump to full FAQ',
                closeBtn: 'Close',
                html: `
                    <div class="space-y-2">
                        <h3 class="text-xs font-black uppercase tracking-wider text-rose-700">1. Print Resolution Rules</h3>
                        <ol class="list-decimal pl-4 space-y-1.5">
                            <li><strong>Handheld prints (books, flyers):</strong> standard <strong>300 DPI</strong>.</li>
                            <li><strong>Wall posters (1 meter viewing):</strong> <strong>150 DPI</strong> is optimal.</li>
                            <li><strong>Billboards (5+ meters viewing):</strong> <strong>30 to 50 DPI</strong> is sufficient for the human eye.</li>
                        </ol>
                    </div>
                `
            }
        },
        tinta: {
            themeColor: 'rose',
            it: {
                btn: 'Guida',
                title: 'Guida Rapida — TintaPerfetta',
                subtitle: 'Matrici di Scarto Colore CMYK',
                faqBtn: '↓ Vai alle FAQ complete',
                closeBtn: 'Chiudi',
                html: `
                    <div class="space-y-2">
                        <h3 class="text-xs font-black uppercase tracking-wider text-rose-700">1. Centrare la Tinta al Primo Colpo</h3>
                        <p>Genera una griglia di variazioni cromatiche con scarto delta (±2%, ±5%) per stampare una prova colore e scegliere a occhio nudo il tono esatto su carta.</p>
                    </div>
                `
            },
            en: {
                btn: 'Guide',
                title: 'Quick Guide — ColorMatch',
                subtitle: 'CMYK Offset Variance Matrices',
                faqBtn: '↓ Jump to full FAQ',
                closeBtn: 'Close',
                html: `
                    <div class="space-y-2">
                        <h3 class="text-xs font-black uppercase tracking-wider text-rose-700">1. Exact Color Target</h3>
                        <p>Generates a calibration grid with percentage delta (±2%, ±5%) to print a proof sheet and choose the exact match directly on press.</p>
                    </div>
                `
            }
        },
        barcode: {
            themeColor: 'rose',
            it: {
                btn: 'Guida',
                title: 'Guida Rapida — OmniBarcode',
                subtitle: 'Generatori Codici a Barre GS1',
                faqBtn: '↓ Vai alle FAQ complete',
                closeBtn: 'Chiudi',
                html: `
                    <div class="space-y-2">
                        <h3 class="text-xs font-black uppercase tracking-wider text-rose-700">1. Tipi di Codici Supportati</h3>
                        <ul class="space-y-1.5">
                            <li><strong>EAN-13:</strong> per prodotti commerciali al dettaglio (GS1 standard con checksum).</li>
                            <li><strong>Code 128:</strong> per logistica e spedizioni alfanumeriche.</li>
                            <li><strong>Code 39:</strong> per Tessere Sanitarie e cartellini tecnici.</li>
                        </ul>
                    </div>
                `
            },
            en: {
                btn: 'Guide',
                title: 'Quick Guide — BarcodeGen',
                subtitle: 'GS1 Compliant Barcode Generator',
                faqBtn: '↓ Jump to full FAQ',
                closeBtn: 'Close',
                html: `
                    <div class="space-y-2">
                        <h3 class="text-xs font-black uppercase tracking-wider text-rose-700">1. Supported Standards</h3>
                        <ul class="space-y-1.5">
                            <li><strong>EAN-13:</strong> standard retail product barcode with modulo 10 checksum.</li>
                            <li><strong>Code 128:</strong> high-density logistics and alphanumeric labeling.</li>
                            <li><strong>Code 39:</strong> healthcare ID cards and inventory badges.</li>
                        </ul>
                    </div>
                `
            }
        },
        copertura: {
            themeColor: 'rose',
            it: {
                btn: 'Guida',
                title: 'Guida Rapida — CoperturaFacile',
                subtitle: 'Copertura Inchiostro CMYK & TAC',
                faqBtn: '↓ Vai alle FAQ complete',
                closeBtn: 'Chiudi',
                html: `
                    <div class="space-y-2">
                        <h3 class="text-xs font-black uppercase tracking-wider text-rose-700">1. Controllo TAC (Total Area Coverage)</h3>
                        <p>Verifica che la somma dei 4 inchiostri non superi il limite massimo della carta (standard ISO 12647-2: <strong>300% per patinata</strong>, <strong>260% per usomano</strong>) per evitare macchie e mancata asciugatura.</p>
                    </div>
                `
            },
            en: {
                btn: 'Guide',
                title: 'Quick Guide — InkCoverage',
                subtitle: 'CMYK Ink Usage & TAC Analysis',
                faqBtn: '↓ Jump to full FAQ',
                closeBtn: 'Close',
                html: `
                    <div class="space-y-2">
                        <h3 class="text-xs font-black uppercase tracking-wider text-rose-700">1. TAC Limits (ISO 12647-2)</h3>
                        <p>Ensures total ink density does not exceed press limits (<strong>300% for coated paper</strong>, <strong>260% for uncoated paper</strong>) preventing set-off and smearing.</p>
                    </div>
                `
            }
        },
        resa: {
            themeColor: 'rose',
            it: {
                btn: 'Guida',
                title: 'Guida Rapida — ResaCarta',
                subtitle: 'Imposizione Posa su Fogli Macchina',
                faqBtn: '↓ Vai alle FAQ complete',
                closeBtn: 'Chiudi',
                html: `
                    <div class="space-y-2">
                        <h3 class="text-xs font-black uppercase tracking-wider text-rose-700">1. Calcolo Poses su 70x100 / 64x88</h3>
                        <p>Ottimizza il numero di tagli utili per foglio steso considerando refili, pinza macchina e verso di fibra della carta.</p>
                    </div>
                `
            },
            en: {
                btn: 'Guide',
                title: 'Quick Guide — SheetYield',
                subtitle: 'Sheet Imposition & Cutting Layout',
                faqBtn: '↓ Jump to full FAQ',
                closeBtn: 'Close',
                html: `
                    <div class="space-y-2">
                        <h3 class="text-xs font-black uppercase tracking-wider text-rose-700">1. Press Sheet Layout</h3>
                        <p>Optimizes total cuts per sheet across standard 70x100, 64x88, and SRA3 stock considering gripper margins and grain direction.</p>
                    </div>
                `
            }
        },
        mutuo: {
            themeColor: 'emerald',
            it: {
                btn: 'Guida',
                title: 'Guida Rapida — MutuoFacile',
                subtitle: 'Ammortamento Francese a Rata Costante',
                faqBtn: '↓ Vai alle FAQ complete',
                closeBtn: 'Chiudi',
                html: `
                    <div class="space-y-2">
                        <h3 class="text-xs font-black uppercase tracking-wider text-emerald-700">1. Come funziona il piano ammortamento</h3>
                        <ol class="list-decimal pl-4 space-y-1.5">
                            <li><strong>Rata costante:</strong> la quota mensile rimane fissa nel tempo.</li>
                            <li><strong>Quota interessi decrescente:</strong> all\'inizio paghi prevalentemente interessi, verso la fine quasi solo capitale.</li>
                            <li><strong>Sostenibilità bancaria:</strong> la rata non dovrebbe superare il <strong>33% del reddito netto mensile</strong> del nucleo familiare.</li>
                        </ol>
                    </div>
                `
            },
            en: {
                btn: 'Guide',
                title: 'Quick Guide — MortgageCalc',
                subtitle: 'Fixed-Rate French Amortization',
                faqBtn: '↓ Jump to full FAQ',
                closeBtn: 'Close',
                html: `
                    <div class="space-y-2">
                        <h3 class="text-xs font-black uppercase tracking-wider text-emerald-700">1. How Amortization Works</h3>
                        <ol class="list-decimal pl-4 space-y-1.5">
                            <li><strong>Fixed monthly payment:</strong> payment remains identical over time.</li>
                            <li><strong>Declining interest:</strong> front-loaded interest early on; capital repayment increases towards maturity.</li>
                            <li><strong>Debt-to-income ratio:</strong> banks typically recommend keeping housing payments under <strong>33% of net monthly income</strong>.</li>
                        </ol>
                    </div>
                `
            }
        },
        pac: {
            themeColor: 'emerald',
            it: {
                btn: 'Guida',
                title: 'Guida Rapida — InteresseComposto',
                subtitle: 'Piano di Accumulo (PAC) & Rendimento',
                faqBtn: '↓ Vai alle FAQ complete',
                closeBtn: 'Chiudi',
                html: `
                    <div class="space-y-2">
                        <h3 class="text-xs font-black uppercase tracking-wider text-emerald-700">1. La Formula della Crescita Esponenziale</h3>
                        <div class="font-mono text-[11px] p-2.5 rounded-xl bg-emerald-50 border border-emerald-200 text-emerald-950">
                            <strong>Montante = C × (1 + r)^t</strong>
                        </div>
                        <p>I guadagni generati ogni anno vengono reinvestiti, producendo a loro volta nuovi interessi e creando una crescita esponenziale nel lungo periodo (10-20+ anni).</p>
                    </div>
                `
            },
            en: {
                btn: 'Guide',
                title: 'Quick Guide — CompoundInterest',
                subtitle: 'DCA Investment & Compounding Growth',
                faqBtn: '↓ Jump to full FAQ',
                closeBtn: 'Close',
                html: `
                    <div class="space-y-2">
                        <h3 class="text-xs font-black uppercase tracking-wider text-emerald-700">1. Exponential Wealth Formula</h3>
                        <div class="font-mono text-[11px] p-2.5 rounded-xl bg-emerald-50 border border-emerald-200 text-emerald-950">
                            <strong>Future Value = P × (1 + r)^t</strong>
                        </div>
                        <p>Reinvested returns generate additional returns, compounding exponentially over 10 to 20+ year horizons.</p>
                    </div>
                `
            }
        },
        margine: {
            themeColor: 'emerald',
            it: {
                btn: 'Guida',
                title: 'Guida Rapida — MargineFacile',
                subtitle: 'Margine di Profitto vs Ricarico (Markup)',
                faqBtn: '↓ Vai alle FAQ complete',
                closeBtn: 'Chiudi',
                html: `
                    <div class="space-y-2">
                        <h3 class="text-xs font-black uppercase tracking-wider text-emerald-700">1. La Differenza Fondamentale</h3>
                        <ul class="space-y-1.5">
                            <li class="p-2.5 rounded-xl bg-slate-50 border border-slate-200">
                                <strong>Ricarico (Markup):</strong> quanto aggiungi sopra al costo d'acquisto. <code>(Prezzo - Costo) / Costo</code>.
                            </li>
                            <li class="p-2.5 rounded-xl bg-emerald-50 border border-emerald-200 text-emerald-950">
                                <strong>Margine di Profitto:</strong> la percentuale di utile che resta dal prezzo finale. <code>(Prezzo - Costo) / Prezzo</code>.
                            </li>
                        </ul>
                    </div>
                `
            },
            en: {
                btn: 'Guide',
                title: 'Quick Guide — MarginCalc',
                subtitle: 'Profit Margin vs Markup Pricing',
                faqBtn: '↓ Jump to full FAQ',
                closeBtn: 'Close',
                html: `
                    <div class="space-y-2">
                        <h3 class="text-xs font-black uppercase tracking-wider text-emerald-700">1. Key Difference</h3>
                        <ul class="space-y-1.5">
                            <li class="p-2.5 rounded-xl bg-slate-50 border border-slate-200">
                                <strong>Markup:</strong> added percentage on top of unit cost. <code>(Price - Cost) / Cost</code>.
                            </li>
                            <li class="p-2.5 rounded-xl bg-emerald-50 border border-emerald-200 text-emerald-950">
                                <strong>Profit Margin:</strong> profit share kept from total revenue. <code>(Price - Cost) / Price</code>.
                            </li>
                        </ul>
                    </div>
                `
            }
        },
        estinzione: {
            themeColor: 'emerald',
            it: {
                btn: 'Guida',
                title: 'Guida Rapida — EstinzioneAnticipata',
                subtitle: 'Riduzione Durata vs Riduzione Rata',
                faqBtn: '↓ Vai alle FAQ complete',
                closeBtn: 'Chiudi',
                html: `
                    <div class="space-y-2">
                        <h3 class="text-xs font-black uppercase tracking-wider text-emerald-700">1. Quale opzione conviene?</h3>
                        <ol class="list-decimal pl-4 space-y-1.5">
                            <li><strong>Riduzione Durata (Consigliata per risparmio max):</strong> mantieni la stessa rata ma tagli anni di mutuo, azzerando gli interessi degli ultimi anni.</li>
                            <li><strong>Riduzione Rata:</strong> abbassi l'esborso mensile per avere più respiro e liquidità subito.</li>
                            <li><strong>Legge Bersani (L. 40/2007):</strong> zero penali per estinzione anticipata su prima casa.</li>
                        </ol>
                    </div>
                `
            },
            en: {
                btn: 'Guide',
                title: 'Quick Guide — PrepaymentCalc',
                subtitle: 'Mortgage Prepayment & Term Shortening',
                faqBtn: '↓ Jump to full FAQ',
                closeBtn: 'Close',
                html: `
                    <div class="space-y-2">
                        <h3 class="text-xs font-black uppercase tracking-wider text-emerald-700">1. Prepayment Strategies</h3>
                        <ol class="list-decimal pl-4 space-y-1.5">
                            <li><strong>Shorten Term (Max interest savings):</strong> keep payment steady while cutting total years off your loan.</li>
                            <li><strong>Lower Monthly Payment:</strong> decreases monthly debt burden for immediate cash flow.</li>
                        </ol>
                    </div>
                `
            }
        },
        risparmio: {
            themeColor: 'emerald',
            it: {
                btn: 'Guida',
                title: 'Guida Rapida — ObiettivoRisparmio',
                subtitle: 'Pianificazione Sinking Fund',
                faqBtn: '↓ Vai alle FAQ complete',
                closeBtn: 'Chiudi',
                html: `
                    <div class="space-y-2">
                        <h3 class="text-xs font-black uppercase tracking-wider text-emerald-700">1. Raggiungere un Traguardo Finanziario</h3>
                        <p>Calcola la quota esatta da accantonare ogni mese (es. per anticipo casa, auto, fondo emergenza o viaggi) con o senza rendimento da conto deposito.</p>
                    </div>
                `
            },
            en: {
                btn: 'Guide',
                title: 'Quick Guide — SavingsGoal',
                subtitle: 'Sinking Fund Target Planning',
                faqBtn: '↓ Jump to full FAQ',
                closeBtn: 'Close',
                html: `
                    <div class="space-y-2">
                        <h3 class="text-xs font-black uppercase tracking-wider text-emerald-700">1. Systematic Savings Goal</h3>
                        <p>Computes the exact monthly deposit needed to reach a targeted capital threshold (home downpayment, car, emergency buffer).</p>
                    </div>
                `
            }
        },
        fire: {
            themeColor: 'emerald',
            it: {
                btn: 'Guida',
                title: 'Guida Rapida — Calcolatore FIRE',
                subtitle: 'Indipendenza Finanziaria & Regola del 4%',
                faqBtn: '↓ Vai alle FAQ complete',
                closeBtn: 'Chiudi',
                html: `
                    <div class="space-y-2">
                        <h3 class="text-xs font-black uppercase tracking-wider text-emerald-700">1. Il Numero FIRE (Trinity Study)</h3>
                        <div class="font-mono text-[11px] p-2.5 rounded-xl bg-emerald-50 border border-emerald-200 text-emerald-950">
                            <strong>Capitale FIRE = Spese Annue × 25</strong>
                        </div>
                        <p>Prelevando il 4% all'anno dal portafoglio investito (Safe Withdrawal Rate), il capitale ha oltre il 95% di probabilità di non esaurirsi mai per oltre 30 anni.</p>
                    </div>
                `
            },
            en: {
                btn: 'Guide',
                title: 'Quick Guide — FIRECalculator',
                subtitle: 'Financial Independence & 4% Rule',
                faqBtn: '↓ Jump to full FAQ',
                closeBtn: 'Close',
                html: `
                    <div class="space-y-2">
                        <h3 class="text-xs font-black uppercase tracking-wider text-emerald-700">1. The FIRE Target Number</h3>
                        <div class="font-mono text-[11px] p-2.5 rounded-xl bg-emerald-50 border border-emerald-200 text-emerald-950">
                            <strong>FIRE Portfolio = Annual Expenses × 25</strong>
                        </div>
                        <p>With a 4% Safe Withdrawal Rate (Trinity Study), a diversified portfolio has a 95%+ probability of lasting 30+ years without depletion.</p>
                    </div>
                `
            }
        }
    };

    function initHelpDrawer() {
        if (document.getElementById('omniHelpDrawer')) return;

        // Build DOM elements
        const backdrop = document.createElement('div');
        backdrop.id = 'omniHelpBackdrop';
        backdrop.onclick = closeHelpDrawer;
        backdrop.className = 'no-print fixed inset-0 bg-slate-900/50 backdrop-blur-xs z-50 hidden opacity-0 transition-opacity duration-200';

        const drawer = document.createElement('aside');
        drawer.id = 'omniHelpDrawer';
        drawer.setAttribute('role', 'dialog');
        drawer.setAttribute('aria-modal', 'true');
        drawer.setAttribute('aria-labelledby', 'helpDrawerTitle');
        drawer.className = 'no-print fixed z-50 bg-white border-slate-200 shadow-2xl transition-transform duration-300 ease-out flex flex-col bottom-0 left-0 right-0 max-h-[85vh] rounded-t-3xl border-t translate-y-full sm:top-0 sm:bottom-0 sm:left-auto sm:right-0 sm:h-full sm:max-h-full sm:w-full sm:max-w-md sm:rounded-none sm:rounded-l-3xl sm:border-t-0 sm:border-l sm:translate-y-0 sm:translate-x-full';

        drawer.innerHTML = `
            <div id="helpDragHandle" class="sm:hidden flex justify-center pt-3 pb-1 cursor-grab active:cursor-grabbing shrink-0">
                <span class="w-10 h-1.5 rounded-full bg-slate-300"></span>
            </div>
            <div class="flex items-center justify-between px-5 py-3.5 sm:py-4 border-b border-slate-200 shrink-0">
                <div class="flex items-center gap-2.5 min-w-0">
                    <span id="helpDrawerIconWrap" class="w-8 h-8 rounded-xl bg-amber-500/15 text-amber-700 border border-amber-500/25 flex items-center justify-center shrink-0">
                        <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"></path><line x1="12" y1="17" x2="12.01" y2="17"></line></svg>
                    </span>
                    <div class="min-w-0">
                        <h2 id="helpDrawerTitle" class="text-sm sm:text-base font-black text-slate-900 truncate">Guida Rapida</h2>
                        <p id="helpDrawerSubtitle" class="text-[11px] text-slate-500 truncate">Formule e istruzioni</p>
                    </div>
                </div>
                <button type="button" onclick="closeHelpDrawer()" aria-label="Chiudi guida" class="w-8 h-8 rounded-xl bg-slate-100 hover:bg-slate-200 text-slate-600 flex items-center justify-center text-sm font-bold transition cursor-pointer shrink-0">✕</button>
            </div>
            <div id="helpDrawerBody" class="p-5 overflow-y-auto space-y-5 text-xs sm:text-[13px] text-slate-600 leading-relaxed flex-1"></div>
            <div class="px-5 py-3 border-t border-slate-200 bg-slate-50 flex items-center justify-between gap-2 shrink-0 rounded-b-none sm:rounded-bl-3xl">
                <button type="button" onclick="scrollToFaqFromHelp()" id="helpScrollFaqBtn" class="text-xs font-bold text-amber-700 hover:text-amber-800 inline-flex items-center gap-1 cursor-pointer">
                    <span>↓ Vai alle FAQ complete</span>
                </button>
                <button type="button" onclick="closeHelpDrawer()" id="helpCloseFooterBtn" class="px-3.5 py-1.5 rounded-xl bg-slate-900 hover:bg-slate-800 text-white text-xs font-bold transition cursor-pointer">Chiudi</button>
            </div>
        `;

        document.body.appendChild(backdrop);
        document.body.appendChild(drawer);

        // Mobile Drag Handle Swipe Down
        const handle = document.getElementById('helpDragHandle');
        if (handle) {
            let startY = 0;
            handle.addEventListener('touchstart', (e) => { startY = e.touches[0].clientY; }, { passive: true });
            handle.addEventListener('touchend', (e) => {
                if (e.changedTouches[0].clientY - startY > 50) closeHelpDrawer();
            }, { passive: true });
        }

        // Keyboard ESC
        document.addEventListener('keydown', (e) => { if (e.key === 'Escape') closeHelpDrawer(); });

        // Insert Header Help Button if missing
        insertHeaderHelpButton();
        syncHelpDrawerLang();
    }

    function insertHeaderHelpButton() {
        if (document.getElementById('headerHelpBtn')) return;
        const installBtn = document.getElementById('headerInstallBtn');
        if (!installBtn || !installBtn.parentNode) return;

        const helpBtn = document.createElement('button');
        helpBtn.type = 'button';
        helpBtn.id = 'headerHelpBtn';
        helpBtn.onclick = openHelpDrawer;
        helpBtn.className = 'no-print inline-flex items-center justify-center gap-1 h-8 w-8 sm:w-auto px-1.5 sm:px-2.5 text-xs font-bold text-amber-800 bg-amber-50 hover:bg-amber-100 active:scale-95 rounded-xl border border-amber-200 transition shadow-2xs cursor-pointer';
        helpBtn.title = 'Guida & Formule';
        helpBtn.innerHTML = `
            <svg class="w-4 h-4 shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"></path><line x1="12" y1="17" x2="12.01" y2="17"></line></svg>
            <span id="headerHelpText" class="hidden sm:inline text-[11px]">Guida</span>
        `;
        installBtn.parentNode.insertBefore(helpBtn, installBtn);
    }

    function getActiveHelpLang() {
        const sel = document.getElementById('langSelect');
        const lang = (sel && sel.value) || localStorage.getItem('omnitools_lang') || 'it';
        return lang === 'it' ? 'it' : 'en';
    }

    window.syncHelpDrawerLang = function() {
        const item = HELP_DATABASE[toolId] || HELP_DATABASE['rampe'];
        const data = item[getActiveHelpLang()] || item['it'];
        const btnText = document.getElementById('headerHelpText');
        const titleEl = document.getElementById('helpDrawerTitle');
        const subEl = document.getElementById('helpDrawerSubtitle');
        const bodyEl = document.getElementById('helpDrawerBody');
        const faqBtn = document.getElementById('helpScrollFaqBtn');
        const closeBtn = document.getElementById('helpCloseFooterBtn');

        if (btnText) btnText.textContent = data.btn;
        if (titleEl) titleEl.textContent = data.title;
        if (subEl) subEl.textContent = data.subtitle;
        if (bodyEl) bodyEl.innerHTML = data.html;
        if (faqBtn) faqBtn.innerHTML = '<span>' + data.faqBtn + '</span>';
        if (closeBtn) closeBtn.textContent = data.closeBtn;
    };

    window.openHelpDrawer = function() {
        syncHelpDrawerLang();
        const backdrop = document.getElementById('omniHelpBackdrop');
        const drawer = document.getElementById('omniHelpDrawer');
        if (!backdrop || !drawer) return;
        backdrop.classList.remove('hidden');
        requestAnimationFrame(() => {
            backdrop.classList.remove('opacity-0');
            drawer.classList.remove('translate-y-full', 'sm:translate-x-full');
        });
        document.body.style.overflow = 'hidden';
    };

    window.closeHelpDrawer = function() {
        const backdrop = document.getElementById('omniHelpBackdrop');
        const drawer = document.getElementById('omniHelpDrawer');
        if (!backdrop || !drawer) return;
        backdrop.classList.add('opacity-0');
        drawer.classList.add('translate-y-full', 'sm:translate-x-full');
        setTimeout(() => {
            backdrop.classList.add('hidden');
            document.body.style.overflow = '';
        }, 250);
    };

    window.scrollToFaqFromHelp = function() {
        closeHelpDrawer();
        setTimeout(() => {
            const faq = document.getElementById('faqSection') || document.getElementById('faqContainer');
            if (faq) faq.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }, 260);
    };

    window.addEventListener('omnitools_lang_changed', syncHelpDrawerLang);
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initHelpDrawer);
    } else {
        initHelpDrawer();
    }
})();
