#!/usr/bin/env python3
"""
Sputnik Rosebank Showcase 2026 - Interactive Design & Print Viewer Server
Spins up a lightweight local server to preview all designs, QR codes, and print templates.
"""

import os
import sys
import http.server
import socketserver

DEFAULT_PORT = 8080
REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=REPO_ROOT, **kwargs)

    def end_headers(self):
        # Enable CORS and caching headers for local preview
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
        super().end_headers()

def main():
    port = DEFAULT_PORT
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        port = int(sys.argv[1])

    os.chdir(REPO_ROOT)
    
    socketserver.TCPServer.allow_reuse_address = True
    
    try:
        with socketserver.TCPServer(("", port), CustomHTTPRequestHandler) as httpd:
            print("=" * 72)
            print("  SPUTNIK TECH GROUP & SPUTNIK DEVS — SHOWCASE 2026 VIEWER")
            print("=" * 72)
            print(f"  Local Server:  http://localhost:{port}/")
            print(f"  Interactive Studio: http://localhost:{port}/viewer/")
            print("\n  Direct Print Layouts:")
            print(f"    • Pull-Up Banner (1m x 2m):   http://localhost:{port}/designs/banner-1x2m/banner-print.html")
            print(f"    • Table Cloth (3m x 3m):      http://localhost:{port}/designs/table-cloth-3x3m/tablecloth-print.html")
            print(f"    • Staff T-Shirts (DTF):       http://localhost:{port}/designs/shirts/shirt-print.html")
            print("=" * 72)
            print("  Press Ctrl+C to stop the server.\n")
            httpd.serve_forever()
    except OSError as e:
        if "Address already in use" in str(e):
            print(f"Port {port} is currently in use. Trying port {port + 1}...")
            if len(sys.argv) > 1:
                sys.argv[1] = str(port + 1)
            else:
                sys.argv.append(str(port + 1))
            main()
        else:
            raise e
    except KeyboardInterrupt:
        print("\n\nServer stopped. Best of luck to Prince & Kenneth at Rosebank Showcase!")

if __name__ == "__main__":
    main()
