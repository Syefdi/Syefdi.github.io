#!/usr/bin/env python3
"""
Clean CSS and JS files from HTML tags
"""

import re

# Clean CSS file
with open('css/main.css', 'r', encoding='utf-8') as f:
    css_content = f.read()

# Remove extra indentation (normalize)
css_lines = [line.lstrip() if line.strip() else '' for line in css_content.split('\n')]
css_clean = '\n'.join(css_lines)

with open('css/main.css', 'w', encoding='utf-8') as f:
    f.write(css_clean)

print("✓ Cleaned css/main.css")

# Clean JS file - remove HTML tags
with open('js/main.js', 'r', encoding='utf-8') as f:
    js_content = f.read()

# Remove script and style tags
js_clean = re.sub(r'</script>.*?<style>', '', js_content, flags=re.DOTALL)
js_clean = re.sub(r'<[^>]+>', '', js_clean)  # Remove any remaining HTML tags
js_clean = js_clean.strip()

with open('js/main.js', 'w', encoding='utf-8') as f:
    f.write(js_clean)

print("✓ Cleaned js/main.js")
print("\nFiles cleaned! Refresh browser to see changes.")
