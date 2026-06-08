from pathlib import Path

# Files that need comment tags added to their footer
files_need_tags = [
    "room.html",
    "Deluxeroom.html",
    "Familyroom.html",
    "Lakeviewroom.html"
]

# Update each file to add the comment tags
for filename in files_need_tags:
    filepath = Path(filename)
    if filepath.exists():
        content = filepath.read_text('utf-8')
        
        # Check if footer comment tags are already there
        if "<!-- Footer Starts -->" not in content:
            # Add opening comment tag before <footer>
            content = content.replace(" <footer>", "\n    <!-- Footer Starts -->\n    <footer>", 1)
            
        if "<!-- Back to top ends -->" not in content:
            # Find the closing pattern and add comment tags
            if "</div>\n    </footer>" in content:
                content = content.replace("</div>\n    </footer>", "</div>\n    </footer>\n    <!-- Footer Ends -->\n\n    <!-- Back to top start -->\n    <div id=\"back-to-top\">\n      <a href=\"#\"></a>\n    </div>\n    <!-- Back to top ends -->", 1)
        
        filepath.write_text(content, 'utf-8')
        print(f"✓ Added footer tags to {filename}")
    else:
        print(f"✗ File not found: {filename}")

print("\nDone!")
