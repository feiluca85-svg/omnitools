#!/usr/bin/env python3
"""
Sync OmniFood category in suiteMenuDropdown and topNewToolDropdown across all HTML files in Calcolatore_Pendenza.
- Total tools: 22 Strumenti / 22 Tools
- OmniFood: 4 Tools
"""

import os
import re

FOOD_PAGES_IT = {'shelflife.html', 'nutriexport.html', 'impasti.html', 'idratazione.html'}
FOOD_PAGES_EN = {'shelf-life-calculator.html', 'nutri-export-converter.html', 'batch-scaler-calculator.html', 'hydration-balance-calculator.html'}

def get_food_block_it(active_tool_id, is_open=False):
    open_attr = " open" if is_open else ""
    
    def get_link(href, tool_id, name, badge, svg_path):
        is_active = (tool_id == active_tool_id)
        active_class = "bg-orange-600 text-white font-bold" if is_active else "text-slate-700 hover:bg-slate-100"
        icon_bg = "bg-orange-600 text-white" if is_active else "bg-orange-500 text-white"
        return f"""<a href="{href}" data-nav-tool-id="{tool_id}" class="flex items-center justify-between p-2 rounded-xl text-xs transition {active_class}">
                            <div class="flex items-center gap-2">
                                <span class="w-4 h-4 rounded-md {icon_bg} flex items-center justify-center p-0.5 shrink-0"><svg class="w-full h-full" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="{svg_path}"/></svg></span>
                                <span class="nav-tool-name font-bold">{name}</span>
                            </div>
                            <span class="nav-tool-badge text-[9px] uppercase px-1.5 py-0.5 rounded-md bg-black/10 font-mono font-bold">{badge}</span>
                        </a>"""

    link_shelflife = get_link("/shelflife", "shelflife", "ShelfLife Export", "UE • FDA • CFIA", "M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z")
    link_nutriexport = get_link("/nutriexport", "nutriexport", "NutriExport Converter", "FDA 21 CFR", "M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z")
    link_impasti = get_link("/impasti", "impasti", "BatchScaler Pro", "Baker's %", "M3 6l3 18h12l3-18H3zm6 0v18m6-18v18")
    link_idratazione = get_link("/idratazione", "idratazione", "HygroBalance Lab", "T-Base &amp; Ghiaccio", "M19.428 15.428a2 2 0 00-1.022-.547l-2.387-.477a6 6 0 00-3.86.517l-.318.158a6 6 0 01-3.86.517L6.05 15.21a2 2 0 00-1.806.547M8 4h8l-1 1v5.172a2 2 0 00.586 1.414l5 5c1.26 1.26.367 3.414-1.415 3.414H4.828c-1.782 0-2.674-2.154-1.414-3.414l5-5A2 2 0 009 10.172V5L8 4z")

    return f"""<details class="group/cat" data-cat="food"{open_attr}>
    <summary class="px-2 py-0.5 text-[10px] font-extrabold uppercase tracking-wider text-orange-700 flex items-center gap-1 justify-between w-full py-1.5 px-2 rounded-lg hover:bg-slate-50 cursor-pointer list-none select-none [&::-webkit-details-marker]:hidden">
        <span class="flex items-center gap-1.5">
                            <span class="w-1.5 h-1.5 rounded-full bg-orange-600"></span> <span>OmniFood (4)</span>
                        </span>
        <svg class="w-3.5 h-3.5 text-slate-400 transition-transform duration-150 group-open/cat:rotate-180 shrink-0" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M19 9l-7 7-7-7"/></svg>
    </summary>
    <div class="space-y-0.5 pt-1">
{link_shelflife}
{link_nutriexport}
{link_impasti}
{link_idratazione}
    </div>
</details>"""

