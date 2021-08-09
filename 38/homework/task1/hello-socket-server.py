from socketserver import StreamRequestHandler, TCPServer, ThreadingMixIn
from Request import Request
from Response import Response
from StaticResponder import StaticResponder
from pages_controller import PagesController
from Router import Router

router = Router()


router.get("/", PagesController, "home")
router.get("/one", PagesController, 'one')
router.get("/two", PagesController, "two")
router.get("/three", PagesController, "three")


class HelloTCPServer(StreamRequestHandler):

    def handle(self):
        request = Request(self.rfile)
        response = Response(self.wfile)

        static_responder = StaticResponder(request, response, "static")

        if static_responder.file:
            static_responder.prepare_response()
        else:
            router.run(request, response)

        response.send()


class ThreadedTCPServer(ThreadingMixIn, TCPServer):
    pass


HOST, PORT = "127.0.0.1", 8000
TCPServer.allow_reuse_address = True

with ThreadedTCPServer((HOST, PORT), HelloTCPServer) as s:
    s.serve_forever()
