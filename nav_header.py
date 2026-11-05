# nav_header.py - Soluzione 1: Clean Breadcrumb Header with Categorized Suite Dropdown

TOOLS = [
    {
        "id": "rampe",
        "category": "OmniBuilding",
        "category_label": "Cantiere & Calcolo",
        "name": "RampaFacile",
        "desc": "Pendenza & D.M. 236/89",
        "emoji": "📐",
        "url": "/rampe",
        "badge": "DM 236/89",
        "color": "blue"
    },
    {
        "id": "scale",
        "category": "OmniBuilding",
        "category_label": "Cantiere & Calcolo",
        "name": "ScalaFacile",
        "desc": "Gradini & Legge di Blondel",
        "emoji": "🪜",
        "url": "/scale",
        "badge": "Blondel",
        "color": "indigo"
    },
    {
        "id": "tubi",
        "category": "OmniBuilding",
        "category_label": "Cantiere & Calcolo",
        "name": "TubiFacili",
        "desc": "Pendenza Scarichi Idraulici",
        "emoji": "🚰",
        "url": "/tubi",
        "badge": "Scarichi",
        "color": "cyan"
    },
    {
        "id": "dorso",
        "category": "OmniGraph",
        "category_label": "Grafica & Prestampa",
        "name": "DorsoFacile",
        "desc": "Spessore Dorso & Copertina KDP",
        "emoji": "📕",
        "url": "/dorso",
        "badge": "Brossura",
        "color": "rose"
    },
    {
        "id": "dpi",
        "category": "OmniGraph",
        "category_label": "Grafica & Prestampa",
        "name": "RisoluzioneFacile",
        "desc": "Pixel, DPI & Acuità Visiva",
        "emoji": "🔍",
        "url": "/dpi",
        "badge": "Pixel/DPI",
        "color": "emerald"
    },
    {
        "id": "tinta",
        "category": "OmniGraph",
        "category_label": "Grafica & Prestampa",
        "name": "TintaFacile",
        "desc": "Resa Inchiostri & Bobine Stampa",
        "emoji": "🎨",
        "url": "/tinta",
        "badge": "Inchiostri",
        "color": "amber"
    },
    {
        "id": "barcode",
        "category": "OmniGraph",
        "category_label": "Grafica & Prestampa",
        "name": "OmniBarcode Studio",
        "desc": "EAN-13, Tessera Sanitaria & GS1",
        "emoji": "🏷️",
        "url": "/barcode",
        "badge": "GS1 / TS",
        "color": "indigo"
    }
]

def get_tool_icon_svg(tool_id):
    if tool_id in ["rampe", "scale", "tubi"]:
        return """<svg class="w-full h-full" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg">
            <circle cx="16" cy="16" r="13.2" stroke="#ffffff" stroke-width="3" />
            <path d="M 9.5 8.5 V 23.5 H 24.5" stroke="#ffffff" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round" />
            <line x1="9.5" y1="23.5" x2="22.5" y2="10.5" stroke="#ffffff" stroke-width="2" stroke-dasharray="2.5 2" />
            <circle cx="9.5" cy="23.5" r="2.2" fill="#fde047" />
        </svg>"""
    elif tool_id == "barcode":
        return """<svg class="w-full h-full" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg">
            <rect x="4" y="6" width="24" height="20" rx="4" fill="#0f172a" />
            <!-- Barcode vertical lines -->
            <line x1="8" y1="10" x2="8" y2="22" stroke="#ffffff" stroke-width="2" stroke-linecap="round"/>
            <line x1="11" y1="10" x2="11" y2="22" stroke="#ffffff" stroke-width="1.2" stroke-linecap="round"/>
            <line x1="14" y1="10" x2="14" y2="22" stroke="#ffffff" stroke-width="2.5" stroke-linecap="round"/>
            <line x1="18" y1="10" x2="18" y2="22" stroke="#ffffff" stroke-width="1.2" stroke-linecap="round"/>
            <line x1="21" y1="10" x2="21" y2="22" stroke="#ffffff" stroke-width="1.8" stroke-linecap="round"/>
            <line x1="24" y1="10" x2="24" y2="22" stroke="#ffffff" stroke-width="2.2" stroke-linecap="round"/>
            <!-- Red Laser Beam 670nm -->
            <line x1="5" y1="16" x2="27" y2="16" stroke="#ef4444" stroke-width="1.6" stroke-linecap="round" />
            <circle cx="16" cy="16" r="1.8" fill="#fee2e2" />
        </svg>"""
    else: # dorso, dpi, tinta
        return """<svg class="w-full h-full" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg">
            <circle cx="16" cy="16" r="13.2" stroke="#ffffff" stroke-width="2.8" />
            <circle cx="16" cy="16" r="6.8" stroke="#ffffff" stroke-width="2" />
            <line x1="16" y1="4.5" x2="16" y2="27.5" stroke="#ffffff" stroke-width="2.2" stroke-linecap="round" />
            <line x1="4.5" y1="16" x2="27.5" y2="16" stroke="#ffffff" stroke-width="2.2" stroke-linecap="round" />
            <circle cx="16" cy="16" r="2.2" fill="#fda4af" />
        </svg>"""

