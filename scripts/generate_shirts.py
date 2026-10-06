#!/usr/bin/env python3
"""
Generate the high-resolution, front-only vector Staff Showcase T-Shirts
for Kenneth Takudzwa Katsande and Prince Lwazi Nkiwane at the South Africa Tech Showcase.

Requirements:
- Front-only print (no back prints).
- Kenneth Takudzwa Katsande: Director of Operations (Commerce & Ecosystem scale, Tradey Bay scannable QR on front).
- Prince Lwazi Nkiwane: Director of Growth (Talent pipeline & campus growth, Academy WIL scannable QR on front).
- Official branding: Sputnik Tech Group & Sputnik Devs Studio.
- Zaha Hadid parametric wave accents in brand purple.
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

def build_shirt_svg(name, full_name, title, focus_tag, chips, qr_type, qr_label, qr_sub):
    qr_tb = get_svg_path_data("assets/qr/qr-tradeybay-playstore.svg")
    qr_acad = get_svg_path_data("assets/qr/qr-academy-apply.svg")
    qr_path = qr_tb if qr_type == "tradeybay" else qr_acad

    badge_accent = "#10b981" if name == "kenneth" else "#a855f7"
    badge_accent_light = "#34d399" if name == "kenneth" else "#c084fc"

    chip1, chip2, chip3 = chips

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 1600 1000" width="1600" height="1000">
  <defs>
    <!-- Gradients -->
    <linearGradient id="shirtGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#18181b"/>
      <stop offset="50%" stop-color="#0f0f12"/>
      <stop offset="100%" stop-color="#050507"/>
    </linearGradient>

    <linearGradient id="neonPurple" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#c084fc"/>
      <stop offset="50%" stop-color="#a855f7"/>
      <stop offset="100%" stop-color="#7c3aed"/>
    </linearGradient>

    <linearGradient id="neonCyan" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#38bdf8"/>
      <stop offset="100%" stop-color="#0284c7"/>
    </linearGradient>

    <linearGradient id="badgeGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#1e1338"/>
      <stop offset="100%" stop-color="#0d0819"/>
    </linearGradient>

    <filter id="glowAccent" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="8" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>

    <filter id="shirtShadow" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="20" stdDeviation="20" flood-color="#000000" flood-opacity="0.8"/>
    </filter>

    <pattern id="dotGrid" width="20" height="20" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="1" fill="#1e293b" fill-opacity="0.4"/>
    </pattern>
  </defs>

  <style>
    .font-sans {{ font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }}
    .font-mono {{ font-family: 'JetBrains Mono', 'Fira Code', monospace; }}
  </style>

  <!-- Background Canvas -->
  <rect width="1600" height="1000" fill="#060911"/>
  <rect width="1600" height="1000" fill="url(#dotGrid)"/>

  <!-- Top Title Header -->
  <g transform="translate(60, 40)">
    <rect width="400" height="34" rx="17" fill="#0f172a" stroke="{badge_accent}" stroke-width="1.5"/>
    <circle cx="20" cy="17" r="6" fill="{badge_accent}"/>
    <text x="35" y="22" fill="{badge_accent_light}" class="font-mono" font-size="12" font-weight="800" letter-spacing="2">STAFF APPAREL // FRONT-ONLY PRINT</text>

    <text x="0" y="72" fill="#ffffff" class="font-sans" font-size="28" font-weight="900" letter-spacing="1">
      {full_name.upper()} • {title.upper()}
    </text>
    <text x="0" y="96" fill="#94a3b8" class="font-sans" font-size="14">
      Sputnik Tech Group &amp; Sputnik Devs Studio • Front Direct-to-Film (DTF) Production Specifications • Noir Black Premium Tee
    </text>
  </g>

  <!-- =================================================================== -->
  <!-- 1. LEFT: GARMENT MOCKUP (X: 60..780, Y: 130..960)                   -->
  <!-- =================================================================== -->
  <g transform="translate(60, 130)">
    <rect x="235" y="10" width="240" height="28" rx="14" fill="#0f172a" stroke="#334155" stroke-width="1"/>
    <text x="355" y="29" text-anchor="middle" fill="#94a3b8" class="font-mono" font-size="12" font-weight="700">SHIRT FRONT // MOCKUP</text>

    <!-- T-Shirt Silhouette Vector -->
    <path d="M 240 50 Q 355 105 470 50 L 590 105 L 530 240 L 475 220 L 475 750 Q 475 770 455 770 L 255 770 Q 235 770 235 750 L 235 220 L 180 240 L 120 105 Z" 
          fill="url(#shirtGrad)" stroke="#27272a" stroke-width="2.5" filter="url(#shirtShadow)"/>

    <!-- Collar & Shoulder Piping -->
    <path d="M 240 50 Q 355 115 470 50" fill="none" stroke="#3f3f46" stroke-width="4"/>
    <path d="M 240 50 L 120 105" stroke="{badge_accent}" stroke-width="2" stroke-opacity="0.8"/>
    <path d="M 470 50 L 590 105" stroke="#a855f7" stroke-width="2" stroke-opacity="0.8"/>

    <!-- Left Chest: Sputnik Co-Brand Metallic Crest (X: 385..460) -->
    <g transform="translate(385, 200)">
      <circle cx="20" cy="20" r="20" fill="#0c192c" stroke="#38bdf8" stroke-width="1.8"/>
      <circle cx="20" cy="20" r="12" fill="#0284c7"/>
      <ellipse cx="20" cy="20" rx="18" ry="6" fill="none" stroke="#ffffff" stroke-width="1.2" transform="rotate(-30 20 20)"/>
      <circle cx="30" cy="13" r="3" fill="#ffffff"/>

      <text x="46" y="16" fill="#ffffff" class="font-sans" font-size="11" font-weight="900" letter-spacing="1">SPUTNIK</text>
      <text x="46" y="27" fill="#38bdf8" class="font-mono" font-size="7.5" font-weight="800" letter-spacing="1.5">TECH &amp; DEVS</text>
      <text x="46" y="37" fill="#94a3b8" class="font-mono" font-size="6.5">SHOWCASE CREW</text>
    </g>

    <!-- Right Chest: Tactical Executive Security ID Badge (X: 200..365) -->
    <g transform="translate(200, 200)">
      <rect x="0" y="0" width="165" height="70" rx="8" fill="url(#badgeGrad)" stroke="{badge_accent}" stroke-width="1.6"/>
      <rect x="0" y="0" width="165" height="16" rx="8" fill="{badge_accent}" fill-opacity="0.25"/>
      <line x1="0" y1="16" x2="165" y2="16" stroke="{badge_accent}" stroke-width="1"/>

      <text x="8" y="12" fill="{badge_accent_light}" class="font-mono" font-size="7.5" font-weight="800">{focus_tag.upper()}</text>
      <circle cx="152" cy="8" r="3" fill="#38bdf8"/>

      <text x="8" y="33" fill="#ffffff" class="font-sans" font-size="13" font-weight="900" letter-spacing="1">{name.upper()}</text>
      <text x="8" y="45" fill="{badge_accent_light}" class="font-mono" font-size="7.5" font-weight="800">{title.upper()}</text>

      <g transform="translate(8, 51)">
        <rect width="45" height="12" rx="3" fill="#0f172a"/>
        <text x="22" y="9" fill="#94a3b8" class="font-mono" font-size="6.5" font-weight="700" text-anchor="middle">{chip1}</text>

        <rect x="49" width="48" height="12" rx="3" fill="#0f172a"/>
        <text x="73" y="9" fill="#94a3b8" class="font-mono" font-size="6.5" font-weight="700" text-anchor="middle">{chip2}</text>

        <rect x="101" width="45" height="12" rx="3" fill="#0f172a"/>
        <text x="123" y="9" fill="{badge_accent_light}" class="font-mono" font-size="6.5" font-weight="700" text-anchor="middle">{chip3}</text>
      </g>
    </g>

    <!-- CENTER FRONT TORSO: SHOWCASE EMBLEM WITH SCANNABLE QR (X: 235..475) -->
    <g transform="translate(245, 290)">
      <!-- Panel Frame -->
      <rect width="220" height="340" rx="16" fill="#090d16" stroke="#7c3aed" stroke-width="1.8"/>
      
      <!-- Upper Zaha Curve Accent -->
      <path d="M 0 35 C 50 15 110 50 160 30 C 190 20 210 28 220 25 L 220 0 L 0 0 Z" fill="url(#neonPurple)" opacity="0.3"/>
      
      <!-- Event Header -->
      <g transform="translate(110, 24)">
        <text x="0" y="0" fill="#c084fc" class="font-mono" font-size="7.5" font-weight="800" letter-spacing="1.5" text-anchor="middle">SOUTH AFRICA TECH SHOWCASE</text>
        <text x="0" y="14" fill="#ffffff" class="font-sans" font-size="11" font-weight="900" letter-spacing="0.5" text-anchor="middle">THE SPUTNIK ECOSYSTEM</text>
      </g>

      <!-- Scannable High-Contrast QR Code Container -->
      <g transform="translate(45, 48)">
        <rect width="130" height="130" rx="12" fill="#ffffff" stroke="#7c3aed" stroke-width="1.5"/>
        <path d="{qr_path}" fill="#1e1b4b" transform="translate(10, 10) scale(0.24)"/>
      </g>

      <!-- QR Title & Subtitle -->
      <g transform="translate(110, 196)">
        <rect x="-85" y="0" width="170" height="20" rx="6" fill="#1e1b4b" stroke="{badge_accent}" stroke-width="1"/>
        <text x="0" y="14" fill="#ffffff" class="font-mono" font-size="7.5" font-weight="800" text-anchor="middle">📱 POINT PHONE TO SCAN</text>

        <text x="0" y="32" fill="{badge_accent_light}" class="font-sans" font-size="10" font-weight="900" text-anchor="middle">{qr_label}</text>
        <text x="0" y="44" fill="#94a3b8" class="font-mono" font-size="7" text-anchor="middle">{qr_sub}</text>
      </g>

      <!-- Platform Tags Strip -->
      <g transform="translate(12, 252)">
        <rect width="196" height="42" rx="6" fill="#0f172a" stroke="#334155" stroke-width="0.8"/>
        <text x="98" y="15" fill="#a855f7" class="font-mono" font-size="7" font-weight="800" text-anchor="middle">TRADEY BAY • STUDENT RES • UNIHUB</text>
        <text x="98" y="27" fill="#38bdf8" class="font-mono" font-size="7" font-weight="800" text-anchor="middle">SHOPNIK SAAS • DEVS ACADEMY</text>
        <text x="98" y="37" fill="#64748b" class="font-mono" font-size="6" text-anchor="middle">Oracle Cloud SA • .NET 10 • Flutter • AI</text>
      </g>

      <!-- Lower Footer URL Bar -->
      <g transform="translate(110, 316)">
        <text x="0" y="0" fill="#94a3b8" class="font-mono" font-size="7" font-weight="700" text-anchor="middle">sputniktechgroup.com • sputnikdevs.com</text>
        <text x="0" y="10" fill="#64748b" class="font-mono" font-size="6" text-anchor="middle">292 Surrey Avenue, Randburg, JHB</text>
      </g>
    </g>

    <!-- Sleeve Badges -->
    <g transform="translate(135, 175) rotate(-35)">
      <rect width="65" height="18" rx="4" fill="#0f172a" stroke="#7c3aed" stroke-width="1"/>
      <text x="32" y="12" fill="#c084fc" class="font-mono" font-size="7" font-weight="800" text-anchor="middle">📱 TRADEY BAY</text>
    </g>
    <g transform="translate(525, 140) rotate(35)">
      <rect width="65" height="18" rx="4" fill="#0f172a" stroke="{badge_accent}" stroke-width="1"/>
      <text x="32" y="12" fill="{badge_accent_light}" class="font-mono" font-size="7" font-weight="800" text-anchor="middle">🚀 DEVS STUDIO</text>
    </g>

    <!-- Hem Line Watermark -->
    <g transform="translate(355, 735)">
      <line x1="-100" y1="0" x2="100" y2="0" stroke="#1e293b" stroke-width="1"/>
      <text x="0" y="16" fill="#475569" class="font-mono" font-size="8" font-weight="700" letter-spacing="2" text-anchor="middle">
        CAMPUS TO CLOUD // JOHANNESBURG
      </text>
    </g>
  </g>


  <!-- =================================================================== -->
  <!-- 2. RIGHT: 1:1 DTF PRODUCTION TRANSFER GANG ART (X: 830..1540)       -->
  <!-- Ready for direct heat press transfer (Front Only)                   -->
  <!-- =================================================================== -->
  <g transform="translate(830, 130)">
    <rect x="235" y="10" width="260" height="28" rx="14" fill="#0f172a" stroke="{badge_accent}" stroke-width="1"/>
    <text x="365" y="29" text-anchor="middle" fill="{badge_accent_light}" class="font-mono" font-size="12" font-weight="700">DTF GANG SHEET // FRONT PRINT ONLY</text>

    <!-- Outer Sheet Frame (Simulating DTF Transparent Film on Dark Garment) -->
    <rect x="20" y="55" width="670" height="745" rx="20" fill="#0b0f19" stroke="#1e293b" stroke-width="2"/>
    <rect x="20" y="55" width="670" height="40" rx="20" fill="#0f172a"/>
    <text x="40" y="80" fill="#94a3b8" class="font-mono" font-size="11" font-weight="800">
      PRODUCTION SPEC: DIRECT-TO-FILM (DTF) • 150°C @ 15s • COLD PEEL
    </text>

    <!-- CUT PIECE 1: Chest Crest (X: 45, Y: 115) -->
    <g transform="translate(45, 115)">
      <rect width="280" height="110" rx="12" fill="#000000" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="6,4"/>
      <text x="15" y="20" fill="#38bdf8" class="font-mono" font-size="8" font-weight="800">PIECE A: LEFT CHEST CREST (100 x 50 MM)</text>

      <g transform="translate(25, 35)">
        <circle cx="28" cy="28" r="28" fill="#0c192c" stroke="#38bdf8" stroke-width="2.5" filter="url(#glowAccent)"/>
        <circle cx="28" cy="28" r="18" fill="#0284c7"/>
        <ellipse cx="28" cy="28" rx="26" ry="9" fill="none" stroke="#ffffff" stroke-width="2" transform="rotate(-30 28 28)"/>
        <circle cx="43" cy="18" r="4" fill="#ffffff"/>

        <text x="68" y="24" fill="#ffffff" class="font-sans" font-size="15" font-weight="900" letter-spacing="1">SPUTNIK</text>
        <text x="68" y="40" fill="#38bdf8" class="font-mono" font-size="11" font-weight="800" letter-spacing="1.5">TECH &amp; DEVS</text>
        <text x="68" y="54" fill="#94a3b8" class="font-mono" font-size="9">SHOWCASE CREW</text>
      </g>
    </g>

    <!-- CUT PIECE 2: Executive ID Badge (X: 350, Y: 115) -->
    <g transform="translate(350, 115)">
      <rect width="320" height="110" rx="12" fill="#000000" stroke="{badge_accent}" stroke-width="1.5" stroke-dasharray="6,4"/>
      <text x="15" y="20" fill="{badge_accent_light}" class="font-mono" font-size="8" font-weight="800">PIECE B: RIGHT CHEST EXECUTIVE ID (120 x 55 MM)</text>

      <g transform="translate(18, 30)">
        <rect x="0" y="0" width="280" height="70" rx="8" fill="url(#badgeGrad)" stroke="{badge_accent}" stroke-width="2"/>
        <rect x="0" y="0" width="280" height="18" rx="8" fill="{badge_accent}" fill-opacity="0.25"/>
        <line x1="0" y1="18" x2="280" y2="18" stroke="{badge_accent}" stroke-width="1"/>

        <text x="12" y="13" fill="{badge_accent_light}" class="font-mono" font-size="8.5" font-weight="800">{focus_tag.upper()} // ROOT EXEC</text>
        <circle cx="265" cy="9" r="3.5" fill="#38bdf8"/>

        <text x="12" y="36" fill="#ffffff" class="font-sans" font-size="14" font-weight="900" letter-spacing="1">{full_name.upper()}</text>
        <text x="12" y="49" fill="{badge_accent_light}" class="font-mono" font-size="9" font-weight="800">{title.upper()}</text>

        <g transform="translate(12, 54)">
          <rect width="80" height="12" rx="3" fill="#0f172a"/>
          <text x="40" y="9" fill="#94a3b8" class="font-mono" font-size="7" font-weight="700" text-anchor="middle">{chip1}</text>

          <rect x="85" width="85" height="12" rx="3" fill="#0f172a"/>
          <text x="127" y="9" fill="#94a3b8" class="font-mono" font-size="7" font-weight="700" text-anchor="middle">{chip2}</text>

          <rect x="175" width="85" height="12" rx="3" fill="#0f172a"/>
          <text x="217" y="9" fill="{badge_accent_light}" class="font-mono" font-size="7" font-weight="700" text-anchor="middle">{chip3}</text>
        </g>
      </g>
    </g>

    <!-- CUT PIECE 3: Center Front Torso Showcase Art (X: 145, Y: 245) -->
    <g transform="translate(145, 245)">
      <rect width="420" height="535" rx="16" fill="#000000" stroke="#7c3aed" stroke-width="2" stroke-dasharray="8,5"/>
      <text x="20" y="25" fill="#c084fc" class="font-mono" font-size="9" font-weight="800">
        PIECE C: FRONT CENTER TORSO EMBLEM (280 x 360 MM)
      </text>

      <g transform="translate(25, 40)">
        <!-- Artwork Inner Box -->
        <rect width="370" height="470" rx="18" fill="#090d16" stroke="#7c3aed" stroke-width="2.5"/>

        <!-- Upper Zaha Curve Accent -->
        <path d="M 0 50 C 90 20 180 70 270 40 C 320 25 350 40 370 35 L 370 0 L 0 0 Z" fill="url(#neonPurple)" opacity="0.35"/>

        <!-- Header -->
        <g transform="translate(185, 35)">
          <text x="0" y="0" fill="#c084fc" class="font-mono" font-size="10" font-weight="800" letter-spacing="2" text-anchor="middle">SOUTH AFRICA TECH SHOWCASE</text>
          <text x="0" y="20" fill="#ffffff" class="font-sans" font-size="16" font-weight="900" letter-spacing="1" text-anchor="middle">THE SPUTNIK ECOSYSTEM</text>
          <text x="0" y="35" fill="#a855f7" class="sans" font-size="10" font-weight="700" text-anchor="middle">Connecting Campus Commerce to Enterprise Cloud</text>
        </g>

        <!-- Scannable QR -->
        <g transform="translate(85, 85)">
          <rect width="200" height="200" rx="16" fill="#ffffff" stroke="#7c3aed" stroke-width="2" filter="url(#glowAccent)"/>
          <path d="{qr_path}" fill="#1e1b4b" transform="translate(16, 16) scale(0.37)"/>
        </g>

        <!-- Target Scan Badge -->
        <g transform="translate(185, 310)">
          <rect x="-130" y="0" width="260" height="26" rx="8" fill="#1e1b4b" stroke="{badge_accent}" stroke-width="1.5"/>
          <text x="0" y="17" fill="#ffffff" class="font-mono" font-size="10" font-weight="800" text-anchor="middle">📱 POINT CAMERA TO SCAN</text>

          <text x="0" y="44" fill="{badge_accent_light}" class="font-sans" font-size="14" font-weight="900" text-anchor="middle">{qr_label}</text>
          <text x="0" y="60" fill="#cbd5e1" class="font-mono" font-size="10" text-anchor="middle">{qr_sub}</text>
        </g>

        <!-- Platform Badges -->
        <g transform="translate(25, 385)">
          <rect width="320" height="42" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1"/>
          <text x="160" y="16" fill="#c084fc" class="font-mono" font-size="9" font-weight="800" text-anchor="middle">TRADEY BAY • STUDENT RES • UNIHUB</text>
          <text x="160" y="30" fill="#38bdf8" class="font-mono" font-size="9" font-weight="800" text-anchor="middle">SHOPNIK SAAS • DEVS ACADEMY</text>
        </g>

        <!-- Footer Contact -->
        <g transform="translate(185, 450)">
          <text x="0" y="0" fill="#94a3b8" class="font-mono" font-size="9" font-weight="700" text-anchor="middle">sputniktechgroup.com  |  sputnikdevs.com</text>
          <text x="0" y="12" fill="#64748b" class="font-mono" font-size="8" text-anchor="middle">292 Surrey Avenue, Randburg, Johannesburg</text>
        </g>
      </g>
    </g>

  </g>

</svg>"""
    return svg

