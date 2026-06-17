#!/usr/bin/env python3
import shutil
shutil.copy('index.html.backup', 'index.html')
print("✓ Restored index.html from backup")
