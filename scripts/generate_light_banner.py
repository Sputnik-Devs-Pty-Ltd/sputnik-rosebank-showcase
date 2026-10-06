#!/usr/bin/env python3
"""
Generate the high-resolution, light-themed, high-value vector Pull-Up Banner (1m x 2m)
for Sputnik Tech Group and Sputnik Devs Studio at the Rosebank Tech Showcase 2026.
Features:
- Real corporate PNG logos embedded via Base64 data URIs
- 100% self-contained inlined vector QR codes (zero external resource dependency, dark navy on pure white)
- Luminous modern tech light background with subtle precision grids and elevated white cards
- Precision high-value custom vector icons replacing generic emojis
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

    # 2. Extract QR code vector paths
    qr_tb = get_svg_path_data("assets/qr/qr-tradeybay-playstore.svg")
    qr_acad = get_svg_path_data("assets/qr/qr-academy-apply.svg")
    qr_srms = get_svg_path_data("assets/qr/qr-student-housing-srms.svg")
    qr_shopnik = get_svg_path_data("assets/qr/qr-shopnik-ecommerce.svg")

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 1000 2000" width="1000mm" height="2000mm">
  <defs>
    <!-- Background Gradients (Luminous Modern Tech Light Theme) -->
    <linearGradient id="bgLightLeft" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="40%" stop-color="#f8faff"/>
      <stop offset="85%" stop-color="#f0f6ff"/>
      <stop offset="100%" stop-color="#e9f2ff"/>
    </linearGradient>

    <linearGradient id="bgLightRight" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="40%" stop-color="#fcfaff"/>
      <stop offset="85%" stop-color="#f5f3ff"/>
      <stop offset="100%" stop-color="#eef2ff"/>
    </linearGradient>

    <!-- Header Gradient Accent -->
    <linearGradient id="headerGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#0284c7"/>
      <stop offset="50%" stop-color="#6750a4"/>
      <stop offset="100%" stop-color="#059669"/>
    </linearGradient>

    <!-- Central Divider Spine -->
    <linearGradient id="dividerSpine" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#38bdf8" stop-opacity="0.2"/>
      <stop offset="15%" stop-color="#0284c7" stop-opacity="0.8"/>
      <stop offset="50%" stop-color="#6750a4" stop-opacity="1"/>
      <stop offset="85%" stop-color="#059669" stop-opacity="0.8"/>
      <stop offset="100%" stop-color="#059669" stop-opacity="0.2"/>
    </linearGradient>

    <!-- Card Drop Shadows -->
    <filter id="softCardShadow" x="-10%" y="-10%" width="120%" height="125%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="8" stdDeviation="14" flood-color="#0f172a" flood-opacity="0.06"/>
      <feDropShadow dx="0" dy="2" stdDeviation="4" flood-color="#0f172a" flood-opacity="0.04"/>
    </filter>

    <filter id="deepCardShadow" x="-10%" y="-10%" width="120%" height="125%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="12" stdDeviation="18" flood-color="#0f172a" flood-opacity="0.10"/>
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#0f172a" flood-opacity="0.06"/>
    </filter>

    <filter id="phoneShadow" x="-15%" y="-10%" width="130%" height="125%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="16" stdDeviation="20" flood-color="#0284c7" flood-opacity="0.18"/>
      <feDropShadow dx="0" dy="4" stdDeviation="8" flood-color="#0f172a" flood-opacity="0.12"/>
    </filter>

    <!-- Phone Screen Clip for Real Production Screenshots -->
    <clipPath id="phoneScreenClip">
      <rect x="0" y="0" width="186" height="402" rx="16"/>
    </clipPath>

    <!-- Subtle Hairline Grids -->
    <pattern id="gridLightLeft" width="28" height="28" patternUnits="userSpaceOnUse">
      <path d="M 28 0 L 0 0 0 28" fill="none" stroke="#0284c7" stroke-width="0.5" stroke-opacity="0.08"/>
    </pattern>

    <pattern id="gridLightRight" width="28" height="28" patternUnits="userSpaceOnUse">
      <path d="M 28 0 L 0 0 0 28" fill="none" stroke="#7c3aed" stroke-width="0.5" stroke-opacity="0.08"/>
    </pattern>

    <!-- Reusable QR Paths for Razor-Sharp Vector Rendering -->
    <path id="qr-path-tradeybay" d="{qr_tb}"/>
    <path id="qr-path-academy" d="{qr_acad}"/>
    <path id="qr-path-srms" d="{qr_srms}"/>
    <path id="qr-path-shopnik" d="{qr_shopnik}"/>

    <!-- =============================================================== -->
    <!-- HIGH-VALUE PRECISION VECTOR ICONS                                -->
    <!-- =============================================================== -->

    <!-- 1. Laptop / Tech Classifieds Icon -->
    <g id="icon-laptop">
      <rect x="3" y="27" width="42" height="4" rx="2" fill="#0284c7"/>
      <path d="M 19 27 L 29 27 L 28 29 L 20 29 Z" fill="#bae6fd"/>
      <rect x="7" y="6" width="34" height="22" rx="2.5" fill="#0f172a" stroke="#0284c7" stroke-width="1.5"/>
      <rect x="9" y="8" width="30" height="18" rx="1" fill="#e0f2fe"/>
      <line x1="12" y1="12" x2="22" y2="12" stroke="#0284c7" stroke-width="1.8" stroke-linecap="round"/>
      <line x1="12" y1="16" x2="33" y2="16" stroke="#38bdf8" stroke-width="1.4" stroke-linecap="round"/>
      <line x1="12" y1="20" x2="27" y2="20" stroke="#0284c7" stroke-width="1.4" stroke-linecap="round"/>
      <circle cx="33" cy="12" r="1.5" fill="#10b981"/>
    </g>

    <!-- 2. Auction Gavel & Spark Icon -->
    <g id="icon-auction">
      <rect x="6" y="34" width="26" height="6" rx="2" fill="#d97706"/>
      <rect x="10" y="32" width="18" height="3" rx="1" fill="#fbbf24"/>
      <g transform="rotate(-30 26 18)">
        <rect x="19" y="6" width="14" height="24" rx="3" fill="#f59e0b" stroke="#b45309" stroke-width="1.5"/>
        <rect x="17" y="4" width="18" height="3" rx="1" fill="#fbbf24"/>
        <rect x="17" y="29" width="18" height="3" rx="1" fill="#fbbf24"/>
        <rect x="24" y="18" width="4" height="26" rx="2" fill="#78350f"/>
      </g>
      <polygon points="38,6 34,14 38,14 32,24 42,12 37,12" fill="#d97706"/>
    </g>

    <!-- 3. AI ATS Resume & Career Match Icon -->
    <g id="icon-ats-resume">
      <path d="M 10 6 L 28 6 L 38 16 L 38 42 C 38 43.5 36.5 44 35 44 L 10 44 C 8.5 44 7 43.5 7 42 L 7 8 C 7 6.5 8.5 6 10 6 Z" fill="#ffffff" stroke="#7c3aed" stroke-width="2"/>
      <path d="M 28 6 L 28 16 L 38 16 Z" fill="#ede9fe" stroke="#7c3aed" stroke-width="1.5"/>
      <circle cx="15" cy="14" r="3.5" fill="#7c3aed"/>
      <line x1="21" y1="14" x2="27" y2="14" stroke="#7c3aed" stroke-width="1.8" stroke-linecap="round"/>
      <line x1="12" y1="22" x2="33" y2="22" stroke="#a78bfa" stroke-width="1.8" stroke-linecap="round"/>
      <line x1="12" y1="27" x2="31" y2="27" stroke="#cbd5e1" stroke-width="1.8" stroke-linecap="round"/>
      <line x1="12" y1="32" x2="25" y2="32" stroke="#cbd5e1" stroke-width="1.8" stroke-linecap="round"/>
      <!-- AI 4-Point Star Sparkle -->
      <path d="M 34 26 Q 34 31 39 31 Q 34 31 34 36 Q 34 31 29 31 Q 34 31 34 26 Z" fill="#d97706"/>
      <circle cx="39" cy="25" r="1.5" fill="#7c3aed"/>
    </g>

    <!-- 4. Branded Storefront & CIPC Merchant Icon -->
    <g id="icon-storefront">
      <path d="M 6 18 L 42 18 L 38 8 L 10 8 Z" fill="#6750a4"/>
      <polygon points="10,8 14,8 12,18 7,18" fill="#8b5cf6"/>
      <polygon points="20,8 24,8 23,18 18,18" fill="#8b5cf6"/>
      <polygon points="30,8 34,8 34,18 29,18" fill="#8b5cf6"/>
      <path d="M 6 18 Q 10 21 14 18 Q 18 21 22 18 Q 26 21 30 18 Q 34 21 38 18 Q 42 21 42 18" fill="none" stroke="#6750a4" stroke-width="2"/>
      <rect x="8" y="20" width="32" height="22" rx="1" fill="#ffffff" stroke="#6750a4" stroke-width="1.8"/>
      <rect x="11" y="23" width="13" height="14" fill="#e0e7ff" stroke="#a5b4fc" stroke-width="1"/>
      <rect x="27" y="23" width="10" height="19" fill="#6750a4" rx="1"/>
      <circle cx="29" cy="33" r="1" fill="#ffffff"/>
      <circle cx="37" cy="10" r="5" fill="#10b981"/>
      <path d="M 35 10 L 36.5 11.5 L 39.5 8.5" fill="none" stroke="#ffffff" stroke-width="1.2" stroke-linecap="round"/>
    </g>

    <!-- 5. Split-View Maps & Geolocation Radar Icon -->
    <g id="icon-map-radar">
      <polygon points="6,12 17,8 31,12 42,8 42,36 31,40 17,36 6,40" fill="#f0fdf4" stroke="#059669" stroke-width="2"/>
      <line x1="17" y1="8" x2="17" y2="36" stroke="#34d399" stroke-width="1.2" stroke-dasharray="2,2"/>
      <line x1="31" y1="12" x2="31" y2="40" stroke="#34d399" stroke-width="1.2" stroke-dasharray="2,2"/>
      <circle cx="24" cy="18" r="8" fill="#10b981" fill-opacity="0.2"/>
      <path d="M 24 10 C 20.5 10 18 12.5 18 16 C 18 21 24 28 24 28 C 24 28 30 21 30 16 C 30 12.5 27.5 10 24 10 Z" fill="#059669"/>
      <circle cx="24" cy="15" r="2.5" fill="#ffffff"/>
    </g>

    <!-- 6. Student Residence Building (SRMS) Modern Architectural Icon -->
    <g id="icon-residence">
      <rect x="12" y="10" width="24" height="32" rx="2" fill="#ffffff" stroke="#059669" stroke-width="2"/>
      <polygon points="10,12 24,4 38,12" fill="#059669"/>
      <rect x="16" y="14" width="4" height="4" rx="1" fill="#10b981"/>
      <rect x="22" y="14" width="4" height="4" rx="1" fill="#10b981"/>
      <rect x="28" y="14" width="4" height="4" rx="1" fill="#10b981"/>
      <rect x="16" y="21" width="4" height="4" rx="1" fill="#10b981"/>
      <rect x="22" y="21" width="4" height="4" rx="1" fill="#10b981"/>
      <rect x="28" y="21" width="4" height="4" rx="1" fill="#10b981"/>
      <rect x="16" y="28" width="4" height="4" rx="1" fill="#10b981"/>
      <rect x="28" y="28" width="4" height="4" rx="1" fill="#10b981"/>
      <rect x="21" y="28" width="6" height="14" rx="1" fill="#065f46"/>
      <line x1="24" y1="28" x2="24" y2="42" stroke="#ffffff" stroke-width="0.8"/>
      <rect x="36" y="20" width="8" height="22" rx="1" fill="#d1fae5" stroke="#059669" stroke-width="1.5"/>
      <rect x="38" y="24" width="4" height="3" rx="0.5" fill="#059669"/>
      <rect x="38" y="30" width="4" height="3" rx="0.5" fill="#059669"/>
    </g>

    <!-- 7. Shopnik E-Commerce Platform Icon -->
    <g id="icon-shopnik">
      <path d="M 10 16 L 38 16 L 41 42 C 41 43.5 39.5 44 38 44 L 10 44 C 8.5 44 7 43.5 7 42 Z" fill="#eef2ff" stroke="#4f46e5" stroke-width="2"/>
      <path d="M 17 17 L 17 11 C 17 7 31 7 31 11 L 31 17" fill="none" stroke="#4f46e5" stroke-width="2.5" stroke-linecap="round"/>
      <circle cx="24" cy="29" r="8" fill="#4f46e5"/>
      <rect x="21" y="27" width="6" height="4" rx="1" fill="#fbbf24"/>
      <line x1="16" y1="38" x2="32" y2="38" stroke="#818cf8" stroke-width="1.8" stroke-linecap="round"/>
    </g>

    <!-- 8. Sputnik Devs Academy Mortarboard & Code Icon -->
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

    <!-- 9. Cyber Security Shield (POPIA) Icon -->
    <g id="icon-shield">
      <path d="M 24 4 L 40 9 C 40 23 32 35 24 42 C 16 35 8 23 8 9 Z" fill="#e0f2fe" stroke="#0284c7" stroke-width="2"/>
      <path d="M 24 9 L 36 13 C 36 22 30 31 24 37 C 18 31 12 22 12 13 Z" fill="#0284c7"/>
      <path d="M 18 23 L 22 27 L 30 19" fill="none" stroke="#ffffff" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
    </g>

    <!-- 10. Chat Message Vector Icon -->
    <g id="icon-chat">
      <path d="M 4 8 C 4 5 6 3 9 3 L 27 3 C 30 3 32 5 32 8 L 32 20 C 32 23 30 25 27 25 L 12 25 L 6 29 L 6 25 L 9 25 C 6 25 4 23 4 20 Z" fill="#0284c7"/>
      <circle cx="12" cy="14" r="1.5" fill="#ffffff"/>
      <circle cx="18" cy="14" r="1.5" fill="#ffffff"/>
      <circle cx="24" cy="14" r="1.5" fill="#ffffff"/>
    </g>
  </defs>

  <style>
    .sans {{ font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }}
    .mono {{ font-family: 'JetBrains Mono', 'Fira Code', monospace; }}
  </style>

  <!-- =================================================================== -->
  <!-- DUAL VERTICAL SPLIT BACKGROUNDS (LUMINOUS TECH LIGHT THEME)         -->
  <!-- =================================================================== -->
  <!-- Left Side: Sputnik Tech Group -->
  <rect x="0" y="0" width="500" height="2000" fill="url(#bgLightLeft)"/>
  <rect x="0" y="0" width="500" height="2000" fill="url(#gridLightLeft)"/>

  <!-- Right Side: Sputnik Devs Studio -->
  <rect x="500" y="0" width="500" height="2000" fill="url(#bgLightRight)"/>
  <rect x="500" y="0" width="500" height="2000" fill="url(#gridLightRight)"/>

  <!-- Soft Ambient Luminous Color Orbs for Depth -->
  <circle cx="150" cy="400" r="260" fill="#bae6fd" fill-opacity="0.25"/>
  <circle cx="350" cy="1350" r="280" fill="#e0e7ff" fill-opacity="0.30"/>
  <circle cx="850" cy="400" r="260" fill="#ede9fe" fill-opacity="0.30"/>
  <circle cx="650" cy="1350" r="280" fill="#d1fae5" fill-opacity="0.28"/>

  <!-- =================================================================== -->
  <!-- CENTRAL VERTICAL DIVIDER SPINE                                      -->
  <!-- =================================================================== -->
  <line x1="500" y1="210" x2="500" y2="1850" stroke="url(#dividerSpine)" stroke-width="3"/>
  <line x1="499" y1="210" x2="499" y2="1850" stroke="#ffffff" stroke-width="1"/>

  <!-- Circuit nodes on the central divider -->
  <circle cx="500" cy="220" r="6" fill="#0284c7" stroke="#ffffff" stroke-width="2"/>
  <circle cx="500" cy="620" r="7" fill="#6750a4" stroke="#ffffff" stroke-width="2"/>
  <circle cx="500" cy="1070" r="7" fill="#8b5cf6" stroke="#ffffff" stroke-width="2"/>
  <circle cx="500" cy="1480" r="7" fill="#059669" stroke="#ffffff" stroke-width="2"/>
  <circle cx="500" cy="1840" r="6" fill="#0284c7" stroke="#ffffff" stroke-width="2"/>

  <!-- Horizontal circuit branch ticks -->
  <path d="M 465 620 L 500 620 L 535 620" stroke="#6750a4" stroke-width="1.8" stroke-opacity="0.5"/>
  <path d="M 465 1070 L 500 1070 L 535 1070" stroke="#8b5cf6" stroke-width="1.8" stroke-opacity="0.5"/>
  <path d="M 465 1480 L 500 1480 L 535 1480" stroke="#059669" stroke-width="1.8" stroke-opacity="0.5"/>

  <!-- =================================================================== -->
  <!-- TOP UNIFIED HEADER (Y: 30 - 200)                                    -->
  <!-- =================================================================== -->
  <g transform="translate(500, 32)">
    <!-- Event Badge -->
    <rect x="-195" y="0" width="390" height="34" rx="17" fill="#ffffff" stroke="#0284c7" stroke-width="1.5" filter="url(#softCardShadow)"/>
    <circle cx="-170" cy="17" r="5" fill="#0284c7"/>
    <text x="-152" y="22" fill="#0369a1" class="mono" font-size="12" font-weight="800" letter-spacing="2">ROSEBANK TECH SHOWCASE 2026</text>

    <!-- Master Title (Deep Slate High Contrast) -->
    <text x="0" y="74" fill="#0f172a" class="sans" font-size="38" font-weight="900" letter-spacing="1" text-anchor="middle">THE SPUTNIK TECH ECOSYSTEM</text>
    <text x="0" y="104" fill="#475569" class="sans" font-size="15" font-weight="600" letter-spacing="0.3" text-anchor="middle">Connecting Campus Marketplace Commerce with Enterprise Cloud Software</text>

    <!-- Subtitle Split Indicator Bar -->
    <rect x="-445" y="126" width="425" height="30" rx="15" fill="#ffffff" stroke="#0284c7" stroke-width="1.5" filter="url(#softCardShadow)"/>
    <circle cx="-425" cy="141" r="4" fill="#0284c7"/>
    <text x="-232" y="146" fill="#0369a1" class="mono" font-size="11" font-weight="800" letter-spacing="2" text-anchor="middle">◀ CONSUMER &amp; CAMPUS MOBILE LABS</text>

    <rect x="20" y="126" width="425" height="30" rx="15" fill="#ffffff" stroke="#7c3aed" stroke-width="1.5" filter="url(#softCardShadow)"/>
    <circle cx="425" cy="141" r="4" fill="#7c3aed"/>
    <text x="232" y="146" fill="#6d28d9" class="mono" font-size="11" font-weight="800" letter-spacing="2" text-anchor="middle">ENTERPRISE SAAS &amp; ACADEMY ▶</text>
  </g>


  <!-- =================================================================== -->
  <!-- LEFT COLUMN: SPUTNIK TECH GROUP & TRADEY BAY APP (X: 38 - 468)       -->
  <!-- =================================================================== -->
  <g transform="translate(38, 215)">

    <!-- Company Branding Header with Real Sputnik Tech Logo -->
    <g transform="translate(0, 0)">
      <rect x="0" y="0" width="56" height="56" rx="14" fill="#ffffff" stroke="#e2e8f0" stroke-width="1" filter="url(#softCardShadow)"/>
      <image href="{sputnik_tech_logo}" x="4" y="4" width="48" height="48" preserveAspectRatio="xMidYMid meet"/>
      <text x="68" y="24" fill="#0f172a" class="sans" font-size="22" font-weight="900" letter-spacing="1">SPUTNIK TECH GROUP</text>
      <text x="68" y="42" fill="#0284c7" class="mono" font-size="11" font-weight="800" letter-spacing="2.5">CONSUMER &amp; MOBILE INNOVATION</text>
    </g>

    <!-- HERO CARD: TRADEY BAY MOBILE APP (Y: 65 to 585) -->
    <g transform="translate(0, 68)">
      <!-- Outer Card Frame (Elevated White Surface with Cyan Highlight) -->
      <rect x="0" y="0" width="430" height="525" rx="22" fill="#ffffff" stroke="#0284c7" stroke-width="2" filter="url(#deepCardShadow)"/>
      
      <!-- Card Top Bar -->
      <rect x="0" y="0" width="430" height="64" rx="22" fill="#f0f9ff"/>
      <path d="M 0 64 L 430 64" stroke="#bae6fd" stroke-width="1"/>
      
      <!-- Real Tradey Bay Primary Logo in Header -->
      <g transform="translate(14, 12)">
        <image href="{tradeybay_primary_logo}" x="0" y="0" width="125" height="40" preserveAspectRatio="xMinYMid meet"/>
        <text x="135" y="25" fill="#6750a4" class="mono" font-size="8.5" font-weight="800" letter-spacing="0.5">FLAGSHIP SUPER APP</text>
      </g>
      <rect x="312" y="18" width="104" height="26" rx="13" fill="#dcfce7" stroke="#16a34a" stroke-width="1"/>
      <circle cx="325" cy="31" r="3.5" fill="#16a34a"/>
      <text x="366" y="35" fill="#15803d" class="mono" font-size="8.5" font-weight="800" text-anchor="middle">LIVE v2.0.2+29</text>

      <!-- DUAL SMARTPHONE PRODUCTION DEVICE MOCKUPS (Side-by-Side Light & Dark Mode) -->
      <!-- Left Phone: Light Mode Production App -->
      <g id="phone-light-mockup">
        <!-- Phone Outer Chassis -->
        <rect x="12" y="70" width="196" height="412" rx="22" fill="#0f172a" stroke="#cbd5e1" stroke-width="2" filter="url(#phoneShadow)"/>
        <!-- Inner Bezel Ring -->
        <rect x="15" y="73" width="190" height="406" rx="19" fill="none" stroke="#334155" stroke-width="1"/>
        
        <!-- Screen Content (Clipped Real Flutter Production Screenshot) -->
        <g transform="translate(17, 75)" clip-path="url(#phoneScreenClip)">
          <image href="{tradeybay_light_screenshot}" x="0" y="0" width="186" height="402" preserveAspectRatio="xMidYMid slice"/>
        </g>

        <!-- Dynamic Island Cutout -->
        <rect x="85" y="78" width="50" height="8" rx="4" fill="#090d16"/>
        <circle cx="95" cy="82" r="2" fill="#1e293b"/>
        <circle cx="120" cy="82" r="1.5" fill="#0369a1"/>

        <!-- Hardware Gloss Reflection -->
        <path d="M 17 75 L 120 75 L 17 240 Z" fill="#ffffff" opacity="0.04"/>

        <!-- Home Bar -->
        <rect x="80" y="471" width="60" height="3" rx="1.5" fill="#64748b" opacity="0.6"/>

        <!-- Theme Pill -->
        <rect x="16" y="488" width="188" height="24" rx="12" fill="#eff6ff" stroke="#0284c7" stroke-width="1.2"/>
        <circle cx="34" cy="500" r="4" fill="#0284c7"/>
        <text x="114" y="504" fill="#0369a1" class="mono" font-size="9" font-weight="800" text-anchor="middle">☀ FLUTTER LIGHT UI</text>
      </g>

      <!-- Right Phone: Dark Mode Production App -->
      <g id="phone-dark-mockup">
        <!-- Phone Outer Chassis -->
        <rect x="222" y="70" width="196" height="412" rx="22" fill="#070c18" stroke="#38bdf8" stroke-width="2" filter="url(#phoneShadow)"/>
        <!-- Inner Bezel Ring -->
        <rect x="225" y="73" width="190" height="406" rx="19" fill="none" stroke="#0284c7" stroke-width="1" stroke-opacity="0.4"/>
        
        <!-- Screen Content (Clipped Real Flutter Production Screenshot) -->
        <g transform="translate(227, 75)" clip-path="url(#phoneScreenClip)">
          <image href="{tradeybay_dark_screenshot}" x="0" y="0" width="186" height="402" preserveAspectRatio="xMidYMid slice"/>
        </g>

        <!-- Dynamic Island Cutout -->
        <rect x="295" y="78" width="50" height="8" rx="4" fill="#000000"/>
        <circle cx="305" cy="82" r="2" fill="#1e293b"/>
        <circle cx="330" cy="82" r="1.5" fill="#38bdf8"/>

        <!-- Hardware Gloss Reflection -->
        <path d="M 227 75 L 330 75 L 227 240 Z" fill="#ffffff" opacity="0.05"/>

        <!-- Home Bar -->
        <rect x="290" y="471" width="60" height="3" rx="1.5" fill="#38bdf8" opacity="0.7"/>

        <!-- Theme Pill -->
        <rect x="226" y="488" width="188" height="24" rx="12" fill="#090d16" stroke="#38bdf8" stroke-width="1.2"/>
        <circle cx="244" cy="500" r="4" fill="#38bdf8"/>
        <text x="324" y="504" fill="#38bdf8" class="mono" font-size="9" font-weight="800" text-anchor="middle">☾ OLED DARK THEME</text>
      </g>
    </g>

    <!-- POINT & EXPLAIN FEATURE CARDS WITH HIGH-VALUE VECTOR ICONS (Y: 605 to 1080) -->
    <g transform="translate(0, 608)">
      <rect x="0" y="0" width="310" height="24" rx="12" fill="#e0f2fe"/>
      <text x="155" y="16" fill="#0369a1" class="mono" font-size="11" font-weight="800" letter-spacing="1.5" text-anchor="middle">OFFICIAL TRADEY BAY PLATFORM PILLARS</text>

      <!-- Point 1: Classifieds & Live Digital Auctions -->
      <g transform="translate(0, 32)">
        <rect width="430" height="88" rx="16" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.2" filter="url(#softCardShadow)"/>
        <rect x="14" y="14" width="60" height="60" rx="12" fill="#e0f2fe"/>
        <!-- High-Value Laptop / Tag Icon -->
        <use href="#icon-laptop" x="20" y="20"/>
        <text x="86" y="34" fill="#0f172a" class="sans" font-size="14" font-weight="800">1. Classified Ads &amp; Real-Time Auctions</text>
        <text x="86" y="52" fill="#475569" class="sans" font-size="11.5">Free listings across Vehicles, Solar, Tech &amp; Dorm gear.</text>
        <text x="86" y="68" fill="#0284c7" class="sans" font-size="11" font-weight="700">Sub-100ms SignalR live bidding with 60s anti-snipe extension.</text>
      </g>

      <!-- Point 2: Seller & Business Storefronts -->
      <g transform="translate(0, 130)">
        <rect width="430" height="88" rx="16" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.2" filter="url(#softCardShadow)"/>
        <rect x="14" y="14" width="60" height="60" rx="12" fill="#ede9fe"/>
        <!-- High-Value Storefront Icon -->
        <use href="#icon-storefront" x="20" y="20"/>
        <text x="86" y="34" fill="#0f172a" class="sans" font-size="14" font-weight="800">2. Branded Seller &amp; Business Storefronts</text>
        <text x="86" y="52" fill="#475569" class="sans" font-size="11.5">Dedicated digital showrooms for private sellers and CIPC stores</text>
        <text x="86" y="68" fill="#6d28d9" class="sans" font-size="11" font-weight="700">with verified vendor badges, product carousels &amp; in-store search.</text>
      </g>

      <!-- Point 3: Interactive Maps & Split View -->
      <g transform="translate(0, 228)">
        <rect width="430" height="88" rx="16" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.2" filter="url(#softCardShadow)"/>
        <rect x="14" y="14" width="60" height="60" rx="12" fill="#d1fae5"/>
        <!-- High-Value Map Radar Icon -->
        <use href="#icon-map-radar" x="20" y="20"/>
        <text x="86" y="34" fill="#0f172a" class="sans" font-size="14" font-weight="800">3. Interactive Split-View Geospatial Maps</text>
        <text x="86" y="52" fill="#475569" class="sans" font-size="11.5">Switch between card grid and live Google Map view with</text>
        <text x="86" y="68" fill="#059669" class="sans" font-size="11" font-weight="700">clustered price pins and bounding box search-as-you-move.</text>
      </g>

      <!-- Point 4: Jobs & Native AI ATS Resume Builder -->
      <g transform="translate(0, 326)">
        <rect width="430" height="88" rx="16" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.2" filter="url(#softCardShadow)"/>
        <rect x="14" y="14" width="60" height="60" rx="12" fill="#fef3c7"/>
        <!-- High-Value ATS Resume Icon -->
        <use href="#icon-ats-resume" x="20" y="20"/>
        <text x="86" y="34" fill="#0f172a" class="sans" font-size="14" font-weight="800">4. Jobs Network &amp; Native AI ATS Resume Builder</text>
        <text x="86" y="52" fill="#475569" class="sans" font-size="11.5">Built-in ATS resume creator with 4 templates &amp; vector PDF export.</text>
        <text x="86" y="68" fill="#b45309" class="sans" font-size="11" font-weight="700">Algorithmic vacancy matching with 1-tap direct applications.</text>
      </g>
    </g>

    <!-- SCANNABLE QR CALL-TO-ACTION CARD (HIGH CONTRAST, 100% INLINED VECTOR) (Y: 1060 to 1540) -->
    <g transform="translate(0, 1065)">
      <!-- Gradient Container Card -->
      <rect width="430" height="475" rx="22" fill="#0369a1" filter="url(#deepCardShadow)"/>
      <rect x="2" y="2" width="426" height="471" rx="20" fill="none" stroke="#38bdf8" stroke-width="2"/>

      <text x="215" y="38" fill="#bae6fd" class="mono" font-size="12" font-weight="800" letter-spacing="2" text-anchor="middle">GET TRADEY BAY TODAY (v2.0.2+29)</text>
      <text x="215" y="62" fill="#ffffff" class="sans" font-size="18" font-weight="900" text-anchor="middle">Scan Camera to Install on Google Play</text>

      <!-- PURE WHITE HIGH-CONTRAST QR CODE CANVAS (INLINED VECTOR PATH) -->
      <g transform="translate(105, 80)">
        <rect width="220" height="220" rx="18" fill="#ffffff" stroke="#ffffff" stroke-width="2" filter="url(#softCardShadow)"/>
        <!-- Corner Targeting Guides -->
        <path d="M 6 18 L 6 6 L 18 6" fill="none" stroke="#0284c7" stroke-width="2.5" stroke-linecap="round"/>
        <path d="M 214 18 L 214 6 L 202 6" fill="none" stroke="#0284c7" stroke-width="2.5" stroke-linecap="round"/>
        <path d="M 6 202 L 6 214 L 18 214" fill="none" stroke="#0284c7" stroke-width="2.5" stroke-linecap="round"/>
        <path d="M 214 202 L 214 214 L 202 214" fill="none" stroke="#0284c7" stroke-width="2.5" stroke-linecap="round"/>

        <!-- Inlined Vector QR Path (49.2 x 49.2 scaled to 196x196, offset 12, 12) -->
        <g transform="translate(12, 12) scale(3.9837)">
          <use href="#qr-path-tradeybay" fill="#0f172a"/>
        </g>
      </g>

      <!-- Google Play Badge -->
      <g transform="translate(68, 318)">
        <rect width="140" height="42" rx="8" fill="#000000" stroke="#38bdf8" stroke-width="1.2"/>
        <text x="25" y="27" fill="#34d399" class="sans" font-size="18">▶</text>
        <text x="48" y="18" fill="#94a3b8" class="mono" font-size="7">GET IT ON</text>
        <text x="48" y="32" fill="#ffffff" class="sans" font-size="12" font-weight="700">Google Play</text>
      </g>

      <!-- iOS Coming Soon Badge -->
      <g transform="translate(222, 318)">
        <rect width="140" height="42" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.2"/>
        <text x="25" y="27" fill="#ffffff" class="sans" font-size="18"></text>
        <text x="48" y="18" fill="#94a3b8" class="mono" font-size="7">APPLE IOS</text>
        <text x="48" y="32" fill="#38bdf8" class="sans" font-size="11" font-weight="700">Coming Soon</text>
      </g>

      <!-- Social Proof Rating Pill -->
      <g transform="translate(35, 376)">
        <rect width="360" height="36" rx="18" fill="#082f49" stroke="#38bdf8" stroke-width="1"/>
        <text x="180" y="23" fill="#fbbf24" class="sans" font-size="11.5" font-weight="800" text-anchor="middle">★★★★★  <tspan fill="#ffffff">4.8 / 5.0</tspan>  <tspan fill="#38bdf8" font-weight="600">· 100% POPIA Compliant &amp; In-Country</tspan></text>
      </g>

      <!-- Corporate Web link -->
      <text x="215" y="442" fill="#ffffff" class="mono" font-size="13" font-weight="800" letter-spacing="1" text-anchor="middle">🌐 sputniktechgroup.com</text>
    </g>

  </g>


  <!-- =================================================================== -->
  <!-- RIGHT COLUMN: SPUTNIK DEVS STUDIO (SAAS & ACADEMY) (X: 532 - 962)   -->
  <!-- =================================================================== -->
  <g transform="translate(532, 215)">

    <!-- Company Branding Header with Real Sputnik Devs Logo -->
    <g transform="translate(0, 0)">
      <rect x="0" y="0" width="56" height="56" rx="14" fill="#ffffff" stroke="#e2e8f0" stroke-width="1" filter="url(#softCardShadow)"/>
      <image href="{sputnik_devs_logo}" x="4" y="4" width="48" height="48" preserveAspectRatio="xMidYMid meet"/>
      <text x="68" y="24" fill="#0f172a" class="sans" font-size="22" font-weight="900" letter-spacing="1">SPUTNIK DEVS STUDIO</text>
      <text x="68" y="42" fill="#059669" class="mono" font-size="11" font-weight="800" letter-spacing="2.5">ENTERPRISE SAAS &amp; ACADEMY</text>
    </g>

    <!-- CARD 1: STUDENT RESIDENCE MANAGEMENT & UNIVERSITY HUB (Y: 68 to 470) -->
    <g transform="translate(0, 68)">
      <rect width="430" height="400" rx="20" fill="#ffffff" stroke="#059669" stroke-width="2" filter="url(#softCardShadow)"/>
      
      <!-- Card Header -->
      <rect width="430" height="56" rx="20" fill="#f0fdf4"/>
      <path d="M 0 56 L 430 56" stroke="#bbf7d0" stroke-width="1"/>
      
      <!-- Vector Residence Icon -->
      <use href="#icon-residence" x="12" y="6"/>
      <text x="64" y="27" fill="#0f172a" class="sans" font-size="15" font-weight="800">Student Res Management System</text>
      <text x="64" y="43" fill="#059669" class="mono" font-size="9" font-weight="700" letter-spacing="0.8">&amp; THE UNIVERSITY HUB PLATFORM</text>
      
      <rect x="332" y="16" width="84" height="24" rx="12" fill="#dcfce7" stroke="#059669" stroke-width="1"/>
      <text x="374" y="32" fill="#065f46" class="mono" font-size="9" font-weight="800" text-anchor="middle">CAMPUS B2B</text>

      <!-- Talking Points for Prince & Kenneth to point at -->
      <g transform="translate(18, 72)">
        <text x="0" y="16" fill="#065f46" class="mono" font-size="10.5" font-weight="800" letter-spacing="1">DESIGNED FOR RESIDENCES &amp; LANDLORDS:</text>
        
        <g transform="translate(0, 30)">
          <circle cx="10" cy="8" r="4" fill="#059669"/>
          <text x="24" y="12" fill="#0f172a" class="sans" font-size="13" font-weight="700">Automated Room &amp; Bed Allocations</text>
          <text x="24" y="28" fill="#475569" class="sans" font-size="11">Replaces spreadsheets with 1-click room assignment &amp; digital leases.</text>
        </g>

        <g transform="translate(0, 75)">
          <circle cx="10" cy="8" r="4" fill="#059669"/>
          <text x="24" y="12" fill="#0f172a" class="sans" font-size="13" font-weight="700">Digital Lease Signing &amp; Rent Billing</text>
          <text x="24" y="28" fill="#475569" class="sans" font-size="11">Automated rent invoices, NSFAS remittances &amp; arrears tracking.</text>
        </g>

        <g transform="translate(0, 120)">
          <circle cx="10" cy="8" r="4" fill="#059669"/>
          <text x="24" y="12" fill="#0f172a" class="sans" font-size="13" font-weight="700">Biometric Gate Access &amp; Maintenance</text>
          <text x="24" y="28" fill="#475569" class="sans" font-size="11">Turnstile integration, maintenance ticket tracking &amp; live room audits.</text>
        </g>

        <g transform="translate(0, 165)">
          <circle cx="10" cy="8" r="4" fill="#0284c7"/>
          <text x="24" y="12" fill="#0f172a" class="sans" font-size="13" font-weight="700">The University Hub Sister Platform</text>
          <text x="24" y="28" fill="#475569" class="sans" font-size="11">Campus life portal: student societies, events &amp; campus notices.</text>
        </g>

        <!-- QR Mini Block & Link (Inlined Vector Path) -->
        <g transform="translate(0, 222)">
          <rect width="394" height="46" rx="12" fill="#f0fdf4" stroke="#059669" stroke-width="1.2"/>
          <g transform="translate(8, 5)">
            <rect width="36" height="36" rx="6" fill="#ffffff" stroke="#bbf7d0" stroke-width="1"/>
            <g transform="translate(2, 2) scale(0.808)">
              <use href="#qr-path-srms" fill="#0f172a"/>
            </g>
          </g>
          <text x="54" y="21" fill="#0f172a" class="sans" font-size="11.5" font-weight="800">Scan for Hostel SRMS Live Demo</text>
          <text x="54" y="35" fill="#059669" class="mono" font-size="10" font-weight="700">sputnikdevs.com/products/hostel</text>
          <text x="360" y="28" fill="#059669" class="sans" font-size="18" font-weight="900">➔</text>
        </g>
      </g>
    </g>

    <!-- CARD 2: SHOPNIK E-COMMERCE SAAS (Y: 480 to 885) -->
    <g transform="translate(0, 482)">
      <rect width="430" height="400" rx="20" fill="#ffffff" stroke="#4f46e5" stroke-width="2" filter="url(#softCardShadow)"/>
      
      <!-- Card Header -->
      <rect width="430" height="56" rx="20" fill="#eef2ff"/>
      <path d="M 0 56 L 430 56" stroke="#c7d2fe" stroke-width="1"/>
      
      <!-- Vector Shopnik Icon -->
      <use href="#icon-shopnik" x="12" y="6"/>
      <text x="64" y="27" fill="#0f172a" class="sans" font-size="15" font-weight="800">Shopnik E-Commerce Platform</text>
      <text x="64" y="43" fill="#4f46e5" class="mono" font-size="9" font-weight="700" letter-spacing="0.8">SOUTH AFRICA'S SHOPIFY ALTERNATIVE</text>
      
      <rect x="332" y="16" width="84" height="24" rx="12" fill="#e0e7ff" stroke="#4f46e5" stroke-width="1"/>
      <text x="374" y="32" fill="#3730a3" class="mono" font-size="9" font-weight="800" text-anchor="middle">SAAS SUITE</text>

      <!-- Talking Points for Prince & Kenneth to point at -->
      <g transform="translate(18, 72)">
        <text x="0" y="16" fill="#3730a3" class="mono" font-size="10.5" font-weight="800" letter-spacing="1">WHY MERCHANTS CHOOSE SHOPNIK:</text>
        
        <g transform="translate(0, 30)">
          <circle cx="10" cy="8" r="4" fill="#4f46e5"/>
          <text x="24" y="12" fill="#0f172a" class="sans" font-size="13" font-weight="700">Native South African Payment Gateways</text>
          <text x="24" y="28" fill="#475569" class="sans" font-size="11">Pre-integrated with PayFast, Ozow, Yoco, Paystack &amp; Capitec Pay.</text>
        </g>

        <g transform="translate(0, 75)">
          <circle cx="10" cy="8" r="4" fill="#4f46e5"/>
          <text x="24" y="12" fill="#0f172a" class="sans" font-size="13" font-weight="700">Zero USD Foreign Exchange Penalties</text>
          <text x="24" y="28" fill="#475569" class="sans" font-size="11">No hidden dollar conversion fees. Transparent, local Rand pricing.</text>
        </g>

        <g transform="translate(0, 120)">
          <circle cx="10" cy="8" r="4" fill="#4f46e5"/>
          <text x="24" y="12" fill="#0f172a" class="sans" font-size="13" font-weight="700">Sub-Second Speed &amp; High-Volume Ready</text>
          <text x="24" y="28" fill="#475569" class="sans" font-size="11">Engineered on .NET 10 &amp; Cloud Redis. Handles Black Friday traffic.</text>
        </g>

        <g transform="translate(0, 165)">
          <circle cx="10" cy="8" r="4" fill="#0284c7"/>
          <text x="24" y="12" fill="#0f172a" class="sans" font-size="13" font-weight="700">Multi-Tier Architecture &amp; Custom Themes</text>
          <text x="24" y="28" fill="#475569" class="sans" font-size="11">Starter, Professional &amp; Enterprise tiers with live split-screen editor.</text>
        </g>

        <!-- QR Mini Block & Link (Inlined Vector Path) -->
        <g transform="translate(0, 222)">
          <rect width="394" height="46" rx="12" fill="#eef2ff" stroke="#4f46e5" stroke-width="1.2"/>
          <g transform="translate(8, 5)">
            <rect width="36" height="36" rx="6" fill="#ffffff" stroke="#c7d2fe" stroke-width="1"/>
            <g transform="translate(2, 2) scale(0.808)">
              <use href="#qr-path-shopnik" fill="#0f172a"/>
            </g>
          </g>
          <text x="54" y="21" fill="#0f172a" class="sans" font-size="11.5" font-weight="800">Scan for Shopnik E-Commerce Store</text>
          <text x="54" y="35" fill="#4f46e5" class="mono" font-size="10" font-weight="700">sputnikdevs.com/products/ecommerce</text>
          <text x="360" y="28" fill="#4f46e5" class="sans" font-size="18" font-weight="900">➔</text>
        </g>
      </g>
    </g>

    <!-- CARD 3: SPUTNIK DEVS ACADEMY — LEARNERSHIPS (GOLD CARD) (Y: 895 to 1540) -->
    <g transform="translate(0, 895)">
      <rect width="430" height="645" rx="22" fill="#ffffff" stroke="#d97706" stroke-width="2.5" filter="url(#deepCardShadow)"/>

      <!-- Gold Banner Header -->
      <rect width="430" height="64" rx="22" fill="#fef3c7"/>
      <path d="M 0 64 L 430 64" stroke="#fcd34d" stroke-width="1.5"/>

      <!-- Vector Academy Icon -->
      <use href="#icon-academy" x="12" y="8"/>
      <text x="64" y="28" fill="#0f172a" class="sans" font-size="16" font-weight="900">SPUTNIK DEVS ACADEMY</text>
      <text x="64" y="46" fill="#b45309" class="mono" font-size="9.5" font-weight="800" letter-spacing="0.8">ACCREDITED TECH LEARNERSHIPS (WIL)</text>
      
      <rect x="316" y="18" width="100" height="28" rx="14" fill="#d97706"/>
      <text x="366" y="36" fill="#ffffff" class="mono" font-size="9.5" font-weight="900" text-anchor="middle">WE ARE HIRING</text>

      <!-- Hook for Students -->
      <g transform="translate(20, 82)">
        <text x="0" y="16" fill="#0f172a" class="sans" font-size="16" font-weight="900">Calling All IT, CS &amp; Software Students!</text>
        <text x="0" y="36" fill="#334155" class="sans" font-size="12">Accelerate your tech career with hands-on Work-Integrated</text>
        <text x="0" y="52" fill="#334155" class="sans" font-size="12">Learning (WIL). Build production systems alongside senior engineers.</text>

        <!-- Feature Points -->
        <g transform="translate(0, 68)">
          <rect width="390" height="42" rx="10" fill="#fef3c7" stroke="#f59e0b" stroke-width="1"/>
          <text x="14" y="26" fill="#92400e" class="mono" font-size="11" font-weight="800">19-Day Intensive &amp; 3-Month Accredited Tracks</text>
        </g>

        <!-- Tech Stack Pills -->
        <g transform="translate(0, 122)">
          <text x="0" y="12" fill="#b45309" class="mono" font-size="9" font-weight="800" letter-spacing="1">PRODUCTION STACK YOU WILL MASTER:</text>
          <g transform="translate(0, 20)">
            <rect x="0" y="0" width="70" height="24" rx="6" fill="#f0f9ff" stroke="#0284c7" stroke-width="1"/>
            <text x="35" y="16" fill="#0284c7" class="mono" font-size="10" font-weight="800" text-anchor="middle">.NET 10</text>
            
            <rect x="78" y="0" width="72" height="24" rx="6" fill="#f0f9ff" stroke="#0284c7" stroke-width="1"/>
            <text x="114" y="16" fill="#0284c7" class="mono" font-size="10" font-weight="800" text-anchor="middle">Flutter</text>
            
            <rect x="158" y="0" width="65" height="24" rx="6" fill="#eef2ff" stroke="#4f46e5" stroke-width="1"/>
            <text x="190" y="16" fill="#4f46e5" class="mono" font-size="10" font-weight="800" text-anchor="middle">Azure</text>
            
            <rect x="231" y="0" width="75" height="24" rx="6" fill="#f0fdf4" stroke="#059669" stroke-width="1"/>
            <text x="268" y="16" fill="#059669" class="mono" font-size="10" font-weight="800" text-anchor="middle">Postgres</text>
            
            <rect x="314" y="0" width="74" height="24" rx="6" fill="#fef3c7" stroke="#d97706" stroke-width="1"/>
            <text x="351" y="16" fill="#b45309" class="mono" font-size="10" font-weight="800" text-anchor="middle">AI Agents</text>
          </g>
        </g>

        <!-- Big Scannable Academy QR Code Box (100% Inlined Vector Path) -->
        <g transform="translate(95, 188)">
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
        <g transform="translate(15, 408)">
          <rect width="360" height="42" rx="12" fill="#d97706" filter="url(#softCardShadow)"/>
          <text x="180" y="26" fill="#ffffff" class="sans" font-size="13" font-weight="900" text-anchor="middle">SCAN TO SUBMIT YOUR CV &amp; PORTFOLIO</text>
        </g>

        <text x="195" y="476" fill="#b45309" class="mono" font-size="12" font-weight="800" letter-spacing="1" text-anchor="middle">🌐 sputnikdevs.com/academy/apply</text>
      </g>
    </g>

  </g>


  <!-- =================================================================== -->
  <!-- BOTTOM BASE & CASSETTE CLEARANCE ZONE (Y: 1850 to 2000)             -->
  <!-- =================================================================== -->
  <g transform="translate(0, 1850)">
    <rect width="1000" height="150" fill="#f8fafc"/>
    <line x1="0" y1="0" x2="1000" y2="0" stroke="#cbd5e1" stroke-width="1.5"/>

    <!-- Left Footer -->
    <g transform="translate(60, 42)">
      <text x="0" y="0" fill="#0f172a" class="sans" font-size="15" font-weight="900">SPUTNIK TECH GROUP (PTY) LTD</text>
      <text x="0" y="20" fill="#64748b" class="sans" font-size="12">Consumer &amp; Mobile Innovation • support@sputniktechgroup.com</text>
      <text x="0" y="38" fill="#0284c7" class="mono" font-size="11" font-weight="700">sputniktechgroup.com</text>
    </g>

    <!-- Center Badge -->
    <g transform="translate(500, 48)">
      <circle cx="0" cy="0" r="20" fill="#ffffff" stroke="#0284c7" stroke-width="1.5" filter="url(#softCardShadow)"/>
      <text x="0" y="5" fill="#0284c7" class="sans" font-size="12" font-weight="900" text-anchor="middle">ST</text>
    </g>

    <!-- Right Footer -->
    <g transform="translate(940, 42)">
      <text x="0" y="0" fill="#0f172a" class="sans" font-size="15" font-weight="900" text-anchor="end">SPUTNIK DEVS STUDIO (PTY) LTD</text>
      <text x="0" y="20" fill="#64748b" class="sans" font-size="12" text-anchor="end">Enterprise Cloud &amp; Tech Academy • info@sputnikdevs.com</text>
      <text x="0" y="38" fill="#059669" class="mono" font-size="11" font-weight="700" text-anchor="end">sputnikdevs.com</text>
    </g>

    <!-- Roller Cassette Warning Margin -->
    <text x="500" y="115" fill="#94a3b8" class="mono" font-size="9" text-anchor="middle">[ ROLL-UP CASSETTE BASE CLEARANCE ZONE - 100mm ]</text>
  </g>

</svg>
"""
    return svg

def main():
    print("Generating High-Resolution Luminous Light Pull-Up Banner SVG...")
    svg_content = build_banner_svg()
    out_path = os.path.join(REPO_ROOT, "designs", "banner-1x2m", "banner.svg")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(svg_content)
    size_kb = os.path.getsize(out_path) / 1024
    print(f"✅ Generated {out_path} ({size_kb:.1f} KB)")

if __name__ == "__main__":
    main()
