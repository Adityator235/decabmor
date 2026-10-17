#!/usr/bin/env python3
import json, re

# Load photos
with open("screenshots/photos.json") as f:
    photos = json.load(f)

PH = {}
for k, v in [
    ("gifts", "Screenshot 2026-10-15 233634.jpg"),
    ("storefront", "Screenshot 2026-10-15 233644.jpg"),
    ("cards", "Screenshot 2026-10-15 233656.jpg"),
    ("health", "Screenshot 2026-10-15 233725.jpg"),
    ("interior", "Screenshot 2026-10-15 233737.jpg"),
    ("counter", "Screenshot 2026-10-15 233746.jpg"),
    ("logo", "Screenshot 2026-10-15 233756.png"),
    ("services", "Screenshot 2026-10-15 233809.jpg"),
]:
    PH[k] = photos[v]

DECA = "https://static.wixstatic.com/media/810bf5_a14a97173fb4422299fc25eb04cf8e088~mv2.png/v1/fill/w_217,h_59,al_c,q_85,usm_0.66_1.00_0.01,enc_avif,quality_auto/LOGO_DECA_65_defxx.png"

# Read CSS
with open("build_theme.py") as f:
    bc = f.read()
cs = bc.find("CSS = r\"\"\"")
ce = bc.find("\"\"\"", cs+9)
CSS = bc[cs+9:ce]

def b64(key):
    fmt = "png" if key == "logo" else "jpeg"
    return "data:image/" + fmt + ";base64," + PH[key]

# Read and substitute placeholders in cover
with open("html_cover.txt") as f:
    cover_html = f.read()
cover_html = cover_html.replace("PH_STOREFRONT", b64("storefront"))
cover_html = cover_html.replace("PH_DECA", DECA)

# Read and substitute placeholders in content
with open("html_content.txt") as f:
    content_html = f.read()
content_html = content_html.replace("PH_STOREFRONT", b64("storefront"))
content_html = content_html.replace("PH_GIFTS", b64("gifts"))
content_html = content_html.replace("PH_INTERIOR", b64("interior"))
content_html = content_html.replace("PH_COUNTER", b64("counter"))
content_html = content_html.replace("PH_CARDS", b64("cards"))
content_html = content_html.replace("PH_SERVICES", b64("services"))

# Split content into individual pages by <!-- PAGE N: -->
pages = re.split(r'<!--\s*PAGE\s*\d+:\s*[^>]*-->\s*\n?', content_html)
pages = [p.strip() for p in pages if p.strip()]

# Build page titles from section labels
def get_title(html):
    m = re.search(r'<h1[^>]*>(.*?)</h1>', html)
    return m.group(1).strip() if m else "Page"

def get_nav_bar():
    return f'''<div class="top-bar"></div>
<div class="nav">
  <img src="{b64("logo")}" alt="StarCare" class="nav-logo">
  <div class="nav-divider"></div>
  <img src="{DECA}" alt="DECA" class="nav-deca">
  <div class="nav-divider"></div>
  <span class="nav-title">Project Swastik - BMOR 2026-2027</span>
</div>'''

def get_nav_controls(curr, total):
    prev_url = "index.html" if curr == 1 else f"page_{curr-1:02d}.html"
    next_url = f"page_{curr+1:02d}.html" if curr < total else "index.html"
    return f'''<div class="nav-controls">
  <a href="{prev_url}" class="nav-link" title="Previous page">&larr; Prev</a>
  <a href="{next_url}" class="nav-link" title="Next page">Next &rarr;</a>
</div>
<div class="page-indicator">Page {curr} of {total}</div>'''

# Write each page
for i, page_html in enumerate(pages):
    page_num = i + 1
    title = get_title(page_html)
    filename = f"page_{page_num:02d}.html"

    full_html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>StarCareRx - {title}</title>
<link href="https://fonts.googleapis.com/css2?family=Merriweather:wght@400;700;900&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<style>
{CSS}
</style>
</head>
<body>
{get_nav_bar()}
{page_html}
{get_nav_controls(page_num, len(pages))}
</body>
</html>'''

    with open(filename, "w", encoding="utf-8") as f:
        f.write(full_html)
    print(f"  {filename} - {title}")

# Write cover page
cover_filename = "index.html"
cover_full = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>StarCareRx - Project Swastik</title>
<link href="https://fonts.googleapis.com/css2?family=Merriweather:wght@400;700;900&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<style>
{CSS}
</style>
</head>
<body>
{get_nav_bar()}
{cover_html}
<div class="nav-controls">
  <a href="page_01.html" class="nav-link" title="Next page">Next &rarr;</a>
</div>
<div class="page-indicator">Cover Page</div>
</body>
</html>'''

with open(cover_filename, "w", encoding="utf-8") as f:
    f.write(cover_full)
print(f"  {cover_filename} - Cover Page")

# Write a simple index page listing all pages
index_links = ""
for i, page_html in enumerate(pages):
    title = get_title(page_html)
    index_links += f'<a href="page_{i+1:02d}.html">{title}</a><br>\n'

index_html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>StarCareRx - Project Swastik</title>
<link href="https://fonts.googleapis.com/css2?family=Merriweather:wght@400;700;900&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<style>
{CSS}
body {{ background: var(--bg); padding: 40px 20px; }}
.index-page {{ max-width: 600px; margin: 0 auto; text-align: center; padding-top: 80px; }}
.index-page h1 {{ font-family: Merriweather, serif; color: var(--primary); margin-bottom: 10px; }}
.index-page p {{ color: #666; margin-bottom: 30px; }}
.index-page a {{ display: block; padding: 12px 20px; margin: 8px 0; background: white; border-radius: 8px; text-decoration: none; color: var(--primary); font-weight: 500; box-shadow: 0 1px 3px rgba(0,0,0,0.1); }}
.index-page a:hover {{ background: var(--teal); color: white; }}
</style>
</head>
<body>
<div class="index-page">
  <h1>Project Swastik</h1>
  <p>StarCare Pharmacy - DECA BMOR 2026-2027</p>
  <a href="index.html">Cover Page</a>
  {index_links}
</div>
</body>
</html>'''

with open("_index.html", "w", encoding="utf-8") as f:
    f.write(index_html)
print("  _index.html - Page Index")

print(f"\nDone! Generated {len(pages) + 2} files total.")
