import socket
import random
import time

IP_Servidor = '127.0.0.1'
# Endereco IP do Servidor
             
PORTA = 8000                  
# Porta em que o servidor estara ouvindo
sair = '!sair'

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
DESTINO = (IP_Servidor, PORTA)
Entrou = "Apartamento entrou" 
udp.sendto (bytes(Entrou,"utf8"), DESTINO) 

def handle_aps():
    barulho = ''
    time.sleep(5)
    nivel = random.randint(50,140)
    print(nivel)

    if (nivel >= 70 and nivel <= 90):
        barulho = ("Apartamento: emitiu som de mais de 70 decibeis") 
        udp.sendto(bytes(str(nivel), 'utf8'), DESTINO)

    if (nivel >= 90 and nivel <= 110):

        barulho = ("Apartamento: emitiu som de mais de 80 decibeis") 
        udp.sendto(bytes(str(nivel), 'utf8'), DESTINO)

    if (nivel >= 110 and nivel <= 139):
        barulho = ("Apartamento: emitiu som de de mais de 100 decibeis")
        udp.sendto(bytes(str(nivel), 'utf8'), DESTINO)

    if (nivel >= 140):
        barulho = ("Apartamento: emitiu som de 140 ou mais decibeis") 
        udp.sendto(bytes(str(nivel), 'utf8'), DESTINO)

    print(barulho)


handle_aps()
alive = True

while alive:
    
    try:
        Mensagem = input()           
        udp.sendto (bytes(Mensagem,"utf8"), DESTINO)
    except:
        alive = False
        udp.close()
        pass
