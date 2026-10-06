#!/usr/bin/env python3
"""
Generate the high-resolution, front-only vector Staff Showcase T-Shirts
for Kenneth Takudzwa Katsande and Prince Lwazi Nkiwane at the South Africa Tech Showcase.

Requirements:
- Front-only print (no back prints).
- HIGH VISIBILITY: 100% garment-focused portrait presentation (1000 x 1350)
  on a bright, clean, premium studio backdrop so the noir black cotton tee pops dramatically!
- Kenneth Takudzwa Katsande: Director of Operations (Commerce & Ecosystem scale, Tradey Bay scannable QR on front).
- Prince Lwazi Nkiwane: Director of Growth (Talent pipeline & campus growth, Academy WIL scannable QR on front).
- Official branding: Sputnik Tech Group & Sputnik Devs Studio.
- Zaha Hadid parametric fluid wave accents.
- Output:
  - designs/shirts/shirt-kenneth.svg
  - designs/shirts/shirt-prince.svg
  - designs/shirts/shirt-print.html
  - designs/shirts/shirts-dtf.pdf
"""

import os
import xml.etree.ElementTree as ET

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

def get_svg_path_data(rel_path):
    abs_path = os.path.join(REPO_ROOT, rel_path)
    tree = ET.parse(abs_path)
    root = tree.getroot()
    for elem in root.iter():
        if elem.tag.endswith("path"):
            return elem.attrib.get("d")
    return None