def build_shirt_print_html():
    qr_tb = get_svg_path_data("assets/qr/qr-tradeybay-playstore.svg")
    qr_acad = get_svg_path_data("assets/qr/qr-academy-apply.svg")

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Sputnik Showcase — Staff T-Shirt Front DTF Gang Sheets</title>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@500;700;800&display=swap');

    @page {{
      size: A3 landscape;
      margin: 8mm;
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    body {{
      background: #060911;
      color: #ffffff;
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
      padding: 15px;
      -webkit-print-color-adjust: exact;
      print-color-adjust: exact;
    }}

    .sheet-page {{
      background: #090e18;
      border: 2px solid #1e293b;
      border-radius: 16px;
      padding: 24px;
      margin-bottom: 30px;
      page-break-after: always;
      min-height: 270mm;
    }}

    .sheet-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 2px solid #1e293b;
      padding-bottom: 12px;
      margin-bottom: 20px;
    }}

    .badge-tag {{
      display: inline-block;
      padding: 5px 14px;
      background: #0f172a;
      border: 1.5px solid #10b981;
      border-radius: 20px;
      font-family: 'JetBrains Mono', monospace;
      font-size: 11px;
      font-weight: 800;
      color: #34d399;
      letter-spacing: 1.5px;
    }}

    .badge-tag-prince {{
      border-color: #a855f7;
      color: #c084fc;
    }}

    .layout-grid {{
      display: grid;
      grid-template-columns: 340px 1fr;
      gap: 25px;
    }}

    .chest-col {{
      display: flex;
      flex-direction: column;
      gap: 20px;
    }}

    .print-pod {{
      background: #000000;
      border: 1.5px dashed #475569;
      border-radius: 14px;
      padding: 18px;
      position: relative;
    }}

    .pod-label {{
      font-family: 'JetBrains Mono', monospace;
      font-size: 10px;
      font-weight: 800;
      color: #94a3b8;
      margin-bottom: 12px;
      display: flex;
      justify-content: space-between;
    }}

    .crest-art {{
      display: flex;
      align-items: center;
      gap: 15px;
      padding: 10px;
      background: #080c14;
      border: 1px solid #1e293b;
      border-radius: 10px;
    }}

    .exec-badge {{
      background: #0d0819;
      border: 2px solid #10b981;
      border-radius: 10px;
      padding: 14px;
    }}

    .exec-badge-prince {{
      border-color: #a855f7;
    }}

    .torso-box {{
      background: #090d16;
      border: 2px solid #7c3aed;
      border-radius: 16px;
      padding: 24px;
      display: flex;
      flex-direction: column;
      align-items: center;
      text-align: center;
    }}
  </style>
