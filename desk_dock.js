/**
 * OmniDesk Dock & Widgets Suite
 * OmniMemo (Multi-post-it, Sticky Tabs, Dockable), OmniCalc, OmniClock (Pop Swatch Edition)
 * 100% Client-side, LocalStorage persistent, Draggable, Responsive.
 */

(function() {
    if (window.__OMNI_DESK_INITIALIZED__) return;
    window.__OMNI_DESK_INITIALIZED__ = true;

    const STORAGE_KEY = 'omnidesk_state_v4';
    const CLOCK_THEME_KEYS = ['teal', 'coral', 'yellow', 'violet', 'stealth'];

    const CLOCK_THEMES = {
        teal: { bg: '#008b8b', face: '#0d9488', dots: '#ffffff', hands: '#2d1b16', rim: '#18181b', accent: '#fde047', label: 'Vintage Teal', borderNext: '#f43f5e' },
        coral: { bg: '#e11d48', face: '#f43f5e', dots: '#ffffff', hands: '#1e293b', rim: '#09090b', accent: '#38bdf8', label: 'Pop Coral', borderNext: '#eab308' },
        yellow: { bg: '#ca8a04', face: '#eab308', dots: '#ffffff', hands: '#1c1917', rim: '#09090b', accent: '#ec4899', label: 'Electric Yellow', borderNext: '#8b5cf6' },
        violet: { bg: '#7c3aed', face: '#8b5cf6', dots: '#ffffff', hands: '#0f172a', rim: '#09090b', accent: '#4ade80', label: 'Ultra Violet', borderNext: '#334155' },
        stealth: { bg: '#0f172a', face: '#1e293b', dots: '#94a3b8', hands: '#f8fafc', rim: '#020617', accent: '#38bdf8', label: 'Dark Stealth', borderNext: '#0d9488' }
    };

    const MEMO_COLORS = {
        yellow: { bg: 'bg-amber-100', border: 'border-amber-300', text: 'text-amber-950', header: 'bg-amber-200/90', tab: 'bg-amber-300 text-amber-900 border-amber-400', dot: '#fef08a' },
        cyan: { bg: 'bg-cyan-100', border: 'border-cyan-300', text: 'text-cyan-950', header: 'bg-cyan-200/90', tab: 'bg-cyan-300 text-cyan-900 border-cyan-400', dot: '#a5f3fc' },
        pink: { bg: 'bg-rose-100', border: 'border-rose-300', text: 'text-rose-950', header: 'bg-rose-200/90', tab: 'bg-rose-300 text-rose-900 border-rose-400', dot: '#fecdd3' },
        mint: { bg: 'bg-emerald-100', border: 'border-emerald-300', text: 'text-emerald-950', header: 'bg-emerald-200/90', tab: 'bg-emerald-300 text-emerald-900 border-emerald-400', dot: '#a7f3d0' },
        lavender: { bg: 'bg-purple-100', border: 'border-purple-300', text: 'text-purple-950', header: 'bg-purple-200/90', tab: 'bg-purple-300 text-purple-900 border-purple-400', dot: '#e9d5ff' }
    };

    let deskState = {
        clock: { open: false, x: null, y: null, theme: 'teal' },
        calc: { open: false, x: null, y: null, current: '0', prev: null, op: null, resetNext: false },
        memos: [
            { id: 'memo-1', title: 'Appunti #1', text: '', color: 'yellow' }
        ],
        activeMemoId: 'memo-1',
        isMemoOpen: false,
        isMemoDocked: false,
        memoX: null,
        memoY: null
    };

    try {
        const saved = localStorage.getItem(STORAGE_KEY);
        if (saved) {
            const parsed = JSON.parse(saved);
            deskState = Object.assign(deskState, parsed);
        }
    } catch (e) {}

    // Always start closed on load
    deskState.clock.open = false;
    deskState.calc.open = false;
    deskState.isMemoOpen = false;

    function saveDeskState() {
        try {
            localStorage.setItem(STORAGE_KEY, JSON.stringify(deskState));
        } catch (e) {}
    }

    // CSS Styles
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
            transition: border-color 0.25s ease, box-shadow 0.25s ease;
        }
        .omnidesk-drag-handle {
            cursor: grab;
        }
        .omnidesk-drag-handle:active {
            cursor: grabbing;
        }
        /* Chrome-style Tab curves */
        .chrome-tab {
            position: relative;
            background: #1e293b;
            color: #94a3b8;
            padding: 6px 14px;
            font-size: 11px;
            font-weight: 700;
            border-top-left-radius: 10px;
            border-top-right-radius: 10px;
            display: inline-flex;
            align-items: center;
            gap: 6px;
            cursor: pointer;
            transition: background 0.15s ease, color 0.15s ease;
            border: 1px solid rgba(255,255,255,0.08);
            border-bottom: none;
        }
        .chrome-tab.active {
            background: #0f172a;
            color: #ffffff;
            border-color: #38bdf8;
            border-bottom: 2px solid #0f172a;
            box-shadow: 0 -2px 6px rgba(0,0,0,0.3);
        }
        /* Sticky bookmark tab */
        .bookmark-tab {
            transition: transform 0.2s cubic-bezier(0.16, 1, 0.3, 1), opacity 0.15s ease;
        }
        .bookmark-tab:hover {
            transform: translateY(-4px);
        }
        /* Docked strictly in Top-Right Corner */
        .memo-docked {
            position: fixed !important;
            right: 16px !important;
            top: 72px !important;
            left: auto !important;
            bottom: auto !important;
            z-index: 9995 !important;
        }

        /* Resizable Post-it Memo box */
        .omnidesk-resizable {
            resize: both;
            overflow: hidden;
            min-width: 280px;
            min-height: 220px;
            max-width: 90vw;
            max-height: 85vh;
        }

        /* OmniMemo Integrated Post-it Tab Flags */
        #memoTabsContainer::-webkit-scrollbar {
            display: none;
        }
        #memoTabsContainer {
            -ms-overflow-style: none;
            scrollbar-width: none;
        }
        .memo-flag-tab {
            display: inline-flex;
            align-items: center;
            gap: 4px;
            padding: 3px 8px;
            font-size: 11px;
            font-weight: 700;
            border-radius: 6px;
            cursor: pointer;
            white-space: nowrap;
            transition: all 0.15s ease;
            border: 1px solid rgba(0,0,0,0.15);
            flex-shrink: 0;
            user-select: none;
        }
        .memo-flag-tab:hover {
            transform: translateY(-1px);
            box-shadow: 0 2px 4px rgba(0,0,0,0.12);
        }
        .memo-flag-tab.active-tab {
            box-shadow: 0 2px 6px rgba(0,0,0,0.18);
            transform: translateY(-1px);
        }
    `;
    document.head.appendChild(styleEl);

    // ==========================================
    // 1. OMNICLOCK (POP SWATCH EDITION)
    // ==========================================
    const clockWidget = document.createElement('div');
    clockWidget.id = 'omnidesk-clock';
    clockWidget.className = 'omnidesk-widget hidden';
    clockWidget.innerHTML = `
        <div class="relative flex flex-col items-center">
            <!-- Bezel / Cassa -->
            <div id="omnidesk-clock-body" title="Trascina • Clicca sulla cassa per cambiare colore" class="omnidesk-drag-handle relative w-[185px] h-[185px] sm:w-[215px] sm:h-[215px] rounded-full bg-zinc-950 p-3 sm:p-3.5 border-4 border-zinc-800 shadow-2xl omnidesk-clock-bezel flex items-center justify-center cursor-grab active:cursor-grabbing group">
                
                <!-- Crown / Aggancio Ore 3 -->
                <div class="absolute -right-3.5 top-1/2 -translate-y-1/2 w-4 h-9 rounded-r-md bg-zinc-700 border-r border-y border-zinc-500/80 shadow-xs"></div>
                <div class="absolute -right-2 top-1/2 -translate-y-1/2 w-2.5 h-4.5 bg-amber-400/90 rounded-r-xs"></div>

                <!-- Hint Tooltip -->
                <div id="clockNextHint" class="absolute -top-3.5 px-2.5 py-0.5 rounded-full bg-slate-900/95 border border-slate-700 text-[8px] font-mono font-bold text-amber-300 opacity-0 group-hover:opacity-100 transition-opacity pointer-events-none shadow-md whitespace-nowrap z-40">
                    🎨 Clicca cassa per cambiare colore
                </div>

                <!-- Clock Dial Face -->
                <div id="omnidesk-clock-face" class="relative w-full h-full rounded-full transition-colors duration-300 overflow-hidden shadow-inner flex items-center justify-center">
                    
                    <div id="omnidesk-clock-dots" class="absolute inset-0"></div>

                    <!-- Center Brand -->
                    <div class="absolute flex flex-col items-center pointer-events-none z-10" style="top: 28%;">
                        <span class="text-[10.5px] sm:text-[12px] font-black tracking-widest text-white uppercase font-sans drop-shadow-[0_1px_3px_rgba(0,0,0,0.85)]">OmniTools</span>
                    </div>

                    <!-- Hands -->
                    <svg class="absolute inset-0 w-full h-full pointer-events-none z-20" viewBox="0 0 200 200">
                        <g id="omnidesk-hand-hour" transform="rotate(0 100 100)">
                            <rect x="94" y="42" width="12" height="66" rx="6" fill="#1c1917" stroke="#000" stroke-width="1.5" />
                            <rect x="97" y="46" width="6" height="24" rx="3" fill="#fef08a" />
                        </g>
                        <g id="omnidesk-hand-min" transform="rotate(0 100 100)">
                            <rect x="95" y="22" width="10" height="88" rx="5" fill="#1c1917" stroke="#000" stroke-width="1.5" />
                            <rect x="97.5" y="26" width="5" height="36" rx="2.5" fill="#fef08a" />
                        </g>
                        <g id="omnidesk-hand-sec" transform="rotate(0 100 100)">
                            <line x1="100" y1="120" x2="100" y2="15" stroke="#f8fafc" stroke-width="2" stroke-linecap="round" />
                            <circle cx="100" cy="100" r="4.5" fill="#f8fafc" />
                            <circle cx="100" cy="30" r="3.5" fill="#f8fafc" />
                        </g>
                        <circle cx="100" cy="100" r="5" fill="#18181b" stroke="#ffffff" stroke-width="2" />
                    </svg>

                    <div class="absolute bottom-11 sm:bottom-12 text-[7.5px] sm:text-[8.5px] font-mono tracking-widest uppercase text-white/90 drop-shadow-[0_1px_2px_rgba(0,0,0,0.8)] pointer-events-none font-bold">
                        PRECISION LAB
                    </div>
                </div>
            </div>
        </div>
    `;
    document.body.appendChild(clockWidget);

    // Build the 12 Dots
    const dotsContainer = clockWidget.querySelector('#omnidesk-clock-dots');
    for (let i = 1; i <= 12; i++) {
        const angle = (i * 30) * (Math.PI / 180);
        const radius = 40;
        const x = 50 + radius * Math.sin(angle);
        const y = 50 - radius * Math.cos(angle);
        
        const dot = document.createElement('div');
        dot.style.width = '10%';
        dot.style.height = '10%';
        dot.style.left = (x - 5) + '%';
        dot.style.top = (y - 5) + '%';

        if (i === 10) {
            // Ore 10: X più grande e spessa
            dot.className = 'absolute rounded-full bg-white hover:bg-rose-500 text-slate-800 hover:text-white flex items-center justify-center font-black cursor-pointer shadow-md transition-all duration-150 active:scale-90 z-30 select-none';
            dot.title = 'Chiudi Orologio';
            dot.innerHTML = `<span style="font-size: 13px; font-weight: 900; line-height: 1; transform: scale(1.15);">✕</span>`;
            dot.addEventListener('click', (e) => {
                e.stopPropagation();
                window.OmniDesk.toggleClock(false);
            });
        } else if (i === 6) {
            // Ore 6: Freccia triangolare rivolta verso il basso (▼)
            dot.className = 'absolute rounded-full bg-white hover:bg-blue-600 text-slate-800 hover:text-white flex items-center justify-center font-black cursor-pointer shadow-md transition-all duration-150 active:scale-90 z-30 select-none';
            dot.title = 'Installa / Apri a Schermo Intero';
            dot.innerHTML = `<span style="font-size: 11px; line-height: 1; transform: translateY(0.5px);">▼</span>`;
            dot.addEventListener('click', (e) => {
                e.stopPropagation();
                window.open('/orologio', '_blank');
            });
        } else {
            dot.className = 'absolute rounded-full bg-white shadow-xs pointer-events-none';
        }
        dotsContainer.appendChild(dot);
    }

    // Bezel click & hover anticipation logic
    const clockBody = clockWidget.querySelector('#omnidesk-clock-body');
    let isClockDragging = false;
    clockBody.addEventListener('mousedown', () => { isClockDragging = false; });
    clockBody.addEventListener('mousemove', () => { isClockDragging = true; });

    function updateBezelHoverColor() {
        const curIdx = CLOCK_THEME_KEYS.indexOf(deskState.clock.theme || 'teal');
        const nextKey = CLOCK_THEME_KEYS[(curIdx + 1) % CLOCK_THEME_KEYS.length];
        const nextTheme = CLOCK_THEMES[nextKey];
        // Preview border color on hover
        clockBody.style.borderColor = nextTheme.face;
        clockBody.style.boxShadow = `0 0 20px ${nextTheme.face}55, inset 0 3px 6px rgba(255,255,255,0.4), 0 8px 24px rgba(0,0,0,0.4)`;
        const hint = document.getElementById('clockNextHint');
        if (hint) {
            hint.textContent = `🎨 Clicca per: ${nextTheme.label}`;
            hint.style.borderColor = nextTheme.face;
        }
    }

    function resetBezelHoverColor() {
        clockBody.style.borderColor = '#27272a';
        clockBody.style.boxShadow = 'inset 0 3px 6px rgba(255,255,255,0.4), 0 8px 24px rgba(0,0,0,0.4)';
    }

    clockBody.addEventListener('mouseenter', updateBezelHoverColor);
    clockBody.addEventListener('mouseleave', resetBezelHoverColor);

    clockBody.addEventListener('click', (e) => {
        if (isClockDragging) return;
        if (e.target.closest('#omnidesk-clock-body') && !e.target.closest('[title="Chiudi Orologio"], [title="Installa / Apri a Schermo Intero"]')) {
            window.OmniDesk.cycleClockTheme();
            updateBezelHoverColor();
        }
    });

    // Clock Animation Hands
    function updateClockHands() {
        const now = new Date();
        const ms = now.getMilliseconds();
        const secs = now.getSeconds() + ms / 1000;
        const mins = now.getMinutes() + secs / 60;
        const hours = (now.getHours() % 12) + mins / 60;

        const secEl = document.getElementById('omnidesk-hand-sec');
        const minEl = document.getElementById('omnidesk-hand-min');
        const hourEl = document.getElementById('omnidesk-hand-hour');

        if (secEl) secEl.setAttribute('transform', `rotate(${secs * 6} 100 100)`);
        if (minEl) minEl.setAttribute('transform', `rotate(${mins * 6} 100 100)`);
        if (hourEl) hourEl.setAttribute('transform', `rotate(${hours * 30} 100 100)`);

        requestAnimationFrame(updateClockHands);
    }
    requestAnimationFrame(updateClockHands);


    // ==========================================
    // 2. OMNIMEMO ADVANCED (RESIZABLE, TOP-RIGHT PIN, INTEGRATED TAB STRIP)
    // ==========================================
    const memoWidget = document.createElement('div');
    memoWidget.id = 'omnidesk-memo';
    memoWidget.className = 'omnidesk-widget hidden fixed z-[9993]';
    memoWidget.innerHTML = `
        <!-- Resizable Post-it Pad Body -->
        <div id="memoPadBody" class="omnidesk-resizable w-80 sm:w-88 rounded-2xl shadow-2xl border flex flex-col transition-colors duration-150 relative">
            <!-- Memo Window Header (Draggable) -->
            <div id="memoWindowHeader" class="omnidesk-drag-handle flex items-center justify-between px-3 py-2 border-b border-black/10 select-none cursor-grab active:cursor-grabbing shrink-0">
                <div class="flex items-center gap-1.5">
                    <span class="w-2.5 h-2.5 rounded-full bg-amber-500 shadow-xs"></span>
                    <span class="text-xs font-black font-sans tracking-wide">OmniMemo</span>
                    <span id="memoCountBadge" class="text-[9px] font-mono px-1.5 py-0.2 rounded-full bg-black/10 font-bold">1</span>
                </div>

                <div class="flex items-center gap-1.5 shrink-0">
                    <!-- Color Selector Dots -->
                    <div class="flex items-center gap-1 mr-1">
                        <button onclick="window.OmniDesk.setCurMemoColor('yellow')" title="Giallo" class="w-3.5 h-3.5 rounded-full bg-amber-300 border border-amber-400 hover:scale-125 transition cursor-pointer"></button>
                        <button onclick="window.OmniDesk.setCurMemoColor('cyan')" title="Azzurro" class="w-3.5 h-3.5 rounded-full bg-cyan-300 border border-cyan-400 hover:scale-125 transition cursor-pointer"></button>
                        <button onclick="window.OmniDesk.setCurMemoColor('pink')" title="Rosa" class="w-3.5 h-3.5 rounded-full bg-rose-300 border border-rose-400 hover:scale-125 transition cursor-pointer"></button>
                        <button onclick="window.OmniDesk.setCurMemoColor('mint')" title="Menta" class="w-3.5 h-3.5 rounded-full bg-emerald-300 border border-emerald-400 hover:scale-125 transition cursor-pointer"></button>
                        <button onclick="window.OmniDesk.setCurMemoColor('lavender')" title="Lavanda" class="w-3.5 h-3.5 rounded-full bg-purple-300 border border-purple-400 hover:scale-125 transition cursor-pointer"></button>
                    </div>

                    <span class="w-[1px] h-3 bg-black/20 mx-0.5"></span>

                    <!-- Add New Memo Button -->
                    <button onclick="window.OmniDesk.addNewMemo()" title="Aggiungi nuovo foglietto (+)" class="p-1 rounded-md hover:bg-black/10 transition text-slate-800 text-xs font-bold cursor-pointer">
                        ➕
                    </button>
                    <!-- Pin to Top-Right Corner -->
                    <button id="memoDockPinBtn" onclick="window.OmniDesk.toggleMemoDock()" title="Incolla nell'angolo in alto a destra" class="p-1 rounded-md hover:bg-black/10 transition text-slate-800 text-xs font-bold cursor-pointer">
                        📌
                    </button>
                    <!-- Close Button -->
                    <button onclick="window.OmniDesk.toggleMemo(false)" title="Chiudi Memo" class="p-1 rounded-md hover:bg-rose-500 hover:text-white transition text-slate-800 text-xs font-black cursor-pointer">
                        ✕
                    </button>
                </div>
            </div>

            <!-- Integrated Post-it Note Index Tab Flags Strip -->
            <div id="memoTabsContainer" class="flex items-center gap-1.5 px-2.5 py-1.5 border-b border-black/10 overflow-x-auto no-scrollbar shrink-0 select-none bg-black/5"></div>

            <!-- Editable Title Bar -->
            <div class="px-3 pt-2 pb-1 border-b border-black/10 shrink-0">
                <input id="memoTitleInput" type="text" placeholder="Nome di questo foglietto..." class="w-full bg-transparent border-0 outline-none text-xs font-extrabold font-sans tracking-tight placeholder-black/35" />
            </div>

            <!-- Memo Text Area (Expands with container resize) -->
            <div class="p-3 flex-1 flex flex-col min-h-0">
                <textarea id="memoTextArea" placeholder="Annota misure, formule, quote qui... Allunga il foglietto trascinando l'angolo in basso a destra!" class="w-full flex-1 bg-transparent border-0 outline-none resize-none text-xs sm:text-sm leading-relaxed font-sans placeholder-black/35 font-medium"></textarea>

                <!-- Bottom Status Bar -->
                <div class="mt-2 pt-2 border-t border-black/10 flex items-center justify-between text-[10px] opacity-80 font-mono shrink-0">
                    <span id="memoSaveStatus">Salvataggio automatico ✓</span>
                    <div class="flex items-center gap-3">
                        <button onclick="window.OmniDesk.copyCurMemo()" class="hover:underline font-bold text-slate-800 cursor-pointer">Copia</button>
                        <button onclick="window.OmniDesk.deleteCurMemo()" class="hover:underline text-rose-700 font-bold cursor-pointer">Elimina</button>
                    </div>
                </div>
            </div>
        </div>
    `;
    document.body.appendChild(memoWidget);

    function getActiveMemo() {
        return deskState.memos.find(m => m.id === deskState.activeMemoId) || deskState.memos[0];
    }

    function updateMemoTabsSide() {}

    function renderTabsInto(container) {
        container.innerHTML = '';
        deskState.memos.forEach((item, idx) => {
            const itemCol = MEMO_COLORS[item.color || 'yellow'];
            const isActive = (item.id === deskState.activeMemoId);
            
            const tab = document.createElement('button');
            tab.type = 'button';
            tab.className = `memo-flag-tab ${itemCol.tab} ${isActive ? 'active-tab ring-2 ring-black/30' : 'opacity-70 hover:opacity-100'}`;
            tab.title = item.title || `Nota #${idx + 1}`;
            
            const tabIcon = isActive ? '📌' : '🔖';
            tab.innerHTML = `
                <span class="text-xs shrink-0">${tabIcon}</span>
                <span class="text-[11px] font-bold truncate max-w-[100px]">${item.title || `Nota #${idx + 1}`}</span>
            `;

            tab.addEventListener('click', (e) => {
                e.stopPropagation();
                deskState.activeMemoId = item.id;
                saveDeskState();
                renderActiveMemo();
            });

            container.appendChild(tab);
        });

        // Quick add button at the end of tab strip
        const addBtn = document.createElement('button');
        addBtn.type = 'button';
        addBtn.className = 'w-6 h-6 rounded-md bg-black/10 hover:bg-black/20 text-slate-800 flex items-center justify-center text-xs font-black shrink-0 transition cursor-pointer';
        addBtn.title = 'Aggiungi nuovo foglietto';
        addBtn.innerHTML = '＋';
        addBtn.addEventListener('click', (e) => {
            e.stopPropagation();
            window.OmniDesk.addNewMemo();
        });
        container.appendChild(addBtn);
    }

    function renderActiveMemo() {
        const m = getActiveMemo();
        if (!m) return;

        const padBody = document.getElementById('memoPadBody');
        const titleInput = document.getElementById('memoTitleInput');
        const textArea = document.getElementById('memoTextArea');
        const header = document.getElementById('memoWindowHeader');
        const col = MEMO_COLORS[m.color || 'yellow'];

        // Apply colors and styling to padBody
        if (padBody) {
            padBody.className = `omnidesk-resizable w-80 sm:w-88 rounded-2xl shadow-2xl border flex flex-col transition-colors duration-150 ${col.bg} ${col.border} ${col.text}`;
        }

        // Apply dock or drag classes to memoWidget
        memoWidget.className = `omnidesk-widget ${deskState.isMemoOpen ? '' : 'hidden'} fixed z-[9993] ${deskState.isMemoDocked ? 'memo-docked' : ''}`;
        if (deskState.isMemoDocked) {
            memoWidget.style.left = 'auto';
            memoWidget.style.top = '68px';
            memoWidget.style.right = '12px';
            memoWidget.style.bottom = 'auto';
        } else {
            memoWidget.style.right = 'auto';
            memoWidget.style.bottom = 'auto';
            if (deskState.memoX !== null && deskState.memoY !== null) {
                memoWidget.style.left = deskState.memoX + 'px';
                memoWidget.style.top = deskState.memoY + 'px';
            }
        }
        if (header) {
            header.className = `omnidesk-drag-handle flex items-center justify-between px-3 py-2 border-b border-black/10 ${col.header} select-none cursor-grab active:cursor-grabbing shrink-0`;
        }

        if (titleInput) titleInput.value = m.title || '';
        if (textArea) textArea.value = m.text || '';

        const pinBtn = document.getElementById('memoDockPinBtn');
        if (pinBtn) {
            pinBtn.textContent = deskState.isMemoDocked ? '🔓' : '📌';
            pinBtn.title = deskState.isMemoDocked ? "Sblocca dall'angolo in alto a destra" : "Incolla nell'angolo in alto a destra";
        }

        const badge = document.getElementById('memoCountBadge');
        if (badge) badge.textContent = `${deskState.memos.length}`;

        // Populate smart tabs container
        const cont = document.getElementById('memoTabsContainer');
        if (cont) renderTabsInto(cont);

        // Update active side (left or right)
        updateMemoTabsSide();
    }

    const titleInput = memoWidget.querySelector('#memoTitleInput');
    const textArea = memoWidget.querySelector('#memoTextArea');

    titleInput.addEventListener('input', () => {
        const m = getActiveMemo();
        if (!m) return;
        m.title = titleInput.value;
        saveDeskState();
        renderMemoTabs();
    });

    textArea.addEventListener('input', () => {
        const m = getActiveMemo();
        if (!m) return;
        m.text = textArea.value;
        saveDeskState();
        const st = document.getElementById('memoSaveStatus');
        if (st) {
            st.textContent = 'Modificato...';
            setTimeout(() => { st.textContent = 'Salvataggio automatico ✓'; }, 500);
        }
    });
    // ==========================================
    // 3. OMNICALC (POCKET CALCULATOR)
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
        <div class="p-3.5 bg-slate-950/80 border-b border-slate-800 flex flex-col items-end">
            <span id="omnidesk-calc-history" class="text-[11px] font-mono text-slate-400 h-4 overflow-hidden"></span>
            <span id="omnidesk-calc-display" class="text-2xl font-black font-mono tracking-tight text-white select-all">0</span>
        </div>
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

    let calcCurrent = '0';
    let calcPrev = null;
    let calcOp = null;
    let calcResetOnNext = false;

    function updateCalcDisplay() {
        const d = document.getElementById('omnidesk-calc-display');
        const h = document.getElementById('omnidesk-calc-history');
        if (d) d.textContent = calcCurrent;
        if (h) h.textContent = calcPrev !== null && calcOp ? `${calcPrev} ${calcOp}` : '';
    }

    // Numpad key listeners
    window.addEventListener('keydown', (e) => {
        const calcEl = document.getElementById('omnidesk-calc');
        if (!calcEl || calcEl.classList.contains('hidden')) return;

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
            calcCurrent = calcCurrent.length > 1 ? calcCurrent.slice(0, -1) : '0';
            updateCalcDisplay();
        }
    });

    // ==========================================
    // 4. PUBLIC CONTROLLER API
    // ==========================================
    window.OmniDesk = {
        updateMemoTabsSide(x) {
            updateMemoTabsSide(x);
        },
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

        cycleClockTheme() {
            const curIdx = CLOCK_THEME_KEYS.indexOf(deskState.clock.theme || 'teal');
            const nextKey = CLOCK_THEME_KEYS[(curIdx + 1) % CLOCK_THEME_KEYS.length];
            window.OmniDesk.setClockTheme(nextKey);
        },

        setClockTheme(themeKey) {
            const t = CLOCK_THEMES[themeKey] || CLOCK_THEMES.teal;
            deskState.clock.theme = themeKey;
            const face = document.getElementById('omnidesk-clock-face');
            if (face) face.style.backgroundColor = t.face;
            saveDeskState();
        },

        // Memo Controls
        toggleMemo(force) {
            const state = typeof force === 'boolean' ? force : !deskState.isMemoOpen;
            deskState.isMemoOpen = state;
            const el = document.getElementById('omnidesk-memo');
            if (state) {
                el.classList.remove('hidden');
                if (!deskState.isMemoDocked) {
                    if (deskState.memoX !== null && deskState.memoY !== null) {
                        el.style.left = deskState.memoX + 'px';
                        el.style.top = deskState.memoY + 'px';
                        el.style.right = 'auto';
                        el.style.bottom = 'auto';
                    } else {
                        el.style.left = Math.max(15, window.innerWidth - 420) + 'px';
                        el.style.top = '120px';
                        el.style.right = 'auto';
                        el.style.bottom = 'auto';
                    }
                }
                renderActiveMemo();
            } else {
                el.classList.add('hidden');
            }
        },

        addNewMemo() {
            const newId = 'memo-' + Date.now();
            const colors = ['yellow', 'cyan', 'pink', 'mint', 'lavender'];
            const nextCol = colors[deskState.memos.length % colors.length];
            deskState.memos.push({
                id: newId,
                title: `Nota #${deskState.memos.length + 1}`,
                text: '',
                color: nextCol
            });
            deskState.activeMemoId = newId;
            saveDeskState();
            renderActiveMemo();
        },

        setCurMemoColor(colorKey) {
            const m = getActiveMemo();
            if (!m) return;
            m.color = colorKey;
            saveDeskState();
            renderMemoTabs();
            renderActiveMemo();
        },

        toggleMemoDock() {
            deskState.isMemoDocked = !deskState.isMemoDocked;
            if (!deskState.isMemoDocked) {
                // When unpinned, place safely inside the viewport and clear docked inline styles
                deskState.memoX = Math.max(40, window.innerWidth - 460);
                deskState.memoY = 120;
                memoWidget.style.right = 'auto';
                memoWidget.style.left = deskState.memoX + 'px';
                memoWidget.style.top = deskState.memoY + 'px';
            }
            saveDeskState();
            renderActiveMemo();
        },

        copyCurMemo() {
            const m = getActiveMemo();
            if (!m) return;
            navigator.clipboard.writeText((m.title ? m.title + "\n\n" : "") + (m.text || '')).then(() => {
                const st = document.getElementById('memoSaveStatus');
                if (st) {
                    st.textContent = 'Copiato negli appunti! ✓';
                    setTimeout(() => { st.textContent = 'Salvataggio automatico ✓'; }, 2000);
                }
            });
        },

        deleteCurMemo() {
            const m = getActiveMemo();
            if (!m) return;
            if (confirm(`Vuoi cancellare "${m.title || 'questa nota'}"?`)) {
                window.OmniDesk.deleteMemoById(m.id);
            }
        },

        deleteMemoById(id) {
            if (deskState.memos.length <= 1) {
                // Reset single note
                deskState.memos[0].text = '';
                deskState.memos[0].title = 'Appunti #1';
            } else {
                deskState.memos = deskState.memos.filter(item => item.id !== id);
                if (deskState.activeMemoId === id) {
                    deskState.activeMemoId = deskState.memos[0].id;
                }
            }
            saveDeskState();
            renderMemoTabs();
            renderActiveMemo();
        },

        // Calculator Controls
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

        calcDigit(d) {
            if (calcResetOnNext) {
                calcCurrent = d === '.' ? '0.' : d;
                calcResetOnNext = false;
            } else {
                if (d === '.' && calcCurrent.includes('.')) return;
                calcCurrent = (calcCurrent === '0' && d !== '.') ? d : calcCurrent + d;
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
                if (calcPrev !== null && calcOp) window.OmniDesk.calcAction('=');
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
// Right dock buttons removed; accessed via top DESK dropdown.

    
    function makeDraggable(element, handle, onMoveEnd) {
        let isDragging = false;
        let startX, startY, initialLeft, initialTop;

        function startDrag(e) {
            // If locked in top right corner, do not drag
            if (element.classList.contains('memo-docked')) return;
            if (e.target.closest('button, textarea, input, select, a, .memo-bookmark-tab')) return;

            isDragging = true;
            startX = e.touches ? e.touches[0].clientX : e.clientX;
            startY = e.touches ? e.touches[0].clientY : e.clientY;

            const rect = element.getBoundingClientRect();
            initialLeft = rect.left;
            initialTop = rect.top;

            // Clear right/bottom so left/top immediately take precedence
            element.style.right = 'auto';
            element.style.bottom = 'auto';

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

            let newLeft = initialLeft + (clientX - startX);
            let newTop = initialTop + (clientY - startY);

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

        if (handle) {
            handle.addEventListener('mousedown', startDrag);
            handle.addEventListener('touchstart', startDrag, { passive: true });
        }
    }

// Make widgets draggable
    makeDraggable(clockWidget, clockWidget.querySelector('#omnidesk-clock-body'), (x, y) => {
        deskState.clock.x = x;
        deskState.clock.y = y;
        saveDeskState();
    });

    makeDraggable(memoWidget, memoWidget.querySelector('#memoWindowHeader'), (x, y) => {
        deskState.memoX = x;
        deskState.memoY = y;
        saveDeskState();
        updateMemoTabsSide(x);
    });

    makeDraggable(calcWidget, calcWidget.querySelector('#omnidesk-calc-header'), (x, y) => {
        deskState.calc.x = x;
        deskState.calc.y = y;
        saveDeskState();
    });

    // Boot theme
    window.OmniDesk.setClockTheme(deskState.clock.theme || 'teal');
    renderMemoTabs();
    renderActiveMemo();

    // Start with widgets closed
    window.OmniDesk.toggleClock(false);
    window.OmniDesk.toggleMemo(false);
    window.OmniDesk.toggleCalc(false);

})();
