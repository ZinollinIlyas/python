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

posts = [
    {
        "author": "John",
        "title": "Hello!",
        "text": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Doloremque "
                "dolores dolorum eum quae reiciendis voluptate. Ducimus maxime odio sed "
                "vitae voluptate? Commodi doloremque eaque laborum minus numquam quia, quibusdam sequi."
    },
    {
        "author": "Jane",
        "title": "This is my first post",
        "text": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Doloremque "
                "dolores dolorum eum quae reiciendis voluptate. Ducimus maxime odio sed "
                "vitae voluptate? Commodi doloremque eaque laborum minus numquam quia, quibusdam sequi."
    },
    {
        "author": "Bob",
        "title": "Hi, my name is Bob",
        "text": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Doloremque "
                "dolores dolorum eum quae reiciendis voluptate. Ducimus maxime odio sed "
                "vitae voluptate? Commodi doloremque eaque laborum minus numquam quia, quibusdam sequi."
    }
]


class HelloTCPServer(StreamRequestHandler):
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
                "last_posts": posts
            })

            if request.uri == "/posts":
                template = env.get_template("templates/posts.html")
                body = template.render({
                    "posts": posts
                })

            response.set_body(body)

        response.send()


class ThreadedTCPServer(ThreadingMixIn, TCPServer):
    pass


HOST, PORT = "127.0.0.1", 8000
TCPServer.allow_reuse_address = True

with ThreadedTCPServer((HOST, PORT), HelloTCPServer) as s:
    s.serve_forever()
