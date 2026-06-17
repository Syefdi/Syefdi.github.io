#!/usr/bin/env python3
"""
Properly extract CSS and JS from backup
"""

import re

# Read backup
with open('index.html.backup', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract CSS - everything between <style> and </style>
css_match = re.search(r'<style>\s*(.*?)\s*</style>', content, re.DOTALL)
if css_match:
    css = css_match.group(1)
    with open('css/main.css', 'w', encoding='utf-8') as f:
        f.write(css)
    print(f"✓ CSS extracted: {len(css)} chars")
else:
    print("✗ CSS not found")

# Extract JS - everything between last <script> (not the theme init) and </script> before </body>
# Find all script tags
script_pattern = r'<script>(.*?)</script>'
scripts = re.findall(script_pattern, content, re.DOTALL)

# The last script should be the main JS (skip the theme initialization one)
if len(scripts) >= 2:
    # Last script is the main one
    js = scripts[-1].strip()
    with open('js/main.js', 'w', encoding='utf-8') as f:
        f.write(js)
    print(f"✓ JS extracted: {len(js)} chars, {js.count('function')} functions found")
else:
    print(f"✗ Found {len(scripts)} scripts, expected at least 2")

print("\n✓ Re-extraction complete!")
print("Now refresh browser (Ctrl+Shift+R)")
