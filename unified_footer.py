# unified_footer.py - Universal Footer, Share Strip, Network Ecosystem Bar & Suggestion Modal

def render_unified_footer(current_tool_id, disclaimer_id="legalDisclaimerText", disclaimer_default=""):
    tools = [
        {"id": "rampe", "name": "📐 Rampe", "url": "/rampe", "color": "blue"},
        {"id": "scale", "name": "🪜 Scale", "url": "/scale", "color": "emerald"},
        {"id": "tubi", "name": "🚰 Scarichi", "url": "/tubi", "color": "cyan"},
        {"id": "dorso", "name": "📕 Dorso", "url": "/dorso", "color": "purple"},
        {"id": "dpi", "name": "🖼️ DPI / Pixel", "url": "/dpi", "color": "emerald"},
        {"id": "tinta", "name": "🎯 Tinta & CMYK", "url": "/tinta", "color": "rose"},
        {"id": "barcode", "name": "🏷️ Barcode", "url": "/barcode", "color": "indigo"},
        {"id": "copertura", "name": "🖨️ Copertura", "url": "/copertura", "color": "rose"},
        {"id": "resa", "name": "📑 Resa Carta", "url": "/resa", "color": "amber"}
    ]

    pills_html = ""
    for t in tools:
        is_active = t["id"] == current_tool_id
        if is_active:
            pills_html += f"""
                    <div class="p-2 rounded-xl bg-slate-800 border border-slate-600 flex items-center justify-between transition shadow-xs">
                        <span class="font-bold text-white text-[11px]">{t['name']}</span>
                        <span class="text-[9px] px-1.5 py-0.5 bg-blue-500/20 text-blue-300 font-extrabold rounded">Attivo</span>
                    </div>"""
        else:
            pills_html += f"""
                    <a href="{t['url']}" class="p-2 rounded-xl bg-slate-800/60 hover:bg-slate-800 border border-slate-700/60 hover:border-slate-500 flex items-center justify-between transition group">
                        <span class="font-bold text-slate-300 group-hover:text-white text-[11px]">{t['name']}</span>
                        <span class="text-[9px] px-1.5 py-0.5 bg-slate-700/50 text-slate-400 group-hover:text-slate-200 font-bold rounded">Apri</span>
                    </a>"""

    return f"""
    <!-- FOOTER WITH OMNITOOLS SUITE & LEGAL DISCLAIMER (Unified Standard) -->
    <footer class="no-print bg-white border-t border-slate-200 pt-8 pb-10 mt-8 text-xs text-slate-500">
        <div class="max-w-4xl mx-auto px-4 space-y-6">
            
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
                        <svg class="w-3.5 h-3.5 fill-current" viewBox="0 0 24 24"><path d="M12 0A12 12 0 0 0 0 12a12 12 0 0 0 12 12 12 12 0 0 0 12-12A12 12 0 0 0 12 0zm5.01 4.744c.688 0 1.25.561 1.25 1.249a1.25 1.25 0 0 1-2.498.056l-2.597-.547-.8 3.747c1.824.07 3.48.632 4.674 1.488.308-.309.73-.491 1.207-.491.968 0 1.754.786 1.754 1.754 0 .716-.435 1.333-1.01 1.614a3.111 3.111 0 0 1 .042.52c0 2.694-3.13 4.87-7.004 4.87-3.874 0-7.004-2.176-7.004-4.87 0-.183.015-.366.043-.534A1.748 1.748 0 0 1 4.028 12c0-.968.786-1.754 1.754-1.754.463 0 .898.196 1.207.49 1.207-.883 2.878-1.43 4.744-1.487l.885-4.182a.342.342 0 0 1 .14-.197.35.35 0 0 1 .238-.042l2.906.617a1.214 1.214 0 0 1 1.108-.701zM9.25 12C8.561 12 8 12.562 8 13.25c0 .687.561 1.248 1.25 1.248.687 0 1.248-.561 1.248-1.249 0-.688-.561-1.249-1.249-1.249zm5.5 0c-.687 0-1.248.561-1.248 1.25 0 .687.561 1.248 1.249 1.248.688 0 1.249-.561 1.249-1.249 0-.687-.562-1.249-1.25-1.249zm-5.466 3.99a.327.327 0 0 0-.231.094.33.33 0 0 0 0 .463c.842.842 2.484.913 2.961.913.477 0 2.105-.056 2.961-.913a.361.361 0 0 0 .029-.463.33.33 0 0 0-.464 0c-.547.533-1.684.73-2.512.73-.828 0-1.979-.197-2.512-.73a.326.326 0 0 0-.232-.095z"/></svg>
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
                        Hai un'idea per un nuovo calcolatore di cantiere o grafica?
                    </span>
                </div>
                <button type="button" onclick="openSuggestModal()" class="px-3.5 py-1.5 bg-blue-600 hover:bg-blue-700 active:scale-95 text-white font-bold text-xs rounded-xl shadow-xs transition shrink-0 inline-flex items-center gap-1">
                    <span id="suggestBtnText">Suggerisci</span>
                    <span>→</span>
                </button>
            </div>

            <!-- OmniTools Network Ecosystem Bar (All 8 Tools) -->
            <div class="bg-slate-900 text-white rounded-2xl p-4 sm:p-5 shadow-lg border border-slate-800">
                <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 pb-3 border-b border-slate-800">
                    <div class="flex items-center gap-2">
                        <div class="w-6 h-6 rounded-lg bg-blue-600 flex items-center justify-center text-white text-xs font-bold">
                            ⌘
                        </div>
                        <span class="font-black text-sm tracking-tight font-jakarta">OMNITOOLS <span class="text-blue-400">NETWORK</span></span>
                    </div>
                    <span class="text-[11px] text-slate-400 font-medium">Suite di Calcolatori & Utility di Precisione (Edilizia & Grafica)</span>
                </div>
                
                <div class="grid grid-cols-2 sm:grid-cols-4 md:grid-cols-8 gap-2 pt-3 text-[11px]">
{pills_html}
                </div>
                <div class="pt-2.5 text-center">
                    <a href="/partnership" class="inline-flex items-center gap-1.5 text-xs font-bold text-indigo-400 hover:text-indigo-300 transition">
                        <span>🤝</span> <span>Diventa Partner Ufficiale o Sponsor della Suite OmniTools</span>
                    </a>
                </div>
            </div>

            <!-- Disclaimer and Copyright -->
            <div class="text-center space-y-2">
                <p class="font-bold text-slate-700">© 2026 OmniTools Network — Tutti i diritti riservati.</p>
                <p id="{disclaimer_id}" class="text-[10px] text-slate-500 leading-relaxed text-justify sm:text-center">
                    {disclaimer_default}
                </p>
            </div>
        </div>
    </footer>

    <!-- Smart Floating PWA Install Banner -->
    <div id="installBanner" class="no-print fixed bottom-3 left-3 right-3 sm:left-auto sm:right-6 sm:bottom-6 sm:max-w-sm bg-slate-900 text-white p-3.5 rounded-2xl shadow-2xl border border-slate-700/60 z-50 flex items-center justify-between gap-3 transition-all duration-300 transform translate-y-0">
        <div class="flex items-center gap-2.5 min-w-0">
            <div class="w-9 h-9 rounded-xl bg-blue-600 flex items-center justify-center text-white shrink-0 font-bold shadow-md">
                📱
            </div>
            <div class="min-w-0">
                <span id="installBannerTitle" class="text-xs font-bold block text-white truncate">Installa OmniTools come App</span>
                <span id="installBannerSub" class="text-[10px] text-slate-300 block truncate">Utility di calcolo professionale sempre a portata di mano</span>
            </div>
        </div>
        <div class="flex items-center gap-1.5 shrink-0">
            <button id="installBannerBtn" onclick="triggerInstall()" class="px-3 py-1.5 bg-blue-600 hover:bg-blue-500 text-white rounded-xl text-xs font-bold transition active:scale-95 shadow-sm">
                Installa
            </button>
            <button onclick="dismissInstallBanner()" class="p-1 text-slate-400 hover:text-white rounded-lg text-xs" title="Chiudi">
                ✕
            </button>
        </div>
    </div>

    <!-- Suggestion Modal Pop-up -->
    <div id="suggestModal" class="hidden no-print fixed inset-0 bg-slate-900/60 z-50 flex items-center justify-center p-3 sm:p-4 backdrop-blur-xs">
        <div class="bg-white rounded-3xl p-5 sm:p-6 max-w-md w-full text-slate-800 shadow-2xl border border-slate-100 space-y-3.5 animate-in fade-in zoom-in-95 duration-150">
            <div class="flex justify-between items-start">
                <div class="flex items-center gap-2.5">
                    <div class="w-9 h-9 rounded-xl bg-blue-50 text-blue-600 border border-blue-100 flex items-center justify-center text-lg font-bold">
                        💡
                    </div>
                    <div>
                        <h4 id="modalSuggestTitle" class="font-extrabold text-base text-slate-900 leading-tight">Suggerisci uno Strumento</h4>
                        <span class="text-[10px] text-slate-500 font-medium">OmniTools User Feedback</span>
                    </div>
                </div>
                <button onclick="closeSuggestModal()" class="text-slate-400 hover:text-slate-700 text-xl font-bold p-1 rounded-lg transition">✕</button>
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
        // Viral Share Functions
        function shareWhatsApp() {
            const url = encodeURIComponent(window.location.href);
            const text = encodeURIComponent(document.title + " su OmniTools Lab: " + window.location.href);
            window.open(`https://api.whatsapp.com/send?text=${text}`, '_blank');
        }

        function shareLinkedIn() {
            const url = encodeURIComponent(window.location.href);
            window.open(`https://www.linkedin.com/sharing/share-offsite/?url=${url}

        function shareReddit() {
            const url = encodeURIComponent(window.location.href);
            const title = encodeURIComponent(document.title);
            window.open('https://reddit.com/submit?url=' + url + '&title=' + title, '_blank');
        }`, '_blank');
        }

        function copyCurrentUrl() {
            navigator.clipboard.writeText(window.location.href).then(() => {
                const el = document.getElementById('shareCopyText');
                if (el) {
                    const orig = el.textContent;
                    el.textContent = 'Copiato! ✓';
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
"""
