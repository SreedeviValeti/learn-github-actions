from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from src.claims import get_claim_status_label

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/health':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"status": "ok", "service": "claims-service"}).encode())
        else:
            self.send_response(404)
            self.end_headers()

    def log_message(self, format, *args):
        pass

if __name__ == '__main__':
    print('Starting claims-service on port 8080')
    HTTPServer(('0.0.0.0', 8080), Handler).serve_forever()
