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
from _music_database import *
from recommend import *

HOST_NAME = 'localhost'
PORT = 8000

test_dictt = {"one":"justin", "two" : "mary", "three":"john"}
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
            d = random_user()
            if d["status"]!="success":
                return
            name = d["user_name"]
            rec = recommend_user(name,mdb)
            rec["user_name"] = name
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
	    	#dictt= sunruochen.get("This is a song")
            self.wfile.write(json.dumps(rec))
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
        mdb = _music_database()
        mdb.load_database("./data/test_sample.txt",2000)


        print 'Started httpserver on port ' , HOST_NAME, PORT

        #Wait forevera for incoming htto requests
        server.serve_forever()

except KeyboardInterrupt:
        print '^C received, shutting down the web server'
        server.socket.close()
