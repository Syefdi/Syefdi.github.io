#!/usr/bin/env python3
"""
Replace inline CSS and JS with external links in index.html
"""

import re

# Read current index
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace inline CSS with link
content = re.sub(
    r'<style>.*?</style>',
    '<link rel="stylesheet" href="css/main.css">',
    content,
    flags=re.DOTALL
)

# Replace inline JS with link (before </body>)
content = re.sub(
    r'<script>\s*// Spotlight effect.*?</script>\s*(</body>)',
    r'<script src="js/main.js"></script>\n\1',
    content,
    flags=re.DOTALL
)

# If above didn't work, try simpler pattern
if 'js/main.js' not in content:
    # Find last <script> before </body>
    content = re.sub(
        r'<script>(?!.*<script>).*?</script>(\s*</body>)',
        r'<script src="js/main.js"></script>\1',
        content,
        flags=re.DOTALL
    )

# Write updated index
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✓ Fixed links in index.html!")
print("  - Inline CSS replaced with: <link href=\"css/main.css\">")
print("  - Inline JS replaced with: <script src=\"js/main.js\">")
