'''
Implement an HTTP web server in Python
'''

import os,sys
import SimpleHTTPServer
from BaseHTTPServer import HTTPServer
webdir ='.' #where html files and cgi-bin script direcroty live
port =80 #default httlp://localhost/, else use http://localhost:xxxx/

os.chdir(webdir)
srvraddr=("",port) #run in HMTL root dir
srvrobj = HTTPServer(srvraddr,SimpleHTTPServer.SimpleHTTPRequestHandler)
srvrobj.serve_forever()
