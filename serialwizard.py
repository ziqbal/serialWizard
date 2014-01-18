# Demonstration of reading data from the serial port
# And dynamic output via HTTP
# Zafar Iqbal, http://zaf.io/

# The serial port to read data from
SERIALPORT = '/dev/tty.usbmodem641' # Mac
#SERIALPORT = '/dev/ttyACM0' # Linux
#SERIALPORT = 'COM6' # Microsoft Windows

##########################################################

# HTTP port for server example http://127.0.0.1:8888
NETWORKPORT = 8888
#NETWORKPORT = 8889

##########################################################

# Imports
import serial
from threading import Thread
import SimpleHTTPServer
import SocketServer
from SimpleHTTPServer import SimpleHTTPRequestHandler
from StringIO import StringIO
import json

# Serial port reading thread
dataRingMax=50;
dataRing = [0]*dataRingMax
dataRingPos = 0
def serialHandle():
    global dataRing,dataRingPos,flagContinue
    s = serial.Serial(port=SERIALPORT)
    while True:
        dataRing[dataRingPos]=s.readline().strip()
        dataRingPos=(dataRingPos+1)%dataRingMax
        print("[SERIAL] "+str(dataRingPos))

thread=Thread(target=serialHandle)
thread.daemon=True
thread.start()

# HTTP Server handler
class MyRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    global dataRing
    def do_GET(self):
        if self.path.startswith('/json'):
            res=StringIO()
            res.write(json.dumps(dataRing))
            self.send_response(200)
            self.send_header("Content-type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(res.tell()))
            self.end_headers()
            res.seek(0)
            self.copyfile(res, self.wfile)
            res.close()
            return
        return SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)
    
httpd = SocketServer.TCPServer(("", NETWORKPORT), MyRequestHandler)
httpd.serve_forever()



