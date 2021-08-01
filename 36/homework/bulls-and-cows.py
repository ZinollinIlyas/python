from socketserver import StreamRequestHandler, TCPServer, ThreadingMixIn
from Request import Request
from random import randint
from urllib.parse import parse_qs


def generate_numbers(count=5):
    numbers = []
    while len(numbers) < count:
        rand_number = randint(1, 10)
        if rand_number not in numbers:
            numbers.append(rand_number)
    return numbers


class HelloTCPServer(StreamRequestHandler):
    secret_numbers = generate_numbers()
    response_body = f'''
            <p>Guess 4 numbers. Enter them separated with spaces:</p>
                <form method="POST" action="/">
                    <input type="text" name="numbers" autocomplete="off"/>
                    <input type="submit" value="Send"/>
                </form>
            '''.encode()

    def handle(self):
        request = Request(self.rfile)
        user_input_byte = parse_qs(request.body)
        print(user_input_byte)
        user_input = {key.decode(): val[0].decode() for key, val in user_input_byte.items()}
        print(user_input)
        # numbers = []
        # if user_input != {}:
        #     numbers = user_input['numbers'].split(' ')
        #
        # for number in numbers:
        #     print(number)
        # numbers = user_input['numbers'].split(' ')
        # print(numbers)

        response_body_length = str(len(self.response_body))

        response = [
            "HTTP/1.1 200 OK",
            "Content-Type: text/html; charset=utf-8",
            f"Content-Length: {response_body_length}",
            "Connection: close",
            "",
            self.response_body.decode()
        ]

        self.wfile.write("\r\n".join(response).encode())

    # def guess_numbers(self, secret, actual):
    #     if len(secret) > len(actual) or not isinstance([number for number in actual], int)


class ThreadedTCPServer(ThreadingMixIn, TCPServer):
    pass


HOST, PORT = "127.0.0.1", 8000
TCPServer.allow_reuse_address = True

with ThreadedTCPServer((HOST, PORT), HelloTCPServer) as s:
    s.serve_forever()
