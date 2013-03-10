import sys
import BaseHTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler
from random import randint

port_mix = randint(1000,9999)

HandlerClass = SimpleHTTPRequestHandler
ServerClass  = BaseHTTPServer.HTTPServer
Protocol     = "HTTP/1.0"

if sys.argv[1:]:
    port = int(sys.argv[1])
else:
    port = port_mix
server_address = ('127.0.0.1', port)

HandlerClass.protocol_version = Protocol
httpd = ServerClass(server_address, HandlerClass)

sa = httpd.socket.getsockname()
print "Ready to role, Lets Go! servin' up your server at ", sa[0], "port", sa[1], "..." 
httpd.serve_forever()

