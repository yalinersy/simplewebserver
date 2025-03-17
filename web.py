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