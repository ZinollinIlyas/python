from socketserver import StreamRequestHandler, TCPServer, ThreadingMixIn
from Request import Request
from Response import Response
from StaticResponder import StaticResponder
from jinja2 import Environment, FileSystemLoader
import os
from pages_controller import ClickController
from Router import Router

router = Router()

THIS_DIR = os.path.dirname(os.path.abspath(__file__))

env = Environment(
    loader=FileSystemLoader(THIS_DIR)
)

router.get("/", ClickController, "get_click")
router.get("/click?", ClickController, "count_click")


class HelloTCPServer(StreamRequestHandler):
    urls = {
        '/': 'index',
        '/one': 'one',
        '/two': 'two',
        '/three': 'three'
    }

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
