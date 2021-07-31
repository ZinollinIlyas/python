import socket
import math

HOST = '127.0.0.1'
PORT = 2345

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f'Waiting for connection on {PORT} port')
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        conn.sendall(b'Please enter your number:\n')
        number = conn.recv(1024)
        number = int(number)
        if number < 5000:
            number = math.factorial(number)
            conn.sendall(bytes(f'{number}\n'.encode()))
        else:
            conn.sendall(b'This number is too big\n')

