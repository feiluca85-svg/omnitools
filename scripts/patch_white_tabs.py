import glob
import re

html_files = glob.glob('Calcolatore_Pendenza/*.html') + glob.glob('Calcolatore_Pendenza/en/*.html')

# 1. In renderChromeTabs: replace the tab and home tab styles
old_render_tab_pattern = re.compile(
    r"tab\.className = `omni-dyn-tab group flex items-center gap-2 px-3 h-\[34px\] text-\[12px\] font-medium border-t-2 border-r transition shrink-0 cursor-pointer \$\{\s*isActive \? 'bg-\[#1E293B\] text-white border-t-blue-500 border-r-slate-700 font-semibold' : 'bg-\[#0F172A\] hover:bg-slate-800 text-\[#CBD5E1\] hover:text-white border-t-transparent border-r-slate-800 font-medium'\}`;"
)

new_render_tab_str = "tab.className = `omni-dyn-tab group flex items-center gap-2 px-3 h-[34px] text-[12px] font-medium border-t-2 border-r transition shrink-0 cursor-pointer ${isActive ? 'bg-[#FFFFFF] text-[#0F172A] border-t-blue-600 border-r-slate-300 font-bold shadow-xs' : 'bg-[#F8FAFC] hover:bg-slate-100 text-[#475569] hover:text-[#0F172A] border-t-transparent border-r-slate-200 font-medium'}`;"

# Home tab in renderChromeTabs
old_home_tab_pattern = re.compile(
    r"homeTab\.className = isHome \s*\?\s*'flex items-center gap-2 px-3\.5 h-\[34px\] bg-\[#1E293B\] text-white font-semibold border-t-2 border-blue-600 shrink-0 text-\[12px\] border-r border-slate-700'\s*:\s*'flex items-center gap-2 px-3\.5 h-\[34px\] bg-\[#0F172A\] hover:bg-slate-800 text-\[#CBD5E1\] hover:text-white font-medium border-t-2 border-transparent transition shrink-0 text-\[12px\] border-r border-slate-800';"
)

new_home_tab_str = "homeTab.className = isHome ? 'flex items-center gap-2 px-3.5 h-[34px] bg-[#FFFFFF] text-[#0F172A] font-bold border-t-2 border-blue-600 shrink-0 text-[12px] border-r border-slate-300 shadow-xs' : 'flex items-center gap-2 px-3.5 h-[34px] bg-[#F8FAFC] hover:bg-slate-100 text-[#475569] hover:text-[#0F172A] font-medium border-t-2 border-transparent transition shrink-0 text-[12px] border-r border-slate-200';"

# In HTML static markup:
# <div id="omniChromeTabsBar" class="hidden md:flex bg-slate-950 px-3 pt-2 pb-0 items-center justify-between border-b border-slate-800 text-xs select-none sticky top-0 z-50 shadow-md">
old_bar_markup = 'class="hidden md:flex bg-slate-950 px-3 pt-2 pb-0 items-center justify-between border-b border-slate-800 text-xs select-none sticky top-0 z-50 shadow-md"'
new_bar_markup = 'class="hidden md:flex bg-white px-3 pt-2 pb-0 items-center justify-between border-b border-slate-200 text-xs select-none sticky top-0 z-50 shadow-xs"'

count_tabs = 0
count_bar = 0

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    changed = False

    if old_bar_markup in content:
        content = content.replace(old_bar_markup, new_bar_markup)
        changed = True
        count_bar += 1

    if old_render_tab_pattern.search(content):
        content = old_render_tab_pattern.sub(new_render_tab_str, content)
        changed = True
        count_tabs += 1

    if old_home_tab_pattern.search(content):
        content = old_home_tab_pattern.sub(new_home_tab_str, content)
        changed = True

    # Also check if there's any close-tab button color in renderChromeTabs
    # change text-[#94A3B8] to text-slate-400 hover:text-slate-700
    if changed:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

print(f'Updated tabs bar in {count_bar} files, and renderChromeTabs in {count_tabs} files.')
