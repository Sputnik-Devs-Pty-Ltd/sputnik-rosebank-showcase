#!/usr/bin/env python3
"""
Generate the high-resolution, Zaha Hadid-inspired, light-themed vector Pull-Up Banner (1m x 2m)
for Sputnik Tech Group and Sputnik Devs Studio at the Rosebank Tech Showcase 2026.

Features:
- Real corporate PNG logos embedded via Base64 data URIs (including horizontal Shopnik logo)
- 100% self-contained inlined vector QR codes (zero external resource dependency)
- Zaha Hadid-inspired architectural background with parametric curves and purple streamlines
- Dual notchless, uncropped smartphone mockups displaying full light and dark mode screenshots
- Authentic Google Play & Apple App Store official vector badges
- Dual scannable QR codes for Student Res Management (SRMS) and The University Hub
- Grounded features from codebase: Paystack & PayFast, COD & In-Store Collection, Oracle Cloud SA hosting
- Updated info@sputniktechgroup.com contact email and v2.0.4+31 Tradey Bay release
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

def build_banner_svg():
    # 1. Load real logo and screenshot base64 strings
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

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 1000 2000" width="1000mm" height="2000mm">
  <defs>
    <!-- Background Canvas Gradient (Luminous Light Violet/Purple Tone) -->
    <linearGradient id="bgCanvasGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="30%" stop-color="#fdfcff"/>
      <stop offset="65%" stop-color="#faf5ff"/>
      <stop offset="100%" stop-color="#f3e8ff"/>
    </linearGradient>

    <!-- Zaha Hadid Parametric Purple Ribbon Gradients -->
    <linearGradient id="zahaPurple1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#c084fc"/>
      <stop offset="50%" stop-color="#a855f7"/>
      <stop offset="100%" stop-color="#7c3aed"/>
    </linearGradient>

    <linearGradient id="zahaPurple2" x1="0%" y1="100%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#7c3aed"/>
      <stop offset="50%" stop-color="#8b5cf6"/>
      <stop offset="100%" stop-color="#c084fc"/>
    </linearGradient>

    <linearGradient id="zahaPurple3" x1="100%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#581c87"/>
      <stop offset="50%" stop-color="#7c3aed"/>
      <stop offset="100%" stop-color="#a855f7"/>
    </linearGradient>

    <linearGradient id="stgCardGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1e1b4b"/>
      <stop offset="45%" stop-color="#2e1065"/>
      <stop offset="100%" stop-color="#3b0764"/>
    </linearGradient>

    <!-- Header Gradient Accent -->
    <linearGradient id="headerGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#6b21a8"/>
      <stop offset="50%" stop-color="#7c3aed"/>
      <stop offset="100%" stop-color="#9333ea"/>
    </linearGradient>

    <!-- Central Divider Spine -->
    <linearGradient id="dividerSpine" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#c084fc" stop-opacity="0.3"/>
      <stop offset="15%" stop-color="#7c3aed" stop-opacity="0.8"/>
      <stop offset="50%" stop-color="#6b21a8" stop-opacity="1"/>
      <stop offset="85%" stop-color="#8b5cf6" stop-opacity="0.8"/>
      <stop offset="100%" stop-color="#c084fc" stop-opacity="0.3"/>
    </linearGradient>

    <!-- Card Drop Shadows -->
    <filter id="softCardShadow" x="-10%" y="-10%" width="120%" height="125%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="6" stdDeviation="12" flood-color="#3b0764" flood-opacity="0.06"/>
      <feDropShadow dx="0" dy="2" stdDeviation="4" flood-color="#0f172a" flood-opacity="0.03"/>
    </filter>

    <filter id="deepCardShadow" x="-10%" y="-10%" width="120%" height="125%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="12" stdDeviation="18" flood-color="#3b0764" flood-opacity="0.12"/>
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#0f172a" flood-opacity="0.05"/>
    </filter>

    <filter id="phoneShadow" x="-15%" y="-10%" width="130%" height="125%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="12" stdDeviation="16" flood-color="#581c87" flood-opacity="0.22"/>
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#0f172a" flood-opacity="0.12"/>
    </filter>

    <!-- Notchless Smartphone Screen Clips (Matches Screenshot 540x1133 ratio: 186x394) -->
    <clipPath id="phoneScreenClipLight">
      <rect x="0" y="0" width="186" height="394" rx="12"/>
    </clipPath>

    <clipPath id="phoneScreenClipDark">
      <rect x="0" y="0" width="186" height="394" rx="12"/>
    </clipPath>

    <!-- Subtle Hairline Purple Grid -->
    <pattern id="gridPurpleLight" width="30" height="30" patternUnits="userSpaceOnUse">
      <path d="M 30 0 L 0 0 0 30" fill="none" stroke="#7c3aed" stroke-width="0.5" stroke-opacity="0.06"/>
    </pattern>

    <!-- Reusable QR Paths for Razor-Sharp Vector Rendering -->
    <path id="qr-path-tradeybay" d="{qr_tb}"/>
    <path id="qr-path-academy" d="{qr_acad}"/>
    <path id="qr-path-srms" d="{qr_srms}"/>
    <path id="qr-path-unihub" d="{qr_unihub}"/>
    <path id="qr-path-shopnik" d="{qr_shopnik}"/>

    <!-- =============================================================== -->
    <!-- OFFICIAL APP STORE & GOOGLE PLAY VECTOR BADGES (200x60 Base)    -->
    <!-- =============================================================== -->
    <g id="badge-google-play">
      <rect width="200" height="60" rx="12" fill="#000000" stroke="#475569" stroke-width="1.5"/>
      <g transform="translate(16, 12)">
        <path d="M4.5 3.2L19.8 18.5L4.5 33.8C3.8 33.2 3.4 32.3 3.4 31.1V5.9C3.4 4.7 3.8 3.8 4.5 3.2Z" fill="#00E5FF"/>
        <path d="M25.2 23.9L19.8 18.5L4.5 33.8C5.4 34.7 6.8 35 8.1 34.3L25.2 23.9Z" fill="#FF0043"/>
        <path d="M25.2 13.1L8.1 2.7C6.8 2 5.4 2.3 4.5 3.2L19.8 18.5L25.2 13.1Z" fill="#00F076"/>
        <path d="M31.5 16.7L25.2 13.1L19.8 18.5L25.2 23.9L31.5 20.3C33 19.4 33 17.6 31.5 16.7Z" fill="#FFD600"/>
      </g>
      <text x="60" y="24" fill="#94A3B8" font-family="'Inter', sans-serif" font-size="10" font-weight="600" letter-spacing="1">GET IT ON</text>
      <text x="60" y="45" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="18" font-weight="700">Google Play</text>
    </g>

    <g id="badge-app-store">
      <rect width="200" height="60" rx="12" fill="#000000" stroke="#475569" stroke-width="1.5"/>
      <g transform="translate(18, 14)">
        <path d="M18.8 15.5C18.8 11.8 21.8 9.9 21.9 9.8C20.2 7.3 17.6 7 16.7 6.9C14.5 6.7 12.3 8.2 11.2 8.2C10 8.2 8.3 6.9 6.5 6.9C4.2 6.9 2 8.2 0.9 10.3C-1.5 14.5 0.3 20.8 2.6 24.1C3.7 25.7 5 27.5 6.8 27.4C8.5 27.3 9.2 26.3 11.3 26.3C13.3 26.3 14 27.4 15.8 27.4C17.6 27.4 18.8 25.8 19.9 24.2C21.2 22.3 21.7 20.5 21.8 20.4C21.7 20.3 18.8 19.2 18.8 15.5Z" fill="#FFFFFF"/>
        <path d="M15.4 4.6C16.4 3.4 17.1 1.7 16.9 0C15.4 0.1 13.6 1 12.6 2.2C11.7 3.3 10.9 5 11.2 6.7C12.8 6.8 14.5 5.8 15.4 4.6Z" fill="#FFFFFF"/>
      </g>
      <text x="56" y="22" fill="#c084fc" font-family="'Inter', sans-serif" font-size="9" font-weight="700" letter-spacing="1">COMING SOON ON</text>
      <text x="56" y="44" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="16" font-weight="700">App Store</text>
    </g>

    <!-- =============================================================== -->
    <!-- HIGH-VALUE PRECISION VECTOR ICONS & PRODUCT LOGOS               -->
    <!-- =============================================================== -->

    <!-- 1. Laptop / Tech Classifieds Icon -->
    <g id="icon-laptop">
      <rect x="3" y="27" width="42" height="4" rx="2" fill="#7c3aed"/>
      <path d="M 19 27 L 29 27 L 28 29 L 20 29 Z" fill="#e9d5ff"/>
      <rect x="7" y="6" width="34" height="22" rx="2.5" fill="#1e1b4b" stroke="#7c3aed" stroke-width="1.5"/>
      <rect x="9" y="8" width="30" height="18" rx="1" fill="#f5f3ff"/>
      <line x1="12" y1="12" x2="22" y2="12" stroke="#7c3aed" stroke-width="1.8" stroke-linecap="round"/>
      <line x1="12" y1="16" x2="33" y2="16" stroke="#a855f7" stroke-width="1.4" stroke-linecap="round"/>
      <line x1="12" y1="20" x2="27" y2="20" stroke="#7c3aed" stroke-width="1.4" stroke-linecap="round"/>
      <circle cx="33" cy="12" r="1.5" fill="#10b981"/>
    </g>

    <!-- 2. Branded Storefront Icon -->
    <g id="icon-storefront">
      <path d="M 6 18 L 42 18 L 38 8 L 10 8 Z" fill="#6b21a8"/>
      <polygon points="10,8 14,8 12,18 7,18" fill="#a855f7"/>
      <polygon points="20,8 24,8 23,18 18,18" fill="#a855f7"/>
      <polygon points="30,8 34,8 34,18 29,18" fill="#a855f7"/>
      <path d="M 6 18 Q 10 21 14 18 Q 18 21 22 18 Q 26 21 30 18 Q 34 21 38 18 Q 42 21 42 18" fill="none" stroke="#6b21a8" stroke-width="2"/>
      <rect x="8" y="20" width="32" height="22" rx="1" fill="#ffffff" stroke="#6b21a8" stroke-width="1.8"/>
      <rect x="11" y="23" width="13" height="14" fill="#faf5ff" stroke="#c084fc" stroke-width="1"/>
      <rect x="27" y="23" width="10" height="19" fill="#7c3aed" rx="1"/>
      <circle cx="29" cy="33" r="1" fill="#ffffff"/>
      <circle cx="37" cy="10" r="5" fill="#10b981"/>
      <path d="M 35 10 L 36.5 11.5 L 39.5 8.5" fill="none" stroke="#ffffff" stroke-width="1.2" stroke-linecap="round"/>
    </g>

    <!-- 3. Split-View Maps & Geolocation Radar Icon -->
    <g id="icon-map-radar">
      <polygon points="6,12 17,8 31,12 42,8 42,36 31,40 17,36 6,40" fill="#faf5ff" stroke="#7c3aed" stroke-width="2"/>
      <line x1="17" y1="8" x2="17" y2="36" stroke="#c084fc" stroke-width="1.2" stroke-dasharray="2,2"/>
      <line x1="31" y1="12" x2="31" y2="40" stroke="#c084fc" stroke-width="1.2" stroke-dasharray="2,2"/>
      <circle cx="24" cy="18" r="8" fill="#a855f7" fill-opacity="0.2"/>
      <path d="M 24 10 C 20.5 10 18 12.5 18 16 C 18 21 24 28 24 28 C 24 28 30 21 30 16 C 30 12.5 27.5 10 24 10 Z" fill="#6b21a8"/>
      <circle cx="24" cy="15" r="2.5" fill="#ffffff"/>
    </g>

    <!-- 4. AI ATS Resume & Career Match Icon -->
    <g id="icon-ats-resume">
      <path d="M 10 6 L 28 6 L 38 16 L 38 42 C 38 43.5 36.5 44 35 44 L 10 44 C 8.5 44 7 43.5 7 42 L 7 8 C 7 6.5 8.5 6 10 6 Z" fill="#ffffff" stroke="#7c3aed" stroke-width="2"/>
      <path d="M 28 6 L 28 16 L 38 16 Z" fill="#ede9fe" stroke="#7c3aed" stroke-width="1.5"/>
      <circle cx="15" cy="14" r="3.5" fill="#7c3aed"/>
      <line x1="21" y1="14" x2="27" y2="14" stroke="#7c3aed" stroke-width="1.8" stroke-linecap="round"/>
      <line x1="12" y1="22" x2="33" y2="22" stroke="#a78bfa" stroke-width="1.8" stroke-linecap="round"/>
      <line x1="12" y1="27" x2="31" y2="27" stroke="#cbd5e1" stroke-width="1.8" stroke-linecap="round"/>
      <line x1="12" y1="32" x2="25" y2="32" stroke="#cbd5e1" stroke-width="1.8" stroke-linecap="round"/>
      <path d="M 34 26 Q 34 31 39 31 Q 34 31 34 36 Q 34 31 29 31 Q 34 31 34 26 Z" fill="#d97706"/>
      <circle cx="39" cy="25" r="1.5" fill="#7c3aed"/>
    </g>

    <!-- 5. Real Hostel Icon (From hostel-icon.svg) -->
    <g id="icon-hostel">
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

    <!-- 6. Real University Hub Icon (From university-hub-icon.svg) -->
    <g id="icon-unihub">
      <circle cx="20" cy="20" r="18" fill="#18181b" stroke="#7c3aed" stroke-width="2"/>
      <path d="M 20 11 L 31 16 L 20 21 L 9 16 Z" fill="#a855f7"/>
      <path d="M 13 18 L 13 24 C 13 27 16 29 20 29 C 24 29 27 27 27 24 L 27 18" fill="none" stroke="#f59e0b" stroke-width="1.8" stroke-linecap="round"/>
      <path d="M 29 17 L 31 22 L 30 22 L 32 26" fill="none" stroke="#ffffff" stroke-width="1" stroke-linecap="round"/>
    </g>

    <!-- 7. Sputnik Devs Academy WIL Icon -->
    <g id="icon-academy">
      <polygon points="24,6 44,15 24,23 4,15" fill="#d97706" stroke="#92400e" stroke-width="1.8"/>
      <path d="M 12 19 L 12 28 C 12 34 36 34 36 28 L 36 19" fill="#fef3c7" stroke="#92400e" stroke-width="1.8"/>
      <path d="M 24 15 Q 38 16 39 26 L 37 32" fill="none" stroke="#b45309" stroke-width="1.8" stroke-linecap="round"/>
      <circle cx="37" cy="33" r="1.8" fill="#b45309"/>
      <g transform="translate(13, 33)">
        <path d="M 4 2 L 0 6 L 4 10" fill="none" stroke="#d97706" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
        <line x1="7" y1="11" x2="11" y2="1" stroke="#d97706" stroke-width="2" stroke-linecap="round"/>
        <path d="M 14 2 L 18 6 L 14 10" fill="none" stroke="#d97706" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
      </g>
    </g>
  </defs>

  <style>
    .sans {{ font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }}
    .mono {{ font-family: 'JetBrains Mono', 'Fira Code', monospace; }}
  </style>

  <!-- =================================================================== -->
  <!-- ZAHA HADID PARAMETRIC PURPLE BACKGROUND ARCHITECTURE                -->
  <!-- =================================================================== -->
  <!-- Base Luminous Light Surface -->
  <rect x="0" y="0" width="1000" height="2000" fill="url(#bgCanvasGrad)"/>
  <rect x="0" y="0" width="1000" height="2000" fill="url(#gridPurpleLight)"/>

  <!-- Ambient Luminous Purple Glow Orbs -->
  <circle cx="180" cy="380" r="280" fill="#ede9fe" fill-opacity="0.50"/>
  <circle cx="820" cy="460" r="300" fill="#f3e8ff" fill-opacity="0.55"/>
  <circle cx="200" cy="1380" r="320" fill="#fae8ff" fill-opacity="0.45"/>
  <circle cx="800" cy="1350" r="300" fill="#ede9fe" fill-opacity="0.50"/>

  <!-- Zaha Hadid Sweeping Fluid Ribbons & Spline Waves -->
  <!-- Upper Parametric Wave (Flowing behind Header & Top Cards) -->
  <path d="M -50 140 C 200 60 380 260 620 180 C 840 110 940 240 1050 170 L 1050 490 C 850 560 680 400 440 470 C 220 540 80 410 -50 480 Z" fill="url(#zahaPurple1)" opacity="0.08"/>

  <!-- Mid-Section Parametric Wave (Dynamic Cross-Canvas Ribbon) -->
  <path d="M -50 720 C 180 630 360 810 580 740 C 780 670 890 810 1050 750 L 1050 1050 C 880 1110 720 970 500 1040 C 300 1110 140 980 -50 1060 Z" fill="url(#zahaPurple2)" opacity="0.07"/>

  <!-- Lower Parametric Wave (Swooping behind QR & Academy Cards) -->
  <path d="M -50 1300 C 220 1210 440 1410 680 1340 C 880 1280 960 1420 1050 1370 L 1050 1690 C 860 1750 680 1610 420 1680 C 200 1740 70 1620 -50 1690 Z" fill="url(#zahaPurple3)" opacity="0.07"/>

  <!-- Parametric Streamlines / Architectural Contour Curves -->
  <path d="M -20 190 C 240 110 420 310 650 230 C 860 160 960 290 1020 220" fill="none" stroke="#a855f7" stroke-width="1.8" stroke-opacity="0.25"/>
  <path d="M -20 220 C 240 140 420 340 650 260 C 860 190 960 320 1020 250" fill="none" stroke="#7c3aed" stroke-width="1.2" stroke-opacity="0.20" stroke-dasharray="6,8"/>
  <path d="M -20 780 C 200 700 400 870 620 800 C 820 730 920 860 1020 810" fill="none" stroke="#8b5cf6" stroke-width="1.8" stroke-opacity="0.22"/>
  <path d="M -20 810 C 200 730 400 900 620 830 C 820 760 920 890 1020 840" fill="none" stroke="#c084fc" stroke-width="1.2" stroke-opacity="0.20" stroke-dasharray="8,6"/>
  <path d="M -20 1360 C 240 1280 460 1480 700 1410 C 900 1350 980 1490 1020 1440" fill="none" stroke="#7c3aed" stroke-width="1.8" stroke-opacity="0.22"/>
  <path d="M -20 1390 C 240 1310 460 1510 700 1440 C 900 1380 980 1520 1020 1470" fill="none" stroke="#a855f7" stroke-width="1.2" stroke-opacity="0.18" stroke-dasharray="6,8"/>

  <!-- =================================================================== -->
  <!-- CENTRAL VERTICAL ARCHITECTURAL DIVIDER SPINE (X: 500)               -->
  <!-- =================================================================== -->
  <line x1="500" y1="210" x2="500" y2="1845" stroke="url(#dividerSpine)" stroke-width="3"/>
  <line x1="499" y1="210" x2="499" y2="1845" stroke="#ffffff" stroke-width="0.8"/>

  <!-- Circuit nodes on the central divider -->
  <circle cx="500" cy="220" r="6" fill="#7c3aed" stroke="#ffffff" stroke-width="2"/>
  <circle cx="500" cy="710" r="7" fill="#6b21a8" stroke="#ffffff" stroke-width="2"/>
  <circle cx="500" cy="1150" r="7" fill="#8b5cf6" stroke="#ffffff" stroke-width="2"/>
  <circle cx="500" cy="1835" r="6" fill="#7c3aed" stroke="#ffffff" stroke-width="2"/>

  <!-- Horizontal circuit branch ticks -->
  <path d="M 465 710 L 500 710 L 535 710" stroke="#7c3aed" stroke-width="1.8" stroke-opacity="0.5"/>
  <path d="M 465 1150 L 500 1150 L 535 1150" stroke="#8b5cf6" stroke-width="1.8" stroke-opacity="0.5"/>

  <!-- =================================================================== -->
  <!-- TOP UNIFIED ARCHITECTURAL HEADER (Y: 30 - 195)                      -->
  <!-- =================================================================== -->
  <g transform="translate(500, 32)">
    <!-- Event Badge -->
    <rect x="-195" y="0" width="390" height="34" rx="17" fill="#ffffff" stroke="#7c3aed" stroke-width="1.8" filter="url(#softCardShadow)"/>
    <circle cx="-168" cy="17" r="5" fill="#7c3aed"/>
    <text x="-148" y="22" fill="#581c87" class="mono" font-size="12" font-weight="800" letter-spacing="2">ROSEBANK TECH SHOWCASE 2026</text>

    <!-- Master Title (Deep Slate High Contrast) -->
    <text x="0" y="74" fill="#0f172a" class="sans" font-size="38" font-weight="900" letter-spacing="1" text-anchor="middle">THE SPUTNIK TECH ECOSYSTEM</text>
    <text x="0" y="102" fill="#581c87" class="sans" font-size="15" font-weight="700" letter-spacing="0.3" text-anchor="middle">Connecting Campus Marketplace Commerce with Enterprise Cloud Software</text>

    <!-- Subtitle Split Indicator Bar -->
    <rect x="-445" y="124" width="425" height="30" rx="15" fill="#ffffff" stroke="#7c3aed" stroke-width="1.5" filter="url(#softCardShadow)"/>
    <circle cx="-425" cy="139" r="4" fill="#7c3aed"/>
    <text x="-232" y="144" fill="#581c87" class="mono" font-size="11" font-weight="800" letter-spacing="2" text-anchor="middle">◀ CONSUMER &amp; CAMPUS MOBILE LABS</text>

    <rect x="20" y="124" width="425" height="30" rx="15" fill="#ffffff" stroke="#8b5cf6" stroke-width="1.5" filter="url(#softCardShadow)"/>
    <circle cx="425" cy="139" r="4" fill="#8b5cf6"/>
    <text x="232" y="144" fill="#581c87" class="mono" font-size="11" font-weight="800" letter-spacing="2" text-anchor="middle">ENTERPRISE SAAS &amp; ACADEMY ▶</text>
  </g>


  <!-- =================================================================== -->
  <!-- LEFT COLUMN: SPUTNIK TECH GROUP & TRADEY BAY APP (X: 36 - 468)       -->
  <!-- =================================================================== -->
  <g transform="translate(36, 210)">

    <!-- Company Branding Header with Real Sputnik Tech Logo -->
    <g transform="translate(0, 0)">
      <rect x="0" y="0" width="56" height="56" rx="14" fill="#ffffff" stroke="#d8b4fe" stroke-width="1.2" filter="url(#softCardShadow)"/>
      <image href="{sputnik_tech_logo}" x="4" y="4" width="48" height="48" preserveAspectRatio="xMidYMid meet"/>
      <text x="68" y="24" fill="#0f172a" class="sans" font-size="22" font-weight="900" letter-spacing="1">SPUTNIK TECH GROUP</text>
      <text x="68" y="42" fill="#7c3aed" class="mono" font-size="11" font-weight="800" letter-spacing="2.5">CONSUMER &amp; MOBILE INNOVATION</text>
    </g>

    <!-- HERO CARD: TRADEY BAY MOBILE APP (Y: 64 to 542) -->
    <g transform="translate(0, 64)">
      <!-- Outer Card Frame (Elevated White Surface with Purple Border) -->
      <rect x="0" y="0" width="432" height="478" rx="22" fill="#ffffff" stroke="#8b5cf6" stroke-width="2" filter="url(#deepCardShadow)"/>
      
      <!-- Card Top Bar -->
      <rect x="0" y="0" width="432" height="54" rx="22" fill="#faf5ff"/>
      <path d="M 0 54 L 432 54" stroke="#e9d5ff" stroke-width="1"/>
      
      <!-- Real Tradey Bay Primary Logo in Header -->
      <g transform="translate(14, 8)">
        <image href="{tradeybay_primary_logo}" x="0" y="0" width="130" height="36" preserveAspectRatio="xMinYMid meet"/>
        <text x="140" y="24" fill="#7c3aed" class="mono" font-size="8.5" font-weight="800" letter-spacing="0.5">CAMPUS SUPER APP</text>
      </g>
      <!-- Live Version Badge: v2.0.4+31 -->
      <rect x="306" y="14" width="112" height="26" rx="13" fill="#dcfce7" stroke="#16a34a" stroke-width="1"/>
      <circle cx="320" cy="27" r="3.5" fill="#16a34a"/>
      <text x="364" y="31" fill="#15803d" class="mono" font-size="8.5" font-weight="800" text-anchor="middle">LIVE v2.0.4+31</text>

      <!-- DUAL SMARTPHONE PRODUCTION DEVICE MOCKUPS (Side-by-Side Light & Dark Mode) -->
      <!-- Notchless, Uncropped, Full UI Visible from Top Search Bar to Bottom Nav -->
      <!-- Left Phone: Light Mode Production App -->
      <g id="phone-light-mockup">
        <!-- Phone Outer Chassis (194x402, 4px minimal bezel) -->
        <rect x="14" y="60" width="194" height="404" rx="16" fill="#0f172a" stroke="#cbd5e1" stroke-width="1.5" filter="url(#phoneShadow)"/>
        <!-- Inner Bezel Ring -->
        <rect x="16" y="62" width="190" height="400" rx="14" fill="none" stroke="#e2e8f0" stroke-width="1"/>
        
        <!-- Screen Content (186x394, exactly matching 540x1132 aspect ratio, zero crop) -->
        <g transform="translate(18, 64)" clip-path="url(#phoneScreenClipLight)">
          <image href="{tradeybay_light_screenshot}" x="0" y="0" width="186" height="394" preserveAspectRatio="none"/>
        </g>

        <!-- Hardware Edge Gloss Reflection -->
        <path d="M 18 64 L 110 64 L 18 220 Z" fill="#ffffff" opacity="0.04"/>

        <!-- Sleek Home Indicator Bar -->
        <rect x="81" y="452" width="60" height="3" rx="1.5" fill="#94a3b8" opacity="0.7"/>
      </g>

      <!-- Right Phone: Dark Mode Production App -->
      <g id="phone-dark-mockup">
        <!-- Phone Outer Chassis (194x402, 4px minimal bezel) -->
        <rect x="224" y="60" width="194" height="404" rx="16" fill="#090d16" stroke="#8b5cf6" stroke-width="1.5" filter="url(#phoneShadow)"/>
        <!-- Inner Bezel Ring -->
        <rect x="226" y="62" width="190" height="400" rx="14" fill="none" stroke="#7c3aed" stroke-width="1" stroke-opacity="0.4"/>
        
        <!-- Screen Content (186x394, exactly matching 540x1135 aspect ratio, zero crop) -->
        <g transform="translate(228, 64)" clip-path="url(#phoneScreenClipDark)">
          <image href="{tradeybay_dark_screenshot}" x="0" y="0" width="186" height="394" preserveAspectRatio="none"/>
        </g>

        <!-- Hardware Edge Gloss Reflection -->
        <path d="M 228 64 L 320 64 L 228 220 Z" fill="#ffffff" opacity="0.05"/>

        <!-- Sleek Home Indicator Bar -->
        <rect x="291" y="452" width="60" height="3" rx="1.5" fill="#a855f7" opacity="0.8"/>
      </g>
    </g>

    <!-- POINT & EXPLAIN FEATURE CARDS WITH HIGH-VALUE VECTOR ICONS (Y: 554 to 940) -->
    <g transform="translate(0, 554)">
      <rect x="0" y="0" width="310" height="24" rx="12" fill="#faf5ff" stroke="#d8b4fe" stroke-width="1"/>
      <text x="155" y="16" fill="#6b21a8" class="mono" font-size="11" font-weight="800" letter-spacing="1.5" text-anchor="middle">OFFICIAL TRADEY BAY PLATFORM PILLARS</text>

      <!-- Point 1: Classifieds & Live Digital Auctions -->
      <g transform="translate(0, 30)">
        <rect width="432" height="82" rx="16" fill="#ffffff" stroke="#e9d5ff" stroke-width="1.2" filter="url(#softCardShadow)"/>
        <rect x="12" y="12" width="58" height="58" rx="12" fill="#faf5ff"/>
        <use href="#icon-laptop" x="18" y="18"/>
        <text x="82" y="30" fill="#0f172a" class="sans" font-size="13.5" font-weight="800">1. Classified Ads &amp; Real-Time Auctions</text>
        <text x="82" y="47" fill="#475569" class="sans" font-size="11">Free listings across Vehicles, Solar, Tech &amp; Dorm gear.</text>
        <text x="82" y="63" fill="#7c3aed" class="sans" font-size="10.5" font-weight="700">Sub-100ms SignalR live bidding with 60s anti-snipe extension.</text>
      </g>

      <!-- Point 2: Seller & Business Storefronts -->
      <g transform="translate(0, 120)">
        <rect width="432" height="82" rx="16" fill="#ffffff" stroke="#e9d5ff" stroke-width="1.2" filter="url(#softCardShadow)"/>
        <rect x="12" y="12" width="58" height="58" rx="12" fill="#faf5ff"/>
        <use href="#icon-storefront" x="18" y="18"/>
        <text x="82" y="30" fill="#0f172a" class="sans" font-size="13.5" font-weight="800">2. Branded Seller &amp; Business Storefronts</text>
        <text x="82" y="47" fill="#475569" class="sans" font-size="11">Dedicated digital showrooms for private sellers and CIPC stores</text>
        <text x="82" y="63" fill="#6b21a8" class="sans" font-size="10.5" font-weight="700">with verified vendor badges, product carousels &amp; in-store search.</text>
      </g>

      <!-- Point 3: Interactive Maps & Split View -->
      <g transform="translate(0, 210)">
        <rect width="432" height="82" rx="16" fill="#ffffff" stroke="#e9d5ff" stroke-width="1.2" filter="url(#softCardShadow)"/>
        <rect x="12" y="12" width="58" height="58" rx="12" fill="#faf5ff"/>
        <use href="#icon-map-radar" x="18" y="18"/>
        <text x="82" y="30" fill="#0f172a" class="sans" font-size="13.5" font-weight="800">3. Interactive Split-View Geospatial Maps</text>
        <text x="82" y="47" fill="#475569" class="sans" font-size="11">Switch between card grid and live Google Map view with</text>
        <text x="82" y="63" fill="#7c3aed" class="sans" font-size="10.5" font-weight="700">clustered price pins and bounding box search-as-you-move.</text>
      </g>

      <!-- Point 4: Jobs & Native AI ATS Resume Builder -->
      <g transform="translate(0, 300)">
        <rect width="432" height="82" rx="16" fill="#ffffff" stroke="#e9d5ff" stroke-width="1.2" filter="url(#softCardShadow)"/>
        <rect x="12" y="12" width="58" height="58" rx="12" fill="#faf5ff"/>
        <use href="#icon-ats-resume" x="18" y="18"/>
        <text x="82" y="30" fill="#0f172a" class="sans" font-size="13.5" font-weight="800">4. Jobs Network &amp; Native AI ATS Resume Builder</text>
        <text x="82" y="47" fill="#475569" class="sans" font-size="11">Built-in ATS resume creator with 4 templates &amp; vector PDF export.</text>
        <text x="82" y="63" fill="#b45309" class="sans" font-size="10.5" font-weight="700">Algorithmic vacancy matching with 1-tap direct applications.</text>
      </g>
    </g>

    <!-- SCANNABLE QR CALL-TO-ACTION CARD (HIGH CONTRAST, 100% INLINED VECTOR) (Y: 948 to 1625) -->
    <g transform="translate(0, 948)">
      <!-- Gradient Container Card -->
      <rect width="432" height="677" rx="22" fill="url(#stgCardGrad)" filter="url(#deepCardShadow)"/>
      <rect x="2" y="2" width="428" height="673" rx="20" fill="none" stroke="#a855f7" stroke-width="2"/>

      <text x="216" y="38" fill="#e9d5ff" class="mono" font-size="12" font-weight="800" letter-spacing="2" text-anchor="middle">GET TRADEY BAY TODAY (v2.0.4+31)</text>
      <text x="216" y="64" fill="#ffffff" class="sans" font-size="18" font-weight="900" text-anchor="middle">Scan Camera to Install on Android &amp; iOS</text>

      <!-- PURE WHITE HIGH-CONTRAST QR CODE CANVAS (INLINED VECTOR PATH) -->
      <g transform="translate(106, 82)">
        <rect width="220" height="220" rx="18" fill="#ffffff" stroke="#ffffff" stroke-width="2" filter="url(#softCardShadow)"/>
        <!-- Corner Targeting Guides -->
        <path d="M 6 18 L 6 6 L 18 6" fill="none" stroke="#7c3aed" stroke-width="2.5" stroke-linecap="round"/>
        <path d="M 214 18 L 214 6 L 202 6" fill="none" stroke="#7c3aed" stroke-width="2.5" stroke-linecap="round"/>
        <path d="M 6 202 L 6 214 L 18 214" fill="none" stroke="#7c3aed" stroke-width="2.5" stroke-linecap="round"/>
        <path d="M 214 202 L 214 214 L 202 214" fill="none" stroke="#7c3aed" stroke-width="2.5" stroke-linecap="round"/>

        <!-- Inlined Vector QR Path (49.2 x 49.2 scaled to 192x192, offset 14, 14) -->
        <g transform="translate(14, 14) scale(3.9024)">
          <use href="#qr-path-tradeybay" fill="#0f172a"/>
        </g>
      </g>

      <!-- REAL OFFICIAL APP STORE & GOOGLE PLAY BADGES -->
      <g transform="translate(36, 320)">
        <!-- Google Play Official Vector Badge -->
        <use href="#badge-google-play" x="0" y="0" transform="scale(0.85)"/>
        <!-- Apple App Store Official Vector Badge -->
        <use href="#badge-app-store" x="220" y="0" transform="scale(0.85)"/>
      </g>

      <!-- POPIA COMPLIANT & IN-COUNTRY HOSTED (RATING REMOVED PER USER SPEC) -->
      <g transform="translate(36, 388)">
        <rect width="360" height="36" rx="18" fill="#1e1b4b" stroke="#8b5cf6" stroke-width="1.2"/>
        <text x="180" y="23" fill="#e9d5ff" class="mono" font-size="11" font-weight="800" text-anchor="middle">🛡️  100% POPIA COMPLIANT &amp; IN-COUNTRY HOSTED</text>
      </g>

      <!-- Live Campus Network Note -->
      <text x="216" y="456" fill="#c084fc" class="sans" font-size="13" font-weight="700" text-anchor="middle">South Africa's Premier Campus Commerce Super App</text>
      <text x="216" y="478" fill="#e2e8f0" class="sans" font-size="11.5" text-anchor="middle">Empowering university students, local entrepreneurs &amp; accredited merchants</text>

      <!-- Corporate Web link -->
      <text x="216" y="520" fill="#ffffff" class="mono" font-size="13" font-weight="800" letter-spacing="1" text-anchor="middle">🌐 sputniktechgroup.com</text>
    </g>

  </g>


  <!-- =================================================================== -->
  <!-- RIGHT COLUMN: SPUTNIK DEVS STUDIO (SAAS & ACADEMY) (X: 532 - 964)   -->
  <!-- =================================================================== -->
  <g transform="translate(532, 210)">

    <!-- Company Branding Header with Real Sputnik Devs Logo -->
    <g transform="translate(0, 0)">
      <rect x="0" y="0" width="56" height="56" rx="14" fill="#ffffff" stroke="#d8b4fe" stroke-width="1.2" filter="url(#softCardShadow)"/>
      <image href="{sputnik_devs_logo}" x="4" y="4" width="48" height="48" preserveAspectRatio="xMidYMid meet"/>
      <text x="68" y="24" fill="#0f172a" class="sans" font-size="22" font-weight="900" letter-spacing="1">SPUTNIK DEVS STUDIO</text>
      <text x="68" y="42" fill="#7c3aed" class="mono" font-size="11" font-weight="800" letter-spacing="2.5">ENTERPRISE SAAS &amp; ACADEMY</text>
    </g>

    <!-- CARD 1: STUDENT RESIDENCE MANAGEMENT & THE UNIVERSITY HUB (Y: 64 to 496) -->
    <!-- Well Spaced, Real Logos, Grounded Features, Dual QR Codes -->
    <g transform="translate(0, 64)">
      <rect width="432" height="432" rx="22" fill="#ffffff" stroke="#7c3aed" stroke-width="2" filter="url(#softCardShadow)"/>
      
      <!-- Card Header (62px height, generous spacing, NO header collision) -->
      <rect width="432" height="62" rx="22" fill="#faf5ff"/>
      <path d="M 0 62 L 432 62" stroke="#e9d5ff" stroke-width="1"/>
      
      <!-- Real Logos: Hostel Building & University Hub Mortarboard -->
      <g transform="translate(14, 14)">
        <use href="#icon-hostel" x="0" y="0"/>
        <use href="#icon-unihub" x="42" y="0"/>
      </g>
      <!-- Title & Subtitle cleanly placed with 240px width before badge -->
      <text x="96" y="27" fill="#0f172a" class="sans" font-size="13.5" font-weight="900">Student Res Management</text>
      <text x="96" y="44" fill="#7c3aed" class="mono" font-size="8.5" font-weight="800" letter-spacing="0.5">&amp; THE UNIVERSITY HUB PLATFORM</text>
      
      <!-- Clean Non-Overlapping Campus B2B Badge -->
      <rect x="322" y="16" width="96" height="28" rx="14" fill="#f3e8ff" stroke="#7c3aed" stroke-width="1.2"/>
      <text x="370" y="34" fill="#581c87" class="mono" font-size="9" font-weight="800" text-anchor="middle">CAMPUS B2B</text>

      <!-- Talking Points for Prince & Kenneth to point at -->
      <g transform="translate(16, 74)">
        <text x="0" y="14" fill="#581c87" class="mono" font-size="10" font-weight="800" letter-spacing="1">INTEGRATED HIGHER ED &amp; RESIDENCE ECOSYSTEM:</text>
        
        <!-- Feature 1: Hostel SRMS -->
        <g transform="translate(0, 26)">
          <circle cx="8" cy="8" r="3.5" fill="#7c3aed"/>
          <text x="20" y="12" fill="#0f172a" class="sans" font-size="12.5" font-weight="800">Hostel SRMS (Residence Operators &amp; Landlords)</text>
          <text x="20" y="26" fill="#475569" class="sans" font-size="10.5">Automated bed allocations, digital lease signing &amp; online rent billing.</text>
          <text x="20" y="38" fill="#7c3aed" class="sans" font-size="10" font-weight="700">6 Integrated Portals: Student, Owner, Manager, Catering, Admin, Maintenance.</text>
        </g>

        <!-- Feature 2: University Hub -->
        <g transform="translate(0, 76)">
          <circle cx="8" cy="8" r="3.5" fill="#7c3aed"/>
          <text x="20" y="12" fill="#0f172a" class="sans" font-size="12.5" font-weight="800">The University Hub (Higher Education Institutions)</text>
          <text x="20" y="26" fill="#475569" class="sans" font-size="10.5">AI smart allocation matching student cohorts to accredited residences.</text>
          <text x="20" y="38" fill="#7c3aed" class="sans" font-size="10" font-weight="700">Central command centre for check-ins, NSFAS/sBux tracking &amp; compliance.</text>
        </g>

        <!-- Feature 3: Biometrics & Interconnected API -->
        <g transform="translate(0, 126)">
          <circle cx="8" cy="8" r="3.5" fill="#7c3aed"/>
          <text x="20" y="12" fill="#0f172a" class="sans" font-size="12.5" font-weight="800">Biometric Gate Access &amp; Interconnected Rest API</text>
          <text x="20" y="26" fill="#475569" class="sans" font-size="10.5">Turnstile integration, maintenance SLAs &amp; HMAC-signed webhooks.</text>
          <text x="20" y="38" fill="#059669" class="sans" font-size="10" font-weight="700">Auto-provisions students into SRMS; live status flows back to University Hub.</text>
        </g>

        <!-- DUAL QR CODES: Left for Student Res Management, Right for University Hub -->
        <g transform="translate(0, 180)">
          <rect width="400" height="98" rx="14" fill="#faf5ff" stroke="#c084fc" stroke-width="1.2"/>
          <line x1="200" y1="0" x2="200" y2="98" stroke="#e9d5ff" stroke-width="1"/>

          <!-- Left QR: Student Res Management (SRMS) -->
          <g transform="translate(10, 10)">
            <rect width="48" height="48" rx="8" fill="#ffffff" stroke="#c084fc" stroke-width="1"/>
            <g transform="translate(4, 4) scale(1.01)">
              <use href="#qr-path-srms" fill="#0f172a"/>
            </g>
            <text x="56" y="18" fill="#0f172a" class="sans" font-size="11" font-weight="800">Hostel SRMS</text>
            <text x="56" y="32" fill="#7c3aed" class="mono" font-size="8" font-weight="700">sputnikdevs.com</text>
            <text x="56" y="44" fill="#7c3aed" class="mono" font-size="8" font-weight="700">/products/hostel</text>
            <text x="0" y="66" fill="#64748b" class="sans" font-size="9" font-weight="600">Scan for Res Manager Demo</text>
          </g>

          <!-- Right QR: The University Hub -->
          <g transform="translate(210, 10)">
            <rect width="48" height="48" rx="8" fill="#ffffff" stroke="#c084fc" stroke-width="1"/>
            <g transform="translate(4, 4) scale(0.90)">
              <use href="#qr-path-unihub" fill="#0f172a"/>
            </g>
            <text x="56" y="18" fill="#0f172a" class="sans" font-size="11" font-weight="800">University Hub</text>
            <text x="56" y="32" fill="#7c3aed" class="mono" font-size="8" font-weight="700">sputnikdevs.com</text>
            <text x="56" y="44" fill="#7c3aed" class="mono" font-size="8" font-weight="700">/products/universityhub</text>
            <text x="0" y="66" fill="#64748b" class="sans" font-size="9" font-weight="600">Scan for Institution Portal</text>
          </g>
        </g>
      </g>
    </g>

    <!-- CARD 2: SHOPNIK E-COMMERCE SAAS (Y: 508 to 940) -->
    <!-- Real Horizontal Logo, Grounded Gateways (Paystack, PayFast, COD, Collection), Oracle Cloud SA -->
    <g transform="translate(0, 508)">
      <rect width="432" height="432" rx="22" fill="#ffffff" stroke="#8b5cf6" stroke-width="2" filter="url(#softCardShadow)"/>
      
      <!-- Card Header (62px height, generous spacing, NO header collision) -->
      <rect width="432" height="62" rx="22" fill="#fbf8ff"/>
      <path d="M 0 62 L 432 62" stroke="#e9d5ff" stroke-width="1"/>
      
      <!-- Real Shopnik Horizontal Logo -->
      <image href="{shopnik_logo}" x="14" y="12" width="135" height="38" preserveAspectRatio="xMinYMid meet"/>
      
      <!-- Clean Non-Overlapping 0% Commission Badge -->
      <rect x="298" y="16" width="120" height="28" rx="14" fill="#f3e8ff" stroke="#7c3aed" stroke-width="1.2"/>
      <text x="358" y="34" fill="#581c87" class="mono" font-size="9" font-weight="800" text-anchor="middle">0% COMMISSION</text>

      <!-- Talking Points: Fully Grounded in Codebase -->
      <g transform="translate(16, 74)">
        <text x="0" y="14" fill="#581c87" class="mono" font-size="10" font-weight="800" letter-spacing="1">WHY MERCHANTS LAUNCH WITH SHOPNIK:</text>
        
        <!-- Point 1: Payment Gateways & Cash Options -->
        <g transform="translate(0, 26)">
          <circle cx="8" cy="8" r="3.5" fill="#7c3aed"/>
          <text x="20" y="12" fill="#0f172a" class="sans" font-size="12.5" font-weight="800">Day-1 Payments &amp; 0% Sales Commission</text>
          <text x="20" y="26" fill="#475569" class="sans" font-size="10.5">Pre-integrated payment gateways: Paystack &amp; PayFast.</text>
          <text x="20" y="38" fill="#7c3aed" class="sans" font-size="10" font-weight="700">Merchant-configurable Cash on Delivery (COD) &amp; In-Store Collection.</text>
        </g>

        <!-- Point 2: Rich Catalog & Themes -->
        <g transform="translate(0, 76)">
          <circle cx="8" cy="8" r="3.5" fill="#7c3aed"/>
          <text x="20" y="12" fill="#0f172a" class="sans" font-size="12.5" font-weight="800">Rich Product Catalog &amp; Multi-Variants</text>
          <text x="20" y="26" fill="#475569" class="sans" font-size="10.5">Color swatches, size options, bundle discounts &amp; stock management.</text>
          <text x="20" y="38" fill="#7c3aed" class="sans" font-size="10" font-weight="700">Starter, Professional &amp; Enterprise tiers with live theme customizer.</text>
        </g>

        <!-- Point 3: Oracle Cloud Hosting SA -->
        <g transform="translate(0, 126)">
          <circle cx="8" cy="8" r="3.5" fill="#7c3aed"/>
          <text x="20" y="12" fill="#0f172a" class="sans" font-size="12.5" font-weight="800">In-Country Oracle Cloud SA Hosting (Joburg)</text>
          <text x="20" y="26" fill="#475569" class="sans" font-size="10.5">Hosted on Oracle Cloud South Africa servers for sub-second latency.</text>
          <text x="20" y="38" fill="#059669" class="sans" font-size="10" font-weight="700">Built on .NET 10 &amp; Cloud Redis. Handles high-traffic flash sales.</text>
        </g>

        <!-- Shopnik Scannable QR Block -->
        <g transform="translate(0, 180)">
          <rect width="400" height="52" rx="12" fill="#faf5ff" stroke="#8b5cf6" stroke-width="1.2"/>
          <g transform="translate(8, 6)">
            <rect width="40" height="40" rx="6" fill="#ffffff" stroke="#c084fc" stroke-width="1"/>
            <g transform="translate(2, 2) scale(0.909)">
              <use href="#qr-path-shopnik" fill="#0f172a"/>
            </g>
          </g>
          <text x="58" y="22" fill="#0f172a" class="sans" font-size="11.5" font-weight="800">Scan to Launch Your Shopnik Store • Live in 30 Min</text>
          <text x="58" y="38" fill="#7c3aed" class="mono" font-size="10" font-weight="700">sputnikdevs.com/products/ecommerce</text>
          <text x="372" y="30" fill="#7c3aed" class="sans" font-size="18" font-weight="900">➔</text>
        </g>
      </g>
    </g>

    <!-- CARD 3: SPUTNIK DEVS ACADEMY — LEARNERSHIPS (GOLD & PURPLE CARD) (Y: 948 to 1625) -->
    <g transform="translate(0, 948)">
      <rect width="432" height="677" rx="22" fill="#ffffff" stroke="#d97706" stroke-width="2.5" filter="url(#deepCardShadow)"/>

      <!-- Gold Banner Header -->
      <rect width="432" height="64" rx="22" fill="#fef3c7"/>
      <path d="M 0 64 L 432 64" stroke="#fcd34d" stroke-width="1.5"/>

      <!-- Vector Academy Icon -->
      <use href="#icon-academy" x="12" y="8"/>
      <text x="64" y="28" fill="#0f172a" class="sans" font-size="16" font-weight="900">SPUTNIK DEVS ACADEMY</text>
      <text x="64" y="46" fill="#b45309" class="mono" font-size="9.5" font-weight="800" letter-spacing="0.8">ACCREDITED TECH LEARNERSHIPS (WIL)</text>
      
      <!-- Clean We Are Hiring Badge -->
      <rect x="306" y="18" width="112" height="28" rx="14" fill="#d97706"/>
      <text x="362" y="36" fill="#ffffff" class="mono" font-size="9.5" font-weight="900" text-anchor="middle">WE ARE HIRING</text>

      <!-- Hook for Students -->
      <g transform="translate(20, 82)">
        <text x="0" y="16" fill="#0f172a" class="sans" font-size="16" font-weight="900">Calling All IT, CS &amp; Software Students!</text>
        <text x="0" y="36" fill="#334155" class="sans" font-size="12">Accelerate your tech career with hands-on Work-Integrated</text>
        <text x="0" y="52" fill="#334155" class="sans" font-size="12">Learning (WIL). Build production systems alongside senior engineers.</text>

        <!-- Feature Points -->
        <g transform="translate(0, 68)">
          <rect width="392" height="42" rx="10" fill="#fef3c7" stroke="#f59e0b" stroke-width="1"/>
          <text x="14" y="26" fill="#92400e" class="mono" font-size="11" font-weight="800">19-Day Intensive &amp; 3-Month Accredited Tracks</text>
        </g>

        <!-- Tech Stack Pills (Oracle Cloud replaces Azure) -->
        <g transform="translate(0, 122)">
          <text x="0" y="12" fill="#b45309" class="mono" font-size="9" font-weight="800" letter-spacing="1">PRODUCTION STACK YOU WILL MASTER:</text>
          <g transform="translate(0, 20)">
            <rect x="0" y="0" width="66" height="24" rx="6" fill="#faf5ff" stroke="#7c3aed" stroke-width="1"/>
            <text x="33" y="16" fill="#7c3aed" class="mono" font-size="10" font-weight="800" text-anchor="middle">.NET 10</text>
            
            <rect x="72" y="0" width="66" height="24" rx="6" fill="#faf5ff" stroke="#7c3aed" stroke-width="1"/>
            <text x="105" y="16" fill="#7c3aed" class="mono" font-size="10" font-weight="800" text-anchor="middle">Flutter</text>
            
            <rect x="144" y="0" width="102" height="24" rx="6" fill="#fff7ed" stroke="#ea580c" stroke-width="1"/>
            <text x="195" y="16" fill="#c2410c" class="mono" font-size="10" font-weight="800" text-anchor="middle">Oracle Cloud</text>
            
            <rect x="252" y="0" width="68" height="24" rx="6" fill="#f0fdf4" stroke="#059669" stroke-width="1"/>
            <text x="286" y="16" fill="#059669" class="mono" font-size="10" font-weight="800" text-anchor="middle">Postgres</text>
            
            <rect x="326" y="0" width="66" height="24" rx="6" fill="#fef3c7" stroke="#d97706" stroke-width="1"/>
            <text x="359" y="16" fill="#b45309" class="mono" font-size="10" font-weight="800" text-anchor="middle">AI Agents</text>
          </g>
        </g>

        <!-- Big Scannable Academy QR Code Box (100% Inlined Vector Path) -->
        <g transform="translate(96, 188)">
          <rect width="200" height="200" rx="16" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5" filter="url(#softCardShadow)"/>
          <!-- Corner Targeting Guides -->
          <path d="M 6 18 L 6 6 L 18 6" fill="none" stroke="#d97706" stroke-width="2.5" stroke-linecap="round"/>
          <path d="M 194 18 L 194 6 L 182 6" fill="none" stroke="#d97706" stroke-width="2.5" stroke-linecap="round"/>
          <path d="M 6 182 L 6 194 L 18 194" fill="none" stroke="#d97706" stroke-width="2.5" stroke-linecap="round"/>
          <path d="M 194 182 L 194 194 L 182 194" fill="none" stroke="#d97706" stroke-width="2.5" stroke-linecap="round"/>

          <!-- Inlined Vector QR Path (39.6 x 39.6 scaled to 176x176, offset 12, 12) -->
          <g transform="translate(12, 12) scale(4.4444)">
            <use href="#qr-path-academy" fill="#0f172a"/>
          </g>
        </g>

        <!-- Callout Banner -->
        <g transform="translate(16, 408)">
          <rect width="360" height="42" rx="12" fill="#d97706" filter="url(#softCardShadow)"/>
          <text x="180" y="26" fill="#ffffff" class="sans" font-size="13" font-weight="900" text-anchor="middle">SCAN TO SUBMIT YOUR CV &amp; PORTFOLIO</text>
        </g>

        <text x="196" y="476" fill="#b45309" class="mono" font-size="12" font-weight="800" letter-spacing="1" text-anchor="middle">🌐 sputnikdevs.com/academy/apply</text>
      </g>
    </g>

  </g>


  <!-- =================================================================== -->
  <!-- BOTTOM BASE & CASSETTE CLEARANCE ZONE (Y: 1845 to 2000)             -->
  <!-- =================================================================== -->
  <g transform="translate(0, 1845)">
    <rect width="1000" height="155" fill="#fdfcff"/>
    <line x1="0" y1="0" x2="1000" y2="0" stroke="#d8b4fe" stroke-width="1.5"/>

    <!-- Left Footer: Updated STG Email -->
    <g transform="translate(60, 42)">
      <text x="0" y="0" fill="#0f172a" class="sans" font-size="15" font-weight="900">SPUTNIK TECH GROUP (PTY) LTD</text>
      <text x="0" y="20" fill="#64748b" class="sans" font-size="12">Consumer &amp; Mobile Innovation • info@sputniktechgroup.com</text>
      <text x="0" y="38" fill="#7c3aed" class="mono" font-size="11" font-weight="700">sputniktechgroup.com</text>
    </g>

    <!-- Center Badge -->
    <g transform="translate(500, 48)">
      <circle cx="0" cy="0" r="20" fill="#ffffff" stroke="#7c3aed" stroke-width="1.5" filter="url(#softCardShadow)"/>
      <text x="0" y="5" fill="#7c3aed" class="sans" font-size="12" font-weight="900" text-anchor="middle">ST</text>
    </g>

    <!-- Right Footer -->
    <g transform="translate(940, 42)">
      <text x="0" y="0" fill="#0f172a" class="sans" font-size="15" font-weight="900" text-anchor="end">SPUTNIK DEVS STUDIO (PTY) LTD</text>
      <text x="0" y="20" fill="#64748b" class="sans" font-size="12" text-anchor="end">Enterprise Cloud &amp; Tech Academy • info@sputnikdevs.com</text>
      <text x="0" y="38" fill="#7c3aed" class="mono" font-size="11" font-weight="700" text-anchor="end">sputnikdevs.com</text>
    </g>

    <!-- Roller Cassette Warning Margin -->
    <text x="500" y="118" fill="#94a3b8" class="mono" font-size="9" text-anchor="middle">[ ROLL-UP CASSETTE BASE CLEARANCE ZONE - 100mm ]</text>
  </g>

</svg>
"""
    return svg

def main():
    print("Generating High-Resolution Zaha Hadid Purple Vector Pull-Up Banner SVG...")
    svg_content = build_banner_svg()
    out_path = os.path.join(REPO_ROOT, "designs", "banner-1x2m", "banner.svg")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(svg_content)
    size_kb = os.path.getsize(out_path) / 1024
    print(f"✅ Generated {out_path} ({size_kb:.1f} KB)")

if __name__ == "__main__":
    main()
