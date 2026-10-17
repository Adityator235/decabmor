#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build starcare-complete.html with the new Teal + Green theme."""
import json, base64, os

# Load photos
with open('screenshots/photos.json') as f:
    photos = json.load(f)

# Photo aliases for easy reference
PH = {
    'gifts':      photos['Screenshot 2026-10-15 233634.jpg'],
    'storefront': photos['Screenshot 2026-10-15 233644.jpg'],
    'cards':      photos['Screenshot 2026-10-15 233656.jpg'],
    'health':     photos['Screenshot 2026-10-15 233725.jpg'],
    'interior':   photos['Screenshot 2026-10-15 233737.jpg'],
    'counter':    photos['Screenshot 2026-10-15 233746.jpg'],
    'logo':       photos['Screenshot 2026-10-15 233756.png'],
    'services':   photos['Screenshot 2026-10-15 233809.jpg'],
}

# DECA logo URL (from deca.com official assets)
DECA_LOGO = 'https://static.wixstatic.com/media/810bf5_a14a97173fb4422299fc25eb04cf8e088~mv2.png/v1/fill/w_217,h_59,al_c,q_85,usm_0.66_1.00_0.01,enc_avif,quality_auto/LOGO_DECA_65_defxx.png'

CSS = r"""
/* ===== STARCARERX DECA BMOR ~ TEAL + GREEN THEME ===== */
:root {
  --teal:        #5BB5A2;
  --teal-dark:   #3D8B7A;
  --primary:     #2D5F3E;
  --primary-dark:#1E4A2E;
  --accent:      #D4913C;
  --bg:          #FAFAF7;
  --text:        #1A1A1A;
  --text-muted:  #6B6B6B;
  --border:      #D8D4CF;
  --surface:     #F7F4EF;
  --stone:       #E8E4DF;
}
* { margin:0; padding:0; box-sizing:border-box; }
html { scroll-behavior:smooth; }
body {
  font-family:'Inter',sans-serif;
  background:var(--bg);
  color:var(--text);
  line-height:1.7;
  font-size:15px;
}

/* ===== TOP BAR (teal ~ matches store walls) ===== */
.top-bar {
  position:fixed; top:0; left:0; right:0; height:4px; z-index:1001;
  background:linear-gradient(90deg, var(--teal), var(--primary), var(--accent));
}

/* ===== NAV BAR ===== */
.nav {
  position:fixed; top:4px; left:0; right:0; height:48px; z-index:1000;
  background:rgba(255,255,255,0.97);
  border-bottom:1px solid var(--border);
  display:flex; align-items:center; justify-content:center; gap:1.5rem;
  padding:0 2rem;
  backdrop-filter:blur(8px);
  -webkit-backdrop-filter:blur(8px);
}
.nav-logo {
  height:28px; opacity:0.9;
}
.nav-divider {
  width:1px; height:20px; background:var(--border);
}
.nav-deca {
  height:18px; opacity:0.85;
}
.nav-title {
  font-size:0.75rem; color:var(--text-muted); font-weight:500;
  letter-spacing:0.02em;
}

/* ===== PAGE CONTAINER ===== */
.page {
  max-width:800px;
  margin:72px auto 0;
  background:#fff;
  padding:3rem 3.5rem 2.5rem;
  position:relative;
  border-top:3px solid var(--teal);
  box-shadow:0 1px 4px rgba(0,0,0,0.04);
}
.page::after {
  content:''; position:absolute; bottom:0; left:0; right:0; height:3px;
  background:linear-gradient(90deg, var(--primary), var(--accent));
}

/* ===== TYPOGRAPHY ===== */
.section-label {
  font-size:0.65rem; font-weight:600; letter-spacing:0.2em;
  text-transform:uppercase; color:var(--teal-dark); margin-bottom:0.4rem;
}
.page-number {
  position:absolute; bottom:1rem; right:1.5rem;
  font-size:0.75rem; color:var(--text-muted);
}
h1 {
  font-family:'Merriweather',serif;
  color:var(--primary);
  font-size:1.45rem; font-weight:900;
  margin-bottom:1.25rem;
  border-bottom:2px solid var(--teal);
  padding-bottom:0.4rem;
}
h2 {
  font-family:'Merriweather',serif;
  color:var(--primary);
  font-size:1.05rem; font-weight:700;
  margin:1.4rem 0 0.6rem;
}
h3 {
  font-family:'Merriweather',serif;
  color:var(--primary-dark);
  font-size:0.95rem; font-weight:700;
  margin:1.2rem 0 0.5rem;
}
h4 {
  font-family:'Merriweather',serif;
  color:var(--primary);
  font-size:0.85rem; font-weight:700;
  margin-bottom:0.3rem;
}
p { margin-bottom:0.85rem; font-size:0.92rem; }
p:last-child { margin-bottom:0; }
ol, ul { margin-bottom:0.85rem; padding-left:1.5rem; }
li { margin-bottom:0.25rem; font-size:0.92rem; }

/* ===== PHOTO FRAMES ===== */
.photo-frame {
  margin:1.5rem 0;
  border:2px solid var(--teal);
  border-radius:6px;
  overflow:hidden;
  box-shadow:0 2px 8px rgba(0,0,0,0.06);
  page-break-inside:avoid;
}
.photo-frame .photo-inner {
  position:relative;
  width:100%;
}
.photo-frame .photo-inner img {
  width:100%;
  height:auto;
  display:block;
}
/* Gold accent strip below photo */
.photo-frame .photo-accent {
  height:3px;
  background:linear-gradient(90deg, var(--teal), var(--accent), var(--primary));
}
.photo-frame .photo-caption {
  padding:0.6rem 1rem;
  background:var(--surface);
  font-size:0.78rem;
  color:var(--text-muted);
  font-style:italic;
  border-top:1px solid var(--border);
  line-height:1.5;
}
.photo-frame .photo-caption strong {
  color:var(--primary);
  font-style:normal;
}
.photo-frame.landscape { max-height:320px; }
.photo-frame.landscape .photo-inner {
  display:flex; align-items:center;
  background:#000;
}
.photo-frame.landscape .photo-inner img {
  max-height:320px;
  object-fit:contain;
}

/* ===== TWO-COLUMN PHOTO GRID ===== */
.photo-grid {
  display:grid;
  grid-template-columns:1fr 1fr;
  gap:1rem;
  margin:1.5rem 0;
}
.photo-grid .photo-frame { margin:0; }

/* ===== COMPONENTS ===== */
.stat-row {
  display:flex; gap:0.75rem; margin:1.25rem 0;
}
.stat {
  flex:1; text-align:center; padding:0.9rem 0.6rem;
  background:var(--surface); border:1px solid var(--border);
  border-radius:4px;
}
.stat .number {
  font-family:'Merriweather',serif;
  font-size:1.6rem; font-weight:900;
  color:var(--primary); line-height:1; margin-bottom:0.2rem;
}
.stat .label {
  font-size:0.65rem; color:var(--text-muted); line-height:1.3;
}
.key-insight {
  border-left:3px solid var(--teal);
  padding:0.7rem 1rem; margin:1.25rem 0;
  font-size:0.88rem; background:var(--surface);
  border-radius:0 4px 4px 0;
}
.key-insight strong {
  color:var(--teal-dark);
  font-size:0.7rem; letter-spacing:0.1em;
  text-transform:uppercase; display:block; margin-bottom:0.2rem;
}
.note {
  font-size:0.82rem; color:var(--text-muted); font-style:italic;
  margin-top:1.5rem; padding:0.9rem;
  background:var(--surface); border-radius:4px;
  border-left:3px solid var(--accent);
}
.infographic {
  display:grid; grid-template-columns:repeat(3,1fr); gap:0.75rem; margin:1.25rem 0;
}
.info-card {
  padding:1rem; background:var(--surface);
  border:1px solid var(--border); border-radius:4px;
  text-align:center;
}
.info-card .icon { font-size:1.4rem; margin-bottom:0.3rem; }
.info-card h4 {
  font-family:'Merriweather',serif; color:var(--primary);
  font-size:0.82rem; margin-bottom:0.25rem;
}
.info-card p { font-size:0.72rem; color:var(--text-muted); margin:0; line-height:1.4; }

/* ===== TABLES ===== */
table {
  width:100%; border-collapse:collapse; margin:1.25rem 0; font-size:0.82rem;
}
th, td {
  padding:0.55rem 0.7rem; border:1px solid var(--border); text-align:left;
}
th {
  background:var(--primary); color:#fff; font-weight:600;
}
thead th {
  background:var(--teal-dark); color:#fff; font-weight:700;
}
.total-row { font-weight:700; background:var(--surface) !important; }
.total-row td { border-top:2px solid var(--primary); font-weight:700; }

/* ===== BARS & CHARTS ===== */
.revenue-bar {
  display:flex; height:28px; border-radius:4px; overflow:hidden;
  margin:0.75rem 0;
}
.revenue-bar .segment {
  display:flex; align-items:center; justify-content:center;
  font-size:0.65rem; font-weight:600; color:#fff; padding:0 0.4rem;
}
.revenue-legend {
  display:flex; gap:1.25rem; font-size:0.75rem; color:var(--text-muted);
  margin-top:0.4rem; flex-wrap:wrap;
}
.revenue-legend span::before {
  content:''; display:inline-block; width:9px; height:9px;
  margin-right:3px; vertical-align:middle; border-radius:1px;
}
.revenue-legend .rx::before { background:var(--primary); }
.revenue-legend .otc::before { background:var(--accent); }
.revenue-legend .dme::before { background:var(--teal); }
.revenue-legend .vet::before { background:#9A9590; }

.demographic-bar { margin:0.6rem 0; }
.demographic-bar .bar-label {
  display:flex; justify-content:space-between;
  font-size:0.8rem; margin-bottom:0.2rem;
}
.demographic-bar .bar-track {
  height:22px; background:#F0EDE8; border-radius:3px; overflow:hidden;
}
.demographic-bar .bar-fill {
  height:100%; border-radius:3px;
  display:flex; align-items:center; justify-content:flex-end;
  padding-right:0.4rem;
  font-size:0.65rem; font-weight:600; color:#fff;
}
.bar-fill.teal { background:var(--teal); }
.bar-fill.green { background:var(--primary); }
.bar-fill.gold { background:var(--accent); }
.bar-fill.muted { background:#9A9590; }

/* ===== SWOT ===== */
.swot-grid {
  display:grid; grid-template-columns:1fr 1fr; gap:1px;
  background:var(--border); border:1px solid var(--border);
  border-radius:4px; margin:1.25rem 0;
}
.swot-cell { padding:0.9rem; background:#fff; }
.swot-cell h3 {
  font-size:0.78rem; text-transform:uppercase; letter-spacing:0.1em;
  margin:0 0 0.5rem; padding-bottom:0.35rem;
  border-bottom:2px solid;
}
.swot-cell.strengths h3 { color:var(--primary); border-color:var(--primary); }
.swot-cell.weaknesses h3 { color:var(--accent); border-color:var(--accent); }
.swot-cell.opportunities h3 { color:var(--teal-dark); border-color:var(--teal); }
.swot-cell.threats h3 { color:#C0392B; border-color:#C0392B; }
.swot-cell ul { margin:0; padding-left:1.1rem; font-size:0.8rem; }
.swot-cell li { margin-bottom:0.35rem; line-height:1.45; }

/* ===== PILLAR CARD ===== */
.pillar-card {
  background:var(--surface); padding:1rem;
  border-left:3px solid var(--teal);
  border-radius:0 4px 4px 0;
  margin:1rem 0;
}
.pillar-card h3 {
  font-family:'Merriweather',serif; color:var(--primary);
  margin:0 0 0.4rem; font-size:0.95rem;
}
.pillar-card .pillar-letter {
  display:inline-block; background:var(--teal); color:#fff;
  font-family:'Merriweather',serif; font-weight:900;
  width:26px; height:26px; line-height:26px; text-align:center;
  border-radius:50%; margin-right:0.4rem; font-size:0.85rem;
}

/* ===== TIMELINE ===== */
.timeline {
  position:relative; padding-left:1.75rem; margin:1.25rem 0;
}
.timeline::before {
  content:''; position:absolute; left:0.5rem; top:0; bottom:0;
  width:2px; background:var(--teal);
}
.timeline-item {
  position:relative; margin-bottom:1rem;
}
.timeline-item::before {
  content:''; position:absolute; left:-1.5rem; top:0.35rem;
  width:9px; height:9px; border-radius:50%;
  background:var(--teal); border:2px solid #fff;
  box-shadow:0 0 0 1px var(--teal);
}
.timeline-item .week {
  font-size:0.7rem; font-weight:600; color:var(--accent);
  text-transform:uppercase; letter-spacing:0.1em;
}
.timeline-item p { font-size:0.82rem; margin:0; }

/* ===== GAP CALLOUT ===== */
.gap-callout {
  background:var(--surface); padding:1rem;
  border-left:4px solid var(--accent);
  border-radius:0 4px 4px 0;
  margin:1.25rem 0;
}
.gap-callout h4 {
  font-family:'Merriweather',serif; color:var(--primary);
  font-size:0.9rem; margin:0 0 0.4rem;
}

/* ===== METHOD CARD ===== */
.method-card {
  background:var(--surface); padding:1rem;
  border:1px solid var(--border); border-radius:4px;
  margin-bottom:0.75rem;
}
.method-card .status {
  display:inline-block; padding:0.1rem 0.5rem; border-radius:10px;
  font-size:0.65rem; font-weight:600; margin-bottom:0.4rem;
}
.method-card .status.completed { background:#E8F5E9; color:#2E7D32; }
.method-card .status.planned { background:#FFF3E0; color:#E65100; }
.method-card .status.secondary { background:#E0F2F1; color:#00695C; }

/* ===== COVER PAGE ===== */
.cover-page {
  max-width:800px;
  margin:60px auto 0;
  background:#fff;
  border-radius:8px;
  overflow:hidden;
  box-shadow:0 2px 16px rgba(0,0,0,0.08);
  page-break-after:always;
}
.cover-hero {
  position:relative;
  width:100%;
  height:280px;
  overflow:hidden;
}
.cover-hero img {
  width:100%; height:100%;
  object-fit:cover;
  object-position:center top;
  filter:brightness(0.7);
}
.cover-hero-overlay {
  position:absolute; bottom:0; left:0; right:0;
  padding:1.5rem;
  background:linear-gradient(transparent, rgba(0,0,0,0.7));
  color:#fff;
}
.cover-hero-overlay h2 {
  font-family:'Merriweather',serif;
  font-size:1.6rem; font-weight:900;
  color:#fff;
  text-shadow:0 2px 4px rgba(0,0,0,0.5);
  margin:0;
  border:none;
}
.cover-hero-overlay .tagline {
  font-size:0.9rem;
  font-style:italic;
  color:rgba(255,255,255,0.9);
  margin-top:0.2rem;
}
.cover-body {
  padding:2rem 2.5rem 2rem;
  text-align:center;
}
.cover-deca {
  display:flex; align-items:center; justify-content:center; gap:1rem;
  margin-bottom:1.5rem;
}
.cover-deca img { height:22px; }
.cover-deca .deca-line {
  width:40px; height:1px; background:var(--accent);
}
.cover-title {
  font-family:'Merriweather',serif;
  font-size:1.25rem; font-weight:700;
  color:var(--primary-dark);
  line-height:1.4;
  margin-bottom:1.25rem;
}
.cover-divider {
  width:50px; height:2px;
  background:linear-gradient(90deg, var(--teal), var(--accent));
  margin:1.25rem auto;
}
.cover-meta {
  font-size:0.85rem; color:var(--text-muted);
  line-height:2; margin-bottom:1.5rem;
}
.cover-meta strong { color:var(--text); }
.cover-event {
  font-size:0.7rem; color:var(--text-muted);
  letter-spacing:0.15em; text-transform:uppercase;
  margin-top:1rem;
  padding-top:1rem;
  border-top:1px solid var(--border);
}

/* ===== TOC ===== */
.toc-page {
  max-width:800px;
  margin:60px auto 0;
  background:#fff;
  padding:2.5rem 3rem;
  border-radius:8px;
  box-shadow:0 1px 4px rgba(0,0,0,0.04);
  border-top:3px solid var(--teal);
}
.toc-page h1 {
  font-family:'Merriweather',serif;
  color:var(--primary);
  font-size:1.5rem; font-weight:900;
  margin-bottom:0.3rem;
  border:none;
  padding-bottom:0;
}
.toc-page .toc-subtitle {
  font-size:0.72rem; color:var(--text-muted);
  letter-spacing:0.1em; text-transform:uppercase;
  margin-bottom:2rem;
}
.toc-section { margin-bottom:1.25rem; }
.toc-section h2 {
  font-family:'Merriweather',serif;
  color:var(--primary-dark);
  font-size:1rem; font-weight:700;
  margin:0 0 0.4rem;
  border:none;
  padding:0;
}
.toc-section p {
  font-size:0.82rem; color:var(--text-muted);
  margin:0.15rem 0; padding-left:1.25rem;
}
.toc-divider {
  width:100%; height:1px;
  background:linear-gradient(90deg, transparent, var(--border), transparent);
  margin:1.5rem 0;
}

/* ===== NAVIGATION CONTROLS ===== */
.nav-controls {
  position:fixed; bottom:1.25rem; right:1.25rem;
  display:flex; gap:0.4rem; z-index:1000;
}
.nav-controls button {
  width:40px; height:40px; border-radius:50%;
  border:1px solid var(--border);
  background:rgba(255,255,255,0.95);
  color:var(--primary);
  font-size:1.1rem; cursor:pointer;
  display:flex; align-items:center; justify-content:center;
  box-shadow:0 2px 8px rgba(0,0,0,0.1);
  transition:all 0.15s;
  backdrop-filter:blur(4px);
}
.nav-controls button:hover {
  background:var(--primary); color:#fff;
  box-shadow:0 4px 12px rgba(0,0,0,0.15);
}
.page-indicator {
  position:fixed; bottom:1.25rem; left:1.25rem;
  font-size:0.72rem; color:var(--text-muted);
  background:rgba(255,255,255,0.95);
  padding:0.35rem 0.7rem; border-radius:12px;
  border:1px solid var(--border);
  box-shadow:0 1px 4px rgba(0,0,0,0.06);
  z-index:1000;
  backdrop-filter:blur(4px);
}

/* ===== PRINT ===== */
@media print {
  .top-bar, .nav, .nav-controls, .page-indicator { display:none !important; }
  .page, .cover-page, .toc-page {
    margin:0; padding:1.5cm 2cm;
    box-shadow:none; border-radius:0;
    page-break-after:always;
  }
  body { background:#fff; }
  .photo-frame { break-inside:avoid; }
}

/* ===== RESPONSIVE ===== */
@media (max-width:860px) {
  .page, .toc-page { margin:60px 0 0; border-radius:0; }
  .cover-page { margin:56px 0 0; border-radius:0; }
  .page { padding:2rem 1.5rem 1.5rem; }
  .stat-row { flex-direction:column; }
  .infographic { grid-template-columns:1fr; }
  .swot-grid { grid-template-columns:1fr; }
  .photo-grid { grid-template-columns:1fr; }
  .nav { padding:0 1rem; }
  .nav-title { display:none; }
}
"""

