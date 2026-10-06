#!/usr/bin/env python3
"""
Generate the high-resolution, Zaha Hadid-inspired, light-themed vector Exhibition Tablecloth (3m x 3m)
for Sputnik Tech Group and Sputnik Devs Studio at the South Africa Tech Showcase.

Clean & Decluttered Design (Per User Request):
- Majestic Zaha Hadid parametric purple fluid ribbons across the entire 3000mm x 3000mm canvas.
- Stripped of dense architecture micro-diagrams, walls of text, and elevator pitches.
- Prominent Company Logos & Names: Sputnik Tech Group & Sputnik Devs Studio.
- Prominent Product Logos & Names: Tradey Bay, Hostel SRMS, The University Hub, Shopnik E-Commerce, Sputnik Devs Academy.
- Large, scannable QR codes for each product.
- Clean Tabletop console with dedicated device demo pads and generous open breathing room for laptops/tablets.
- Official Executive Leadership Plaque:
  Takudzwa Mupanesure (Founder, Chief Executive Officer & Lead Architect)
  Sputnik Tech Group (Pty) Ltd | 292 Surrey Avenue, Randburg, Johannesburg, 2194
  Direct: takudzwam@sputniktechgroup.com | +27 66 321 5528 | +263 787 015 123
  In Concurrence with: Kenneth Takudzwa Katsande (Director of Operations) & Prince Lwazi Nkiwane (Director of Growth)
"""

import os
import base64
import xml.etree.ElementTree as ET

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

def get_base64_img(rel_path):
    abs_path = os.path.join(REPO_ROOT, rel_path)
    mime = "image/png"
    if rel_path.lower().endswith(".jpeg") or rel_path.lower().endswith(".jpg"):
        mime = "image/jpeg"
    with open(abs_path, "rb") as f:
        data = base64.b64encode(f.read()).decode("utf-8")
    return f"data:{mime};base64,{data}"

def get_svg_path_data(rel_path):
    abs_path = os.path.join(REPO_ROOT, rel_path)
    tree = ET.parse(abs_path)
    root = tree.getroot()
    for elem in root.iter():
        if elem.tag.endswith("path"):
            return elem.attrib.get("d")
    return None

