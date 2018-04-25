from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
from SocketServer   import ForkingMixIn
from . import generate_data
import getopt
import json
import logging
import mimetypes
import os
import subprocess
import sys

HOST_NAME = 'localhost'
PORT = 8000

def getList(s_u, u_s, song):
	listt = []
	for u in s_u[song]:
		listt.extend(u_s[u])
	songs = {}
	for s in listt:
		if s not in songs:
			songs[s] = 1
		else:
			songs[s] = songs++
	for key, value in sorted(songs.iteritems(), key=lambda(k,v):(v,k)):
		listt.append(key)
	return listt[-10:]
		

class myHandler(BaseHTTPRequestHandler):

        #Handler for the GET requests
    def do_GET(self):
        if self.path=="/":
            self.path="./index.html"
	self.send_response(200)
	self.send_header("Content-type", "text/html")
	self.end_headers()
	print(self.wfile)
	u_s, s_u = gen_data('./data/test_sample.txt', 2000)
	listt = getList(s_u, u_s, song)
	self.wfile.write("<html><head><title>Title goes here.</title></head>")
	self.wfile.write("<body><p>This is a test.</p>")
		        # If someone went to "http://something.somewhere.net/foo/bar/",
			        # then s.path equals "/foo/bar/".
	for i in listt:
		self.wfile.write("<p>Song: %s</p>" % i)
	self.wfile.write("</body></html>")
	self.wfile.close()

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

        #Wait forevera for incoming htto requests
        server.serve_forever()

except KeyboardInterrupt:
        print '^C received, shutting down the web server'
        server.socket.close()
