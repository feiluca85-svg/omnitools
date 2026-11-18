import glob
import re

html_files = [f for f in glob.glob('Calcolatore_Pendenza/*.html') + glob.glob('Calcolatore_Pendenza/en/*.html') if 'index.html' not in f]

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    changed = False

    # Check if header has headerHelpBtn
    if 'id="headerHelpBtn"' not in content and '<header' in content:
        # We can insert the headerHelpBtn right next to the langSelect pill
        # Find: <div class="inline-flex items-center h-[36px] bg-[#F8FAFC]
        # or <div class="inline-flex items-center h-[36px]
        # or class="flex items-center gap-2 shrink-0">
        
        help_btn_markup = '''<button type="button" id="headerHelpBtn" onclick="openHelpDrawer()" class="no-print inline-flex items-center justify-center gap-1.5 h-[36px] px-3 text-xs font-semibold text-amber-900 bg-amber-50 hover:bg-amber-100 border border-amber-300 transition cursor-pointer shrink-0" style="border-radius: 0px;" title="Guida & Formule">
                    <svg class="w-3.5 h-3.5 text-amber-800 shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"></path><line x1="12" y1="17" x2="12.01" y2="17"></line></svg>
                    <span id="headerHelpText" class="text-[12px] font-semibold text-amber-950">Guida</span>
                </button>
                '''

        pattern = r'(<div class="flex items-center gap-2 shrink-0">\s*)(<div class="inline-flex items-center h-\[36px\])'
        if re.search(pattern, content):
            content = re.sub(pattern, r'\1' + help_btn_markup + r'\2', content)
            changed = True

    # Check if style id="omni-sharp-precision-grid-rules" can include the white tab bar rules and globe icon constraint
    if '<style id="omni-sharp-precision-grid-rules">' in content and '/* Deterministic Top Tab Bar White */' not in content:
        style_addition = '''
        /* Deterministic Top Tab Bar White */
        #omniChromeTabsBar {
            background-color: #ffffff !important;
            border-bottom: 1px solid #e2e8f0 !important;
        }
        #omniTabHome {
            background-color: #ffffff !important;
            color: #0f172a !important;
            border-top: 2px solid #2563eb !important;
            border-right: 1px solid #cbd5e1 !important;
            border-radius: 0px !important;
            font-weight: 700 !important;
            box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.05) !important;
        }
        #omniTabHome svg {
            color: #2563eb !important;
            stroke: #2563eb !important;
        }
        #omniTabHome span {
            color: #0f172a !important;
        }
        .omni-dyn-tab.active-tab {
            background-color: #ffffff !important;
            color: #0f172a !important;
            border-top: 2px solid #2563eb !important;
            border-right: 1px solid #cbd5e1 !important;
            font-weight: 700 !important;
            box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.05) !important;
        }
        .omni-dyn-tab.inactive-tab {
            background-color: #f8fafc !important;
            color: #475569 !important;
            border-top: 2px solid transparent !important;
            border-right: 1px solid #e2e8f0 !important;
            font-weight: 500 !important;
        }
        .omni-dyn-tab.inactive-tab:hover {
            background-color: #f1f5f9 !important;
            color: #0f172a !important;
        }
        /* Top Bar DESK and Nuovo Tool Buttons */
        #topDeskBtn {
            background-color: #fffbeb !important;
            color: #b45309 !important;
            border: 1px solid #fcd34d !important;
        }
        #topNewToolBtn {
            background-color: #f8fafc !important;
            color: #334155 !important;
            border: 1px solid #cbd5e1 !important;
        }
        /* Language Globe & Theme SVGs deterministic constraint */
        #langSelect + svg, #langSelect ~ svg, .relative:has(#langSelect) svg,
        .omni-lang-box svg, select[data-lang-switcher] ~ svg, header .relative svg:first-child {
            width: 15px !important;
            height: 15px !important;
            min-width: 15px !important;
            max-width: 15px !important;
            min-height: 15px !important;
            max-height: 15px !important;
            stroke-width: 1.75px !important;
        }
        '''
        content = content.replace(
            '<style id="omni-sharp-precision-grid-rules">',
            '<style id="omni-sharp-precision-grid-rules">' + style_addition
        )
        changed = True

    # Also update explicit SVG attributes in the header language selector
    # <svg class="w-[15px] h-[15px] text-[#64748B] dark:text-slate-400 pointer-events-none shrink-0"
    content = content.replace(
        '<svg class="w-[15px] h-[15px] text-[#64748B] dark:text-slate-400 pointer-events-none shrink-0"',
        '<svg width="15" height="15" style="width:15px;height:15px;min-width:15px;max-width:15px;" class="w-[15px] h-[15px] text-[#64748B] dark:text-slate-400 pointer-events-none shrink-0"'
    )
    changed = True

    if changed:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

print(f"Updated {len(html_files)} tool HTML files with headerHelpBtn, white tabs rules and svg dimensions!")
