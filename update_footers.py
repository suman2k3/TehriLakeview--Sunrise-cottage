from pathlib import Path

# Read the footer from index.html
index_file = Path("index.html")
index_content = index_file.read_text('utf-8')

# Extract the footer section from index.html
footer_start = index_content.find("    <!-- Footer Starts -->")
footer_end = index_content.find("    <!-- Back to top ends -->") + len("    <!-- Back to top ends -->")
new_footer = index_content[footer_start:footer_end]

# Files to update
files_to_update = [
    "aboutus.html",
    "blog-full.html",
    "restaurant.html",
    "contact.html",
    "room.html",
    "Deluxeroom.html",
    "Familyroom.html",
    "Lakeviewroom.html"
]

# Update each file
for filename in files_to_update:
    filepath = Path(filename)
    if filepath.exists():
        content = filepath.read_text('utf-8')
        
        # Find and replace footer
        footer_start_pattern = "    <!-- Footer Starts -->"
        footer_end_pattern = "    <!-- Back to top ends -->"
        
        old_footer_start = content.find(footer_start_pattern)
        old_footer_end = content.find(footer_end_pattern) + len(footer_end_pattern)
        
        if old_footer_start != -1 and old_footer_end > old_footer_start:
            new_content = content[:old_footer_start] + new_footer + content[old_footer_end:]
            filepath.write_text(new_content, 'utf-8')
            print(f"✓ Updated {filename}")
        else:
            print(f"✗ Could not find footer in {filename}")
    else:
        print(f"✗ File not found: {filename}")

print("\nDone!")