def build_shirt_svg(name, full_name, title, focus_tag, chips, qr_type, qr_badge_title, qr_badge_sub, qr_action, qr_footer):
    qr_tb = get_svg_path_data("assets/qr/qr-tradeybay-playstore.svg")
    qr_acad = get_svg_path_data("assets/qr/qr-academy-apply.svg")
    qr_path = qr_tb if qr_type == "tradeybay" else qr_acad

    is_kenneth = (name == "kenneth")
    accent_color = "#10b981" if is_kenneth else "#a855f7"
    accent_light = "#34d399" if is_kenneth else "#c084fc"
    accent_dark = "#065f46" if is_kenneth else "#581c87"
    badge_bg = "#064e3b" if is_kenneth else "#3b0764"
    role_initials = "KK" if is_kenneth else "PN"

    chip1, chip2, chip3 = chips

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 1000 1350" width="1000" height="1350">
  <defs>
    <!-- Studio Lighting Background Gradients -->
    <radialGradient id="studioLighting" cx="50%" cy="40%" r="70%">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="45%" stop-color="#f8fafc"/>
      <stop offset="80%" stop-color="#f1f5f9"/>
      <stop offset="100%" stop-color="#e2e8f0"/>
    </radialGradient>

    <!-- Premium Noir Combed Cotton Fabric Gradients -->
    <linearGradient id="cottonFabric" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1c1d22"/>
      <stop offset="25%" stop-color="#121316"/>
      <stop offset="60%" stop-color="#18191f"/>
      <stop offset="100%" stop-color="#0c0d10"/>
    </linearGradient>

    <!-- Collar & Hem Ribbing -->
    <linearGradient id="collarRibbing" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#2a2b33"/>
      <stop offset="50%" stop-color="#1a1b20"/>
      <stop offset="100%" stop-color="#121316"/>
    </linearGradient>

    <!-- Zaha Hadid Purple Waves -->
    <linearGradient id="zahaShirtPurple" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#7c3aed"/>
      <stop offset="50%" stop-color="#a855f7"/>
      <stop offset="100%" stop-color="#c084fc"/>
    </linearGradient>

    <linearGradient id="neonAccentGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="{accent_color}"/>
      <stop offset="100%" stop-color="{accent_light}"/>
    </linearGradient>

    <!-- Studio Shadows -->
    <filter id="studioDropShadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="25" stdDeviation="30" flood-color="#0f172a" flood-opacity="0.25"/>
      <feDropShadow dx="0" dy="8" stdDeviation="12" flood-color="#0f172a" flood-opacity="0.15"/>
    </filter>

    <filter id="badgeGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="4" stdDeviation="8" flood-color="{accent_color}" flood-opacity="0.35"/>
    </filter>

    <filter id="qrCardShadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="8" stdDeviation="14" flood-color="#000000" flood-opacity="0.5"/>
    </filter>

    <!-- Studio Floor Vignette -->
    <radialGradient id="floorShadow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#94a3b8" stop-opacity="0.35"/>
      <stop offset="60%" stop-color="#cbd5e1" stop-opacity="0.15"/>
      <stop offset="100%" stop-color="#f1f5f9" stop-opacity="0"/>
    </radialGradient>
  </defs>

  <style>
    .sans {{ font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; }}
    .mono {{ font-family: 'JetBrains Mono', 'Fira Code', 'Courier New', monospace; }}
  </style>

  <!-- =================================================================== -->
  <!-- 1. STUDIO PRESENTATION BACKDROP                                    -->
  <!-- Clean, bright, photorealistic Apple/Nike style studio presentation  -->
  <!-- =================================================================== -->
  <rect width="1000" height="1350" rx="20" fill="url(#studioLighting)"/>
  <rect width="1000" height="1350" rx="20" fill="none" stroke="#cbd5e1" stroke-width="2"/>

  <!-- Studio Floor Ground Shadow -->
  <ellipse cx="500" cy="1255" rx="360" ry="38" fill="url(#floorShadow)"/>

  <!-- Presentation Header Banner -->
  <g transform="translate(50, 36)">
    <!-- Pill -->
    <rect width="360" height="30" rx="15" fill="#ffffff" stroke="#7c3aed" stroke-width="1.2"/>
    <circle cx="18" cy="15" r="5" fill="#7c3aed"/>
    <text x="32" y="20" fill="#581c87" class="mono" font-size="11" font-weight="900" letter-spacing="1.5">SOUTH AFRICA TECH SHOWCASE</text>

    <!-- Title & Staff Role -->
    <text x="0" y="58" fill="#0f172a" class="sans" font-size="24" font-weight="900">
      {full_name.upper()}
    </text>
    <text x="0" y="78" fill="#581c87" class="mono" font-size="12" font-weight="800">
      {title.upper()} • SPUTNIK TECH GROUP &amp; SPUTNIK DEVS STUDIO
    </text>

    <!-- Right-aligned Spec Badge -->
    <g transform="translate(680, 0)">
      <rect width="220" height="42" rx="10" fill="#ffffff" stroke="#94a3b8" stroke-width="1"/>
      <text x="110" y="18" fill="#475569" class="mono" font-size="10" font-weight="700" text-anchor="middle">GARMENT SPECIFICATION</text>
      <text x="110" y="32" fill="#0f172a" class="sans" font-size="11" font-weight="800" text-anchor="middle">Front-Only DTF Print • 100% Cotton</text>
    </g>
  </g>


  <!-- =================================================================== -->
  <!-- 2. HIGH-RESOLUTION T-SHIRT GARMENT SILHOUETTE (CENTER STAGE)       -->
  <!-- Perfectly proportioned crewneck tee filling 85% of viewport         -->
  <!-- =================================================================== -->
  <g transform="translate(500, 140)">

    <!-- T-Shirt Fabric Body with Studio Drop Shadow -->
    <!-- Center coordinate is at 0 (X: -420 to +420, Y: 0 to 1080) -->
    <path d="M -150 25 
             Q 0 95 150 25 
             L 300 95 
             L 420 250 
             L 340 310 
             L 285 245 
             L 285 1030 
             Q 285 1060 255 1060 
             L -255 1060 
             Q -285 1060 -285 1030 
             L -285 245 
             L -340 310 
             L -420 250 
             L -300 95 Z" 
          fill="url(#cottonFabric)" 
          stroke="#26272f" 
          stroke-width="3" 
          filter="url(#studioDropShadow)"/>

    <!-- Subtle Fabric Crease Shadows & Form Shading -->
    <!-- Left Flank Shading -->
    <path d="M -285 245 L -285 1030 Q -285 1060 -255 1060 L -230 1060 L -260 260 Z" fill="#0a0a0d" opacity="0.4"/>
    <!-- Right Flank Shading -->
    <path d="M 285 245 L 285 1030 Q 285 1060 255 1060 L 230 1060 L 260 260 Z" fill="#0a0a0d" opacity="0.4"/>
    <!-- Sleeve Seam Lines -->
    <path d="M -300 95 L -285 245" stroke="#2d2e38" stroke-width="2.5"/>
    <path d="M 300 95 L 285 245" stroke="#2d2e38" stroke-width="2.5"/>

    <!-- Bottom Hem Double Stitch Line -->
    <line x1="-275" y1="1040" x2="275" y2="1040" stroke="#2a2b34" stroke-width="1.8" stroke-dasharray="6,4"/>
    <line x1="-275" y1="1046" x2="275" y2="1046" stroke="#22232a" stroke-width="1.8" stroke-dasharray="6,4"/>

    <!-- Sleeve Cuffs Stitch Lines -->
    <line x1="-405" y1="260" x2="-330" y2="318" stroke="#2a2b34" stroke-width="1.5"/>
    <line x1="405" y1="260" x2="330" y2="318" stroke="#2a2b34" stroke-width="1.5"/>

    <!-- Ribbed Crewneck Collar -->
    <path d="M -150 25 Q 0 105 150 25 Q 0 75 -150 25 Z" fill="url(#collarRibbing)" stroke="#383944" stroke-width="2"/>
    <path d="M -145 28 Q 0 100 145 28" fill="none" stroke="#262730" stroke-width="2.5"/>

    <!-- Inner Neck Label Tape -->
    <path d="M -110 32 Q 0 65 110 32 Q 0 45 -110 32 Z" fill="#0d0e12"/>
    <text x="0" y="46" fill="#64748b" class="mono" font-size="8" font-weight="700" letter-spacing="1" text-anchor="middle">SPUTNIK TECH • 100% COMBED COTTON</text>

    <!-- Shoulder Accents -->
    <path d="M -150 25 L -300 95" stroke="#33343f" stroke-width="2"/>
    <path d="M 150 25 L 300 95" stroke="#33343f" stroke-width="2"/>


    <!-- ================================================================= -->
    <!-- 3. FRONT PRINT GRAPHICS (THE ACTUAL HIGH-CONTRAST DTF PRINT)      -->
    <!-- All elements positioned with generous spacing & 100% legibility   -->
    <!-- ================================================================= -->

    <!-- 3A. LEFT CHEST: OFFICIAL CORPORATE BRAND CREST (X: -190, Y: 180) -->
    <g transform="translate(-150, 180)">
      <rect x="-95" y="-35" width="190" height="70" rx="14" fill="#0f1118" stroke="#7c3aed" stroke-width="1.5" filter="url(#badgeGlow)"/>
      <circle cx="-65" cy="0" r="18" fill="#1e1338" stroke="#a855f7" stroke-width="1.5"/>
      <!-- Sputnik Rocket Vector -->
      <path d="M -65 -10 L -59 2 L -63 0 L -63 8 L -67 8 L -67 0 L -71 2 Z" fill="#ffffff"/>
      <polygon points="-65,8 -62,13 -68,13" fill="#f59e0b"/>

      <text x="-40" y="-8" fill="#ffffff" class="sans" font-size="12" font-weight="900" letter-spacing="1">SPUTNIK TECH</text>
      <text x="-40" y="8" fill="{accent_light}" class="mono" font-size="9" font-weight="800">DEVS STUDIO</text>
      <text x="-40" y="22" fill="#94a3b8" class="sans" font-size="8" font-weight="600">VIP EXHIBITION CREW</text>
    </g>

    <!-- 3B. RIGHT CHEST: EXECUTIVE VIP BADGE (X: +150, Y: 180) -->
    <g transform="translate(150, 180)">
      <rect x="-95" y="-35" width="190" height="70" rx="14" fill="#0f1118" stroke="{accent_color}" stroke-width="1.8" filter="url(#badgeGlow)"/>
      <circle cx="-65" cy="0" r="18" fill="{badge_bg}" stroke="{accent_light}" stroke-width="1.5"/>
      <text x="-65" y="5" fill="#ffffff" class="mono" font-size="13" font-weight="900" text-anchor="middle">{role_initials}</text>

      <text x="-40" y="-10" fill="#ffffff" class="sans" font-size="12" font-weight="900">{full_name.split()[0].upper()}</text>
      <rect x="-40" y="-3" width="125" height="18" rx="4" fill="{badge_bg}"/>
      <text x="22" y="10" fill="{accent_light}" class="mono" font-size="8" font-weight="800" text-anchor="middle">{title.upper()}</text>
      <text x="-40" y="24" fill="#94a3b8" class="mono" font-size="7.5" font-weight="600">{focus_tag}</text>
    </g>

    <!-- 3C. CENTER FRONT TORSO: HIGH-CONTRAST SCANNABLE LAUNCHPAD CARD    -->
    <!-- Center coordinate (0, 560), Width 440, Height 530                 -->
    <!-- Extremely crisp white QR container on deep backdrop               -->
    <!-- ================================================================= -->
    <g transform="translate(0, 560)">

      <!-- Torso Card Outer Glow & Silhouette -->
      <rect x="-225" y="-270" width="450" height="520" rx="28" fill="#0d0e14" stroke="#7c3aed" stroke-width="2.2" filter="url(#qrCardShadow)"/>
      <rect x="-225" y="-270" width="450" height="520" rx="28" fill="none" stroke="{accent_color}" stroke-width="1" stroke-opacity="0.4"/>

      <!-- Card Top Category Pill -->
      <g transform="translate(0, -240)">
        <rect x="-140" y="-12" width="280" height="24" rx="12" fill="#18132b" stroke="#a855f7" stroke-width="1"/>
        <circle cx="-120" cy="0" r="4" fill="{accent_color}"/>
        <text x="0" y="4" fill="#ffffff" class="mono" font-size="9.5" font-weight="800" letter-spacing="1.5" text-anchor="middle">{qr_badge_title}</text>
      </g>

      <!-- Main Product Headline -->
      <text x="0" y="-195" fill="#ffffff" class="sans" font-size="28" font-weight="900" letter-spacing="1" text-anchor="middle">
        {"Tradey" if is_kenneth else "Sputnik Devs "}<tspan fill="{accent_light}">{"Bay" if is_kenneth else "Academy"}</tspan>
      </text>
      <text x="0" y="-170" fill="#cbd5e1" class="sans" font-size="12" font-weight="700" text-anchor="middle">
        {qr_badge_sub}
      </text>

      <!-- 3 Feature Pills -->
      <g transform="translate(0, -145)">
        <rect x="-195" y="-10" width="120" height="22" rx="6" fill="#1c1d27"/>
        <text x="-135" y="5" fill="{accent_light}" class="mono" font-size="8.5" font-weight="800" text-anchor="middle">{chip1}</text>

        <rect x="-65" y="-10" width="130" height="22" rx="6" fill="#1c1d27"/>
        <text x="0" y="5" fill="#ffffff" class="mono" font-size="8.5" font-weight="800" text-anchor="middle">{chip2}</text>

        <rect x="75" y="-10" width="120" height="22" rx="6" fill="#1c1d27"/>
        <text x="135" y="5" fill="{accent_light}" class="mono" font-size="8.5" font-weight="800" text-anchor="middle">{chip3}</text>
      </g>

      <!-- THE MASSIVE ULTRA-CRISP HIGH-CONTRAST SCANNABLE QR CODE CONTAINER -->
      <!-- 250 x 250 mm pure white card with deep purple vector QR modules    -->
      <!-- Scannable from 2.5 meters away directly off staff's chest!         -->
      <g transform="translate(0, 15)">
        <rect x="-120" y="-120" width="240" height="240" rx="20" fill="#ffffff" stroke="#c084fc" stroke-width="2" filter="url(#badgeGlow)"/>
        <path d="{qr_path}" fill="#2e1065" transform="translate(-95, -95) scale(0.42)"/>
      </g>

      <!-- Direct Scan Call-To-Action Pill Button -->
      <g transform="translate(0, 175)">
        <rect x="-170" y="-18" width="340" height="36" rx="18" fill="url(#neonAccentGrad)"/>
        <text x="0" y="6" fill="#040711" class="mono" font-size="12" font-weight="900" letter-spacing="1" text-anchor="middle">
          {qr_action}
        </text>
      </g>

      <!-- Official Sub-Footer -->
      <text x="0" y="222" fill="#94a3b8" class="sans" font-size="10.5" font-weight="600" text-anchor="middle">
        {qr_footer}
      </text>
    </g>

    <!-- 3D. ZAHA HADID FLUID ARCHITECTURAL HEM ACCENTS (Y: 960..1050) -->
    <path d="M -260 970 C -150 940 -50 1020 50 980 C 150 940 220 1010 260 980 L 260 1030 C 200 1045 100 1020 0 1040 C -100 1060 -180 1030 -260 1035 Z" 
          fill="url(#zahaShirtPurple)" opacity="0.4"/>
    <path d="M -255 985 C -145 955 -45 1035 55 995 C 155 955 225 1025 255 995" 
          fill="none" stroke="{accent_light}" stroke-width="2" stroke-opacity="0.6"/>

    <!-- Subtle Tech Specs on Lower Hem -->
    <g transform="translate(0, 1020)">
      <text x="0" y="0" fill="#64748b" class="mono" font-size="9" font-weight="600" text-anchor="middle">
        SPUTNIK TECH GROUP (PTY) LTD • 292 SURREY AVE, RANDBURG, JHB • RSA HOSTED
      </text>
    </g>

  </g>