def render_suite_header(current_id):
    current = next((t for t in TOOLS if t["id"] == current_id), TOOLS[0])
    is_building = current["category"] == "OmniBuilding"
    
    brand_gradient = "bg-gradient-to-br from-amber-500 to-amber-700 shadow-amber-500/20" if is_building else "bg-gradient-to-br from-rose-800 to-rose-950 shadow-rose-900/20"
    if current_id == "barcode":
        brand_gradient = "bg-gradient-to-br from-slate-900 via-indigo-950 to-slate-900 shadow-slate-900/30"
        
    cat_tag_class = "bg-blue-100 text-blue-800 border-blue-200/80" if is_building else "bg-purple-100 text-purple-800 border-purple-200/80"
    cat_name = "Building" if is_building else "Graph"
    
    building_tools_html = ""
    for t in [x for x in TOOLS if x["category"] == "OmniBuilding"]:
        is_active = t["id"] == current_id
        active_class = "bg-blue-50/80 text-blue-700 border border-blue-200" if is_active else "hover:bg-slate-50 text-slate-700"
        badge_html = '<span class="text-[9px] font-extrabold px-1.5 py-0.5 rounded-md bg-blue-600 text-white shadow-2xs">Attivo</span>' if is_active else f'<span class="text-[9px] font-bold px-1.5 py-0.5 rounded-md bg-slate-100 text-slate-500">{t["badge"]}</span>'
        building_tools_html += f"""
            <a href="{t['url']}" class="flex items-center justify-between px-2.5 py-1.5 rounded-xl text-xs font-semibold transition group {active_class}">
                <div class="flex items-center gap-2">
                    <span class="text-base shrink-0">{t['emoji']}</span>
                    <div class="text-left">
                        <div class="font-bold text-slate-900 leading-tight group-hover:text-blue-600">{t['name']}</div>
                        <div class="text-[10px] text-slate-500 font-normal leading-tight">{t['desc']}</div>
                    </div>
                </div>
                {badge_html}
            </a>"""

    graph_tools_html = ""
    for t in [x for x in TOOLS if x["category"] == "OmniGraph"]:
        is_active = t["id"] == current_id
        active_class = "bg-purple-50/80 text-purple-700 border border-purple-200" if is_active else "hover:bg-slate-50 text-slate-700"
        badge_html = '<span class="text-[9px] font-extrabold px-1.5 py-0.5 rounded-md bg-purple-600 text-white shadow-2xs">Attivo</span>' if is_active else f'<span class="text-[9px] font-bold px-1.5 py-0.5 rounded-md bg-slate-100 text-slate-500">{t["badge"]}</span>'
        graph_tools_html += f"""
            <a href="{t['url']}" class="flex items-center justify-between px-2.5 py-1.5 rounded-xl text-xs font-semibold transition group {active_class}">
                <div class="flex items-center gap-2">
                    <span class="text-base shrink-0">{t['emoji']}</span>
                    <div class="text-left">
                        <div class="font-bold text-slate-900 leading-tight group-hover:text-purple-600">{t['name']}</div>
                        <div class="text-[10px] text-slate-500 font-normal leading-tight">{t['desc']}</div>
                    </div>
                </div>
                {badge_html}
            </a>"""

    icon_svg = get_tool_icon_svg(current_id)

    html = f"""    <!-- Top Navigation Header (Soluzione 1: Breadcrumb + Suite Dropdown) -->
    <header class="bg-white border-b border-slate-200 sticky top-0 z-40 shadow-2xs backdrop-blur-md bg-white/95" style="padding-top: max(env(safe-area-inset-top), 8px); padding-bottom: 8px;">
        <div class="max-w-5xl mx-auto px-3 sm:px-4 py-1 flex items-center justify-between gap-2">
            
            <!-- Breadcrumb Navigation & Suite Switcher -->
            <div class="flex items-center gap-2 sm:gap-2.5 min-w-0">
                <!-- Home Link & Brand Logo -->
                <a href="/" class="w-[34px] h-[34px] sm:w-[38px] sm:h-[38px] rounded-xl {brand_gradient} flex items-center justify-center text-white shadow-md shrink-0 p-1 transition hover:opacity-95 active:scale-95" title="Torna alla Home di OmniTools">
                    {icon_svg}
                </a>

                <!-- Breadcrumb Title with Integrated Dropdown Switcher -->
                <div class="relative flex items-center min-w-0">
                    <div class="flex items-center gap-1 sm:gap-1.5 text-xs sm:text-sm font-jakarta font-bold text-slate-900 leading-none">
                        <a href="/" class="hover:text-blue-600 transition flex items-center shrink-0" title="Home Hub">
                            <span>Omni<span class="text-blue-600">Tools</span></span>
                        </a>
                        <span class="text-slate-300 font-normal">/</span>
                        <span id="brandBadge" class="text-[9px] sm:text-[10px] font-extrabold uppercase px-1.5 py-0.5 rounded-full {cat_tag_class} border shrink-0 hidden xs:inline-block">{cat_name}</span>
                        <span id="brandBadgeMobile" class="hidden">{current['badge']}</span>
                        <span class="text-slate-300 font-normal hidden xs:inline-block">/</span>
                        
                        <!-- Dropdown Switcher Button -->
                        <button id="suiteMenuBtn" onclick="toggleSuiteMenu(event)" class="inline-flex items-center gap-1 px-1.5 sm:px-2 py-1 rounded-lg bg-slate-100 hover:bg-slate-200/80 active:bg-slate-200 text-slate-800 font-bold transition border border-slate-200/70" aria-label="Cambia strumento" aria-expanded="false" title="Cambia strumento della suite">
                            <span id="brandTitle" class="truncate max-w-[110px] sm:max-w-none">{current['name']}</span>
                            <span id="brandTitleMobile" class="hidden">{current['name']}</span>
                            <svg id="suiteMenuChevron" class="w-3.5 h-3.5 text-slate-500 shrink-0 transition-transform duration-200" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M19 9l-7 7-7-7"></path>
                            </svg>
                        </button>
                    </div>

                    <!-- Dropdown Popover Menu (All 7 Tools Categorized) -->
                    <div id="suiteMenuDropdown" class="hidden absolute left-0 top-full mt-2 w-72 sm:w-80 bg-white rounded-2xl shadow-2xl border border-slate-200/90 py-2 z-50 transition-all duration-150">
                        <div class="px-3 py-1.5 border-b border-slate-100 flex items-center justify-between">
                            <span class="text-[11px] font-bold uppercase tracking-wider text-slate-400">Strumenti OmniTools</span>
                            <a href="/" class="text-[11px] font-bold text-blue-600 hover:text-blue-700 flex items-center gap-0.5">
                                Home Hub →
                            </a>
                        </div>

                        <!-- Cantiere & Struttura -->
                        <div class="px-2 pt-2 pb-1">
                            <div class="px-1 text-[10px] font-extrabold uppercase tracking-wider text-amber-700 flex items-center gap-1 mb-1">
                                <span>🏗️</span> OmniBuilding · Cantiere & Struttura
                            </div>
                            <div class="space-y-0.5">
                                {building_tools_html}
                            </div>
                        </div>

                        <div class="border-t border-slate-100 my-1"></div>

                        <!-- Grafica & Prestampa -->
                        <div class="px-2 pt-1 pb-1">
                            <div class="px-1 text-[10px] font-extrabold uppercase tracking-wider text-purple-700 flex items-center gap-1 mb-1">
                                <span>🎯</span> OmniGraph · Grafica & Stampa
                            </div>
                            <div class="space-y-0.5">
                                {graph_tools_html}
                            </div>
                        </div>

                        <!-- Footer Link to Hub -->
                        <div class="border-t border-slate-100 mt-1 pt-1.5 px-3 pb-1">
                            <a href="/" class="flex items-center justify-center gap-1.5 w-full py-1.5 text-center text-xs font-bold text-slate-600 hover:text-blue-600 bg-slate-50 hover:bg-blue-50 rounded-xl transition">
                                <span>🏠</span> Tutti gli strumenti nella Home
                            </a>
                        </div>
                    </div>
                </div>
            </div>
            
            <!-- Quick Actions on Right: Clean & Zero Mobile Clutter -->
            <div class="flex items-center gap-1.5 sm:gap-2 shrink-0">
                <!-- Language Selector Dropdown -->
                <div class="relative inline-block text-left">
                    <select id="langSelect" onchange="changeLanguage(this.value)" class="bg-slate-100 hover:bg-slate-200 text-slate-800 text-xs font-bold py-1.5 px-2 rounded-xl border border-slate-200 focus:outline-none cursor-pointer transition">
                        <option value="it">🇮🇹 IT</option>
                        <option value="en">🇬🇧 EN</option>
                        <option value="es">🇪🇸 ES</option>
                        <option value="fr">🇫🇷 FR</option>
                        <option value="de">🇩🇪 DE</option>
                        <option value="pt">🇵🇹 PT</option>
                    </select>
                </div>

                <button onclick="triggerInstall()" id="headerInstallBtn" class="no-print inline-flex items-center justify-center p-1.5 sm:px-2.5 sm:py-1.5 text-xs font-bold text-blue-700 bg-blue-50 hover:bg-blue-100 active:scale-95 rounded-xl border border-blue-200 transition" title="Installa come App">
                    <span>📲</span>
                    <span id="headerInstallText" class="hidden sm:inline ml-1">App</span>
                </button>
                <button onclick="window.print()" class="no-print inline-flex items-center justify-center p-1.5 sm:px-2.5 sm:py-1.5 text-xs font-bold text-slate-700 bg-slate-100 hover:bg-slate-200 active:scale-95 rounded-xl transition shadow-2xs" title="Stampa Scheda Tecnica">
                    <svg class="w-4 h-4 text-slate-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 17h2a2 2 0 002-2v-4a2 2 0 00-2-2H5a2 2 0 00-2 2v4a2 2 0 002 2h2m2 4h6a2 2 0 002-2v-4a2 2 0 00-2-2H9a2 2 0 00-2 2v4a2 2 0 002 2zm8-12V5a2 2 0 00-2-2H9a2 2 0 00-2 2v4h10z" />
                    </svg>
                    <span id="printBtnText" class="hidden sm:inline ml-1">Stampa</span>
                </button>
            </div>
        </div>
    </header>"""
    return html

