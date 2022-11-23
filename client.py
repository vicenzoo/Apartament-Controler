import socket


def main():
    SERVER = ('127.0.0.1', 8000)
    TCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    TCP.connect(SERVER)

    alive = True
    while alive:
        try:
            TCP.send(input().encode())
        except:
            alive = False
            TCP.close()
            pass


main()