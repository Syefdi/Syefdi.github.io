#!/usr/bin/env python3
"""
Build new clean index.html with external CSS and JS
"""

import re

# Read backup
with open('index.html.backup', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract HTML body (between <body> and last </script>)
body_match = re.search(r'<body>(.*?)<script>', content, re.DOTALL)
if body_match:
    body_content = body_match.group(1).strip()
else:
    print("Error: Could not extract body content")
    exit(1)

# Build new HTML
new_html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Syefdi Syaban | QA Tester & Builder</title>
    <meta name="description" content="Syefdi Fasmawi Syaban - Junior QA Tester based in South Jakarta. Hands-on experience in functional testing, regression testing, and contributing to enterprise web systems.">
    <meta name="author" content="Syefdi Fasmawi Syaban">
    <meta name="keywords" content="QA Tester, Quality Assurance, Software Testing, Junior QA, South Jakarta, Indonesia">
    
    <!-- Open Graph for social sharing -->
    <meta property="og:type" content="website">
    <meta property="og:title" content="Syefdi Fasmawi Syaban | QA Tester & Builder">
    <meta property="og:description" content="Junior QA Tester with hands-on experience in functional testing, regression testing, and contributing to enterprise web systems at CV Gemilang Inti Teknologi.">
    <meta property="og:locale" content="en_US">
    
    <!-- Twitter Card -->
    <meta name="twitter:card" content="summary">
    <meta name="twitter:title" content="Syefdi Fasmawi Syaban | QA Tester & Builder">
    <meta name="twitter:description" content="Junior QA Tester with hands-on experience in functional testing, regression testing, and contributing to enterprise web systems.">
    
    <!-- Favicon -->
    <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><rect width='100' height='100' rx='20' fill='%230ea5e9'/><text y='.9em' font-size='70' x='50%' text-anchor='middle' font-family='monospace' fill='white'>S</text></svg>">
    
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Fira+Code:wght@400;500&display=swap" rel="stylesheet">
    
    <!-- Devicons for technology icons -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/devicon.min.css">
    
    <!-- Stylesheet -->
    <link rel="stylesheet" href="css/main.css">
    
    <!-- FOUC Prevention: Theme Initialization -->
    <script>
        (function() {
            const storedTheme = localStorage.getItem('theme');
            const systemPrefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
            const theme = storedTheme || (systemPrefersDark ? 'dark' : 'light');
            document.documentElement.setAttribute('data-theme', theme);
        })();
    </script>
</head>
<body>
''' + body_content + '''
    <!-- Main Script -->
    <script src="js/main.js"></script>
</body>
</html>'''

# Write new index.html
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("✓ New clean index.html created!")
print("  - Links to css/main.css")
print("  - Links to js/main.js")
print("  - Original backed up to index.html.backup")
