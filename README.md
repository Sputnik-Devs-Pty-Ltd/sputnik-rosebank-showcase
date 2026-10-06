# 🚀 Sputnik Tech Group & Sputnik Devs Studio — Rosebank Showcase 2026

Official high-resolution print assets, interactive exhibition web viewer, scalable vector artwork, and production files for the **Rosebank Tech Showcase (Johannesburg, South Africa)**.

---

## 🏢 Dual Company Ecosystem & Showcase Touchpoints

1. **Sputnik Tech Group (Consumer & Mobile Tech Ecosystem)**
   * **Flagship Product:** **Tradey Bay App (v2.0.4+31)**
   * *Status:* Live on Google Play Store (Android), Apple App Store (Coming Soon).
   * *Platform Pillars:*
     - **Multi-Vertical Marketplace:** 0% commission classifieds across Vehicles, Solar/Energy, Electronics, Dorm Gear & Student Essentials.
     - **Real-Time Auctions:** SignalR live digital bidding with automatic anti-snipe 60-second countdown extensions.
     - **Native AI ATS Resume Builder:** 4 ATS-optimized templates, instant PDF generation, and algorithmic candidate-vacancy matching.
     - **CIPC Branded Storefronts & Split Maps:** Verified merchant profiles with split-view Google Maps and geo-radius discovery.
     - **Direct Messaging & Student Verification:** Real-time in-app chat negotiation and verified student identities with zero listing fees.
   * *Play Store:* [Tradey Bay on Google Play](https://play.google.com/store/apps/details?id=com.sputniktech.tradey_bay_mobile)
   * *Portal:* [sputniktechgroup.com](https://sputniktechgroup.com)

2. **Sputnik Devs Studio (Enterprise Engineering & B2B SaaS)**
   * **Student Residence Management System (SRMS):** End-to-end digital accommodation, room allocation, maintenance ticketing & student housing administration.
   * **The University Hub:** Sister platform for campus life, university societies, academic forums & student services.
   * **Shopnik E-Commerce SaaS:** Multi-tier e-commerce engine starting from R349/month with 0% platform commission, pre-integrated SA payments (Paystack & PayFast, COD, In-Store Collection), admin store dashboard, and built-in AI recommendations.
   * **Sputnik Devs Academy:** Accredited 19-day & 3-month Work-Integrated Learning (WIL) learnerships for tech students (.NET 10, Cloud, AI Agents, Microservices).
   * *Portal:* [sputnikdevs.com](https://sputnikdevs.com) | [Apply for Learnerships](https://sputnikdevs.com/academy/apply)

---

## 📦 What's Inside This Repository

```
sputnik-rosebank-showcase/
├── assets/
│   ├── logos/                     # Sputnik Devs, Sputnik Tech, Tradey Bay, Shopnik, Hostel logos
│   ├── qr/                        # High-precision vector SVG & PNG QR codes
│   └── badges/                    # Google Play, App Store, Tech stack badges
├── designs/
│   ├── banner-1x2m/               # 1m x 2m Roll-up Standing Pull-Up Banner
│   │   ├── banner.svg             # 1:1 Scalable Vector SVG
│   │   ├── banner-print.html      # Print stylesheet (@page { size: 1000mm 2000mm })
│   │   └── banner-spec.md         # Print shop specifications
│   ├── table-cloth-3x3m/          # 3m x 3m Exhibition Table Drape
│   │   ├── tablecloth.svg         # 1:1 Scalable Vector with tabletop scan pads
│   │   ├── tablecloth-print.html  # Full fabric print stylesheet
│   │   └── tablecloth-spec.md     # Fabric & hem specifications
│   └── shirts/                    # Staff Showcase T-Shirts
│       ├── shirt-prince.svg       # Prince (Tech Ops & Dev) Front & Back mockup
│       ├── shirt-kenneth.svg      # Kenneth (COO & Product) Front & Back mockup
│       ├── shirt-print.html       # Direct-to-Film (DTF) gang sheet layout
│       └── shirt-spec.md          # Apparel DTF print specifications
├── viewer/                        # Interactive Web Studio & Previewer
│   ├── index.html                 # 2D Canvas Viewer, QR testing, print triggers
│   ├── viewer.css                 # Cyber-glassmorphism dark UI
│   └── viewer.js                  # View switching, zoom & pan controls
├── scripts/
│   ├── generate_qr_codes.py       # Python script generating vector SVG QR codes
│   ├── export_highres_pdf.py      # Automated headless Chrome print-to-PDF engine
│   └── serve_viewer.py            # Zero-dependency local web server
├── PRINTING_INSTRUCTIONS_JOBURG.md # On-the-ground action guide for Prince & Kenneth
└── README.md
```

---

## 🖥️ How to Run the Interactive Showcase Viewer

You can launch the interactive preview app in seconds using Python:

```bash
cd sputnik-rosebank-showcase
python3 scripts/serve_viewer.py
```
Open your browser to: **`http://localhost:8080/viewer`**

From the viewer, you can:
* Inspect the 1m x 2m pull-up banner with zoom & pan.
* Preview how the 3m x 3m table cloth drapes across a standard 1.8m table.
* Switch between Prince's and Kenneth's custom shirts.
* Scan and test every single live QR code on your phone screen.
* Download print-ready SVGs or jump directly to print stylesheets.

---

## 🖨️ Automated PDF Export Script

To render ultra-high-resolution print-ready PDFs directly via Google Chrome:

```bash
python3 scripts/export_highres_pdf.py
```

This generates:
* `designs/banner-1x2m/banner.pdf`
* `designs/table-cloth-3x3m/tablecloth.pdf`
* `designs/shirts/shirts-dtf.pdf`

---

## 👥 On-the-Ground Showcase Representatives (Joburg)
* **Prince** — Head of Tech & Operations
* **Kenneth** — Chief Operating Officer (COO) & Product Lead

See [`PRINTING_INSTRUCTIONS_JOBURG.md`](file:///home/sputniktech/repos/sputnik-rosebank-showcase/PRINTING_INSTRUCTIONS_JOBURG.md) for step-by-step instructions for print shops in Rosebank / Sandton / Braamfontein.
