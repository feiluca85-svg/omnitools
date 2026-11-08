# nav_header.py - Dynamic Google Chrome Tabs & Multi-Tool Floating Workspace Engine

# Monochrome modern SVG pictograms with division background colors:
# Building: bg-amber-500
# Graph: bg-rose-700
# Finance: bg-emerald-600

TOOL_ICONS = {
    "rampe": """<span class="w-4 h-4 rounded-md bg-amber-500 text-white flex items-center justify-center p-0.5 shrink-0"><svg class="w-full h-full" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M3 20h18L3 8v12z"/></svg></span>""",
    "scale": """<span class="w-4 h-4 rounded-md bg-amber-500 text-white flex items-center justify-center p-0.5 shrink-0"><svg class="w-full h-full" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M4 20h4v-4h4v-4h4v-4h4"/></svg></span>""",
        "tubi": """<span class="w-4 h-4 rounded-md bg-amber-500 text-white flex items-center justify-center p-0.5 shrink-0"><svg class="w-full h-full" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M4 14h6a4 4 0 004-4V4"/></svg></span>""",
    "tetto": """<span class="w-4 h-4 rounded-md bg-amber-500 text-white flex items-center justify-center p-0.5 shrink-0"><svg class="w-full h-full" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M3 12l9-9 9 9M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3"/></svg></span>""",
    "taglio": """<span class="w-4 h-4 rounded-md bg-amber-500 text-white flex items-center justify-center p-0.5 shrink-0"><svg class="w-full h-full" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M14.121 14.121L19 19m-7-7l7-7m-7 7l-2.879 2.879a3 3 0 11-4.242-4.242L10.758 10.758m0 0l2.879-2.879a3 3 0 10-4.242-4.242L6.515 6.515"/></svg></span>""",

    
    "dorso": """<span class="w-4 h-4 rounded-md bg-rose-700 text-white flex items-center justify-center p-0.5 shrink-0"><svg class="w-full h-full" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"/></svg></span>""",
    "dpi": """<span class="w-4 h-4 rounded-md bg-rose-700 text-white flex items-center justify-center p-0.5 shrink-0"><svg class="w-full h-full" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="8.5" cy="8.5" r="1.5"/><path d="M21 15l-5-5L5 21"/></svg></span>""",
    "tinta": """<span class="w-4 h-4 rounded-md bg-rose-700 text-white flex items-center justify-center p-0.5 shrink-0"><svg class="w-full h-full" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M7 21a4 4 0 01-4-4c0-2.5 4-8 4-8s4 5.5 4 8a4 4 0 01-4 4z"/></svg></span>""",
    "barcode": """<span class="w-4 h-4 rounded-md bg-rose-700 text-white flex items-center justify-center p-0.5 shrink-0"><svg class="w-full h-full" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M4 6v12M8 6v12M12 6v12M15 6v12M19 6v12"/></svg></span>""",
    "copertura": """<span class="w-4 h-4 rounded-md bg-rose-700 text-white flex items-center justify-center p-0.5 shrink-0"><svg class="w-full h-full" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M19 11H5m14 0a7 7 0 01-7 7m7-7a7 7 0 00-7-7m0 14a7 7 0 01-7-7m7 7v4m0-18v4"/></svg></span>""",
    "resa": """<span class="w-4 h-4 rounded-md bg-rose-700 text-white flex items-center justify-center p-0.5 shrink-0"><svg class="w-full h-full" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/></svg></span>""",
    
    "mutuo": """<span class="w-4 h-4 rounded-md bg-emerald-600 text-white flex items-center justify-center p-0.5 shrink-0"><svg class="w-full h-full" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M3 10h18M7 15h1m4 0h1m-7 4h12a3 3 0 003-3V8a3 3 0 00-3-3H6a3 3 0 00-3 3v8a3 3 0 003 3z"/></svg></span>""",
    "pac": """<span class="w-4 h-4 rounded-md bg-emerald-600 text-white flex items-center justify-center p-0.5 shrink-0"><svg class="w-full h-full" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"/></svg></span>""",
    "margine": """<span class="w-4 h-4 rounded-md bg-emerald-600 text-white flex items-center justify-center p-0.5 shrink-0"><svg class="w-full h-full" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M7 7h.01M7 3h5a1.99 1.99 0 011.414.586l7 7a2 2 0 010 2.828l-7 7a2 2 0 01-2.828 0l-7-7A1.994 1.994 0 013 12V5a2 2 0 012-2z"/></svg></span>""",
        "estinzione": """<span class="w-4 h-4 rounded-md bg-emerald-600 text-white flex items-center justify-center p-0.5 shrink-0"><svg class="w-full h-full" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg></span>""",
        "risparmio": """<span class="w-4 h-4 rounded-md bg-emerald-600 text-white flex items-center justify-center p-0.5 shrink-0"><svg class="w-full h-full" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M17 9V7a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2m2 4h10a2 2 0 002-2v-6a2 2 0 00-2-2H9a2 2 0 00-2 2v6a2 2 0 002 2zm7-5a2 2 0 11-4 0 2 2 0 014 0z"/></svg></span>""",
    "fire": """<span class="w-4 h-4 rounded-md bg-emerald-600 text-white flex items-center justify-center p-0.5 shrink-0"><svg class="w-full h-full" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M17.657 18.657A8 8 0 016.343 7.343S7 9 9 10c0-2 .5-5 2.986-7C14 5 16.09 5.777 17.656 7.343A7.975 7.975 0 0120 13a7.975 7.975 0 01-2.343 5.657z"/></svg></span>"""
}