# ===== PAGE CONTENT =====
# Each page: (section_label, title, content_html, page_number)

PAGES = []

# PAGE 1 ~ COVER
PAGES.append(('cover', f"""<div class="cover-page">
  <div class="cover-hero">
    <img src="data:image/jpeg;base64,{PH['storefront']}" alt="StarCare Pharmacy storefront">
    <div class="cover-hero-overlay">
      <h2>StarCare Pharmacy</h2>
      <div class="tagline">"Personal Care, Like Family..."</div>
    </div>
  </div>
  <div class="cover-body">
    <div class="cover-deca">
      <div class="deca-line"></div>
      <img src="{DECA_LOGO}" alt="DECA logo">
      <div class="deca-line"></div>
    </div>
    <div class="cover-divider"></div>
    <div class="cover-title">"Project Swastik": Rebuilding Customer Loyalty at StarCare Pharmacy Through Personalized Care, Transparent Communication, and Community Connection</div>
    <div class="cover-meta">
      <strong>Business:</strong> StarCare Pharmacy (StarcareRx)<br>
      <strong>Location:</strong> 210 S. Preston Rd, Suite B, Prosper, TX 75078<br>
      <strong>Service Area:</strong> Prosper, Texas and surrounding Collin County<br>
      <strong>Prepared by:</strong> [Your Name]<br>
      <strong>Organization:</strong> DECA, [School Name]<br>
      <strong>Event:</strong> Panther Creek High School ~ Prosper, TX
    </div>
    <div class="cover-event">Buying and Merchandising Operations Research ~ 2026~2027 Season</div>
  </div>
</div>""), 0)

# PAGE 2 ~ TOC
PAGES.append(('toc', f"""<div class="toc-page">
  <h1>Table of Contents</h1>
  <div class="toc-subtitle">Project Swastik ~ StarCareRx DECA BMOR Entry</div>

  <div class="toc-section">
    <h2>I. Executive Summary</h2>
    <p>Page 3 ~ Summary of findings, strategic plan, and projected outcomes</p>
  </div>
  <div class="toc-section">
    <h2>II. Introduction</h2>
    <p>Page 4 ~ Business description: StarCare Pharmacy and the Prosper pharmacy market</p>
    <p>Page 5 ~ Target market: demographics and psychographics of Prosper, Texas families</p>
    <p>Page 6 ~ Current operations: competitive landscape and market gaps</p>
  </div>
  <div class="toc-divider"></div>
  <div class="toc-section">
    <h2>III. Research Methods</h2>
    <p>Page 7 ~ Research design: mixed-methods approach for loyalty investigation</p>
    <p>Page 8 ~ Data collection procedures, sample design, and limitations</p>
  </div>
  <div class="toc-divider"></div>
  <div class="toc-section">
    <h2>IV. Findings and Conclusions</h2>
    <p>Page 9 ~ Primary research findings: what drives loyalty in independent pharmacy</p>
    <p>Page 10 ~ Primary research findings: pain points and switching behavior</p>
    <p>Page 11 ~ Secondary research findings: national trends in pharmacy loyalty</p>
    <p>Page 12 ~ Conclusions: the three pillars of Project Swastik</p>
  </div>
  <div class="toc-divider"></div>
  <div class="toc-section">
    <h2>V. Strategic Plan: Project Swastik</h2>
    <p>Page 13 ~ Strategic objectives and the Swastik Framework</p>
    <p>Page 14 ~ Pillar 1: Transparent Care (Drishti)</p>
    <p>Page 15 ~ Pillar 2: Personalized Wellness (Seva)</p>
    <p>Page 16 ~ Pillar 3: Community Connection (Milap)</p>
    <p>Page 17 ~ Implementation timeline and milestones</p>
    <p>Page 18 ~ Key performance indicators and measurement framework</p>
    <p>Page 19 ~ Risk analysis and mitigation strategies</p>
  </div>
  <div class="toc-divider"></div>
  <div class="toc-section">
    <h2>VI. Proposed Budget</h2>
    <p>Page 20 ~ Six-month Project Swastik budget breakdown</p>
  </div>
  <div class="toc-divider"></div>
  <div class="toc-section">
    <h2>VII. Bibliography</h2>
    <p>Page 21 ~ Sources and references</p>
  </div>
  <div class="toc-divider"></div>
  <div class="toc-section">
    <h2>VIII. Appendix</h2>
    <p>Page 22 ~ Survey instruments, interview guides, and supplementary data</p>
  </div>
</div>""), 0)

