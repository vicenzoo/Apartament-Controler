import socket
import threading
import random
import time

sair = "!OUT" #Texto para desconectar Apartamento
alive = True
maxtime = 10 #Tempo Maximo

#Causas
c1 = "Fez um Barulho acima dos 1000 decibeis"
c2 = "Está Arrastando Movéis após as 22h"
c3 = "Está carregando moveis de mudança fora da garagem"
c4 = "Barulho Elevado de Cachorro!"
c5 = "Barulho Elevado de Criança chorando!"
c6 = "Barulho Elevado de Calçado Alto!"

causes = [c1,c2,c3,c4,c5,c6] #Array de Motivos para Notificação

#Função notificação de barulhos
def noises():
    while alive:
        exec = 0 #Tempo de execução
        time.sleep(10)
        exec += 1
        num = random.randint(1,threading.activeCount() - 1) #Sorteia apartamento
        notification = random.choice(causes) #Sorteia Causa
        print(f"-> Apartamento {num}: {notification}. [ENTRAR EM CONTATO]") #Notificação

        if (exec >= maxtime): #Pausa
            exec = 0
            time.sleep(5)



 
#Thread de Gerenciamento de apartamentos
def handle_client(con,adress):
    print(f"Apartamento entrou {adress}")
    time.sleep(5)
    noises()

    while alive:
        ap_sair = con.recv(1024)
        if ap_sair == sair:
            alive = False           
        con.send(ap_sair.encode())
    con.close()


#Server Central
def main():
    print("Central Online!")
    SERVER = ('127.0.0.1', 8000) #Configura server
    TCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    TCP.bind(SERVER)
    TCP.listen(1)
    while True:
        con,adress = TCP.accept()
        thread = threading.Thread(target=handle_client,args=(con,adress)) #Monta Thread
        thread.start() #Executa Thread
        print(f"Apartamento {threading.activeCount() - 1} Conectou-se") #Gerencia Threads

main()