TOOLS = [
    {
        "id": "rampe",
        "category": "OmniBuilding",
        "category_label": "Cantiere & Calcolo",
        "name": "RampaFacile",
        "desc": "Pendenza & D.M. 236/89",
        "url": "/rampe",
        "badge": "DM 236/89"
    },
    {
        "id": "scale",
        "category": "OmniBuilding",
        "category_label": "Cantiere & Calcolo",
        "name": "ScalaFacile",
        "desc": "Gradini & Legge di Blondel",
        "url": "/scale",
        "badge": "Blondel"
    },
    {
        "id": "tubi",
        "category": "OmniBuilding",
        "category_label": "Cantiere & Calcolo",
        "name": "TubiFacili",
        "desc": "Pendenza Scarichi Idraulici",
        "url": "/tubi",
        "badge": "Scarichi"
    },
    {
        "id": "tetto",
        "category": "OmniBuilding",
        "category_label": "Cantiere & Calcolo",
        "name": "TettoFacile",
        "desc": "Pendenza Falda, Gradi & Trave",
        "url": "/tetto",
        "badge": "Pendenza & Falda"
    },
    {
        "id": "taglio",
        "category": "OmniBuilding",
        "category_label": "Cantiere & Calcolo",
        "name": "TaglioOttimo",
        "desc": "Ottimizzatore Taglio 1D & Sfrido",
        "url": "/taglio",
        "badge": "Bin-Packing 1D"
    },
    {
        "id": "dorso",
        "category": "OmniGraph",
        "category_label": "Grafica & Prestampa",
        "name": "DorsoFacile",
        "desc": "Spessore Dorso & Copertina KDP",
        "url": "/dorso",
        "badge": "Brossura"
    },
    {
        "id": "dpi",
        "category": "OmniGraph",
        "category_label": "Grafica & Prestampa",
        "name": "RisoluzioneFacile",
        "desc": "DPI, Megapixel & Dimensioni Stampa",
        "url": "/dpi",
        "badge": "DPI / PPI"
    },
    {
        "id": "tinta",
        "category": "OmniGraph",
        "category_label": "Grafica & Prestampa",
        "name": "TintaPerfetta",
        "desc": "Conversione Pantone, CMYK, RGB & Hex",
        "url": "/tinta",
        "badge": "Color Match"
    },
    {
        "id": "barcode",
        "category": "OmniGraph",
        "category_label": "Grafica & Prestampa",
        "name": "OmniBarcode",
        "desc": "Generatore Codici EAN-13, ITF-14 & Checksum",
        "url": "/barcode",
        "badge": "ISO/IEC 15420"
    },
    {
        "id": "copertura",
        "category": "OmniGraph",
        "category_label": "Grafica & Prestampa",
        "name": "CoperturaFacile",
        "desc": "Calcolo Inchiostro & TAC/TIL Prestampa",
        "url": "/copertura",
        "badge": "ISO 12647-2"
    },
    {
        "id": "resa",
        "category": "OmniGraph",
        "category_label": "Grafica & Prestampa",
        "name": "ResaCarta",
        "desc": "Calcolo Segnature, Resa Fogli & Scarto",
        "url": "/resa",
        "badge": "Fogli Macchina"
    },
    {
        "id": "mutuo",
        "category": "OmniFinance",
        "category_label": "Finanza & Business",
        "name": "MutuoFacile",
        "desc": "Ammortamento Francese, Rata & Quota Interessi",
        "url": "/mutuo",
        "badge": "Finanziario"
    },
    {
        "id": "pac",
        "category": "OmniFinance",
        "category_label": "Finanza & Business",
        "name": "InteresseComposto",
        "desc": "PAC, Rendimento Composto & Montante Futuro",
        "url": "/pac",
        "badge": "Piano Accumulo"
    },
    {
        "id": "margine",
        "category": "OmniFinance",
        "category_label": "Finanza & Business",
        "name": "MargineFacile",
        "desc": "Margine di Profitto vs Ricarico & Prezzo COGS",
        "url": "/margine",
        "badge": "Markup / IVA"
    },
    {
        "id": "estinzione",
        "category": "OmniFinance",
        "category_label": "Finanza & Business",
        "name": "EstinzioneMutuo",
        "desc": "Estinzione Anticipata: Rata vs Anni",
        "url": "/estinzione",
        "badge": "Bersani"
    },
    {
        "id": "risparmio",
        "category": "OmniFinance",
        "category_label": "Finanza & Business",
        "name": "ObiettivoRisparmio",
        "desc": "Sinking Fund & Quota Risparmio Mensile",
        "url": "/risparmio",
        "badge": "Sinking Fund"
    },
    {
        "id": "fire",
        "category": "OmniFinance",
        "category_label": "Finanza & Business",
        "name": "FIRE & Rendita",
        "desc": "Libertà Finanziaria & Regola del 4%",
        "url": "/fire",
        "badge": "Trinity Study"
    }
]


