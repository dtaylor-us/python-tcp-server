import argparse, socket

HOST = '127.0.0.1'

PORT = 3000


def create_socket():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((HOST, PORT))
    sock.listen(1)
    print('Listening at', sock.getsockname())
    return sock


def recvall(sock, length):
    data = b''
    while len(data) < length:
        more = sock.recv(length - len(data))
        if not more:
            raise EOFError('was expecting %d bytes but only received'
                           ' %d bytes before the socket closed'
                           % (length, len(data)))
        data += more
    return data


def recieve_message(sc):
    message = recvall(sc, 16)
    print('  message from client:', repr(message))


def close_connection(sc):
    sc.sendall(b'Goodbye, client!')
    sc.close()
    print('  Closing socket')


def main():
    sock = create_socket()
    while True:
        print('Waiting for a new connection')

        sc, sock_name = sock.accept()
        print('Connection from', sock_name)
        print('  Socket name:', sc.getsockname())
        print('  Socket peer:', sc.getpeername())

        recieve_message(sc)
        close_connection(sc)


if __name__ == "__main__":
    main()
