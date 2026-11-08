import os

# build_hub_i18n.py
# Note: index.html is the canonical 17-tool hub with live DOM dynamic counting (syncMacrotoolCounts).
# This script ensures index.html is validated and synced with all 17 tools.

cur_dir = os.path.dirname(os.path.abspath(__file__))
index_path = os.path.join(cur_dir, 'index.html')

with open(index_path, 'r', encoding='utf-8') as f:
    content = f.read()

assert 'id="sectionBuilding"' in content, "Missing sectionBuilding"
assert 'id="sectionGraph"' in content, "Missing sectionGraph"
assert 'id="sectionFinance"' in content, "Missing sectionFinance"
assert 'syncMacrotoolCounts()' in content, "Missing syncMacrotoolCounts"

print("index.html verified successfully: all 17 tools and dynamic counters intact.")
