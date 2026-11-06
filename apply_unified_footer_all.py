#!/usr/bin/env python3
"""
apply_unified_footer_all.py - Systematically unifies the bottom of all tools:
1. FAQ Accordion format
2. Share & Viral Action Strip
3. Suggestion Prompt Strip
4. OmniTools Network Ecosystem Bar (All 8 Tools + Partnership)
5. Legal Disclaimer & Copyright
6. Floating PWA Install Banner
7. Suggestion Modal
8. Complete JS Handlers
"""

import re
import subprocess

# 1. Update build_barcode_i18n.py
with open('Calcolatore_Pendenza/build_barcode_i18n.py', 'r', encoding='utf-8') as f:
    code = f.read()

if 'from unified_footer import' not in code:
    code = code.replace(
        'from nav_header import render_suite_header, render_suite_header_js',
        'from nav_header import render_suite_header, render_suite_header_js\nfrom unified_footer import render_unified_footer, render_unified_footer_js'
    )
    code = code.replace(
        'it_t = t_data["it"]',
        'it_t = t_data["it"]\nfooter_html = render_unified_footer("barcode", disclaimer_id="legalDisclaimer", disclaimer_default=it_t["legal_disclaimer"])\nfooter_js = render_unified_footer_js()'
    )

pattern_barcode_footer = r'<!-- Technical Disclaimer -->\s*<div class="text-\[11px\] text-slate-500 text-center leading-relaxed max-w-3xl mx-auto px-2">.*?</footer>'
code = re.sub(pattern_barcode_footer, '</main>\n\n    {footer_html}', code, flags=re.DOTALL)

# Ensure footer_js is in script
if '{footer_js}' not in code:
    code = code.replace('<script>\n        const TRANSLATIONS = {t_json_str};', '<script>\n{footer_js}\n        const TRANSLATIONS = {t_json_str};')

# Also fix the closing </main> if duplicated
code = code.replace('</main>\n\n    </main>', '</main>')

with open('Calcolatore_Pendenza/build_barcode_i18n.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("Updated build_barcode_i18n.py")


# 2. Update build_tinta_i18n.py
with open('Calcolatore_Pendenza/build_tinta_i18n.py', 'r', encoding='utf-8') as f:
    code = f.read()

if 'from unified_footer import' not in code:
    code = code.replace(
        'from nav_header import render_suite_header, render_suite_header_js',
        'from nav_header import render_suite_header, render_suite_header_js\nfrom unified_footer import render_unified_footer, render_unified_footer_js'
    )
    code = code.replace(
        'it_t = t_data["it"]',
        'it_t = t_data["it"]\nfooter_html = render_unified_footer("tinta", disclaimer_id="legalDisclaimerText", disclaimer_default=it_t["legal_disclaimer"])\nfooter_js = render_unified_footer_js()'
    )

pattern_tinta_footer = r'<!-- Share & Viral Action Strip -->.*?</footer>'
code = re.sub(pattern_tinta_footer, '</main>\n\n    {footer_html}', code, flags=re.DOTALL)
if '{footer_js}' not in code:
    code = code.replace('<script>\n        const TRANSLATIONS = {t_json_str};', '<script>\n{footer_js}\n        const TRANSLATIONS = {t_json_str};')
code = code.replace('</main>\n\n    </main>', '</main>')

with open('Calcolatore_Pendenza/build_tinta_i18n.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("Updated build_tinta_i18n.py")


# 3. Update build_tubi_i18n.py, build_dorso_i18n.py, build_dpi_i18n.py, build_rampe_i18n.py, build_scale_i18n.py
tools_to_update = [
    ('tubi', 'build_tubi_i18n.py'),
    ('dorso', 'build_dorso_i18n.py'),
    ('dpi', 'build_dpi_i18n.py'),
    ('rampe', 'build_rampe_i18n.py'),
    ('scale', 'build_scale_i18n.py')
]

for tool_id, fn in tools_to_update:
    path = f'Calcolatore_Pendenza/{fn}'
    with open(path, 'r', encoding='utf-8') as f:
        code = f.read()

    if 'from unified_footer import' not in code:
        code = code.replace(
            'from nav_header import render_suite_header, render_suite_header_js',
            'from nav_header import render_suite_header, render_suite_header_js\nfrom unified_footer import render_unified_footer, render_unified_footer_js'
        )
        code = code.replace(
            'it_t = t_data["it"]',
            f'it_t = t_data["it"]\nfooter_html = render_unified_footer("{tool_id}", disclaimer_id="legalDisclaimerText", disclaimer_default=it_t.get("legal_disclaimer", ""))\nfooter_js = render_unified_footer_js()'
        )

    # Replace old footer & modals with unified footer
    pattern_standard_footer = r'<!-- Footer with OmniTools Suite & Legal Disclaimer -->.*?<!-- Script & Calculation Engine'
    replacement = '{footer_html}\n\n    <!-- Script & Calculation Engine'
    if re.search(pattern_standard_footer, code, flags=re.DOTALL):
        code = re.sub(pattern_standard_footer, replacement, code, flags=re.DOTALL)
    
    # Also check variant footer comment
    pattern_alt = r'<!-- Footer with OmniTools Suite & Legal Disclaimer -->.*?<script>'
    if re.search(pattern_alt, code, flags=re.DOTALL):
        code = re.sub(pattern_alt, '{footer_html}\n\n    <script>', code, flags=re.DOTALL)

    if '{footer_js}' not in code:
        code = code.replace('{header_js}', '{header_js}\n{footer_js}')

    with open(path, 'w', encoding='utf-8') as f:
        f.write(code)

    print(f"Updated {fn}")

print("All build scripts updated successfully.")