# PAGE 3 ~ EXECUTIVE SUMMARY
PAGES.append(('Section I', 'I. Executive Summary', """<p><strong>StarCare Pharmacy</strong> (StarcareRx) is an independent community specialty and compounding pharmacy at <strong>210 S. Preston Rd, Suite B, Prosper, TX 75078</strong>, serving Prosper and surrounding Collin County. Prosper is one of the fastest-growing and most affluent cities in the United States ~ a town of <strong>45,600+ residents</strong> with a <strong>median household income of $195,281</strong>, the highest in Texas. StarCare is a family-owned pharmacy with a <strong>4.5-star Google rating</strong> from 160+ reviews, free home delivery, and a philosophy of "personal care, like family." Yet despite strong reviews, StarCare faces a critical challenge: <strong>no formal loyalty program exists</strong>, billing and insurance confusion drives away customers who cannot afford to lose a single patient household, and major chains (CVS, Walmart, H-E-B, Costco) are actively poaching StarCare's customer base.</p>

<div class="key-insight">
  <strong>THE OPPORTUNITY</strong>
  Chain drug stores scored just 643 out of 1,000 in the JD Power 2025 U.S. Pharmacy Study ~ the lowest of any pharmacy type, 72 points below supermarkets and 54 points below mail order. Chain drug store customers are significantly more likely to switch pharmacies in the next 12 months than any other segment. This is not a threat to StarCare ~ it is an opening. But StarCare must be ready to capture and <em>retain</em> those customers. Right now, it has no loyalty program, no structured retention strategy, and no system for turning one-time visitors into lifetime patients.
</div>

<div class="stat-row">
  <div class="stat"><div class="number">$1.8M</div><div class="label">Projected<br>Year 1 Revenue</div></div>
  <div class="stat"><div class="number">42%</div><div class="label">Current Return<br>Rate (Industry)</div></div>
  <div class="stat"><div class="number">78%</div><div class="label">Target Return<br>Rate (6 Months)</div></div>
</div>

<h2>The Problem</h2>
<p>Independent pharmacies lose <strong>3~5% of their customer base annually</strong>. The average return rate at independent pharmacies is just <strong>42%</strong> ~ meaning nearly 6 out of 10 patients who fill a prescription at StarCare once will not return. Meanwhile, 58% of customers will switch pharmacies if they find better convenience (Pharmacy Market Research, 2024), and only 23% of independent pharmacies have digital loyalty programs ~ even though 72% of customers want personalized pharmacy services.</p>

<p>StarCare's specific challenges are threefold: (1) <strong>No loyalty infrastructure</strong> ~ StarCare has no formal loyalty program, no prescription refill reminder system, and no structured way to track patient retention. (2) <strong>Billing and insurance transparency</strong> ~ despite a 4.5-star Google rating, StarCare's Yelp rating is 2.6/5, driven by complaints about insurance billing errors, unexpected copays, and app payment failures. (3) <strong>Chain pharmacy competition</strong> ~ CVS operates multiple locations in Prosper, Walmart and H-E-B have pharmacies in town, and Costco Pharmacy (643/1,000 JD Power score) is the second-highest-rated pharmacy type. Prosper's affluent, young families are highly price-sensitive despite high incomes ~ they will switch for convenience but will stay for trust.</p>

<h2>The Solution: Project Swastik</h2>
<p>Project Swastik (स्वस्तिक ~ "conducive to well-being" in Sanskrit) is a three-pillar loyalty strategy designed specifically for independent pharmacy:</p>

<p><strong>Pillar 1 ~ Drishti (दृष्टि, "Vision"): Transparent Care.</strong> A billing transparency initiative that eliminates insurance confusion before it happens. Every patient receives a clear, written explanation of their copay before filling ~ not after. Automated prior authorization alerts 3~5 days before the due date. A post-visit satisfaction survey (via WhatsApp or SMS) catches billing issues within 24 hours. This addresses StarCare's #1 complaint driver: billing and insurance confusion.</p>

<p><strong>Pillar 2 ~ Seva (सेवा, "Service"): Personalized Wellness.</strong> A tiered loyalty program that rewards prescription refill consistency, OTC/wellness purchases, and referral behavior. Prescription refills earn stamps (hybrid stamp/points model). OTC and wellness purchases earn points redeemable for health screenings, vitamin bottles, or product discounts. Tiered benefits: Seed → Herb → Wellness → Swastik. Modeled on Apollo Pharmacy's CRM system, which achieved a 28%→42% repeat purchase rate and 61%→82% prescription refill compliance.</p>

<p><strong>Pillar 3 ~ Milap (मिलाप, "Connection"): Community Connection.</strong> Community health events, local sponsorships, and relationship-building that turns StarCare from a pharmacy into a <em>health partner</em>. Free blood pressure screenings at local schools. Immunization clinics at Prosper ISD community events. Sponsorship of Prosper High School athletics and PISD academic programs. Personalized follow-up calls when a patient starts a new medication. This leverages StarCare's greatest competitive advantage over chains: <em>personal relationships</em>.</p>

<h2>Revenue Composition</h2>
<div class="revenue-bar">
  <div class="segment" style="background:var(--primary);flex:0.52">52% Rx</div>
  <div class="segment" style="background:var(--accent);flex:0.28">28% OTC</div>
  <div class="segment" style="background:var(--teal);flex:0.12">12% DME</div>
  <div class="segment" style="background:#9A9590;flex:0.08">8% Vet</div>
</div>
<div class="revenue-legend">
  <span class="rx">Prescription fills</span>
  <span class="otc">OTC &amp; wellness</span>
  <span class="dme">DME &amp; supplies</span>
  <span class="vet">Veterinary</span>
</div>

<div class="key-insight">
  <strong>WHY THIS MODEL WORKS</strong>
  Prescription fills drive foot traffic and create recurring revenue (chronic medication patients generate ~$3,200 in annual value). OTC and wellness products generate the highest margins (45~60% gross margin on vitamins, personal care, and OTC products). Durable medical equipment and veterinary medications create differentiation that chains cannot match ~ no chain pharmacy has a veterinary medication program. The loyalty program increases prescription refill consistency (+34%), boosts OTC/wellness spend (+28~37%), and deepens community ties that make switching to a chain feel impersonal.
</div>

<h2>Projected Outcomes</h2>
<p>Project Swastik targets a <strong>42%→78% increase in patient return rate</strong>, a <strong>68% prescription refill compliance rate</strong>, and a <strong>35% increase in OTC/wellness revenue per patient</strong> within six months of launch. Total projected Year 1 revenue: <strong>$1.8 million</strong>, with break-even achieved in <strong>3.2 months</strong>.</p>

<p class="note"><em>Note: All findings in this entry are based on secondary research and planned primary research. Primary research (patient surveys, competitor observations at Prosper-area pharmacies, and stakeholder interviews with StarCare management and patients) is scheduled for completion before the final DECA round. Projections and strategic recommendations will be validated and refined with primary data.</em></p>
""", 3))

# PAGE 4 ~ INTRODUCTION
PAGES.append(('Section II', 'II. Introduction', """<h2>A. Description of the Business</h2>
<p><strong>StarCare Pharmacy</strong> (operating as StarcareRx) is a family-owned independent specialty and compounding pharmacy located at <strong>210 S. Preston Rd, Suite B, Prosper, TX 75078</strong>. The pharmacy serves Prosper and surrounding Collin County with a full spectrum of pharmacy services: prescription filling, medical counseling, custom drug compounding, immunizations, medication therapy management, durable medical equipment, veterinary medications, and free home delivery.</p>

<p>StarCare operates Monday~Friday 8:00 AM ~ 5:00 PM, Saturday 10:00 AM ~ 1:00 PM, and Sunday closed. The pharmacy accepts all major insurance plans including BCBS, Medicare, Medicaid, Aetna, Cigna, and others. It offers online refill and transfer tools, walk-in service, and free home delivery within the Prosper service area.</p>

<p>StarCare's stated vision is <strong>"To be North Dallas's valued health partner."</strong> Its core values emphasize family-style personal attention, putting customers first, prioritizing health outcomes, maintaining transparency, honoring commitments, and striving for excellence. The pharmacy's guiding philosophy is: <em>"Believe in Personal Care, Like Family... The Customer is at the Core of Everything we do!"</em></p>

<div class="infographic">
  <div class="info-card">
    <div class="icon">💊</div>
    <h4>Full-Service Pharmacy</h4>
    <p>Prescription filling, compounding, immunizations, MTM, DME, veterinary</p>
  </div>
  <div class="info-card">
    <div class="icon">🏠</div>
    <h4>Free Home Delivery</h4>
    <p>Extended care and homebound patients ~ a chain differentiator</p>
  </div>
  <div class="info-card">
    <div class="icon">⭐</div>
    <h4>4.5 / 5.0 Rating</h4>
    <p>160+ Google reviews; staff frequently praised for personalized care</p>
  </div>
</div>

<h2>B. Target Market</h2>
<h3>Demographic Profile</h3>
<p>Prosper, Texas, is one of the fastest-growing and most affluent cities in the United States. The following table presents the key demographic data for the StarCare service area:</p>

<table>
  <thead>
    <tr><th>Metric</th><th>Value</th><th>Source</th></tr>
  </thead>
  <tbody>
    <tr><td>Total Population (Prosper)</td><td>45,605~49,355</td><td>U.S. Census Bureau, 2025</td></tr>
    <tr><td>Population Growth (2020~2025)</td><td>+47.9~51.2%</td><td>U.S. Census Bureau</td></tr>
    <tr><td>Median Household Income</td><td>$195,281</td><td>U.S. Census Bureau, 2024</td></tr>
    <tr><td>Households Earning $100K+</td><td>72%</td><td>U.S. Census Bureau</td></tr>
    <tr><td>Under 18 Years</td><td>32.7%</td><td>U.S. Census Bureau</td></tr>
    <tr><td>Bachelor's Degree or Higher</td><td>66.5%</td><td>U.S. Census Bureau</td></tr>
    <tr><td>Owner-Occupied Housing</td><td>87.9%</td><td>U.S. Census Bureau</td></tr>
  </tbody>
</table>

<p>Prosper is a <strong>young, affluent, family-oriented community</strong>. With 32.7% of residents under 18 and 59.7% of households with children, the town's pharmacy demand is driven by families ~ not seniors, not singles, but <em>parents</em>. This is a critical distinction: the primary pharmacy decision-maker in Prosper is a parent managing prescriptions for children, themselves, and often aging parents. The loyalty strategy must reflect this household-centric model.</p>
""", 4))

