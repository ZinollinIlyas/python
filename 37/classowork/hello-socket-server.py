from socketserver import StreamRequestHandler, TCPServer, ThreadingMixIn
from Request import Request
from Response import Response
from StaticResponder import StaticResponder


class MyTCPHandler(StreamRequestHandler):
    def handle(self):
        request = Request(self.rfile)
        response = Response(self.wfile)

        static_responder = StaticResponder(request, response, "static")

        if static_responder.file:
            static_responder.prepare_response()
        else:
            response.add_header("Content-Type", "text/html")
            response.add_header("Connection", "close")
            response.set_body('''
                   <link rel="stylesheets" href="/css/main.css">
                   <h1>Hello!</h1>
                   ''')

        response.send()


class ThreadedTCPServer(ThreadingMixIn, TCPServer):
    pass


HOST, PORT = "localhost", 8008
TCPServer.allow_reuse_address = True

with ThreadedTCPServer((HOST, PORT), MyTCPHandler) as server:
    server.serve_forever()
