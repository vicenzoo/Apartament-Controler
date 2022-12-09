
import socket
import threading
import time

IP = '127.0.0.1'                              
PORTA = 8000
exit = "!sair"

def listen_ap(con,adress):
    print(f"Apartamento entrou {adress}")
    ap_listen = udp.recvfrom(1024)
    strtoint = int(ap_listen[0])
    alive = True

    if (strtoint >= 70 and strtoint <= 79):
        print(f"Apartamento {ap_num}: Está causando um Barulho Leve")

    if (strtoint >= 80 and strtoint <= 89):
        print(f"Apartamento {ap_num}: Está causando um Barulho Moderado")

    if (strtoint >= 90 and strtoint <= 139):
        print(f"Apartamento {ap_num}: Está causando um Barulho Alto!")
    
    if (strtoint >= 140):
        print(f"Apartamento {ap_num}: Está causando um Barulho Altissimo! [ENTRAR EM CONTATO]")

    while alive:
        if ap_listen == exit:
            alive = False


    con.close()



udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
SERVIDOR = (IP, PORTA) 
udp.bind(SERVIDOR) 
                                
while True:
    con,adress = udp.recvfrom(1024)
    thread = threading.Thread(target=listen_ap,args=(con,adress)) #Monta Thread
    thread.start() #Executa Thread
    ap_num = (threading.activeCount() - 1)
    print(f"Apartamento {ap_num} Conectou-se") #Gerencia Threads 
