import http.server 
import socketserver
import socket
import os
import webbrowser
import pyqrcode
from PIL import Image
import subprocess

PORT = 3000

DIRECTORY =  "E:\\final year\\"

if not os.path.exists(DIRECTORY):
    os.makedirs(DIRECTORY)

class FileHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,directory=DIRECTORY,**kwargs)

def generate_qrcode(url,output_file="qrcode.png"):
    qr = pyqrcode.create(url)
    qr.png(output_file, scale=8)
    print("QRCode generated")
    os.startfile(output_file)

def start_http_server():
    with socketserver.TCPServer(("",PORT),FileHandler) as httpd:
        print("Server started on port",PORT)

        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)
        print("Server IP:",ip)

        url = f"http://{ip}:{PORT}/"
        print(f"access files at :{url}")

        generate_qrcode(url)

        webbrowser.open(url)

        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped")
            httpd.server_close()

if __name__ == "__main__":
    print("Starting file transfer server.....")
    print(f"place files in the {DIRECTORY} ")
    start_http_server()