def get_food_block_en(active_tool_id, is_open=False):
    open_attr = " open" if is_open else ""
    
    def get_link(href, tool_id, name, badge, svg_path):
        is_active = (tool_id == active_tool_id)
        active_class = "bg-orange-600 text-white font-bold" if is_active else "text-slate-700 hover:bg-slate-100"
        icon_bg = "bg-orange-600 text-white" if is_active else "bg-orange-500 text-white"
        return f"""<a href="{href}" data-nav-tool-id="{tool_id}" class="flex items-center justify-between p-2 rounded-xl text-xs transition {active_class}">
                            <div class="flex items-center gap-2">
                                <span class="w-4 h-4 rounded-md {icon_bg} flex items-center justify-center p-0.5 shrink-0"><svg class="w-full h-full" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="{svg_path}"/></svg></span>
                                <span class="nav-tool-name font-bold">{name}</span>
                            </div>
                            <span class="nav-tool-badge text-[9px] uppercase px-1.5 py-0.5 rounded-md bg-black/10 font-mono font-bold">{badge}</span>
                        </a>"""

    link_shelflife = get_link("/en/shelf-life-calculator", "shelflife", "ShelfLife Export", "EU • FDA • CFIA", "M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z")
    link_nutriexport = get_link("/en/nutri-export-converter", "nutriexport", "NutriExport Converter", "FDA 21 CFR", "M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z")
    link_impasti = get_link("/en/batch-scaler-calculator", "impasti", "BatchScaler Pro", "Baker's %", "M3 6l3 18h12l3-18H3zm6 0v18m6-18v18")
    link_idratazione = get_link("/en/hydration-balance-calculator", "idratazione", "HygroBalance Lab", "T-Base &amp; Ice", "M19.428 15.428a2 2 0 00-1.022-.547l-2.387-.477a6 6 0 00-3.86.517l-.318.158a6 6 0 01-3.86.517L6.05 15.21a2 2 0 00-1.806.547M8 4h8l-1 1v5.172a2 2 0 00.586 1.414l5 5c1.26 1.26.367 3.414-1.415 3.414H4.828c-1.782 0-2.674-2.154-1.414-3.414l5-5A2 2 0 009 10.172V5L8 4z")

    return f"""<details class="group/cat" data-cat="food"{open_attr}>
    <summary class="px-2 py-0.5 text-[10px] font-extrabold uppercase tracking-wider text-orange-700 flex items-center gap-1 justify-between w-full py-1.5 px-2 rounded-lg hover:bg-slate-50 cursor-pointer list-none select-none [&::-webkit-details-marker]:hidden">
        <span class="flex items-center gap-1.5">
                            <span class="w-1.5 h-1.5 rounded-full bg-orange-600"></span> <span>OmniFood (4)</span>
                        </span>
        <svg class="w-3.5 h-3.5 text-slate-400 transition-transform duration-150 group-open/cat:rotate-180 shrink-0" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M19 9l-7 7-7-7"/></svg>
    </summary>
    <div class="space-y-0.5 pt-1">
{link_shelflife}
{link_nutriexport}
{link_impasti}
{link_idratazione}
    </div>
</details>"""

def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    fname = os.path.basename(file_path)
    is_en = '/en/' in file_path or file_path.startswith('en/')
    
    # Identify active tool id if this is a food page
    active_tool_id = ""
    is_open = False
    if is_en:
        if fname == 'shelf-life-calculator.html': active_tool_id = 'shelflife'; is_open = True
        elif fname == 'nutri-export-converter.html': active_tool_id = 'nutriexport'; is_open = True
        elif fname == 'batch-scaler-calculator.html': active_tool_id = 'impasti'; is_open = True
        elif fname == 'hydration-balance-calculator.html': active_tool_id = 'idratazione'; is_open = True
    else:
        if fname == 'shelflife.html': active_tool_id = 'shelflife'; is_open = True
        elif fname == 'nutriexport.html': active_tool_id = 'nutriexport'; is_open = True
        elif fname == 'impasti.html': active_tool_id = 'impasti'; is_open = True
        elif fname == 'idratazione.html': active_tool_id = 'idratazione'; is_open = True

    # Replacement block
    if is_en:
        new_block = get_food_block_en(active_tool_id, is_open)
    else:
        new_block = get_food_block_it(active_tool_id, is_open)

    # Replace all occurrences of <details class="group/cat" data-cat="food"[^>]*>[\s\S]*?</details>
    pattern = r'<details class="group/cat" data-cat="food"[^>]*>[\s\S]*?</details>'
    updated = re.sub(pattern, new_block, content)

    # Update tool count label from "19 Strumenti" / "19 Tool" to "22 Strumenti" / "22 Tools"
    updated = re.sub(r'id="suiteDropToolCount">19 Strumenti<', 'id="suiteDropToolCount">22 Strumenti<', updated)
    updated = re.sub(r'id="topDropToolCount"[^>]*>19 Tool<', 'id="topDropToolCount" class="text-blue-600 font-bold font-mono">22 Tool<', updated)
    updated = re.sub(r'id="suiteDropToolCount">19 Tools<', 'id="suiteDropToolCount">22 Tools<', updated)
    updated = re.sub(r'id="topDropToolCount"[^>]*>19 Tools<', 'id="topDropToolCount" class="text-blue-600 font-bold font-mono">22 Tools<', updated)

    if updated != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(updated)
        print(f"Updated: {file_path}")
    else:
        print(f"Unchanged: {file_path}")

prod_dir = 'Calcolatore_Pendenza'
for root, dirs, files in os.walk(prod_dir):
    for f in files:
        if f.endswith('.html'):
            process_file(os.path.join(root, f))

print("Sync of suite dropdowns completed successfully.")
