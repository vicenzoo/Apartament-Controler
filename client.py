import socket

sair = "!OUT" #Texto para desconectar Apartamento


def main():
    SERVER = ('127.0.0.1', 8000)#Configura Cliente
    TCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    TCP.connect(SERVER)

    alive = True
    while alive:
        try:
            msag = input()
            TCP.send(msag.encode()) #Espaço para comando de saida
            if(msag == sair):
                alive = False      
        except:
            alive = False
            TCP.close()
            pass


main()