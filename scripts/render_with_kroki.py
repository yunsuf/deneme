#!/usr/bin/env python3
"""Render mermaid diagrams using kroki.io API"""

import os
import base64
import zlib
import urllib.request
import urllib.error

DIAGRAMS_DIR = "diagrams"
OUTPUT_DIR = "images"

def encode_kroki(source: str) -> str:
    """Encode diagram source for kroki.io"""
    compressed = zlib.compress(source.encode('utf-8'), 9)
    encoded = base64.urlsafe_b64encode(compressed).decode('ascii')
    return encoded

def render_diagram(mmd_file: str) -> bool:
    """Render a single mermaid file to PNG"""
    name = os.path.splitext(os.path.basename(mmd_file))[0]
    output_file = os.path.join(OUTPUT_DIR, f"diagram_{name}.png")
    
    with open(mmd_file, 'r', encoding='utf-8') as f:
        source = f.read()
    
    encoded = encode_kroki(source)
    url = f"https://kroki.io/mermaid/png/{encoded}"
    
    try:
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req, timeout=30) as response:
            data = response.read()
            
            # Check if PNG
            if data[:4] == b'\x89PNG':
                with open(output_file, 'wb') as f:
                    f.write(data)
                print(f"✅ {name}")
                return True
            else:
                print(f"❌ {name} (not PNG)")
                return False
    except urllib.error.HTTPError as e:
        print(f"❌ {name} (HTTP {e.code})")
        return False
    except Exception as e:
        print(f"❌ {name} ({e})")
        return False

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    success = 0
    failed = 0
    
    for filename in sorted(os.listdir(DIAGRAMS_DIR)):
        if filename.endswith('.mmd'):
            filepath = os.path.join(DIAGRAMS_DIR, filename)
            if render_diagram(filepath):
                success += 1
            else:
                failed += 1
    
    print(f"\n📊 Sonuç: {success} başarılı, {failed} başarısız")
    
    # List generated files
    print("\n📁 Oluşturulan görseller:")
    for f in sorted(os.listdir(OUTPUT_DIR)):
        if f.startswith('diagram_') and f.endswith('.png'):
            size = os.path.getsize(os.path.join(OUTPUT_DIR, f))
            print(f"  - {f} ({size} bytes)")

if __name__ == "__main__":
    main()
