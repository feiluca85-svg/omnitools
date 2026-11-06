/**
 * OmniDesk Dock & Widgets Suite
 * OmniMemo (Sticker Notes), OmniCalc (Pocket Calculator), OmniClock (Vintage Pop Swatch Clock)
 * 100% Client-side, LocalStorage persistent, Draggable, Responsive.
 */

(function() {
    // Avoid double initialization
    if (window.__OMNI_DESK_INITIALIZED__) return;
    window.__OMNI_DESK_INITIALIZED__ = true;

    // Load state from localStorage
    const STORAGE_KEY = 'omnidesk_state_v2';
    let deskState = {
        dockExpanded: false,
        clock: { open: false, x: null, y: null, theme: 'teal', size: 'normal' },
        memo: { open: false, x: null, y: null, text: '', color: 'yellow' },
        calc: { open: false, x: null, y: null, current: '0', prev: null, op: null, resetNext: false }
    };

    try {
        const saved = localStorage.getItem(STORAGE_KEY);
        if (saved) {
            const parsed = JSON.parse(saved);
            // Default open state to false on new page load so it never annoys the user!
            deskState = Object.assign(deskState, parsed);
            deskState.clock.open = false;
            deskState.memo.open = false;
            deskState.calc.open = false;
            deskState.dockExpanded = false;
        }
    } catch (e) {
        console.warn('OmniDesk: could not read localStorage', e);
    }

    function saveDeskState() {
        try {
            localStorage.setItem(STORAGE_KEY, JSON.stringify(deskState));
        } catch (e) {}
    }

    // Color palettes for Pop Swatch
    const CLOCK_THEMES = {
        teal: { bg: '#008b8b', face: '#0d9488', dots: '#ffffff', hands: '#2d1b16', rim: '#18181b', accent: '#fde047', label: 'Vintage Teal' },
        coral: { bg: '#e11d48', face: '#f43f5e', dots: '#ffffff', hands: '#1e293b', rim: '#09090b', accent: '#38bdf8', label: 'Pop Coral' },
        yellow: { bg: '#ca8a04', face: '#eab308', dots: '#ffffff', hands: '#1c1917', rim: '#09090b', accent: '#ec4899', label: 'Electric Yellow' },
        violet: { bg: '#7c3aed', face: '#8b5cf6', dots: '#ffffff', hands: '#0f172a', rim: '#09090b', accent: '#4ade80', label: 'Ultra Violet' },
        stealth: { bg: '#0f172a', face: '#1e293b', dots: '#94a3b8', hands: '#f8fafc', rim: '#020617', accent: '#38bdf8', label: 'Dark Stealth' }
    };

    // Color palettes for OmniMemo
    const MEMO_COLORS = {
        yellow: { bg: 'bg-amber-100', border: 'border-amber-300', text: 'text-amber-950', header: 'bg-amber-200/80', dot: '#fef08a' },
        cyan: { bg: 'bg-cyan-100', border: 'border-cyan-300', text: 'text-cyan-950', header: 'bg-cyan-200/80', dot: '#a5f3fc' },
        pink: { bg: 'bg-rose-100', border: 'border-rose-300', text: 'text-rose-950', header: 'bg-rose-200/80', dot: '#fecdd3' },
        mint: { bg: 'bg-emerald-100', border: 'border-emerald-300', text: 'text-emerald-950', header: 'bg-emerald-200/80', dot: '#a7f3d0' },
        lavender: { bg: 'bg-purple-100', border: 'border-purple-300', text: 'text-purple-950', header: 'bg-purple-200/80', dot: '#e9d5ff' }
    };

    // Inject CSS for animations, discreet pill handle and widgets
    const styleEl = document.createElement('style');
    styleEl.textContent = `
        .omnidesk-widget {
            position: fixed;
            z-index: 9999;
            touch-action: none;
            user-select: none;
            filter: drop-shadow(0 15px 30px rgba(0,0,0,0.3));
            transition: transform 0.15s ease, opacity 0.15s ease;
        }
        .omnidesk-clock-bezel {
            box-shadow: inset 0 3px 6px rgba(255,255,255,0.4), 0 8px 24px rgba(0,0,0,0.4);
        }
        .omnidesk-drag-handle {
            cursor: grab;
        }
        .omnidesk-drag-handle:active {
            cursor: grabbing;
        }
        #omnidesk-dock-panel {
            transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1), opacity 0.2s ease;
        }
    `;
    document.head.appendChild(styleEl);

    // ==========================================
    // 0. COMPACT RETRACTABLE DOCK (Discreet Edge Tab)
    // ==========================================
    // On smartphone (screens < 768px), do not show floating tabs that interfere with thumb scrolling!
    // Visible ONLY on desktop/tablet (hidden md:flex).
    const dockContainer = document.createElement('div');
    dockContainer.id = 'omnidesk-dock';
    dockContainer.setAttribute('aria-label', 'OmniDesk Quick Utilities');
    dockContainer.className = 'hidden md:flex fixed right-0 top-1/2 -translate-y-1/2 z-[9990] items-center print:hidden';
    dockContainer.innerHTML = `
        <!-- Collapsible Tray Panel -->
        <div id="omnidesk-dock-panel" class="hidden flex-col items-center bg-slate-900/95 backdrop-blur-md p-1.5 rounded-l-2xl border-y border-l border-slate-700/80 shadow-2xl mr-0">
            <!-- Clock Button -->
            <button id="omnidesk-btn-clock" title="Orologio da banco" class="w-10 h-10 flex items-center justify-center rounded-xl text-teal-400 hover:bg-slate-800 active:scale-90 transition">
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <circle cx="12" cy="12" r="9" stroke-width="2"></circle>
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 7v5l3 2"></path>
                </svg>
            </button>

            <!-- Memo Button -->
            <button id="omnidesk-btn-memo" title="Post-it & Note" class="w-10 h-10 flex items-center justify-center rounded-xl text-amber-400 hover:bg-slate-800 active:scale-90 transition mt-1">
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"></path>
                </svg>
            </button>

            <!-- Calc Button -->
            <button id="omnidesk-btn-calc" title="Calcolatrice rapida" class="w-10 h-10 flex items-center justify-center rounded-xl text-blue-400 hover:bg-slate-800 active:scale-90 transition mt-1">
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <rect x="4" y="2" width="16" height="20" rx="2" stroke-width="2"></rect>
                    <line x1="8" y1="6" x2="16" y2="6" stroke-width="2"></line>
                    <line x1="8" y1="10" x2="10" y2="10" stroke-width="2"></line>
                    <line x1="14" y1="10" x2="16" y2="10" stroke-width="2"></line>
                    <line x1="8" y1="14" x2="10" y2="14" stroke-width="2"></line>
                    <line x1="14" y1="14" x2="16" y2="14" stroke-width="2"></line>
                    <line x1="8" y1="18" x2="16" y2="18" stroke-width="2"></line>
                </svg>
            </button>
        </div>

        <!-- Discreet Trigger Tab (Sits on screen edge, minimal footprint) -->
        <button id="omnidesk-trigger-tab" title="Strumenti da scrivania (Note, Calc, Orologio)" class="bg-slate-900/90 hover:bg-slate-900 text-slate-300 hover:text-white border-y border-l border-slate-700/80 rounded-l-xl px-1.5 py-3 shadow-lg flex flex-col items-center gap-1 active:scale-95 transition">
            <span class="text-[10px] font-black tracking-widest text-amber-400 font-mono">DESK</span>
            <svg id="omnidesk-arrow-icon" class="w-3.5 h-3.5 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M15 19l-7-7 7-7"></path>
            </svg>
        </button>
    `;
    document.body.appendChild(dockContainer);

    const dockPanel = dockContainer.querySelector('#omnidesk-dock-panel');
    const triggerTab = dockContainer.querySelector('#omnidesk-trigger-tab');
    const arrowIcon = dockContainer.querySelector('#omnidesk-arrow-icon');

    function toggleDockPanel(force) {
        const isOpen = typeof force === 'boolean' ? force : dockPanel.classList.contains('hidden');
        if (isOpen) {
            dockPanel.classList.remove('hidden');
            arrowIcon.style.transform = 'rotate(180deg)';
        } else {
            dockPanel.classList.add('hidden');
            arrowIcon.style.transform = 'rotate(0deg)';
        }
    }
    triggerTab.addEventListener('click', () => toggleDockPanel());

    // ==========================================
    // 1. DRAG ENGINE (Touch & Mouse Support)
    // ==========================================
    function makeDraggable(element, handle, onMoveEnd) {
        let isDragging = false;
        let startX, startY, initialLeft, initialTop;

        function startDrag(e) {
            const clientX = e.touches ? e.touches[0].clientX : e.clientX;
            const clientY = e.touches ? e.touches[0].clientY : e.clientY;
            
            if (e.target.closest('button, textarea, input, select, a')) return;

            isDragging = true;
            startX = clientX;
            startY = clientY;

            const rect = element.getBoundingClientRect();
            initialLeft = rect.left;
            initialTop = rect.top;

            document.addEventListener('mousemove', onDrag, { passive: false });
            document.addEventListener('mouseup', endDrag);
            document.addEventListener('touchmove', onDrag, { passive: false });
            document.addEventListener('touchend', endDrag);
        }

        function onDrag(e) {
            if (!isDragging) return;
            e.preventDefault();
            const clientX = e.touches ? e.touches[0].clientX : e.clientX;
            const clientY = e.touches ? e.touches[0].clientY : e.clientY;

            const dx = clientX - startX;
            const dy = clientY - startY;

            let newLeft = initialLeft + dx;
            let newTop = initialTop + dy;

            const maxW = window.innerWidth - element.offsetWidth - 10;
            const maxH = window.innerHeight - element.offsetHeight - 10;
            newLeft = Math.max(10, Math.min(newLeft, maxW));
            newTop = Math.max(10, Math.min(newTop, maxH));

            element.style.left = newLeft + 'px';
            element.style.top = newTop + 'px';
            element.style.right = 'auto';
            element.style.bottom = 'auto';
        }

        function endDrag() {
            if (!isDragging) return;
            isDragging = false;
            document.removeEventListener('mousemove', onDrag);
            document.removeEventListener('mouseup', endDrag);
            document.removeEventListener('touchmove', onDrag);
            document.removeEventListener('touchend', endDrag);
            if (onMoveEnd) {
                const rect = element.getBoundingClientRect();
                onMoveEnd(rect.left, rect.top);
            }
        }

        handle.addEventListener('mousedown', startDrag);
        handle.addEventListener('touchstart', startDrag, { passive: true });
    }

    // ==========================================
    // 2. OMNICLOCK (POP SWATCH EDITION)
    // ==========================================
    const clockWidget = document.createElement('div');
    clockWidget.id = 'omnidesk-clock';
    clockWidget.className = 'omnidesk-widget hidden';
    clockWidget.innerHTML = `
        <div class="relative flex flex-col items-center">
            <!-- Pop Swatch Outer Shell / Bezel -->
            <div id="omnidesk-clock-body" class="omnidesk-drag-handle relative w-[180px] h-[180px] sm:w-[210px] sm:h-[210px] rounded-full bg-zinc-950 p-3 sm:p-3.5 border-4 border-zinc-800 shadow-2xl omnidesk-clock-bezel flex items-center justify-center cursor-grab active:cursor-grabbing">
                
                <!-- Watch Crown / Clip Lug on RIGHT Side (Ore 3) -->
                <div class="absolute -right-3 top-1/2 -translate-y-1/2 w-3 h-8 rounded-r-md bg-zinc-700 border-r border-y border-zinc-500/80 shadow-xs"></div>
                <div class="absolute -right-1.5 top-1/2 -translate-y-1/2 w-2 h-4 bg-amber-400/90 rounded-r-xs"></div>

                <!-- Clock Dial Face -->
                <div id="omnidesk-clock-face" class="relative w-full h-full rounded-full transition-colors duration-300 overflow-hidden shadow-inner flex items-center justify-center">
                    
                    <!-- White Dots for 12 Hours (Clean Dial) -->
                    <div id="omnidesk-clock-dots" class="absolute inset-0"></div>

                    <!-- Center OmniTools Brand Text (Perfect Visibility) -->
                    <div class="absolute flex flex-col items-center pointer-events-none z-10" style="top: 27%;">
                        <span class="text-[11px] sm:text-[13px] font-black tracking-wider text-white uppercase font-sans drop-shadow-[0_1px_2px_rgba(0,0,0,0.8)]">OmniTools</span>
                    </div>

                    <!-- Hands Canvas / SVG -->
                    <svg class="absolute inset-0 w-full h-full pointer-events-none z-20" viewBox="0 0 200 200">
                        <!-- Hour Hand -->
                        <g id="omnidesk-hand-hour" transform="rotate(0 100 100)">
                            <rect x="94" y="42" width="12" height="66" rx="6" fill="#1c1917" stroke="#000" stroke-width="1.5" />
                            <rect x="97" y="46" width="6" height="24" rx="3" fill="#fef08a" />
                        </g>
                        <!-- Minute Hand -->
                        <g id="omnidesk-hand-min" transform="rotate(0 100 100)">
                            <rect x="95" y="22" width="10" height="88" rx="5" fill="#1c1917" stroke="#000" stroke-width="1.5" />
                            <rect x="97.5" y="26" width="5" height="36" rx="2.5" fill="#fef08a" />
                        </g>
                        <!-- Second Hand (Thin Needle) -->
                        <g id="omnidesk-hand-sec" transform="rotate(0 100 100)">
                            <line x1="100" y1="120" x2="100" y2="15" stroke="#f8fafc" stroke-width="2" stroke-linecap="round" />
                            <circle cx="100" cy="100" r="4.5" fill="#f8fafc" />
                            <circle cx="100" cy="30" r="3.5" fill="#f8fafc" />
                        </g>
                        <!-- Center Pin -->
                        <circle cx="100" cy="100" r="5" fill="#18181b" stroke="#ffffff" stroke-width="2" />
                    </svg>

                    <!-- Bottom Accent Text (Above 6 o'clock dot) -->
                    <div class="absolute bottom-11 sm:bottom-12 text-[8px] sm:text-[9px] font-mono tracking-widest uppercase text-white/90 drop-shadow-[0_1px_2px_rgba(0,0,0,0.8)] pointer-events-none font-bold">
                        PRECISION LAB
                    </div>
                </div>
            </div>

            <!-- Mini Control Bar Below Watch -->
            <div class="mt-2 flex items-center gap-1.5 bg-slate-900/90 backdrop-blur-md px-2.5 py-1 rounded-full border border-slate-700/80 shadow-lg">
                <button onclick="window.OmniDesk.setClockTheme('teal')" title="Teal" class="w-4 h-4 rounded-full bg-teal-600 border border-white/60 hover:scale-125 transition"></button>
                <button onclick="window.OmniDesk.setClockTheme('coral')" title="Coral" class="w-4 h-4 rounded-full bg-rose-600 border border-white/60 hover:scale-125 transition"></button>
                <button onclick="window.OmniDesk.setClockTheme('yellow')" title="Giallo" class="w-4 h-4 rounded-full bg-amber-500 border border-white/60 hover:scale-125 transition"></button>
                <button onclick="window.OmniDesk.setClockTheme('violet')" title="Viola" class="w-4 h-4 rounded-full bg-purple-600 border border-white/60 hover:scale-125 transition"></button>
                <button onclick="window.OmniDesk.setClockTheme('stealth')" title="Stealth" class="w-4 h-4 rounded-full bg-slate-800 border border-white/60 hover:scale-125 transition"></button>
                
                <span class="w-[1px] h-3 bg-slate-700 mx-0.5"></span>
                <a href="/orologio" target="_blank" title="Apri a schermo intero" class="text-slate-400 hover:text-white transition p-0.5">
                    <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"></path></svg>
                </a>
                <button onclick="window.OmniDesk.toggleClock(false)" title="Chiudi" class="text-slate-400 hover:text-rose-400 transition p-0.5">
                    <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
                </button>
            </div>
        </div>
    `;
    document.body.appendChild(clockWidget);

    // Build the 12 Dots around the Pop Swatch Dial
    const dotsContainer = clockWidget.querySelector('#omnidesk-clock-dots');
    for (let i = 1; i <= 12; i++) {
        const angle = (i * 30) * (Math.PI / 180);
        const radius = 40;
        const x = 50 + radius * Math.sin(angle);
        const y = 50 - radius * Math.cos(angle);
        
        const dot = document.createElement('div');
        dot.className = 'absolute rounded-full bg-white shadow-xs';
        dot.style.width = '10%';
        dot.style.height = '10%';
        dot.style.left = (x - 5) + '%';
        dot.style.top = (y - 5) + '%';
        dotsContainer.appendChild(dot);
    }

    // Animate the Clock Hands
    function updateClockHands() {
        const now = new Date();
        const ms = now.getMilliseconds();
        const secs = now.getSeconds() + ms / 1000;
        const mins = now.getMinutes() + secs / 60;
        const hours = (now.getHours() % 12) + mins / 60;

        const secDeg = secs * 6;
        const minDeg = mins * 6;
        const hourDeg = hours * 30;

        const secEl = document.getElementById('omnidesk-hand-sec');
        const minEl = document.getElementById('omnidesk-hand-min');
        const hourEl = document.getElementById('omnidesk-hand-hour');

        if (secEl) secEl.setAttribute('transform', `rotate(${secDeg} 100 100)`);
        if (minEl) minEl.setAttribute('transform', `rotate(${minDeg} 100 100)`);
        if (hourEl) hourEl.setAttribute('transform', `rotate(${hourDeg} 100 100)`);

        requestAnimationFrame(updateClockHands);
    }
    requestAnimationFrame(updateClockHands);


    // ==========================================
    // 3. OMNIMEMO (STICKER / POST-IT)
    // ==========================================
    const memoWidget = document.createElement('div');
    memoWidget.id = 'omnidesk-memo';
    memoWidget.className = 'omnidesk-widget hidden w-72 sm:w-80 rounded-2xl shadow-2xl overflow-hidden border transition-all duration-200';
    memoWidget.innerHTML = `
        <div id="omnidesk-memo-header" class="omnidesk-drag-handle flex items-center justify-between px-3 py-2 border-b cursor-grab active:cursor-grabbing">
            <div class="flex items-center gap-2">
                <span class="w-2.5 h-2.5 rounded-full bg-amber-500 shadow-xs"></span>
                <span class="text-xs font-bold font-sans tracking-wide">OmniMemo • Appunti</span>
            </div>
            <div class="flex items-center gap-1.5">
                <button onclick="window.OmniDesk.setMemoColor('yellow')" class="w-3.5 h-3.5 rounded-full bg-amber-300 border border-amber-400 hover:scale-125 transition"></button>
                <button onclick="window.OmniDesk.setMemoColor('cyan')" class="w-3.5 h-3.5 rounded-full bg-cyan-300 border border-cyan-400 hover:scale-125 transition"></button>
                <button onclick="window.OmniDesk.setMemoColor('pink')" class="w-3.5 h-3.5 rounded-full bg-rose-300 border border-rose-400 hover:scale-125 transition"></button>
                <button onclick="window.OmniDesk.setMemoColor('mint')" class="w-3.5 h-3.5 rounded-full bg-emerald-300 border border-emerald-400 hover:scale-125 transition"></button>
                <button onclick="window.OmniDesk.setMemoColor('lavender')" class="w-3.5 h-3.5 rounded-full bg-purple-300 border border-purple-400 hover:scale-125 transition"></button>
                
                <span class="w-[1px] h-3 bg-black/20 mx-1"></span>
                <button onclick="window.OmniDesk.copyMemo()" title="Copia appunti" class="p-1 hover:bg-black/10 rounded-md transition text-slate-700">
                    <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 16H6a2 2 0 01-2-2V6a2 2 0 012-2h8a2 2 0 012 2v2m-6 12h8a2 2 0 002-2v-8a2 2 0 00-2-2h-8a2 2 0 00-2 2v8a2 2 0 002 2z"></path></svg>
                </button>
                <a href="/memo" target="_blank" title="Apri a schermo intero" class="p-1 hover:bg-black/10 rounded-md transition text-slate-700">
                    <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"></path></svg>
                </a>
                <button onclick="window.OmniDesk.toggleMemo(false)" title="Chiudi" class="p-1 hover:bg-rose-500 hover:text-white rounded-md transition text-slate-700">
                    <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
                </button>
            </div>
        </div>
        <div class="p-3">
            <textarea id="omnidesk-memo-area" placeholder="Annota misure, quote, prezzi, formule qui... Si salvano in automatico!" rows="6" class="w-full bg-transparent border-0 outline-none resize-none text-xs sm:text-sm leading-relaxed font-sans placeholder-black/40"></textarea>
            <div class="mt-2 pt-2 border-t border-black/10 flex items-center justify-between text-[10px] opacity-75 font-mono">
                <span id="omnidesk-memo-status">Salvataggio automatico ✓</span>
                <button onclick="window.OmniDesk.clearMemo()" class="hover:underline text-rose-700">Cancella tutto</button>
            </div>
        </div>
    `;
    document.body.appendChild(memoWidget);

    const memoTextarea = memoWidget.querySelector('#omnidesk-memo-area');
    memoTextarea.value = deskState.memo.text || '';
    memoTextarea.addEventListener('input', (e) => {
        deskState.memo.text = e.target.value;
        saveDeskState();
        const st = document.getElementById('omnidesk-memo-status');
        if (st) {
            st.textContent = 'Modificato...';
            setTimeout(() => { st.textContent = 'Salvataggio automatico ✓'; }, 500);
        }
    });


    // ==========================================
    // 4. OMNICALC (POCKET CALCULATOR)
    // ==========================================
    const calcWidget = document.createElement('div');
    calcWidget.id = 'omnidesk-calc';
    calcWidget.className = 'omnidesk-widget hidden w-64 sm:w-72 bg-slate-900 text-white rounded-2xl shadow-2xl overflow-hidden border border-slate-700';
    calcWidget.innerHTML = `
        <div id="omnidesk-calc-header" class="omnidesk-drag-handle flex items-center justify-between px-3.5 py-2.5 bg-slate-800 border-b border-slate-700 cursor-grab active:cursor-grabbing">
            <div class="flex items-center gap-2">
                <span class="w-2.5 h-2.5 rounded-full bg-blue-500 shadow-xs"></span>
                <span class="text-xs font-bold tracking-wide">OmniCalc • Rapida</span>
            </div>
            <div class="flex items-center gap-1.5">
                <a href="/calcolatrice" target="_blank" title="Apri a schermo intero" class="text-slate-400 hover:text-white transition p-0.5">
                    <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"></path></svg>
                </a>
                <button onclick="window.OmniDesk.toggleCalc(false)" class="text-slate-400 hover:text-rose-400 transition p-0.5">
                    <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
                </button>
            </div>
        </div>
        <!-- Display -->
        <div class="p-3.5 bg-slate-950/80 border-b border-slate-800 flex flex-col items-end">
            <span id="omnidesk-calc-history" class="text-[11px] font-mono text-slate-400 h-4 overflow-hidden"></span>
            <span id="omnidesk-calc-display" class="text-2xl font-black font-mono tracking-tight text-white select-all">0</span>
        </div>
        <!-- Keypad -->
        <div class="p-2.5 grid grid-cols-4 gap-1.5 text-xs font-mono font-bold">
            <button onclick="window.OmniDesk.calcAction('C')" class="p-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-rose-400 active:scale-95 transition">C</button>
            <button onclick="window.OmniDesk.calcAction('±')" class="p-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 active:scale-95 transition">±</button>
            <button onclick="window.OmniDesk.calcAction('%')" class="p-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 active:scale-95 transition">%</button>
            <button onclick="window.OmniDesk.calcAction('/')" class="p-2.5 rounded-xl bg-amber-500/20 hover:bg-amber-500 text-amber-300 hover:text-white active:scale-95 transition">÷</button>

            <button onclick="window.OmniDesk.calcDigit('7')" class="p-2.5 rounded-xl bg-slate-800/80 hover:bg-slate-700 text-white active:scale-95 transition">7</button>
            <button onclick="window.OmniDesk.calcDigit('8')" class="p-2.5 rounded-xl bg-slate-800/80 hover:bg-slate-700 text-white active:scale-95 transition">8</button>
            <button onclick="window.OmniDesk.calcDigit('9')" class="p-2.5 rounded-xl bg-slate-800/80 hover:bg-slate-700 text-white active:scale-95 transition">9</button>
            <button onclick="window.OmniDesk.calcAction('*')" class="p-2.5 rounded-xl bg-amber-500/20 hover:bg-amber-500 text-amber-300 hover:text-white active:scale-95 transition">×</button>

            <button onclick="window.OmniDesk.calcDigit('4')" class="p-2.5 rounded-xl bg-slate-800/80 hover:bg-slate-700 text-white active:scale-95 transition">4</button>
            <button onclick="window.OmniDesk.calcDigit('5')" class="p-2.5 rounded-xl bg-slate-800/80 hover:bg-slate-700 text-white active:scale-95 transition">5</button>
            <button onclick="window.OmniDesk.calcDigit('6')" class="p-2.5 rounded-xl bg-slate-800/80 hover:bg-slate-700 text-white active:scale-95 transition">6</button>
            <button onclick="window.OmniDesk.calcAction('-')" class="p-2.5 rounded-xl bg-amber-500/20 hover:bg-amber-500 text-amber-300 hover:text-white active:scale-95 transition">−</button>

            <button onclick="window.OmniDesk.calcDigit('1')" class="p-2.5 rounded-xl bg-slate-800/80 hover:bg-slate-700 text-white active:scale-95 transition">1</button>
            <button onclick="window.OmniDesk.calcDigit('2')" class="p-2.5 rounded-xl bg-slate-800/80 hover:bg-slate-700 text-white active:scale-95 transition">2</button>
            <button onclick="window.OmniDesk.calcDigit('3')" class="p-2.5 rounded-xl bg-slate-800/80 hover:bg-slate-700 text-white active:scale-95 transition">3</button>
            <button onclick="window.OmniDesk.calcAction('+')" class="p-2.5 rounded-xl bg-amber-500/20 hover:bg-amber-500 text-amber-300 hover:text-white active:scale-95 transition">+</button>

            <button onclick="window.OmniDesk.calcDigit('0')" class="col-span-2 p-2.5 rounded-xl bg-slate-800/80 hover:bg-slate-700 text-white text-left pl-5 active:scale-95 transition">0</button>
            <button onclick="window.OmniDesk.calcDigit('.')" class="p-2.5 rounded-xl bg-slate-800/80 hover:bg-slate-700 text-white active:scale-95 transition">.</button>
            <button onclick="window.OmniDesk.calcAction('=')" class="p-2.5 rounded-xl bg-blue-600 hover:bg-blue-500 text-white font-black active:scale-95 transition">=</button>
        </div>
    `;
    document.body.appendChild(calcWidget);

    // Calculator State & Logic
    let calcCurrent = '0';
    let calcPrev = null;
    let calcOp = null;
    let calcResetOnNext = false;

    function updateCalcDisplay() {
        const d = document.getElementById('omnidesk-calc-display');
        const h = document.getElementById('omnidesk-calc-history');
        if (d) d.textContent = calcCurrent;
        if (h) {
            h.textContent = calcPrev !== null && calcOp ? `${calcPrev} ${calcOp}` : '';
        }
    }

    // Keyboard & Numpad Listener for Floating Calculator
    window.addEventListener('keydown', (e) => {
        const calcEl = document.getElementById('omnidesk-calc');
        if (!calcEl || calcEl.classList.contains('hidden')) return;

        // Don't intercept if user is typing in a form input or memo textarea
        const activeTag = document.activeElement ? document.activeElement.tagName.toLowerCase() : '';
        if (['input', 'textarea', 'select'].includes(activeTag)) return;

        if ((e.key >= '0' && e.key <= '9') || e.key === '.') {
            e.preventDefault();
            window.OmniDesk.calcDigit(e.key);
        } else if (e.key === '+') {
            e.preventDefault();
            window.OmniDesk.calcAction('+');
        } else if (e.key === '-') {
            e.preventDefault();
            window.OmniDesk.calcAction('-');
        } else if (e.key === '*' || e.key === 'x') {
            e.preventDefault();
            window.OmniDesk.calcAction('*');
        } else if (e.key === '/') {
            e.preventDefault();
            window.OmniDesk.calcAction('/');
        } else if (e.key === 'Enter' || e.key === '=') {
            e.preventDefault();
            window.OmniDesk.calcAction('=');
        } else if (e.key === 'Escape' || e.key.toLowerCase() === 'c') {
            e.preventDefault();
            window.OmniDesk.calcAction('C');
        } else if (e.key === '%') {
            e.preventDefault();
            window.OmniDesk.calcAction('%');
        } else if (e.key === 'Backspace') {
            e.preventDefault();
            if (calcCurrent.length > 1) {
                calcCurrent = calcCurrent.slice(0, -1);
            } else {
                calcCurrent = '0';
            }
            updateCalcDisplay();
        }
    });

    // ==========================================
    // 5. PUBLIC CONTROLLER API
    // ==========================================
    window.OmniDesk = {
        toggleClock(force) {
            const el = document.getElementById('omnidesk-clock');
            const state = typeof force === 'boolean' ? force : el.classList.contains('hidden');
            deskState.clock.open = state;
            if (state) {
                el.classList.remove('hidden');
                if (deskState.clock.x === null) {
                    el.style.left = Math.max(15, window.innerWidth - 240) + 'px';
                    el.style.top = '100px';
                }
            } else {
                el.classList.add('hidden');
            }
        },

        toggleMemo(force) {
            const el = document.getElementById('omnidesk-memo');
            const state = typeof force === 'boolean' ? force : el.classList.contains('hidden');
            deskState.memo.open = state;
            if (state) {
                el.classList.remove('hidden');
                if (deskState.memo.x === null) {
                    el.style.left = Math.max(15, window.innerWidth - 350) + 'px';
                    el.style.top = '160px';
                }
                const area = document.getElementById('omnidesk-memo-area');
                if (area) area.focus();
            } else {
                el.classList.add('hidden');
            }
        },

        toggleCalc(force) {
            const el = document.getElementById('omnidesk-calc');
            const state = typeof force === 'boolean' ? force : el.classList.contains('hidden');
            deskState.calc.open = state;
            if (state) {
                el.classList.remove('hidden');
                if (deskState.calc.x === null) {
                    el.style.left = Math.max(15, window.innerWidth - 310) + 'px';
                    el.style.top = '220px';
                }
            } else {
                el.classList.add('hidden');
            }
        },

        setClockTheme(themeKey) {
            const t = CLOCK_THEMES[themeKey] || CLOCK_THEMES.teal;
            deskState.clock.theme = themeKey;
            const face = document.getElementById('omnidesk-clock-face');
            if (face) face.style.backgroundColor = t.face;
            saveDeskState();
        },

        setMemoColor(colorKey) {
            const c = MEMO_COLORS[colorKey] || MEMO_COLORS.yellow;
            deskState.memo.color = colorKey;
            const m = document.getElementById('omnidesk-memo');
            const hdr = document.getElementById('omnidesk-memo-header');
            if (m && hdr) {
                m.className = `omnidesk-widget ${c.bg} ${c.border} ${c.text} w-72 sm:w-80 rounded-2xl shadow-2xl overflow-hidden border transition-all duration-200`;
                hdr.className = `omnidesk-drag-handle flex items-center justify-between px-3 py-2 border-b border-black/10 ${c.header} cursor-grab active:cursor-grabbing`;
            }
            saveDeskState();
        },

        copyMemo() {
            const area = document.getElementById('omnidesk-memo-area');
            if (!area) return;
            navigator.clipboard.writeText(area.value).then(() => {
                const st = document.getElementById('omnidesk-memo-status');
                if (st) {
                    st.textContent = 'Copiato negli appunti! ✓';
                    setTimeout(() => { st.textContent = 'Salvataggio automatico ✓'; }, 2000);
                }
            });
        },

        clearMemo() {
            if (confirm('Vuoi davvero cancellare tutti gli appunti salvati?')) {
                const area = document.getElementById('omnidesk-memo-area');
                if (area) area.value = '';
                deskState.memo.text = '';
                saveDeskState();
            }
        },

        calcDigit(d) {
            if (calcResetOnNext) {
                calcCurrent = d === '.' ? '0.' : d;
                calcResetOnNext = false;
            } else {
                if (d === '.' && calcCurrent.includes('.')) return;
                if (calcCurrent === '0' && d !== '.') {
                    calcCurrent = d;
                } else {
                    calcCurrent += d;
                }
            }
            updateCalcDisplay();
        },

        calcAction(act) {
            if (act === 'C') {
                calcCurrent = '0';
                calcPrev = null;
                calcOp = null;
                calcResetOnNext = false;
            } else if (act === '±') {
                calcCurrent = (parseFloat(calcCurrent) * -1).toString();
            } else if (act === '%') {
                calcCurrent = (parseFloat(calcCurrent) / 100).toString();
            } else if (['+', '-', '*', '/'].includes(act)) {
                if (calcPrev !== null && calcOp) {
                    window.OmniDesk.calcAction('=');
                }
                calcPrev = parseFloat(calcCurrent);
                calcOp = act;
                calcResetOnNext = true;
            } else if (act === '=') {
                if (calcPrev === null || !calcOp) return;
                const curr = parseFloat(calcCurrent);
                let res = 0;
                switch (calcOp) {
                    case '+': res = calcPrev + curr; break;
                    case '-': res = calcPrev - curr; break;
                    case '*': res = calcPrev * curr; break;
                    case '/': res = curr === 0 ? 'Errore' : calcPrev / curr; break;
                }
                calcCurrent = typeof res === 'number' ? (Math.round(res * 100000000) / 100000000).toString() : res;
                calcPrev = null;
                calcOp = null;
                calcResetOnNext = true;
            }
            updateCalcDisplay();
        }
    };

    // Attach Dock Buttons
    document.getElementById('omnidesk-btn-clock').addEventListener('click', () => window.OmniDesk.toggleClock());
    document.getElementById('omnidesk-btn-memo').addEventListener('click', () => window.OmniDesk.toggleMemo());
    document.getElementById('omnidesk-btn-calc').addEventListener('click', () => window.OmniDesk.toggleCalc());

    // Make elements draggable & restore saved positions
    makeDraggable(clockWidget, clockWidget.querySelector('#omnidesk-clock-body'), (x, y) => {
        deskState.clock.x = x;
        deskState.clock.y = y;
        saveDeskState();
    });

    makeDraggable(memoWidget, memoWidget.querySelector('#omnidesk-memo-header'), (x, y) => {
        deskState.memo.x = x;
        deskState.memo.y = y;
        saveDeskState();
    });

    makeDraggable(calcWidget, calcWidget.querySelector('#omnidesk-calc-header'), (x, y) => {
        deskState.calc.x = x;
        deskState.calc.y = y;
        saveDeskState();
    });

    // Apply saved positions & themes on boot
    window.OmniDesk.setClockTheme(deskState.clock.theme || 'teal');
    window.OmniDesk.setMemoColor(deskState.memo.color || 'yellow');

    if (deskState.clock.x !== null && deskState.clock.y !== null) {
        clockWidget.style.left = deskState.clock.x + 'px';
        clockWidget.style.top = deskState.clock.y + 'px';
    }
    if (deskState.memo.x !== null && deskState.memo.y !== null) {
        memoWidget.style.left = deskState.memo.x + 'px';
        memoWidget.style.top = deskState.memo.y + 'px';
    }
    if (deskState.calc.x !== null && deskState.calc.y !== null) {
        calcWidget.style.left = deskState.calc.x + 'px';
        calcWidget.style.top = deskState.calc.y + 'px';
    }

    // Always start with widgets closed on initial page view
    window.OmniDesk.toggleClock(false);
    window.OmniDesk.toggleMemo(false);
    window.OmniDesk.toggleCalc(false);

})();