def render_chrome_tabs_strip(current_id="home"):
    def render_tool_items_tabs(category_name):
        items = [t for t in TOOLS if t["category"] == category_name]
        html_out = ""
        for tool in items:
            is_active = (tool["id"] == current_id)
            active_badge = 'bg-blue-600 text-white font-bold' if is_active else 'text-slate-700 hover:bg-slate-100'
            icon_svg = TOOL_ICONS.get(tool["id"], "")
            html_out += f"""
            <a href="{tool['url']}" class="flex items-center justify-between p-2 rounded-xl text-xs transition {active_badge}">
                <div class="flex items-center gap-2">
                    {icon_svg}
                    <span class="font-bold">{tool['name']}</span>
                </div>
                <span class="text-[9px] uppercase px-1.5 py-0.5 rounded-md bg-black/10 font-mono font-bold">{tool['badge']}</span>
            </a>
            """
        return html_out

    b_tools = render_tool_items_tabs("OmniBuilding")
    g_tools = render_tool_items_tabs("OmniGraph")
    f_tools = render_tool_items_tabs("OmniFinance")

    return f"""
    <!-- TOP CHROME-STYLE TABS STRIP (DESKTOP ONLY: sticky top-0, always visible) -->
    <div id="omniChromeTabsBar" class="hidden md:flex bg-slate-950 px-3 pt-2 pb-0 items-center justify-between border-b border-slate-800 text-xs select-none sticky top-0 z-50 shadow-md">
        
        <!-- Track of Tabs (Home Tab + Dynamic Opened Tabs) -->
        <div id="omniChromeTabsTrack" class="flex items-center gap-1 overflow-x-auto no-scrollbar max-w-[calc(100%-250px)]">
            <!-- Fixed Home Hub Tab -->
            <a href="/" id="omniTabHome" class="flex items-center gap-1.5 px-3.5 py-1.5 rounded-t-xl bg-slate-800 hover:bg-slate-700 text-slate-300 font-bold border-t-2 border-transparent transition shrink-0 text-[11px]" title="Torna alla Home Hub">
                <span class="w-4 h-4 rounded-md bg-blue-600 text-white flex items-center justify-center p-0.5 shrink-0 shadow-2xs">
                    <svg class="w-full h-full" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"/></svg>
                </span>
                <span>Home Hub</span>
            </a>
        </div>

        <!-- Right Side: DESK Menu & Nuovo Tool -->
        <div class="flex items-center gap-2 shrink-0 pb-1.5 pr-1">
            
            <!-- DESK Dropdown Trigger Button -->
            <div class="relative">
                <button id="topDeskBtn" onclick="toggleTopDeskMenu(event)" class="px-2.5 py-1 bg-gradient-to-r from-amber-500/20 to-amber-600/20 hover:from-amber-500 hover:to-amber-600 text-amber-300 hover:text-white rounded-lg text-xs font-black transition border border-amber-500/40 flex items-center gap-1.5 shadow-xs cursor-pointer" title="Apri strumenti da scrivania (Memo, Calc, Orologio)">
                    <span class="w-3.5 h-3.5 rounded bg-amber-500 text-slate-950 flex items-center justify-center font-black text-[9px]">⚡</span>
                    <span class="tracking-wider">DESK</span>
                    <svg class="w-3 h-3 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M19 9l-7 7-7-7"></path></svg>
                </button>

                <!-- DESK Menu Dropdown in Top Bar -->
                <div id="topDeskDropdown" class="hidden absolute right-0 mt-2 w-56 bg-slate-900 border border-slate-700 rounded-2xl shadow-2xl p-2 z-50 space-y-1 text-xs">
                    <div class="px-2 py-1 text-[10px] font-black uppercase tracking-wider text-amber-400 border-b border-slate-800">
                        Strumenti da Scrivania
                    </div>
                    <button type="button" onclick="openDeskTool('memo');" class="w-full flex items-center gap-2.5 p-2 rounded-xl text-amber-200 hover:bg-slate-800 transition font-bold text-left cursor-pointer">
                        <span class="w-4 h-4 rounded-md bg-amber-400 text-slate-950 flex items-center justify-center font-bold text-[10px]">📝</span>
                        <span>OmniMemo (Post-it)</span>
                    </button>
                    <button type="button" onclick="openDeskTool('calc');" class="w-full flex items-center gap-2.5 p-2 rounded-xl text-blue-300 hover:bg-slate-800 transition font-bold text-left cursor-pointer">
                        <span class="w-4 h-4 rounded-md bg-blue-500 text-white flex items-center justify-center font-bold text-[10px]">🔢</span>
                        <span>OmniCalc (Calcolatrice)</span>
                    </button>
                    <button type="button" onclick="openDeskTool('clock');" class="w-full flex items-center gap-2.5 p-2 rounded-xl text-teal-300 hover:bg-slate-800 transition font-bold text-left cursor-pointer">
                        <span class="w-4 h-4 rounded-md bg-teal-500 text-white flex items-center justify-center font-bold text-[10px]">⏱️</span>
                        <span>OmniClock (Orologio)</span>
                    </button>
                </div>
            </div>

            <!-- Nuovo Tool (+) Button (Dropdown opens fully aligned to RIGHT edge!) -->
            <div class="relative">
                <button id="topNewToolBtn" onclick="toggleTopNewToolMenu(event)" class="px-2.5 py-1 bg-slate-800 hover:bg-slate-700 text-slate-200 hover:text-white rounded-lg text-xs font-bold transition flex items-center gap-1 border border-slate-700 cursor-pointer" title="Apri un nuovo calcolatore in scheda">
                    <span>➕</span>
                    <span class="hidden lg:inline">Nuovo Tool</span>
                </button>

                <!-- Full Tool Catalog Dropdown Aligned to Right edge -->
                <div id="topNewToolDropdown" class="hidden absolute right-0 mt-2 w-72 sm:w-80 bg-white rounded-2xl shadow-2xl border border-slate-200 z-50 p-2 space-y-2 text-left">
                    <div class="px-2 pt-1 pb-0.5 border-b border-slate-100 flex items-center justify-between text-[11px] font-extrabold text-slate-400 uppercase">
                        <span>Scegli Calcolatore</span>
                        <span class="text-blue-600 font-bold font-mono">17 Tool</span>
                    </div>

                    <!-- Category: OmniBuilding -->
                    <div>
                        <div class="px-2 py-0.5 text-[10px] font-extrabold uppercase tracking-wider text-amber-600 flex items-center gap-1">
                            <span class="w-1.5 h-1.5 rounded-full bg-amber-500"></span> OmniBuilding (5)
                        </div>
                        {b_tools}
                    </div>

                    <!-- Category: OmniGraph -->
                    <div>
                        <div class="px-2 py-0.5 text-[10px] font-extrabold uppercase tracking-wider text-rose-600 flex items-center gap-1">
                            <span class="w-1.5 h-1.5 rounded-full bg-rose-700"></span> OmniGraph (6)
                        </div>
                        {g_tools}
                    </div>

                    <!-- Category: OmniFinance -->
                    <div>
                        <div class="px-2 py-0.5 text-[10px] font-extrabold uppercase tracking-wider text-emerald-600 flex items-center gap-1">
                            <span class="w-1.5 h-1.5 rounded-full bg-emerald-600"></span> OmniFinance (6)
                        </div>
                        {f_tools}
                    </div>
                </div>
            </div>

        </div>
    </div>
    """

