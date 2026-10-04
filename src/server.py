import os
from http.server import BaseHTTPRequestHandler, HTTPServer
import json


tasks = [
    {"id": 1, "title": "Learn Git", "completed": False},
    {"id": 2, "title": "Complete M1", "completed": True},
    {"id": 3, "title": "Study Docker", "completed": False}
]


class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Task Management API")

        elif self.path == "/healthz":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        elif self.path == "/tasks":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(tasks).encode())

        else:
            self.send_response(404)
            self.end_headers()


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "8080"))

    server = HTTPServer(("0.0.0.0", port), Handler)

    print(f"Server running on port {port}")

    server.serve_forever()