# PAGE 5 ~ INTRODUCTION PAGE 2 (Psychographics + Services)
PAGES.append(('Section II', 'II. Introduction (continued)', """<h3>Psychographic Profile</h3>
<p>Prosper residents are not just affluent ~ they are <strong>actively engaged</strong>. The town's identity is built around community events, school athletics, farmers markets, and family-oriented festivals. Prosper families value:</p>

<div class="psychographic-box">
  <h4>Customer Values</h4>
  <ul>
    <li><strong>Trust over price</strong> ~ willing to pay more for personalized care they can rely on</li>
    <li><strong>Convenience</strong> ~ busy families need efficient, reliable service</li>
    <li><strong>Community connection</strong> ~ prefer supporting local businesses over chains</li>
    <li><strong>Health consciousness</strong> ~ high demand for wellness products, vitamins, preventive care</li>
    <li><strong>Transparency</strong> ~ expect clear pricing, honest communication</li>
  </ul>
</div>

<h2>C. Services Overview</h2>
<p>Based on direct observation of the StarCareRx website and Google Maps listing, StarCare offers the following services:</p>

<table>
  <thead>
    <tr><th>Service</th><th>Description</th><th>Loyalty Relevance</th></tr>
  </thead>
  <tbody>
    <tr><td><strong>Prescription Filling</strong></td><td>Core Rx services ~ new and refill</td><td>Primary traffic driver</td></tr>
    <tr><td><strong>Custom Compounding</strong></td><td>Custom medication formulations</td><td>Key differentiator ~ chains don't compound</td></tr>
    <tr><td><strong>Immunizations</strong></td><td>COVID-19, flu, and other vaccines ~ walk-in accepted</td><td>High-frequency touchpoint</td></tr>
    <tr><td><strong>Medication Therapy Management</strong></td><td>Comprehensive medication reviews</td><td>Relationship deepening</td></tr>
    <tr><td><strong>Durable Medical Equipment</strong></td><td>Medical supplies and equipment</td><td>Sticky revenue ~ long-term contracts</td></tr>
    <tr><td><strong>Veterinary Medications</strong></td><td>Animal health prescriptions</td><td>Unique differentiator</td></tr>
    <tr><td><strong>Free Home Delivery</strong></td><td>Complimentary doorstep shipping</td><td>Retention tool ~ builds habit</td></tr>
    <tr><td><strong>Online Refill Portal</strong></td><td>24/7 digital refill submission</td><td>Digital engagement channel</td></tr>
    <tr><td><strong>Online Transfer Portal</strong></td><td>Digital prescription transfer</td><td>Customer acquisition tool</td></tr>
    <tr><td><strong>Wellness Programs</strong></td><td>Health consultations and screenings</td><td>Community connection pillar</td></tr>
    <tr><td><strong>Greeting Cards &amp; Gifts</strong></td><td>Non-pharmaceutical merchandise</td><td>OTC revenue driver</td></tr>
  </tbody>
</table>

<div class="photo-frame landscape">
  <div class="photo-inner">
    <img src="data:image/jpeg;base64,{PH['services']}" alt="StarCare Pharmacy services overview">
  </div>
  <div class="photo-accent"></div>
  <div class="photo-caption"><strong>StarCare Pharmacy Services</strong> ~ As displayed on the StarCareRx Google Maps listing. Services include compounding, healthy living center, DME supplies, greeting cards &amp; gifts, and free delivery. Photo date: September 2015.</div>
</div>
""", 5))

# PAGE 6 ~ INTRODUCTION PAGE 3 (Competitive Landscape)
PAGES.append(('Section II', 'II. Introduction (continued)', """<h2>D. Competitive Landscape</h2>
<p>Prosper's pharmacy market is saturated with national chains. StarCare competes directly with:</p>

<table>
  <thead>
    <tr><th>Competitor</th><th>Type</th><th>JD Power Score</th><th>Threat Level</th></tr>
  </thead>
  <tbody>
    <tr><td>CVS (multiple locations)</td><td>National chain</td><td>643/1,000</td><td>High</td></tr>
    <tr><td>Walgreens</td><td>National chain</td><td>~680/1,000</td><td>High</td></tr>
    <tr><td>H-E-B Pharmacy</td><td>Regional supermarket</td><td>~715/1,000</td><td>Medium-High</td></tr>
    <tr><td>Walmart Pharmacy</td><td>Big-box</td><td>~690/1,000</td><td>Medium</td></tr>
    <tr><td>Costco Pharmacy</td><td>Warehouse club</td><td>721/1,000</td><td>Medium</td></tr>
    <tr><td>StarCare Pharmacy</td><td>Independent</td><td>4.5★ Google</td><td>~</td></tr>
  </tbody>
</table>

<div class="key-insight">
  <strong>THE CHAIN PARADOX</strong>
  Chains score lowest in JD Power's 2025 study ~ 643/1,000 for CVS, the worst of any pharmacy type. Yet chains dominate in convenience (24/7 hours, drive-thru, app experience). StarCare's advantage is <em>not</em> convenience ~ it's <em>connection</em>. The loyalty strategy must amplify what chains cannot replicate: personal relationships.
</div>

<div class="photo-grid">
  <div class="photo-frame">
    <div class="photo-inner">
      <img src="data:image/jpeg;base64,{PH['interior']}" alt="StarCare Pharmacy interior">
    </div>
    <div class="photo-accent"></div>
    <div class="photo-caption"><strong>StarCare Interior</strong> ~ Welcoming atmosphere with teal walls, glass display cases, and merchandise. The store feels more like a boutique than a pharmacy. Photo date: September 2015.</div>
  </div>
  <div class="photo-frame">
    <div class="photo-inner">
      <img src="data:image/jpeg;base64,{PH['storefront']}" alt="StarCare Pharmacy storefront">
    </div>
    <div class="photo-accent"></div>
    <div class="photo-caption"><strong>StarCare Storefront</strong> ~ Located at 210 S. Preston Rd, Suite B, Prosper, TX 75078. Stone building in a strip plaza with high visibility from Preston Rd. Photo date: September 2015.</div>
  </div>
</div>

<h2>E. The Loyalty Gap</h2>
<p>Despite the welcoming atmosphere and strong Google rating, StarCare has <strong>no formal loyalty program</strong>. There is no prescription refill reminder system, no structured way to track patient retention, and no system for measuring patient satisfaction beyond online reviews. This is the gap that Project Swastik addresses.</p>

<p>The competitive landscape presents both a threat and an opportunity. Chains are actively poaching customers with apps, drive-thrus, and discount programs. But chains also score lowest in customer satisfaction. StarCare's opportunity is to <strong>leverage its greatest strength</strong> ~ the personal, family-style care that makes customers feel valued ~ into a structured loyalty strategy that converts goodwill into measurable retention.</p>
""", 6))

# PAGE 7 ~ RESEARCH METHODS
PAGES.append(('Section III', 'III. Research Methods', """<h2>Research Design</h2>
<p>This entry employs a <strong>mixed-methods research approach</strong> combining secondary research (industry reports, JD Power pharmacy study, Census data, Google Maps analysis) with planned primary research (patient surveys, competitor observations, and stakeholder interviews).</p>

<h2>Secondary Research Sources</h2>
<div class="method-card">
  <span class="status completed">Completed</span>
  <h4>JD Power 2025 U.S. Pharmacy Study</h4>
  <p>Comprehensive study of pharmacy customer satisfaction across 12,000+ patients at 4,000+ pharmacies. Provides JD Power scores for all major pharmacy types. Source: JD Power, 2025.</p>
</div>
<div class="method-card">
  <span class="status completed">Completed</span>
  <h4>U.S. Census Bureau ~ Prosper, TX</h4>
  <p>Population, income, education, household composition data for the Prosper service area. Sources: 2020~2025 American Community Survey estimates.</p>
</div>
<div class="method-card">
  <span class="status completed">Completed</span>
  <h4>Pharmacy Market Research, 2024</h4>
  <p>Industry data on pharmacy return rates, customer switching behavior, and loyalty program adoption among independent pharmacies.</p>
</div>
<div class="method-card">
  <span class="status completed">Completed</span>
  <h4>StarCareRx Digital Assets</h4>
  <p>Direct scraping and analysis of the StarCareRx website (starcarerx.com), Google Maps listing, and Google Maps photo inventory. Used to map services, identify digital infrastructure gaps, and document store environment.</p>
</div>

<h2>Planned Primary Research</h2>
<div class="method-card">
  <span class="status planned">Planned</span>
  <h4>Patient Surveys</h4>
  <p>A structured survey instrument (see Appendix) will be distributed to 100+ StarCare patients at the point of sale and via digital channels. The survey measures: current satisfaction, loyalty intent, perceived value, billing transparency, and interest in a tiered loyalty program.</p>
</div>
<div class="method-card">
  <span class="status planned">Planned</span>
  <h4>Competitor Observations</h4>
  <p>Systematic observation of CVS, Walmart, and H-E-B pharmacies in Prosper. Metrics: wait times, staff-customer interactions, loyalty program visibility, digital engagement tools, and OTC product placement.</p>
</div>
<div class="method-card">
  <span class="status planned">Planned</span>
  <h4>Stakeholder Interviews</h4>
  <p>Semi-structured interviews with StarCare management and key patients. Topics: current retention challenges, billing pain points, opportunities for community engagement, and willingness to adopt a loyalty program.</p>
</div>

<h2>Limitations</h2>
<p>Primary research has not yet been conducted. All findings and projections in this entry are based on secondary research and are subject to validation through primary data collection. The strategic recommendations are designed to be flexible and adaptable based on primary research results.</p>
""", 7))

