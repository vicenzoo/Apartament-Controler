
import socket
import threading
import time

IP = '127.0.0.1'                              
PORTA = 8000
SERV = (IP,PORTA)
sair = "!sair"

def listen_ap():

    ap_listen = udp.recvfrom(1024)
    #ap_listen = ap_listen.decode('utf8')
    strtoint = int(ap_listen[0])
    #print(ap_listen[0])





    if (strtoint <= 70):
        pass

    if (strtoint >= 70 and strtoint <= 79):
        print(f"Apartamento {ap_num}: Está causando um Barulho Leve")

    if (strtoint >= 80 and strtoint <= 89):
        print(f"Apartamento {ap_num}: Está causando um Barulho Moderado")

    if (strtoint >= 90 and strtoint <= 139):
        print(f"Apartamento {ap_num}: Está causando um Barulho Alto!")
    
    if (strtoint >= 140):
        print(f"Apartamento {ap_num}: Está causando um Barulho Altissimo! [ENTRAR EM CONTATO]")



def handle_client(con,adress):

    
    aliveV = True

    while aliveV:
        print(f"Apartamento entrou {adress}")
        time.sleep(5)
        ap_sair = udp.recvfrom(1024)
        if ap_sair == sair:
            aliveV = False        
    con.close()


udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
SERVIDOR = (IP, PORTA) 
udp.bind(SERVIDOR) 
                                
while True:
    con, adress = udp.recvfrom(1024)
    thread = threading.Thread(target=handle_client,args=(con,adress)) #Monta Thread
    thread.start() #Executa Thread
    ap_num = (threading.activeCount() - 1)
    print(f"Apartamento {ap_num} Conectou-se") #Gerencia Threads 
    listen_ap()