</head>
<body>

  <!-- =================================================================== -->
  <!-- PAGE 1: KENNETH'S FRONT DTF GANG SHEET                             -->
  <!-- =================================================================== -->
  <div class="sheet-page">
    <div class="sheet-header">
      <div>
        <span class="badge-tag">UNIT 01: KENNETH TAKUDZWA KATSANDE</span>
        <h1 style="font-size: 20px; font-weight: 900; margin-top: 6px;">DIRECTOR OF OPERATIONS // FRONT PRINT GANG SHEET</h1>
        <p style="font-size: 11px; color: #94a3b8;">Direct-to-Film (DTF) Heat Transfer • 150°C for 15s • Peel Cold • Noir Black 200gsm Tee</p>
      </div>
      <div style="text-align: right; font-family: 'JetBrains Mono', monospace; font-size: 11px; color: #64748b;">
        PRINT AREA: FRONT ONLY<br>
        SHOWCASE 2026 // SPUTNIK
      </div>
    </div>

    <div class="layout-grid">
      <!-- Left Column: Chest Crest & Executive Badge -->
      <div class="chest-col">
        <!-- Piece A: Chest Crest -->
        <div class="print-pod">
          <div class="pod-label">
            <span>PIECE A: LEFT CHEST CREST</span>
            <span>100 x 50 MM</span>
          </div>
          <div class="crest-art">
            <svg width="44" height="44" viewBox="0 0 44 44">
              <circle cx="22" cy="22" r="21" fill="#0c192c" stroke="#38bdf8" stroke-width="2"/>
              <circle cx="22" cy="22" r="14" fill="#0284c7"/>
              <ellipse cx="22" cy="22" rx="20" ry="7" fill="none" stroke="#ffffff" stroke-width="1.5" transform="rotate(-30 22 22)"/>
              <circle cx="34" cy="14" r="3" fill="#ffffff"/>
            </svg>
            <div>
              <div style="font-size: 14px; font-weight: 900; letter-spacing: 1px;">SPUTNIK</div>
              <div style="font-family: 'JetBrains Mono', monospace; font-size: 10px; font-weight: 800; color: #38bdf8;">TECH &amp; DEVS</div>
              <div style="font-family: 'JetBrains Mono', monospace; font-size: 8px; color: #94a3b8;">SHOWCASE CREW</div>
            </div>
          </div>
        </div>

        <!-- Piece B: Executive Badge -->
        <div class="print-pod">
          <div class="pod-label">
            <span>PIECE B: EXECUTIVE ID BADGE</span>
            <span>120 x 55 MM</span>
          </div>
          <div class="exec-badge">
            <div style="font-family: 'JetBrains Mono', monospace; font-size: 8px; font-weight: 800; color: #34d399; margin-bottom: 4px;">
              EXECUTIVE LEADERSHIP // OPS
            </div>
            <div style="font-size: 14px; font-weight: 900; letter-spacing: 1px;">KENNETH TAKUDZWA KATSANDE</div>
            <div style="font-family: 'JetBrains Mono', monospace; font-size: 10px; font-weight: 800; color: #34d399; margin-top: 2px;">
              DIRECTOR OF OPERATIONS
            </div>
            <div style="display: flex; gap: 6px; margin-top: 8px; font-family: 'JetBrains Mono', monospace; font-size: 7px; color: #94a3b8;">
              <span style="background: #1e293b; padding: 2px 6px; border-radius: 3px;">OPERATIONS</span>
              <span style="background: #1e293b; padding: 2px 6px; border-radius: 3px;">COMMERCE</span>
              <span style="background: #1e293b; padding: 2px 6px; border-radius: 3px; color: #34d399;">SCALE</span>
            </div>
          </div>
        </div>
      </div>

      <!-- Right Column: Center Front Torso Showcase Art -->
      <div class="print-pod">
        <div class="pod-label">
          <span>PIECE C: FRONT CENTER TORSO SHOWCASE EMBLEM</span>
          <span>280 x 360 MM</span>
        </div>
        <div class="torso-box">
          <div style="font-family: 'JetBrains Mono', monospace; font-size: 10px; font-weight: 800; color: #c084fc; letter-spacing: 2px;">
            SOUTH AFRICA TECH SHOWCASE
          </div>
          <div style="font-size: 18px; font-weight: 900; letter-spacing: 1px; margin-top: 4px;">
            THE SPUTNIK ECOSYSTEM
          </div>
          <div style="font-size: 11px; color: #a855f7; font-weight: 600; margin-top: 2px;">
            Connecting Campus Commerce to Enterprise Cloud
          </div>

          <!-- Tradey Bay QR -->
          <div style="background: #ffffff; padding: 12px; border-radius: 12px; border: 2px solid #7c3aed; margin: 16px 0;">
            <svg width="150" height="150" viewBox="0 0 150 150">
              <path d="{qr_tb}" fill="#1e1b4b" transform="translate(10, 10) scale(0.28)"/>
            </svg>
          </div>

          <div style="background: #1e1b4b; border: 1px solid #10b981; border-radius: 6px; padding: 4px 14px; font-family: 'JetBrains Mono', monospace; font-size: 9px; font-weight: 800;">
            📱 SCAN TO INSTALL TRADEY BAY (ANDROID &amp; iOS)
          </div>
          <div style="font-size: 12px; font-weight: 900; color: #34d399; margin-top: 6px;">
            Tradey Bay Campus Super App • 0% Commission
          </div>
          <div style="font-family: 'JetBrains Mono', monospace; font-size: 9px; color: #94a3b8; margin-top: 2px;">
            v2.0.4+31 • Student Housing • Classifieds • POPIA Compliant
          </div>

          <div style="background: #0f172a; border: 1px solid #334155; border-radius: 6px; padding: 6px 14px; margin-top: 14px; font-family: 'JetBrains Mono', monospace; font-size: 8px;">
            <span style="color: #c084fc;">TRADEY BAY • STUDENT RES • UNIHUB</span> | 
            <span style="color: #38bdf8;">SHOPNIK SAAS • DEVS ACADEMY</span>
          </div>

          <div style="margin-top: 12px; font-family: 'JetBrains Mono', monospace; font-size: 8px; color: #64748b;">
            sputniktechgroup.com • sputnikdevs.com • 292 Surrey Avenue, Randburg, JHB
          </div>
        </div>
      </div>
    </div>
  </div>


  <!-- =================================================================== -->
  <!-- PAGE 2: PRINCE'S FRONT DTF GANG SHEET                              -->
  <!-- =================================================================== -->
  <div class="sheet-page">
    <div class="sheet-header">
      <div>
        <span class="badge-tag badge-tag-prince">UNIT 02: PRINCE LWAZI NKIWANE</span>
        <h1 style="font-size: 20px; font-weight: 900; margin-top: 6px;">DIRECTOR OF GROWTH // FRONT PRINT GANG SHEET</h1>
        <p style="font-size: 11px; color: #94a3b8;">Direct-to-Film (DTF) Heat Transfer • 150°C for 15s • Peel Cold • Noir Black 200gsm Tee</p>
      </div>
      <div style="text-align: right; font-family: 'JetBrains Mono', monospace; font-size: 11px; color: #64748b;">
        PRINT AREA: FRONT ONLY<br>
        SHOWCASE 2026 // SPUTNIK
      </div>
    </div>

    <div class="layout-grid">
      <!-- Left Column: Chest Crest & Executive Badge -->
      <div class="chest-col">
        <!-- Piece A: Chest Crest -->
        <div class="print-pod">
          <div class="pod-label">
            <span>PIECE A: LEFT CHEST CREST</span>
            <span>100 x 50 MM</span>
          </div>
          <div class="crest-art">
            <svg width="44" height="44" viewBox="0 0 44 44">
              <circle cx="22" cy="22" r="21" fill="#0c192c" stroke="#38bdf8" stroke-width="2"/>
              <circle cx="22" cy="22" r="14" fill="#0284c7"/>
              <ellipse cx="22" cy="22" rx="20" ry="7" fill="none" stroke="#ffffff" stroke-width="1.5" transform="rotate(-30 22 22)"/>
              <circle cx="34" cy="14" r="3" fill="#ffffff"/>
            </svg>
            <div>
              <div style="font-size: 14px; font-weight: 900; letter-spacing: 1px;">SPUTNIK</div>
              <div style="font-family: 'JetBrains Mono', monospace; font-size: 10px; font-weight: 800; color: #38bdf8;">TECH &amp; DEVS</div>
              <div style="font-family: 'JetBrains Mono', monospace; font-size: 8px; color: #94a3b8;">SHOWCASE CREW</div>
            </div>
          </div>
        </div>

        <!-- Piece B: Executive Badge -->
        <div class="print-pod">
          <div class="pod-label">
            <span>PIECE B: EXECUTIVE ID BADGE</span>
            <span>120 x 55 MM</span>
          </div>
          <div class="exec-badge exec-badge-prince">
            <div style="font-family: 'JetBrains Mono', monospace; font-size: 8px; font-weight: 800; color: #c084fc; margin-bottom: 4px;">
              EXECUTIVE LEADERSHIP // GROWTH
            </div>
            <div style="font-size: 14px; font-weight: 900; letter-spacing: 1px;">PRINCE LWAZI NKIWANE</div>
            <div style="font-family: 'JetBrains Mono', monospace; font-size: 10px; font-weight: 800; color: #c084fc; margin-top: 2px;">
              DIRECTOR OF GROWTH
            </div>
            <div style="display: flex; gap: 6px; margin-top: 8px; font-family: 'JetBrains Mono', monospace; font-size: 7px; color: #94a3b8;">
              <span style="background: #1e293b; padding: 2px 6px; border-radius: 3px;">GROWTH</span>
              <span style="background: #1e293b; padding: 2px 6px; border-radius: 3px;">TALENT</span>
              <span style="background: #1e293b; padding: 2px 6px; border-radius: 3px; color: #c084fc;">EXPANSION</span>
            </div>
          </div>
        </div>
      </div>

      <!-- Right Column: Center Front Torso Showcase Art -->
      <div class="print-pod">
        <div class="pod-label">
          <span>PIECE C: FRONT CENTER TORSO SHOWCASE EMBLEM</span>
          <span>280 x 360 MM</span>
        </div>
        <div class="torso-box">
          <div style="font-family: 'JetBrains Mono', monospace; font-size: 10px; font-weight: 800; color: #c084fc; letter-spacing: 2px;">
            SOUTH AFRICA TECH SHOWCASE
          </div>
          <div style="font-size: 18px; font-weight: 900; letter-spacing: 1px; margin-top: 4px;">
            THE SPUTNIK ECOSYSTEM
          </div>
          <div style="font-size: 11px; color: #a855f7; font-weight: 600; margin-top: 2px;">
            Connecting Campus Commerce to Enterprise Cloud
          </div>

          <!-- Academy QR -->
          <div style="background: #ffffff; padding: 12px; border-radius: 12px; border: 2px solid #7c3aed; margin: 16px 0;">
            <svg width="150" height="150" viewBox="0 0 150 150">
              <path d="{qr_acad}" fill="#1e1b4b" transform="translate(10, 10) scale(0.28)"/>
            </svg>
          </div>

          <div style="background: #1e1b4b; border: 1px solid #a855f7; border-radius: 6px; padding: 4px 14px; font-family: 'JetBrains Mono', monospace; font-size: 9px; font-weight: 800;">
            🚀 SCAN TO APPLY: WIL LEARNERSHIPS &amp; TALENT
          </div>
          <div style="font-size: 12px; font-weight: 900; color: #c084fc; margin-top: 6px;">
            Sputnik Devs Academy • Work-Integrated Learning
          </div>
          <div style="font-family: 'JetBrains Mono', monospace; font-size: 9px; color: #94a3b8; margin-top: 2px;">
            REST/gRPC • Flutter • DevOps CI/CD • Postgres/Redis • AI Agents
          </div>

          <div style="background: #0f172a; border: 1px solid #334155; border-radius: 6px; padding: 6px 14px; margin-top: 14px; font-family: 'JetBrains Mono', monospace; font-size: 8px;">
            <span style="color: #c084fc;">TRADEY BAY • STUDENT RES • UNIHUB</span> | 
            <span style="color: #38bdf8;">SHOPNIK SAAS • DEVS ACADEMY</span>
          </div>

          <div style="margin-top: 12px; font-family: 'JetBrains Mono', monospace; font-size: 8px; color: #64748b;">
            sputniktechgroup.com • sputnikdevs.com • 292 Surrey Avenue, Randburg, JHB
          </div>
        </div>
      </div>
    </div>
  </div>

