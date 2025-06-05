# EX01 Developing a Simple Webserver
# Date:17.02.2025

## AIM:
To develop a simple webserver to serve html pages and display the list of protocols in TCP/IP Protocol Suite.

## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Import the necessary modules.

### Step 5:
Define a custom request handler.

### Step 6:
Start an HTTP server on a specific port.

### Step 7:
Run the Python script to serve web pages.

### Step 8:
Serve the HTML pages.

### Step 9:
Start the server script and check for errors.

### Step 10:
Open a browser and navigate to http://127.0.0.1:8000 (or the assigned port).

## PROGRAM:
```
from http.server import HTTPServer, BaseHTTPRequestHandler
content = """

<html>
    <body>
        <h1 style="color:red;text-align: center">TCP/IP PROTOCOL SUITE</h1>
        <ul align="center">
            <b>Application Layer:</b> Uses HTTP/HTTPS (port 80/443) <br>
            <b>Transport Layer:</b>	Uses TCP (ensures reliable delivery) <br>
            <b>Internet Layer:</b> Uses IP for addressing and routing <br>
            <b>Network Access Layer:</b> Uses Ethernet, Wi-Fi <br>
        </ul>
    </body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()
```
## OUTPUT:
![Screenshot (6)](https://github.com/user-attachments/assets/cb311d5d-bf57-4e41-b4c7-d8d3bcb054d0)

![alt text](<Screenshot (5).png>)

## RESULT:
The program for implementing simple webserver is executed successfully.
