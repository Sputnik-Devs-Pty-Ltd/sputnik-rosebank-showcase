#!/usr/bin/env python3
"""
Generate the high-resolution, Zaha Hadid-inspired, light-themed vector Handheld Print Flyer (A5 Portrait: 148mm x 210mm)
for Sputnik Tech Group and Sputnik Devs Studio at the South Africa Tech Showcase.

Replicates the exact locked-down banner design and content, fully optimized for A5 handheld print:
1. Vibrant Zaha Hadid Architectural Background in royal brand purples.
2. Left Column: Sputnik Tech Group, Tradey Bay (v2.0.4+31, notchless phone mockups, 4 platform pillars, scannable QR, POPIA compliant).
3. Right Column: Sputnik Devs Studio, Student Res Management & University Hub (4 pillars, dual QRs), Shopnik (from R349/mo, 5 pillars, QR), Devs Academy (5 broad production disciplines, WIL, QR).
4. Executive Leadership & Contact Footer:
   - Takudzwa Mupanesure: Founder, Chief Executive Officer & Lead Architect
   - In Concurrence with: Kenneth Takudzwa Katsande (Director of Operations) & Prince Lwazi Nkiwane (Director of Growth)
   - 292 Surrey Avenue, Randburg, Johannesburg, 2194
   - Direct: takudzwam@sputniktechgroup.com | info@sputniktechgroup.com | +27 66 321 5528 | +263 787 015 123
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

def build_flyer_svg():
    # 1. Load real corporate logos and screenshots
    sputnik_tech_logo = get_base64_img("assets/Sputnik-Tech-Group-Logo.png")
    sputnik_devs_logo = get_base64_img("assets/Sputnik-Devs-Studio-logo.png")
    tradeybay_primary_logo = get_base64_img("assets/TradeyBay_primary_Logo.png")
    tradeybay_dark_screenshot = get_base64_img("assets/TradeyBayScreenShopDarkMode.jpeg")
    tradeybay_light_screenshot = get_base64_img("assets/TradeyBayScreenshopLigtMode.jpeg")
    shopnik_logo = get_base64_img("assets/logos/shopnik-logo-horizontal-transparent.png")

    # 2. Extract QR code vector paths
    qr_tb = get_svg_path_data("assets/qr/qr-tradeybay-playstore.svg")
    qr_acad = get_svg_path_data("assets/qr/qr-academy-apply.svg")
    qr_srms = get_svg_path_data("assets/qr/qr-student-housing-srms.svg")
    qr_unihub = get_svg_path_data("assets/qr/qr-university-hub.svg")
    qr_shopnik = get_svg_path_data("assets/qr/qr-shopnik-ecommerce.svg")

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 1480 2100" width="148mm" height="210mm">
  <defs>
    <!-- Background Canvas Base Gradient -->
    <linearGradient id="bgCanvasGradFlyer" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="25%" stop-color="#fdfbfe"/>
      <stop offset="60%" stop-color="#faf5ff"/>
      <stop offset="100%" stop-color="#f3e8ff"/>
    </linearGradient>

    <!-- Vibrant Zaha Hadid Parametric Purple Ribbon Gradients -->
    <linearGradient id="zahaPurple1Flyer" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#c084fc"/>
      <stop offset="35%" stop-color="#a855f7"/>
      <stop offset="70%" stop-color="#7c3aed"/>
      <stop offset="100%" stop-color="#6b21a8"/>
    </linearGradient>

    <linearGradient id="zahaPurple2Flyer" x1="0%" y1="100%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#6b21a8"/>
      <stop offset="40%" stop-color="#7c3aed"/>
      <stop offset="80%" stop-color="#9333ea"/>
      <stop offset="100%" stop-color="#c084fc"/>
    </linearGradient>

    <linearGradient id="zahaPurple3Flyer" x1="100%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#581c87"/>
      <stop offset="45%" stop-color="#7c3aed"/>
      <stop offset="85%" stop-color="#a855f7"/>
      <stop offset="100%" stop-color="#e9d5ff"/>
    </linearGradient>

    <linearGradient id="zahaStreamGrad1Flyer" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#7c3aed"/>
      <stop offset="50%" stop-color="#a855f7"/>
      <stop offset="100%" stop-color="#c084fc"/>
    </linearGradient>

    <linearGradient id="zahaStreamGrad2Flyer" x1="100%" y1="0%" x2="0%" y2="0%">
      <stop offset="0%" stop-color="#6b21a8"/>
      <stop offset="50%" stop-color="#8b5cf6"/>
      <stop offset="100%" stop-color="#c084fc"/>
    </linearGradient>

    <linearGradient id="tbLightCardGradFlyer" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="50%" stop-color="#faf5ff"/>
      <stop offset="100%" stop-color="#f3e8ff"/>
    </linearGradient>

    <!-- Professional Card Shadows -->
    <filter id="softCardShadowFlyer" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="6" stdDeviation="10" flood-color="#7c3aed" flood-opacity="0.08"/>
    </filter>

    <filter id="deepCardShadowFlyer" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="10" stdDeviation="16" flood-color="#581c87" flood-opacity="0.12"/>
    </filter>

    <filter id="phoneShadowFlyer" x="-15%" y="-15%" width="130%" height="130%">
      <feDropShadow dx="0" dy="12" stdDeviation="16" flood-color="#0f172a" flood-opacity="0.22"/>
    </filter>

    <!-- Clip Paths for Notchless Fullscreen Phone Mockups -->
    <clipPath id="phoneScreenClipFlyerLight">
      <rect x="0" y="0" width="277" height="372" rx="20"/>
    </clipPath>
    <clipPath id="phoneScreenClipFlyerDark">
      <rect x="0" y="0" width="277" height="372" rx="20"/>
    </clipPath>

    <!-- Subtle Parametric Pattern -->
    <pattern id="gridPurpleLightFlyer" width="30" height="30" patternUnits="userSpaceOnUse">
      <path d="M 30 0 L 0 0 0 30" fill="none" stroke="#7c3aed" stroke-width="0.5" stroke-opacity="0.06"/>
    </pattern>

    <!-- Inlined QR Code Vector Paths -->
    <path id="qr-path-tradeybay-f" d="{qr_tb}"/>
    <path id="qr-path-academy-f" d="{qr_acad}"/>
    <path id="qr-path-srms-f" d="{qr_srms}"/>
    <path id="qr-path-unihub-f" d="{qr_unihub}"/>
    <path id="qr-path-shopnik-f" d="{qr_shopnik}"/>

    <!-- REAL OFFICIAL GOOGLE PLAY BADGE -->
    <g id="badge-google-play-flyer">
      <rect width="180" height="52" rx="10" fill="#000000" stroke="#334155" stroke-width="1.2"/>
      <g transform="translate(14, 10)">
        <path d="M 1.5 2.5 L 18 16 L 1.5 29.5 Z" fill="#22c55e"/>
        <path d="M 1.5 2.5 L 18 16 L 24 10 L 5.5 0.5 Z" fill="#0ea5e9"/>
        <path d="M 18 16 L 1.5 29.5 L 5.5 31.5 L 24 22 Z" fill="#ef4444"/>
        <path d="M 18 16 L 24 10 L 29 13.5 C 31 14.8 31 17.2 29 18.5 L 24 22 Z" fill="#eab308"/>
      </g>
      <text x="56" y="20" fill="#94a3b8" font-family="'Inter', sans-serif" font-size="9" font-weight="700" letter-spacing="0.8">GET IT ON</text>
      <text x="56" y="38" fill="#ffffff" font-family="'Inter', sans-serif" font-size="16" font-weight="900" letter-spacing="0.2">Google Play</text>
    </g>

    <!-- REAL OFFICIAL APPLE APP STORE BADGE -->
    <g id="badge-app-store-flyer">
      <rect width="180" height="52" rx="10" fill="#000000" stroke="#334155" stroke-width="1.2"/>
      <g transform="translate(16, 12)">
        <path d="M 15 13 C 15 8.5 18.5 6 18.7 5.8 C 16.5 2.6 13 2.1 11.8 2.1 C 8.8 1.8 5.8 3.9 4.2 3.9 C 2.6 3.9 0.2 2.1 -2 2.1 C -5 2.1 -8 4 -9.6 7 C -12.9 12.8 -10.4 21.3 -7.2 25.8 C -5.6 28 -3.8 30.5 -1.2 30.4 C 1.2 30.3 2.2 28.8 5.2 28.8 C 8.2 28.8 9.1 30.4 11.8 30.4 C 14.5 30.4 16.1 28.1 17.7 25.8 C 19.5 23.2 20.3 20.6 20.4 20.4 C 20.2 20.3 15 18.3 15 13 Z" fill="#ffffff" transform="scale(0.85) translate(14, 0)"/>
        <path d="M 10.5 0 C 11.8 -1.7 12.7 -4 12.4 -6.4 C 10.4 -6.3 8 -5 6.7 -3.4 C 5.5 -1.9 4.5 0.5 4.8 2.8 C 7 3 9.3 1.6 10.5 0 Z" fill="#ffffff" transform="scale(0.85) translate(14, 0)"/>
      </g>
      <text x="56" y="20" fill="#94a3b8" font-family="'Inter', sans-serif" font-size="8.5" font-weight="700" letter-spacing="0.8">COMING SOON ON</text>
      <text x="56" y="38" fill="#ffffff" font-family="'Inter', sans-serif" font-size="16" font-weight="900" letter-spacing="0.2">App Store</text>
    </g>

    <!-- Vector Feature Icons -->
    <g id="icon-laptop-f">
      <rect x="3" y="27" width="42" height="4" rx="2" fill="#7c3aed"/>
      <path d="M 6 30 L 42 30" stroke="#c084fc" stroke-width="1"/>
      <rect x="7" y="6" width="34" height="22" rx="2.5" fill="#1e1b4b" stroke="#7c3aed" stroke-width="1.5"/>
      <rect x="9" y="8" width="30" height="18" rx="1" fill="#f5f3ff"/>
      <line x1="12" y1="12" x2="22" y2="12" stroke="#7c3aed" stroke-width="1.8" stroke-linecap="round"/>
      <line x1="12" y1="16" x2="33" y2="16" stroke="#a855f7" stroke-width="1.4" stroke-linecap="round"/>
      <line x1="12" y1="20" x2="27" y2="20" stroke="#7c3aed" stroke-width="1.4" stroke-linecap="round"/>
      <circle cx="31" cy="19" r="4.5" fill="#7c3aed"/>
      <path d="M 29.5 19 L 30.5 20.5 L 33 17.5" fill="none" stroke="#ffffff" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"/>
    </g>

    <g id="icon-storefront-f">
      <path d="M 4 14 L 8 4 L 40 4 L 44 14 Z" fill="#7c3aed"/>
      <path d="M 4 14 Q 8 18 12 14 Q 16 18 20 14 Q 24 18 28 14 Q 32 18 36 14 Q 40 18 44 14" fill="#a855f7"/>
      <rect x="8" y="16" width="32" height="24" rx="1.5" fill="#ffffff" stroke="#7c3aed" stroke-width="1.8"/>
      <rect x="12" y="22" width="10" height="18" rx="1" fill="#ede9fe"/>
      <rect x="26" y="22" width="10" height="10" rx="1" fill="#ede9fe"/>
      <circle cx="32" cy="34" r="5" fill="#22c55e"/>
      <path d="M 30 34 L 31.5 35.5 L 34.5 32.5" fill="none" stroke="#ffffff" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"/>
    </g>

    <g id="icon-map-radar-f">
      <path d="M 4 10 L 16 5 L 32 10 L 44 5 L 44 37 L 32 42 L 16 37 L 4 42 Z" fill="#faf5ff" stroke="#7c3aed" stroke-width="1.8" stroke-linejoin="round"/>
      <line x1="16" y1="5" x2="16" y2="37" stroke="#c084fc" stroke-width="1.5" stroke-dasharray="2,2"/>
      <line x1="32" y1="10" x2="32" y2="42" stroke="#c084fc" stroke-width="1.5" stroke-dasharray="2,2"/>
      <circle cx="24" cy="20" r="10" fill="#ede9fe" fill-opacity="0.7"/>
      <circle cx="24" cy="20" r="5" fill="#7c3aed"/>
      <circle cx="24" cy="20" r="1.5" fill="#ffffff"/>
      <path d="M 24 10 C 18 10 14 14 14 19 C 14 26 24 33 24 33 C 24 33 34 26 34 19 C 34 14 30 10 24 10 Z" fill="#7c3aed" opacity="0.3"/>
    </g>

    <g id="icon-ats-resume-f">
      <rect x="8" y="4" width="32" height="40" rx="3" fill="#ffffff" stroke="#7c3aed" stroke-width="2"/>
      <rect x="14" y="10" width="8" height="8" rx="4" fill="#c084fc"/>
      <line x1="26" y1="11" x2="34" y2="11" stroke="#7c3aed" stroke-width="2" stroke-linecap="round"/>
      <line x1="26" y1="15" x2="32" y2="15" stroke="#a855f7" stroke-width="1.5" stroke-linecap="round"/>
      <line x1="14" y1="23" x2="34" y2="23" stroke="#94a3b8" stroke-width="1.8" stroke-linecap="round"/>
      <line x1="14" y1="28" x2="34" y2="28" stroke="#94a3b8" stroke-width="1.8" stroke-linecap="round"/>
      <line x1="14" y1="33" x2="26" y2="33" stroke="#94a3b8" stroke-width="1.8" stroke-linecap="round"/>
      <circle cx="34" cy="31" r="7" fill="#fef3c7" stroke="#d97706" stroke-width="1.5"/>
      <path d="M 34 26 Q 34 31 39 31 Q 34 31 34 36 Q 34 31 29 31 Q 34 31 34 26 Z" fill="#d97706"/>
      <circle cx="39" cy="25" r="1.5" fill="#7c3aed"/>
    </g>

    <g id="icon-hostel-f">
      <rect x="2" y="8" width="34" height="28" rx="2" fill="#ffffff" stroke="#7c3aed" stroke-width="2"/>
      <polygon points="1,8 19,0 37,8" fill="#7c3aed"/>
      <rect x="6" y="12" width="5" height="5" fill="#c084fc"/>
      <rect x="16" y="12" width="5" height="5" fill="#c084fc"/>
      <rect x="26" y="12" width="5" height="5" fill="#c084fc"/>
      <rect x="6" y="20" width="5" height="5" fill="#c084fc"/>
      <rect x="16" y="20" width="5" height="5" fill="#c084fc"/>
      <rect x="26" y="20" width="5" height="5" fill="#c084fc"/>
      <rect x="6" y="28" width="5" height="5" fill="#c084fc"/>
      <rect x="26" y="28" width="5" height="5" fill="#c084fc"/>
      <rect x="15" y="28" width="8" height="8" rx="1" fill="#4c1d95"/>
    </g>

    <g id="icon-unihub-f">
      <circle cx="20" cy="20" r="18" fill="#18181b" stroke="#7c3aed" stroke-width="2"/>
      <path d="M 20 11 L 31 16 L 20 21 L 9 16 Z" fill="#a855f7"/>
      <path d="M 13 18 L 13 24 C 13 27 16 29 20 29 C 24 29 27 27 27 24 L 27 18" fill="none" stroke="#f59e0b" stroke-width="1.8" stroke-linecap="round"/>
      <path d="M 29 17 L 31 22 L 30 22 L 32 26" fill="none" stroke="#ffffff" stroke-width="1" stroke-linecap="round"/>
    </g>

    <g id="icon-academy-f">
      <polygon points="24,6 44,15 24,23 4,15" fill="#d97706" stroke="#92400e" stroke-width="1.8"/>
      <path d="M 12 19 L 12 28 C 12 34 36 34 36 28 L 36 19" fill="#fef3c7" stroke="#92400e" stroke-width="1.8"/>
      <path d="M 24 15 Q 38 16 39 26 L 37 32" fill="none" stroke="#b45309" stroke-width="1.8" stroke-linecap="round"/>
      <circle cx="37" cy="33" r="1.8" fill="#b45309"/>
      <g transform="translate(13, 33)">
        <path d="M 0 5 L 8 0 L 16 5 L 14 7 L 8 3 L 2 7 Z" fill="#92400e"/>
        <path d="M 8 3 L 8 9" stroke="#92400e" stroke-width="1.8" stroke-linecap="round"/>
      </g>
    </g>
  </defs>

  <style>
    .sans {{ font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }}
    .mono {{ font-family: 'JetBrains Mono', 'Fira Code', monospace; }}
  </style>

  <!-- =================================================================== -->
  <!-- ZAHA HADID PARAMETRIC PURPLE BACKGROUND ARCHITECTURE (A5 CANVAS)    -->
  <!-- =================================================================== -->
  <rect x="0" y="0" width="1480" height="2100" fill="url(#bgCanvasGradFlyer)"/>
  <rect x="0" y="0" width="1480" height="2100" fill="url(#gridPurpleLightFlyer)"/>

  <!-- Ambient Glow Fields -->
  <circle cx="260" cy="400" r="450" fill="#ede9fe" fill-opacity="0.65"/>
  <circle cx="1220" cy="480" r="460" fill="#f3e8ff" fill-opacity="0.70"/>
  <circle cx="280" cy="1500" r="480" fill="#fae8ff" fill-opacity="0.60"/>
  <circle cx="1200" cy="1460" r="460" fill="#ede9fe" fill-opacity="0.65"/>

  <!-- Zaha Hadid Fluid Ribbons -->
  <path d="M -80 60 C 300 150 560 90 740 125 C 920 160 1180 100 1560 60 L 1560 380 C 1280 430 1000 340 740 375 C 480 410 200 330 -80 380 Z" fill="url(#zahaPurple1Flyer)" opacity="0.16"/>
  <path d="M -80 450 C 320 380 620 570 980 480 C 1280 420 1420 540 1560 470 L 1560 700 C 1300 770 1040 630 720 710 C 380 780 150 650 -80 720 Z" fill="url(#zahaPurple2Flyer)" opacity="0.12"/>
  <path d="M -80 720 C 260 630 560 830 890 750 C 1180 670 1330 830 1560 750 L 1560 1100 C 1300 1180 1060 1010 740 1090 C 420 1160 180 1020 -80 1110 Z" fill="url(#zahaPurple2Flyer)" opacity="0.15"/>
  <path d="M -80 1320 C 320 1210 650 1440 1000 1360 C 1310 1290 1430 1440 1560 1380 L 1560 1800 C 1260 1870 1000 1720 620 1800 C 280 1870 90 1730 -80 1810 Z" fill="url(#zahaPurple3Flyer)" opacity="0.16"/>

  <!-- Edge Framing Ribbons -->
  <path d="M 0 0 C 120 320 40 740 130 1150 C 200 1520 60 1890 0 2100 L 0 0 Z" fill="url(#zahaPurple1Flyer)" opacity="0.08"/>
  <path d="M 1480 0 C 1360 340 1440 760 1350 1170 C 1270 1550 1420 1910 1480 2100 L 1480 0 Z" fill="url(#zahaPurple2Flyer)" opacity="0.08"/>

  <!-- Contour Streamlines -->
  <path d="M -60 160 C 280 230 560 180 740 210 C 920 240 1200 190 1540 160" fill="none" stroke="url(#zahaStreamGrad1Flyer)" stroke-width="2" opacity="0.32"/>
  <path d="M -60 520 C 340 460 640 630 960 550 C 1260 480 1400 610 1540 540" fill="none" stroke="url(#zahaStreamGrad2Flyer)" stroke-width="1.8" opacity="0.25"/>
  <path d="M -60 840 C 280 760 580 940 910 870 C 1200 800 1340 950 1540 880" fill="none" stroke="url(#zahaStreamGrad1Flyer)" stroke-width="2.2" opacity="0.30"/>
  <path d="M -60 1460 C 340 1370 660 1580 980 1510 C 1290 1440 1410 1580 1540 1520" fill="none" stroke="url(#zahaStreamGrad2Flyer)" stroke-width="2.2" opacity="0.28"/>


  <!-- =================================================================== -->
  <!-- TOP HEADER & DUAL ECOSYSTEM PILLARS (Y: 20 to 180)                  -->
  <!-- =================================================================== -->
  <g transform="translate(740, 24)">
    <!-- Tech Showcase Badge -->
    <rect x="-190" y="0" width="380" height="36" rx="18" fill="#ffffff" stroke="#7c3aed" stroke-width="1.8" filter="url(#softCardShadowFlyer)"/>
    <circle cx="-150" cy="18" r="5" fill="#7c3aed"/>
    <text x="-130" y="24" fill="#581c87" class="mono" font-size="13" font-weight="800" letter-spacing="2.5">SOUTH AFRICA TECH SHOWCASE</text>

    <!-- Master Title -->
    <text x="0" y="78" fill="#0f172a" class="sans" font-size="44" font-weight="900" letter-spacing="1.2" text-anchor="middle">THE SPUTNIK TECH ECOSYSTEM</text>
    <text x="0" y="108" fill="#581c87" class="sans" font-size="17" font-weight="700" letter-spacing="0.4" text-anchor="middle">Connecting Campus Marketplace Commerce with Enterprise Cloud Software</text>

    <!-- Split Indicator Bar -->
    <rect x="-700" y="132" width="665" height="34" rx="17" fill="#ffffff" stroke="#7c3aed" stroke-width="1.6" filter="url(#softCardShadowFlyer)"/>
    <circle cx="-675" cy="149" r="4.5" fill="#7c3aed"/>
    <text x="-367" y="155" fill="#581c87" class="mono" font-size="12" font-weight="800" letter-spacing="2" text-anchor="middle">◀ CONSUMER &amp; CAMPUS MOBILE LABS</text>

    <rect x="35" y="132" width="665" height="34" rx="17" fill="#ffffff" stroke="#8b5cf6" stroke-width="1.6" filter="url(#softCardShadowFlyer)"/>
    <circle cx="670" cy="149" r="4.5" fill="#8b5cf6"/>
    <text x="367" y="155" fill="#581c87" class="mono" font-size="12" font-weight="800" letter-spacing="2" text-anchor="middle">ENTERPRISE SAAS &amp; ACADEMY ▶</text>
  </g>


  <!-- =================================================================== -->
  <!-- LEFT COLUMN: SPUTNIK TECH GROUP & TRADEY BAY APP (X: 40 - 705)       -->
  <!-- Transform Y: 195. Total Height: 1735px (terminates at Y: 1930)       -->
  <!-- =================================================================== -->
  <g transform="translate(40, 195)">

    <!-- Company Branding Header with Real Sputnik Tech Logo (Y: 0 to 52) -->
    <g transform="translate(0, 0)">
      <rect x="0" y="0" width="52" height="52" rx="13" fill="#ffffff" stroke="#d8b4fe" stroke-width="1.4" filter="url(#softCardShadowFlyer)"/>
      <image href="{sputnik_tech_logo}" x="4" y="4" width="44" height="44" preserveAspectRatio="xMidYMid meet"/>
      <text x="66" y="24" fill="#0f172a" class="sans" font-size="23" font-weight="900" letter-spacing="1">SPUTNIK TECH GROUP</text>
      <text x="66" y="43" fill="#7c3aed" class="mono" font-size="11.5" font-weight="800" letter-spacing="2.2">CONSUMER &amp; MOBILE INNOVATION</text>
    </g>

    <!-- HERO CARD: TRADEY BAY MOBILE APP (Y: 60 to 525, Height: 465) -->
    <g transform="translate(0, 60)">
      <rect x="0" y="0" width="665" height="465" rx="22" fill="#ffffff" stroke="#8b5cf6" stroke-width="2" filter="url(#deepCardShadowFlyer)"/>
      
      <!-- App Header Bar inside Hero Card -->
      <g transform="translate(16, 12)">
        <image href="{tradeybay_primary_logo}" x="0" y="0" width="34" height="34" preserveAspectRatio="xMidYMid meet"/>
        <text x="44" y="22" fill="#581c87" class="mono" font-size="11.5" font-weight="800" letter-spacing="1.5">CAMPUS SUPER APP</text>
        
        <rect x="495" y="4" width="138" height="26" rx="13" fill="#ecfdf5" stroke="#10b981" stroke-width="1.2"/>
        <circle cx="510" cy="17" r="4" fill="#10b981"/>
        <text x="522" y="21" fill="#065f46" class="mono" font-size="11" font-weight="800">LIVE v2.0.4+31</text>
      </g>

      <!-- DUAL NOTCHLESS FULLSCREEN PHONE MOCKUPS (Side-by-Side) -->
      <!-- Light Mode Mock Phone (Left) -->
      <g transform="translate(32, 60)" filter="url(#phoneShadowFlyer)">
        <rect x="0" y="0" width="285" height="385" rx="24" fill="#1e1b4b" stroke="#7c3aed" stroke-width="2.5"/>
        <rect x="4" y="4" width="277" height="377" rx="21" fill="#000000"/>
        <!-- Notchless Screen -->
        <g transform="translate(4, 4)" clip-path="url(#phoneScreenClipFlyerLight)">
          <image href="{tradeybay_light_screenshot}" x="0" y="0" width="277" height="372" preserveAspectRatio="xMidYMid slice"/>
        </g>
        <!-- Phone Top Speaker Slit & Glare -->
        <path d="M 4 4 L 100 4 L 4 200 Z" fill="#ffffff" opacity="0.06"/>
        <rect x="110" y="373" width="65" height="3" rx="1.5" fill="#a855f7" opacity="0.8"/>
      </g>

      <!-- OLED Dark Mode Mock Phone (Right) -->
      <g transform="translate(348, 60)" filter="url(#phoneShadowFlyer)">
        <rect x="0" y="0" width="285" height="385" rx="24" fill="#1e1b4b" stroke="#8b5cf6" stroke-width="2.5"/>
        <rect x="4" y="4" width="277" height="377" rx="21" fill="#000000"/>
        <!-- Notchless Screen -->
        <g transform="translate(4, 4)" clip-path="url(#phoneScreenClipFlyerDark)">
          <image href="{tradeybay_dark_screenshot}" x="0" y="0" width="277" height="372" preserveAspectRatio="xMidYMid slice"/>
        </g>
        <path d="M 4 4 L 100 4 L 4 200 Z" fill="#ffffff" opacity="0.05"/>
        <rect x="110" y="373" width="65" height="3" rx="1.5" fill="#a855f7" opacity="0.8"/>
      </g>
    </g>

    <!-- POINT & EXPLAIN FEATURE CARDS (Y: 540 to 1060, Height: 520) -->
    <g transform="translate(0, 540)">
      <rect x="0" y="0" width="370" height="28" rx="14" fill="#faf5ff" stroke="#d8b4fe" stroke-width="1.2"/>
      <text x="185" y="19" fill="#6b21a8" class="mono" font-size="12" font-weight="800" letter-spacing="1.5" text-anchor="middle">OFFICIAL TRADEY BAY PLATFORM PILLARS</text>

      <!-- Point 1: Classified Ads & Real-Time Auctions -->
      <g transform="translate(0, 36)">
        <rect width="665" height="106" rx="16" fill="#ffffff" stroke="#e9d5ff" stroke-width="1.2" filter="url(#softCardShadowFlyer)"/>
        <rect x="14" y="18" width="70" height="70" rx="14" fill="#faf5ff"/>
        <use href="#icon-laptop-f" x="25" y="28"/>
        <text x="98" y="36" fill="#0f172a" class="sans" font-size="15.5" font-weight="800">1. Classified Ads &amp; Real-Time Auctions</text>
        <text x="98" y="58" fill="#475569" class="sans" font-size="12.5">Free listings across Vehicles, Solar, Tech &amp; Dorm gear.</text>
        <text x="98" y="79" fill="#7c3aed" class="sans" font-size="12" font-weight="700">Sub-100ms SignalR live bidding with 60s anti-snipe extension.</text>
      </g>

      <!-- Point 2: Seller & Business Storefronts -->
      <g transform="translate(0, 154)">
        <rect width="665" height="106" rx="16" fill="#ffffff" stroke="#e9d5ff" stroke-width="1.2" filter="url(#softCardShadowFlyer)"/>
        <rect x="14" y="18" width="70" height="70" rx="14" fill="#faf5ff"/>
        <use href="#icon-storefront-f" x="25" y="28"/>
        <text x="98" y="36" fill="#0f172a" class="sans" font-size="15.5" font-weight="800">2. Branded Seller &amp; Business Storefronts</text>
        <text x="98" y="58" fill="#475569" class="sans" font-size="12.5">Dedicated digital showrooms for private sellers and CIPC registered stores</text>
        <text x="98" y="79" fill="#6b21a8" class="sans" font-size="12" font-weight="700">with verified vendor badges, product carousels &amp; in-store search.</text>
      </g>

      <!-- Point 3: Interactive Maps & Split View -->
      <g transform="translate(0, 272)">
        <rect width="665" height="106" rx="16" fill="#ffffff" stroke="#e9d5ff" stroke-width="1.2" filter="url(#softCardShadowFlyer)"/>
        <rect x="14" y="18" width="70" height="70" rx="14" fill="#faf5ff"/>
        <use href="#icon-map-radar-f" x="25" y="28"/>
        <text x="98" y="36" fill="#0f172a" class="sans" font-size="15.5" font-weight="800">3. Interactive Split-View Geospatial Maps</text>
        <text x="98" y="58" fill="#475569" class="sans" font-size="12.5">Switch between card grid and live Google Map view with clustered pins</text>
        <text x="98" y="79" fill="#7c3aed" class="sans" font-size="12" font-weight="700">and bounding-box search-as-you-move across South African metros.</text>
      </g>

      <!-- Point 4: Jobs & Native AI ATS Resume Builder -->
      <g transform="translate(0, 390)">
        <rect width="665" height="106" rx="16" fill="#ffffff" stroke="#e9d5ff" stroke-width="1.2" filter="url(#softCardShadowFlyer)"/>
        <rect x="14" y="18" width="70" height="70" rx="14" fill="#faf5ff"/>
        <use href="#icon-ats-resume-f" x="25" y="28"/>
        <text x="98" y="36" fill="#0f172a" class="sans" font-size="15.5" font-weight="800">4. Jobs Network &amp; Native AI ATS Resume Builder</text>
        <text x="98" y="58" fill="#475569" class="sans" font-size="12.5">Built-in ATS resume creator with 4 templates &amp; vector PDF export.</text>
        <text x="98" y="79" fill="#b45309" class="sans" font-size="12" font-weight="700">Algorithmic vacancy matching with 1-tap direct applications.</text>
      </g>
    </g>

    <!-- SCANNABLE QR CALL-TO-ACTION CARD (Y: 1075 to 1735, Height: 660) -->
    <!-- Terminus: 195 + 1735 = 1930 (Clean 15px clearance before Y: 1945 footer) -->
    <g transform="translate(0, 1075)">
      <rect width="665" height="660" rx="22" fill="url(#tbLightCardGradFlyer)" stroke="#7c3aed" stroke-width="2.5" filter="url(#deepCardShadowFlyer)"/>

      <!-- Header Strip -->
      <rect width="665" height="62" rx="22" fill="#f5f3ff"/>
      <path d="M 0 62 L 665 62" stroke="#e9d5ff" stroke-width="1.5"/>

      <text x="332" y="27" fill="#6b21a8" class="mono" font-size="13" font-weight="800" letter-spacing="1.5" text-anchor="middle">GET TRADEY BAY TODAY (v2.0.4+31)</text>
      <text x="332" y="50" fill="#0f172a" class="sans" font-size="19" font-weight="900" text-anchor="middle">Scan Camera to Install on Android &amp; iOS</text>

      <!-- PURE WHITE HIGH-CONTRAST QR CODE CANVAS -->
      <g transform="translate(217, 76)">
        <rect width="230" height="230" rx="18" fill="#ffffff" stroke="#c084fc" stroke-width="2.5" filter="url(#softCardShadowFlyer)"/>
        <!-- Corner Targeting Guides -->
        <path d="M 8 22 L 8 8 L 22 8" fill="none" stroke="#7c3aed" stroke-width="3" stroke-linecap="round"/>
        <path d="M 222 22 L 222 8 L 208 8" fill="none" stroke="#7c3aed" stroke-width="3" stroke-linecap="round"/>
        <path d="M 8 208 L 8 222 L 22 222" fill="none" stroke="#7c3aed" stroke-width="3" stroke-linecap="round"/>
        <path d="M 222 208 L 222 222 L 208 222" fill="none" stroke="#7c3aed" stroke-width="3" stroke-linecap="round"/>

        <!-- Inlined Vector QR Path (49.2 x 49.2 scaled to 200x200, offset 15, 15) -->
        <g transform="translate(15, 15) scale(4.065)">
          <use href="#qr-path-tradeybay-f" fill="#0f172a"/>
        </g>
      </g>

      <!-- REAL OFFICIAL APP STORE & GOOGLE PLAY BADGES -->
      <g transform="translate(142, 322)">
        <use href="#badge-google-play-flyer" x="0" y="0"/>
        <use href="#badge-app-store-flyer" x="200" y="0"/>
      </g>

      <!-- POPIA COMPLIANT & IN-COUNTRY HOSTED -->
      <g transform="translate(102, 388)">
        <rect width="460" height="40" rx="20" fill="#ede9fe" stroke="#8b5cf6" stroke-width="1.5"/>
        <text x="230" y="25" fill="#4c1d95" class="mono" font-size="12.5" font-weight="800" text-anchor="middle">🛡️  100% POPIA COMPLIANT &amp; IN-COUNTRY HOSTED</text>
      </g>

      <!-- Value Proposition Copy -->
      <g transform="translate(30, 448)">
        <text x="302" y="0" fill="#581c87" class="sans" font-size="15.5" font-weight="900" text-anchor="middle">South Africa's Premier Campus Commerce Super App</text>
        <text x="302" y="24" fill="#475569" class="sans" font-size="13" text-anchor="middle">Empowering university students, local entrepreneurs &amp; accredited merchants</text>
        <text x="302" y="44" fill="#475569" class="sans" font-size="13" text-anchor="middle">with zero listing fees, direct buyer-seller chat and verified student identities.</text>
      </g>

      <!-- Corporate Web link button -->
      <g transform="translate(142, 516)">
        <rect width="380" height="44" rx="16" fill="#ffffff" stroke="#7c3aed" stroke-width="2" filter="url(#softCardShadowFlyer)"/>
        <text x="190" y="28" fill="#6b21a8" class="mono" font-size="14.5" font-weight="800" letter-spacing="1" text-anchor="middle">🌐 sputniktechgroup.com</text>
      </g>

      <!-- Support Contact -->
      <text x="332" y="594" fill="#64748b" class="mono" font-size="12.5" font-weight="700" text-anchor="middle">Direct Developer Inquiries: info@sputniktechgroup.com</text>
    </g>

  </g>


  <!-- =================================================================== -->
  <!-- RIGHT COLUMN: SPUTNIK DEVS STUDIO (SAAS & ACADEMY) (X: 775 - 1440)  -->
  <!-- Transform Y: 195. Total Height: 1735px (terminates at Y: 1930)       -->
  <!-- =================================================================== -->
  <g transform="translate(775, 195)">

    <!-- Company Branding Header with Real Sputnik Devs Logo (Y: 0 to 52) -->
    <g transform="translate(0, 0)">
      <rect x="0" y="0" width="52" height="52" rx="13" fill="#ffffff" stroke="#d8b4fe" stroke-width="1.4" filter="url(#softCardShadowFlyer)"/>
      <image href="{sputnik_devs_logo}" x="4" y="4" width="44" height="44" preserveAspectRatio="xMidYMid meet"/>
      <text x="66" y="24" fill="#0f172a" class="sans" font-size="23" font-weight="900" letter-spacing="1">SPUTNIK DEVS STUDIO</text>
      <text x="66" y="43" fill="#7c3aed" class="mono" font-size="11.5" font-weight="800" letter-spacing="2.2">ENTERPRISE SAAS &amp; ACADEMY</text>
    </g>

    <!-- CARD 1: STUDENT RESIDENCE MANAGEMENT & THE UNIVERSITY HUB (Y: 60 to 525, Height: 465) -->
    <g transform="translate(0, 60)">
      <rect width="665" height="465" rx="22" fill="#ffffff" stroke="#7c3aed" stroke-width="2" filter="url(#softCardShadowFlyer)"/>
      
      <!-- Card Header -->
      <rect width="665" height="58" rx="22" fill="#faf5ff"/>
      <path d="M 0 58 L 665 58" stroke="#e9d5ff" stroke-width="1"/>
      
      <g transform="translate(16, 11)">
        <use href="#icon-hostel-f" x="0" y="0"/>
        <use href="#icon-unihub-f" x="44" y="0"/>
      </g>
      <text x="104" y="25" fill="#0f172a" class="sans" font-size="15" font-weight="900">Student Res Management</text>
      <text x="104" y="42" fill="#7c3aed" class="mono" font-size="9.5" font-weight="800" letter-spacing="0.5">&amp; THE UNIVERSITY HUB PLATFORM</text>
      
      <rect x="525" y="14" width="124" height="28" rx="14" fill="#f3e8ff" stroke="#7c3aed" stroke-width="1.2"/>
      <text x="587" y="32" fill="#581c87" class="mono" font-size="10" font-weight="800" text-anchor="middle">CAMPUS B2B</text>

      <!-- 4 Pillars -->
      <g transform="translate(20, 70)">
        <text x="0" y="11" fill="#581c87" class="mono" font-size="10.5" font-weight="800" letter-spacing="1">INTEGRATED HIGHER ED &amp; RESIDENCE ECOSYSTEM:</text>
        
        <!-- Pillar 1 -->
        <g transform="translate(0, 20)">
          <circle cx="8" cy="8" r="4" fill="#7c3aed"/>
          <text x="22" y="11" fill="#0f172a" class="sans" font-size="13" font-weight="800">Hostel SRMS (Residence Operators &amp; Landlords)</text>
          <text x="22" y="26" fill="#475569" class="sans" font-size="11">Automated bed allocations, digital lease signing &amp; room inventory checks.</text>
          <text x="22" y="38" fill="#7c3aed" class="sans" font-size="10.5" font-weight="700">6 Portals: Student, Owner, Property Manager, Catering, Admin, Maintenance.</text>
        </g>

        <!-- Pillar 2 -->
        <g transform="translate(0, 68)">
          <circle cx="8" cy="8" r="4" fill="#7c3aed"/>
          <text x="22" y="11" fill="#0f172a" class="sans" font-size="13" font-weight="800">The University Hub (Higher Education Institutions)</text>
          <text x="22" y="26" fill="#475569" class="sans" font-size="11">AI smart allocation matching verified student cohorts to accredited residences.</text>
          <text x="22" y="38" fill="#7c3aed" class="sans" font-size="10.5" font-weight="700">Central command centre for check-ins, NSFAS/sBux tracking &amp; DHET compliance.</text>
        </g>

        <!-- Pillar 3 -->
        <g transform="translate(0, 116)">
          <circle cx="8" cy="8" r="4" fill="#7c3aed"/>
          <text x="22" y="11" fill="#0f172a" class="sans" font-size="13" font-weight="800">Biometric Gate Turnstiles &amp; Interconnected REST API</text>
          <text x="22" y="26" fill="#475569" class="sans" font-size="11">Hardware turnstile integrations, live student presence &amp; HMAC-signed webhooks.</text>
          <text x="22" y="38" fill="#059669" class="sans" font-size="10.5" font-weight="700">Auto-provisions students into SRMS; live status flows back to University Hub.</text>
        </g>

        <!-- Pillar 4 -->
        <g transform="translate(0, 164)">
          <circle cx="8" cy="8" r="4" fill="#7c3aed"/>
          <text x="22" y="11" fill="#0f172a" class="sans" font-size="13" font-weight="800">Split Bursary Invoicing &amp; Emergency SOS Alerts</text>
          <text x="22" y="26" fill="#475569" class="sans" font-size="11">Automated student statements, split bursary funding &amp; deposit reconciliation.</text>
          <text x="22" y="38" fill="#b45309" class="sans" font-size="10.5" font-weight="700">Real-time emergency broadcast alerts &amp; SLA maintenance escalation.</text>
        </g>

        <!-- Connectivity Strip Banner -->
        <g transform="translate(0, 214)">
          <rect width="625" height="26" rx="8" fill="#f5f3ff" stroke="#c084fc" stroke-width="1"/>
          <text x="312" y="18" fill="#6b21a8" class="mono" font-size="9.5" font-weight="800" text-anchor="middle">⚡ 100% SYNCHRONIZED CLOUD ARCHITECTURE BETWEEN CAMPUS &amp; RESIDENCES</text>
        </g>

        <!-- DUAL QR CODES (SRMS & UniHub) -->
        <g transform="translate(0, 252)">
          <rect width="625" height="130" rx="14" fill="#faf5ff" stroke="#c084fc" stroke-width="1.2"/>
          <line x1="312" y1="0" x2="312" y2="130" stroke="#e9d5ff" stroke-width="1.2"/>

          <!-- Left QR: SRMS -->
          <g transform="translate(14, 14)">
            <rect width="68" height="68" rx="8" fill="#ffffff" stroke="#c084fc" stroke-width="1.2"/>
            <g transform="translate(5, 5) scale(1.42)">
              <use href="#qr-path-srms-f" fill="#0f172a"/>
            </g>
            <text x="82" y="22" fill="#0f172a" class="sans" font-size="14" font-weight="800">Hostel SRMS</text>
            <text x="82" y="39" fill="#7c3aed" class="mono" font-size="9.5" font-weight="700">sputnikdevs.com</text>
            <text x="82" y="53" fill="#7c3aed" class="mono" font-size="9.5" font-weight="700">/products/hostel</text>
            <rect x="0" y="78" width="284" height="26" rx="6" fill="#ffffff" stroke="#d8b4fe" stroke-width="1"/>
            <text x="142" y="95" fill="#581c87" class="sans" font-size="10.5" font-weight="700" text-anchor="middle">Scan for Res Manager Demo ➔</text>
          </g>

          <!-- Right QR: University Hub -->
          <g transform="translate(326, 14)">
            <rect width="68" height="68" rx="8" fill="#ffffff" stroke="#c084fc" stroke-width="1.2"/>
            <g transform="translate(5, 5) scale(1.26)">
              <use href="#qr-path-unihub-f" fill="#0f172a"/>
            </g>
            <text x="82" y="22" fill="#0f172a" class="sans" font-size="14" font-weight="800">University Hub</text>
            <text x="82" y="39" fill="#7c3aed" class="mono" font-size="9.5" font-weight="700">sputnikdevs.com</text>
            <text x="82" y="53" fill="#7c3aed" class="mono" font-size="9.5" font-weight="700">/products/universityhub</text>
            <rect x="0" y="78" width="284" height="26" rx="6" fill="#ffffff" stroke="#d8b4fe" stroke-width="1"/>
            <text x="142" y="95" fill="#581c87" class="sans" font-size="10.5" font-weight="700" text-anchor="middle">Scan for Institution Portal ➔</text>
          </g>
        </g>
      </g>
    </g>

    <!-- CARD 2: SHOPNIK E-COMMERCE SAAS (Y: 540 to 1060, Height: 520) -->
    <g transform="translate(0, 540)">
      <rect width="665" height="520" rx="22" fill="#ffffff" stroke="#8b5cf6" stroke-width="2" filter="url(#softCardShadowFlyer)"/>
      
      <!-- Header -->
      <rect width="665" height="58" rx="22" fill="#fdf4ff"/>
      <path d="M 0 58 L 665 58" stroke="#f0abfc" stroke-width="1"/>
      
      <image href="{shopnik_logo}" x="16" y="10" width="135" height="38" preserveAspectRatio="xMidYMid meet"/>
      
      <rect x="525" y="14" width="124" height="28" rx="14" fill="#faf5ff" stroke="#c084fc" stroke-width="1.2"/>
      <text x="587" y="32" fill="#6b21a8" class="mono" font-size="10" font-weight="800" text-anchor="middle">0% COMMISSION</text>

      <!-- 5 Value Pillars -->
      <g transform="translate(20, 68)">
        <text x="0" y="11" fill="#701a75" class="mono" font-size="10.5" font-weight="800" letter-spacing="1">WHY SA MERCHANTS LAUNCH WITH SHOPNIK:</text>
        
        <!-- Pillar 1 -->
        <g transform="translate(0, 20)">
          <circle cx="8" cy="8" r="4" fill="#7c3aed"/>
          <text x="22" y="11" fill="#0f172a" class="sans" font-size="13" font-weight="800">Day-1 SA Payments &amp; 0% Platform Commission</text>
          <text x="22" y="26" fill="#475569" class="sans" font-size="11">Pre-integrated payment gateways: Paystack &amp; PayFast with instant activation.</text>
          <text x="22" y="38" fill="#7c3aed" class="sans" font-size="10.5" font-weight="700">Merchant-configurable Cash on Delivery (COD) &amp; In-Store Collection.</text>
        </g>

        <!-- Pillar 2 -->
        <g transform="translate(0, 68)">
          <circle cx="8" cy="8" r="4" fill="#7c3aed"/>
          <text x="22" y="11" fill="#0f172a" class="sans" font-size="13" font-weight="800">Rich Product Catalog &amp; Multi-Variant Matrices</text>
          <text x="22" y="26" fill="#475569" class="sans" font-size="11">Color swatches, size tiers, bundle discounts &amp; real-time inventory tracking.</text>
          <text x="22" y="38" fill="#7c3aed" class="sans" font-size="10.5" font-weight="700">Starter (R349/mo), Professional (R699/mo) &amp; Enterprise with live customizer.</text>
        </g>

        <!-- Pillar 3 -->
        <g transform="translate(0, 116)">
          <circle cx="8" cy="8" r="4" fill="#7c3aed"/>
          <text x="22" y="11" fill="#0f172a" class="sans" font-size="13" font-weight="800">Store Management Dashboard &amp; Coupons</text>
          <text x="22" y="26" fill="#475569" class="sans" font-size="11">Real-time sales graphs, order processing, stock alerts &amp; customer accounts.</text>
          <text x="22" y="38" fill="#059669" class="sans" font-size="10.5" font-weight="700">Discount coupon engine, automated order emails &amp; role-based admin access.</text>
        </g>

        <!-- Pillar 4 -->
        <g transform="translate(0, 164)">
          <circle cx="8" cy="8" r="4" fill="#7c3aed"/>
          <text x="22" y="11" fill="#0f172a" class="sans" font-size="13" font-weight="800">In-Country Oracle Cloud SA Hosting (Johannesburg)</text>
          <text x="22" y="26" fill="#475569" class="sans" font-size="11">Hosted on Oracle Cloud South Africa servers for blazing sub-second response.</text>
          <text x="22" y="38" fill="#059669" class="sans" font-size="10.5" font-weight="700">Engineered with .NET 10 &amp; Cloud Redis. Handles high-traffic flash sales.</text>
        </g>

        <!-- Pillar 5 -->
        <g transform="translate(0, 212)">
          <circle cx="8" cy="8" r="4" fill="#7c3aed"/>
          <text x="22" y="11" fill="#0f172a" class="sans" font-size="13" font-weight="800">AI Recommendations &amp; Customer Reviews</text>
          <text x="22" y="26" fill="#475569" class="sans" font-size="11">Built-in AI product recommendation engine &amp; AI customer review summaries.</text>
          <text x="22" y="38" fill="#7c3aed" class="sans" font-size="10.5" font-weight="700">Verified buyer star ratings, customer wishlists &amp; marketing email tools.</text>
        </g>

        <!-- Expanded Scannable Shopnik QR Block -->
        <g transform="translate(0, 268)">
          <rect width="625" height="152" rx="16" fill="#faf5ff" stroke="#8b5cf6" stroke-width="1.2"/>
          <g transform="translate(18, 16)">
            <rect width="120" height="120" rx="12" fill="#ffffff" stroke="#c084fc" stroke-width="1.2"/>
            <g transform="translate(7, 7) scale(2.35)">
              <use href="#qr-path-shopnik-f" fill="#0f172a"/>
            </g>
          </g>
          <g transform="translate(158, 22)">
            <text x="0" y="15" fill="#0f172a" class="sans" font-size="16.5" font-weight="900">Launch Your Online Store Today</text>
            <text x="0" y="37" fill="#475569" class="sans" font-size="13">Plans start at R349/month • 0% platform sales cut</text>
            <text x="0" y="56" fill="#7c3aed" class="mono" font-size="11.5" font-weight="800">sputnikdevs.com/products/ecommerce</text>
            
            <rect x="0" y="68" width="340" height="36" rx="18" fill="#7c3aed"/>
            <text x="170" y="91" fill="#ffffff" class="sans" font-size="12.5" font-weight="800" text-anchor="middle">Scan Camera to Launch on Shopnik ➔</text>
          </g>
        </g>
      </g>
    </g>

    <!-- CARD 3: SPUTNIK DEVS ACADEMY — PRODUCTION DISCIPLINES (Y: 1075 to 1735, Height: 660) -->
    <!-- Terminus: 195 + 1735 = 1930 (Clean 15px clearance before Y: 1945 footer) -->
    <g transform="translate(0, 1075)">
      <rect width="665" height="660" rx="22" fill="#ffffff" stroke="#d97706" stroke-width="2.5" filter="url(#deepCardShadowFlyer)"/>

      <!-- Gold Banner Header -->
      <rect width="665" height="62" rx="22" fill="#fef3c7"/>
      <path d="M 0 62 L 665 62" stroke="#fcd34d" stroke-width="1.5"/>

      <use href="#icon-academy-f" x="16" y="8"/>
      <text x="74" y="27" fill="#0f172a" class="sans" font-size="18.5" font-weight="900">SPUTNIK DEVS ACADEMY</text>
      <text x="74" y="47" fill="#b45309" class="mono" font-size="10.5" font-weight="800" letter-spacing="0.8">ACCREDITED TECH LEARNERSHIPS (WIL)</text>
      
      <rect x="505" y="16" width="144" height="28" rx="14" fill="#d97706"/>
      <text x="577" y="34" fill="#ffffff" class="mono" font-size="10.5" font-weight="900" text-anchor="middle">WE ARE HIRING</text>

      <!-- Hook & Disciplines -->
      <g transform="translate(20, 74)">
        <text x="0" y="15" fill="#0f172a" class="sans" font-size="16" font-weight="900">Calling All IT, CS &amp; Software Students!</text>
        <text x="0" y="34" fill="#334155" class="sans" font-size="12.5">Accelerate your career through hands-on Work-Integrated Learning (WIL).</text>
        <text x="0" y="50" fill="#334155" class="sans" font-size="12.5">Work on real production microservices &amp; apps alongside senior architects.</text>

        <!-- Accredited Track Pill -->
        <g transform="translate(0, 60)">
          <rect width="625" height="30" rx="8" fill="#fef3c7" stroke="#f59e0b" stroke-width="1.2"/>
          <text x="312" y="20" fill="#92400e" class="mono" font-size="11.5" font-weight="800" text-anchor="middle">🎓 19-DAY INTENSIVE &amp; 3-MONTH ACCREDITED WIL TRACKS</text>
        </g>

        <!-- 5 Production Disciplines -->
        <g transform="translate(0, 100)">
          <text x="0" y="11" fill="#b45309" class="mono" font-size="10.5" font-weight="800" letter-spacing="1">CORE PRODUCTION DISCIPLINES YOU WILL MASTER:</text>
          
          <!-- 1. Backend -->
          <g transform="translate(0, 18)">
            <rect width="625" height="35" rx="8" fill="#faf5ff" stroke="#c084fc" stroke-width="1"/>
            <rect x="8" y="6" width="22" height="22" rx="4" fill="#7c3aed"/>
            <text x="19" y="21" fill="#ffffff" class="mono" font-size="10.5" font-weight="900" text-anchor="middle">1</text>
            <text x="38" y="15" fill="#0f172a" class="sans" font-size="12" font-weight="800">Backend Systems: REST &amp; gRPC Microservices</text>
            <text x="38" y="28" fill="#6b21a8" class="sans" font-size="10">High-throughput APIs, gRPC binary streaming, SignalR hubs &amp; auth</text>
          </g>

          <!-- 2. Mobile -->
          <g transform="translate(0, 58)">
            <rect width="625" height="35" rx="8" fill="#faf5ff" stroke="#c084fc" stroke-width="1"/>
            <rect x="8" y="6" width="22" height="22" rx="4" fill="#7c3aed"/>
            <text x="19" y="21" fill="#ffffff" class="mono" font-size="10.5" font-weight="900" text-anchor="middle">2</text>
            <text x="38" y="15" fill="#0f172a" class="sans" font-size="12" font-weight="800">Mobile Engineering: Cross-Platform Native Apps</text>
            <text x="38" y="28" fill="#6b21a8" class="sans" font-size="10">Production iOS &amp; Android, state management, offline sync &amp; biometrics</text>
          </g>

          <!-- 3. DevOps -->
          <g transform="translate(0, 98)">
            <rect width="625" height="35" rx="8" fill="#fff7ed" stroke="#fdba74" stroke-width="1"/>
            <rect x="8" y="6" width="22" height="22" rx="4" fill="#ea580c"/>
            <text x="19" y="21" fill="#ffffff" class="mono" font-size="10.5" font-weight="900" text-anchor="middle">3</text>
            <text x="38" y="15" fill="#0f172a" class="sans" font-size="12" font-weight="800">DevOps &amp; Cloud: Automated CI/CD Pipelines</text>
            <text x="38" y="28" fill="#c2410c" class="sans" font-size="10">Automated GitHub Actions, container orchestration &amp; Oracle Cloud SA</text>
          </g>

          <!-- 4. Data -->
          <g transform="translate(0, 138)">
            <rect width="625" height="35" rx="8" fill="#f0fdf4" stroke="#86efac" stroke-width="1"/>
            <rect x="8" y="6" width="22" height="22" rx="4" fill="#16a34a"/>
            <text x="19" y="21" fill="#ffffff" class="mono" font-size="10.5" font-weight="900" text-anchor="middle">4</text>
            <text x="38" y="15" fill="#0f172a" class="sans" font-size="12" font-weight="800">Data Architecture: Enterprise Databases &amp; Caching</text>
            <text x="38" y="28" fill="#15803d" class="sans" font-size="10">High-concurrency PostgreSQL, indexing, ACID transactions &amp; Redis cache</text>
          </g>

          <!-- 5. AI -->
          <g transform="translate(0, 178)">
            <rect width="625" height="35" rx="8" fill="#fefce8" stroke="#fde047" stroke-width="1"/>
            <rect x="8" y="6" width="22" height="22" rx="4" fill="#ca8a04"/>
            <text x="19" y="21" fill="#ffffff" class="mono" font-size="10.5" font-weight="900" text-anchor="middle">5</text>
            <text x="38" y="15" fill="#0f172a" class="sans" font-size="12" font-weight="800">Applied AI: Autonomous AI Agents &amp; Automation</text>
            <text x="38" y="28" fill="#b45309" class="sans" font-size="10">Intelligent LLM tool-calling, agent workflows &amp; ATS ranking algorithms</text>
          </g>
        </g>

        <!-- Big Scannable Academy QR Code Box -->
        <g transform="translate(242, 332)">
          <rect width="140" height="140" rx="14" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5" filter="url(#softCardShadowFlyer)"/>
          <path d="M 6 16 L 6 6 L 16 6" fill="none" stroke="#d97706" stroke-width="2.5" stroke-linecap="round"/>
          <path d="M 134 16 L 134 6 L 124 6" fill="none" stroke="#d97706" stroke-width="2.5" stroke-linecap="round"/>
          <path d="M 6 124 L 6 134 L 16 134" fill="none" stroke="#d97706" stroke-width="2.5" stroke-linecap="round"/>
          <path d="M 134 124 L 134 134 L 124 134" fill="none" stroke="#d97706" stroke-width="2.5" stroke-linecap="round"/>

          <g transform="translate(9, 9) scale(3.08)">
            <use href="#qr-path-academy-f" fill="#0f172a"/>
          </g>
        </g>

        <!-- Callout Banner -->
        <g transform="translate(112, 488)">
          <rect width="400" height="42" rx="14" fill="#d97706" filter="url(#softCardShadowFlyer)"/>
          <text x="200" y="26" fill="#ffffff" class="sans" font-size="13.5" font-weight="900" text-anchor="middle">SCAN TO SUBMIT YOUR CV &amp; PORTFOLIO</text>
        </g>

        <text x="312" y="555" fill="#b45309" class="mono" font-size="12" font-weight="800" letter-spacing="1" text-anchor="middle">🌐 sputnikdevs.com/academy/apply</text>
      </g>
    </g>

  </g>

  <!-- Central Subtle Vertical Divider -->
  <line x1="740" y1="195" x2="740" y2="1930" stroke="#e9d5ff" stroke-width="1.8" stroke-dasharray="6,4"/>
  <circle cx="740" cy="525" r="4.5" fill="#c084fc"/>
  <circle cx="740" cy="1060" r="4.5" fill="#c084fc"/>


  <!-- =================================================================== -->
  <!-- BOTTOM BASE & EXECUTIVE LEADERSHIP ZONE (Y: 1945 to 2085)           -->
  <!-- =================================================================== -->
  <g transform="translate(0, 1945)">
    <rect width="1480" height="140" fill="#fdfcff"/>
    <line x1="0" y1="0" x2="1480" y2="0" stroke="#d8b4fe" stroke-width="1.5"/>

    <!-- Left Footer: Sputnik Tech Group & CEO -->
    <g transform="translate(40, 28)">
      <text x="0" y="0" fill="#0f172a" class="sans" font-size="16" font-weight="900">SPUTNIK TECH GROUP (PTY) LTD</text>
      <text x="0" y="20" fill="#581c87" class="sans" font-size="13" font-weight="800">Takudzwa Mupanesure <tspan fill="#64748b" font-weight="500">— Founder, Chief Executive Officer &amp; Lead Architect</tspan></text>
      <text x="0" y="40" fill="#475569" class="sans" font-size="12">292 Surrey Avenue, Randburg, Johannesburg, 2194 • Direct: takudzwam@sputniktechgroup.com</text>
      <text x="0" y="58" fill="#7c3aed" class="mono" font-size="11.5" font-weight="700">Tel: +27 66 321 5528 | +263 787 015 123 • sputniktechgroup.com</text>
    </g>

    <!-- Center Badge & Leadership Concurrence -->
    <g transform="translate(740, 28)">
      <text x="0" y="0" fill="#7c3aed" class="mono" font-size="11" font-weight="800" letter-spacing="1" text-anchor="middle">IN CONCURRENCE WITH EXECUTIVE LEADERSHIP:</text>
      <text x="0" y="22" fill="#0f172a" class="sans" font-size="13" font-weight="800" text-anchor="middle">Kenneth Takudzwa Katsande <tspan fill="#64748b" font-weight="500">(Director of Operations)</tspan></text>
      <text x="0" y="42" fill="#0f172a" class="sans" font-size="13" font-weight="800" text-anchor="middle">Prince Lwazi Nkiwane <tspan fill="#64748b" font-weight="500">(Director of Growth)</tspan></text>
      <text x="0" y="60" fill="#6b21a8" class="mono" font-size="11" font-weight="700" text-anchor="middle">info@sputniktechgroup.com • info@sputnikdevs.com</text>
    </g>

    <!-- Right Footer: Sputnik Devs Studio -->
    <g transform="translate(1440, 28)">
      <text x="0" y="0" fill="#0f172a" class="sans" font-size="16" font-weight="900" text-anchor="end">SPUTNIK DEVS STUDIO (PTY) LTD</text>
      <text x="0" y="20" fill="#64748b" class="sans" font-size="13" text-anchor="end">Enterprise Cloud, Higher Ed SaaS &amp; Tech Academy</text>
      <text x="0" y="40" fill="#7c3aed" class="mono" font-size="12" font-weight="700" text-anchor="end">sputnikdevs.com • info@sputnikdevs.com</text>
      <text x="0" y="58" fill="#94a3b8" class="mono" font-size="10.5" text-anchor="end">[ A5 HANDHELD FLYER • SOUTH AFRICA TECH SHOWCASE ]</text>
    </g>
  </g>

</svg>
"""
    return svg

def main():
    print("Generating High-Resolution A5 Vector Handheld Print Flyer SVG...")
    svg_content = build_flyer_svg()
    out_path = os.path.join(REPO_ROOT, "designs", "flyer", "flyer-a5.svg")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(svg_content)
    size_kb = os.path.getsize(out_path) / 1024
    print(f"✅ Generated {out_path} ({size_kb:.1f} KB)")

if __name__ == "__main__":
    main()
