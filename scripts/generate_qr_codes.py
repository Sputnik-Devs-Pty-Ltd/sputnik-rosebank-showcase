#!/usr/bin/env python3
"""
Sputnik Showcase 2026 - QR Code Generator
Generates high-precision, scalable SVG and PNG QR codes for all showcase touchpoints.
"""

import os
import qrcode
import qrcode.image.svg

DEST_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'assets', 'qr'))
os.makedirs(DEST_DIR, exist_ok=True)

QR_TARGETS = [
    {
        "id": "qr-tradeybay-playstore",
        "title": "Tradey Bay - Google Play Store",
        "url": "https://play.google.com/store/apps/details?id=com.sputniktech.tradey_bay_mobile",
        "box_size": 12,
        "border": 2
    },
    {
        "id": "qr-academy-apply",
        "title": "Sputnik Devs Academy - Learnership Application",
        "url": "https://sputnikdevs.com/academy/apply",
        "box_size": 12,
        "border": 2
    },
    {
        "id": "qr-student-housing-srms",
        "title": "Student Residence Management & University Hub",
        "url": "https://sputnikdevs.com/products/hostel",
        "box_size": 12,
        "border": 2
    },
    {
        "id": "qr-shopnik-ecommerce",
        "title": "Shopnik E-Commerce SaaS",
        "url": "https://sputnikdevs.com/products/ecommerce",
        "box_size": 12,
        "border": 2
    },
    {
        "id": "qr-sputnik-tech-group",
        "title": "Sputnik Tech Group Website",
        "url": "https://sputniktechgroup.com",
        "box_size": 12,
        "border": 2
    },
    {
        "id": "qr-sputnik-devs",
        "title": "Sputnik Devs Studio Portal",
        "url": "https://sputnikdevs.com",
        "box_size": 12,
        "border": 2
    }
]

def generate_svg_qr(target):
    factory = qrcode.image.svg.SvgPathImage
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=target["box_size"],
        border=target["border"],
        image_factory=factory
    )
    qr.add_data(target["url"])
    qr.make(fit=True)
    img = qr.make_image(attrib={'class': f'qr-code-svg {target["id"]}'})
    
    svg_path = os.path.join(DEST_DIR, f"{target['id']}.svg")
    img.save(svg_path)
    print(f"✓ Generated SVG: {svg_path} -> {target['url']}")

def generate_png_qr(target):
    try:
        qr = qrcode.QRCode(
            version=None,
            error_correction=qrcode.constants.ERROR_CORRECT_M,
            box_size=target["box_size"],
            border=target["border"]
        )
        qr.add_data(target["url"])
        qr.make(fit=True)
        img = qr.make_image(fill_color="#000000", back_color="#ffffff")
        png_path = os.path.join(DEST_DIR, f"{target['id']}.png")
        img.save(png_path)
        print(f"✓ Generated PNG: {png_path}")
    except Exception as e:
        print(f"Note: PNG generation skipped or needs Pillow ({e})")

def main():
    print("=" * 60)
    print("Sputnik Tech Group & Sputnik Devs Studio - QR Code Engine")
    print("=" * 60)
    for target in QR_TARGETS:
        generate_svg_qr(target)
        generate_png_qr(target)
    print("\nAll QR codes generated successfully in assets/qr/")

if __name__ == "__main__":
    main()
