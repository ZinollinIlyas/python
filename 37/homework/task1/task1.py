import socket


HOST = '127.0.0.1'
PORT = 8006
user_input = []
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.listen()
conn, addr = s.accept()
print(f'Waiting for connection on {PORT} port')
print(f'Connected by {addr}')
while True:
    data = conn.recv(1024)
    if data != b'--END--\r\n':
        user_input.append(data)
    else:
        line_counter = len(user_input)
        final_string = b''
        for i in range(len(user_input)):
            final_string += user_input[i]
        final_string.decode()
        length_counter = len(final_string)
        conn.sendall(f"Hello, Client!\n".encode())
        conn.sendall(f"Total lines: {line_counter}\n".encode())
        conn.sendall((f"Total length: {length_counter}\n".encode()))
        conn.close()
        s.close()
        break