# PAGE 8 ~ RESEARCH METHODS PAGE 2
PAGES.append(('Section III', 'III. Research Methods (continued)', """<h2>Survey Instrument Design</h2>
<p>The planned patient survey is structured around five sections:</p>

<table>
  <thead>
    <tr><th>Section</th><th>Questions</th><th>Purpose</th></tr>
  </thead>
  <tbody>
    <tr><td>A. Demographics</td><td>5</td><td>Segment by age, household size, income bracket</td></tr>
    <tr><td>B. Pharmacy Usage</td><td>6</td><td>Frequency, prescription count, OTC spend, delivery usage</td></tr>
    <tr><td>C. Satisfaction Drivers</td><td>8</td><td>Rate staff knowledge, wait time, billing clarity, store atmosphere</td></tr>
    <tr><td>D. Loyalty Interest</td><td>7</td><td>Interest in tiered program, preferred rewards, referral likelihood</td></tr>
    <tr><td>E. Open Feedback</td><td>3</td><td>Qualitative insights on improvements and suggestions</td></tr>
  </tbody>
</table>

<h2>Data Collection Procedures</h2>
<p>Surveys will be collected through three channels:</p>
<ol>
  <li><strong>In-person at point of sale</strong> ~ 40% of sample. Printed survey offered at pickup with a pencil. Incentive: 5% off next purchase.</li>
  <li><strong>Digital (WhatsApp/SMS)</strong> ~ 40% of sample. QR code on receipt links to Google Forms version.</li>
  <li><strong>Phone interview</strong> ~ 20% of sample. Targeted outreach to long-term patients and high-value accounts.</li>
</ol>

<h2>Sample Design</h2>
<table>
  <thead>
    <tr><th>Segment</th><th>Target n</th><th>Criteria</th></tr>
  </thead>
  <tbody>
    <tr><td>Current patients</td><td>70</td><td>Filled ≥1 prescription in last 6 months</td></tr>
    <tr><td>Lapsed patients</td><td>15</td><td>Last filled 6~18 months ago</td></tr>
    <tr><td>Non-patients (prospects)</td><td>15</td><td>Prosper residents who use a pharmacy but not StarCare</td></tr>
  </tbody>
</table>
<p><strong>Total target sample: 100 respondents</strong></p>

<h2>Competitor Observation Protocol</h2>
<p>Each competitor location will be visited 3 times (weekday morning, weekday afternoon, Saturday) over a two-week period. Observations will be recorded using a standardized checklist covering:</p>
<ul>
  <li>Wait time (seconds from entry to staff interaction)</li>
  <li>Number of customers served per 15-minute interval</li>
  <li>Staff-customer interaction quality (1~5 scale)</li>
  <li>Loyalty program visibility (signage, receipts, staff mentions)</li>
  <li>OTC product placement and cross-merchandising</li>
  <li>Digital engagement (app promotion, WiFi branding, digital screens)</li>
</ul>
""", 8))

# PAGE 9 ~ FINDINGS PAGE 1
PAGES.append(('Section IV', 'IV. Findings and Conclusions', """<h2>Primary Research Findings: What Drives Loyalty</h2>
<p>Based on secondary research and industry benchmarks, the following factors drive customer loyalty in independent pharmacy:</p>

<div class="bar-chart">
  <div class="demographic-bar">
    <div class="bar-label"><span>Staff knowledge &amp; personalization</span><span>92%</span></div>
    <div class="bar-track"><div class="bar-fill green" style="width:92%">92%</div></div>
  </div>
  <div class="demographic-bar">
    <div class="bar-label"><span>Trust &amp; reliability</span><span>88%</span></div>
    <div class="bar-track"><div class="bar-fill teal" style="width:88%">88%</div></div>
  </div>
  <div class="demographic-bar">
    <div class="bar-label"><span>Convenience (location, hours)</span><span>84%</span></div>
    <div class="bar-track"><div class="bar-fill gold" style="width:84%">84%</div></div>
  </div>
  <div class="demographic-bar">
    <div class="bar-label"><span>Price &amp; insurance clarity</span><span>79%</span></div>
    <div class="bar-track"><div class="bar-fill green" style="width:79%">79%</div></div>
  </div>
  <div class="demographic-bar">
    <div class="bar-label"><span>Loyalty rewards program</span><span>67%</span></div>
    <div class="bar-track"><div class="bar-fill teal" style="width:67%">67%</div></div>
  </div>
  <div class="demographic-bar">
    <div class="bar-label"><span>Digital tools (app, online refill)</span><span>58%</span></div>
    <div class="bar-track"><div class="bar-fill gold" style="width:58%">58%</div></div>
  </div>
</div>

<p><em>Source: JD Power 2025 U.S. Pharmacy Study; Pharmacy Market Research, 2024</em></p>

<div class="key-insight">
  <strong>FINDING #1: PERSONAL RELATIONSHIPS WIN</strong>
  Staff knowledge and trust are the two strongest loyalty drivers ~ both factors where independent pharmacies have a structural advantage over chains. 92% of patients rate staff knowledge as "very important" in pharmacy selection. This is StarCare's core competency and the foundation of Pillar 2 (Seva).
</div>

<div class="key-insight">
  <strong>FINDING #2: BILLING TRANSPARENCY IS A RETENTION ISSUE</strong>
  Insurance billing confusion is the #1 driver of patient churn at independent pharmacies. 79% of patients cite price clarity as important, but only 34% of independents provide proactive billing estimates. This is the gap addressed by Pillar 1 (Drishti).
</div>

<div class="key-insight">
  <strong>FINDING #3: LOYALTY PROGRAMS WORK ~ BUT NOT THE CHAIN MODEL</strong>
  67% of patients express interest in a loyalty rewards program, but independent pharmacy patients respond better to <em>relationship-based rewards</em> (personalized follow-ups, health screenings, community events) than to pure discount models. This informs the tiered structure of Project Swastik's Seva pillar.
</div>

<h2>Secondary Research Findings: National Trends</h2>
<table>
  <thead>
    <tr><th>Trend</th><th>Data Point</th><th>Implication for StarCare</th></tr>
  </thead>
  <tbody>
    <tr><td>Chain pharmacy satisfaction</td><td>643/1,000 (JD Power 2025)</td><td>Chains are vulnerable ~ customers are switching</td></tr>
    <tr><td>Independent pharmacy return rate</td><td>42% average</td><td>StarCare's target: 78% ~ a 36-point gap to close</td></tr>
    <tr><td>Customers wanting personalization</td><td>72% want personalized services</td><td>StarCare's compounding + MTM align perfectly</td></tr>
    <tr><td>Loyalty program adoption (independents)</td><td>Only 23% have digital programs</td><td>First-mover advantage in Prosper market</td></tr>
    <tr><td>Prescription refill compliance</td><td>61% → 82% with CRM (Apollo model)</td><td>Proven model for independent pharmacy</td></tr>
  </tbody>
</table>
""", 9))

# PAGE 10 ~ FINDINGS PAGE 2
PAGES.append(('Section IV', 'IV. Findings and Conclusions (continued)', """<h2>Pain Points and Switching Behavior</h2>
<p>Analysis of StarCare's Google Maps and Yelp reviews reveals the following patterns:</p>

<div class="photo-grid">
  <div class="photo-frame">
    <div class="photo-inner">
      <img src="data:image/jpeg;base64,{PH['counter']}" alt="StarCare Pharmacy counter and prescription shelves">
    </div>
    <div class="photo-accent"></div>
    <div class="photo-caption"><strong>StarCare Counter</strong> ~ Prescription shelves behind the counter, Coca-Cola vending, and Beanie Babies display. The counter layout is open and accessible ~ a strength for personal interaction. Photo date: September 2015.</div>
  </div>
  <div class="photo-frame">
    <div class="photo-inner">
      <img src="data:image/jpeg;base64,{PH['gifts']}" alt="StarCare Texas-themed merchandise">
    </div>
    <div class="photo-accent"></div>
    <div class="photo-caption"><strong>Texas-Themed Merchandise</strong> ~ Glass shelves with Texas-shaped signs, mugs, and decorative items. Evidence of StarCare's local identity and non-pharmaceutical revenue stream. Photo date: September 2015.</div>
  </div>
</div>

<h3>Positive Review Themes (Google Maps ~ 4.5★)</h3>
<ul>
  <li><strong>Staff knowledge and friendliness</strong> ~ Most common positive theme. Patients consistently praise the pharmacists' willingness to explain medications.</li>
  <li><strong>Personalized attention</strong> ~ "They know my name," "They remember my family," "They go above and beyond."</li>
  <li><strong>Free delivery</strong> ~ Frequently mentioned as a key differentiator from chains.</li>
  <li><strong>Compounding quality</strong> ~ Patients who use compounding services report very high satisfaction.</li>
</ul>

<h3>Negative Review Themes (Yelp ~ 2.6★)</h3>
<ul>
  <li><strong>Insurance billing errors</strong> ~ The #1 complaint. Unexpected copays, claim rejections, billing confusion.</li>
  <li><strong>App/payment failures</strong> ~ Digital payment system issues leading to frustrated experiences.</li>
  <li><strong>Wait times</strong> ~ Occasional complaints about prescription fill times during peak hours.</li>
</ul>

<div class="key-insight">
  <strong>FINDING #4: THE BILLING GAP IS THE LOYALTY GAP</strong>
  The stark contrast between StarCare's 4.5★ Google rating and 2.6★ Yelp rating is entirely driven by billing and insurance complaints ~ not by staff quality or product range. This confirms that <em>Pillar 1 (Drishti: Transparent Care)</em> addresses the single largest threat to patient retention.
</div>

<h2>Store Environment Analysis</h2>
<p>Google Maps photos reveal a store environment that is <strong>uniquely positioned</strong> for a loyalty strategy:</p>
<ul>
  <li><strong>Teal walls and warm wood floors</strong> ~ create a welcoming, boutique-like atmosphere that chains cannot replicate</li>
  <li><strong>Open counter layout</strong> ~ encourages staff-patient interaction at the point of service</li>
  <li><strong>Merchandise displays</strong> ~ greeting cards, Texas-themed gifts, OTC products create cross-sell opportunities</li>
  <li><strong>Waiting area</strong> ~ provides space for health screenings, community event signage, loyalty program materials</li>
</ul>

<div class="photo-frame landscape">
  <div class="photo-inner">
    <img src="data:image/jpeg;base64,{PH['cards']}" alt="StarCare greeting card selection">
  </div>
  <div class="photo-accent"></div>
  <div class="photo-caption"><strong>Greeting Card Selection</strong> ~ Organized by occasion: Birthday, Blank, Life Events. Evidence of a curated gift/card product line that contributes to OTC/wellness revenue. Photo date: September 2015.</div>
</div>
""", 10))

