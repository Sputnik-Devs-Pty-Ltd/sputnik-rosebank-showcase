#!/usr/bin/env python3
"""
Sputnik Rosebank Showcase 2026 - High-Resolution PDF Exporter
Automates headless Chrome rendering to produce exact-dimension, 1:1 scale print PDFs.
"""

import os
import sys
import shutil
import subprocess

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

TARGETS = [
    {
        "name": "Pull-Up Banner (1m x 2m)",
        "input_html": os.path.join(REPO_ROOT, "designs", "banner-1x2m", "banner-print.html"),
        "output_pdf": os.path.join(REPO_ROOT, "designs", "banner-1x2m", "banner.pdf"),
        "dimensions": "1000mm x 2000mm"
    },
    {
        "name": "Exhibition Table Cloth (3m x 3m)",
        "input_html": os.path.join(REPO_ROOT, "designs", "table-cloth-3x3m", "tablecloth-print.html"),
        "output_pdf": os.path.join(REPO_ROOT, "designs", "table-cloth-3x3m", "tablecloth.pdf"),
        "dimensions": "3000mm x 3000mm"
    },
    {
        "name": "Staff T-Shirts (Prince & Kenneth DTF Gang Sheet)",
        "input_html": os.path.join(REPO_ROOT, "designs", "shirts", "shirt-print.html"),
        "output_pdf": os.path.join(REPO_ROOT, "designs", "shirts", "shirts-dtf.pdf"),
        "dimensions": "DTF Production Sheets"
    },
    {
        "name": "Handheld Print Flyer (A5: 148mm x 210mm)",
        "input_html": os.path.join(REPO_ROOT, "designs", "flyer", "flyer-print.html"),
        "output_pdf": os.path.join(REPO_ROOT, "designs", "flyer", "flyer-a5.pdf"),
        "dimensions": "148mm x 210mm"
    }
]

def find_chrome():
    candidates = [
        "google-chrome",
        "google-chrome-stable",
        "chromium-browser",
        "chromium",
        "/usr/bin/google-chrome",
        "/usr/bin/chromium-browser",
        "/usr/bin/chromium",
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
        "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe",
    ]
    for candidate in candidates:
        if shutil.which(candidate) or os.path.isfile(candidate):
            return candidate
    return None

def export_pdf(chrome_bin, target):
    name = target["name"]
    input_html = target["input_html"]
    output_pdf = target["output_pdf"]
    dim = target["dimensions"]

    print(f"\n⏳ Rendering '{name}' [{dim}]...")
    if not os.path.isfile(input_html):
        print(f"❌ Input file not found: {input_html}")
        return False

    import tempfile
    user_data_dir = tempfile.mkdtemp(prefix="chrome_pdf_")
    file_url = f"file://{os.path.abspath(input_html)}"
    
    cmd = [
        chrome_bin,
        "--headless=new",
        "--disable-gpu",
        "--no-sandbox",
        "--disable-dev-shm-usage",
        "--disable-background-networking",
        "--disable-extensions",
        "--no-first-run",
        f"--user-data-dir={user_data_dir}",
        "--no-pdf-header-footer",
        f"--print-to-pdf={output_pdf}",
        file_url
    ]

    try:
        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=300)
        if os.path.isfile(output_pdf) and os.path.getsize(output_pdf) > 0:
            size_mb = os.path.getsize(output_pdf) / (1024 * 1024)
            print(f"✅ Created: {output_pdf} ({size_mb:.2f} MB)")
            return True
        else:
            print(f"❌ Failed to generate PDF. Chrome output:\n{result.stderr}")
            return False
    except subprocess.TimeoutExpired:
        print(f"❌ Rendering timed out after 300s.")
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False
    finally:
        shutil.rmtree(user_data_dir, ignore_errors=True)

def main():
    print("=" * 70)
    print("Sputnik Tech Group & Sputnik Devs Studio — High-Res Print PDF Engine")
    print("=" * 70)

    chrome_bin = find_chrome()
    if not chrome_bin:
        print("❌ Could not find Google Chrome or Chromium installed.")
        print("Please install Google Chrome or use the browser's native 'Print to PDF' dialog.")
        sys.exit(1)

    print(f"Using Chrome binary: {chrome_bin}")

    success_count = 0
    for target in TARGETS:
        if export_pdf(chrome_bin, target):
            success_count += 1

    print("\n" + "=" * 70)
    print(f"Completed: {success_count}/{len(TARGETS)} PDFs exported successfully!")
    print("The PDF files are ready to be sent directly to the print shop in Rosebank!")
    print("=" * 70)

if __name__ == "__main__":
    main()