</svg>"""
    return svg

def build_shirt_print_html():
    """Generates the DTF Production Sheet HTML for direct heat press printing."""
    qr_tb = get_svg_path_data("assets/qr/qr-tradeybay-playstore.svg")
    qr_acad = get_svg_path_data("assets/qr/qr-academy-apply.svg")

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Sputnik Showcase — Staff T-Shirts Front-Only DTF Print Sheets</title>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800;900&family=JetBrains+Mono:wght@600;700;800&display=swap');

    @page {{
      size: A3 landscape;
      margin: 10mm;
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    body {{
      background: #0f172a;
      color: #ffffff;
      font-family: 'Inter', sans-serif;
      padding: 20px;
    }}

    .page-sheet {{
      background: #ffffff;
      color: #0f172a;
      width: 400mm;
      min-height: 275mm;
      margin: 0 auto 30px auto;
      padding: 15mm;
      box-shadow: 0 10px 30px rgba(0,0,0,0.4);
      border-radius: 8px;
      page-break-after: always;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }}

    .sheet-header {{
      border-bottom: 2px solid #7c3aed;
      padding-bottom: 10px;
      margin-bottom: 15px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}

    .sheet-title {{
      font-size: 20px;
      font-weight: 900;
      color: #3b0764;
    }}

    .sheet-sub {{
      font-family: 'JetBrains Mono', monospace;
      font-size: 11px;
      color: #6b21a8;
      font-weight: 700;
    }}

    .print-grid {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 20px;
      flex: 1;
    }}

    .cut-block {{
      border: 1.5px dashed #7c3aed;
      border-radius: 12px;
      padding: 15px;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      background: #faf5ff;
      position: relative;
    }}

    .cut-label {{
      position: absolute;
      top: 8px;
      left: 12px;
      font-family: 'JetBrains Mono', monospace;
      font-size: 10px;
      font-weight: 800;
      color: #7c3aed;
      background: #ffffff;
      padding: 2px 8px;
      border-radius: 4px;
      border: 1px solid #c084fc;
    }}

    .qr-box {{
      background: #ffffff;
      padding: 12px;
      border-radius: 12px;
      box-shadow: 0 4px 12px rgba(0,0,0,0.1);
      border: 1px solid #e9d5ff;
      margin: 10px 0;
    }}

    .badge-preview {{
      background: #0f172a;
      color: #ffffff;
      padding: 10px 20px;
      border-radius: 10px;
      margin: 8px 0;
      text-align: center;
    }}
  </style>
</head>
<body>

  <!-- SHEET 1: KENNETH TAKUDZWA KATSANDE (DIRECTOR OF OPERATIONS) -->
  <div class="page-sheet">
    <div class="sheet-header">
      <div>
        <div class="sheet-title">STAFF SHIRT 1 // KENNETH TAKUDZWA KATSANDE</div>
        <div class="sheet-sub">DIRECTOR OF OPERATIONS • FRONT-ONLY DTF PRODUCTION GANG SHEET</div>
      </div>
      <div style="text-align: right; font-family: 'JetBrains Mono', monospace; font-size: 11px; color: #10b981; font-weight: 800;">
        NOIR BLACK PREMIUM TEE (M/L/XL)<br>
        HEAT PRESS: 160°C • 15 SECONDS
      </div>
    </div>

    <div class="print-grid">
      <!-- Left Chest Badge -->
      <div class="cut-block">
        <div class="cut-label">PIECE A: LEFT CHEST BRAND CREST (100mm x 45mm)</div>
        <div class="badge-preview" style="border: 1.5px solid #7c3aed; width: 260px;">
          <div style="font-weight: 900; font-size: 14px; letter-spacing: 1px;">SPUTNIK TECH GROUP</div>
          <div style="color: #c084fc; font-family: 'JetBrains Mono', monospace; font-size: 10px; font-weight: 700;">SPUTNIK DEVS STUDIO</div>
          <div style="color: #94a3b8; font-size: 9px; margin-top: 2px;">VIP EXHIBITION CREW</div>
        </div>
      </div>

      <!-- Right Chest Executive Badge -->
      <div class="cut-block">
        <div class="cut-label">PIECE B: RIGHT CHEST EXECUTIVE BADGE (100mm x 45mm)</div>
        <div class="badge-preview" style="border: 1.5px solid #10b981; width: 260px;">
          <div style="font-weight: 900; font-size: 14px; letter-spacing: 0.5px;">KENNETH KATSANDE</div>
          <div style="background: #064e3b; color: #34d399; font-family: 'JetBrains Mono', monospace; font-size: 10px; font-weight: 800; border-radius: 4px; padding: 2px 6px; margin: 3px 0;">
            DIRECTOR OF OPERATIONS
          </div>
          <div style="color: #94a3b8; font-size: 8.5px;">Ecosystem Scale &amp; Ops</div>
        </div>
      </div>

      <!-- Center Torso QR Placard -->
      <div class="cut-block" style="grid-column: span 2; padding: 25px;">
        <div class="cut-label">PIECE C: FRONT TORSO LAUNCHPAD &amp; SCANNABLE QR (260mm x 320mm)</div>
        <div style="background: #0f172a; border: 2px solid #7c3aed; border-radius: 16px; padding: 20px 40px; text-align: center; color: #ffffff; width: 440px;">
          <div style="font-family: 'JetBrains Mono', monospace; font-size: 10px; font-weight: 800; color: #c084fc; letter-spacing: 1.5px;">
            CAMPUS COMMERCE SUPER APP
          </div>
          <div style="font-size: 24px; font-weight: 900; margin: 4px 0;">
            Tradey<span style="color: #34d399;">Bay</span>
          </div>
          <div style="font-size: 11px; color: #cbd5e1; margin-bottom: 10px;">
            0% Commission • Verified Student Network
          </div>

          <div class="qr-box" style="display: inline-block;">
            <svg width="180" height="180" viewBox="0 0 100 100">
              <path d="{qr_tb}" fill="#2e1065" transform="translate(6, 6) scale(0.35)"/>
            </svg>
          </div>

          <div style="background: #10b981; color: #040711; font-family: 'JetBrains Mono', monospace; font-size: 11px; font-weight: 900; border-radius: 20px; padding: 6px 16px; margin-top: 8px;">
            📱 SCAN TO INSTALL APP
          </div>
          <div style="font-size: 9.5px; color: #94a3b8; margin-top: 6px;">
            Google Play &amp; Apple App Store • In-Country Cloud Hosted
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- SHEET 2: PRINCE LWAZI NKIWANE (DIRECTOR OF GROWTH) -->
  <div class="page-sheet">
    <div class="sheet-header">
      <div>
        <div class="sheet-title">STAFF SHIRT 2 // PRINCE LWAZI NKIWANE</div>
        <div class="sheet-sub">DIRECTOR OF GROWTH • FRONT-ONLY DTF PRODUCTION GANG SHEET</div>
      </div>
      <div style="text-align: right; font-family: 'JetBrains Mono', monospace; font-size: 11px; color: #a855f7; font-weight: 800;">
        NOIR BLACK PREMIUM TEE (M/L/XL)<br>
        HEAT PRESS: 160°C • 15 SECONDS
      </div>
    </div>

    <div class="print-grid">
      <!-- Left Chest Badge -->
      <div class="cut-block">
        <div class="cut-label">PIECE A: LEFT CHEST BRAND CREST (100mm x 45mm)</div>
        <div class="badge-preview" style="border: 1.5px solid #7c3aed; width: 260px;">
          <div style="font-weight: 900; font-size: 14px; letter-spacing: 1px;">SPUTNIK TECH GROUP</div>
          <div style="color: #c084fc; font-family: 'JetBrains Mono', monospace; font-size: 10px; font-weight: 700;">SPUTNIK DEVS STUDIO</div>
          <div style="color: #94a3b8; font-size: 9px; margin-top: 2px;">VIP EXHIBITION CREW</div>
        </div>
      </div>

      <!-- Right Chest Executive Badge -->
      <div class="cut-block">
        <div class="cut-label">PIECE B: RIGHT CHEST EXECUTIVE BADGE (100mm x 45mm)</div>
        <div class="badge-preview" style="border: 1.5px solid #a855f7; width: 260px;">
          <div style="font-weight: 900; font-size: 14px; letter-spacing: 0.5px;">PRINCE LWAZI NKIWANE</div>
          <div style="background: #3b0764; color: #c084fc; font-family: 'JetBrains Mono', monospace; font-size: 10px; font-weight: 800; border-radius: 4px; padding: 2px 6px; margin: 3px 0;">
            DIRECTOR OF GROWTH
          </div>
          <div style="color: #94a3b8; font-size: 8.5px;">Campus Talent &amp; Devs Academy</div>
        </div>
      </div>

      <!-- Center Torso QR Placard -->
      <div class="cut-block" style="grid-column: span 2; padding: 25px;">
        <div class="cut-label">PIECE C: FRONT TORSO LAUNCHPAD &amp; SCANNABLE QR (260mm x 320mm)</div>
        <div style="background: #0f172a; border: 2px solid #7c3aed; border-radius: 16px; padding: 20px 40px; text-align: center; color: #ffffff; width: 440px;">
          <div style="font-family: 'JetBrains Mono', monospace; font-size: 10px; font-weight: 800; color: #c084fc; letter-spacing: 1.5px;">
            PRODUCTION SOFTWARE ENGINEERING
          </div>
          <div style="font-size: 24px; font-weight: 900; margin: 4px 0;">
            Sputnik Devs <span style="color: #c084fc;">Academy</span>
          </div>
          <div style="font-size: 11px; color: #cbd5e1; margin-bottom: 10px;">
            19-Day Intensive &amp; 3-Month Accredited WIL Tracks
          </div>

          <div class="qr-box" style="display: inline-block;">
            <svg width="180" height="180" viewBox="0 0 100 100">
              <path d="{qr_acad}" fill="#2e1065" transform="translate(6, 6) scale(0.35)"/>
            </svg>
          </div>

          <div style="background: #a855f7; color: #ffffff; font-family: 'JetBrains Mono', monospace; font-size: 11px; font-weight: 900; border-radius: 20px; padding: 6px 16px; margin-top: 8px;">
            🚀 SCAN TO APPLY ONLINE
          </div>
          <div style="font-size: 9.5px; color: #94a3b8; margin-top: 6px;">
            REST/gRPC • Flutter Apps • CI/CD Cloud • AI Agents
          </div>
        </div>
      </div>
    </div>
  </div>

</body>
</html>"""
    return html

