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
            <p>Guess {len(secret_numbers)} numbers. Enter them separated with spaces:</p>
                <form method="POST" action="/">
                    <input type="text" name="numbers" autocomplete="off"/>
                    <input type="submit" value="Send"/>
                </form>
            '''.encode()

    def handle(self):
        request = Request(self.rfile)
        user_input_byte = parse_qs(request.body)
        user_input = {key.decode(): val[0].decode() for key, val in user_input_byte.items()}
        numbers = []
        if user_input != {}:
            numbers = user_input['numbers'].split(' ')

        int_list = map(int, numbers)
        int_numbers = list(int_list)

        if request.method == "POST":
            self.response_body += self.guess_numbers(self.secret_numbers, int_numbers)

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

    def guess_numbers(self, secret, actual):
        bulls = 0
        cows = 0
        if len(secret) > len(actual):
            return f"<p>Error, wrong input</p>".encode()
        else:
            for i in range(len(actual)):
                if actual[i] == secret[i]:
                    bulls += 1
                elif actual[i] in secret and actual[i] != secret[i]:
                    cows += 1
                elif actual[i] > 10:
                    return f"<p>Numbers must be between 1 and 10</p>".encode()
            return f"<p>Bulls: {bulls}, cows: {cows}".encode()


class ThreadedTCPServer(ThreadingMixIn, TCPServer):
    pass


HOST, PORT = "127.0.0.1", 8000
TCPServer.allow_reuse_address = True

with ThreadedTCPServer((HOST, PORT), HelloTCPServer) as s:
    s.serve_forever()
