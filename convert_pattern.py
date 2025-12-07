#!/usr/bin/env python3
import sys
import os

def convert_text_pattern_to_binary(input_file, output_file):
    """Convert text pattern file (space/newline separated integers) to binary format"""
    try:
        # Read the text file
        with open(input_file, 'r') as f:
            content = f.read()
        
        # Parse all numbers from the text
        # Remove newlines and split by whitespace
        numbers = []
        for part in content.split():
            try:
                num = int(part)
                # Ensure value is in valid byte range
                if 0 <= num <= 255:
                    numbers.append(num)
                else:
                    print(f"⚠️  Skipping invalid value: {num}")
            except ValueError:
                pass
        
        print(f"📊 Found {len(numbers)} byte values")
        
        # Write as binary
        with open(output_file, 'wb') as f:
            f.write(bytes(numbers))
        
        print(f"✅ Converted: {input_file} ({len(numbers)} bytes)")
        print(f"✅ Output: {output_file}")
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

# Convert all pattern files
base_dir = "/Users/maximcomarov/WebstormProjects/master/ar"

patterns = [
    ("hiro.pat", "hiro.patt"),
    ("pattern-kanji.patt", "pattern-kanji.patt"),
    ("pattern-letterA.patt", "pattern-letterA.patt"),
]

print("🔄 Converting pattern files to binary format...\n")

for input_name, output_name in patterns:
    input_path = os.path.join(base_dir, input_name)
    output_path = os.path.join(base_dir, output_name)
    
    if os.path.exists(input_path):
        print(f"Processing: {input_name}")
        convert_text_pattern_to_binary(input_path, output_path)
        print()
    else:
        print(f"⚠️  File not found: {input_path}\n")

print("✨ Done!")
