#!/usr/bin/env python3
"""
Generate the high-resolution, Zaha Hadid-inspired, light-themed vector Exhibition Tablecloth (3m x 3m)
for Sputnik Tech Group and Sputnik Devs Studio at the South Africa Tech Showcase.

Aligned precisely with the locked-down visual identity:
1. Vibrant Zaha Hadid architectural canopy waves & contour streamlines in royal purple tones (#3b0764, #581c87, #7c3aed, #8b5cf6, #a855f7).
2. 5-Zone layout:
   - Front Aisle Billboard (2600 x 950 mm): Dual-column ecosystem showcase with authentic logos, QR codes, and executive leadership bar.
   - Tabletop Console (1800 x 750 mm): Tradey Bay launchpad reticle, Unified Cloud Architecture Blueprint (.NET 10, OCI SA, Postgres, Redis, gRPC, AI), and SaaS / Academy testbed.
   - Left Skirt: Tradey Bay & Mobile Labs focus with QR code.
   - Right Skirt: Sputnik Devs Studio, Shopnik & Academy focus with QR code.
   - Rear Operator HUD (rotated 180°): Tactical cheat sheet for Kenneth & Prince.
3. Official corporate information:
   - 292 Surrey Avenue, Randburg, Johannesburg, 2194
   - Direct: takudzwam@sputniktechgroup.com | info@sputniktechgroup.com | +27 66 321 5528 | +263 787 015 123
   - Takudzwa Mupanesure (Founder, Chief Executive Officer & Lead Architect)
   - In Concurrence with: Kenneth Takudzwa Katsande (Director of Operations) & Prince Lwazi Nkiwane (Director of Growth)
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
    tradeybay_dark_screenshot = get_base64_img("assets/TradeyBayScreenShopDarkMode.jpeg")
    tradeybay_light_screenshot = get_base64_img("assets/TradeyBayScreenshopLigtMode.jpeg")
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
    <linearGradient id="qrLightBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="40%" stop-color="#faf5ff"/>
      <stop offset="100%" stop-color="#f3e8ff"/>
    </linearGradient>

    <linearGradient id="cardGradWhite" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="100%" stop-color="#faf7ff"/>
    </linearGradient>

    <linearGradient id="blueCardGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="100%" stop-color="#f0fdfa"/>
    </linearGradient>

    <linearGradient id="darkConsoleBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f0926"/>
      <stop offset="50%" stop-color="#1e1145"/>
      <stop offset="100%" stop-color="#0a0518"/>
    </linearGradient>

    <!-- Card Drop Shadows (objectBoundingBox default prevents clipping) -->
    <filter id="softCardShadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="6" stdDeviation="12" flood-color="#3b0764" flood-opacity="0.08"/>
      <feDropShadow dx="0" dy="2" stdDeviation="4" flood-color="#0f172a" flood-opacity="0.04"/>
    </filter>

    <filter id="deepCardShadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="12" stdDeviation="18" flood-color="#3b0764" flood-opacity="0.12"/>
      <feDropShadow dx="0" dy="3" stdDeviation="6" flood-color="#0f172a" flood-opacity="0.05"/>
    </filter>

    <filter id="glowPurple" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="10" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>

    <!-- Subtle Background Dot Grid -->
    <pattern id="tcDotGrid" width="40" height="40" patternUnits="userSpaceOnUse">
      <circle cx="3" cy="3" r="1.5" fill="#7c3aed" fill-opacity="0.10"/>
    </pattern>
  </defs>

  <style>
    .sans {{ font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; }}
    .mono {{ font-family: 'JetBrains Mono', 'Fira Code', 'Courier New', monospace; }}
  </style>

  <!-- =================================================================== -->
  <!-- 0. BASE CANVAS (3000 x 3000 mm)                                     -->
  <!-- =================================================================== -->
  <rect width="3000" height="3000" fill="url(#tcBgGrad)"/>
  <rect width="3000" height="3000" fill="url(#tcDotGrid)"/>

  <!-- Soft Ambient Glow Pools -->
  <circle cx="800" cy="1500" r="600" fill="#ede9fe" fill-opacity="0.7"/>
  <circle cx="2200" cy="1500" r="600" fill="#f5f3ff" fill-opacity="0.7"/>
  <circle cx="1500" cy="2350" r="700" fill="#ede9fe" fill-opacity="0.5"/>
  <circle cx="1500" cy="650" r="600" fill="#ede9fe" fill-opacity="0.5"/>

  <!-- Zaha Hadid Parametric Fluid Ribbons (Flowing Across the 3m Cloth) -->
  <!-- Canopy Wave 1 (Upper Rear to Center) -->
  <path d="M -100 400 C 400 200 900 600 1500 350 C 2100 100 2600 500 3100 300 L 3100 800 C 2600 650 2000 850 1500 700 C 900 550 400 800 -100 650 Z" fill="url(#zahaPurple1)" opacity="0.14"/>

  <!-- Canopy Wave 2 (Center Mid-Flank) -->
  <path d="M -100 1300 C 500 1100 1000 1550 1600 1350 C 2200 1150 2650 1450 3100 1300 L 3100 1700 C 2600 1550 2100 1800 1500 1650 C 900 1500 400 1750 -100 1600 Z" fill="url(#zahaPurple2)" opacity="0.10"/>

  <!-- Canopy Wave 3 (Front Drape Aisle Flow) -->
  <path d="M -100 2100 C 500 1900 1100 2350 1700 2150 C 2300 1950 2700 2250 3100 2050 L 3100 2550 C 2600 2400 2100 2650 1500 2500 C 900 2350 400 2600 -100 2450 Z" fill="url(#zahaPurple3)" opacity="0.12"/>

  <!-- Dynamic Contour Streamlines -->
  <path d="M -50 480 C 450 280 950 680 1550 430 C 2150 180 2650 580 3050 380" fill="none" stroke="url(#zahaStreamGrad1)" stroke-width="3" stroke-opacity="0.35"/>
  <path d="M -50 510 C 450 310 950 710 1550 460 C 2150 210 2650 610 3050 410" fill="none" stroke="#7c3aed" stroke-width="2" stroke-opacity="0.25" stroke-dasharray="10,12"/>

  <path d="M -50 2180 C 550 1980 1150 2430 1750 2230 C 2350 2030 2750 2330 3050 2130" fill="none" stroke="url(#zahaStreamGrad2)" stroke-width="3" stroke-opacity="0.35"/>
  <path d="M -50 2210 C 550 2010 1150 2460 1750 2260 C 2350 2060 2750 2360 3050 2160" fill="none" stroke="#a855f7" stroke-width="2" stroke-opacity="0.25" stroke-dasharray="12,10"/>

  <!-- Outer Hem Clearance Safety Border (15mm from perimeter) -->
  <rect x="15" y="15" width="2970" height="2970" fill="none" stroke="#7c3aed" stroke-width="1.5" stroke-dasharray="25 15" stroke-opacity="0.3"/>

  <!-- Tabletop Boundary Marker (1800 x 750 mm table, X: 600..2400, Y: 1125..1875) -->
  <rect x="600" y="1125" width="1800" height="750" fill="none" stroke="#7c3aed" stroke-width="2" stroke-dasharray="16 10" stroke-opacity="0.4"/>
  <g transform="translate(615, 1145)">
    <rect width="260" height="26" rx="13" fill="#ffffff" stroke="#7c3aed" stroke-width="1.2" filter="url(#softCardShadow)"/>
    <text x="130" y="17" fill="#581c87" class="mono" font-size="11" font-weight="800" text-anchor="middle">◀ 1.8M TABLE SURFACE BOUNDARY</text>
  </g>
  <g transform="translate(2125, 1145)">
    <rect width="260" height="26" rx="13" fill="#ffffff" stroke="#7c3aed" stroke-width="1.2" filter="url(#softCardShadow)"/>
    <text x="130" y="17" fill="#581c87" class="mono" font-size="11" font-weight="800" text-anchor="middle">TABLE SURFACE BOUNDARY ▶</text>
  </g>


  <!-- =================================================================== -->
  <!-- ZONE 1: TABLETOP INTERACTIVE COMMAND CONSOLE (1800 x 750 mm)        -->
  <!-- Located at X: 600..2400, Y: 1125..1875                              -->
  <!-- =================================================================== -->
  <g transform="translate(600, 1125)">

    <!-- 1A. LEFT POD: TRADEY BAY INTERACTIVE SCAN LAUNCHPAD (X: 25..575) -->
    <g transform="translate(25, 25)">
      <rect width="550" height="700" rx="24" fill="url(#cardGradWhite)" stroke="#7c3aed" stroke-width="2" filter="url(#softCardShadow)"/>
      <rect width="550" height="54" rx="24" fill="url(#zahaPurple1)" opacity="0.12"/>
      <line x1="0" y1="54" x2="550" y2="54" stroke="#7c3aed" stroke-width="1.5" stroke-opacity="0.4"/>

      <!-- Pod Header -->
      <g transform="translate(20, 15)">
        <circle cx="12" cy="12" r="8" fill="#7c3aed"/>
        <text x="30" y="17" fill="#3b0764" class="sans" font-size="16" font-weight="900" letter-spacing="1">TRADEY BAY // CONSUMER LAUNCHPAD</text>
        <rect x="420" y="0" width="110" height="24" rx="12" fill="#faf5ff" stroke="#7c3aed" stroke-width="1"/>
        <text x="475" y="16" fill="#6b21a8" class="mono" font-size="10" font-weight="800" text-anchor="middle">v2.0.4+31</text>
      </g>

      <!-- Target Phone Placement Reticle -->
      <g transform="translate(30, 80)">
        <rect width="210" height="210" rx="20" fill="#ffffff" stroke="#7c3aed" stroke-width="2" filter="url(#softCardShadow)"/>
        <!-- Scannable Tradey Bay QR -->
        <path d="{qr_tb}" fill="#2e1065" transform="translate(18, 18) scale(0.39)"/>
      </g>

      <!-- Callout Text Beside QR -->
      <g transform="translate(260, 85)">
        <rect width="260" height="32" rx="8" fill="#faf5ff" stroke="#7c3aed" stroke-width="1"/>
        <text x="130" y="21" fill="#6b21a8" class="mono" font-size="11" font-weight="800" text-anchor="middle">📱 POINT CAMERA TO INSTALL</text>

        <text x="0" y="65" fill="#1e1b4b" class="sans" font-size="24" font-weight="900">Tradey<tspan fill="#7c3aed">Bay</tspan></text>
        <text x="0" y="85" fill="#581c87" class="mono" font-size="11" font-weight="700">MULTI-VERTICAL SUPER APP</text>
        
        <text x="0" y="112" fill="#475569" class="sans" font-size="12" font-weight="500">Free Verified Student Marketplace</text>
        <text x="0" y="130" fill="#475569" class="sans" font-size="12" font-weight="500">0% Commission • Classifieds • Housing</text>

        <!-- Google Play & App Store Indicators -->
        <g transform="translate(0, 150)">
          <rect width="260" height="36" rx="8" fill="#0f172a"/>
          <text x="130" y="23" fill="#ffffff" class="sans" font-size="12" font-weight="700" text-anchor="middle">▶ Google Play &amp; Apple App Store</text>
        </g>
      </g>

      <!-- 4 Point & Explain Pillars -->
      <g transform="translate(30, 315)">
        <rect width="490" height="78" rx="12" fill="#ffffff" stroke="#e9d5ff" stroke-width="1.2"/>
        <circle cx="28" cy="39" r="14" fill="#faf5ff" stroke="#7c3aed" stroke-width="1"/>
        <text x="28" y="44" fill="#7c3aed" class="sans" font-size="14" font-weight="900" text-anchor="middle">0%</text>
        <text x="56" y="32" fill="#1e1b4b" class="sans" font-size="13" font-weight="800">Zero Commission for Students</text>
        <text x="56" y="52" fill="#64748b" class="sans" font-size="11">Peer-to-peer textbook trading, campus dorm gear, electronics &amp; study materials.</text>
      </g>

      <g transform="translate(30, 405)">
        <rect width="490" height="78" rx="12" fill="#ffffff" stroke="#e9d5ff" stroke-width="1.2"/>
        <circle cx="28" cy="39" r="14" fill="#faf5ff" stroke="#7c3aed" stroke-width="1"/>
        <text x="28" y="44" fill="#7c3aed" class="sans" font-size="14" font-weight="900" text-anchor="middle">🏠</text>
        <text x="56" y="32" fill="#1e1b4b" class="sans" font-size="13" font-weight="800">Student Accommodation Marketplace</text>
        <text x="56" y="52" fill="#64748b" class="sans" font-size="11">Verified private student residences, accredited off-campus rooms &amp; subleases.</text>
      </g>

      <g transform="translate(30, 495)">
        <rect width="490" height="78" rx="12" fill="#ffffff" stroke="#e9d5ff" stroke-width="1.2"/>
        <circle cx="28" cy="39" r="14" fill="#faf5ff" stroke="#7c3aed" stroke-width="1"/>
        <text x="28" y="44" fill="#7c3aed" class="sans" font-size="14" font-weight="900" text-anchor="middle">💬</text>
        <text x="56" y="32" fill="#1e1b4b" class="sans" font-size="13" font-weight="800">In-App Chat &amp; Offer Countering</text>
        <text x="56" y="52" fill="#64748b" class="sans" font-size="11">Direct encrypted messaging between verified students, campus safety first.</text>
      </g>

      <g transform="translate(30, 585)">
        <rect width="490" height="85" rx="12" fill="#f5f3ff" stroke="#7c3aed" stroke-width="1.2"/>
        <text x="245" y="30" fill="#4c1d95" class="mono" font-size="11" font-weight="800" text-anchor="middle">🔒 100% POPIA COMPLIANT // RSA DATA PRIVACY</text>
        <text x="245" y="52" fill="#6b21a8" class="sans" font-size="11" font-weight="600" text-anchor="middle">Direct Support: info@sputniktechgroup.com</text>
        <text x="245" y="70" fill="#64748b" class="mono" font-size="10" text-anchor="middle">Built with Flutter Native &amp; Cloud Microservices</text>
      </g>
    </g>


    <!-- 1B. CENTER POD: UNIFIED ARCHITECTURE BLUEPRINT (X: 600..1200) -->
    <g transform="translate(600, 25)">
      <rect width="600" height="700" rx="24" fill="#ffffff" stroke="#7c3aed" stroke-width="2" filter="url(#softCardShadow)"/>
      <rect width="600" height="54" rx="24" fill="url(#zahaPurple2)" opacity="0.12"/>
      <line x1="0" y1="54" x2="600" y2="54" stroke="#7c3aed" stroke-width="1.5" stroke-opacity="0.4"/>

      <!-- Pod Header -->
      <g transform="translate(20, 15)">
        <circle cx="12" cy="12" r="8" fill="#8b5cf6"/>
        <text x="30" y="17" fill="#3b0764" class="sans" font-size="16" font-weight="900" letter-spacing="1">SYSTEMS BLUEPRINT // UNIFIED CLOUD ENGINE</text>
        <rect x="470" y="0" width="110" height="24" rx="12" fill="#faf5ff" stroke="#8b5cf6" stroke-width="1"/>
        <text x="525" y="16" fill="#7c3aed" class="mono" font-size="10" font-weight="800" text-anchor="middle">ARCH 2026</text>
      </g>

      <!-- Architecture Flow Diagram -->
      <!-- Tier 1: Client Layer (Top) -->
      <g transform="translate(30, 75)">
        <rect width="540" height="85" rx="12" fill="#faf5ff" stroke="#c084fc" stroke-width="1.2"/>
        <text x="20" y="24" fill="#581c87" class="mono" font-size="11" font-weight="800">CLIENT CHANNELS &amp; TOUCHPOINTS</text>
        
        <!-- 3 Channel Nodes -->
        <g transform="translate(20, 35)">
          <rect width="155" height="38" rx="6" fill="#ffffff" stroke="#7c3aed" stroke-width="1"/>
          <text x="77" y="23" fill="#1e1b4b" class="sans" font-size="11" font-weight="700" text-anchor="middle">📱 Tradey Bay App</text>
        </g>
        <g transform="translate(190, 35)">
          <rect width="160" height="38" rx="6" fill="#ffffff" stroke="#0284c7" stroke-width="1"/>
          <text x="80" y="23" fill="#0f172a" class="sans" font-size="11" font-weight="700" text-anchor="middle">🏢 SRMS &amp; UniHub</text>
        </g>
        <g transform="translate(365, 35)">
          <rect width="155" height="38" rx="6" fill="#ffffff" stroke="#10b981" stroke-width="1"/>
          <text x="77" y="23" fill="#064e3b" class="sans" font-size="11" font-weight="700" text-anchor="middle">🛍️ Shopnik SaaS</text>
        </g>
      </g>

      <!-- Connecting Flow Arrows -->
      <g transform="translate(300, 165)">
        <line x1="0" y1="0" x2="0" y2="25" stroke="#7c3aed" stroke-width="2" stroke-dasharray="4,4"/>
        <polygon points="0,28 -5,20 5,20" fill="#7c3aed"/>
      </g>

      <!-- Tier 2: Gateway & API Layer -->
      <g transform="translate(30, 195)">
        <rect width="540" height="90" rx="12" fill="#ffffff" stroke="#7c3aed" stroke-width="1.5" filter="url(#softCardShadow)"/>
        <text x="20" y="24" fill="#3b0764" class="mono" font-size="11" font-weight="800">API GATEWAY &amp; SERVICE MESH</text>
        
        <g transform="translate(20, 35)">
          <rect width="160" height="42" rx="8" fill="#f5f3ff" stroke="#7c3aed" stroke-width="1"/>
          <text x="80" y="20" fill="#4c1d95" class="sans" font-size="11" font-weight="800" text-anchor="middle">REST &amp; gRPC</text>
          <text x="80" y="34" fill="#6b21a8" class="mono" font-size="9" text-anchor="middle">Low-Latency RPC</text>
        </g>
        <g transform="translate(190, 35)">
          <rect width="160" height="42" rx="8" fill="#f0fdf4" stroke="#10b981" stroke-width="1"/>
          <text x="80" y="20" fill="#065f46" class="sans" font-size="11" font-weight="800" text-anchor="middle">PAYMENTS</text>
          <text x="80" y="34" fill="#047857" class="mono" font-size="9" text-anchor="middle">Paystack • PayFast • COD</text>
        </g>
        <g transform="translate(360, 35)">
          <rect width="160" height="42" rx="8" fill="#eff6ff" stroke="#3b82f6" stroke-width="1"/>
          <text x="80" y="20" fill="#1e40af" class="sans" font-size="11" font-weight="800" text-anchor="middle">IDENTITY &amp; AUTH</text>
          <text x="80" y="34" fill="#2563eb" class="mono" font-size="9" text-anchor="middle">Biometric / SSO / RBAC</text>
        </g>
      </g>

      <!-- Connecting Flow Arrows -->
      <g transform="translate(300, 290)">
        <line x1="0" y1="0" x2="0" y2="25" stroke="#7c3aed" stroke-width="2" stroke-dasharray="4,4"/>
        <polygon points="0,28 -5,20 5,20" fill="#7c3aed"/>
      </g>

      <!-- Tier 3: Core Compute & Cloud Engine -->
      <g transform="translate(30, 320)">
        <rect width="540" height="135" rx="12" fill="#faf5ff" stroke="#6b21a8" stroke-width="1.8"/>
        <rect x="360" y="10" width="160" height="22" rx="11" fill="#ede9fe"/>
        <text x="440" y="25" fill="#581c87" class="mono" font-size="9" font-weight="800" text-anchor="middle">ORACLE CLOUD SA (JHB)</text>
        <text x="20" y="26" fill="#3b0764" class="sans" font-size="13" font-weight="900">CORE BACKEND MICROSERVICES (.NET 10)</text>

        <!-- Microservice Pods -->
        <g transform="translate(20, 42)">
          <rect width="115" height="40" rx="6" fill="#ffffff" stroke="#c084fc" stroke-width="1"/>
          <text x="57" y="24" fill="#1e1b4b" class="mono" font-size="10" font-weight="700" text-anchor="middle">Marketplace Svc</text>
        </g>
        <g transform="translate(145, 42)">
          <rect width="115" height="40" rx="6" fill="#ffffff" stroke="#c084fc" stroke-width="1"/>
          <text x="57" y="24" fill="#1e1b4b" class="mono" font-size="10" font-weight="700" text-anchor="middle">Residency Svc</text>
        </g>
        <g transform="translate(270, 42)">
          <rect width="115" height="40" rx="6" fill="#ffffff" stroke="#c084fc" stroke-width="1"/>
          <text x="57" y="24" fill="#1e1b4b" class="mono" font-size="10" font-weight="700" text-anchor="middle">Shopnik Engine</text>
        </g>
        <g transform="translate(395, 42)">
          <rect width="125" height="40" rx="6" fill="#fdf4ff" stroke="#a21caf" stroke-width="1"/>
          <text x="62" y="24" fill="#701a75" class="mono" font-size="10" font-weight="800" text-anchor="middle">AI Workflow Agents</text>
        </g>

        <!-- Sub-features -->
        <text x="20" y="105" fill="#581c87" class="mono" font-size="10" font-weight="600">High-Concurrency Async Workers • Distributed Pub/Sub Messaging • Health Checks</text>
        <text x="20" y="122" fill="#64748b" class="sans" font-size="10">Zero-downtime deployment pipelines with full container orchestration.</text>
      </g>

      <!-- Connecting Flow Arrows -->
      <g transform="translate(300, 460)">
        <line x1="0" y1="0" x2="0" y2="25" stroke="#7c3aed" stroke-width="2" stroke-dasharray="4,4"/>
        <polygon points="0,28 -5,20 5,20" fill="#7c3aed"/>
      </g>

      <!-- Tier 4: Enterprise Data & Cache Layer -->
      <g transform="translate(30, 490)">
        <rect width="540" height="85" rx="12" fill="#ffffff" stroke="#7c3aed" stroke-width="1.5" filter="url(#softCardShadow)"/>
        <text x="20" y="24" fill="#3b0764" class="mono" font-size="11" font-weight="800">DATA PERSISTENCE &amp; IN-MEMORY ACCELERATION</text>

        <g transform="translate(20, 35)">
          <rect width="245" height="38" rx="8" fill="#f5f3ff" stroke="#7c3aed" stroke-width="1"/>
          <text x="122" y="23" fill="#3b0764" class="sans" font-size="11" font-weight="800" text-anchor="middle">🐘 PostgreSQL Enterprise Cluster</text>
        </g>
        <g transform="translate(275, 35)">
          <rect width="245" height="38" rx="8" fill="#fdf2f8" stroke="#db2777" stroke-width="1"/>
          <text x="122" y="23" fill="#9d174d" class="sans" font-size="11" font-weight="800" text-anchor="middle">⚡ Redis Distributed Caching</text>
        </g>
      </g>

      <!-- Tier 5: Academy Talent Pipeline (Bottom Link) -->
      <g transform="translate(30, 595)">
        <rect width="540" height="80" rx="12" fill="#f5f3ff" stroke="#a855f7" stroke-width="1.2"/>
        <text x="270" y="28" fill="#3b0764" class="sans" font-size="13" font-weight="900" text-anchor="middle">SPUTNIK DEVS ACADEMY // TALENT PIPELINE</text>
        <text x="270" y="48" fill="#6b21a8" class="mono" font-size="11" font-weight="700" text-anchor="middle">Work-Integrated Learning (WIL) • Engineering Production Systems</text>
        <text x="270" y="66" fill="#64748b" class="sans" font-size="10" text-anchor="middle">Graduates build and maintain these mission-critical cloud backends.</text>
      </g>
    </g>


    <!-- 1C. RIGHT POD: SAAS & ACADEMY INTERACTIVE SCAN LAUNCHPAD (X: 1225..1775) -->
    <g transform="translate(1225, 25)">
      <rect width="550" height="700" rx="24" fill="url(#cardGradWhite)" stroke="#7c3aed" stroke-width="2" filter="url(#softCardShadow)"/>
      <rect width="550" height="54" rx="24" fill="url(#zahaPurple3)" opacity="0.12"/>
      <line x1="0" y1="54" x2="550" y2="54" stroke="#7c3aed" stroke-width="1.5" stroke-opacity="0.4"/>

      <!-- Pod Header -->
      <g transform="translate(20, 15)">
        <circle cx="12" cy="12" r="8" fill="#a855f7"/>
        <text x="30" y="17" fill="#3b0764" class="sans" font-size="16" font-weight="900" letter-spacing="1">SPUTNIK DEVS // ENTERPRISE SAAS &amp; WIL</text>
        <rect x="420" y="0" width="110" height="24" rx="12" fill="#faf5ff" stroke="#a855f7" stroke-width="1"/>
        <text x="475" y="16" fill="#7c3aed" class="mono" font-size="10" font-weight="800" text-anchor="middle">STUDIO LIVE</text>
      </g>

      <!-- Row 1: Student Res & UniHub Scan Pad -->
      <g transform="translate(25, 75)">
        <rect width="500" height="185" rx="14" fill="#ffffff" stroke="#c084fc" stroke-width="1.2" filter="url(#softCardShadow)"/>
        <!-- QR Code -->
        <g transform="translate(15, 15)">
          <rect width="155" height="155" rx="12" fill="#faf5ff" stroke="#7c3aed" stroke-width="1"/>
          <path d="{qr_unihub}" fill="#2e1065" transform="translate(12, 12) scale(0.32)"/>
        </g>
        <!-- Info -->
        <g transform="translate(185, 22)">
          <text x="0" y="16" fill="#1e1b4b" class="sans" font-size="15" font-weight="900">Student Res + UniHub Portal</text>
          <text x="0" y="34" fill="#6b21a8" class="mono" font-size="10" font-weight="700">CAMPUS ACCOMMODATION SAAS</text>
          
          <text x="0" y="58" fill="#475569" class="sans" font-size="11">✓ Biometric &amp; Facial Recognition Access</text>
          <text x="0" y="76" fill="#475569" class="sans" font-size="11">✓ Room Allocation &amp; Lease Agreements</text>
          <text x="0" y="94" fill="#475569" class="sans" font-size="11">✓ NSFAS / Bursary Automated Invoicing</text>
          <text x="0" y="112" fill="#475569" class="sans" font-size="11">✓ Maintenance SOS &amp; Incident Ticketing</text>
          
          <g transform="translate(0, 124)">
            <rect width="295" height="26" rx="6" fill="#faf5ff" stroke="#7c3aed" stroke-width="1"/>
            <text x="147" y="17" fill="#581c87" class="mono" font-size="10" font-weight="800" text-anchor="middle">🔗 sputnikdevs.com/products/hostel</text>
          </g>
        </g>
      </g>

      <!-- Row 2: Shopnik E-Commerce Scan Pad -->
      <g transform="translate(25, 275)">
        <rect width="500" height="195" rx="14" fill="#ffffff" stroke="#c084fc" stroke-width="1.2" filter="url(#softCardShadow)"/>
        <!-- QR Code -->
        <g transform="translate(15, 15)">
          <rect width="165" height="165" rx="12" fill="#faf5ff" stroke="#7c3aed" stroke-width="1"/>
          <path d="{qr_shopnik}" fill="#2e1065" transform="translate(14, 14) scale(0.34)"/>
        </g>
        <!-- Info -->
        <g transform="translate(195, 22)">
          <text x="0" y="16" fill="#1e1b4b" class="sans" font-size="15" font-weight="900">Shopnik E-Commerce SaaS</text>
          <rect x="0" y="24" width="135" height="18" rx="4" fill="#f0fdf4"/>
          <text x="6" y="37" fill="#166534" class="mono" font-size="10" font-weight="800">STARTS AT R349/MO</text>
          
          <text x="0" y="60" fill="#475569" class="sans" font-size="11">✓ Native SA: Paystack, PayFast, COD &amp; Collection</text>
          <text x="0" y="78" fill="#475569" class="sans" font-size="11">✓ Multi-Variant Matrices (Sizes, Colors, Swatches)</text>
          <text x="0" y="96" fill="#475569" class="sans" font-size="11">✓ In-Country Oracle Cloud SA Hosting (Joburg)</text>
          <text x="0" y="114" fill="#475569" class="sans" font-size="11">✓ Store Admin Dashboard, Analytics &amp; Coupons</text>

          <g transform="translate(0, 126)">
            <rect width="285" height="26" rx="6" fill="#faf5ff" stroke="#7c3aed" stroke-width="1"/>
            <text x="142" y="17" fill="#581c87" class="mono" font-size="10" font-weight="800" text-anchor="middle">🔗 sputnikdevs.com/products/ecommerce</text>
          </g>
        </g>
      </g>

      <!-- Row 3: Devs Academy WIL Scan Pad -->
      <g transform="translate(25, 485)">
        <rect width="500" height="195" rx="14" fill="#faf5ff" stroke="#7c3aed" stroke-width="1.5" filter="url(#softCardShadow)"/>
        <!-- QR Code -->
        <g transform="translate(15, 15)">
          <rect width="165" height="165" rx="12" fill="#ffffff" stroke="#7c3aed" stroke-width="1"/>
          <path d="{qr_acad}" fill="#2e1065" transform="translate(14, 14) scale(0.34)"/>
        </g>
        <!-- Info -->
        <g transform="translate(195, 20)">
          <text x="0" y="16" fill="#1e1b4b" class="sans" font-size="15" font-weight="900">Sputnik Devs Academy (WIL)</text>
          <text x="0" y="34" fill="#7c3aed" class="mono" font-size="10" font-weight="700">WORK-INTEGRATED LEARNING</text>
          
          <text x="0" y="56" fill="#475569" class="sans" font-size="11">⚙️ Backend: REST &amp; gRPC Microservices</text>
          <text x="0" y="74" fill="#475569" class="sans" font-size="11">📱 Mobile: Cross-Platform Flutter</text>
          <text x="0" y="92" fill="#475569" class="sans" font-size="11">🚀 DevOps: Automated CI/CD Pipelines</text>
          <text x="0" y="110" fill="#475569" class="sans" font-size="11">🤖 Applied AI: Autonomous Workflow Agents</text>

          <g transform="translate(0, 122)">
            <rect width="285" height="28" rx="6" fill="#7c3aed"/>
            <text x="142" y="18" fill="#ffffff" class="mono" font-size="11" font-weight="800" text-anchor="middle">SCAN TO APPLY // WIL INTAKE ↗</text>
          </g>
        </g>
      </g>
    </g>

  </g>


  <!-- =================================================================== -->
  <!-- ZONE 2: FRONT AISLE BILLBOARD (2600 x 950 mm, Y: 1875..2825)       -->
  <!-- Facing visitors walking down the exhibition aisle                   -->
  <!-- =================================================================== -->
  <g transform="translate(200, 1875)">

    <!-- Outer Frame Card with Soft Ambient Shadow -->
    <rect width="2600" height="920" rx="32" fill="#ffffff" stroke="#7c3aed" stroke-width="2.5" filter="url(#deepCardShadow)"/>
    <rect width="2600" height="920" rx="32" fill="url(#cardGradWhite)"/>

    <!-- Top Billboard Header Ribbon -->
    <g transform="translate(0, 0)">
      <rect width="2600" height="110" rx="32" fill="url(#zahaPurple1)" opacity="0.10"/>
      <line x1="0" y1="110" x2="2600" y2="110" stroke="#7c3aed" stroke-width="2" stroke-opacity="0.3"/>

      <!-- Evergreen Showcase Badge -->
      <g transform="translate(1300, 24)">
        <rect x="-170" y="0" width="340" height="30" rx="15" fill="#ffffff" stroke="#7c3aed" stroke-width="1.5" filter="url(#softCardShadow)"/>
        <circle cx="-145" cy="15" r="5" fill="#7c3aed"/>
        <text x="0" y="20" fill="#581c87" class="mono" font-size="12" font-weight="800" letter-spacing="2" text-anchor="middle">SOUTH AFRICA TECH SHOWCASE</text>
      </g>

      <!-- Main Headline & Subtitle -->
      <text x="1300" y="78" fill="#1e1b4b" class="sans" font-size="34" font-weight="900" letter-spacing="1" text-anchor="middle">THE SPUTNIK TECH ECOSYSTEM</text>
      <text x="1300" y="100" fill="#6b21a8" class="sans" font-size="14" font-weight="700" letter-spacing="0.5" text-anchor="middle">Connecting Campus Marketplace Commerce with Enterprise Cloud Software</text>

      <!-- Left Corporate Logo -->
      <g transform="translate(50, 18)">
        <image href="{sputnik_tech_logo}" x="0" y="0" width="220" height="74" preserveAspectRatio="xMidYMid meet"/>
      </g>

      <!-- Right Corporate Logo -->
      <g transform="translate(2330, 18)">
        <image href="{sputnik_devs_logo}" x="0" y="0" width="220" height="74" preserveAspectRatio="xMidYMid meet"/>
      </g>
    </g>

    <!-- Main Dual Split Content (Y: 125..770) -->
    <!-- LEFT WING: CONSUMER & CAMPUS MOBILE LABS (X: 40..1280, Width: 1240) -->
    <g transform="translate(40, 125)">
      <rect width="1240" height="635" rx="20" fill="#ffffff" stroke="#e9d5ff" stroke-width="1.5" filter="url(#softCardShadow)"/>
      
      <!-- Sub-Header Pill -->
      <g transform="translate(30, 20)">
        <rect width="360" height="30" rx="15" fill="#faf5ff" stroke="#7c3aed" stroke-width="1.2"/>
        <circle cx="20" cy="15" r="4" fill="#7c3aed"/>
        <text x="190" y="20" fill="#581c87" class="mono" font-size="11" font-weight="800" letter-spacing="1.5" text-anchor="middle">◀ CONSUMER &amp; CAMPUS MOBILE LABS</text>
      </g>

      <!-- Tradey Bay Primary Card Content -->
      <g transform="translate(30, 65)">
        <image href="{tradeybay_primary_logo}" x="0" y="0" width="180" height="52" preserveAspectRatio="xMidYMid meet"/>
        <rect x="195" y="10" width="90" height="26" rx="6" fill="#faf5ff" stroke="#7c3aed" stroke-width="1"/>
        <text x="240" y="27" fill="#6b21a8" class="mono" font-size="11" font-weight="800" text-anchor="middle">v2.0.4+31</text>
        <rect x="295" y="10" width="130" height="26" rx="6" fill="#f5f3ff" stroke="#a855f7" stroke-width="1"/>
        <text x="360" y="27" fill="#581c87" class="mono" font-size="10" font-weight="800" text-anchor="middle">OFFICIAL LAUNCH</text>

        <text x="0" y="80" fill="#1e1b4b" class="sans" font-size="20" font-weight="900">Multi-Vertical Campus Super App</text>
        <text x="0" y="102" fill="#475569" class="sans" font-size="12" font-weight="500">Free verified student marketplace with 0% seller commission.</text>
        <text x="0" y="120" fill="#475569" class="sans" font-size="12" font-weight="500">Trade textbooks, electronics, dorm essentials, and find verified off-campus student housing.</text>

        <!-- Feature Badges -->
        <g transform="translate(0, 138)">
          <rect width="185" height="30" rx="6" fill="#faf5ff" stroke="#e9d5ff" stroke-width="1"/>
          <text x="92" y="20" fill="#581c87" class="mono" font-size="11" font-weight="700" text-anchor="middle">🏷️ 0% Commission</text>

          <rect x="195" width="220" height="30" rx="6" fill="#faf5ff" stroke="#e9d5ff" stroke-width="1"/>
          <text x="305" y="20" fill="#581c87" class="mono" font-size="11" font-weight="700" text-anchor="middle">🏠 Student Housing Portal</text>
        </g>
        <g transform="translate(0, 176)">
          <rect width="210" height="30" rx="6" fill="#faf5ff" stroke="#e9d5ff" stroke-width="1"/>
          <text x="105" y="20" fill="#581c87" class="mono" font-size="11" font-weight="700" text-anchor="middle">📚 Classifieds &amp; Auctions</text>

          <rect x="220" width="195" height="30" rx="6" fill="#faf5ff" stroke="#e9d5ff" stroke-width="1"/>
          <text x="317" y="20" fill="#581c87" class="mono" font-size="11" font-weight="700" text-anchor="middle">💬 Encrypted In-App Chat</text>
        </g>

        <!-- Scannable QR Container -->
        <g transform="translate(0, 222)">
          <rect width="415" height="185" rx="16" fill="url(#qrLightBg)" stroke="#7c3aed" stroke-width="1.5" filter="url(#softCardShadow)"/>
          <!-- QR Code -->
          <g transform="translate(18, 18)">
            <rect width="148" height="148" rx="10" fill="#ffffff" stroke="#e9d5ff" stroke-width="1"/>
            <path d="{qr_tb}" fill="#2e1065" transform="translate(11, 11) scale(0.30)"/>
          </g>
          <!-- Badges & Instructions -->
          <g transform="translate(180, 24)">
            <text x="0" y="16" fill="#1e1b4b" class="sans" font-size="14" font-weight="800">Scan to Install Mobile App</text>
            <text x="0" y="34" fill="#6b21a8" class="mono" font-size="10" font-weight="700">ANDROID &amp; APPLE IOS</text>

            <g transform="translate(0, 50)">
              <rect width="215" height="34" rx="6" fill="#000000"/>
              <text x="107" y="22" fill="#ffffff" class="sans" font-size="11" font-weight="700" text-anchor="middle">▶ GET IT ON Google Play</text>
            </g>
            <g transform="translate(0, 92)">
              <rect width="215" height="34" rx="6" fill="#000000"/>
              <text x="107" y="22" fill="#ffffff" class="sans" font-size="11" font-weight="700" text-anchor="middle"> Download on App Store</text>
            </g>
          </g>
        </g>

        <!-- Compliance & Info Bar -->
        <g transform="translate(0, 422)">
          <rect width="415" height="34" rx="8" fill="#f5f3ff" stroke="#7c3aed" stroke-width="1"/>
          <text x="207" y="21" fill="#4c1d95" class="mono" font-size="10" font-weight="800" text-anchor="middle">🔒 100% POPIA COMPLIANT // RSA DATA PRIVACY</text>
        </g>
        <g transform="translate(0, 464)">
          <text x="207" y="20" fill="#64748b" class="sans" font-size="12" font-weight="600" text-anchor="middle">Direct App Inquiries: <tspan fill="#581c87" font-weight="800">info@sputniktechgroup.com</tspan></text>
        </g>
      </g>

      <!-- Smartphone Mockups (Side-by-Side on the Right of Left Wing) -->
      <g transform="translate(480, 55)">
        <!-- Phone 1: Light Mode -->
        <g transform="translate(0, 0)">
          <rect width="340" height="555" rx="36" fill="#0f172a" stroke="#cbd5e1" stroke-width="4" filter="url(#softCardShadow)"/>
          <rect x="6" y="6" width="328" height="543" rx="30" fill="#ffffff"/>
          <clipPath id="tcPhoneClipLight">
            <rect x="6" y="6" width="328" height="543" rx="30"/>
          </clipPath>
          <image href="{tradeybay_light_screenshot}" x="6" y="6" width="328" height="543" preserveAspectRatio="xMidYMid slice" clip-path="url(#tcPhoneClipLight)"/>
        </g>
        <!-- Phone 2: Dark Mode -->
        <g transform="translate(370, 0)">
          <rect width="340" height="555" rx="36" fill="#0f172a" stroke="#475569" stroke-width="4" filter="url(#softCardShadow)"/>
          <rect x="6" y="6" width="328" height="543" rx="30" fill="#090d16"/>
          <clipPath id="tcPhoneClipDark">
            <rect x="6" y="6" width="328" height="543" rx="30"/>
          </clipPath>
          <image href="{tradeybay_dark_screenshot}" x="6" y="6" width="328" height="543" preserveAspectRatio="xMidYMid slice" clip-path="url(#tcPhoneClipDark)"/>
        </g>
      </g>
    </g>


    <!-- RIGHT WING: ENTERPRISE SAAS & ACADEMY (X: 1320..2560, Width: 1240) -->
    <g transform="translate(1320, 125)">
      <rect width="1240" height="635" rx="20" fill="#ffffff" stroke="#e9d5ff" stroke-width="1.5" filter="url(#softCardShadow)"/>

      <!-- Sub-Header Pill -->
      <g transform="translate(30, 20)">
        <rect width="360" height="30" rx="15" fill="#faf5ff" stroke="#8b5cf6" stroke-width="1.2"/>
        <circle cx="20" cy="15" r="4" fill="#8b5cf6"/>
        <text x="190" y="20" fill="#581c87" class="mono" font-size="11" font-weight="800" letter-spacing="1.5" text-anchor="middle">ENTERPRISE SAAS &amp; ACADEMY ▶</text>
      </g>

      <!-- 3 Tier Cards (Horizontal Stack in Front Drape) -->
      <!-- CARD 1: Student Res & UniHub (X: 30..415) -->
      <g transform="translate(30, 65)">
        <rect width="380" height="545" rx="16" fill="#ffffff" stroke="#c084fc" stroke-width="1.2" filter="url(#softCardShadow)"/>
        <rect width="380" height="42" rx="16" fill="#f5f3ff"/>
        <line x1="0" y1="42" x2="380" y2="42" stroke="#e9d5ff" stroke-width="1"/>

        <text x="20" y="26" fill="#3b0764" class="sans" font-size="13" font-weight="900">STUDENT RES // UNIHUB</text>

        <g transform="translate(20, 55)">
          <text x="0" y="16" fill="#1e1b4b" class="sans" font-size="16" font-weight="900">Residence Management</text>
          <text x="0" y="32" fill="#7c3aed" class="mono" font-size="10" font-weight="700">INTERCONNECTED CAMPUS SAAS</text>

          <text x="0" y="58" fill="#475569" class="sans" font-size="11">✓ Biometric &amp; Facial Recognition Access</text>
          <text x="0" y="78" fill="#475569" class="sans" font-size="11">✓ Automated Room Allocation &amp; Leases</text>
          <text x="0" y="98" fill="#475569" class="sans" font-size="11">✓ NSFAS / Bursary Direct Invoicing</text>
          <text x="0" y="118" fill="#475569" class="sans" font-size="11">✓ UniHub Student Self-Service Portal</text>
          <text x="0" y="138" fill="#475569" class="sans" font-size="11">✓ Maintenance SOS &amp; Incident Dispatch</text>

          <!-- QR Code Container -->
          <g transform="translate(0, 160)">
            <rect width="340" height="150" rx="12" fill="#faf5ff" stroke="#7c3aed" stroke-width="1"/>
            <g transform="translate(15, 12)">
              <rect width="125" height="125" rx="8" fill="#ffffff" stroke="#e9d5ff" stroke-width="1"/>
              <path d="{qr_unihub}" fill="#2e1065" transform="translate(10, 10) scale(0.26)"/>
            </g>
            <g transform="translate(155, 25)">
              <text x="0" y="16" fill="#1e1b4b" class="sans" font-size="13" font-weight="800">Scan to Explore</text>
              <text x="0" y="32" fill="#6b21a8" class="mono" font-size="10" font-weight="700">UNIHUB PORTAL</text>
              <text x="0" y="52" fill="#64748b" class="sans" font-size="10">Direct live market page</text>
              <rect x="0" y="65" width="170" height="26" rx="6" fill="#7c3aed"/>
              <text x="85" y="82" fill="#ffffff" class="mono" font-size="9" font-weight="800" text-anchor="middle">VISIT UNIHUB ↗</text>
            </g>
          </g>

          <g transform="translate(0, 325)">
            <rect width="340" height="30" rx="6" fill="#f0fdf4" stroke="#86efac" stroke-width="1"/>
            <text x="170" y="20" fill="#166534" class="mono" font-size="10" font-weight="800" text-anchor="middle">🎓 Live Pilot in Johannesburg Res</text>
          </g>
        </g>
      </g>

      <!-- CARD 2: Shopnik E-Commerce (X: 430..815) -->
      <g transform="translate(430, 65)">
        <rect width="380" height="545" rx="16" fill="#ffffff" stroke="#c084fc" stroke-width="1.2" filter="url(#softCardShadow)"/>
        <rect width="380" height="42" rx="16" fill="#f5f3ff"/>
        <line x1="0" y1="42" x2="380" y2="42" stroke="#e9d5ff" stroke-width="1"/>

        <text x="20" y="26" fill="#3b0764" class="sans" font-size="13" font-weight="900">SHOPNIK // E-COMMERCE SAAS</text>

        <g transform="translate(20, 55)">
          <text x="0" y="16" fill="#1e1b4b" class="sans" font-size="16" font-weight="900">Modern Headless E-Commerce</text>
          <rect x="0" y="24" width="140" height="20" rx="4" fill="#f0fdf4"/>
          <text x="8" y="38" fill="#166534" class="mono" font-size="10" font-weight="800">STARTS AT R349/MO</text>

          <text x="0" y="64" fill="#475569" class="sans" font-size="11">✓ Paystack &amp; PayFast Gateways Built-In</text>
          <text x="0" y="84" fill="#475569" class="sans" font-size="11">✓ Cash on Delivery &amp; In-Store Collection</text>
          <text x="0" y="104" fill="#475569" class="sans" font-size="11">✓ Multi-Variant Matrices (Sizes, Colors)</text>
          <text x="0" y="124" fill="#475569" class="sans" font-size="11">✓ In-Country Oracle Cloud SA Hosting (JHB)</text>
          <text x="0" y="144" fill="#475569" class="sans" font-size="11">✓ Store Admin Dashboard &amp; Analytics</text>

          <!-- QR Code Container -->
          <g transform="translate(0, 160)">
            <rect width="340" height="150" rx="12" fill="#faf5ff" stroke="#7c3aed" stroke-width="1"/>
            <g transform="translate(15, 12)">
              <rect width="125" height="125" rx="8" fill="#ffffff" stroke="#e9d5ff" stroke-width="1"/>
              <path d="{qr_shopnik}" fill="#2e1065" transform="translate(10, 10) scale(0.26)"/>
            </g>
            <g transform="translate(155, 25)">
              <text x="0" y="16" fill="#1e1b4b" class="sans" font-size="13" font-weight="800">Scan to Launch Store</text>
              <text x="0" y="32" fill="#6b21a8" class="mono" font-size="10" font-weight="700">SHOPNIK SAAS</text>
              <text x="0" y="52" fill="#64748b" class="sans" font-size="10">South Africa Cloud Native</text>
              <rect x="0" y="65" width="170" height="26" rx="6" fill="#7c3aed"/>
              <text x="85" y="82" fill="#ffffff" class="mono" font-size="9" font-weight="800" text-anchor="middle">OPEN STORE ↗</text>
            </g>
          </g>

          <g transform="translate(0, 325)">
            <rect width="340" height="30" rx="6" fill="#eff6ff" stroke="#bfdbfe" stroke-width="1"/>
            <text x="170" y="20" fill="#1d4ed8" class="mono" font-size="10" font-weight="800" text-anchor="middle">☁️ 100% Hosted in South Africa</text>
          </g>
        </g>
      </g>

      <!-- CARD 3: Sputnik Devs Academy (X: 830..1215) -->
      <g transform="translate(830, 65)">
        <rect width="380" height="545" rx="16" fill="#faf5ff" stroke="#7c3aed" stroke-width="1.5" filter="url(#softCardShadow)"/>
        <rect width="380" height="42" rx="16" fill="#ede9fe"/>
        <line x1="0" y1="42" x2="380" y2="42" stroke="#c084fc" stroke-width="1"/>

        <text x="20" y="26" fill="#3b0764" class="sans" font-size="13" font-weight="900">SPUTNIK DEVS ACADEMY // WIL</text>

        <g transform="translate(20, 55)">
          <text x="0" y="16" fill="#1e1b4b" class="sans" font-size="16" font-weight="900">Work-Integrated Learning</text>
          <text x="0" y="32" fill="#7c3aed" class="mono" font-size="10" font-weight="700">PRODUCTION DISCIPLINES</text>

          <text x="0" y="58" fill="#475569" class="sans" font-size="11">⚙️ Backend: REST &amp; gRPC Microservices</text>
          <text x="0" y="78" fill="#475569" class="sans" font-size="11">📱 Mobile: Cross-Platform Flutter</text>
          <text x="0" y="98" fill="#475569" class="sans" font-size="11">🚀 DevOps: Automated CI/CD Pipelines</text>
          <text x="0" y="118" fill="#475569" class="sans" font-size="11">🐘 Databases: PostgreSQL &amp; Cloud Redis</text>
          <text x="0" y="138" fill="#475569" class="sans" font-size="11">🤖 Applied AI: Autonomous Workflow Agents</text>

          <!-- QR Code Container -->
          <g transform="translate(0, 160)">
            <rect width="340" height="150" rx="12" fill="#ffffff" stroke="#7c3aed" stroke-width="1"/>
            <g transform="translate(15, 12)">
              <rect width="125" height="125" rx="8" fill="#faf5ff" stroke="#e9d5ff" stroke-width="1"/>
              <path d="{qr_acad}" fill="#2e1065" transform="translate(10, 10) scale(0.26)"/>
            </g>
            <g transform="translate(155, 25)">
              <text x="0" y="16" fill="#1e1b4b" class="sans" font-size="13" font-weight="800">Scan to Apply</text>
              <text x="0" y="32" fill="#7c3aed" class="mono" font-size="10" font-weight="700">WIL LEARNERSHIPS</text>
              <text x="0" y="52" fill="#64748b" class="sans" font-size="10">CS Graduates &amp; Engineers</text>
              <rect x="0" y="65" width="170" height="26" rx="6" fill="#7c3aed"/>
              <text x="85" y="82" fill="#ffffff" class="mono" font-size="9" font-weight="800" text-anchor="middle">APPLY ONLINE ↗</text>
            </g>
          </g>

          <g transform="translate(0, 325)">
            <rect width="340" height="30" rx="6" fill="#fdf4ff" stroke="#f0abfc" stroke-width="1"/>
            <text x="170" y="20" fill="#a21caf" class="mono" font-size="10" font-weight="800" text-anchor="middle">🚀 Engineering Real African Tech</text>
          </g>
        </g>
      </g>
    </g>

    <!-- BOTTOM PANORAMIC EXECUTIVE BANNER (Y: 780..900) -->
    <g transform="translate(40, 785)">
      <rect width="2520" height="110" rx="18" fill="url(#zahaPurple1)" opacity="0.12"/>
      <rect width="2520" height="110" rx="18" fill="none" stroke="#7c3aed" stroke-width="1.8"/>

      <!-- Company & Contact Info -->
      <g transform="translate(40, 32)">
        <text x="0" y="0" fill="#1e1b4b" class="sans" font-size="18" font-weight="900">SPUTNIK TECH GROUP (PTY) LTD &amp; SPUTNIK DEVS STUDIO</text>
        <text x="0" y="24" fill="#581c87" class="mono" font-size="12" font-weight="700">📍 292 Surrey Avenue, Randburg, Johannesburg, 2194  |  Direct: takudzwam@sputniktechgroup.com  |  info@sputniktechgroup.com</text>
        <text x="0" y="46" fill="#64748b" class="mono" font-size="12">📞 South Africa: +27 66 321 5528  |  International: +263 787 015 123  |  sputniktechgroup.com  |  sputnikdevs.com</text>
      </g>

      <!-- Executive Leadership Endorsement -->
      <g transform="translate(1450, 32)">
        <rect width="1030" height="58" rx="12" fill="#ffffff" stroke="#7c3aed" stroke-width="1.2" filter="url(#softCardShadow)"/>
        <text x="515" y="24" fill="#3b0764" class="sans" font-size="13" font-weight="900" text-anchor="middle">Takudzwa Mupanesure — Founder, Chief Executive Officer &amp; Lead Architect</text>
        <text x="515" y="44" fill="#6b21a8" class="sans" font-size="11" font-weight="700" text-anchor="middle">In Concurrence with: Kenneth Takudzwa Katsande (Director of Operations) &amp; Prince Lwazi Nkiwane (Director of Growth)</text>
      </g>
    </g>

  </g>


  <!-- =================================================================== -->
  <!-- ZONE 3: LEFT SIDE SKIRT (X: 80..520, Y: 1145..1855)                 -->
  <!-- Facing left aisle foot traffic                                      -->
  <!-- =================================================================== -->
  <g transform="translate(80, 1145)">
    <rect width="440" height="710" rx="22" fill="#ffffff" stroke="#7c3aed" stroke-width="2" filter="url(#softCardShadow)"/>
    <rect width="440" height="50" rx="22" fill="url(#zahaPurple1)" opacity="0.12"/>
    <line x1="0" y1="50" x2="440" y2="50" stroke="#7c3aed" stroke-width="1.2"/>

    <text x="220" y="32" fill="#3b0764" class="sans" font-size="15" font-weight="900" letter-spacing="1" text-anchor="middle">SPUTNIK TECH GROUP</text>

    <!-- Content -->
    <g transform="translate(30, 80)">
      <image href="{tradeybay_primary_logo}" x="50" y="0" width="280" height="70" preserveAspectRatio="xMidYMid meet"/>

      <text x="190" y="105" fill="#1e1b4b" class="sans" font-size="18" font-weight="900" text-anchor="middle">Campus Super App</text>
      <text x="190" y="125" fill="#7c3aed" class="mono" font-size="11" font-weight="800" text-anchor="middle">VERSION v2.0.4+31</text>

      <!-- Scannable QR -->
      <g transform="translate(85, 145)">
        <rect width="210" height="210" rx="16" fill="#faf5ff" stroke="#7c3aed" stroke-width="1.5" filter="url(#softCardShadow)"/>
        <g transform="translate(18, 18)">
          <rect width="174" height="174" rx="10" fill="#ffffff"/>
          <path d="{qr_tb}" fill="#2e1065" transform="translate(12, 12) scale(0.36)"/>
        </g>
      </g>

      <text x="190" y="390" fill="#581c87" class="mono" font-size="12" font-weight="800" text-anchor="middle">📱 POINT CAMERA TO INSTALL</text>
      <text x="190" y="415" fill="#475569" class="sans" font-size="12" font-weight="600" text-anchor="middle">Google Play &amp; Apple App Store</text>

      <!-- 3 Key Badges -->
      <g transform="translate(10, 440)">
        <rect width="360" height="34" rx="8" fill="#faf5ff" stroke="#e9d5ff" stroke-width="1"/>
        <text x="180" y="22" fill="#581c87" class="sans" font-size="12" font-weight="700" text-anchor="middle">🏷️ 0% Commission for Students</text>

        <rect y="44" width="360" height="34" rx="8" fill="#faf5ff" stroke="#e9d5ff" stroke-width="1"/>
        <text x="180" y="66" fill="#581c87" class="sans" font-size="12" font-weight="700" text-anchor="middle">🏠 Verified Student Housing</text>

        <rect y="88" width="360" height="34" rx="8" fill="#faf5ff" stroke="#e9d5ff" stroke-width="1"/>
        <text x="180" y="110" fill="#581c87" class="sans" font-size="12" font-weight="700" text-anchor="middle">🔒 100% POPIA Compliant</text>
      </g>

      <g transform="translate(10, 580)">
        <rect width="360" height="32" rx="8" fill="#f5f3ff" stroke="#7c3aed" stroke-width="1"/>
        <text x="180" y="21" fill="#4c1d95" class="mono" font-size="10" font-weight="800" text-anchor="middle">info@sputniktechgroup.com</text>
      </g>
    </g>
  </g>


  <!-- =================================================================== -->
  <!-- ZONE 4: RIGHT SIDE SKIRT (X: 2480..2920, Y: 1145..1855)              -->
  <!-- Facing right aisle foot traffic                                     -->
  <!-- =================================================================== -->
  <g transform="translate(2480, 1145)">
    <rect width="440" height="710" rx="22" fill="#ffffff" stroke="#7c3aed" stroke-width="2" filter="url(#softCardShadow)"/>
    <rect width="440" height="50" rx="22" fill="url(#zahaPurple3)" opacity="0.12"/>
    <line x1="0" y1="50" x2="440" y2="50" stroke="#7c3aed" stroke-width="1.2"/>

    <text x="220" y="32" fill="#3b0764" class="sans" font-size="15" font-weight="900" letter-spacing="1" text-anchor="middle">SPUTNIK DEVS STUDIO</text>

    <!-- Content -->
    <g transform="translate(30, 75)">
      <image href="{sputnik_devs_logo}" x="40" y="0" width="300" height="70" preserveAspectRatio="xMidYMid meet"/>

      <text x="190" y="100" fill="#1e1b4b" class="sans" font-size="17" font-weight="900" text-anchor="middle">Enterprise Cloud &amp; WIL</text>
      <text x="190" y="120" fill="#7c3aed" class="mono" font-size="11" font-weight="800" text-anchor="middle">ACADEMY LEARNERSHIP</text>

      <!-- Scannable QR -->
      <g transform="translate(85, 140)">
        <rect width="210" height="210" rx="16" fill="#faf5ff" stroke="#7c3aed" stroke-width="1.5" filter="url(#softCardShadow)"/>
        <g transform="translate(18, 18)">
          <rect width="174" height="174" rx="10" fill="#ffffff"/>
          <path d="{qr_acad}" fill="#2e1065" transform="translate(12, 12) scale(0.36)"/>
        </g>
      </g>

      <text x="190" y="385" fill="#581c87" class="mono" font-size="12" font-weight="800" text-anchor="middle">🚀 POINT CAMERA TO APPLY</text>
      <text x="190" y="410" fill="#475569" class="sans" font-size="12" font-weight="600" text-anchor="middle">CS Graduates &amp; Tech Talent</text>

      <!-- 3 Key Badges -->
      <g transform="translate(10, 435)">
        <rect width="360" height="34" rx="8" fill="#faf5ff" stroke="#e9d5ff" stroke-width="1"/>
        <text x="180" y="22" fill="#581c87" class="sans" font-size="12" font-weight="700" text-anchor="middle">🏢 Student Residence Management</text>

        <rect y="44" width="360" height="34" rx="8" fill="#faf5ff" stroke="#e9d5ff" stroke-width="1"/>
        <text x="180" y="66" fill="#581c87" class="sans" font-size="12" font-weight="700" text-anchor="middle">🛍️ Shopnik SaaS (From R349/mo)</text>

        <rect y="88" width="360" height="34" rx="8" fill="#faf5ff" stroke="#e9d5ff" stroke-width="1"/>
        <text x="180" y="110" fill="#581c87" class="sans" font-size="12" font-weight="700" text-anchor="middle">🤖 Autonomous AI Workflows</text>
      </g>

      <g transform="translate(10, 580)">
        <rect width="360" height="32" rx="8" fill="#f5f3ff" stroke="#7c3aed" stroke-width="1"/>
        <text x="180" y="21" fill="#4c1d95" class="mono" font-size="10" font-weight="800" text-anchor="middle">sputnikdevs.com/academy</text>
      </g>
    </g>
  </g>


  <!-- =================================================================== -->
  <!-- ZONE 5: REAR OPERATOR TACTICAL HUD (X: 600..2400, Y: 350..1100)    -->
  <!-- Rotated 180° so it reads right-side-up to Kenneth & Prince          -->
  <!-- =================================================================== -->
  <g transform="translate(1500, 725) rotate(180)">
    <!-- Centered frame: 1800 x 700 mm (X: -900..900, Y: -350..350) -->
    <rect x="-900" y="-350" width="1800" height="700" rx="24" fill="#ffffff" stroke="#7c3aed" stroke-width="2" filter="url(#deepCardShadow)"/>
    <rect x="-900" y="-350" width="1800" height="54" rx="24" fill="url(#zahaPurple1)" opacity="0.12"/>
    <line x1="-900" y1="-296" x2="900" y2="-296" stroke="#7c3aed" stroke-width="1.5" stroke-opacity="0.4"/>

    <!-- HUD Header -->
    <text x="0" y="-315" fill="#3b0764" class="sans" font-size="18" font-weight="900" letter-spacing="1.5" text-anchor="middle">
      SPUTNIK BOOTH OPERATIONAL HUD // CHEAT SHEET FOR KENNETH &amp; PRINCE
    </text>

    <!-- 3 Tactical Columns (Width: 540 each) -->
    <!-- Col 1: Student 30-Sec Pitch (Left: X = -870..-330) -->
    <g transform="translate(-870, -270)">
      <rect width="540" height="590" rx="16" fill="#faf5ff" stroke="#c084fc" stroke-width="1.2"/>
      <rect width="540" height="38" rx="16" fill="#ede9fe"/>
      <text x="270" y="25" fill="#3b0764" class="sans" font-size="14" font-weight="900" text-anchor="middle">1. STUDENT 30-SEC ELEVATOR PITCH</text>

      <g transform="translate(25, 60)">
        <text x="0" y="0" fill="#581c87" class="mono" font-size="12" font-weight="800">HOOK: "Are you paying fees to sell your own books?"</text>
        
        <text x="0" y="26" fill="#1e1b4b" class="sans" font-size="12" font-weight="700">• 0% Commission Guarantee:</text>
        <text x="12" y="44" fill="#475569" class="sans" font-size="11">"Unlike generic classifieds, Tradey Bay takes zero cut from verified students."</text>

        <text x="0" y="74" fill="#1e1b4b" class="sans" font-size="12" font-weight="700">• Student Housing Without Scams:</text>
        <text x="12" y="92" fill="#475569" class="sans" font-size="11">"Verified student rooms, off-campus subleases &amp; dorm listings."</text>

        <text x="0" y="122" fill="#1e1b4b" class="sans" font-size="12" font-weight="700">• Safety &amp; Trust:</text>
        <text x="12" y="140" fill="#475569" class="sans" font-size="11">"Campus-gated verification, in-app messaging, no phone numbers exposed."</text>

        <text x="0" y="170" fill="#1e1b4b" class="sans" font-size="12" font-weight="700">• Call to Action:</text>
        <text x="12" y="188" fill="#475569" class="sans" font-size="11">"Point your phone right now at the table pad — live on Android &amp; iOS!"</text>

        <!-- Rapid Conversion Metric -->
        <g transform="translate(0, 230)">
          <rect width="490" height="110" rx="12" fill="#ffffff" stroke="#7c3aed" stroke-width="1"/>
          <text x="245" y="28" fill="#3b0764" class="mono" font-size="12" font-weight="800" text-anchor="middle">TRADEY BAY QUICK METRICS</text>
          <text x="245" y="52" fill="#7c3aed" class="sans" font-size="12" font-weight="700" text-anchor="middle">Latest Version: v2.0.4+31 • 100% POPIA Compliant</text>
          <text x="245" y="74" fill="#64748b" class="sans" font-size="11" text-anchor="middle">Categories: Textbooks • Laptops • Dorm Gear • Housing</text>
          <text x="245" y="94" fill="#166534" class="mono" font-size="11" font-weight="800" text-anchor="middle">0% Transaction Fees for Student Accounts</text>
        </g>
      </g>
    </g>

    <!-- Col 2: Residence Manager & Merchant Pitch (Center: X = -270..270) -->
    <g transform="translate(-270, -270)">
      <rect width="540" height="590" rx="16" fill="#faf5ff" stroke="#c084fc" stroke-width="1.2"/>
      <rect width="540" height="38" rx="16" fill="#ede9fe"/>
      <text x="270" y="25" fill="#3b0764" class="sans" font-size="14" font-weight="900" text-anchor="middle">2. RES MANAGER &amp; SHOPNIK PITCH</text>

      <g transform="translate(25, 60)">
        <text x="0" y="0" fill="#581c87" class="mono" font-size="12" font-weight="800">HOOK: "Turnkey Student Housing &amp; SA E-Commerce"</text>

        <text x="0" y="26" fill="#1e1b4b" class="sans" font-size="12" font-weight="700">• Student Res Management System (SRMS):</text>
        <text x="12" y="44" fill="#475569" class="sans" font-size="11">"Biometric entry, automated room allocations, lease signing &amp; NSFAS billing."</text>

        <text x="0" y="74" fill="#1e1b4b" class="sans" font-size="12" font-weight="700">• The University Hub Integration:</text>
        <text x="12" y="92" fill="#475569" class="sans" font-size="11">"Students view rooms, request repairs &amp; manage residency on one mobile portal."</text>

        <text x="0" y="122" fill="#1e1b4b" class="sans" font-size="12" font-weight="700">• Shopnik SaaS Platform:</text>
        <text x="12" y="140" fill="#475569" class="sans" font-size="11">"Starts at R349/month. Paystack, PayFast, COD, In-Store Pickup built-in."</text>

        <text x="0" y="170" fill="#1e1b4b" class="sans" font-size="12" font-weight="700">• In-Country Sovereign Hosting:</text>
        <text x="12" y="188" fill="#475569" class="sans" font-size="11">"100% Hosted in Johannesburg on Oracle Cloud SA. Low-latency, ultra-fast."</text>

        <!-- Pricing Callout Box -->
        <g transform="translate(0, 230)">
          <rect width="490" height="110" rx="12" fill="#ffffff" stroke="#7c3aed" stroke-width="1"/>
          <text x="245" y="28" fill="#3b0764" class="mono" font-size="12" font-weight="800" text-anchor="middle">COMMERCIAL LICENSING CHEAT SHEET</text>
          <text x="245" y="52" fill="#166534" class="sans" font-size="12" font-weight="800" text-anchor="middle">Shopnik: Starts at R349 / month (Paystack, PayFast, COD)</text>
          <text x="245" y="74" fill="#6b21a8" class="sans" font-size="11" font-weight="700" text-anchor="middle">SRMS / UniHub: Tiered SaaS per bed / campus licensing</text>
          <text x="245" y="94" fill="#581c87" class="mono" font-size="11" text-anchor="middle">Book Demo: takudzwam@sputniktechgroup.com</text>
        </g>
      </g>
    </g>

    <!-- Col 3: Academy Pitch & Leadership Emergency Hub (Right: X = 330..870) -->
    <g transform="translate(330, -270)">
      <rect width="540" height="590" rx="16" fill="#faf5ff" stroke="#c084fc" stroke-width="1.2"/>
      <rect width="540" height="38" rx="16" fill="#ede9fe"/>
      <text x="270" y="25" fill="#3b0764" class="sans" font-size="14" font-weight="900" text-anchor="middle">3. ACADEMY &amp; LEADERSHIP CHEAT SHEET</text>

      <g transform="translate(25, 60)">
        <text x="0" y="0" fill="#581c87" class="mono" font-size="12" font-weight="800">HOOK: "Building production software, not tutorials."</text>

        <text x="0" y="26" fill="#1e1b4b" class="sans" font-size="12" font-weight="700">• Work-Integrated Learning (WIL):</text>
        <text x="12" y="44" fill="#475569" class="sans" font-size="11">"CS graduates build real cloud backends, Flutter mobile apps &amp; AI agents."</text>

        <text x="0" y="74" fill="#1e1b4b" class="sans" font-size="12" font-weight="700">• Production Disciplines:</text>
        <text x="12" y="92" fill="#475569" class="sans" font-size="11">"Backend REST &amp; gRPC • Flutter • DevOps CI/CD • Postgres/Redis • AI."</text>

        <!-- Leadership Contacts -->
        <g transform="translate(0, 130)">
          <rect width="490" height="210" rx="12" fill="#ffffff" stroke="#7c3aed" stroke-width="1.2"/>
          <text x="245" y="24" fill="#3b0764" class="sans" font-size="13" font-weight="900" text-anchor="middle">EXECUTIVE DIRECTORY &amp; ESCALATION</text>

          <text x="20" y="52" fill="#1e1b4b" class="sans" font-size="11" font-weight="800">Takudzwa Mupanesure</text>
          <text x="20" y="68" fill="#581c87" class="sans" font-size="10">Founder, CEO &amp; Lead Architect  |  +27 66 321 5528  |  +263 787 015 123</text>
          <text x="20" y="84" fill="#64748b" class="mono" font-size="10">takudzwam@sputniktechgroup.com</text>

          <line x1="20" y1="96" x2="470" y2="96" stroke="#e9d5ff" stroke-width="1"/>

          <text x="20" y="116" fill="#1e1b4b" class="sans" font-size="11" font-weight="800">Kenneth Takudzwa Katsande</text>
          <text x="20" y="132" fill="#581c87" class="sans" font-size="10">Director of Operations  |  Sputnik Tech Group</text>

          <line x1="20" y1="144" x2="470" y2="144" stroke="#e9d5ff" stroke-width="1"/>

          <text x="20" y="164" fill="#1e1b4b" class="sans" font-size="11" font-weight="800">Prince Lwazi Nkiwane</text>
          <text x="20" y="180" fill="#581c87" class="sans" font-size="10">Director of Growth  |  Sputnik Tech Group</text>
        </g>
      </g>
    </g>

  </g>

</svg>"""
    return svg

def main():
    print("Generating Zaha Hadid Light-Theme Exhibition Tablecloth (3m x 3m)...")
    svg_content = build_tablecloth_svg()
    out_path = os.path.join(REPO_ROOT, "designs", "table-cloth-3x3m", "tablecloth.svg")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(svg_content)
    size_kb = os.path.getsize(out_path) / 1024
    print(f"✅ Generated: {out_path} ({size_kb:.1f} KB)")

if __name__ == "__main__":
    main()
