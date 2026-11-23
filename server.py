#!/usr/bin/env python3
"""Minimal Render Web Service server for the static portfolio."""

import os
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

ROOT = os.path.dirname(os.path.abspath(__file__))


class PortfolioHandler(SimpleHTTPRequestHandler):
    extensions_map = {
        **SimpleHTTPRequestHandler.extensions_map,
        ".webmanifest": "application/manifest+json",
        ".mp4": "video/mp4",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".gif": "image/gif",
        ".svg": "image/svg+xml",
        ".ico": "image/x-icon",
        ".css": "text/css",
        ".js": "text/javascript",
        ".json": "application/json",
        ".txt": "text/plain",
        ".xml": "application/xml",
    }

    def send_error(self, code, message=None, explain=None):
        if code == 404:
            error_page = os.path.join(ROOT, "404.html")
            if os.path.isfile(error_page):
                with open(error_page, "rb") as fh:
                    body = fh.read()
                self.send_response(404)
                self.send_header("Content-Type", "text/html; charset=utf-8")
                self.send_header("Content-Length", str(len(body)))
                self.end_headers()
                self.wfile.write(body)
                return
        super().send_error(code, message, explain)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "10000"))
    handler = partial(PortfolioHandler, directory=ROOT)
    with ThreadingHTTPServer(("0.0.0.0", port), handler) as server:
        print("Serving {0} on 0.0.0.0:{1}".format(ROOT, port), flush=True)
        server.serve_forever()
