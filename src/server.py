'''from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
from SocketServer   import ForkingMixIn

import getopt
import json
import logging
import mimetypes
import os
import subprocess
import sys

HOST_NAME = 'localhost'
PORT = 8000

class myHandler(BaseHTTPRequestHandler):

	#Handler for the GET requests
    def do_GET(self):
        if self.path=="/":
            self.path="./index.html"
        try:
            f = open(self.path)
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()
            # Send the html message
            self.wfile.write(f.read())
            f.close()
            return
        except IOError:
			self.send_error(404,'File Not Found: %s' % self.path)

try:
	#Create a web server and define the handler to manage the
	#incoming request
	server = HTTPServer((HOST_NAME, PORT), myHandler)
	print 'Started httpserver on port ' , HOST_NAME, PORT

	#Wait forever for incoming htto requests
	server.serve_forever()

except KeyboardInterrupt:
	print '^C received, shutting down the web server'
	server.socket.close()'''
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
from SocketServer   import ForkingMixIn
#from . import generate_data
#from . import sunruochen
import getopt
import json
import logging
import mimetypes
import os
import subprocess
import sys

HOST_NAME = 'localhost'
PORT = 8000

test_dictt = {"number one":"justin", "number two" : "mary", "number three":"john"}
# dictt for testing

class myHandler(BaseHTTPRequestHandler):

        #Handler for the GET requests
    def do_GET(self):
        if self.path=="/":
			print "hello"
			#self.send_response(200)
			#self.send_header('Content-type','text/html')
			self.path="./index.html"
			f = open(self.path)
			self.send_response(200)
			self.send_header('Content-type','text/html')
			self.end_headers()
            # Send the html message
			self.wfile.write(f.read())
			f.close()
        elif self.path=="/search":
            print "world"
            print test_dictt
            self.send_response(200)
            self.send_header("Content-type", "application/json")
	    	#dictt= sunruochen.get("This is a song")
            self.wfile.write(json.dumps(test_dictt))
            self.wfile.close()
        return
        '''try:

            return
        except IOError:
            self.send_error(404,'File Not Found: %s' % self.path)'''

try:
        #Create a web server and define the handler to manage the
        #incoming request
        server = HTTPServer((HOST_NAME, PORT), myHandler)
        print 'Started httpserver on port ' , HOST_NAME, PORT

        #Wait forevera for incoming htto requests
        server.serve_forever()

except KeyboardInterrupt:
        print '^C received, shutting down the web server'
        server.socket.close()