def main():
    print("Generating High-Visibility Front-Only Staff Shirts & DTF Gang Sheets...")

    # 1. Kenneth Shirt SVG (1000 x 1350 portrait mockup on light studio background)
    kenneth_svg = build_shirt_svg(
        name="kenneth",
        full_name="Kenneth Takudzwa Katsande",
        title="Director of Operations",
        focus_tag="ECOSYSTEM SCALE & OPS",
        chips=["0% COMMISSION", "VERIFIED NETWORK", "SA CLOUD HOSTED"],
        qr_type="tradeybay",
        qr_badge_title="CAMPUS COMMERCE SUPER APP",
        qr_badge_sub="Free Verified Student Marketplace • Zero Listing Fees",
        qr_action="📱 POINT CAMERA TO INSTALL",
        qr_footer="Google Play & App Store • RSA Cloud Hosted • POPIA"
    )
    k_path = os.path.join(REPO_ROOT, "designs", "shirts", "shirt-kenneth.svg")
    with open(k_path, "w", encoding="utf-8") as f:
        f.write(kenneth_svg)
    print(f"✅ Generated High-Visibility Kenneth Shirt: {k_path}")

    # 2. Prince Shirt SVG (1000 x 1350 portrait mockup on light studio background)
    prince_svg = build_shirt_svg(
        name="prince",
        full_name="Prince Lwazi Nkiwane",
        title="Director of Growth",
        focus_tag="CAMPUS TALENT & GROWTH",
        chips=["WIL ACCREDITED", "PRODUCTION CODE", "JOB PLACEMENT"],
        qr_type="academy",
        qr_badge_title="PRODUCTION SOFTWARE ENGINEERING",
        qr_badge_sub="19-Day Intensive & 3-Month Work-Integrated Learning",
        qr_action="🚀 POINT CAMERA TO APPLY",
        qr_footer="REST/gRPC • Flutter Mobile • CI/CD Cloud • AI Workflows"
    )
    p_path = os.path.join(REPO_ROOT, "designs", "shirts", "shirt-prince.svg")
    with open(p_path, "w", encoding="utf-8") as f:
        f.write(prince_svg)
    print(f"✅ Generated High-Visibility Prince Shirt: {p_path}")

    # 3. Print HTML
    html_content = build_shirt_print_html()
    h_path = os.path.join(REPO_ROOT, "designs", "shirts", "shirt-print.html")
    with open(h_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"✅ Generated DTF Print HTML: {h_path}")

if __name__ == "__main__":
    main()
