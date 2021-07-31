import socket
from random import randint

HOST = '127.0.0.1'
PORT = 1234

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    quote = [
        'Умение слушать - большой плюс, а умение делать вид, что слушаешь, и в нужный момент вставлять слово - талант.\n',
        'Мы работаем, чтобы иметь свободное время, и воюем, чтобы жить мирно.\n',
        'Два года человек учится говорить, а потом всю оставшуюся жизнь — молчать.\n',
        'Не было еще ни одного великого ума без примеси безумства.', 'Корни образования горькие, но плоды сладкие.\n']
    s.bind((HOST, PORT))
    s.listen()
    print(f'Waiting for connection on {PORT} port')
    conn, addr = s.accept()
    with conn:
        print(f'Connected by {addr}')
        rand = randint(0, 4)
        conn.sendall(bytes(f'{quote[rand]}\n'.encode()))
