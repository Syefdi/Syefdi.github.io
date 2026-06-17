#!/usr/bin/env python3
"""
Refactor script to extract CSS and JS from index.html
"""

import re
import os

# Read the original index.html
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract CSS (between <style> and </style>)
css_match = re.search(r'<style>(.*?)</style>', content, re.DOTALL)
if css_match:
    css_content = css_match.group(1).strip()
    os.makedirs('css', exist_ok=True)
    with open('css/main.css', 'w', encoding='utf-8') as f:
        f.write(css_content)
    print(f"✓ Extracted {len(css_content)} chars of CSS to css/main.css")

# Extract JS (between <script> tags at the end, before </body>)
js_match = re.search(r'<script>\s*\/\/ Spotlight effect(.*?)</script>\s*</body>', content, re.DOTALL)
if js_match:
    js_content = js_match.group(1).strip()
    os.makedirs('js', exist_ok=True)
    with open('js/main.js', 'w', encoding='utf-8') as f:
        # Add spotlight effect comment
        f.write('// Spotlight effect\n')
        f.write(js_content)
    print(f"✓ Extracted {len(js_content)} chars of JS to js/main.js")
else:
    # Try another pattern
    js_match = re.search(r'<script>(.*?)</script>\s*</body>', content, re.DOTALL)
    if js_match:
        js_content = js_match.group(1).strip()
        os.makedirs('js', exist_ok=True)
        with open('js/main.js', 'w', encoding='utf-8') as f:
            f.write(js_content)
        print(f"✓ Extracted {len(js_content)} chars of JS to js/main.js")

print("\n✓ Refactoring complete!")
print("  - CSS extracted to: css/main.css")
print("  - JS extracted to: js/main.js")
print("\nNext: Update index.html to link these files")
