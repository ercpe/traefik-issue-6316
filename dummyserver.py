import http.server
import socketserver
from http import HTTPStatus

class Handler(http.server.BaseHTTPRequestHandler):
    
    def do_GET(self):
        self.send_response(HTTPStatus.OK)
        self.send_header("Content-type", "text/plain")
        self.send_header('X-Response-Header-With-Quotes', 'this is a "test"')
        self.end_headers()


with socketserver.TCPServer(("", 8000), Handler) as httpd:
    httpd.serve_forever()
