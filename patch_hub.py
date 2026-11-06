with open('/Users/ilalu/Documents/Altenative Businnes/Calcolatore_Pendenza/build_hub_i18n.py', 'r', encoding='utf-8') as f:
    c = f.read()

# 1. Update tab counts
c = c.replace('<span class="sm:hidden font-black text-[11px] block text-white">Tutti (7)</span>', '<span class="sm:hidden font-black text-[11px] block text-white">Tutti (8)</span>')
c = c.replace('<span class="subtext text-[10px] text-blue-100 font-semibold hidden sm:block">7 Strumenti</span>', '<span class="subtext text-[10px] text-blue-100 font-semibold hidden sm:block">8 Strumenti</span>')
c = c.replace('<span class="sm:hidden font-black text-[11px] block text-current">Graph (4)</span>', '<span class="sm:hidden font-black text-[11px] block text-current">Graph (5)</span>')
c = c.replace('<span class="subtext text-[10px] text-slate-500 font-semibold hidden sm:block">4 Grafica & Stampa</span>', '<span class="subtext text-[10px] text-slate-500 font-semibold hidden sm:block">5 Grafica & Stampa</span>')
c = c.replace('<span class="text-xs font-mono font-bold text-rose-900 bg-rose-50 px-2.5 py-1 rounded-xl border border-rose-200 hidden sm:inline-block">4 Tool Attivi</span>', '<span class="text-xs font-mono font-bold text-rose-900 bg-rose-50 px-2.5 py-1 rounded-xl border border-rose-200 hidden sm:inline-block">5 Tool Attivi</span>')

# 2. Add CoperturaFacile card after Barcode
target_barcode_end = """                        <!-- Big Action CTA Button -->
                        <div class="pt-3 border-t border-slate-100">
                            <div class="w-full py-2 px-3 rounded-xl bg-indigo-50 group-hover:bg-indigo-600 text-indigo-800 group-hover:text-white font-bold text-xs flex items-center justify-between transition-colors shadow-2xs">
                                <span id="toolBarcodeCta">Genera Codice a Barre</span>
                                <span class="group-hover:translate-x-1 transition-transform">➔</span>
                            </div>
                        </div>
                    </a>"""

copertura_card = """                        <!-- Big Action CTA Button -->
                        <div class="pt-3 border-t border-slate-100">
                            <div class="w-full py-2 px-3 rounded-xl bg-indigo-50 group-hover:bg-indigo-600 text-indigo-800 group-hover:text-white font-bold text-xs flex items-center justify-between transition-colors shadow-2xs">
                                <span id="toolBarcodeCta">Genera Codice a Barre</span>
                                <span class="group-hover:translate-x-1 transition-transform">➔</span>
                            </div>
                        </div>
                    </a>

                    <!-- TOOL 8: CoperturaFacile -->
                    <a href="/copertura" class="tool-card group relative bg-white hover:bg-rose-50/20 rounded-3xl p-5 border-2 border-slate-200/90 hover:border-rose-700 shadow-xs hover:shadow-xl hover:-translate-y-1 transition-all duration-200 flex flex-col justify-between space-y-4" data-tags="copertura inchiostro cmyk tac total area coverage costo copia stampa preventivo quadricromia densitometria rip">
                        <div class="space-y-3">
                            <!-- Visual Header & Micro Blueprint -->
                            <div class="flex items-center justify-between">
                                <div class="w-12 h-12 rounded-2xl bg-gradient-to-br from-rose-800 to-rose-950 text-white flex items-center justify-center shadow-md shadow-rose-900/25 p-2">
                                    <svg class="w-full h-full" viewBox="0 0 32 32" fill="none" stroke="currentColor">
                                        <rect x="4" y="6" width="24" height="20" rx="4" fill="#881337" />
                                        <circle cx="11" cy="13" r="3" fill="#22d3ee" />
                                        <circle cx="21" cy="13" r="3" fill="#ec4899" />
                                        <circle cx="16" cy="20" r="3" fill="#facc15" />
                                    </svg>
                                </div>
                                <span class="text-[10px] font-extrabold uppercase px-2 py-0.5 rounded-full bg-rose-50 text-rose-800 border border-rose-200" id="toolCoperturaBadge">CMYK & Costo Copia</span>
                            </div>

                            <!-- Title & Direct Question Hook -->
                            <div>
                                <h3 id="toolCoperturaTitle" class="text-base sm:text-lg font-black text-slate-900 group-hover:text-rose-700 transition">CoperturaFacile</h3>
                                <div id="toolCoperturaHook" class="text-xs font-bold text-rose-800 mt-0.5">Quanto inchiostro consumerà la commessa?</div>
                            </div>

                            <!-- Plain Description -->
                            <p id="toolCoperturaDesc" class="text-xs text-slate-600 leading-relaxed">
                                Analisi densitometrica CMYK e TAC (Total Area Coverage) in tempo reale. Calcola il consumo in grammi e il costo copia con privacy totale.
                            </p>

                            <!-- Feature Tags -->
                            <div class="flex flex-wrap gap-1 pt-1 text-[10px] font-bold text-slate-500">
                                <span class="px-2 py-0.5 bg-slate-100 rounded-md">📊 Separazione CMYK</span>
                                <span class="px-2 py-0.5 bg-slate-100 rounded-md">🔥 Mappa TAC</span>
                                <span class="px-2 py-0.5 bg-slate-100 rounded-md">💰 Costo Tiratura</span>
                            </div>
                        </div>

                        <!-- Big Action CTA Button -->
                        <div class="pt-3 border-t border-slate-100">
                            <div class="w-full py-2 px-3 rounded-xl bg-rose-50 group-hover:bg-rose-900 text-rose-900 group-hover:text-white font-bold text-xs flex items-center justify-between transition-colors shadow-2xs">
                                <span id="toolCoperturaCta">Calcola Copertura & Costi</span>
                                <span class="group-hover:translate-x-1 transition-transform">➔</span>
                            </div>
                        </div>
                    </a>"""

