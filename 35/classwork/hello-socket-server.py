from socketserver import StreamRequestHandler, TCPServer, ThreadingMixIn
from request import Request


class MyTCPHandler(StreamRequestHandler):
    def handle(self):
        request = Request(self.rfile)

        print('Method:', request.method)
        print('Uri:', request.uri)
        print('Protocol:', request.protocol)

        response_body = '<h1>Hello, world!</h1>'
        response_body_length = len(response_body.encode())

        response = [
            'HTTP/1.1 200 OK',
            'Content-Type: text/html',
            'Content-Length: ' + str(response_body_length),
            'Connection: close',
            '',
            response_body
        ]

        self.wfile.write('\r\n'.join(response).encode())


class ThreadedTCPServer(ThreadingMixIn, TCPServer):
    pass


HOST, PORT = "localhost", 8000
TCPServer.allow_reuse_address = True

with ThreadedTCPServer((HOST, PORT), MyTCPHandler) as server:
    server.serve_forever()
