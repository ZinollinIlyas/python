from socketserver import StreamRequestHandler, TCPServer, ThreadingMixIn
from Request import Request
from Response import Response
from StaticResponder import StaticResponder
from jinja2 import Environment, FileSystemLoader
import os

THIS_DIR = os.path.dirname(os.path.abspath(__file__))


env = Environment(
    loader=FileSystemLoader(THIS_DIR)
)


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
            body = ""
            response.add_header("Content-Type", "text/html")
            response.add_header("Connection", "close")
            template = env.get_template("templates/index.html")
            body = template.render({
                "my_var": "My Variable Value",
            })

            if request.uri not in self.urls:
                template = env.get_template("templates/error_page.html")
                response.set_status(404)
                body = template.render({"status": response._get_status_line()})
            else:
                template = env.get_template(f"templates/{self.urls[request.uri]}.html")
                body = template.render()

            response.set_body(body)

        response.send()


class ThreadedTCPServer(ThreadingMixIn, TCPServer):
    pass


HOST, PORT = "127.0.0.1", 8000
TCPServer.allow_reuse_address = True

with ThreadedTCPServer((HOST, PORT), HelloTCPServer) as s:
    s.serve_forever()
