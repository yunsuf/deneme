#!/bin/bash

# Mermaid.ink API kullanarak diyagramları PNG'ye çevir
# Usage: ./render_diagrams.sh

DIAGRAMS_DIR="diagrams"
OUTPUT_DIR="images"

mkdir -p "$OUTPUT_DIR"

for file in "$DIAGRAMS_DIR"/*.mmd; do
    if [ -f "$file" ]; then
        name=$(basename "$file" .mmd)
        content=$(cat "$file")
        
        # Base64 encode
        encoded=$(echo "$content" | base64 -w 0)
        
        # Mermaid.ink URL
        url="https://mermaid.ink/img/base64:${encoded}"
        
        # Download
        output_file="$OUTPUT_DIR/diagram_${name}.png"
        
        if curl -s -o "$output_file" "$url"; then
            # Check if valid PNG
            if file "$output_file" | grep -q "PNG"; then
                echo "✅ $name"
            else
                echo "❌ $name (invalid response)"
                rm -f "$output_file"
            fi
        else
            echo "❌ $name (download failed)"
        fi
    fi
done

echo ""
echo "Tamamlanan görseller:"
ls -la "$OUTPUT_DIR"/diagram_*.png 2>/dev/null || echo "Hiçbir görsel oluşturulamadı"
