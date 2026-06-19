import re
import os
from pathlib import Path

# Path to the workspace
workspace_dir = Path("c:/Users/Suman/Desktop/tehri2")

# 1. Read clean footer from index.html
index_path = workspace_dir / "index.html"
index_content = index_path.read_text(encoding='utf-8')

footer_match = re.search(r"<footer>.*?</footer>", index_content, re.DOTALL)
if not footer_match:
    print("Error: Could not find footer in index.html")
    exit(1)
clean_footer = footer_match.group(0)

# 2. Iterate through all HTML files and apply footer/specific tag fixes
html_files = [f for f in os.listdir(workspace_dir) if f.endswith('.html')]

for file_name in html_files:
    file_path = workspace_dir / file_name
    content = file_path.read_text(encoding='utf-8')
    original_content = content
    
    # --- File Specific Fixes ---
    
    if file_name == "restaurant-menu.html":
        # Fix double </head> by removing the first </head>\n    <style> and placing <style> inside the head
        if "</head>\n    <style>" in content:
            content = content.replace("</head>\n    <style>", "\n    <style>", 1)
        elif "</head>\r\n    <style>" in content:
            content = content.replace("</head>\r\n    <style>", "\r\n    <style>", 1)
            
    elif file_name == "Lakeviewroom.html":
        # Fix unclosed <p> at line 291 and unclosed divs/sections
        target_p = """<p style="font-size:17px;line-height:1.9;">
    <span style="background-color: #fff3a0; font-weight: bold; padding: 3px 6px; border-radius: 4px;">
     Wake up to breathtaking lake views, enjoy modern amenities,
    free WiFi, room service, and a peaceful atmosphere designed
    to make your stay unforgettable.
    </span>

            </div>"""
        
        replacement_p = """<p style="font-size:17px;line-height:1.9;">
    <span style="background-color: #fff3a0; font-weight: bold; padding: 3px 6px; border-radius: 4px;">
     Wake up to breathtaking lake views, enjoy modern amenities,
    free WiFi, room service, and a peaceful atmosphere designed
    to make your stay unforgettable.
    </span>
</p>
            </div>
        </div>
    </div>
</section>"""
        if target_p in content:
            content = content.replace(target_p, replacement_p, 1)
        else:
            # Let's try replacing with normalized newlines
            content = content.replace(target_p.replace('\n', '\r\n'), replacement_p.replace('\n', '\r\n'), 1)
            
        # Ensure we have scripts, body, and html tags if they were cut off
        if "</body>" not in content:
            content += """
    <!-- *Scripts* -->
    <script src="js/jquery-3.3.1.min.js"></script>
    <script src="js/bootstrap.min.js"></script>
    <script src="js/plugin.js"></script>
    <script src="js/main.js"></script>
    <script src="js/custom-nav.js"></script>
</body>
</html>
"""

    elif file_name == "room.html":
        # Fix link outside head
        bad_link = '<html lang="en">\n  <link rel="stylesheet"\nhref="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css">\n<head>'
        bad_link_crlf = '<html lang="en">\r\n  <link rel="stylesheet"\r\nhref="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css">\r\n<head>'
        good_link = '<html lang="en">\n<head>\n  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css">'
        if bad_link in content:
            content = content.replace(bad_link, good_link, 1)
        elif bad_link_crlf in content:
            content = content.replace(bad_link_crlf, good_link.replace('\n', '\r\n'), 1)
            
        # Fix double </style>
        content = content.replace("</style>\n    </style>", "</style>", 1)
        content = content.replace("</style>\r\n    </style>", "</style>", 1)
        
        # Fix commented out <li> on instagram link
        bad_li = """                <!--   <li>
                    <a href="#"><i class="fab fa-twitter" aria-hidden="true"></i></a>
                  </li>
                  <li> -->
                    <a href="https://www.instagram.com/tehrilakeviewsunrisecottages/reels/" target="_blank"><i class="fab fa-instagram" aria-hidden="true"></i></a>
                  </li>"""
        good_li = """                  <li>
                    <a href="https://www.instagram.com/tehrilakeviewsunrisecottages/reels/" target="_blank"><i class="fab fa-instagram" aria-hidden="true"></i></a>
                  </li>"""
        if bad_li in content:
            content = content.replace(bad_li, good_li, 1)
        else:
            content = content.replace(bad_li.replace('\n', '\r\n'), good_li.replace('\n', '\r\n'), 1)
            
        # Close the room-page section before the footer if unclosed
        if "</section>\n    \n    <!-- Footer Starts -->" not in content and "</section>\r\n    \r\n    <!-- Footer Starts -->" not in content:
            # Let's add the </section> tag right before the footer starts
            content = content.replace("    <!-- Footer Starts -->", "</section>\n    \n    <!-- Footer Starts -->", 1)
            content = content.replace("    <footer>", "</section>\n    \n    <footer>", 1)

    elif file_name == "Familyroom.html":
        # Close the room-page section before footer and remove extra section tag at the end
        if "</section>\n    \n    <!-- Footer Starts -->" not in content and "</section>\r\n    \r\n    <!-- Footer Starts -->" not in content:
            content = content.replace("    <!-- Footer Starts -->", "</section>\n    \n    <!-- Footer Starts -->", 1)
            content = content.replace("    <footer>", "</section>\n    \n    <footer>", 1)
            
        if "</section>\n\n\n</body>" not in content and "</body>" not in content:
            # Remove trailing </section> and add scripts + body + html
            content = re.sub(r"</section>\s*$", "", content)
            content += """
    <!-- *Scripts* -->
    <script src="js/jquery-3.3.1.min.js"></script>
    <script src="js/bootstrap.min.js"></script>
    <script src="js/plugin.js"></script>
    <script src="js/main.js"></script>
    <script src="js/custom-nav.js"></script>
</body>
</html>
"""

    elif file_name == "Deluxeroom.html":
        # Close room-page section before footer and ensure we have scripts, body, and html tags
        if "</section>\n    \n    <!-- Footer Starts -->" not in content and "</section>\r\n    \r\n    <!-- Footer Starts -->" not in content:
            content = content.replace("    <!-- Footer Starts -->", "</section>\n    \n    <!-- Footer Starts -->", 1)
            content = content.replace("    <footer>", "</section>\n    \n    <footer>", 1)
            
        if "js/jquery-3.3.1.min.js" not in content:
            # Remove trailing </body>\n</html> if any and append correctly with scripts
            content = re.sub(r"</body>\s*</html>\s*$", "", content)
            content += """
    <!-- *Scripts* -->
    <script src="js/jquery-3.3.1.min.js"></script>
    <script src="js/bootstrap.min.js"></script>
    <script src="js/plugin.js"></script>
    <script src="js/main.js"></script>
    <script src="js/custom-nav.js"></script>
</body>
</html>
"""

    # --- Footer Replacements ---
    
    # Replace footer in all files except index.html
    if file_name != "index.html":
        content = re.sub(r"<footer>.*?</footer>", clean_footer, content, flags=re.DOTALL)

    if content != original_content:
        file_path.write_text(content, encoding='utf-8')
        print(f"✓ Fixed tags/footer in {file_name}")

print("\nDone applying HTML fixes!")
