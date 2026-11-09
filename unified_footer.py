# unified_footer.py - Universal Clean & Categorized Footer, Share Strip, Network Ecosystem Bar & Suggestion Modal

def render_unified_footer(current_tool_id, disclaimer_id="legalDisclaimerText", disclaimer_default=""):
    building_tools = [
        {"id": "rampe", "name": "📐 Rampe", "desc": "Pendenza & DM 236", "url": "/rampe"},
        {"id": "scale", "name": "🪜 Scale", "desc": "Gradini & Blondel", "url": "/scale"},
        {"id": "tubi", "name": "🚰 Scarichi", "desc": "Pendenza UNI EN", "url": "/tubi"},
        {"id": "tetto", "name": "🏠 Tetto & Falda", "desc": "Pendenza, Gradi & Trave", "url": "/tetto"},
        {"id": "taglio", "name": "🪚 Taglio 1D", "desc": "Ottimizzatore Barre & Sfrido", "url": "/taglio"},
    ]
    graph_tools = [
        {"id": "dorso", "name": "📕 Dorso", "desc": "Spessore & KDP", "url": "/dorso"},
        {"id": "dpi", "name": "🖼️ DPI / Pixel", "desc": "Stampa & Acuità", "url": "/dpi"},
        {"id": "tinta", "name": "🎯 Tinta & CMYK", "desc": "Scarto & Calibrazione", "url": "/tinta"},
        {"id": "barcode", "name": "🏷️ Barcode", "desc": "Vettoriale & GS1", "url": "/barcode"},
        {"id": "copertura", "name": "🖨️ Copertura", "desc": "Inchiostro & Costi", "url": "/copertura"},
        {"id": "resa", "name": "📑 Resa Carta", "desc": "Nesting & Taglio", "url": "/resa"},
    ]
    finance_tools = [
        {"id": "mutuo", "name": "🏦 Rata Mutuo", "desc": "Ammortamento & Sostenibilità", "url": "/mutuo"},
        {"id": "pac", "name": "📈 Interesse PAC", "desc": "Crescita & Rendita 4%", "url": "/pac"},
        {"id": "margine", "name": "🏷️ Margine & Ricarico", "desc": "COGS, Markup & IVA", "url": "/margine"},
        {"id": "estinzione", "name": "⚡ Estinzione Mutuo", "desc": "Rata vs Anni & Bersani", "url": "/estinzione"},
        {"id": "risparmio", "name": "🎯 Obiettivo Risparmio", "desc": "Sinking Fund & Piano Mensile", "url": "/risparmio"},
        {"id": "fire", "name": "🔥 FIRE & Rendita", "desc": "Libertà & Trinity 4%", "url": "/fire"},
    ]

    def render_pills(tool_list, division_type):
        html = ""
        for t in tool_list:
            is_active = t["id"] == current_tool_id
            if is_active:
                if division_type == "building":
                    bg_active = "bg-blue-600/30 border-blue-400/50"
                    txt_desc = "text-blue-200"
                    badge_bg = "bg-blue-500"
                elif division_type == "finance":
                    bg_active = "bg-emerald-600/30 border-emerald-400/50"
                    txt_desc = "text-emerald-200"
                    badge_bg = "bg-emerald-500"
                else:
                    bg_active = "bg-rose-600/30 border-rose-400/50"
                    txt_desc = "text-rose-200"
                    badge_bg = "bg-rose-500"

                html += f"""
                    <div class="p-2 sm:p-2.5 rounded-xl {bg_active} border flex items-center justify-between transition shadow-xs">
                        <div class="min-w-0 pr-1">
                            <span class="font-bold text-white text-[11px] block truncate">{t['name']}</span>
                            <span class="text-[9px] {txt_desc} block truncate">{t['desc']}</span>
                        </div>
                        <span class="footer-pill-active text-[9px] px-1.5 py-0.5 {badge_bg} text-white font-extrabold rounded shrink-0">Attivo</span>
                    </div>"""
            else:
                html += f"""
                    <a href="{t['url']}" class="p-2 sm:p-2.5 rounded-xl bg-slate-800/80 hover:bg-slate-800 border border-slate-700/80 hover:border-slate-500 flex items-center justify-between transition group">
                        <div class="min-w-0 pr-1">
                            <span class="font-bold text-slate-200 group-hover:text-white text-[11px] block truncate">{t['name']}</span>
                            <span class="text-[9px] text-slate-400 group-hover:text-slate-300 block truncate">{t['desc']}</span>
                        </div>
                        <span class="footer-pill-open text-[9px] px-1.5 py-0.5 bg-slate-700/60 text-slate-300 group-hover:bg-slate-700 group-hover:text-white font-semibold rounded shrink-0">Apri ➔</span>
                    </a>"""
        return html

    building_pills = render_pills(building_tools, "building")
    graph_pills = render_pills(graph_tools, "graph")
    finance_pills = render_pills(finance_tools, "finance")

    default_legal = disclaimer_default if disclaimer_default else "OmniTools Network fornisce utility di precisione a scopo estimativo, didattico e di verifica preliminare. I calcoli tecnici (edilizia, grafica) e finanziari non sostituiscono il parere vincolante di tecnici abilitati o consulenti finanziari abilitati (TUF / D.Lgs. 58/1998)."

    # Smart Related Tools Matrix (Cross-linking for SEO & viral dwell-time)
    related_map = {
        # Building
        "rampe": [
            {"id": "scale", "title": "ScalaFacile", "desc": "Formula Blondel gradini", "badge": "Edilizia", "icon": "🪜", "url": "/scale", "color": "amber"},
            {"id": "tubi", "title": "ScaricoFacile", "desc": "Pendenza tubi UNI EN", "badge": "Impianti", "icon": "🚰", "url": "/tubi", "color": "amber"},
            {"id": "mutuo", "title": "MutuoFacile", "desc": "Rata mutuo casa & 33%", "badge": "Finanza", "icon": "🏦", "url": "/mutuo", "color": "emerald"},
        ],
        "scale": [
            {"id": "rampe", "title": "RampaFacile", "desc": "Pendenza disabili DM 236", "badge": "Edilizia", "icon": "📐", "url": "/rampe", "color": "amber"},
            {"id": "tubi", "title": "ScaricoFacile", "desc": "Pendenza scarichi", "badge": "Impianti", "icon": "🚰", "url": "/tubi", "color": "amber"},
            {"id": "mutuo", "title": "MutuoFacile", "desc": "Preventivo rata mutuo", "badge": "Finanza", "icon": "🏦", "url": "/mutuo", "color": "emerald"},
        ],
        "tubi": [
            {"id": "rampe", "title": "RampaFacile", "desc": "Pendenza cantiere % e °", "badge": "Edilizia", "icon": "📐", "url": "/rampe", "color": "amber"},
            {"id": "scale", "title": "ScalaFacile", "desc": "Alzata e pedata scale", "badge": "Edilizia", "icon": "🪜", "url": "/scale", "color": "amber"},
            {"id": "margine", "title": "MargineFacile", "desc": "Margine e ricarico prezzi", "badge": "Business", "icon": "🏷️", "url": "/margine", "color": "emerald"},
        ],
        # Graph
        "dorso": [
            {"id": "copertura", "title": "CoperturaFacile", "desc": "Analisi CMYK & TAC 300%", "badge": "Stampa", "icon": "🖨️", "url": "/copertura", "color": "rose"},
            {"id": "resa", "title": "ResaCarta", "desc": "Nesting e taglio foglio", "badge": "Tipografia", "icon": "📑", "url": "/resa", "color": "rose"},
            {"id": "dpi", "title": "RisoluzioneFacile", "desc": "DPI ottimali per distanza", "badge": "Grafica", "icon": "🖼️", "url": "/dpi", "color": "rose"},
        ],
        "dpi": [
            {"id": "copertura", "title": "CoperturaFacile", "desc": "Limite inchiostro CMYK", "badge": "Stampa", "icon": "🖨️", "url": "/copertura", "color": "rose"},
            {"id": "dorso", "title": "DorsoFacile", "desc": "Spessore dorso copertina", "badge": "Editoria", "icon": "📕", "url": "/dorso", "color": "rose"},
            {"id": "barcode", "title": "OmniBarcode", "desc": "Codici a barre vettoriali", "badge": "Packaging", "icon": "🏷️", "url": "/barcode", "color": "rose"},
        ],
        "tinta": [
            {"id": "copertura", "title": "CoperturaFacile", "desc": "Consumo grammi inchiostro", "badge": "Stampa", "icon": "🖨️", "url": "/copertura", "color": "rose"},
            {"id": "dpi", "title": "RisoluzioneFacile", "desc": "Pixel in cm per stampa", "badge": "Grafica", "icon": "🖼️", "url": "/dpi", "color": "rose"},
            {"id": "dorso", "title": "DorsoFacile", "desc": "Spessore brossura libro", "badge": "Editoria", "icon": "📕", "url": "/dorso", "color": "rose"},
        ],
        "barcode": [
            {"id": "copertura", "title": "CoperturaFacile", "desc": "Verifica TAC e densità", "badge": "Stampa", "icon": "🖨️", "url": "/copertura", "color": "rose"},
            {"id": "resa", "title": "ResaCarta", "desc": "Ottimizzazione fogli", "badge": "Tipografia", "icon": "📑", "url": "/resa", "color": "rose"},
            {"id": "margine", "title": "MargineFacile", "desc": "Prezzo al consumo & IVA", "badge": "Commercio", "icon": "🏷️", "url": "/margine", "color": "emerald"},
        ],
        "copertura": [
            {"id": "dorso", "title": "DorsoFacile", "desc": "Dorso libro & KDP", "badge": "Editoria", "icon": "📕", "url": "/dorso", "color": "rose"},
            {"id": "resa", "title": "ResaCarta", "desc": "Resa e sfrido di taglio", "badge": "Tipografia", "icon": "📑", "url": "/resa", "color": "rose"},
            {"id": "tinta", "title": "TintaPerfetta", "desc": "Matrice scarto cromatico", "badge": "Colore", "icon": "🎯", "url": "/tinta", "color": "rose"},
        ],
        "resa": [
            {"id": "copertura", "title": "CoperturaFacile", "desc": "Costo copia & CMYK", "badge": "Stampa", "icon": "🖨️", "url": "/copertura", "color": "rose"},
            {"id": "dorso", "title": "DorsoFacile", "desc": "Calcolo pagine & mano", "badge": "Editoria", "icon": "📕", "url": "/dorso", "color": "rose"},
            {"id": "margine", "title": "MargineFacile", "desc": "Ricarico commessa & COGS", "badge": "Pricing", "icon": "🏷️", "url": "/margine", "color": "emerald"},
        ],
        # Finance
        "mutuo": [
            {"id": "pac", "title": "InteresseComposto", "desc": "Simulatore PAC & Regola 4%", "badge": "Investimenti", "icon": "📈", "url": "/pac", "color": "emerald"},
            {"id": "margine", "title": "MargineFacile", "desc": "Margine profitto & ricarico", "badge": "Business", "icon": "🏷️", "url": "/margine", "color": "emerald"},
            {"id": "rampe", "title": "RampaFacile", "desc": "Calcolo pendenza cantiere", "badge": "Edilizia", "icon": "📐", "url": "/rampe", "color": "amber"},
        ],
        "pac": [
            {"id": "mutuo", "title": "MutuoFacile", "desc": "Rata mutuo & ammortamento", "badge": "Finanza", "icon": "🏦", "url": "/mutuo", "color": "emerald"},
            {"id": "margine", "title": "MargineFacile", "desc": "Prezzo di vendita & markup", "badge": "Business", "icon": "🏷️", "url": "/margine", "color": "emerald"},
            {"id": "dorso", "title": "DorsoFacile", "desc": "Spessore libro editoria", "badge": "Grafica", "icon": "📕", "url": "/dorso", "color": "rose"},
        ],
        "margine": [
            {"id": "mutuo", "title": "MutuoFacile", "desc": "Sostenibilità rata/reddito", "badge": "Finanza", "icon": "🏦", "url": "/mutuo", "color": "emerald"},
            {"id": "pac", "title": "InteresseComposto", "desc": "Crescita piano accumulo", "badge": "Investimenti", "icon": "📈", "url": "/pac", "color": "emerald"},
            {"id": "resa", "title": "ResaCarta", "desc": "Ottimizzazione fogli e sfrido", "badge": "Produzione", "icon": "📑", "url": "/resa", "color": "rose"},
        ],
    }

    # Generate Related Cards HTML
    rel_cards = related_map.get(current_tool_id, [
        {"id": "rampe", "title": "RampaFacile", "desc": "Calcolo pendenze DM 236", "badge": "Cantiere", "icon": "📐", "url": "/rampe", "color": "amber"},
        {"id": "dorso", "title": "DorsoFacile", "desc": "Spessore dorso libro", "badge": "Grafica", "icon": "📕", "url": "/dorso", "color": "rose"},
        {"id": "mutuo", "title": "MutuoFacile", "desc": "Ammortamento rata mutuo", "badge": "Finanza", "icon": "🏦", "url": "/mutuo", "color": "emerald"},
    ])

    rel_html = ""
    for r in rel_cards:
        if r['color'] == 'amber':
            b_color = "bg-amber-50 text-amber-800 border-amber-200"
            border_hover = "hover:border-amber-500 hover:bg-amber-50/30"
        elif r['color'] == 'emerald':
            b_color = "bg-emerald-50 text-emerald-800 border-emerald-200"
            border_hover = "hover:border-emerald-500 hover:bg-emerald-50/30"
        else:
            b_color = "bg-rose-50 text-rose-800 border-rose-200"
            border_hover = "hover:border-rose-500 hover:bg-rose-50/30"

        rel_html += f"""
        <a href="{r['url']}" class="group p-3.5 bg-slate-50 hover:bg-white rounded-2xl border border-slate-200/90 {border_hover} transition-all duration-200 shadow-2xs hover:shadow-md flex flex-col justify-between">
            <div class="flex items-center justify-between mb-2">
                <span class="text-xl group-hover:scale-110 transition-transform">{r['icon']}</span>
                <span class="text-[9px] font-extrabold uppercase px-2 py-0.5 rounded-full {b_color} border">{r['badge']}</span>
            </div>
            <div>
                <span class="font-extrabold text-slate-900 group-hover:text-blue-600 text-xs block transition-colors">{r['title']}</span>
                <span class="text-[11px] text-slate-500 line-clamp-1 block mt-0.5">{r['desc']}</span>
            </div>
            <div class="mt-2.5 pt-2 border-t border-slate-200/50 flex items-center justify-between text-[10px] font-bold text-slate-600 group-hover:text-blue-600 transition">
                <span class="footer-rel-open">Apri Calcolatore</span>
                <span class="group-hover:translate-x-1 transition-transform">➔</span>
            </div>
        </a>"""

    return f"""
    <!-- FOOTER WITH OMNITOOLS SUITE & LEGAL DISCLAIMER (Unified Standard) -->
    <footer class="no-print bg-white border-t border-slate-200 pt-8 pb-10 mt-8 text-xs text-slate-500">
        <div class="max-w-5xl mx-auto px-3 sm:px-6 space-y-6">
            
            <!-- SMART CROSS-LINKING: Related Tools (SEO Engine & Retention) -->
            <div class="bg-white rounded-3xl p-5 sm:p-6 border border-slate-200 shadow-xs space-y-3.5">
                <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-1 pb-2 border-b border-slate-100">
                    <div class="flex items-center gap-2">
                        <span class="text-base">⚡</span>
                        <h3 id="footerRelTitle" class="text-xs sm:text-sm font-black text-slate-900 uppercase tracking-wide">Altri Calcolatori Tecnici Consigliati</h3>
                    </div>
                    <span id="footerRelSub" class="text-[10px] font-bold text-slate-400">Precision Utilities • 100% Gratuito</span>
                </div>
                <div class="grid grid-cols-1 sm:grid-cols-3 gap-3">
                    {rel_html}
                </div>
            </div>

            <!-- Share & Viral Action Strip -->
            <div class="bg-white p-3.5 sm:p-4 rounded-2xl border border-slate-200/90 shadow-xs flex flex-col sm:flex-row items-center justify-between gap-3 text-center sm:text-left">
                <div class="flex items-center gap-2.5">
                    <span class="text-xl">📢</span>
                    <div>
                        <span id="shareTitleText" class="text-xs sm:text-sm font-bold text-slate-800 block">Ti è stato utile questo calcolatore?</span>
                        <span id="shareSubText" class="text-[11px] text-slate-500 block">Condividilo con colleghi, collaboratori o clienti</span>
                    </div>
                </div>
                <div class="flex items-center gap-1.5 flex-wrap justify-center shrink-0">
                    <button type="button" onclick="shareWhatsApp()" class="inline-flex items-center gap-1.5 px-2.5 py-1.5 bg-[#25D366] hover:bg-[#20ba59] active:scale-95 text-white text-xs font-bold rounded-xl transition shadow-xs" title="Condividi su WhatsApp">
                        <svg class="w-3.5 h-3.5 fill-current" viewBox="0 0 24 24"><path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.305 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-.999 3.648 3.742-.981zm11.387-5.464c-.074-.124-.272-.198-.57-.347-.297-.149-1.758-.868-2.031-.967-.272-.099-.47-.149-.669.149-.198.297-.768.967-.941 1.165-.173.198-.347.223-.644.074-.297-.149-1.255-.462-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.297-.347.446-.521.151-.172.2-.296.3-.495.099-.198.05-.372-.025-.521-.075-.148-.669-1.611-.916-2.206-.242-.579-.487-.501-.669-.51l-.57-.01c-.198 0-.52.074-.792.372s-1.04 1.016-1.04 2.479 1.065 2.876 1.213 3.074c.149.198 2.095 3.2 5.076 4.487.709.306 1.263.489 1.694.626.712.226 1.36.194 1.872.118.571-.085 1.758-.719 2.006-1.413.248-.695.248-1.29.173-1.414z"/></svg>
                        <span>WhatsApp</span>
                    </button>
                    <button type="button" onclick="shareLinkedIn()" class="inline-flex items-center gap-1.5 px-2.5 py-1.5 bg-[#0A66C2] hover:bg-[#004182] active:scale-95 text-white text-xs font-bold rounded-xl transition shadow-xs" title="Condividi su LinkedIn">
                        <svg class="w-3.5 h-3.5 fill-current" viewBox="0 0 24 24"><path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/></svg>
                        <span>LinkedIn</span>
                    </button>
                    <button type="button" onclick="shareReddit()" class="inline-flex items-center gap-1.5 px-2.5 py-1.5 bg-[#FF4500] hover:bg-[#e03d00] active:scale-95 text-white text-xs font-bold rounded-xl transition shadow-xs" title="Condividi su Reddit">
                        <svg class="w-3.5 h-3.5 fill-current" viewBox="0 0 24 24"><path d="M12 0A12 12 0 0 0 0 12a12 12 0 0 0 12 12 12 12 0 0 0 12-12A12 12 0 0 0 12 0zm5.01 4.744c.688 0 1.25.561 1.25 1.249a1.25 1.25 0 0 1-2.498.056l-2.597-.547-.8 3.747c1.824.07 3.48.632 4.674 1.488.308-.309.73-.491 1.207-.491.968 0 1.754.786 1.754 1.754 0 .716-.435 1.333-1.01 1.614a3.111 3.111 0 0 1 .042.52c0 2.694-3.13 4.87-7.004 4.87-3.874 0-7.004-2.176-7.004-4.87 0-.183.015-.366.043-.534A1.748 1.748 0 0 1 4.028 8.99c0-.968.786-1.754 1.754-1.754.463 0 .898.196 1.207.49 1.207-.883 2.878-1.43 4.744-1.487l.885-4.182a.342.342 0 0 1 .14-.197.35.35 0 0 1 .238-.042l2.906.617a1.214 1.214 0 0 1 1.108-.701zM9.25 12C8.56 12 8 12.56 8 13.25c0 .69.56 1.25 1.25 1.25.69 0 1.25-.56 1.25-1.25 0-.69-.56-1.25-1.25-1.25zm5.5 0c-.69 0-1.25.56-1.25 1.25 0 .69.56 1.25 1.25 1.25.69 0 1.25-.56 1.25-1.25 0-.69-.56-1.25-1.25-1.25zm-5.465 4.542a.335.335 0 0 0-.232.095.33.33 0 0 0 0 .464c.732.732 2.012.986 2.947.986.935 0 2.215-.254 2.947-.986a.33.33 0 0 0 0-.464.335.335 0 0 0-.464 0c-.547.533-1.684.73-2.512.73-.828 0-1.979-.197-2.512-.73a.326.326 0 0 0-.232-.095z"/></svg>
                        <span>Reddit</span>
                    </button>
                    <button type="button" onclick="copyCurrentUrl()" class="inline-flex items-center gap-1.5 px-2.5 py-1.5 bg-slate-100 hover:bg-slate-200 active:scale-95 text-slate-700 text-xs font-bold rounded-xl border border-slate-200 transition" title="Copia Link">
                        <svg class="w-3.5 h-3.5 text-slate-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 16H6a2 2 0 01-2-2V6a2 2 0 012-2h8a2 2 0 012 2v2m-6 12h8a2 2 0 002-2v-8a2 2 0 00-2-2h-8a2 2 0 00-2 2v8a2 2 0 002 2z"/></svg>
                        <span id="shareCopyText">Copia Link</span>
                    </button>
                    <button type="button" onclick="nativeShare()" class="inline-flex sm:hidden items-center gap-1.5 px-2.5 py-1.5 bg-blue-600 hover:bg-blue-500 active:scale-95 text-white text-xs font-bold rounded-xl transition shadow-xs" title="Altre opzioni di condivisione">
                        <svg class="w-3.5 h-3.5 fill-current" viewBox="0 0 24 24"><path d="M18 16.08c-.76 0-1.44.3-1.96.77L8.91 12.7c.05-.23.09-.46.09-.7s-.04-.47-.09-.7l7.05-4.11c.54.5 1.25.81 2.04.81 1.66 0 3-1.34 3-3s-1.34-3-3-3-3 1.34-3 3c0 .24.04.47.09.7L8.04 9.81C7.5 9.31 6.79 9 6 9c-1.66 0-3 1.34-3 3s1.34 3 3 3c.79 0 1.5-.31 2.04-.81l7.12 4.16c-.05.21-.08.43-.08.65 0 1.61 1.31 2.92 2.92 2.92 1.61 0 2.92-1.31 2.92-2.92s-1.31-2.92-2.92-2.92z"/></svg>
                        <span>Condividi</span>
                    </button>
                </div>
            </div>

            <!-- Suggestion Prompt Strip -->
            <div class="bg-gradient-to-r from-blue-50 to-indigo-50/70 border border-blue-200/80 rounded-2xl p-3.5 sm:p-4 flex flex-col sm:flex-row items-center justify-between gap-3 text-center sm:text-left transition shadow-xs">
                <div class="flex items-center gap-2.5">
                    <span class="text-xl">💡</span>
                    <span id="suggestBannerText" class="text-xs sm:text-sm font-bold text-slate-800">
                        Hai un'idea per un nuovo calcolatore di cantiere, grafica o finanza?
                    </span>
                </div>
                <button type="button" onclick="openSuggestModal()" class="px-3.5 py-1.5 bg-blue-600 hover:bg-blue-700 active:scale-95 text-white font-bold text-xs rounded-xl shadow-xs transition shrink-0 inline-flex items-center gap-1">
                    <span id="suggestBtnText">Suggerisci</span>
                    <span>→</span>
                </button>
            </div>

            <!-- Categorized OmniTools Ecosystem Bar (Clean 3-Section Grid) -->
            <div class="bg-slate-900 text-white rounded-2xl p-4 sm:p-5 shadow-lg border border-slate-800 space-y-4">
                <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-1 pb-3 border-b border-slate-800">
                    <div class="flex items-center gap-2">
                        <div class="w-6 h-6 rounded-lg bg-blue-600 flex items-center justify-center font-bold text-white text-xs">
                            ⌘
                        </div>
                        <span class="font-bold text-white text-xs sm:text-sm tracking-wide">OMNITOOLS NETWORK</span>
                    </div>
                    <span id="footerNetSub" class="text-[11px] text-slate-400 font-medium">17 Strumenti Gratuiti • Precision Utilities Suite</span>
                </div>
                
                <!-- Division 1: OmniBuilding (5 Tools) -->
                <div class="space-y-1.5">
                    <div class="text-[10px] font-extrabold uppercase tracking-wider text-amber-400 flex items-center gap-1">
                        <span>🏗️</span> <span id="footerCatBuilding">OmniBuilding (5 Cantiere & Fabbricazione)</span>
                    </div>
                    <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-2">
                        {building_pills}
                    </div>
                </div>

                <!-- Division 2: OmniGraph (6 Tools) -->
                <div class="space-y-1.5 pt-1">
                    <div class="text-[10px] font-extrabold uppercase tracking-wider text-rose-400 flex items-center gap-1">
                        <span>🎨</span> <span id="footerCatGraph">OmniGraph (6 Grafica & Stampa)</span>
                    </div>
                    <div class="grid grid-cols-1 sm:grid-cols-3 gap-2">
                        {graph_pills}
                    </div>
                </div>

                <!-- Division 3: OmniFinance (6 Tools) -->
                <div class="space-y-1.5 pt-1">
                    <div class="text-[10px] font-extrabold uppercase tracking-wider text-emerald-400 flex items-center gap-1">
                        <span>💼</span> <span id="footerCatFinance">OmniFinance (6 Finanza & Libertà)</span>
                    </div>
                    <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-2">
                        {finance_pills}
                    </div>
                </div>

                <!-- Division 4: OmniDesk Utilities (Quick Tools) -->
                <div class="space-y-1.5 pt-1">
                    <div class="text-[10px] font-extrabold uppercase tracking-wider text-amber-300 flex items-center gap-1">
                        <span>⚡</span> <span id="footerCatDesk">OmniDesk — Strumenti Rapidi da Scrivania</span>
                    </div>
                    <div class="grid grid-cols-3 gap-2 text-[11px] text-center font-bold">
                        <a href="/memo" class="p-2 rounded-xl bg-slate-800/80 hover:bg-slate-700 text-amber-300 border border-slate-700/80 transition flex items-center justify-center gap-1">
                            <span>📝</span> <span>Memo</span>
                        </a>
                        <a href="/calcolatrice" class="p-2 rounded-xl bg-slate-800/80 hover:bg-slate-700 text-blue-300 border border-slate-700/80 transition flex items-center justify-center gap-1">
                            <span>🔢</span> <span>Calcolatrice</span>
                        </a>
                        <a href="/orologio" class="p-2 rounded-xl bg-slate-800/80 hover:bg-slate-700 text-teal-300 border border-slate-700/80 transition flex items-center justify-center gap-1">
                            <span>⏱️</span> <span>Orologio</span>
                        </a>
                    </div>
                </div>

                <div class="pt-2 text-center border-t border-slate-800/80">
                    <a href="/partnership" class="inline-flex items-center gap-1.5 text-xs font-bold text-indigo-400 hover:text-indigo-300 transition">
                        <span>🤝</span> <span id="footerPartnerText">Diventa Partner Ufficiale o Sponsor della Suite OmniTools</span>
                    </a>
                </div>
            </div>

            <!-- Disclaimer and Copyright -->
            <div class="text-center space-y-2 pt-2">
                <p id="footerRights" class="font-bold text-slate-700">© 2026 OmniTools Network — Tutti i diritti riservati.</p>
                <p id="{disclaimer_id}" class="text-[10px] text-slate-500 leading-relaxed text-justify sm:text-center max-w-2xl mx-auto">
                    {default_legal}
                </p>
            </div>
        </div>
    </footer>

    <!-- Floating PWA Install Banner -->
    <div id="installBanner" class="no-print hidden fixed bottom-4 right-4 max-w-sm bg-slate-900 text-white p-3.5 rounded-2xl shadow-xl border border-slate-700 z-50 flex items-center justify-between gap-3">
        <div class="flex items-center gap-2.5">
            <span class="text-2xl">📲</span>
            <div>
                <span id="installBannerTitle" class="text-xs font-bold block text-white">Installa OmniTools come App</span>
                <span id="installBannerSub" class="text-[10px] text-slate-400 block">Utility di calcolo professionale sempre a portata di mano</span>
            </div>
        </div>
        <div class="flex items-center gap-1.5 shrink-0">
            <button type="button" onclick="triggerInstall()" class="px-3 py-1 bg-blue-600 hover:bg-blue-500 active:scale-95 text-white text-xs font-bold rounded-xl transition">
                Installa
            </button>
            <button type="button" onclick="dismissInstallBanner()" class="p-1 text-slate-400 hover:text-white rounded-lg transition" title="Chiudi">
                ✕
            </button>
        </div>
    </div>

    <!-- Suggestion Modal Pop-up -->
    <div id="suggestModal" class="no-print hidden fixed inset-0 z-50 bg-slate-900/60 backdrop-blur-xs flex items-center justify-center p-4">
        <div class="bg-white rounded-3xl max-w-md w-full p-5 sm:p-6 shadow-2xl border border-slate-200 space-y-4">
            <div class="flex items-center justify-between border-b border-slate-100 pb-3">
                <div class="flex items-center gap-2">
                    <span class="text-xl">💡</span>
                    <h3 id="modalSuggestTitle" class="text-base font-extrabold text-slate-900">Suggerisci uno Strumento</h3>
                </div>
                <button type="button" onclick="closeSuggestModal()" class="w-7 h-7 rounded-xl bg-slate-100 hover:bg-slate-200 text-slate-600 flex items-center justify-center font-bold text-xs transition">
                    ✕
                </button>
            </div>

            <p id="modalSuggestDesc" class="text-xs text-slate-600 leading-relaxed">
                Quale nuovo calcolatore, formula o funzione vorresti vedere su OmniTools?
            </p>

            <div id="suggestFormContainer" class="space-y-3">
                <textarea id="suggestMessage" rows="3" class="w-full p-3 bg-slate-50 border border-slate-200 rounded-xl text-xs sm:text-sm text-slate-900 focus:bg-white focus:outline-none focus:ring-2 focus:ring-blue-500 transition resize-none" placeholder="Scrivi qui la tua idea..."></textarea>
                
                <div class="flex items-center justify-between text-[10px] text-slate-500">
                    <span id="modalPrivacyNote">🔒 Invio 100% anonimo. Non serve registrarsi.</span>
                </div>

                <div class="flex gap-2 pt-1">
                    <button type="button" onclick="closeSuggestModal()" id="modalCloseBtn" class="flex-1 py-2 rounded-xl border border-slate-200 text-xs font-bold text-slate-700 hover:bg-slate-50 transition active:scale-95">
                        Annulla
                    </button>
                    <button type="button" onclick="submitSuggestion()" id="modalSubmitBtn" class="flex-1 py-2 rounded-xl bg-blue-600 hover:bg-blue-700 text-white text-xs font-bold shadow-md shadow-blue-500/20 active:scale-95 transition">
                        Invia
                    </button>
                </div>
            </div>

            <div id="suggestSuccessContainer" class="hidden text-center py-4 space-y-3">
                <div class="w-12 h-12 mx-auto rounded-2xl bg-emerald-100 text-emerald-600 flex items-center justify-center text-2xl font-bold">
                    ✓
                </div>
                <p id="modalSuccessText" class="text-xs sm:text-sm font-bold text-slate-800 leading-relaxed px-2">
                    Grazie mille! La tua idea è stata registrata e guiderà i prossimi strumenti di OmniTools.
                </p>
                <button type="button" onclick="closeSuggestModal()" class="px-5 py-2 rounded-xl bg-slate-900 text-white text-xs font-bold hover:bg-slate-800 transition">
                    Fatto
                </button>
            </div>
        </div>
    </div>
"""