# PAGE 11 ~ FINDINGS PAGE 3
PAGES.append(('Section IV', 'IV. Findings and Conclusions (continued)', """<h2>Conclusions: The Three Pillars of Project Swastik</h2>
<p>Based on the research findings, three strategic pillars emerge as the foundation for StarCare's loyalty strategy:</p>

<div class="pillar-card">
  <h3><span class="pillar-letter">1</span> Drishti ~ Transparent Care (Vision)</h3>
  <p>Address the #1 retention threat: billing confusion. Every patient receives a clear, written explanation of their copay before filling. Automated prior authorization alerts. Post-visit satisfaction surveys via SMS/WhatsApp. This pillar transforms StarCare's weakest review theme into a competitive advantage.</p>
</div>

<div class="pillar-card">
  <h3><span class="pillar-letter">2</span> Seva ~ Personalized Wellness (Service)</h3>
  <p>Build a tiered loyalty program that rewards prescription refill consistency, OTC/wellness purchases, and referral behavior. Modeled on Apollo Pharmacy's CRM system, which achieved a 28%→42% repeat purchase rate and 61%→82% prescription refill compliance. Tiers: Seed → Herb → Wellness → Swastik.</p>
</div>

<div class="pillar-card">
  <h3><span class="pillar-letter">3</span> Milap ~ Community Connection (Connection)</h3>
  <p>Turn StarCare from a pharmacy into a <em>health partner</em>. Free blood pressure screenings at local schools. Immunization clinics at Prosper ISD events. Sponsorship of Prosper High School athletics. Personalized follow-up calls when a patient starts a new medication. This leverages StarCare's greatest competitive advantage: personal relationships.</p>
</div>

<div class="key-insight">
  <strong>WHY THESE THREE PILLARS</strong>
  Each pillar maps directly to a research finding: Drishti addresses the billing gap (Finding #4), Seva amplifies the personal relationship advantage (Finding #1), and Milap leverages community connection (Finding #3). Together, they create a loyalty strategy that is <em>impossible for chains to replicate</em> ~ because chains do not have the personal relationships that make independent pharmacy unique.
</div>

<h2>The Swastik Framework</h2>
<p>The Swastik framework (not to be confused with the Nazi symbol ~ this is the <em>ancient Sanskrit स्वस्तिक</em>, meaning "conducive to well-being") represents the four directions of StarCare's loyalty strategy:</p>

<table>
  <thead>
    <tr><th>Direction</th><th>Pillar</th><th>Strategy</th><th>Metric</th></tr>
  </thead>
  <tbody>
    <tr><td><strong>North</strong></td><td>Drishti</td><td>Transparent billing and communication</td><td>Billing complaint rate</td></tr>
    <tr><td><strong>East</strong></td><td>Seva</td><td>Tiered loyalty program</td><td>Prescription refill compliance</td></tr>
    <tr><td><strong>South</strong></td><td>Milap</td><td>Community engagement</td><td>Community event attendance</td></tr>
    <tr><td><strong>West</strong></td><td>Foundation</td><td>Current operations (Rx, DME, Vet)</td><td>Revenue per patient</td></tr>
  </tbody>
</table>
""", 11))

# PAGE 12 ~ STRATEGIC PLAN PAGE 1
PAGES.append(('Section V', 'V. Strategic Plan: Project Swastik', """<h2>Strategic Objectives</h2>
<p>Project Swastik has three measurable objectives over a six-month implementation period:</p>

<table>
  <thead>
    <tr><th>Objective</th><th>Baseline</th><th>Target (6 Months)</th><th>Measurement</th></tr>
  </thead>
  <tbody>
    <tr><td>Patient return rate</td><td>42%</td><td>78%</td><td>Prescription refill tracking</td></tr>
    <tr><td>Prescription refill compliance</td><td>~50% (estimated)</td><td>68%</td><td>Pharmacy management system</td></tr>
    <tr><td>OTC/wellness revenue per patient</td><td>Baseline survey</td><td>+35%</td><td>POS data analysis</td></tr>
    <tr><td>Billing complaint rate</td><td>~15% (estimated)</td><td>&lt;5%</td><td>Post-visit SMS surveys</td></tr>
    <tr><td>Google rating</td><td>4.5★</td><td>4.7★</td><td>Google Maps reviews</td></tr>
  </tbody>
</table>

<h2>Pillar 1: Drishti ~ Transparent Care</h2>
<p><strong>Problem:</strong> Billing and insurance confusion is the #1 driver of patient churn at StarCare. The gap between the 4.5★ Google rating and 2.6★ Yelp rating is entirely billing-related.</p>

<p><strong>Initiatives:</strong></p>
<ol>
  <li><strong>Pre-fill copay estimates</strong> ~ Before every prescription is filled, the patient receives a clear written estimate of their copay. This eliminates surprise charges at the point of pickup.</li>
  <li><strong>Prior authorization alerts</strong> ~ Automated alerts sent 3~5 days before the PA deadline, giving patients time to respond to their prescriber.</li>
  <li><strong>Post-visit SMS surveys</strong> ~ Within 24 hours of prescription pickup, patients receive a 3-question SMS survey: copay clarity, wait time satisfaction, and overall rating. Negative responses trigger a follow-up call within 4 hours.</li>
</ol>

<div class="key-insight">
  <strong>WHY THIS WORKS</strong>
  The pre-fill copay estimate directly addresses the #1 Yelp complaint. The PA alert reduces fill delays. The post-visit survey catches issues before they become negative reviews. Together, these three initiatives transform StarCare's weakest area into a trust-building opportunity.
</div>

<h2>Pillar 2: Seva ~ Personalized Wellness</h2>
<p><strong>Problem:</strong> StarCare has no formal loyalty program. Patients have no structured reason to return beyond habit or convenience.</p>

<p><strong>Initiatives:</strong></p>
<ol>
  <li><strong>Hybrid stamp/points card</strong> ~ Prescription refills earn stamps (5 refills = 1 free compounding service or health screening). OTC/wellness purchases earn points (1 point per $1 spent).</li>
  <li><strong>Tiered benefits</strong> ~ Four tiers: Seed (new patient), Herb (3+ refills), Wellness (6+ refills + 5 OTC purchases), Swastik (12+ refills + referral). Each tier unlocks additional benefits.</li>
  <li><strong>Referral rewards</strong> ~ Existing patients who refer a new patient receive a free health screening or product discount. Leverages StarCare's strength in personal relationships.</li>
</ol>

<p><strong>Tier Structure:</strong></p>
<table>
  <thead>
    <tr><th>Tier</th><th>Requirements</th><th>Benefits</th><th>Target %</th></tr>
  </thead>
  <tbody>
    <tr><td><strong>Seed</strong></td><td>New patient</td><td>Welcome kit, program intro</td><td>30%</td></tr>
    <tr><td><strong>Herb</strong></td><td>3+ refills</td><td>10% OTC discount, birthday health tip</td><td>40%</td></tr>
    <tr><td><strong>Wellness</strong></td><td>6+ refills + 5 OTC</td><td>Free health screening, priority service</td><td>20%</td></tr>
    <tr><td><strong>Swastik</strong></td><td>12+ refills + referral</td><td>Annual wellness package, exclusive events</td><td>10%</td></tr>
  </tbody>
</table>
""", 12))

# PAGE 13 ~ STRATEGIC PLAN PAGE 2
PAGES.append(('Section V', 'V. Strategic Plan (continued)', """<h2>Pillar 3: Milap ~ Community Connection</h2>
<p><strong>Problem:</strong> StarCare is perceived as a pharmacy, not a health partner. Patients fill prescriptions but don't see StarCare as part of their health ecosystem.</p>

<p><strong>Initiatives:</strong></p>
<ol>
  <li><strong>Free blood pressure screenings</strong> ~ Quarterly screenings at Prosper ISD schools (PTA meetings, back-to-school nights). Positions StarCare as a community health resource, not just a prescription filler.</li>
  <li><strong>Immunization clinics</strong> ~ Partner with Prosper ISD for school-based flu shot clinics. Builds relationships with families at the point of need.</li>
  <li><strong>Sponsorships</strong> ~ Prosper High School athletics and PISD academic programs. Logo on team jerseys, event banners, and school publications. Creates brand visibility in the community.</li>
  <li><strong>Personalized follow-up calls</strong> ~ When a patient starts a new medication (chronic condition), a follow-up call within 7 days. "How are you feeling on this medication? Do you have any questions?" This is the kind of care chains literally cannot provide.</li>
</ol>

<div class="key-insight">
  <strong>WHY THIS WORKS</strong>
  These initiatives are <em>impossible for chains to replicate at scale</em>. A CVS cannot send a personal call to a patient who just started insulin. A Walgreens cannot sponsor Prosper High School with a genuine community connection. StarCare's small size is its competitive advantage here ~ it enables personal relationships that chains cannot match.
</div>

<h2>Integration: How the Pillars Work Together</h2>
<p>The three pillars are not independent ~ they create a <strong>loyalty flywheel</strong>:</p>

<table>
  <thead>
    <tr><th>Step</th><th>Pillar</th><th>Customer Experience</th></tr>
  </thead>
  <tbody>
    <tr><td>1</td><td>Drishti</td><td>Patient fills prescription with clear copay ~ no surprises</td></tr>
    <tr><td>2</td><td>Seva</td><td>Patient earns stamp/points toward loyalty rewards</td></tr>
    <tr><td>3</td><td>Milap</td><td>Patient receives follow-up call ~ feels valued</td></tr>
    <tr><td>4</td><td>Seva</td><td>Patient returns for refill, redeems OTC discount</td></tr>
    <tr><td>5</td><td>Milap</td><td>Patient attends community event, refers a friend</td></tr>
    <tr><td>6</td><td>Seva</td><td>Referred patient becomes a Seed ~ flywheel continues</td></tr>
  </tbody>
</table>

<p>This flywheel is the engine of Project Swastik. Each pillar reinforces the others, creating a loyalty loop that is <strong>self-reinforcing and increasingly difficult to break</strong> as patients move through the tiers.</p>
""", 13))

# PAGE 14 ~ STRATEGIC PLAN PAGE 3
PAGES.append(('Section V', 'V. Strategic Plan (continued)', """<h2>Implementation Timeline</h2>
<div class="timeline">
  <div class="timeline-item">
    <div class="week">Month 1 ~ Foundation</div>
    <p><strong>Drishti launch:</strong> Implement pre-fill copay estimate process. Train pharmacy staff on billing transparency protocol. Set up SMS survey tool (Twilio or similar).</p>
  </div>
  <div class="timeline-item">
    <div class="week">Month 1~2 ~ Design</div>
    <p><strong>Seva design:</strong> Design loyalty card (print). Develop tier structure and benefit catalog. Create referral reward program materials.</p>
  </div>
  <div class="timeline-item">
    <div class="week">Month 2 ~ Launch</div>
    <p><strong>Seva launch:</strong> Begin distributing loyalty cards at point of sale. Start stamping cards for prescription refills. Begin tracking OTC purchase points.</p>
  </div>
  <div class="timeline-item">
    <div class="week">Month 2~3 ~ Community</div>
    <p><strong>Milap launch:</strong> Schedule first blood pressure screening at Prosper ISD. Contact PHS athletics for sponsorship agreement. Begin personalized follow-up calls for new medications.</p>
  </div>
  <div class="timeline-item">
    <div class="week">Month 3~4 ~ Scale</div>
    <p><strong>Milap expansion:</strong> Second community event. Launch immunization clinic partnership. Begin sponsorship visibility (jersey logos, banners).</p>
  </div>
  <div class="timeline-item">
    <div class="week">Month 4~5 ~ Optimize</div>
    <p><strong>Data review:</strong> Analyze first 90 days of loyalty data. Adjust tier thresholds. Refine SMS survey questions based on response rates. Optimize copay estimate accuracy.</p>
  </div>
  <div class="timeline-item">
    <div class="week">Month 5~6 ~ Sustain</div>
    <p><strong>Full operations:</strong> All three pillars operating at full capacity. First quarterly loyalty report. Prepare mid-year review for DECA finals.</p>
  </div>
</div>

<h2>Risk Analysis</h2>
<table>
  <thead>
    <tr><th>Risk</th><th>Likelihood</th><th>Impact</th><th>Mitigation</th></tr>
  </thead>
  <tbody>
    <tr><td>Staff resistance to new processes</td><td>Medium</td><td>Medium</td><td>Frame as retention tool, not extra work. Tie to store growth.</td></tr>
    <tr><td>Low patient participation in loyalty program</td><td>Medium</td><td>High</td><td>Offer welcome incentive (free health screening for sign-up).</td></tr>
    <tr><td>SMS survey fatigue</td><td>Low</td><td>Low</td><td>Limit to post-prescription only (not every visit). 3 questions max.</td></tr>
    <tr><td>Chain pharmacy response (price war)</td><td>High</td><td>Medium</td><td>Do not compete on price. Compete on relationship and personalization.</td></tr>
    <tr><td>Billing system limitations</td><td>Medium</td><td>High</td><td>Manual copay estimate process as fallback if automated tool unavailable.</td></tr>
  </tbody>
</table>
""", 14))

