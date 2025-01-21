import http.server 
import socketserver
import socket
import os
import webbrowser
import pyqrcode
from pyqrcode import QRCode
import png

PORT = 3000

desktop ='E:/'
os.chdir(desktop)

# creating a http request
Handler = http.server.SimpleHTTPRequestHandler
hostname =  socket.gethostname()

# finding the IP address of the PC
s =socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
IP = "http://" + s.getsockname()[0] + ":" + str(PORT)
link =IP

# converts the IP address into a Qrcode
url = pyqrcode.create(link)
url.svg("myqr.svg", scale=8)

# opens the Qrcode image in the web browser
webbrowser.open("myqr.svg")


# continuous stream of data between client and server
def start_http_server():
    with socketserver.TCPServer(("",PORT),Handler) as httpd :
        print("Starting server on port", PORT)
        print("Connecting to ip", link)
        httpd.serve_forever()

if __name__ == "__main__":
    
    start_http_server()