def render_suite_header(current_id):
    # Match the exact main container width of the current tool:
    # OmniFinance tools (mutuo, pac, margine) use max-w-6xl, while OmniBuilding & OmniGraph use max-w-5xl
    container_max_w = "max-w-5xl"
    current_tool = next((t for t in TOOLS if t["id"] == current_id), None)
    if not current_tool:
        current_tool = {
            "name": "Tool",
            "desc": "Strumento di calcolo",
            "badge": "OmniTools",
            "category_label": "Suite"
        }

    # Generate Tool Lists for dropdown
    def render_tool_items(category_name):
        items = [t for t in TOOLS if t["category"] == category_name]
        html_out = ""
        for tool in items:
            is_active = (tool["id"] == current_id)
            active_badge = 'bg-blue-600 text-white font-bold' if is_active else 'text-slate-700 hover:bg-slate-100'
            icon_svg = TOOL_ICONS.get(tool["id"], "")
            html_out += f"""
            <a href="{tool['url']}" class="flex items-center justify-between p-2 rounded-xl text-xs transition {active_badge}">
                <div class="flex items-center gap-2">
                    {icon_svg}
                    <span class="font-bold">{tool['name']}</span>
                </div>
                <span class="text-[9px] uppercase px-1.5 py-0.5 rounded-md bg-black/10 font-mono font-bold">{tool['badge']}</span>
            </a>
            """
        return html_out

    building_tools_html = render_tool_items("OmniBuilding")
    graph_tools_html = render_tool_items("OmniGraph")
    finance_tools_html = render_tool_items("OmniFinance")
    current_icon = TOOL_ICONS.get(current_id, "")

    html = f"""
    {render_chrome_tabs_strip(current_id)}
    <!-- MAIN NAVBAR & LOGO HEADER (Mobile clean, desktop sits under tabs) -->
    <header class="bg-white border-b border-slate-200 sticky top-0 md:top-[38px] z-40 shadow-2xs backdrop-blur-md bg-white/95" style="padding-top: max(env(safe-area-inset-top), 8px); padding-bottom: 8px;">
        <div class="{container_max_w} mx-auto px-3 sm:px-6 flex items-center justify-between gap-3">
            
            <!-- Logo & Suite Switcher -->
            <div class="flex items-center gap-3">
                <a href="/" class="flex items-center gap-2.5 group shrink-0">
                    <div class="w-[36px] h-[36px] sm:w-[40px] sm:h-[40px] rounded-xl bg-gradient-to-br from-blue-600 to-indigo-700 flex items-center justify-center text-white shadow-md shadow-blue-500/20 shrink-0 p-1 transition group-hover:scale-105">
                        <svg class="w-full h-full" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <circle cx="16" cy="16" r="13.2" stroke="#ffffff" stroke-width="3.4" />
                            <path d="M 7.5 11.5 H 24.5 M 16 11.5 V 24.5" stroke="#ffffff" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round" />
                            <circle cx="16" cy="11.5" r="2.1" fill="#38bdf8" />
                        </svg>
                    </div>
                    <div>
                        <div class="flex items-center gap-1.5">
                            <span class="font-jakarta font-black text-sm sm:text-base tracking-tight text-slate-900">OmniTools</span>
                            <span class="text-[9px] font-jakarta font-extrabold uppercase bg-blue-100 text-blue-800 px-1.5 py-0.5 rounded-full border border-blue-200/80">Lab</span>
                        </div>
                    </div>
                </a>

                <span class="text-slate-300">/</span>

                <!-- Current Tool Dropdown Button -->
                <div class="relative">
                    <button id="suiteMenuBtn" onclick="toggleSuiteMenu(event)" class="flex items-center gap-1.5 px-2.5 py-1.5 rounded-xl bg-slate-100 hover:bg-slate-200 text-slate-800 text-xs font-bold transition">
                        {current_icon}
                        <span class="hidden sm:inline">{current_tool['name']}</span>
                        <svg id="suiteMenuChevron" class="w-3.5 h-3.5 text-slate-500 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
                    </button>

                    <!-- Dropdown Menu Panel -->
                    <div id="suiteMenuDropdown" class="hidden absolute left-0 mt-2 w-72 sm:w-80 bg-white rounded-2xl shadow-2xl border border-slate-200 z-50 p-2 space-y-2">
                        <div class="px-2 pt-1 pb-0.5 border-b border-slate-100 flex items-center justify-between text-[11px] font-extrabold text-slate-400 uppercase">
                            <span>Scegli Calcolatore</span>
                            <span>17 Strumenti</span>
                        </div>

                        <div class="space-y-0.5">
                            <div class="px-2 text-[10px] font-extrabold uppercase text-amber-700 flex items-center gap-1">
                                <span class="w-2 h-2 rounded-full bg-amber-500"></span> OmniBuilding (5)
                            </div>
                            {building_tools_html}
                        </div>

                        <div class="space-y-0.5 pt-1 border-t border-slate-100">
                            <div class="px-2 text-[10px] font-extrabold uppercase text-rose-700 flex items-center gap-1">
                                <span class="w-2 h-2 rounded-full bg-rose-700"></span> OmniGraph (6)
                            </div>
                            {graph_tools_html}
                        </div>

                        <div class="space-y-0.5 pt-1 border-t border-slate-100">
                            <div class="px-2 text-[10px] font-extrabold uppercase text-emerald-700 flex items-center gap-1">
                                <span class="w-2 h-2 rounded-full bg-emerald-600"></span> OmniFinance (6)
                            </div>
                            {finance_tools_html}
                        </div>
                    </div>
                </div>
            </div>

            <!-- Right Actions -->
            <div class="flex items-center gap-2">
                <button onclick="if(typeof triggerInstall==='function'){{triggerInstall();}}else{{alert('OmniTools è già installato o pronto nel browser.');}}" id="headerInstallBtn" class="no-print inline-flex items-center gap-1.5 px-2.5 py-1.5 text-xs font-bold text-blue-700 bg-blue-50 hover:bg-blue-100 active:scale-95 rounded-xl border border-blue-200 transition shadow-2xs" title="Installa come App">
                    <span>📲</span>
                    <span id="headerInstallText" class="hidden sm:inline">Installa</span>
                </button>
                <button onclick="window.print()" class="no-print inline-flex items-center gap-1 px-2.5 py-1.5 text-xs font-bold text-slate-700 bg-slate-100 hover:bg-slate-200 rounded-xl transition">
                    <span>🖨️</span>
                    <span class="hidden sm:inline">Stampa</span>
                </button>
            </div>
        </div>
    </header>
    """
    return html

