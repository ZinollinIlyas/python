import socket

HOST = '127.0.0.1'
PORT = 8800

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f'Waiting for connection on {PORT} port')
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        conn.sendall(b'Please enter first number:\n')
        number1 = conn.recv(1024)
        conn.sendall(b'Please enter second number:\n')
        number2 = conn.recv(1024)
        number1 = int(number1)
        number2 = int(number2)
        conn.sendall(b'Results:\n')
        conn.sendall(bytes(f'{number1 + number2}\n'.encode()))
        conn.sendall(bytes(f'{number1 - number2}\n'.encode()))
        conn.sendall(bytes(f'{number1 * number2}\n'.encode()))
        conn.sendall(bytes(f'{number1 / number2}\n'.encode()))

