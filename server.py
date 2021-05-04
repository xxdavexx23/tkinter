import random, socket, time

dev = None
dist = 0
degr = 0


def randr(mn, mx, rnd):
    return round(random.random() * (mx - mn) + mn, rnd)


def send_msg(sock, *msgs):
    for msg in msgs:
        msg = bytes(str(msg), 'utf-8')
        sock.sendall(msg)


ip = '10.0.0.17'
port = 45002

s = socket.socket()
s.bind((ip, port))
s.listen(5)


def handle(sock):
    while True:
        msg = str(sock.recv(3), 'utf-8')
        print(msg)
        if msg == 'pu\n' or msg == 'sc\n' or msg == 'sp\n' or msg == 'of\n':
            with open('../ledstrip/python/mode_' + msg[0:2] + '.txt', 'w') as f:
                pass
        if msg == 'qqq' or len(msg) == 0:
            return


while True:
    print('Listening on {} port {}'.format(ip, port))
    sock, addr = s.accept()
    print('Accepted connection from {}'.format(addr))
    handle(sock)
    sock.close()