def render_unified_footer_js():
    return """

        // Global Footer I18N Engine (6 Languages)
        const FOOTER_TRANSLATIONS = {
    "it": {
        "rel_title": "Altri Calcolatori Tecnici Consigliati",
        "rel_sub": "Precision Utilities \u2022 100% Gratuito",
        "rel_open": "Apri Calcolatore",
        "share_title": "Ti \u00e8 stato utile questo calcolatore?",
        "share_sub": "Condividilo con colleghi, collaboratori o clienti",
        "share_copy": "Copia Link",
        "share_copied": "Copiato! \u2713",
        "share_btn": "Condividi",
        "suggest_banner": "Hai un'idea per un nuovo calcolatore di cantiere, grafica o finanza?",
        "suggest_btn": "Suggerisci",
        "net_sub": "17 Strumenti Gratuiti \u2022 Precision Utilities Suite",
        "cat_building": "OmniBuilding (5 Cantiere & Fabbricazione)",
        "cat_graph": "OmniGraph (6 Grafica & Stampa)",
        "cat_finance": "OmniFinance (6 Finanza & Libert\u00e0)",
        "cat_desk": "OmniDesk \u2014 Strumenti Rapidi da Scrivania",
        "partner_text": "Diventa Partner Ufficiale o Sponsor della Suite OmniTools",
        "rights": "\u00a9 2026 OmniTools Network \u2014 Tutti i diritti riservati.",
        "pill_active": "Attivo",
        "pill_open": "Apri \u2794",
        "install_title": "Installa OmniTools come App",
        "install_sub": "Utility di calcolo professionale sempre a portata di mano",
        "install_btn": "Installa",
        "suggest_modal_title": "Suggerisci uno Strumento",
        "suggest_modal_desc": "Quale nuovo calcolatore, formula o funzione vorresti vedere su OmniTools?",
        "suggest_modal_ph": "Scrivi qui la tua idea...",
        "suggest_modal_anon": "🔒 Invio 100% anonimo. Non serve registrarsi.",
        "suggest_modal_cancel": "Annulla",
        "suggest_modal_send": "Invia",
        "suggest_modal_success": "Grazie mille! La tua idea \u00e8 stata registrata e guider\u00e0 i prossimi strumenti di OmniTools.",
        "suggest_modal_done": "Fatto"
    },
    "en": {
        "rel_title": "Other Recommended Technical Calculators",
        "rel_sub": "Precision Utilities \u2022 100% Free",
        "rel_open": "Open Calculator",
        "share_title": "Was this calculator useful to you?",
        "share_sub": "Share it with colleagues, teammates, or clients",
        "share_copy": "Copy Link",
        "share_copied": "Copied! \u2713",
        "share_btn": "Share",
        "suggest_banner": "Have an idea for a new construction, graphics, or finance calculator?",
        "suggest_btn": "Suggest",
        "net_sub": "17 Free Tools \u2022 Precision Utilities Suite",
        "cat_building": "OmniBuilding (5 Construction & Fabrication)",
        "cat_graph": "OmniGraph (6 Graphics & Prepress)",
        "cat_finance": "OmniFinance (6 Finance & Freedom)",
        "cat_desk": "OmniDesk \u2014 Fast Desktop Utilities",
        "partner_text": "Become an Official Partner or Sponsor of OmniTools Suite",
        "rights": "\u00a9 2026 OmniTools Network \u2014 All rights reserved.",
        "pill_active": "Active",
        "pill_open": "Open \u2794",
        "install_title": "Install OmniTools as an App",
        "install_sub": "Professional calculation utilities always at your fingertips",
        "install_btn": "Install",
        "suggest_modal_title": "Suggest a Tool",
        "suggest_modal_desc": "What new calculator, formula, or feature would you like to see on OmniTools?",
        "suggest_modal_ph": "Write your idea here...",
        "suggest_modal_anon": "🔒 100% anonymous submission. No sign-up required.",
        "suggest_modal_cancel": "Cancel",
        "suggest_modal_send": "Send",
        "suggest_modal_success": "Thank you very much! Your suggestion has been saved and will shape upcoming OmniTools.",
        "suggest_modal_done": "Done"
    },
    "es": {
        "rel_title": "Otras Calculadoras T\u00e9cnicas Recomendadas",
        "rel_sub": "Utilidades de Precisi\u00f3n \u2022 100% Gratis",
        "rel_open": "Abrir Calculadora",
        "share_title": "\u00bfTe ha sido \u00fatil esta calculadora?",
        "share_sub": "Comp\u00e1rtela con colegas, colaboradores o clientes",
        "share_copy": "Copiar Enlace",
        "share_copied": "\u00a1Copiado! \u2713",
        "share_btn": "Compartir",
        "suggest_banner": "\u00bfTienes una idea para una nueva calculadora de obra, gr\u00e1fica o finanzas?",
        "suggest_btn": "Sugerir",
        "net_sub": "17 Herramientas Gratuitas \u2022 Precision Utilities Suite",
        "cat_building": "OmniBuilding (5 Construcci\u00f3n y Fabricaci\u00f3n)",
        "cat_graph": "OmniGraph (6 Gr\u00e1fica y Preimpresi\u00f3n)",
        "cat_finance": "OmniFinance (6 Finanzas y Libertad)",
        "cat_desk": "OmniDesk \u2014 Herramientas R\u00e1pidas de Escritorio",
        "partner_text": "Convi\u00e9rtete en Socio Oficial o Patrocinador de la Suite OmniTools",
        "rights": "\u00a9 2026 OmniTools Network \u2014 Todos los derechos reservados.",
        "pill_active": "Activo",
        "pill_open": "Abrir \u2794",
        "install_title": "Instala OmniTools como App",
        "install_sub": "Utilidades de c\u00e1lculo profesional siempre a tu alcance",
        "install_btn": "Instalar",
        "suggest_modal_title": "Sugerir una Herramienta",
        "suggest_modal_desc": "\u00bfQu\u00e9 nueva calculadora, f\u00f3rmula o funci\u00f3n te gustar\u00eda ver en OmniTools?",
        "suggest_modal_ph": "Escribe tu idea aqu\u00ed...",
        "suggest_modal_anon": "🔒 Env\u00edo 100% an\u00f3nimo. Sin registros.",
        "suggest_modal_cancel": "Cancelar",
        "suggest_modal_send": "Enviar",
        "suggest_modal_success": "\u00a1Muchas gracias! Tu idea ha sido registrada y guiar\u00e1 las pr\u00f3ximas herramientas.",
        "suggest_modal_done": "Hecho"
    },
    "fr": {
        "rel_title": "Autres Calculateurs Techniques Recommand\u00e9s",
        "rel_sub": "Utilitaires de Pr\u00e9cision \u2022 100% Gratuit",
        "rel_open": "Ouvrir le Calculateur",
        "share_title": "Ce calculateur vous a-t-il \u00e9t\u00e9 utile ?",
        "share_sub": "Partagez-le avec vos coll\u00e8gues, collaborateurs ou clients",
        "share_copy": "Copier le Lien",
        "share_copied": "Copi\u00e9 ! \u2713",
        "share_btn": "Partager",
        "suggest_banner": "Une id\u00e9e de nouveau calculateur pour le chantier, le graphisme ou la finance ?",
        "suggest_btn": "Sugg\u00e9rer",
        "net_sub": "17 Outils Gratuits \u2022 Precision Utilities Suite",
        "cat_building": "OmniBuilding (5 B\u00e2timent & Fabrication)",
        "cat_graph": "OmniGraph (6 Graphisme & Pr\u00e9presse)",
        "cat_finance": "OmniFinance (6 Finance & Libert\u00e9)",
        "cat_desk": "OmniDesk \u2014 Outils Rapides de Bureau",
        "partner_text": "Devenez Partenaire Officiel ou Sponsor de la Suite OmniTools",
        "rights": "\u00a9 2026 OmniTools Network \u2014 Tous droits r\u00e9serv\u00e9s.",
        "pill_active": "Actif",
        "pill_open": "Ouvrir \u2794",
        "install_title": "Installer OmniTools comme Application",
        "install_sub": "Utilitaires de calcul professionnel toujours \u00e0 port\u00e9e de main",
        "install_btn": "Installer",
        "suggest_modal_title": "Sugg\u00e9rer un Outil",
        "suggest_modal_desc": "Quel calculateur, formule ou fonctionnalit\u00e9 aimeriez-vous voir sur OmniTools ?",
        "suggest_modal_ph": "\u00c9crivez votre id\u00e9e ici...",
        "suggest_modal_anon": "🔒 Envoi 100% anonyme. Aucune inscription requise.",
        "suggest_modal_cancel": "Annuler",
        "suggest_modal_send": "Envoyer",
        "suggest_modal_success": "Merci beaucoup ! Votre id\u00e9e a \u00e9t\u00e9 enregistr\u00e9e pour les prochains outils.",
        "suggest_modal_done": "Termin\u00e9"
    },
    "de": {
        "rel_title": "Weitere Empfohlene Technische Rechner",
        "rel_sub": "Pr\u00e4zisions-Tools \u2022 100% Kostenlos",
        "rel_open": "Rechner \u00d6ffnen",
        "share_title": "War dieser Rechner hilfreich f\u00fcr Sie?",
        "share_sub": "Teilen Sie ihn mit Kollegen, Partnern oder Kunden",
        "share_copy": "Link Kopieren",
        "share_copied": "Kopiert! \u2713",
        "share_btn": "Teilen",
        "suggest_banner": "Haben Sie eine Idee f\u00fcr einen neuen Rechner f\u00fcr Bau, Grafik oder Finanzen?",
        "suggest_btn": "Vorschlagen",
        "net_sub": "17 Kostenlose Tools \u2022 Precision Utilities Suite",
        "cat_building": "OmniBuilding (5 Bau & Fertigung)",
        "cat_graph": "OmniGraph (6 Grafik & Druckvorstufe)",
        "cat_finance": "OmniFinance (6 Finanzen & Freiheit)",
        "cat_desk": "OmniDesk \u2014 Schnelle Schreibtisch-Tools",
        "partner_text": "Werden Sie offizieller Partner oder Sponsor der OmniTools Suite",
        "rights": "\u00a9 2026 OmniTools Network \u2014 Alle Rechte vorbehalten.",
        "pill_active": "Aktiv",
        "pill_open": "\u00d6ffnen \u2794",
        "install_title": "OmniTools als App Installieren",
        "install_sub": "Professionelle Rechenwerkzeuge immer griffbereit",
        "install_btn": "Installieren",
        "suggest_modal_title": "Ein Tool Vorschlagen",
        "suggest_modal_desc": "Welchen neuen Rechner, welche Formel oder Funktion w\u00fcnschen Sie sich bei OmniTools?",
        "suggest_modal_ph": "Schreiben Sie Ihre Idee hier...",
        "suggest_modal_anon": "🔒 100% anonyme \u00dcbermittlung. Keine Registrierung n\u00f6tig.",
        "suggest_modal_cancel": "Abbrechen",
        "suggest_modal_send": "Senden",
        "suggest_modal_success": "Vielen Dank! Ihre Idee wurde gespeichert und flie\u00dft in kommende Tools ein.",
        "suggest_modal_done": "Fertig"
    },
    "pt": {
        "rel_title": "Outras Calculadoras T\u00e9cnicas Recomendadas",
        "rel_sub": "Utilit\u00e1rios de Precis\u00e3o \u2022 100% Gratuito",
        "rel_open": "Abrir Calculadora",
        "share_title": "Esta calculadora foi \u00fatil para voc\u00ea?",
        "share_sub": "Compartilhe com colegas, parceiros ou clientes",
        "share_copy": "Copiar Link",
        "share_copied": "Copiado! \u2713",
        "share_btn": "Compartilhar",
        "suggest_banner": "Tem uma ideia para uma nova calculadora de obra, gr\u00e1fica ou finan\u00e7as?",
        "suggest_btn": "Sugerir",
        "net_sub": "17 Ferramentas Gratuitas \u2022 Precision Utilities Suite",
        "cat_building": "OmniBuilding (5 Constru\u00e7\u00e3o & Fabrica\u00e7\u00e3o)",
        "cat_graph": "OmniGraph (6 Design & Pr\u00e9-impress\u00e3o)",
        "cat_finance": "OmniFinance (6 Finan\u00e7as & Liberdade)",
        "cat_desk": "OmniDesk \u2014 Ferramentas R\u00e1pidas de Secret\u00e1ria",
        "partner_text": "Seja um Parceiro Oficial ou Patrocinador da Suite OmniTools",
        "rights": "\u00a9 2026 OmniTools Network \u2014 Todos os direitos reservados.",
        "pill_active": "Ativo",
        "pill_open": "Abrir \u2794",
        "install_title": "Instalar OmniTools como Aplicativo",
        "install_sub": "Utilit\u00e1rios profissionais de c\u00e1lculo sempre \u00e0 m\u00e3o",
        "install_btn": "Instalar",
        "suggest_modal_title": "Sugerir uma Ferramenta",
        "suggest_modal_desc": "Qual nova calculadora, f\u00f3rmula ou recurso voc\u00ea gostaria de ver no OmniTools?",
        "suggest_modal_ph": "Escreva sua ideia aqui...",
        "suggest_modal_anon": "🔒 Envio 100% an\u00f4nimo. Sem necessidade de cadastro.",
        "suggest_modal_cancel": "Cancelar",
        "suggest_modal_send": "Enviar",
        "suggest_modal_success": "Muito obrigado! Sua ideia foi registrada e guiar\u00e1 as pr\u00f3ximas ferramentas.",
        "suggest_modal_done": "Conclu\u00eddo"
    }
};

        function updateFooterTranslations(lang) {
            const l = FOOTER_TRANSLATIONS[lang] ? lang : "it";
            const tr = FOOTER_TRANSLATIONS[l];

            const relTitle = document.getElementById("footerRelTitle");
            if (relTitle) relTitle.textContent = tr.rel_title;

            const relSub = document.getElementById("footerRelSub");
            if (relSub) relSub.textContent = tr.rel_sub;

            document.querySelectorAll(".footer-rel-open").forEach(el => {
                el.textContent = tr.rel_open;
            });

            const shareTitle = document.getElementById("shareTitleText");
            if (shareTitle) shareTitle.textContent = tr.share_title;

            const shareSub = document.getElementById("shareSubText");
            if (shareSub) shareSub.textContent = tr.share_sub;

            const shareCopy = document.getElementById("shareCopyText");
            if (shareCopy) shareCopy.textContent = tr.share_copy;

            const suggestBanner = document.getElementById("suggestBannerText");
            if (suggestBanner) suggestBanner.textContent = tr.suggest_banner;

            const suggestBtn = document.getElementById("suggestBtnText");
            if (suggestBtn) suggestBtn.textContent = tr.suggest_btn;

            const netSub = document.getElementById("footerNetSub");
            if (netSub) netSub.textContent = tr.net_sub;

            const catB = document.getElementById("footerCatBuilding");
            if (catB) catB.textContent = tr.cat_building;

            const catG = document.getElementById("footerCatGraph");
            if (catG) catG.textContent = tr.cat_graph;

            const catF = document.getElementById("footerCatFinance");
            if (catF) catF.textContent = tr.cat_finance;

            const catDesk = document.getElementById("footerCatDesk");
            if (catDesk) catDesk.textContent = tr.cat_desk;

            const partner = document.getElementById("footerPartnerText");
            if (partner) partner.textContent = tr.partner_text;

            const rights = document.getElementById("footerRights");
            if (rights) rights.textContent = tr.rights;

            document.querySelectorAll(".footer-pill-active").forEach(el => {
                el.textContent = tr.pill_active;
            });

            document.querySelectorAll(".footer-pill-open").forEach(el => {
                el.textContent = tr.pill_open;
            });

            const installT = document.getElementById("installBannerTitle");
            if (installT) installT.textContent = tr.install_title;

            const installS = document.getElementById("installBannerSub");
            if (installS) installS.textContent = tr.install_sub;

            const modalT = document.getElementById("modalSuggestTitle");
            if (modalT) modalT.textContent = tr.suggest_modal_title;

            const modalD = document.getElementById("modalSuggestDesc");
            if (modalD) modalD.textContent = tr.suggest_modal_desc;

            const modalMsg = document.getElementById("suggestMessage");
            if (modalMsg) modalMsg.placeholder = tr.suggest_modal_ph;

            const modalAnon = document.getElementById("modalPrivacyNote");
            if (modalAnon) modalAnon.textContent = tr.suggest_modal_anon;

            const modalClose = document.getElementById("modalCloseBtn");
            if (modalClose) modalClose.textContent = tr.suggest_modal_cancel;

            const modalSubmit = document.getElementById("modalSubmitBtn");
            if (modalSubmit) modalSubmit.textContent = tr.suggest_modal_send;

            const modalSucc = document.getElementById("modalSuccessText");
            if (modalSucc) modalSucc.textContent = tr.suggest_modal_success;
        }

        document.addEventListener("DOMContentLoaded", () => {
            const saved = localStorage.getItem("omnitools_lang") || "it";
            updateFooterTranslations(saved);
        });

        window.addEventListener("omnitools_lang_changed", (e) => {
            if (e.detail && e.detail.lang) updateFooterTranslations(e.detail.lang);
        });

        // Viral Share Functions
        function shareWhatsApp() {
            const url = encodeURIComponent(window.location.href);
            const text = encodeURIComponent(document.title + " su OmniTools Lab: " + window.location.href);
            window.open('https://api.whatsapp.com/send?text=' + text, '_blank');
        }

        function shareLinkedIn() {
            const url = encodeURIComponent(window.location.href);
            window.open('https://www.linkedin.com/sharing/share-offsite/?url=' + url, '_blank');
        }

        function shareReddit() {
            const url = encodeURIComponent(window.location.href);
            const title = encodeURIComponent(document.title);
            window.open('https://reddit.com/submit?url=' + url + '&title=' + title, '_blank');
        }

        function copyCurrentUrl() {
            navigator.clipboard.writeText(window.location.href).then(() => {
                const el = document.getElementById('shareCopyText');
                if (el) {
                    const orig = el.textContent;
                    const curL = localStorage.getItem('omnitools_lang') || 'it'; el.textContent = (FOOTER_TRANSLATIONS[curL] && FOOTER_TRANSLATIONS[curL].share_copied) || 'Copiato! ✓';
                    setTimeout(() => { el.textContent = orig; }, 2000);
                }
            }).catch(() => {
                alert('URL copiato: ' + window.location.href);
            });
        }

        function nativeShare() {
            if (navigator.share) {
                navigator.share({
                    title: document.title,
                    text: document.title + ' su OmniTools Lab',
                    url: window.location.href
                }).catch(() => {});
            } else {
                copyCurrentUrl();
            }
        }

        // Suggestion Modal Functions
        function openSuggestModal() {
            const modal = document.getElementById('suggestModal');
            if (modal) modal.classList.remove('hidden');
        }

        function closeSuggestModal() {
            const modal = document.getElementById('suggestModal');
            if (modal) modal.classList.add('hidden');
        }

        function submitSuggestion() {
            const msgEl = document.getElementById('suggestMessage');
            const msg = msgEl ? msgEl.value.trim() : '';
            if (!msg) {
                alert('Inserisci la tua idea prima di inviare.');
                return;
            }
            const formBox = document.getElementById('suggestFormContainer');
            const successBox = document.getElementById('suggestSuccessContainer');
            if (formBox) formBox.classList.add('hidden');
            if (successBox) successBox.classList.remove('hidden');
        }

        function dismissInstallBanner() {
            const banner = document.getElementById('installBanner');
            if (banner) banner.classList.add('hidden');
        }

        // Dynamically load OmniDesk Workspace Dock (Memo, Calc, Pop Swatch Clock)
        (function() {
            if (!document.getElementById('omnidesk-script')) {
                const s = document.createElement('script');
                s.id = 'omnidesk-script';
                s.src = '/desk_dock.js';
                s.defer = true;
                document.body.appendChild(s);
            }
        })();
"""

if __name__ == "__main__":
    print("unified_footer.py module compiled successfully with 3 divisions (12 tools).")
