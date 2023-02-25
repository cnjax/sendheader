#!/usr/bin/env python3

from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer
import logging
import sys

try:
    PORT = int(sys.argv[1])
except:
    PORT = 18081

class GetHandler(SimpleHTTPRequestHandler):

    def do_GET(self):
        myheaders=self.headers
        self.send_response(200)
        self.send_header('Content-Type', 'text/plain')
        self.end_headers()
        self.wfile.write(str(myheaders).encode("UTF-8"))
        print(myheaders)

Handler = GetHandler
httpd = TCPServer(('0.0.0.0', PORT), Handler)

httpd.serve_forever()