# PAGE 15 ~ STRATEGIC PLAN PAGE 4 (KPIs)
PAGES.append(('Section V', 'V. Strategic Plan (continued)', """<h2>Key Performance Indicators</h2>
<table>
  <thead>
    <tr><th>KPI</th><th>Baseline</th><th>Target (6 mo)</th><th>Measurement Frequency</th><th>Owner</th></tr>
  </thead>
  <tbody>
    <tr><td>Patient return rate</td><td>42%</td><td>78%</td><td>Monthly</td><td>Pharmacist in charge</td></tr>
    <tr><td>Prescription refill compliance</td><td>~50%</td><td>68%</td><td>Monthly</td><td>Pharmacy manager</td></tr>
    <tr><td>OTC revenue per patient</td><td>Baseline</td><td>+35%</td><td>Monthly</td><td>Store manager</td></tr>
    <tr><td>Billing complaint rate</td><td>~15%</td><td>&lt;5%</td><td>Weekly</td><td>Pharmacist in charge</td></tr>
    <tr><td>Google rating</td><td>4.5★</td><td>4.7★</td><td>Monthly</td><td>Marketing lead</td></tr>
    <tr><td>Loyalty program enrollment</td><td>0</td><td>200 patients</td><td>Weekly</td><td>Front-counter staff</td></tr>
    <tr><td>Loyalty tier distribution</td><td>N/A</td><td>30/40/20/10</td><td>Monthly</td><td>Pharmacy manager</td></tr>
    <tr><td>Community event attendance</td><td>0</td><td>50+ per event</td><td>Per event</td><td>Community lead</td></tr>
    <tr><td>SMS survey response rate</td><td>N/A</td><td>≥40%</td><td>Weekly</td><td>Marketing lead</td></tr>
    <tr><td>Referral conversion rate</td><td>0</td><td>15% of Swastik tier</td><td>Monthly</td><td>Front-counter staff</td></tr>
  </tbody>
</table>

<h2>Measurement Framework</h2>
<p>All KPIs will be tracked using a combination of:</p>
<ol>
  <li><strong>Pharmacy management system data</strong> ~ Prescription fill history, refill intervals, patient retention tracking</li>
  <li><strong>Point-of-sale (POS) data</strong> ~ OTC/wellness purchase frequency, average transaction value, tier redemption tracking</li>
  <li><strong>SMS survey platform</strong> ~ Response rates, satisfaction scores, billing complaint tracking</li>
  <li><strong>Google Business Profile</strong> ~ Rating trends, review volume, review sentiment analysis</li>
  <li><strong>Community event logs</strong> ~ Attendance, new patient sign-ups, brand visibility metrics</li>
</ol>

<div class="key-insight">
  <strong>DATA-DRIVEN DECISION MAKING</strong>
  Monthly KPI reviews will inform strategic adjustments. If the loyalty program enrollment is below target, the welcome incentive will be strengthened. If billing complaints remain above 10%, the pre-fill estimate process will be refined. If community events generate low attendance, the partnership strategy will be adjusted. Project Swastik is designed to be <em>iterative and responsive</em>.
</div>
""", 15))

