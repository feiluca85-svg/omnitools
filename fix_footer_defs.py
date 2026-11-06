#!/usr/bin/env python3
import re

files = [
    ('rampe', 'build_rampe_i18n.py'),
    ('scale', 'build_scale_i18n.py'),
    ('tubi', 'build_tubi_i18n.py'),
    ('dorso', 'build_dorso_i18n.py'),
    ('dpi', 'build_dpi_i18n.py'),
    ('tinta', 'build_tinta_i18n.py'),
    ('barcode', 'build_barcode_i18n.py')
]

for tool_id, fn in files:
    path = f'Calcolatore_Pendenza/{fn}'
    with open(path, 'r', encoding='utf-8') as f:
        code = f.read()

    # Ensure import is present
    if 'from unified_footer import render_unified_footer, render_unified_footer_js' not in code:
        code = 'from unified_footer import render_unified_footer, render_unified_footer_js\n' + code

    # Ensure definition is present right after header_js
    if 'footer_html = render_unified_footer' not in code:
        code = code.replace(
            'header_js = render_suite_header_js()',
            f'header_js = render_suite_header_js()\nfooter_html = render_unified_footer("{tool_id}")\nfooter_js = render_unified_footer_js()'
        )

    # In HTML template: ensure {footer_html} replaces whatever footer was there
    # Look for </main> followed by <footer>...
    if '{footer_html}' not in code:
        # replace </main> ... <script> with </main>\n\n    {footer_html}\n\n    <script>
        pattern = r'</main>\s*<!-- Footer.*?<script>'
        if re.search(pattern, code, flags=re.DOTALL):
            code = re.sub(pattern, '</main>\n\n    {footer_html}\n\n    <script>', code, flags=re.DOTALL)
        else:
            # Try alternate footer pattern
            pattern2 = r'<footer.*?</footer\s*>'
            # Also remove installBanner and suggestModal if present outside footer
            pattern_banners = r'<div id="installBanner".*?</div>\s*</div>'
            pattern_modal = r'<div id="suggestModal".*?</div>\s*</div>'
            code = re.sub(pattern2, '{footer_html}', code, flags=re.DOTALL)
            code = re.sub(pattern_banners, '', code, flags=re.DOTALL)
            code = re.sub(pattern_modal, '', code, flags=re.DOTALL)

    # In JS: ensure {footer_js} is injected
    if '{footer_js}' not in code:
        if '{header_js}' in code:
            code = code.replace('{header_js}', '{header_js}\n{footer_js}')
        else:
            code = code.replace('<script>', '<script>\n{footer_js}')

    with open(path, 'w', encoding='utf-8') as f:
        f.write(code)

    print(f"Fixed {fn}")
