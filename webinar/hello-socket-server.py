from socketserver import StreamRequestHandler, TCPServer, ThreadingMixIn
from Request import Request


class HelloTCPServer(StreamRequestHandler):
    def _get_template(self, file, context=None):
        if context is None:
            context = {}

        with open(file, "r") as f:
            template = f.read()
            for key, value in context.items():
                template = template.replace("{{%s}}" % key, value)
            return template.encode()

    def handle(self):
        request = Request(self.rfile)

        router = {
            "/": self._get_template(
                "index.html",
                {"var": "asdasda", "another_var": "qweqwe"}
            ),
            "/products/mobile": self._get_template("product.html", {"name": "Xiaomi mi 9SE"}),
            "/products/notebook": self._get_template("product.html", {"name": "Lenovo Legion"}),
            "/products/accessory": self._get_template("product.html", {"name": "Computer Mouse"})
        }

        response_body = router.get(request.uri, self._get_template("404.html"))

        response_body_length = str(len(response_body))

        response = [
            "HTTP/1.1 200 OK",
            "Content-Type: text/html; charset=utf-8",
            f"Content-Length: {response_body_length}",
            "Connection: close",
            "",
            response_body.decode()
        ]

        self.wfile.write("\r\n".join(response).encode())


class ThreadedTCPServer(ThreadingMixIn, TCPServer):
    pass


HOST, PORT = "127.0.0.1", 8000
TCPServer.allow_reuse_address = True

with ThreadedTCPServer((HOST, PORT), HelloTCPServer) as s:
    s.serve_forever()