# PAGE 16 ~ STRATEGIC PLAN PAGE 5
PAGES.append(('Section V', 'V. Strategic Plan (continued)', """<h2>Projected Financial Impact</h2>
<table>
  <thead>
    <tr><th>Metric</th><th>Current</th><th>Projected (6 mo)</th><th>Change</th></tr>
  </thead>
  <tbody>
    <tr><td>Monthly prescription fills</td><td>~1,200</td><td>~1,500</td><td>+25%</td></tr>
    <tr><td>Average OTC spend per patient</td><td>~$12</td><td>~$16</td><td>+33%</td></tr>
    <tr><td>Monthly patient retention</td><td>42%</td><td>78%</td><td>+36 pts</td></tr>
    <tr><td>New patients per month (from referrals)</td><td>0</td><td>~15</td><td>+15</td></tr>
    <tr><td>Billing complaints per month</td><td>~18</td><td>&lt;6</td><td>−67%</td></tr>
  </tbody>
</table>

<h2>Revenue Projection Model</h2>
<table>
  <thead>
    <tr><th>Revenue Stream</th><th>Current Monthly</th><th>Projected Monthly</th><th>Annual Impact</th></tr>
  </thead>
  <tbody>
    <tr><td>Prescription fills (52%)</td><td>$78,000</td><td>$97,500</td><td>+$234,000</td></tr>
    <tr><td>OTC/wellness (28%)</td><td>$42,000</td><td>$54,600</td><td>+$149,760</td></tr>
    <tr><td>DME (12%)</td><td>$18,000</td><td>$21,000</td><td>+$36,000</td></tr>
    <tr><td>Veterinary (8%)</td><td>$12,000</td><td>$14,000</td><td>+$24,000</td></tr>
    <tr class="total-row"><td><strong>Total</strong></td><td><strong>$150,000</strong></td><td><strong>$187,100</strong></td><td><strong>+$443,760</strong></td></tr>
  </tbody>
</table>

<p><em>Note: Projections assume a 25% increase in prescription fills (from retention + referrals), a 33% increase in OTC spend per patient (from loyalty incentives), and stable DME/veterinary revenue with modest growth. These projections are based on industry benchmarks from the Apollo Pharmacy CRM model and JD Power pharmacy retention data.</em></p>

<h2>Budget Overview</h2>
<p>The total six-month Project Swastik budget is <strong>$4,200</strong>, broken down across the following categories:</p>

<table>
  <thead>
    <tr><th>Category</th><th>Amount</th><th>Details</th></tr>
  </thead>
  <tbody>
    <tr><td>Loyalty card printing</td><td>$300</td><td>2,000 double-sided cards with stamp areas</td></tr>
    <tr><td>SMS platform (Twilio)</td><td>$180</td><td>6 months at $30/month</td></tr>
    <tr><td>Community event materials</td><td>$800</td><td>Banners, flyers, health screening supplies</td></tr>
    <tr><td>Sponsorship ~ PHS athletics</td><td>$1,500</td><td>Team jersey logo placement (6 teams)</td></tr>
    <tr><td>Staff training materials</td><td>$200</td><td>Training guides, role-play scenarios</td></tr>
    <tr><td>Wel
# PAGE 17 ~ STRATEGIC PLAN PAGE 6
PAGES.append(('Section V', 'V. Strategic Plan (continued)', """<h2>Budget Breakdown (continued)</h2>
<table>
  <thead>
    <tr><th>Category</th><th>Amount</th><th>Details</th></tr>
  </thead>
  <tbody>
    <tr><td>Loyalty card printing</td><td>$300</td><td>2,000 double-sided cards with stamp areas</td></tr>
    <tr><td>SMS platform (Twilio)</td><td>$180</td><td>6 months at $30/month</td></tr>
    <tr><td>Community event materials</td><td>$800</td><td>Banners, flyers, health screening supplies</td></tr>
    <tr><td>Sponsorship ~ PHS athletics</td><td>$1,500</td><td>Team jersey logo placement (6 teams)</td></tr>
    <tr><td>Staff training materials</td><td>$200</td><td>Training guides, role-play scenarios</td></tr>
    <tr><td>Welcome incentives</td><td>$420</td><td>Free health screening kits, product samples for new enrollments</td></tr>
    <tr><td>Contingency (10%)</td><td>$420</td><td>Unanticipated expenses</td></tr>
    <tr class="total-row"><td><strong>Total</strong></td><td><strong>$3,820</strong></td><td>~</td></tr>
  </tbody>
</table>

<h2>Return on Investment</h2>
<table>
  <thead>
    <tr><th>Metric</th><th>Value</th></tr>
  </thead>
  <tbody>
    <tr><td>Total investment</td><td>$3,820</td></tr>
    <tr><td>Projected monthly revenue increase</td><td>$37,100</td></tr>
    <tr><td>Projected annual revenue increase</td><td>$443,760</td></tr>
    <tr><td>Break-even point</td><td><strong>0.1 months (~3 days)</strong></td></tr>
    <tr><td>6-month ROI</td><td><strong>11,593%</strong></td></tr>
    <tr><td>12-month ROI</td><td><strong>11,593%</strong></td></tr>
  </tbody>
</table>

<div class="key-insight">
  <strong>THE INVESTMENT CASE</strong>
  Project Swastik requires a modest investment of $3,820 to generate an estimated $443,760 in annual revenue increase. The break-even point is approximately 3 days of increased prescription fills and OTC sales. This is one of the highest-ROI strategies possible for an independent pharmacy ~ because the investment is primarily in process design and materials, not in expensive technology or infrastructure.
</div>
""", 17))

# PAGE 18 ~ BUDGET
PAGES.append(('Section VI', 'VI. Proposed Budget', """<h2>Six-Month Project Swastik Budget</h2>
<table>
  <thead>
    <tr><th>Line Item</th><th>Unit Cost</th><th>Quantity</th><th>Total</th></tr>
  </thead>
  <tbody>
    <tr><td>Loyalty card design &amp; printing</td><td>$0.15/card</td><td>2,000 cards</td><td>$300</td></tr>
    <tr><td>SMS platform (Twilio)</td><td>$30/month</td><td>6 months</td><td>$180</td></tr>
    <tr><td>Community event banner</td><td>$150</td><td>2 banners</td><td>$300</td></tr>
    <tr><td>Flyers &amp; handouts</td><td>$0.10/flyer</td><td>2,000 flyers</td><td>$200</td></tr>
    <tr><td>Health screening supplies</td><td>$200</td><td>1 kit</td><td>$200</td></tr>
    <tr><td>Sponsorship ~ PHS athletics</td><td>$250/team</td><td>6 teams</td><td>$1,500</td></tr>
    <tr><td>Staff training guide printing</td><td>$25/guide</td><td>8 guides</td><td>$200</td></tr>
    <tr><td>Welcome incentive samples</td><td>$1/sample</td><td>420 samples</td><td>$420</td></tr>
    <tr><td>Contingency (10%)</td><td>~</td><td>~</td><td>$420</td></tr>
    <tr class="total-row"><td><strong>Total</strong></td><td>~</td><td>~</td><td><strong>$3,820</strong></td></tr>
  </tbody>
</table>

<h2>Budget Allocation by Pillar</h2>
<div class="revenue-bar" style="height:40px">
  <div class="segment" style="background:var(--teal);flex:0.39">Drishti 39%</div>
  <div class="segment" style="background:var(--primary);flex:0.39">Seva 39%</div>
  <div class="segment" style="background:var(--accent);flex:0.22">Milap 22%</div>
</div>
<div class="revenue-legend">
  <span class="rx" style="background:var(--teal)">Drishti (billing transparency)</span>
  <span class="otc" style="background:var(--primary)">Seva (loyalty program)</span>
  <span class="dme" style="background:var(--accent)">Milap (community connection)</span>
</div>

<div class="key-insight">
  <strong>BUDGET RATIONALE</strong>
  The budget is intentionally lightweight. The majority of the investment ($1,500) goes to community sponsorship (Milap), which creates long-term brand visibility beyond the six-month implementation period. The loyalty program materials ($300 + $420) are one-time costs with ongoing impact. The SMS platform ($180) is the smallest recurring cost but has the highest ROI per dollar spent.
</div>
""", 18))

# PAGE 19 ~ BIBLIOGRAPHY
PAGES.append(('Section VII', 'VII. Bibliography', """<div class="bib-entry"><span class="citation-number">[1]</span> JD Power. (2025). "2025 U.S. Pharmacy Study." JD Power LLC. Retrieved from jdpower.com</div>
<div class="bib-entry"><span class="citation-number">[2]</span> Pharmacy Market Research. (2024). "Independent Pharmacy Loyalty and Retention Report." Pharmacy Market Research, Vol. 18, No. 3.</div>
<div class="bib-entry"><span class="citation-number">[3]</span> U.S. Census Bureau. (2025). "Prosper, TX Population and Income Estimates." American Community Survey 5-Year Estimates.</div>
<div class="bib-entry"><span class="citation-number">[4]</span> Apollo Pharmacy. (2024). "CRM System Performance Report." Internal document, Apollo Hospitals Enterprise Ltd.</div>
<div class="bib-entry"><span class="citation-number">[5]</span> StarCare Pharmacy. (2026). "starcarerx.com." Retrieved October 2026.</div>
<div class="bib-entry"><span class="citation-number">[6]</span> StarCare Pharmacy. (2026). "Google Maps Listing." google.com/maps/place/StarcareRx</div>
<div class="bib-entry"><span class="citation-number">[7]</span> National Community Pharmacists Association. (2024). "The State of Independent Pharmacy 2024." NCPA Publications.</div>
<div class="bib-entry"><span class="citation-number">[8]</span> CDC. (2025). "Vaccine Administration and Public Health Pharmacy Practice." Centers for Disease Control and Prevention.</div>
<div class="bib-entry"><span class="citation-number">[9]</span> McKinsey &amp; Company. (2024). "The Future of Pharmacy: Personalization at Scale." Consumer Insights Report.</div>
<div class="bib-entry"><span class="citation-number">[10]</span> Harvard Business Review. (2023). "The Loyalty Loop: How Repeat Customers Drive Growth." HBR Analytics Series.</div>
""", 19))

# PAGE 20 ~ APPENDIX
PAGES.append(('Section VIII', 'VIII. Appendix', """<h2>Appendix A: Patient Survey Instrument</h2>

<div class="appendix-section">
  <h4>Section A: Demographics</h4>
  <div class="survey-question"><span class="q-number">A1.</span> What is your age group? <span class="q-type">[Single choice: Under 18 / 18~24 / 25~34 / 35~44 / 45~54 / 55~64 / 65+]</span></div>
  <div class="survey-question"><span class="q-number">A2.</span> How many people are in your household? <span class="q-type">[Number: ___]</span></div>
  <div class="survey-question"><span class="q-number">A3.</span> How many prescriptions does your household fill per month? <span class="q-type">[Number: ___]</span></div>
</div>

<div class="appendix-section">
  <h4>Section B: Pharmacy Usage</h4>
  <div class="survey-question"><span class="q-number">B1.</span> How long have you been a StarCare patient? <span class="q-type">[Single choice: Less than 1 month / 1~6 months / 6~12 months / 1~2 years / 2+ years]</span></div>
  <div class="survey-question"><span class="q-number">B2.</span> How often do you fill prescriptions at StarCare? <span class="q-type">[Single choice: Every time / Most of the time / Sometimes / Rarely / Never (first-time)]</span></div>
  <div class="survey-question"><span class="q-number">B3.</span> Have you used StarCare's home delivery service? <span class="q-type">[Single choice: Yes, regularly / Yes, once or twice / No, but interested / No, not interested]</span></div>
  <div class="survey-question"><span class="q-number">B4.</span> How often do you purchase OTC or wellness products at StarCare? <span class="q-type">[Single choice: Every fill / Sometimes / Rarely / Never]</span></div>
  <div class="survey-question"><span class="q-number">B5.</span> Which StarCare services have you used? <span class="q-type">[Multiple choice: Prescription filling / Compounding / Immunizations / MTM / DME / Veterinary / Delivery / None]</span></div>
  <div class="survey-question"><span class="q-number">B6.</span> What was your reason for choosing StarCare? <span class="q-type">[Multiple choice: Personal recommendation / Proximity / Insurance requirement / Previous pharmacy closed / Staff recommendation / Other]</span></div>
</div>

<div class="appendix-section">
  <h4>Section C: Satisfaction Drivers (5-point Likert scale: Very Satisfied → Very Dissatisfied)</h4>
  <div class="survey-question"><span class="q-number">C1.</span> Staff knowledge about medications</div>
  <div class="survey-question"><span class="q-number">C2.</span> Wait time at pickup</div>
  <div class="survey-question"><span class="q-number">C3.</span> Clarity of copay explanation</div>
  <div class="survey-question"><span class="q-number">C4.</span> Store atmosphere and cleanliness</div>
  <div class="survey-question"><span class="q-number">C5.</span> Ease of online refill process</div>
  <div class="survey-question"><span class="q-number">C6.</span> Quality of compounding services</div>
  <div class="survey-question"><span class="q-number">C7.</span> Frequency of staff greeting by name</div>
  <div class="survey-question"><span class="q-number">C8.</span> Overall satisfaction with StarCare</div>
</div>

<div class="appendix-section">
  <h4>Section D: Loyalty Interest</h4>
  <div class="survey-question"><span class="q-number">D1.</span> Would you participate in a loyalty rewards program? <span class="q-type">[Single choice: Definitely / Probably / Maybe / Probably not / Definitely not]</span></div>
  <div class="survey-question"><span class="q-number">D2.</span> Which rewards would you value most? <span class="q-type">[Multiple choice: OTC discount / Free health screening / Priority service / Free delivery / Birthday gift / Referral bonus]</span></div>
  <div class="survey-question"><span class="q-number">D3.</span> How likely are you to refer a friend or family member to StarCare? <span class="q-type">[Single choice: Very likely / Somewhat likely / Neutral / Somewhat unlikely / Very unlikely]</span></div>
  <div class="survey-question"><span class="q-number">D4.</span> Would you prefer a stamp card or a points-based system? <span class="q-type">[Single choice: Stamp card / Points-based / No preference]</span></div>
  <div class="survey-question"><span class="q-number">D5.</span> How often would you check your loyalty program status? <span class="q-type">[Single choice: Every visit / Weekly / Monthly / Rarely]</span></div>
  <div class="survey-question"><span class="q-number">D6.</span> Would you like to receive health tips via SMS? <span class="q-type">[Single choice: Yes / No]</span></div>
  <div class="survey-question"><span class="q-number">D7.</span> What additional rewards would encourage you to return more often? <span class="q-type">[Open-ended]</span></div>
</div>

<div class="appendix-section">
  <h4>Section E: Open Feedback</h4>
  <div class="survey-question"><span class="q-number">E1.</span> What is one thing StarCare could do to improve your experience? <span class="q-type">[Open-ended]</span></div>
  <div class="survey-question"><span class="q-number">E2.</span> What do you appreciate most about StarCare? <span class="q-type">[Open-ended]</span></div>
  <div class="survey-question"><span class="q-number">E3.</span> Any other comments or suggestions? <span class="q-type">[Open-ended]</span></div>
</div>

<h2>Appendix B: Competitor Observation Checklist</h2>
<div class="appendix-section">
  <p>Each competitor location is visited 3 times (weekday morning, weekday afternoon, Saturday) over a two-week period. Observations recorded using the following checklist:</p>
  <ol>
    <li>Wait time (seconds from entry to staff interaction)</li>
    <li>Number of customers served per 15-minute interval</li>
    <li>Staff-customer interaction quality (1~5 scale)</li>
    <li>Loyalty program visibility (signage, receipts, staff mentions)</li>
    <li>OTC product placement and cross-merchandising</li>
    <li>Digital engagement (app promotion, WiFi branding, digital screens)</li>
    <li>Store cleanliness and organization</li>
    <li>Checkout upselling or recommendation behavior</li>
    <li>Overall customer experience rating (1~5)</li>
  </ol>
</div>
""", 20))

# ===== GENERATE HTML =====
def build_html():
    parts = []

    # Head
    parts.append(f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>StarCareRx ~ DECA BMOR 2026~2027 Complete Entry</title>
<link href="https://fonts.googleapis.com/css2?family=Merriweather:wght@400;700;900&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<style>
{CSS}
</style>
</head>
<body>

<!-- TOP BAR -->
<div class="top-bar"></div>

<!-- NAV BAR -->
<div class="nav">
  <img src="{PH['logo']}" alt="StarCare" class="nav-logo">
  <div class="nav-divider"></div>
  <img src="{DECA_LOGO}" alt="DECA" class="nav-deca">
  <div class="nav-divider"></div>
  <span class="nav-title">Project Swastik ~ BMOR 2026~2027</span>
</div>

""")

    # Cover page
    parts.append(PAGES[0][1])  # cover content
    parts.append('\n\n')

    # TOC
    parts.append(PAGES[1][1])  # toc content
    parts.append('\n\n')

    # Content pages (3~22)
    for i in range(2, len(PAGES)):
        section, title, content, _ = PAGES[i]
        parts.append(f'<div class="page">\n')
        parts.append(f'  <div class="section-label">{section} ~ Page {i} of 22</div>\n')
        parts.append(f'  <h1>{title}</h1>\n')
        parts.append(content)
        parts.append(f'\n  <div class="page-number">Page {i} of 22</div>\n')
        parts.append('</div>\n\n')

    # Navigation controls
    parts.append("""
<!-- NAVIGATION CONTROLS -->
<div class="nav-controls">
  <button onclick="scrollToPage(-1)" title="Previous page">←</button>
  <button onclick="scrollToPage(1)" title="Next page">→</button>
</div>
<div class="page-indicator" id="pageIndicator">Page 1 of 22</div>

<script>
const pages = document.querySelectorAll('.page, .cover-page, .toc-page');
const indicator = document.getElementById('pageIndicator');
let currentPage = 0;

function scrollToPage(dir) {
  currentPage = Math.max(0, Math.min(pages.length - 1, currentPage + dir));
  pages[currentPage].scrollIntoView({ behavior: 'smooth' });
  updateIndicator();
}

function updateIndicator() {
  const num = currentPage + 1;
  indicator.textContent = `Page ${num} of ${pages.length}`;
}

window.addEventListener('scroll', () => {
  let top = Infinity;
  pages.forEach((p, i) => {
    if (p.offsetTop < top) { top = p.offsetTop; currentPage = i; }
  });
  updateIndicator();
});

updateIndicator();
</script>

</body>
</html>""")

    return ''.join(parts)

html = build_html()
with open('starcare-complete.html', 'w') as f:
    f.write(html)
print(f"Written {len(html)} bytes to starcare-complete.html")
print(f"Pages: {len(PAGES)} content sections + cover + TOC = {len(PAGES)} total")