def render_suite_header_js():
    return """
// Top DESK Dropdown
function toggleTopDeskMenu(e) {
    if (e) e.stopPropagation();
    const drop = document.getElementById('topDeskDropdown');
    const newToolDrop = document.getElementById('topNewToolDropdown');
    if (newToolDrop) newToolDrop.classList.add('hidden');
    if (drop) drop.classList.toggle('hidden');
}

// Top Nuovo Tool Dropdown (aligned right)
function toggleTopNewToolMenu(e) {
    if (e) e.stopPropagation();
    const drop = document.getElementById('topNewToolDropdown');
    const deskDrop = document.getElementById('topDeskDropdown');
    if (deskDrop) deskDrop.classList.add('hidden');
    if (drop) drop.classList.toggle('hidden');
}

function openDeskTool(toolType) {
    const drop = document.getElementById('topDeskDropdown');
    if (drop) drop.classList.add('hidden');
    if (window.OmniDesk) {
        if (toolType === 'memo') window.OmniDesk.toggleMemo(true);
        else if (toolType === 'calc') window.OmniDesk.toggleCalc(true);
        else if (toolType === 'clock') window.OmniDesk.toggleClock(true);
    } else {
        // Fallback open standalone page
        const map = { memo: '/memo', calc: '/calcolatrice', clock: '/orologio' };
        window.open(map[toolType], '_blank');
    }
}

// Suite Menu Dropdown (header)
function toggleSuiteMenu(e) {
    if (e) e.stopPropagation();
    const menu = document.getElementById('suiteMenuDropdown');
    const chevron = document.getElementById('suiteMenuChevron');
    if (!menu) return;
    const isHidden = menu.classList.contains('hidden');
    if (isHidden) {
        menu.classList.remove('hidden');
        if (chevron) chevron.classList.add('rotate-180');
    } else {
        menu.classList.add('hidden');
        if (chevron) chevron.classList.remove('rotate-180');
    }
}

document.addEventListener('click', (e) => {
    const menu = document.getElementById('suiteMenuDropdown');
    const btn = document.getElementById('suiteMenuBtn');
    if (menu && !menu.classList.contains('hidden')) {
        if (!menu.contains(e.target) && (!btn || !btn.contains(e.target))) {
            menu.classList.add('hidden');
            const chevron = document.getElementById('suiteMenuChevron');
            if (chevron) chevron.classList.remove('rotate-180');
        }
    }
    const deskDrop = document.getElementById('topDeskDropdown');
    const topDeskBtn = document.getElementById('topDeskBtn');
    if (deskDrop && !deskDrop.classList.contains('hidden')) {
        if (!deskDrop.contains(e.target) && (!topDeskBtn || !topDeskBtn.contains(e.target))) {
            deskDrop.classList.add('hidden');
        }
    }
    const newToolDrop = document.getElementById('topNewToolDropdown');
    const topNewToolBtn = document.getElementById('topNewToolBtn');
    if (newToolDrop && !newToolDrop.classList.contains('hidden')) {
        if (!newToolDrop.contains(e.target) && (!topNewToolBtn || !topNewToolBtn.contains(e.target))) {
            newToolDrop.classList.add('hidden');
        }
    }
});

// Dynamic Chrome Tabs & Multi-Window Detach Engine
(function() {
    const TOOL_ICONS_JS = {
        'rampe': `<span class="w-4 h-4 rounded-md bg-amber-500 text-white flex items-center justify-center p-0.5 shrink-0 shadow-2xs"><svg class="w-full h-full" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M3 20h18L3 8v12z"/></svg></span>`,
        'scale': `<span class="w-4 h-4 rounded-md bg-amber-500 text-white flex items-center justify-center p-0.5 shrink-0 shadow-2xs"><svg class="w-full h-full" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M4 20h4v-4h4v-4h4v-4h4"/></svg></span>`,
        'tubi': `<span class="w-4 h-4 rounded-md bg-amber-500 text-white flex items-center justify-center p-0.5 shrink-0 shadow-2xs"><svg class="w-full h-full" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M4 14h6a4 4 0 004-4V4"/></svg></span>`,
        'tetto': `<span class="w-4 h-4 rounded-md bg-amber-500 text-white flex items-center justify-center p-0.5 shrink-0 shadow-2xs"><svg class="w-full h-full" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M3 12l9-9 9 9M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3"/></svg></span>`,
        'taglio': `<span class="w-4 h-4 rounded-md bg-amber-500 text-white flex items-center justify-center p-0.5 shrink-0 shadow-2xs"><svg class="w-full h-full" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M14.121 14.121L19 19m-7-7l7-7m-7 7l-2.879 2.879a3 3 0 11-4.242-4.242L10.758 10.758m0 0l2.879-2.879a3 3 0 10-4.242-4.242L6.515 6.515"/></svg></span>`,
        'dorso': `<span class="w-4 h-4 rounded-md bg-rose-700 text-white flex items-center justify-center p-0.5 shrink-0 shadow-2xs"><svg class="w-full h-full" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"/></svg></span>`,
        'dpi': `<span class="w-4 h-4 rounded-md bg-rose-700 text-white flex items-center justify-center p-0.5 shrink-0 shadow-2xs"><svg class="w-full h-full" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="8.5" cy="8.5" r="1.5"/><path d="M21 15l-5-5L5 21"/></svg></span>`,
        'tinta': `<span class="w-4 h-4 rounded-md bg-rose-700 text-white flex items-center justify-center p-0.5 shrink-0 shadow-2xs"><svg class="w-full h-full" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M7 21a4 4 0 01-4-4c0-2.5 4-8 4-8s4 5.5 4 8a4 4 0 01-4 4z"/></svg></span>`,
        'barcode': `<span class="w-4 h-4 rounded-md bg-rose-700 text-white flex items-center justify-center p-0.5 shrink-0 shadow-2xs"><svg class="w-full h-full" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M4 6v12M8 6v12M12 6v12M15 6v12M19 6v12"/></svg></span>`,
        'copertura': `<span class="w-4 h-4 rounded-md bg-rose-700 text-white flex items-center justify-center p-0.5 shrink-0 shadow-2xs"><svg class="w-full h-full" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M19 11H5m14 0a7 7 0 01-7 7m7-7a7 7 0 00-7-7m0 14a7 7 0 01-7-7m7 7v4m0-18v4"/></svg></span>`,
        'resa': `<span class="w-4 h-4 rounded-md bg-rose-700 text-white flex items-center justify-center p-0.5 shrink-0 shadow-2xs"><svg class="w-full h-full" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/></svg></span>`,
        'mutuo': `<span class="w-4 h-4 rounded-md bg-emerald-600 text-white flex items-center justify-center p-0.5 shrink-0 shadow-2xs"><svg class="w-full h-full" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M3 10h18M7 15h1m4 0h1m-7 4h12a3 3 0 003-3V8a3 3 0 00-3-3H6a3 3 0 00-3 3v8a3 3 0 003 3z"/></svg></span>`,
        'pac': `<span class="w-4 h-4 rounded-md bg-emerald-600 text-white flex items-center justify-center p-0.5 shrink-0 shadow-2xs"><svg class="w-full h-full" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"/></svg></span>`,
        'margine': `<span class="w-4 h-4 rounded-md bg-emerald-600 text-white flex items-center justify-center p-0.5 shrink-0 shadow-2xs"><svg class="w-full h-full" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M7 7h.01M7 3h5a1.99 1.99 0 011.414.586l7 7a2 2 0 010 2.828l-7 7a2 2 0 01-2.828 0l-7-7A1.994 1.994 0 013 12V5a2 2 0 012-2z"/></svg></span>`,
        'estinzione': `<span class="w-4 h-4 rounded-md bg-emerald-600 text-white flex items-center justify-center p-0.5 shrink-0 shadow-2xs"><svg class="w-full h-full" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg></span>`,
        'risparmio': `<span class="w-4 h-4 rounded-md bg-emerald-600 text-white flex items-center justify-center p-0.5 shrink-0 shadow-2xs"><svg class="w-full h-full" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M17 9V7a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2m2 4h10a2 2 0 002-2v-6a2 2 0 00-2-2H9a2 2 0 00-2 2v6a2 2 0 002 2zm7-5a2 2 0 11-4 0 2 2 0 014 0z"/></svg></span>`,
        'fire': `<span class="w-4 h-4 rounded-md bg-emerald-600 text-white flex items-center justify-center p-0.5 shrink-0 shadow-2xs"><svg class="w-full h-full" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M17.657 18.657A8 8 0 016.343 7.343S7 9 9 10c0-2 .5-5 2.986-7C14 5 16.09 5.777 17.656 7.343A7.975 7.975 0 0120 13a7.975 7.975 0 01-2.343 5.657z"/></svg></span>`
    };

    const TOOLS_MAP = {
        'rampe': { name: 'RampaFacile', url: '/rampe', color: 'bg-amber-500' },
        'scale': { name: 'ScalaFacile', url: '/scale', color: 'bg-amber-500' },
        'tubi': { name: 'TubiFacili', url: '/tubi', color: 'bg-amber-500' },
        'tetto': { name: 'TettoFacile', url: '/tetto', color: 'bg-amber-500' },
        'taglio': { name: 'TaglioOttimo', url: '/taglio', color: 'bg-amber-500' },
        'dorso': { name: 'DorsoFacile', url: '/dorso', color: 'bg-rose-700' },
        'dpi': { name: 'Risoluzione', url: '/dpi', color: 'bg-rose-700' },
        'tinta': { name: 'TintaPerfetta', url: '/tinta', color: 'bg-rose-700' },
        'barcode': { name: 'OmniBarcode', url: '/barcode', color: 'bg-rose-700' },
        'copertura': { name: 'Copertura', url: '/copertura', color: 'bg-rose-700' },
        'resa': { name: 'ResaCarta', url: '/resa', color: 'bg-rose-700' },
        'mutuo': { name: 'MutuoFacile', url: '/mutuo', color: 'bg-emerald-600' },
        'pac': { name: 'Interesse', url: '/pac', color: 'bg-emerald-600' },
        'margine': { name: 'MargineFacile', url: '/margine', color: 'bg-emerald-600' },
        'estinzione': { name: 'Estinzione', url: '/estinzione', color: 'bg-emerald-600' },
        'risparmio': { name: 'Risparmio', url: '/risparmio', color: 'bg-emerald-600' },
        'fire': { name: 'FIRE & Rendita', url: '/fire', color: 'bg-emerald-600' }
    };

    const TABS_KEY = 'omni_open_tabs_v1';
    let openTabs = [];
    try {
        openTabs = JSON.parse(sessionStorage.getItem(TABS_KEY)) || [];
    } catch(e) {}

    const pathname = window.location.pathname.replace('.html', '').replace('/', '');
    if (pathname && TOOLS_MAP[pathname]) {
        if (!openTabs.includes(pathname)) {
            openTabs.push(pathname);
            try { sessionStorage.setItem(TABS_KEY, JSON.stringify(openTabs)); } catch(e) {}
        }
    }

    let detachedWindows = {};

    window.OmniMultiWindow = {
        detachTool(id) {
            const tool = TOOLS_MAP[id];
            if (!tool) return;
            if (detachedWindows[id]) return;

            const win = document.createElement('div');
            win.id = `detached-win-${id}`;
            win.className = 'fixed z-[9992] bg-white rounded-2xl shadow-2xl border-2 border-slate-700/80 overflow-hidden flex flex-col';
            win.style.width = 'min(760px, 92vw)';
            win.style.height = 'min(580px, 82vh)';
            win.style.minWidth = '360px';
            win.style.minHeight = '260px';
            win.style.resize = 'both';
            win.style.minHeight = '300px';
            win.style.left = Math.max(20, Math.min(window.innerWidth - 780, 80 + Object.keys(detachedWindows).length * 40)) + 'px';
            win.style.top = (100 + Object.keys(detachedWindows).length * 40) + 'px';

            win.innerHTML = `
                <div class="window-header bg-slate-900 text-white px-3 py-2 flex items-center justify-between cursor-grab active:cursor-grabbing select-none border-b border-slate-800">
                    <div class="flex items-center gap-2">
                        ${TOOL_ICONS_JS[id] || `<span class="w-4 h-4 rounded-md ${tool.color} text-white flex items-center justify-center text-[10px] font-bold">●</span>`}
                        <span class="text-xs font-bold tracking-tight">${tool.name}</span>
                        <span class="text-[9px] font-mono px-1.5 py-0.2 bg-blue-600 rounded text-white font-bold">Finestra Staccata</span>
                    </div>
                    <div class="flex items-center gap-1.5">
                        <button onclick="window.OmniMultiWindow.dockBack('${id}')" title="Riancora nella barra delle schede in alto" class="px-2 py-0.5 rounded bg-slate-800 hover:bg-slate-700 text-sky-400 hover:text-white text-[11px] font-bold transition flex items-center gap-1">
                            <span>⤶</span>
                            <span>Riancora</span>
                        </button>
                        <button onclick="window.OmniMultiWindow.closeDetached('${id}')" title="Chiudi finestra" class="p-1 rounded hover:bg-rose-600 text-slate-300 hover:text-white transition text-xs font-bold">
                            ✕
                        </button>
                    </div>
                </div>
                <div class="flex-1 w-full bg-slate-50 relative overflow-hidden flex flex-col">
                    <iframe src="${tool.url}" class="w-full flex-1 border-0"></iframe>
                    <!-- Resize grip bar at bottom -->
                    <div class="h-4 bg-slate-100 border-t border-slate-200/80 flex items-center justify-between px-2 text-[10px] text-slate-400 select-none">
                        <span class="font-mono">Ridimensiona finestra trascinando i bordi</span>
                        <div class="window-resize-grip w-3.5 h-3.5 flex items-center justify-center cursor-se-resize text-slate-500 hover:text-slate-900 active:text-blue-600 transition" title="Trascina per ridimensionare larghezza e altezza">
                            <svg class="w-3 h-3" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M19 19H5m14-6H11m8-6H17"/></svg>
                        </div>
                    </div>
                </div>
            `;
            document.body.appendChild(win);
            detachedWindows[id] = win;

            makeWindowDraggable(win, win.querySelector('.window-header'));
            makeWindowResizable(win, win.querySelector('.window-resize-grip'));

            openTabs = openTabs.filter(x => x !== id);
            try { sessionStorage.setItem(TABS_KEY, JSON.stringify(openTabs)); } catch(e) {}
            renderChromeTabs();
        },

        dockBack(id) {
            const win = detachedWindows[id];
            if (win) {
                win.remove();
                delete detachedWindows[id];
            }
            if (!openTabs.includes(id)) {
                openTabs.push(id);
                try { sessionStorage.setItem(TABS_KEY, JSON.stringify(openTabs)); } catch(e) {}
            }
            renderChromeTabs();
        },

        closeDetached(id) {
            const win = detachedWindows[id];
            if (win) {
                win.remove();
                delete detachedWindows[id];
            }
        }
    };

    function makeWindowDraggable(el, handle) {
        let isDrag = false, startX, startY, initL, initT;
        function onStart(e) {
            if (e.target.closest('button, select, input, a')) return;
            isDrag = true;
            startX = e.clientX;
            startY = e.clientY;
            const r = el.getBoundingClientRect();
            initL = r.left;
            initT = r.top;
            // Prevent iframe swallowing mouse events while dragging
            const ifr = el.querySelector('iframe');
            if (ifr) ifr.style.pointerEvents = 'none';
            document.addEventListener('mousemove', onMove);
            document.addEventListener('mouseup', onEnd);
        }
        function onMove(e) {
            if (!isDrag) return;
            el.style.left = Math.max(10, Math.min(window.innerWidth - el.offsetWidth - 10, initL + (e.clientX - startX))) + 'px';
            el.style.top = Math.max(10, Math.min(window.innerHeight - el.offsetHeight - 10, initT + (e.clientY - startY))) + 'px';
        }
        function onEnd() {
            isDrag = false;
            const ifr = el.querySelector('iframe');
            if (ifr) ifr.style.pointerEvents = 'auto';
            document.removeEventListener('mousemove', onMove);
            document.removeEventListener('mouseup', onEnd);
        }
        handle.addEventListener('mousedown', onStart);
    }

    function makeWindowResizable(el, handle) {
        let isResizing = false, startX, startY, startW, startH;
        function onResizeStart(e) {
            e.preventDefault();
            e.stopPropagation();
            isResizing = true;
            startX = e.clientX;
            startY = e.clientY;
            startW = el.offsetWidth;
            startH = el.offsetHeight;
            // Temporarily disable iframe pointer events so smooth mousemove works over iframe
            const ifr = el.querySelector('iframe');
            if (ifr) ifr.style.pointerEvents = 'none';
            document.body.style.cursor = 'se-resize';
            document.addEventListener('mousemove', onResizeMove);
            document.addEventListener('mouseup', onResizeEnd);
        }
        function onResizeMove(e) {
            if (!isResizing) return;
            const newW = Math.max(380, Math.min(window.innerWidth - el.offsetLeft - 10, startW + (e.clientX - startX)));
            const newH = Math.max(280, Math.min(window.innerHeight - el.offsetTop - 10, startH + (e.clientY - startY)));
            el.style.width = newW + 'px';
            el.style.height = newH + 'px';
        }
        function onResizeEnd() {
            isResizing = false;
            const ifr = el.querySelector('iframe');
            if (ifr) ifr.style.pointerEvents = 'auto';
            document.body.style.cursor = 'default';
            document.removeEventListener('mousemove', onResizeMove);
            document.removeEventListener('mouseup', onResizeEnd);
        }
        if (handle) {
            handle.addEventListener('mousedown', onResizeStart);
        }
    }

    function renderChromeTabs() {
        const track = document.getElementById('omniChromeTabsTrack');
        if (!track) return;

        const homeTab = document.getElementById('omniTabHome');
        const isHome = (!pathname || pathname === 'index');
        if (homeTab) {
            homeTab.className = isHome 
                ? 'flex items-center gap-1.5 px-3 py-1.5 rounded-t-xl bg-white text-slate-900 font-extrabold border-t-2 border-blue-600 transition shrink-0 text-[11px] shadow-xs'
                : 'flex items-center gap-1.5 px-3 py-1.5 rounded-t-xl bg-slate-800 hover:bg-slate-700 text-slate-300 font-bold border-t-2 border-transparent transition shrink-0 text-[11px]';
        }

        track.querySelectorAll('.omni-dyn-tab').forEach(el => el.remove());

        openTabs.forEach(id => {
            const tool = TOOLS_MAP[id];
            if (!tool) return;
            const isActive = (id === pathname);

            const tab = document.createElement('div');
            tab.className = `omni-dyn-tab group flex items-center gap-1.5 px-3 py-1.5 rounded-t-xl text-[11px] font-bold border-t-2 transition shrink-0 cursor-pointer ${isActive ? 'bg-white text-slate-900 border-blue-600 shadow-xs' : 'bg-slate-800 hover:bg-slate-700 text-slate-300 border-transparent'}`;
            tab.title = 'Trascina in basso o clicca ↗ per staccare in finestra';
            
            const iconMarkup = TOOL_ICONS_JS[id] || `<span class="w-4 h-4 rounded-md ${tool.color} text-white flex items-center justify-center text-[10px] font-bold">●</span>`;
            tab.innerHTML = `
                <a href="${tool.url}" class="flex items-center gap-2 text-inherit no-underline">
                    ${iconMarkup}
                    <span class="truncate max-w-[95px] sm:max-w-[130px] font-bold">${tool.name}</span>
                </a>
                <button onclick="event.preventDefault(); event.stopPropagation(); window.OmniMultiWindow.detachTool('${id}')" title="Stacca in finestra affiancata" class="hover:text-amber-400 px-1 py-0.5 rounded hover:bg-black/10 text-slate-400 font-mono text-[11px] font-bold">
                    ↗
                </button>
                <span class="close-tab hover:text-rose-500 hover:bg-black/10 rounded px-1.5 py-0.5 transition text-slate-400 font-bold" title="Chiudi scheda">✕</span>
            `;

            let tabDragY = 0;
            tab.addEventListener('mousedown', (e) => {
                if (e.target.closest('button, span.close-tab')) return;
                tabDragY = e.clientY;
                function checkDetach(evt) {
                    if (evt.clientY - tabDragY > 40) {
                        document.removeEventListener('mousemove', checkDetach);
                        window.OmniMultiWindow.detachTool(id);
                    }
                }
                function stopCheck() {
                    document.removeEventListener('mousemove', checkDetach);
                    document.removeEventListener('mouseup', stopCheck);
                }
                document.addEventListener('mousemove', checkDetach);
                document.addEventListener('mouseup', stopCheck);
            });

            tab.querySelector('.close-tab').addEventListener('click', (e) => {
                e.preventDefault();
                e.stopPropagation();
                openTabs = openTabs.filter(x => x !== id);
                try { sessionStorage.setItem(TABS_KEY, JSON.stringify(openTabs)); } catch(err) {}
                if (isActive) {
                    const nextId = openTabs.length ? openTabs[openTabs.length - 1] : '';
                    window.location.href = nextId ? TOOLS_MAP[nextId].url : '/';
                } else {
                    renderChromeTabs();
                }
            });

            track.appendChild(tab);
        });
    }

    document.addEventListener('DOMContentLoaded', renderChromeTabs);
})();
"""
