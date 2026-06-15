import http.server
import socketserver

PORT = 8080
DIRECTORY = "public"

import os

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def do_GET(self):
        # Fayl mövcud deyilsə və bu bir API sorğusu deyilsə, index.html-i qaytarırıq (SPA routing)
        path = self.translate_path(self.path)
        if not os.path.exists(path) and '.' not in self.path.split('/')[-1]:
            self.path = '/index.html'
        return super().do_GET()

    def end_headers(self):
        # WebContainer və SharedArrayBuffer üçün vacib olan headerlər
        self.send_header('Cross-Origin-Opener-Policy', 'same-origin')
        self.send_header('Cross-Origin-Embedder-Policy', 'require-corp')
        self.send_header('Cross-Origin-Resource-Policy', 'cross-origin')
        super().end_headers()

with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
    print(f"Serving at port {PORT} with COOP/COEP headers and SPA routing")
    httpd.serve_forever()
