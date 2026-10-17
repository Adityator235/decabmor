#!/usr/bin/env python3
import json

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

# Read CSS from existing file
with open("build_theme.py") as f:
    bc = f.read()
cs = bc.find("CSS = r\"\"\"")
ce = bc.find("\"\"\"", cs+9)
CSS = bc[cs+9:ce]

# Read HTML content parts
with open("html_cover.txt") as f:
    COVER = f.read()
with open("html_content.txt") as f:
    CONTENT = f.read()

# Helper to wrap base64 in data URI
def b64(key):
    fmt = "png" if key == "logo" else "jpeg"
    return "data:image/" + fmt + ";base64," + PH[key]

# Substitute placeholders
COVER = COVER.replace("PH_STOREFRONT", b64("storefront"))
COVER = COVER.replace("PH_DECA", DECA)
CONTENT = CONTENT.replace("PH_STOREFRONT", b64("storefront"))
CONTENT = CONTENT.replace("PH_GIFTS", b64("gifts"))
CONTENT = CONTENT.replace("PH_INTERIOR", b64("interior"))
CONTENT = CONTENT.replace("PH_COUNTER", b64("counter"))
CONTENT = CONTENT.replace("PH_CARDS", b64("cards"))
CONTENT = CONTENT.replace("PH_SERVICES", b64("services"))

# Build pages list
pages = []

# Write the HTML
out = []
out.append("<!DOCTYPE html>")
out.append('<html lang="en">')
out.append("<head>")
out.append('<meta charset="UTF-8">')
out.append('<meta name="viewport" content="width=device-width, initial-scale=1.0">')
out.append('<title>StarCareRx - DECA BMOR 2026-2027 Complete Entry</title>')
out.append('<link href="https://fonts.googleapis.com/css2?family=Merriweather:wght@400;700;900&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">')
out.append("<style>")
out.append(CSS)
out.append("</style>")
out.append("</head>")
out.append("<body>")
out.append("")
out.append('<div class="top-bar"></div>')
out.append("")
out.append('<div class="nav">')
out.append('  <img src="' + b64("logo") + '" alt="StarCare" class="nav-logo">')
out.append('  <div class="nav-divider"></div>')
out.append('  <img src="' + DECA + '" alt="DECA" class="nav-deca">')
out.append('  <div class="nav-divider"></div>')
out.append('  <span class="nav-title">Project Swastik - BMOR 2026-2027</span>')
out.append("</div>")
out.append("")
out.append(COVER)
out.append("")
out.append(CONTENT)
out.append("")
out.append('<div class="nav-controls">')
out.append('  <button onclick="scrollToPage(-1)" title="Previous page">&larr;</button>')
out.append('  <button onclick="scrollToPage(1)" title="Next page">&rarr;</button>')
out.append("</div>")
out.append('<div class="page-indicator" id="pageIndicator">Page 1 of 20</div>')
out.append("")
out.append("""<script>
const pages = document.querySelectorAll('.page, .cover-page');
const indicator = document.getElementById('pageIndicator');
let currentPage = 0;

function scrollToPage(dir) {
  currentPage = Math.max(0, Math.min(pages.length - 1, currentPage + dir));
  pages[currentPage].scrollIntoView({ behavior: 'smooth' });
  updateIndicator();
}

function updateIndicator() {
  const num = currentPage + 1;
  indicator.textContent = 'Page ' + num + ' of ' + pages.length;
}

window.addEventListener('scroll', () => {
  let top = Infinity;
  pages.forEach((p, i) => {
    if (p.offsetTop < top) { top = p.offsetTop; currentPage = i; }
  });
  updateIndicator();
});

updateIndicator();
</script>""")
out.append("")
out.append("</body>")
out.append("</html>")

with open("starcare-complete.html", "w", encoding="utf-8") as f:
    f.write("\n".join(out))

print("Done! Written starcare-complete.html")
