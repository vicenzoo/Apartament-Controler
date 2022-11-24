import socket
import threading
import random

def handle_client(con,adress):
    print(f"Apartamento entrou")
    num = random.randint(1,threading.activeCount() - 1)
    print(num)
    con.close()



def main():
    print("Central Online!")
    SERVER = ('127.0.0.1', 8000)
    TCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    TCP.bind(SERVER)
    TCP.listen(1)
    while True:
        con,adress = TCP.accept()
        thread = threading.Thread(target=handle_client,args=(con,adress))
        thread.start()
        print(f"apartamento {threading.activeCount() - 1} Conectou-se")

main()