</body>
</html>"""
    return html

def main():
    print("Generating Front-Only Staff Shirts & DTF Gang Sheets...")

    # 1. Kenneth Shirt SVG
    kenneth_svg = build_shirt_svg(
        name="kenneth",
        full_name="Kenneth Takudzwa Katsande",
        title="Director of Operations",
        focus_tag="OPERATIONS & COMMERCE",
        chips=["OPERATIONS", "COMMERCE", "SCALE"],
        qr_type="tradeybay",
        qr_label="Tradey Bay Super App",
        qr_sub="0% Commission • v2.0.4+31 • Housing"
    )
    k_path = os.path.join(REPO_ROOT, "designs", "shirts", "shirt-kenneth.svg")
    with open(k_path, "w", encoding="utf-8") as f:
        f.write(kenneth_svg)
    print(f"✅ Generated Kenneth Shirt: {k_path}")

    # 2. Prince Shirt SVG
    prince_svg = build_shirt_svg(
        name="prince",
        full_name="Prince Lwazi Nkiwane",
        title="Director of Growth",
        focus_tag="GROWTH & TALENT",
        chips=["GROWTH", "TALENT", "EXPANSION"],
        qr_type="academy",
        qr_label="Sputnik Devs Academy",
        qr_sub="WIL Learnerships • CS Graduates"
    )
    p_path = os.path.join(REPO_ROOT, "designs", "shirts", "shirt-prince.svg")
    with open(p_path, "w", encoding="utf-8") as f:
        f.write(prince_svg)
    print(f"✅ Generated Prince Shirt: {p_path}")

    # 3. Print HTML
    html_content = build_shirt_print_html()
    h_path = os.path.join(REPO_ROOT, "designs", "shirts", "shirt-print.html")
    with open(h_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"✅ Generated DTF Print HTML: {h_path}")

if __name__ == "__main__":
    main()
