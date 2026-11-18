#!/usr/bin/env python3
"""
Update index.html (Home Hub):
1. Add the 3 new OmniFood tools to #sectionFood grid.
2. Update JSON-LD hasPart.
3. Update badgeCountFood to '4 Tool'.
4. Update footer OmniFood section.
"""

import os
import re

with open('Calcolatore_Pendenza/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update JSON-LD hasPart to include all 4 tools
shelflife_json_part = """{
      "@type": "WebApplication",
      "name": "ShelfLife & Export Date",
      "applicationCategory": "BusinessApplication",
      "url": "https://www.omnitoolslab.com/shelflife"
    }"""

four_tools_json = """{
      "@type": "WebApplication",
      "name": "ShelfLife & Export Date",
      "applicationCategory": "BusinessApplication",
      "url": "https://www.omnitoolslab.com/shelflife"
    },
    {
      "@type": "WebApplication",
      "name": "NutriExport Converter",
      "applicationCategory": "BusinessApplication",
      "url": "https://www.omnitoolslab.com/nutriexport"
    },
    {
      "@type": "WebApplication",
      "name": "BatchScaler Pro",
      "applicationCategory": "BusinessApplication",
      "url": "https://www.omnitoolslab.com/impasti"
    },
    {
      "@type": "WebApplication",
      "name": "HygroBalance Lab",
      "applicationCategory": "BusinessApplication",
      "url": "https://www.omnitoolslab.com/idratazione"
    }"""

content = content.replace(shelflife_json_part, four_tools_json)

# 2. Update badgeCountFood
content = re.sub(r'<span id="badgeCountFood"[^>]*>1 Tool</span>', '<span id="badgeCountFood" class="text-[10px] sm:text-[11px] font-bold text-orange-800 bg-orange-500/10 px-2 py-0.5 rounded-md border border-orange-500/20">4 Tool</span>', content)

# 3. New Cards for sectionFood
new_cards = """                    <!-- Tool 2: NutriExport Converter -->
                    <a href="/nutriexport" class="tool-card group relative bg-white hover:bg-orange-50/20 rounded-3xl p-5 border-2 border-slate-200/90 hover:border-orange-500 shadow-xs hover:shadow-xl hover:-translate-y-1 transition-all duration-200 flex flex-col justify-between space-y-4" data-tags="nutrizione fda 100g 21 cfr 101.9 tabella nutrizionale racc sodio sale calorie">
                        <div class="space-y-3">
                            <div class="flex items-center justify-between">
                                <span class="w-10 h-10 rounded-2xl bg-orange-500/10 text-orange-700 flex items-center justify-center font-bold text-lg group-hover:scale-110 group-hover:bg-orange-600 group-hover:text-white transition duration-200 shadow-xs">
                                    <svg class="w-5 h-5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/></svg>
                                </span>
                                <span class="text-[10px] font-extrabold uppercase px-2 py-0.5 rounded-full bg-slate-100 text-slate-600 border border-slate-200 group-hover:border-orange-200 group-hover:bg-orange-50 transition">FDA 21 CFR</span>
                            </div>
                            <div>
                                <h3 class="font-jakarta text-base font-extrabold text-slate-900 group-hover:text-orange-600 transition flex items-center justify-between">
                                    <span>NutriExport Converter</span>
                                    <span class="text-slate-400 group-hover:translate-x-1 group-hover:text-orange-600 transition">→</span>
                                </h3>
                                <p class="text-xs text-slate-500 mt-1 leading-relaxed">Da tabella nutrizionale UE (100g) a etichetta USA FDA con porzioni RACC, sale/sodio e arrotondamenti legali.</p>
                            </div>
                        </div>
                        <div class="pt-3 border-t border-slate-100 flex items-center justify-between text-[11px] text-slate-400">
                            <span class="font-medium text-orange-700">RACC • % DV • Sodium</span>
                            <span class="font-bold text-slate-700 group-hover:text-orange-600 transition">Apri Tool</span>
                        </div>
                    </a>

                    <!-- Tool 3: BatchScaler Pro -->
                    <a href="/impasti" class="tool-card group relative bg-white hover:bg-orange-50/20 rounded-3xl p-5 border-2 border-slate-200/90 hover:border-orange-500 shadow-xs hover:shadow-xl hover:-translate-y-1 transition-all duration-200 flex flex-col justify-between space-y-4" data-tags="impasti pane pizza panificazione baker percentage sfrido calo cottura lotti">
                        <div class="space-y-3">
                            <div class="flex items-center justify-between">
                                <span class="w-10 h-10 rounded-2xl bg-orange-500/10 text-orange-700 flex items-center justify-center font-bold text-lg group-hover:scale-110 group-hover:bg-orange-600 group-hover:text-white transition duration-200 shadow-xs">
                                    <svg class="w-5 h-5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M3 6l3 18h12l3-18H3zm6 0v18m6-18v18"/></svg>
                                </span>
                                <span class="text-[10px] font-extrabold uppercase px-2 py-0.5 rounded-full bg-slate-100 text-slate-600 border border-slate-200 group-hover:border-orange-200 group-hover:bg-orange-50 transition">Baker's %</span>
                            </div>
                            <div>
                                <h3 class="font-jakarta text-base font-extrabold text-slate-900 group-hover:text-orange-600 transition flex items-center justify-between">
                                    <span>BatchScaler Pro</span>
                                    <span class="text-slate-400 group-hover:translate-x-1 group-hover:text-orange-600 transition">→</span>
                                </h3>
                                <p class="text-xs text-slate-500 mt-1 leading-relaxed">Scalatore professionale impasti: calcolo lotti per peso target, pezzi o ingrediente limitante con sfrido e calo peso cottura.</p>
                            </div>
                        </div>
                        <div class="pt-3 border-t border-slate-100 flex items-center justify-between text-[11px] text-slate-400">
                            <span class="font-medium text-orange-700">Farina 100% • Sfrido • Banco</span>
                            <span class="font-bold text-slate-700 group-hover:text-orange-600 transition">Apri Tool</span>
                        </div>
                    </a>

                    <!-- Tool 4: HygroBalance Lab -->
                    <a href="/idratazione" class="tool-card group relative bg-white hover:bg-orange-50/20 rounded-3xl p-5 border-2 border-slate-200/90 hover:border-orange-500 shadow-xs hover:shadow-xl hover:-translate-y-1 transition-all duration-200 flex flex-col justify-between space-y-4" data-tags="idratazione acqua impasto t-base ghiaccio termodinamica lievito madre uova latte burro">
                        <div class="space-y-3">
                            <div class="flex items-center justify-between">
                                <span class="w-10 h-10 rounded-2xl bg-orange-500/10 text-orange-700 flex items-center justify-center font-bold text-lg group-hover:scale-110 group-hover:bg-orange-600 group-hover:text-white transition duration-200 shadow-xs">
                                    <svg class="w-5 h-5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M19.428 15.428a2 2 0 00-1.022-.547l-2.387-.477a6 6 0 00-3.86.517l-.318.158a6 6 0 01-3.86.517L6.05 15.21a2 2 0 00-1.806.547M8 4h8l-1 1v5.172a2 2 0 00.586 1.414l5 5c1.26 1.26.367 3.414-1.415 3.414H4.828c-1.782 0-2.674-2.154-1.414-3.414l5-5A2 2 0 009 10.172V5L8 4z"/></svg>
                                </span>
                                <span class="text-[10px] font-extrabold uppercase px-2 py-0.5 rounded-full bg-slate-100 text-slate-600 border border-slate-200 group-hover:border-orange-200 group-hover:bg-orange-50 transition">T-Base &amp; Ghiaccio</span>
                            </div>
                            <div>
                                <h3 class="font-jakarta text-base font-extrabold text-slate-900 group-hover:text-orange-600 transition flex items-center justify-between">
                                    <span>HygroBalance Lab</span>
                                    <span class="text-slate-400 group-hover:translate-x-1 group-hover:text-orange-600 transition">→</span>
                                </h3>
                                <p class="text-xs text-slate-500 mt-1 leading-relaxed">Idratazione reale vs apparente (acqua legata in uova, burro, latte), regola termodinamica della T-Base e dosaggio ghiaccio.</p>
                            </div>
                        </div>
                        <div class="pt-3 border-t border-slate-100 flex items-center justify-between text-[11px] text-slate-400">
                            <span class="font-medium text-orange-700">Acqua Legata • Ghiaccio • 80 kcal</span>
                            <span class="font-bold text-slate-700 group-hover:text-orange-600 transition">Apri Tool</span>
                        </div>
                    </a>"""

# Insert new cards right after Tool 1 (ShelfLife) in sectionFood
# Find end of shelflife card:
shelflife_card_end = content.find('</a>', content.find('href="/shelflife" class="tool-card')) + 4
content = content[:shelflife_card_end] + "\n\n" + new_cards + content[shelflife_card_end:]

# 4. Update footer in index.html:
footer_food_old = """<!-- Division 3B: OmniFood (1 Tool) -->
                <div class="space-y-1.5 pt-1">
                    <div class="text-[10px] font-extrabold uppercase tracking-wider text-orange-400 flex items-center gap-1">
                        <span>🥫</span> <span>OmniFood (1 Food &amp; Export Compliance)</span>
                    </div>
                    <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-2">
                        <a href="/shelflife" class="p-2 sm:p-2.5 rounded-xl bg-slate-800/60 hover:bg-slate-800 border border-slate-700/60 flex items-center justify-between transition group shadow-xs">
                            <div class="min-w-0 pr-1">
                                <span class="font-bold text-slate-200 group-hover:text-white text-[11px] block truncate">🥫 ShelfLife Export</span>
                                <span class="text-[9px] text-slate-400 group-hover:text-slate-300 block truncate">TMC, FDA, CFIA &amp; GCC</span>
                            </div>
                            <span class="text-slate-400 group-hover:text-white text-xs shrink-0 transition">→</span>
                        </a>
                    </div>
                </div>"""

footer_food_new = """<!-- Division 3B: OmniFood (4 Tools) -->
                <div class="space-y-1.5 pt-1">
                    <div class="text-[10px] font-extrabold uppercase tracking-wider text-orange-400 flex items-center gap-1">
                        <span>🥫</span> <span>OmniFood (4 FoodTech &amp; Export Compliance)</span>
                    </div>
                    <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-2">
                        <a href="/shelflife" class="p-2 sm:p-2.5 rounded-xl bg-slate-800/60 hover:bg-slate-800 border border-slate-700/60 flex items-center justify-between transition group shadow-xs">
                            <div class="min-w-0 pr-1">
                                <span class="font-bold text-slate-200 group-hover:text-white text-[11px] block truncate">🥫 ShelfLife Export</span>
                                <span class="text-[9px] text-slate-400 group-hover:text-slate-300 block truncate">TMC, FDA, CFIA &amp; GCC</span>
                            </div>
                            <span class="text-slate-400 group-hover:text-white text-xs shrink-0 transition">→</span>
                        </a>
                        <a href="/nutriexport" class="p-2 sm:p-2.5 rounded-xl bg-slate-800/60 hover:bg-slate-800 border border-slate-700/60 flex items-center justify-between transition group shadow-xs">
                            <div class="min-w-0 pr-1">
                                <span class="font-bold text-slate-200 group-hover:text-white text-[11px] block truncate">🧪 NutriExport</span>
                                <span class="text-[9px] text-slate-400 group-hover:text-slate-300 block truncate">FDA 21 CFR • RACC</span>
                            </div>
                            <span class="text-slate-400 group-hover:text-white text-xs shrink-0 transition">→</span>
                        </a>
                        <a href="/impasti" class="p-2 sm:p-2.5 rounded-xl bg-slate-800/60 hover:bg-slate-800 border border-slate-700/60 flex items-center justify-between transition group shadow-xs">
                            <div class="min-w-0 pr-1">
                                <span class="font-bold text-slate-200 group-hover:text-white text-[11px] block truncate">🥖 BatchScaler Pro</span>
                                <span class="text-[9px] text-slate-400 group-hover:text-slate-300 block truncate">Baker's % • Sfrido</span>
                            </div>
                            <span class="text-slate-400 group-hover:text-white text-xs shrink-0 transition">→</span>
                        </a>
                        <a href="/idratazione" class="p-2 sm:p-2.5 rounded-xl bg-slate-800/60 hover:bg-slate-800 border border-slate-700/60 flex items-center justify-between transition group shadow-xs">
                            <div class="min-w-0 pr-1">
                                <span class="font-bold text-slate-200 group-hover:text-white text-[11px] block truncate">💧 HygroBalance</span>
                                <span class="text-[9px] text-slate-400 group-hover:text-slate-300 block truncate">T-Base • Ghiaccio</span>
                            </div>
                            <span class="text-slate-400 group-hover:text-white text-xs shrink-0 transition">→</span>
                        </a>
                    </div>
                </div>"""

content = content.replace(footer_food_old, footer_food_new)

with open('Calcolatore_Pendenza/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("index.html updated successfully with 4 OmniFood tools.")
