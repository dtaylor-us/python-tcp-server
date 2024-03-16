import socket

PORT = 3000

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


def main():
    sock = createSocketConnection()
    sock.sendall(b'Greetings, server')
    reply = recvall(sock, 16)
    print('Server: ', repr(reply))
    sock.close()


def createSocketConnection():
    host = '127.0.0.1'
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, PORT))
    print('Client has been assigned the socket: ', sock.getsockname())
    return sock


if __name__ == "__main__":
    main()
