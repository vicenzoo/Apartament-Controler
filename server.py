import socket
import threading

def handle_client(con,adress):
    print("Apartamento entrou")



def main():
    print("Central Online!")
    SERVER = ('127.0.0.1', 8000)
    TCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    TCP.bind(SERVER)
    TCP.listen(1)
    alive = True
    while alive:
        con,adress = TCP.accept()
        thread = threading.Thread(target=handle_client,args=(con,adress))
        thread.start()

        try:
            print(f"apartamento {threading.activeCount() - 1} Conectou-se")
        except:
            con.close()
            alive = False
            pass

main()
