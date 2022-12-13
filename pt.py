
from http.server import HTTPServer, BaseHTTPRequestHandler

content = """
<html>
<head>
<title>MY WEBSERVER</title>
</head>
<body>
<h1>WELCOME TO PROGRAMMING</h1>
</body>
</html>
"""
class Hellohander(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type','text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())

server_address = ('',8080)
httpd = HTTPServer(server_address,Hellohander)
httpd.serve_forever()

