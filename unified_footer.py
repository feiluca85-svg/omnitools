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
        {"id": "copertura", "name": "🖨️ Copertura", "url": "/copertura", "color": "rose"}
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
                    <button type="button" onclick="shareWhatsApp()" class="inline-flex items-center gap-1.5 px-3 py-1.5 bg-emerald-600 hover:bg-emerald-500 active:scale-95 text-white text-xs font-bold rounded-xl transition shadow-xs" title="Condividi su WhatsApp">
                        <span>💬</span> <span>WhatsApp</span>
                    </button>
                    <button type="button" onclick="shareLinkedIn()" class="inline-flex items-center gap-1.5 px-3 py-1.5 bg-[#0a66c2] hover:bg-[#004182] active:scale-95 text-white text-xs font-bold rounded-xl transition shadow-xs" title="Condividi su LinkedIn">
                        <span>💼</span> <span>LinkedIn</span>
                    </button>
                    <button type="button" onclick="copyCurrentUrl()" class="inline-flex items-center gap-1.5 px-3 py-1.5 bg-slate-100 hover:bg-slate-200 active:scale-95 text-slate-700 text-xs font-bold rounded-xl border border-slate-200 transition" title="Copia Link">
                        <span>🔗</span> <span id="shareCopyText">Copia Link</span>
                    </button>
                    <button type="button" onclick="nativeShare()" class="inline-flex sm:hidden items-center gap-1.5 px-3 py-1.5 bg-blue-600 hover:bg-blue-500 active:scale-95 text-white text-xs font-bold rounded-xl transition shadow-xs" title="Altre opzioni di condivisione">
                        <span>📤</span> <span>Condividi</span>
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
            window.open(`https://www.linkedin.com/sharing/share-offsite/?url=${url}`, '_blank');
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