def render_suite_header_js():
    return """
// Soluzione 1: Suite Switcher Dropdown Interaction
function toggleSuiteMenu(e) {
    if (e) e.stopPropagation();
    const menu = document.getElementById('suiteMenuDropdown');
    const chevron = document.getElementById('suiteMenuChevron');
    const btn = document.getElementById('suiteMenuBtn');
    if (!menu) return;
    const isClosed = menu.classList.contains('hidden');
    if (isClosed) {
        menu.classList.remove('hidden');
        if (chevron) chevron.classList.add('rotate-180');
        if (btn) btn.setAttribute('aria-expanded', 'true');
    } else {
        menu.classList.add('hidden');
        if (chevron) chevron.classList.remove('rotate-180');
        if (btn) btn.setAttribute('aria-expanded', 'false');
    }
}

document.addEventListener('click', function(e) {
    const menu = document.getElementById('suiteMenuDropdown');
    const btn = document.getElementById('suiteMenuBtn');
    if (menu && !menu.classList.contains('hidden')) {
        if (!menu.contains(e.target) && (!btn || !btn.contains(e.target))) {
            menu.classList.add('hidden');
            const chevron = document.getElementById('suiteMenuChevron');
            if (chevron) chevron.classList.remove('rotate-180');
            if (btn) btn.setAttribute('aria-expanded', 'false');
        }
    }
});

document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape') {
        const menu = document.getElementById('suiteMenuDropdown');
        if (menu && !menu.classList.contains('hidden')) {
            menu.classList.add('hidden');
            const chevron = document.getElementById('suiteMenuChevron');
            if (chevron) chevron.classList.remove('rotate-180');
            const btn = document.getElementById('suiteMenuBtn');
            if (btn) btn.setAttribute('aria-expanded', 'false');
        }
    }
});
"""

if __name__ == "__main__":
    print("nav_header.py module compiled successfully.")
