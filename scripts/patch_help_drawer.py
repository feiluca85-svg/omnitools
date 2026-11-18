import re

old_fn = '''    function insertHeaderHelpButton() {
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
    }'''

new_fn = '''    function insertHeaderHelpButton() {
        if (document.getElementById('headerHelpBtn')) return;
        const helpBtn = document.createElement('button');
        helpBtn.type = 'button';
        helpBtn.id = 'headerHelpBtn';
        helpBtn.onclick = openHelpDrawer;
        helpBtn.className = 'no-print inline-flex items-center justify-center gap-1.5 h-[36px] px-3 text-xs font-semibold text-amber-900 bg-amber-50 hover:bg-amber-100 border border-amber-300 transition cursor-pointer shrink-0';
        helpBtn.style.borderRadius = '0px';
        helpBtn.title = 'Guida & Formule';
        helpBtn.innerHTML = `
            <svg class="w-3.5 h-3.5 text-amber-800 shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"></path><line x1="12" y1="17" x2="12.01" y2="17"></line></svg>
            <span id="headerHelpText" class="text-[12px] font-semibold text-amber-950">Guida</span>
        `;

        const langPill = document.querySelector('.omni-lang-theme-pill') || (document.getElementById('langSelect') ? document.getElementById('langSelect').closest('.inline-flex') : null);
        if (langPill && langPill.parentNode) {
            langPill.parentNode.insertBefore(helpBtn, langPill);
            return;
        }

        const installBtn = document.getElementById('headerInstallBtn');
        if (installBtn && installBtn.parentNode) {
            installBtn.parentNode.insertBefore(helpBtn, installBtn);
            return;
        }

        const headerRight = document.querySelector('header .flex.items-center.gap-2.shrink-0') || document.querySelector('header > div > div:last-child');
        if (headerRight) {
            headerRight.insertBefore(helpBtn, headerRight.firstChild);
        }
    }'''

with open('Calcolatore_Pendenza/omni_help_drawer.js', 'r') as f:
    content = f.read()

if old_fn in content:
    content = content.replace(old_fn, new_fn)
    style_inject = '''
    /* Inject Deterministic Sharp Rules for Header & Top Bar */
    (function injectGlobalStyles() {
        const style = document.createElement('style');
        style.id = 'omni-help-drawer-injected-styles';
        style.textContent = `
            /* Fix language globe icon size */
            #langSelect + svg, #langSelect ~ svg, .relative:has(#langSelect) svg,
            .omni-lang-box svg, select[data-lang-switcher] ~ svg {
                width: 15px !important;
                height: 15px !important;
                min-width: 15px !important;
                max-width: 15px !important;
                min-height: 15px !important;
                max-height: 15px !important;
                stroke-width: 1.75px !important;
            }
            /* White Top Tab Bar */
            #omniChromeTabsBar {
                background-color: #FFFFFF !important;
                border-bottom: 1px solid #E2E8F0 !important;
            }
            #omniTabHome {
                border-radius: 0px !important;
            }
            .omni-dyn-tab {
                border-radius: 0px !important;
            }
        `;
        document.head.appendChild(style);
    })();
'''
    content += style_inject
    with open('Calcolatore_Pendenza/omni_help_drawer.js', 'w') as f:
        f.write(content)
    print('Updated omni_help_drawer.js successfully!')
else:
    print('old_fn not found in omni_help_drawer.js')