c = c.replace(target_barcode_end, copertura_card)

# 3. Update applyTranslations JS
target_js_barcode = """            // Tool 7: Barcode
            if (t.tool_barcode_title) document.getElementById('toolBarcodeTitle').textContent = t.tool_barcode_title;
            if (t.tool_barcode_hook) document.getElementById('toolBarcodeHook').textContent = t.tool_barcode_hook;
            if (t.tool_barcode_desc) document.getElementById('toolBarcodeDesc').textContent = t.tool_barcode_desc;
            if (t.tool_barcode_cta) document.getElementById('toolBarcodeCta').textContent = t.tool_barcode_cta;
            if (t.tool_barcode_badge) document.getElementById('toolBarcodeBadge').textContent = t.tool_barcode_badge;"""

copertura_js = """            // Tool 7: Barcode
            if (t.tool_barcode_title) document.getElementById('toolBarcodeTitle').textContent = t.tool_barcode_title;
            if (t.tool_barcode_hook) document.getElementById('toolBarcodeHook').textContent = t.tool_barcode_hook;
            if (t.tool_barcode_desc) document.getElementById('toolBarcodeDesc').textContent = t.tool_barcode_desc;
            if (t.tool_barcode_cta) document.getElementById('toolBarcodeCta').textContent = t.tool_barcode_cta;
            if (t.tool_barcode_badge) document.getElementById('toolBarcodeBadge').textContent = t.tool_barcode_badge;

            // Tool 8: Copertura
            if (t.tool_copertura_title) document.getElementById('toolCoperturaTitle').textContent = t.tool_copertura_title;
            if (t.tool_copertura_hook) document.getElementById('toolCoperturaHook').textContent = t.tool_copertura_hook;
            if (t.tool_copertura_desc) document.getElementById('toolCoperturaDesc').textContent = t.tool_copertura_desc;
            if (t.tool_copertura_cta) document.getElementById('toolCoperturaCta').textContent = t.tool_copertura_cta;
            if (t.tool_copertura_badge) document.getElementById('toolCoperturaBadge').textContent = t.tool_copertura_badge;"""

c = c.replace(target_js_barcode, copertura_js)

# 4. Change grid class for graph section to wrap nicely
c = c.replace('<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">', '<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">')

with open('/Users/ilalu/Documents/Altenative Businnes/Calcolatore_Pendenza/build_hub_i18n.py', 'w', encoding='utf-8') as f:
    f.write(c)

print("build_hub_i18n.py updated successfully.")
