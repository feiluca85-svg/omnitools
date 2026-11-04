#!/usr/bin/env python3
import os
import re

files = ['rampe.html', 'scale.html', 'tubi.html', 'dorso.html', 'dpi.html']
base_dir = '/Users/ilalu/Documents/Altenative Businnes/Calcolatore_Pendenza'

print("="*60)
print("=== OMNITOOLS LAB: PRINT QUALITY ASSURANCE VERIFICATION ===")
print("="*60)

all_passed = True

for f in files:
    path = os.path.join(base_dir, f)
    with open(path, 'r', encoding='utf-8') as fh:
        content = fh.read()
    
    print(f"\n--- Checking: {f} ---")
    
    # 1. Check @page size A4 portrait
    page_match = re.search(r'@page\s*\{([^}]*)\}', content)
    has_portrait = False
    if page_match:
        rules = page_match.group(1).lower()
        if 'a4' in rules and 'portrait' in rules:
            has_portrait = True
            print("  [PASS] @page: strictly A4 portrait")
        else:
            print(f"  [FAIL] @page is not A4 portrait: {rules}")
            all_passed = False
    else:
        print("  [FAIL] @page rule missing")
        all_passed = False
        
    # 2. Check Vector SVG Logo in print header
    has_svg_logo = False
    # Check if printHeader or print-only has the calibrated circle & T-square SVG
    if 'printHeader' in content or 'print-only' in content:
        # Check for circle cx="16" cy="16" and path d="M 7.5 11.5
        if 'viewBox="0 0 32 32"' in content and 'r="13.2"' in content and 'M 7.5 11.5' in content:
            has_svg_logo = True
            print("  [PASS] Logo: Official calibrated Vector SVG logo present in print header")
        else:
            print("  [FAIL] Vector SVG logo missing from print header")
            all_passed = False
    else:
        print("  [FAIL] Print header missing entirely")
        all_passed = False
        
    # 3. Check FAQ suppression in print
    # FAQ should NOT be visible in print
    # Either section has no-print, or is hidden by ID
    faq_clean = False
    if 'id="faqSection"' in content:
        # Check if faqSection has no-print
        faq_tag = re.search(r'<section[^>]*id=\"faqSection\"[^>]*>', content)
        if faq_tag and 'no-print' in faq_tag.group(0):
            faq_clean = True
            print("  [PASS] FAQ: Strictly hidden in print (.no-print on #faqSection)")
        else:
            print(f"  [FAIL] FAQ not tagged with .no-print: {faq_tag.group(0) if faq_tag else 'None'}")
            all_passed = False
    elif 'id="faqContainer"' in content:
        faq_parent = re.search(r'<section[^>]*class=\"[^\"]*no-print[^\"]*\"[^>]*>.*?id=\"faqContainer\"', content, re.DOTALL)
        if faq_parent:
            faq_clean = True
            print("  [PASS] FAQ: Strictly hidden in print (.no-print on container)")
        else:
            print("  [FAIL] FAQ container not inside .no-print section")
            all_passed = False
    else:
        print("  [WARN] No FAQ section found")

    # 4. Check Normative / Long text guide suppression in print
    if 'id="normSection"' in content:
        norm_tag = re.search(r'<section[^>]*id=\"normSection\"[^>]*>', content)
        if norm_tag and 'no-print' in norm_tag.group(0):
            print("  [PASS] Normative Guide: Strictly hidden in print (.no-print)")
        else:
            print("  [FAIL] Normative guide visible in print")
            all_passed = False
    else:
        # Check if table guide has no-print
        guide_tag = re.search(r'<section[^>]*Tabella Normativa[^>]*>', content)
        if guide_tag and 'no-print' in guide_tag.group(0):
            print("  [PASS] Table Guide: Strictly hidden in print (.no-print)")

    # 5. Check Dedicated Print Footer with Signature Block
    if 'id="printFooterBox"' in content:
        print("  [PASS] Footer: Signature & technical notes box present")
    else:
        print("  [FAIL] Print signature footer box missing")
        all_passed = False

print("\n" + "="*60)
if all_passed:
    print(">>> ALL 5 TOOLS PASSED THE PRINT QUALITY ASSURANCE PROTOCOL! <<<")
else:
    print(">>> SOME CHECKS FAILED - REVIEW REQUIRED <<<")
print("="*60)
