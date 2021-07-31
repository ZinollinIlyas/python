from socketserver import StreamRequestHandler, TCPServer, ThreadingMixIn


class Request:
    def __init__(self, file):
        self.file = file

        self.method = ''
        self.uri = ''
        self.protocol = ''
        self.headers = {}

        self.parse_request_line()
        self.parse_body()

    def parse_request_line(self):
        request_line = self.read_line()

        self.method, self.uri, self.protocol = request_line.split(' ')

        if self.protocol != 'HTTP/1.1':
            raise ValueError('Wrong protocol')

    def parse_headers(self):
        while True:
            header = self.read_line()

            if header == '':
                break

            header_name, header_value = header.split(': ')
            self.headers[header_name] = header_value
            print(self.headers)

    def read_line(self):
        return self.file.readline().decode().strip()

    def parse_body(self):
        if 'Content-Length' in self.headers:
            content_length = int(self.headers['Content-Length'])
            self.body = self.file.read(content_length)


class MyTCPHandler(StreamRequestHandler):
    urls = {
        "/": "<h1>Follow the white rabbit</h1>",
        "/white_rabbit": "<h1>You are living in the matrix</h1>"
    }

    def handle(self):
        request = Request(self.rfile)

        print('Method:', request.method)
        print('Uri:', request.uri)
        print('Protocol:', request.protocol)

        response_body = ''
        status = 'HTTP/1.1 200 OK'

        if request.method != 'GET' or request.uri not in self.urls:
            response_body = f"<h1 style='color: red'>501 Not Implemented</h1>"
            status = 'HTTP/1.1 501 Not Implemented'
        else:
            response_body = self.urls.get(request.uri)

        response_body_length = len(response_body.encode())

        response = [
            status,
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
