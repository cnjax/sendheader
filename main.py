#!/usr/bin/env python3

from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer
import logging
import sys

try:
    PORT = int(sys.argv[1])
except:
    PORT = 80

class GetHandler(SimpleHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200, self.headers)

Handler = GetHandler
httpd = TCPServer(('', PORT), Handler)

httpd.serve_forever()