def build_tablecloth_svg():
    # 1. Base64 images
    sputnik_tech_logo = get_base64_img("assets/Sputnik-Tech-Group-Logo.png")
    sputnik_devs_logo = get_base64_img("assets/Sputnik-Devs-Studio-logo.png")
    tradeybay_primary_logo = get_base64_img("assets/TradeyBay_primary_Logo.png")
    shopnik_logo = get_base64_img("assets/logos/shopnik-logo-horizontal-transparent.png")

    # 2. Vector QR codes
    qr_tb = get_svg_path_data("assets/qr/qr-tradeybay-playstore.svg")
    qr_acad = get_svg_path_data("assets/qr/qr-academy-apply.svg")
    qr_srms = get_svg_path_data("assets/qr/qr-student-housing-srms.svg")
    qr_unihub = get_svg_path_data("assets/qr/qr-university-hub.svg")
    qr_shopnik = get_svg_path_data("assets/qr/qr-shopnik-ecommerce.svg")

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 3000 3000" width="3000mm" height="3000mm">
  <defs>
    <!-- Background Canvas Base Gradient -->
    <linearGradient id="tcBgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="25%" stop-color="#fdfbfe"/>
      <stop offset="60%" stop-color="#faf5ff"/>
      <stop offset="100%" stop-color="#f3e8ff"/>
    </linearGradient>

    <!-- Zaha Hadid Parametric Purple Ribbon Gradients -->
    <linearGradient id="zahaPurple1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#c084fc"/>
      <stop offset="35%" stop-color="#a855f7"/>
      <stop offset="70%" stop-color="#7c3aed"/>
      <stop offset="100%" stop-color="#6b21a8"/>
    </linearGradient>

    <linearGradient id="zahaPurple2" x1="0%" y1="100%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#6b21a8"/>
      <stop offset="40%" stop-color="#7c3aed"/>
      <stop offset="80%" stop-color="#9333ea"/>
      <stop offset="100%" stop-color="#c084fc"/>
    </linearGradient>

    <linearGradient id="zahaPurple3" x1="100%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#581c87"/>
      <stop offset="45%" stop-color="#7c3aed"/>
      <stop offset="85%" stop-color="#a855f7"/>
      <stop offset="100%" stop-color="#e9d5ff"/>
    </linearGradient>

    <linearGradient id="zahaPurpleDark" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#3b0764"/>
      <stop offset="50%" stop-color="#581c87"/>
      <stop offset="100%" stop-color="#4c1d95"/>
    </linearGradient>

    <linearGradient id="zahaStreamGrad1" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#7c3aed"/>
      <stop offset="50%" stop-color="#a855f7"/>
      <stop offset="100%" stop-color="#c084fc"/>
    </linearGradient>

    <linearGradient id="zahaStreamGrad2" x1="100%" y1="0%" x2="0%" y2="0%">
      <stop offset="0%" stop-color="#6b21a8"/>
      <stop offset="50%" stop-color="#8b5cf6"/>
      <stop offset="100%" stop-color="#c084fc"/>
    </linearGradient>

    <!-- Luminous QR / Pod Container Gradients -->
    <linearGradient id="cardGradWhite" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="100%" stop-color="#faf7ff"/>
    </linearGradient>

    <linearGradient id="cardGradSoftPurple" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="100%" stop-color="#f5f3ff"/>
    </linearGradient>

    <!-- Card Drop Shadows -->
    <filter id="softCardShadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="6" stdDeviation="12" flood-color="#3b0764" flood-opacity="0.08"/>
      <feDropShadow dx="0" dy="2" stdDeviation="4" flood-color="#0f172a" flood-opacity="0.04"/>
    </filter>

    <filter id="deepCardShadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="14" stdDeviation="22" flood-color="#3b0764" flood-opacity="0.12"/>
      <feDropShadow dx="0" dy="4" stdDeviation="8" flood-color="#0f172a" flood-opacity="0.05"/>
    </filter>

    <!-- Subtle Background Dot Grid -->
    <pattern id="tcDotGrid" width="40" height="40" patternUnits="userSpaceOnUse">
      <circle cx="3" cy="3" r="1.5" fill="#7c3aed" fill-opacity="0.08"/>
    </pattern>

    <!-- Icons for Products -->
    <!-- Hostel SRMS Icon -->
    <g id="icon-hostel-srms">
      <rect width="64" height="64" rx="16" fill="#f5f3ff" stroke="#7c3aed" stroke-width="1.5"/>
      <path d="M 32 14 L 50 28 L 46 28 L 46 48 L 36 48 L 36 36 L 28 36 L 28 48 L 18 48 L 18 28 L 14 28 Z" fill="#7c3aed"/>
      <rect x="22" y="30" width="6" height="6" rx="1" fill="#ffffff"/>
      <rect x="36" y="30" width="6" height="6" rx="1" fill="#ffffff"/>
    </g>

    <!-- UniHub Icon -->
    <g id="icon-unihub">
      <rect width="64" height="64" rx="16" fill="#faf5ff" stroke="#a855f7" stroke-width="1.5"/>
      <!-- Mortarboard -->
      <polygon points="32,16 52,26 32,36 12,26" fill="#9333ea"/>
      <path d="M 20 32 L 20 44 C 20 48 25 51 32 51 C 39 51 44 48 44 44 L 44 32" fill="none" stroke="#7c3aed" stroke-width="3" stroke-linecap="round"/>
      <path d="M 46 29 L 51 38 L 49 38 L 52 46" fill="none" stroke="#f59e0b" stroke-width="2" stroke-linecap="round"/>
    </g>

    <!-- Devs Academy Icon -->
    <g id="icon-academy">
      <rect width="64" height="64" rx="16" fill="#fff7ed" stroke="#f97316" stroke-width="1.5"/>
      <!-- Code brackets & rocket -->
      <path d="M 22 24 L 14 32 L 22 40" fill="none" stroke="#ea580c" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/>
      <path d="M 42 24 L 50 32 L 42 40" fill="none" stroke="#ea580c" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/>
      <line x1="35" y1="20" x2="29" y2="44" stroke="#c2410c" stroke-width="3" stroke-linecap="round"/>
    </g>
  </defs>

  <style>
    .sans {{ font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; }}
    .mono {{ font-family: 'JetBrains Mono', 'Fira Code', 'Courier New', monospace; }}
  </style>

  <!-- =================================================================== -->
  <!-- 0. BASE CANVAS & ZAHA HADID PARAMETRIC FLUID CANOPY (3000 x 3000 mm)-->
  <!-- =================================================================== -->
  <rect width="3000" height="3000" fill="url(#tcBgGrad)"/>
  <rect width="3000" height="3000" fill="url(#tcDotGrid)"/>

  <!-- Soft Ambient Glow Pools -->
  <circle cx="800" cy="1500" r="700" fill="#ede9fe" fill-opacity="0.6"/>
  <circle cx="2200" cy="1500" r="700" fill="#f5f3ff" fill-opacity="0.6"/>
  <circle cx="1500" cy="2400" r="800" fill="#ede9fe" fill-opacity="0.5"/>
  <circle cx="1500" cy="600" r="700" fill="#ede9fe" fill-opacity="0.5"/>

  <!-- Zaha Hadid Parametric Fluid Ribbons (Flowing Across the 3m Cloth) -->
  <!-- Canopy Wave 1 (Upper Rear to Center) -->
  <path d="M -100 400 C 400 180 900 620 1500 360 C 2100 100 2600 520 3100 310 L 3100 820 C 2600 660 2000 860 1500 710 C 900 560 400 820 -100 660 Z" fill="url(#zahaPurple1)" opacity="0.14"/>

  <!-- Canopy Wave 2 (Center Mid-Flank - Under Tabletop) -->
  <path d="M -100 1280 C 500 1080 1000 1560 1600 1360 C 2200 1160 2650 1460 3100 1310 L 3100 1720 C 2600 1560 2100 1820 1500 1660 C 900 1510 400 1760 -100 1610 Z" fill="url(#zahaPurple2)" opacity="0.10"/>

  <!-- Canopy Wave 3 (Front Drape Aisle Flow) -->
  <path d="M -100 2080 C 500 1880 1100 2360 1700 2160 C 2300 1960 2700 2260 3100 2060 L 3100 2580 C 2600 2420 2100 2680 1500 2520 C 900 2360 400 2620 -100 2460 Z" fill="url(#zahaPurple3)" opacity="0.12"/>

  <!-- Dynamic Contour Streamlines -->
  <path d="M -50 480 C 450 280 950 680 1550 430 C 2150 180 2650 580 3050 380" fill="none" stroke="url(#zahaStreamGrad1)" stroke-width="3" stroke-opacity="0.35"/>
  <path d="M -50 510 C 450 310 950 710 1550 460 C 2150 210 2650 610 3050 410" fill="none" stroke="#7c3aed" stroke-width="2" stroke-opacity="0.25" stroke-dasharray="10,12"/>

  <path d="M -50 2180 C 550 1980 1150 2430 1750 2230 C 2350 2030 2750 2330 3050 2130" fill="none" stroke="url(#zahaStreamGrad2)" stroke-width="3" stroke-opacity="0.35"/>
  <path d="M -50 2210 C 550 2010 1150 2460 1750 2260 C 2350 2060 2750 2360 3050 2160" fill="none" stroke="#a855f7" stroke-width="2" stroke-opacity="0.25" stroke-dasharray="12,10"/>

  <!-- Outer Hem Clearance Safety Border (15mm from perimeter) -->
  <rect x="15" y="15" width="2970" height="2970" fill="none" stroke="#7c3aed" stroke-width="1.5" stroke-dasharray="25 15" stroke-opacity="0.3"/>

  <!-- Tabletop Boundary Guideline (1800 x 750 mm table, X: 600..2400, Y: 1125..1875) -->
  <rect x="600" y="1125" width="1800" height="750" fill="none" stroke="#7c3aed" stroke-width="2" stroke-dasharray="16 10" stroke-opacity="0.35"/>
  <g transform="translate(615, 1145)">
    <rect width="250" height="26" rx="13" fill="#ffffff" stroke="#7c3aed" stroke-width="1.2" filter="url(#softCardShadow)"/>
    <text x="125" y="17" fill="#581c87" class="mono" font-size="10.5" font-weight="800" text-anchor="middle">◀ 1.8M TABLETOP EDGE</text>
  </g>
  <g transform="translate(2135, 1145)">
    <rect width="250" height="26" rx="13" fill="#ffffff" stroke="#7c3aed" stroke-width="1.2" filter="url(#softCardShadow)"/>
    <text x="125" y="17" fill="#581c87" class="mono" font-size="10.5" font-weight="800" text-anchor="middle">TABLETOP EDGE ▶</text>
  </g>


  <!-- =================================================================== -->
  <!-- ZONE 1: TABLETOP EXECUTIVE SURFACE (1800 x 750 mm)                  -->
  <!-- Clean, open, uncluttered, device-ready (X: 600..2400, Y: 1125..1875) -->
  <!-- =================================================================== -->
  <g transform="translate(600, 1125)">

    <!-- Centerpiece Brand Monogram / Crest (X: 675..1125, Y: 100..650) -->
    <g transform="translate(900, 360)">
      <circle cx="0" cy="0" r="160" fill="#ffffff" stroke="#7c3aed" stroke-width="2.5" filter="url(#softCardShadow)"/>
      <circle cx="0" cy="0" r="148" fill="#faf5ff"/>
      <circle cx="0" cy="0" r="144" fill="none" stroke="#c084fc" stroke-width="1.5" stroke-dasharray="8 6"/>

      <!-- Orbiting Accent Rings -->
      <ellipse cx="0" cy="0" rx="190" ry="85" fill="none" stroke="#7c3aed" stroke-width="1.5" stroke-opacity="0.35" transform="rotate(-25)"/>
      <ellipse cx="0" cy="0" rx="205" ry="90" fill="none" stroke="#a855f7" stroke-width="1" stroke-opacity="0.25" stroke-dasharray="12 8" transform="rotate(35)"/>

      <!-- Center Logo / Brand Typography -->
      <image href="{sputnik_tech_logo}" x="-120" y="-85" width="240" height="80" preserveAspectRatio="xMidYMid meet"/>
      <line x1="-90" y1="5" x2="90" y2="5" stroke="#7c3aed" stroke-width="1.5"/>
      <text x="0" y="28" fill="#1e1b4b" class="sans" font-size="15" font-weight="900" letter-spacing="2" text-anchor="middle">SPUTNIK DEVS STUDIO</text>
      <text x="0" y="48" fill="#6b21a8" class="mono" font-size="10" font-weight="800" letter-spacing="1.5" text-anchor="middle">SOUTH AFRICA TECH SHOWCASE</text>
      <text x="0" y="66" fill="#64748b" class="mono" font-size="9" text-anchor="middle">sputniktechgroup.com • sputnikdevs.com</text>
    </g>

    <!-- LEFT DEMO PAD: TRADEY BAY APP (X: 60..580, Y: 80..670) -->
    <g transform="translate(60, 80)">
      <rect width="520" height="590" rx="24" fill="#ffffff" stroke="#7c3aed" stroke-width="2" filter="url(#softCardShadow)"/>
      <rect width="520" height="60" rx="24" fill="url(#zahaPurple1)" opacity="0.12"/>
      <line x1="0" y1="60" x2="520" y2="60" stroke="#7c3aed" stroke-width="1.5" stroke-opacity="0.4"/>

      <!-- Header -->
      <g transform="translate(25, 20)">
        <circle cx="10" cy="10" r="7" fill="#7c3aed"/>
        <text x="26" y="16" fill="#3b0764" class="sans" font-size="15" font-weight="900" letter-spacing="1">TRADEY BAY // MOBILE APP DEMO</text>
        <rect x="370" y="0" width="100" height="22" rx="11" fill="#faf5ff" stroke="#7c3aed" stroke-width="1"/>
        <text x="420" y="15" fill="#6b21a8" class="mono" font-size="10" font-weight="800" text-anchor="middle">v2.0.4+31</text>
      </g>

      <!-- Center Logo & Phone Reticle -->
      <g transform="translate(260, 195)">
        <image href="{tradeybay_primary_logo}" x="-130" y="-105" width="260" height="70" preserveAspectRatio="xMidYMid meet"/>
        <text x="0" y="-12" fill="#1e1b4b" class="sans" font-size="20" font-weight="900" text-anchor="middle">Campus Commerce Super App</text>
        <text x="0" y="10" fill="#6b21a8" class="mono" font-size="11" font-weight="700" text-anchor="middle">Zero Listing Fees • Verified Student Network</text>
      </g>

      <!-- Scannable QR Container -->
      <g transform="translate(145, 240)">
        <rect width="230" height="230" rx="20" fill="#faf5ff" stroke="#7c3aed" stroke-width="2" filter="url(#softCardShadow)"/>
        <rect x="15" y="15" width="200" height="200" rx="14" fill="#ffffff"/>
        <path d="{qr_tb}" fill="#2e1065" transform="translate(26, 26) scale(0.42)"/>
      </g>

      <g transform="translate(260, 505)">
        <rect x="-150" y="0" width="300" height="34" rx="17" fill="#0f172a"/>
        <text x="0" y="22" fill="#ffffff" class="mono" font-size="12" font-weight="800" text-anchor="middle">📱 SCAN TO INSTALL APP</text>
        <text x="0" y="52" fill="#64748b" class="sans" font-size="11" text-anchor="middle">Available on Google Play &amp; Apple App Store</text>
      </g>
    </g>

    <!-- RIGHT DEMO PAD: SPUTNIK DEVS & SAAS (X: 1220..1740, Y: 80..670) -->
    <g transform="translate(1220, 80)">
      <rect width="520" height="590" rx="24" fill="#ffffff" stroke="#7c3aed" stroke-width="2" filter="url(#softCardShadow)"/>
      <rect width="520" height="60" rx="24" fill="url(#zahaPurple3)" opacity="0.12"/>
      <line x1="0" y1="60" x2="520" y2="60" stroke="#7c3aed" stroke-width="1.5" stroke-opacity="0.4"/>

      <!-- Header -->
      <g transform="translate(25, 20)">
        <circle cx="10" cy="10" r="7" fill="#a855f7"/>
        <text x="26" y="16" fill="#3b0764" class="sans" font-size="15" font-weight="900" letter-spacing="1">SPUTNIK DEVS // CLOUD &amp; ACADEMY</text>
        <rect x="365" y="0" width="110" height="22" rx="11" fill="#faf5ff" stroke="#a855f7" stroke-width="1"/>
        <text x="420" y="15" fill="#7c3aed" class="mono" font-size="10" font-weight="800" text-anchor="middle">STUDIO LIVE</text>
      </g>

      <!-- Center Logo & Info -->
      <g transform="translate(260, 195)">
        <image href="{sputnik_devs_logo}" x="-135" y="-105" width="270" height="70" preserveAspectRatio="xMidYMid meet"/>
        <text x="0" y="-12" fill="#1e1b4b" class="sans" font-size="20" font-weight="900" text-anchor="middle">Enterprise Software &amp; WIL Academy</text>
        <text x="0" y="10" fill="#6b21a8" class="mono" font-size="11" font-weight="700" text-anchor="middle">Hostel SRMS • UniHub • Shopnik • Devs Academy</text>
      </g>

      <!-- Scannable QR Container -->
      <g transform="translate(145, 240)">
        <rect width="230" height="230" rx="20" fill="#faf5ff" stroke="#7c3aed" stroke-width="2" filter="url(#softCardShadow)"/>
        <rect x="15" y="15" width="200" height="200" rx="14" fill="#ffffff"/>
        <path d="{qr_acad}" fill="#2e1065" transform="translate(26, 26) scale(0.42)"/>
      </g>

      <g transform="translate(260, 505)">
        <rect x="-150" y="0" width="300" height="34" rx="17" fill="#7c3aed"/>
        <text x="0" y="22" fill="#ffffff" class="mono" font-size="12" font-weight="800" text-anchor="middle">🚀 SCAN TO APPLY / VISIT</text>
        <text x="0" y="52" fill="#64748b" class="sans" font-size="11" text-anchor="middle">sputnikdevs.com • sputnikdevs.com/academy</text>
      </g>
    </g>

  </g>


  <!-- =================================================================== -->
  <!-- ZONE 2: FRONT AISLE BILLBOARD (Y: 1875..2950)                       -->
  <!-- Facing visitors walking down the exhibition aisle                   -->
  <!-- Pure Majestic Zaha Hadid, Corporate & Product Logos (NO DENSE TEXT) -->
  <!-- =================================================================== -->
  <g transform="translate(150, 1900)">

    <!-- Outer Frame Card with Soft Ambient Shadow (2700 x 980 mm) -->
    <rect width="2700" height="980" rx="36" fill="#ffffff" stroke="#7c3aed" stroke-width="2.5" filter="url(#deepCardShadow)"/>
    <rect width="2700" height="980" rx="36" fill="url(#cardGradWhite)"/>

    <!-- 2A. TOP BILLBOARD HEADER RIBBON (Y: 0..150) -->
    <g transform="translate(0, 0)">
      <rect width="2700" height="150" rx="36" fill="url(#zahaPurple1)" opacity="0.10"/>
      <line x1="0" y1="150" x2="2700" y2="150" stroke="#7c3aed" stroke-width="2" stroke-opacity="0.3"/>

      <!-- Left Corporate Logo: Sputnik Tech Group -->
      <g transform="translate(60, 25)">
        <image href="{sputnik_tech_logo}" x="0" y="0" width="300" height="95" preserveAspectRatio="xMidYMid meet"/>
      </g>

      <!-- Center Showcase Title -->
      <g transform="translate(1350, 32)">
        <rect x="-210" y="0" width="420" height="34" rx="17" fill="#ffffff" stroke="#7c3aed" stroke-width="1.5" filter="url(#softCardShadow)"/>
        <circle cx="-185" cy="17" r="6" fill="#7c3aed"/>
        <text x="0" y="23" fill="#581c87" class="mono" font-size="13" font-weight="900" letter-spacing="2.5" text-anchor="middle">SOUTH AFRICA TECH SHOWCASE</text>

        <text x="0" y="70" fill="#1e1b4b" class="sans" font-size="34" font-weight="900" letter-spacing="1.5" text-anchor="middle">THE SPUTNIK TECH ECOSYSTEM</text>
        <text x="0" y="96" fill="#6b21a8" class="sans" font-size="16" font-weight="800" letter-spacing="1" text-anchor="middle">Enterprise Software Engineering • Campus Digital Infrastructure • High-Velocity Cloud</text>
      </g>

      <!-- Right Corporate Logo: Sputnik Devs Studio -->
      <g transform="translate(2340, 25)">
        <image href="{sputnik_devs_logo}" x="0" y="0" width="300" height="95" preserveAspectRatio="xMidYMid meet"/>
      </g>
    </g>

    <!-- 2B. THE 5 CORE PRODUCT & BRAND SHOWCASE CARDS (Y: 180..680) -->
    <!-- 5 Columns across 2700 width (X: 45, 575, 1105, 1635, 2165 — Width 490 each) -->
    
    <!-- CARD 1: TRADEY BAY (X: 45) -->
    <g transform="translate(45, 180)">
      <rect width="490" height="500" rx="20" fill="#ffffff" stroke="#7c3aed" stroke-width="1.8" filter="url(#softCardShadow)"/>
      <rect width="490" height="60" rx="20" fill="url(#zahaPurple1)" opacity="0.12"/>
      <line x1="0" y1="60" x2="490" y2="60" stroke="#e9d5ff" stroke-width="1.2"/>

      <text x="245" y="38" fill="#3b0764" class="sans" font-size="17" font-weight="900" letter-spacing="1" text-anchor="middle">TRADEY BAY</text>

      <!-- Logo & Title -->
      <g transform="translate(245, 120)">
        <image href="{tradeybay_primary_logo}" x="-130" y="-45" width="260" height="65" preserveAspectRatio="xMidYMid meet"/>
        <text x="0" y="42" fill="#1e1b4b" class="sans" font-size="18" font-weight="900" text-anchor="middle">Campus Commerce Super App</text>
        <text x="0" y="64" fill="#6b21a8" class="mono" font-size="11" font-weight="700" text-anchor="middle">0% Listing Fees • Student Network</text>
      </g>

      <!-- Scannable QR -->
      <g transform="translate(155, 215)">
        <rect width="180" height="180" rx="16" fill="#faf5ff" stroke="#7c3aed" stroke-width="1.5" filter="url(#softCardShadow)"/>
        <rect x="12" y="12" width="156" height="156" rx="10" fill="#ffffff"/>
        <path d="{qr_tb}" fill="#2e1065" transform="translate(21, 21) scale(0.33)"/>
      </g>

      <!-- Button / Link -->
      <g transform="translate(245, 435)">
        <rect x="-140" y="0" width="280" height="38" rx="19" fill="#0f172a"/>
        <text x="0" y="24" fill="#ffffff" class="mono" font-size="12" font-weight="800" text-anchor="middle">📱 SCAN TO INSTALL APP</text>
        <text x="0" y="52" fill="#64748b" class="sans" font-size="10.5" text-anchor="middle">tradeybay.com • iOS &amp; Android</text>
      </g>
    </g>

    <!-- CARD 2: HOSTEL SRMS (X: 575) -->
    <g transform="translate(575, 180)">
      <rect width="490" height="500" rx="20" fill="#ffffff" stroke="#c084fc" stroke-width="1.8" filter="url(#softCardShadow)"/>
      <rect width="490" height="60" rx="20" fill="url(#zahaPurple2)" opacity="0.12"/>
      <line x1="0" y1="60" x2="490" y2="60" stroke="#e9d5ff" stroke-width="1.2"/>

      <text x="245" y="38" fill="#3b0764" class="sans" font-size="17" font-weight="900" letter-spacing="1" text-anchor="middle">HOSTEL SRMS</text>

      <!-- Icon & Title -->
      <g transform="translate(245, 120)">
        <use href="#icon-hostel-srms" x="-32" y="-45"/>
        <text x="0" y="42" fill="#1e1b4b" class="sans" font-size="18" font-weight="900" text-anchor="middle">Student Residence Management</text>
        <text x="0" y="64" fill="#7c3aed" class="mono" font-size="11" font-weight="700" text-anchor="middle">6 Portals • Leases &amp; NSFAS Billing</text>
      </g>

      <!-- Scannable QR -->
      <g transform="translate(155, 215)">
        <rect width="180" height="180" rx="16" fill="#faf5ff" stroke="#7c3aed" stroke-width="1.5" filter="url(#softCardShadow)"/>
        <rect x="12" y="12" width="156" height="156" rx="10" fill="#ffffff"/>
        <path d="{qr_srms}" fill="#2e1065" transform="translate(21, 21) scale(0.33)"/>
      </g>

      <!-- Button / Link -->
      <g transform="translate(245, 435)">
        <rect x="-140" y="0" width="280" height="38" rx="19" fill="#7c3aed"/>
        <text x="0" y="24" fill="#ffffff" class="mono" font-size="12" font-weight="800" text-anchor="middle">🏢 SCAN TO EXPLORE SAAS</text>
        <text x="0" y="52" fill="#64748b" class="sans" font-size="10.5" text-anchor="middle">sputnikdevs.com/products/hostel</text>
      </g>
    </g>

    <!-- CARD 3: THE UNIVERSITY HUB (X: 1105) -->
    <g transform="translate(1105, 180)">
      <rect width="490" height="500" rx="20" fill="#ffffff" stroke="#c084fc" stroke-width="1.8" filter="url(#softCardShadow)"/>
      <rect width="490" height="60" rx="20" fill="url(#zahaPurple3)" opacity="0.12"/>
      <line x1="0" y1="60" x2="490" y2="60" stroke="#e9d5ff" stroke-width="1.2"/>

      <text x="245" y="38" fill="#3b0764" class="sans" font-size="17" font-weight="900" letter-spacing="1" text-anchor="middle">THE UNIVERSITY HUB</text>

      <!-- Icon & Title -->
      <g transform="translate(245, 120)">
        <use href="#icon-unihub" x="-32" y="-45"/>
        <text x="0" y="42" fill="#1e1b4b" class="sans" font-size="18" font-weight="900" text-anchor="middle">Higher Ed Placement Platform</text>
        <text x="0" y="64" fill="#9333ea" class="mono" font-size="11" font-weight="700" text-anchor="middle">Accredited Student Residence Network</text>
      </g>

      <!-- Scannable QR -->
      <g transform="translate(155, 215)">
        <rect width="180" height="180" rx="16" fill="#faf5ff" stroke="#7c3aed" stroke-width="1.5" filter="url(#softCardShadow)"/>
        <rect x="12" y="12" width="156" height="156" rx="10" fill="#ffffff"/>
        <path d="{qr_unihub}" fill="#2e1065" transform="translate(21, 21) scale(0.33)"/>
      </g>

      <!-- Button / Link -->
      <g transform="translate(245, 435)">
        <rect x="-140" y="0" width="280" height="38" rx="19" fill="#9333ea"/>
        <text x="0" y="24" fill="#ffffff" class="mono" font-size="12" font-weight="800" text-anchor="middle">🎓 SCAN TO VISIT HUB</text>
        <text x="0" y="52" fill="#64748b" class="sans" font-size="10.5" text-anchor="middle">sputnikdevs.com/products/unihub</text>
      </g>
    </g>

    <!-- CARD 4: SHOPNIK E-COMMERCE (X: 1635) -->
    <g transform="translate(1635, 180)">
      <rect width="490" height="500" rx="20" fill="#ffffff" stroke="#c084fc" stroke-width="1.8" filter="url(#softCardShadow)"/>
      <rect width="490" height="60" rx="20" fill="url(#zahaPurple1)" opacity="0.12"/>
      <line x1="0" y1="60" x2="490" y2="60" stroke="#e9d5ff" stroke-width="1.2"/>

      <text x="245" y="38" fill="#3b0764" class="sans" font-size="17" font-weight="900" letter-spacing="1" text-anchor="middle">SHOPNIK</text>

      <!-- Logo & Title -->
      <g transform="translate(245, 120)">
        <image href="{shopnik_logo}" x="-120" y="-42" width="240" height="60" preserveAspectRatio="xMidYMid meet"/>
        <text x="0" y="42" fill="#1e1b4b" class="sans" font-size="18" font-weight="900" text-anchor="middle">High-Velocity Cloud E-Commerce</text>
        <text x="0" y="64" fill="#059669" class="mono" font-size="11" font-weight="800" text-anchor="middle">Starts R349/Mo • Oracle Cloud SA (JHB)</text>
      </g>

      <!-- Scannable QR -->
      <g transform="translate(155, 215)">
        <rect width="180" height="180" rx="16" fill="#faf5ff" stroke="#7c3aed" stroke-width="1.5" filter="url(#softCardShadow)"/>
        <rect x="12" y="12" width="156" height="156" rx="10" fill="#ffffff"/>
        <path d="{qr_shopnik}" fill="#2e1065" transform="translate(21, 21) scale(0.33)"/>
      </g>

      <!-- Button / Link -->
      <g transform="translate(245, 435)">
        <rect x="-140" y="0" width="280" height="38" rx="19" fill="#059669"/>
        <text x="0" y="24" fill="#ffffff" class="mono" font-size="12" font-weight="800" text-anchor="middle">🛍️ SCAN TO LAUNCH STORE</text>
        <text x="0" y="52" fill="#64748b" class="sans" font-size="10.5" text-anchor="middle">sputnikdevs.com/products/ecommerce</text>
      </g>
    </g>

    <!-- CARD 5: SPUTNIK DEVS ACADEMY (X: 2165) -->
    <g transform="translate(2165, 180)">
      <rect width="490" height="500" rx="20" fill="#faf5ff" stroke="#7c3aed" stroke-width="2" filter="url(#softCardShadow)"/>
      <rect width="490" height="60" rx="20" fill="url(#zahaPurpleDark)" opacity="0.10"/>
      <line x1="0" y1="60" x2="490" y2="60" stroke="#c084fc" stroke-width="1.2"/>

      <text x="245" y="38" fill="#3b0764" class="sans" font-size="17" font-weight="900" letter-spacing="1" text-anchor="middle">SPUTNIK DEVS ACADEMY</text>

      <!-- Icon & Title -->
      <g transform="translate(245, 120)">
        <use href="#icon-academy" x="-32" y="-45"/>
        <text x="0" y="42" fill="#1e1b4b" class="sans" font-size="18" font-weight="900" text-anchor="middle">Production Software Engineering</text>
        <text x="0" y="64" fill="#ea580c" class="mono" font-size="11" font-weight="800" text-anchor="middle">19-Day Intensive &amp; 3-Month WIL Tracks</text>
      </g>

      <!-- Scannable QR -->
      <g transform="translate(155, 215)">
        <rect width="180" height="180" rx="16" fill="#ffffff" stroke="#7c3aed" stroke-width="1.5" filter="url(#softCardShadow)"/>
        <rect x="12" y="12" width="156" height="156" rx="10" fill="#ffffff"/>
        <path d="{qr_acad}" fill="#2e1065" transform="translate(21, 21) scale(0.33)"/>
      </g>

      <!-- Button / Link -->
      <g transform="translate(245, 435)">
        <rect x="-140" y="0" width="280" height="38" rx="19" fill="#ea580c"/>
        <text x="0" y="24" fill="#ffffff" class="mono" font-size="12" font-weight="800" text-anchor="middle">🚀 SCAN TO APPLY ONLINE</text>
        <text x="0" y="52" fill="#64748b" class="sans" font-size="10.5" text-anchor="middle">sputnikdevs.com/academy</text>
      </g>
    </g>

    <!-- 2C. EXECUTIVE LEADERSHIP & CORPORATE CONTACT FOOTER (Y: 715..940) -->
    <g transform="translate(45, 715)">
      <rect width="2610" height="230" rx="24" fill="#ffffff" stroke="#7c3aed" stroke-width="2" filter="url(#softCardShadow)"/>
      <rect width="2610" height="42" rx="24" fill="url(#zahaPurple1)" opacity="0.10"/>
      <line x1="0" y1="42" x2="2610" y2="42" stroke="#e9d5ff" stroke-width="1.2"/>

      <!-- Header Pill -->
      <g transform="translate(1305, 12)">
        <rect x="-190" y="0" width="380" height="24" rx="12" fill="#faf5ff" stroke="#7c3aed" stroke-width="1"/>
        <circle cx="-165" cy="12" r="4" fill="#7c3aed"/>
        <text x="0" y="16" fill="#581c87" class="mono" font-size="11" font-weight="800" letter-spacing="2" text-anchor="middle">CORPORATE HEADQUARTERS &amp; LEADERSHIP</text>
      </g>

      <!-- 3 Executive Columns -->
      <!-- Column 1: Founder & CEO (X: 50) -->
      <g transform="translate(60, 68)">
        <rect x="-10" y="-10" width="760" height="150" rx="16" fill="#faf5ff" stroke="#e9d5ff" stroke-width="1"/>
        <circle cx="20" cy="20" r="14" fill="#7c3aed"/>
        <text x="20" y="25" fill="#ffffff" class="mono" font-size="14" font-weight="900" text-anchor="middle">TM</text>
        
        <text x="48" y="18" fill="#1e1b4b" class="sans" font-size="17" font-weight="900">Takudzwa Mupanesure</text>
        <text x="48" y="38" fill="#6b21a8" class="sans" font-size="13" font-weight="700">Founder, Chief Executive Officer &amp; Lead Architect</text>
        <text x="48" y="62" fill="#0f172a" class="sans" font-size="13" font-weight="800">Sputnik Tech Group (Pty) Ltd</text>
        <text x="48" y="82" fill="#475569" class="mono" font-size="12">📍 292 Surrey Avenue, Randburg, Johannesburg, 2194</text>
        <text x="48" y="104" fill="#581c87" class="mono" font-size="12" font-weight="700">Direct: takudzwam@sputniktechgroup.com</text>
        <text x="48" y="124" fill="#475569" class="mono" font-size="12">RSA: +27 66 321 5528  |  Intl: +263 787 015 123</text>
      </g>

      <!-- Column 2: In Concurrence With (X: 860) -->
      <g transform="translate(860, 68)">
        <rect x="-10" y="-10" width="860" height="150" rx="16" fill="#ffffff" stroke="#c084fc" stroke-width="1.2" filter="url(#softCardShadow)"/>
        
        <text x="10" y="16" fill="#7c3aed" class="sans" font-size="12" font-weight="800" letter-spacing="1">IN CONCURRENCE WITH EXECUTIVE DIRECTORS:</text>
        
        <!-- Kenneth Katsande -->
        <g transform="translate(10, 36)">
          <circle cx="16" cy="16" r="14" fill="#10b981"/>
          <text x="16" y="21" fill="#ffffff" class="mono" font-size="13" font-weight="900" text-anchor="middle">KK</text>
          <text x="42" y="14" fill="#0f172a" class="sans" font-size="15" font-weight="900">Kenneth Takudzwa Katsande</text>
          <text x="42" y="32" fill="#059669" class="sans" font-size="12.5" font-weight="800">Director of Operations</text>
          <text x="42" y="48" fill="#64748b" class="sans" font-size="11">Marketplace Operations, Scale &amp; Commercial Partnerships</text>
        </g>

        <!-- Prince Nkiwane -->
        <g transform="translate(10, 96)">
          <circle cx="16" cy="16" r="14" fill="#a855f7"/>
          <text x="16" y="21" fill="#ffffff" class="mono" font-size="13" font-weight="900" text-anchor="middle">PN</text>
          <text x="42" y="14" fill="#0f172a" class="sans" font-size="15" font-weight="900">Prince Lwazi Nkiwane</text>
          <text x="42" y="32" fill="#7c3aed" class="sans" font-size="12.5" font-weight="800">Director of Growth</text>
          <text x="42" y="48" fill="#64748b" class="sans" font-size="11">Campus Talent Pipeline, Academy WIL &amp; User Acquisition</text>
        </g>
      </g>

      <!-- Column 3: Digital Portals & Inquiries (X: 1760) -->
      <g transform="translate(1760, 68)">
        <rect x="-10" y="-10" width="800" height="150" rx="16" fill="#faf5ff" stroke="#e9d5ff" stroke-width="1"/>
        <text x="10" y="16" fill="#3b0764" class="sans" font-size="14" font-weight="900" letter-spacing="1">OFFICIAL DIGITAL PORTALS &amp; SUPPORT</text>
        
        <g transform="translate(10, 36)">
          <rect width="365" height="42" rx="8" fill="#ffffff" stroke="#7c3aed" stroke-width="1"/>
          <text x="20" y="18" fill="#581c87" class="mono" font-size="11" font-weight="800">🌐 Corporate Portal:</text>
          <text x="20" y="32" fill="#0f172a" class="mono" font-size="11">sputniktechgroup.com</text>
        </g>

        <g transform="translate(400, 36)">
          <rect width="370" height="42" rx="8" fill="#ffffff" stroke="#7c3aed" stroke-width="1"/>
          <text x="20" y="18" fill="#581c87" class="mono" font-size="11" font-weight="800">💻 Studio &amp; Academy:</text>
          <text x="20" y="32" fill="#0f172a" class="mono" font-size="11">sputnikdevs.com</text>
        </g>

        <g transform="translate(10, 90)">
          <rect width="760" height="38" rx="8" fill="#f5f3ff" stroke="#c084fc" stroke-width="1"/>
          <text x="380" y="24" fill="#4c1d95" class="mono" font-size="11.5" font-weight="800" text-anchor="middle">📧 Direct Showcase Inquiries: info@sputniktechgroup.com</text>
        </g>
      </g>

    </g>

  </g>


  <!-- =================================================================== -->
  <!-- ZONE 3: LEFT SIDE SKIRT (X: 60..520, Y: 1145..1855)                 -->
  <!-- Facing left aisle foot traffic                                      -->
  <!-- =================================================================== -->
  <g transform="translate(60, 1145)">
    <rect width="460" height="710" rx="24" fill="#ffffff" stroke="#7c3aed" stroke-width="2" filter="url(#softCardShadow)"/>
    <rect width="460" height="56" rx="24" fill="url(#zahaPurple1)" opacity="0.12"/>
    <line x1="0" y1="56" x2="460" y2="56" stroke="#7c3aed" stroke-width="1.2"/>

    <text x="230" y="36" fill="#3b0764" class="sans" font-size="16" font-weight="900" letter-spacing="1" text-anchor="middle">SPUTNIK TECH GROUP</text>

    <!-- Content -->
    <g transform="translate(30, 80)">
      <image href="{tradeybay_primary_logo}" x="50" y="0" width="300" height="75" preserveAspectRatio="xMidYMid meet"/>

      <text x="200" y="105" fill="#1e1b4b" class="sans" font-size="20" font-weight="900" text-anchor="middle">Campus Super App</text>
      <text x="200" y="128" fill="#7c3aed" class="mono" font-size="12" font-weight="800" text-anchor="middle">VERSION v2.0.4+31</text>

      <!-- Scannable QR -->
      <g transform="translate(90, 150)">
        <rect width="220" height="220" rx="18" fill="#faf5ff" stroke="#7c3aed" stroke-width="1.8" filter="url(#softCardShadow)"/>
        <g transform="translate(20, 20)">
          <rect width="180" height="180" rx="12" fill="#ffffff"/>
          <path d="{qr_tb}" fill="#2e1065" transform="translate(13, 13) scale(0.38)"/>
        </g>
      </g>

      <text x="200" y="405" fill="#581c87" class="mono" font-size="13" font-weight="800" text-anchor="middle">📱 POINT CAMERA TO INSTALL</text>
      <text x="200" y="430" fill="#475569" class="sans" font-size="12" font-weight="600" text-anchor="middle">Google Play &amp; Apple App Store</text>

      <!-- 3 Clean Brand Badges -->
      <g transform="translate(20, 455)">
        <rect width="360" height="34" rx="8" fill="#faf5ff" stroke="#e9d5ff" stroke-width="1"/>
        <text x="180" y="22" fill="#581c87" class="sans" font-size="12" font-weight="700" text-anchor="middle">🏷️ 0% Commission for Students</text>

        <rect y="44" width="360" height="34" rx="8" fill="#faf5ff" stroke="#e9d5ff" stroke-width="1"/>
        <text x="180" y="66" fill="#581c87" class="sans" font-size="12" font-weight="700" text-anchor="middle">🏠 Verified Student Housing</text>

        <rect y="88" width="360" height="34" rx="8" fill="#faf5ff" stroke="#e9d5ff" stroke-width="1"/>
        <text x="180" y="110" fill="#581c87" class="sans" font-size="12" font-weight="700" text-anchor="middle">🔒 100% POPIA Compliant</text>
      </g>

      <g transform="translate(20, 595)">
        <rect width="360" height="34" rx="8" fill="#f5f3ff" stroke="#7c3aed" stroke-width="1"/>
        <text x="180" y="22" fill="#4c1d95" class="mono" font-size="11" font-weight="800" text-anchor="middle">info@sputniktechgroup.com</text>
      </g>
    </g>
  </g>


  <!-- =================================================================== -->
  <!-- ZONE 4: RIGHT SIDE SKIRT (X: 2480..2940, Y: 1145..1855)              -->
  <!-- Facing right aisle foot traffic                                     -->
  <!-- =================================================================== -->
  <g transform="translate(2480, 1145)">
    <rect width="460" height="710" rx="24" fill="#ffffff" stroke="#7c3aed" stroke-width="2" filter="url(#softCardShadow)"/>
    <rect width="460" height="56" rx="24" fill="url(#zahaPurple3)" opacity="0.12"/>
    <line x1="0" y1="56" x2="460" y2="56" stroke="#7c3aed" stroke-width="1.2"/>

    <text x="230" y="36" fill="#3b0764" class="sans" font-size="16" font-weight="900" letter-spacing="1" text-anchor="middle">SPUTNIK DEVS STUDIO</text>

    <!-- Content -->
    <g transform="translate(30, 80)">
      <image href="{sputnik_devs_logo}" x="40" y="0" width="320" height="75" preserveAspectRatio="xMidYMid meet"/>

      <text x="200" y="105" fill="#1e1b4b" class="sans" font-size="19" font-weight="900" text-anchor="middle">Enterprise Cloud &amp; WIL</text>
      <text x="200" y="128" fill="#7c3aed" class="mono" font-size="12" font-weight="800" text-anchor="middle">ACADEMY LEARNERSHIP</text>

      <!-- Scannable QR -->
      <g transform="translate(90, 150)">
        <rect width="220" height="220" rx="18" fill="#faf5ff" stroke="#7c3aed" stroke-width="1.8" filter="url(#softCardShadow)"/>
        <g transform="translate(20, 20)">
          <rect width="180" height="180" rx="12" fill="#ffffff"/>
          <path d="{qr_acad}" fill="#2e1065" transform="translate(13, 13) scale(0.38)"/>
        </g>
      </g>

      <text x="200" y="405" fill="#581c87" class="mono" font-size="13" font-weight="800" text-anchor="middle">🚀 POINT CAMERA TO APPLY</text>
      <text x="200" y="430" fill="#475569" class="sans" font-size="12" font-weight="600" text-anchor="middle">CS Graduates &amp; Tech Talent</text>

      <!-- 3 Clean Brand Badges -->
      <g transform="translate(20, 455)">
        <rect width="360" height="34" rx="8" fill="#faf5ff" stroke="#e9d5ff" stroke-width="1"/>
        <text x="180" y="22" fill="#581c87" class="sans" font-size="12" font-weight="700" text-anchor="middle">🏢 Student Residence Management</text>

        <rect y="44" width="360" height="34" rx="8" fill="#faf5ff" stroke="#e9d5ff" stroke-width="1"/>
        <text x="180" y="66" fill="#581c87" class="sans" font-size="12" font-weight="700" text-anchor="middle">🛍️ Shopnik SaaS (From R349/mo)</text>

        <rect y="88" width="360" height="34" rx="8" fill="#faf5ff" stroke="#e9d5ff" stroke-width="1"/>
        <text x="180" y="110" fill="#581c87" class="sans" font-size="12" font-weight="700" text-anchor="middle">🤖 Autonomous AI Workflows</text>
      </g>

      <g transform="translate(20, 595)">
        <rect width="360" height="34" rx="8" fill="#f5f3ff" stroke="#7c3aed" stroke-width="1"/>
        <text x="180" y="22" fill="#4c1d95" class="mono" font-size="11" font-weight="800" text-anchor="middle">sputnikdevs.com/academy</text>
      </g>
    </g>
  </g>


  <!-- =================================================================== -->
  <!-- ZONE 5: REAR OPERATOR DRAPE (X: 600..2400, Y: 150..1050)            -->
  <!-- Inverted 180° so it faces the staff standing behind the table       -->
  <!-- =================================================================== -->
  <g transform="translate(1500, 600) rotate(180)">
    <rect x="-850" y="-350" width="1700" height="700" rx="32" fill="#ffffff" stroke="#7c3aed" stroke-width="2" filter="url(#softCardShadow)"/>
    <rect x="-850" y="-350" width="1700" height="700" rx="32" fill="url(#cardGradSoftPurple)"/>

    <!-- Inverted Branding Header -->
    <g transform="translate(0, -220)">
      <rect x="-180" y="-18" width="360" height="36" rx="18" fill="#faf5ff" stroke="#7c3aed" stroke-width="1.2"/>
      <circle cx="-150" cy="0" r="5" fill="#7c3aed"/>
      <text x="0" y="6" fill="#581c87" class="mono" font-size="12" font-weight="800" letter-spacing="2" text-anchor="middle">SOUTH AFRICA TECH SHOWCASE</text>

      <text x="0" y="55" fill="#1e1b4b" class="sans" font-size="30" font-weight="900" letter-spacing="1" text-anchor="middle">SPUTNIK TECH GROUP &amp; SPUTNIK DEVS STUDIO</text>
      <text x="0" y="85" fill="#6b21a8" class="sans" font-size="15" font-weight="700" text-anchor="middle">292 Surrey Avenue, Randburg, Johannesburg, 2194 • South Africa</text>
    </g>

    <!-- Side-by-Side Corporate Logos -->
    <g transform="translate(-520, -50)">
      <image href="{sputnik_tech_logo}" x="0" y="0" width="320" height="100" preserveAspectRatio="xMidYMid meet"/>
    </g>
    <g transform="translate(200, -50)">
      <image href="{sputnik_devs_logo}" x="0" y="0" width="320" height="100" preserveAspectRatio="xMidYMid meet"/>
    </g>

    <!-- Executive Leadership Credit -->
    <g transform="translate(0, 160)">
      <rect x="-600" y="-35" width="1200" height="110" rx="16" fill="#ffffff" stroke="#7c3aed" stroke-width="1.2" filter="url(#softCardShadow)"/>
      <text x="0" y="-2" fill="#3b0764" class="sans" font-size="16" font-weight="900" text-anchor="middle">Takudzwa Mupanesure — Founder, Chief Executive Officer &amp; Lead Architect</text>
      <text x="0" y="24" fill="#6b21a8" class="sans" font-size="13" font-weight="700" text-anchor="middle">In Concurrence with: Kenneth Takudzwa Katsande (Director of Operations) &amp; Prince Lwazi Nkiwane (Director of Growth)</text>
      <text x="0" y="50" fill="#475569" class="mono" font-size="11.5" text-anchor="middle">Direct: takudzwam@sputniktechgroup.com | +27 66 321 5528 | +263 787 015 123</text>
    </g>
  </g>

</svg>"""

    out_path = os.path.join(REPO_ROOT, "designs", "table-cloth-3x3m", "tablecloth.svg")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(svg)

    print(f"✅ Generated decluttered tablecloth SVG at {out_path} ({len(svg)/1024:.1f} KB)")

if __name__ == "__main__":
    build_tablecloth_svg()
