from threading import Thread
import time, os
# código da thread
def corredor(nome, pausa, distancia):
    percorrido = 0
    print(nome, "iniciou!")
    while percorrido <= distancia:
        print(nome, ":", percorrido, "/", distancia)
        percorrido += 1
        time.sleep(pausa)
        print(nome, "terminou.")
# define as threads
corredor1 = Thread(target=corredor, args=["Onofre", 0.3, 50])
corredor2 = Thread(target=corredor, args=["Godofredo", 0.9, 30])
os.system("cls" if os.name== "nt" else"clear")
input("Pressione Enterpara iniciar a corrida:\n")
# inicia as threads
corredor1.start()
corredor2.start()
# continua com o bloco (thread) principal de comandos
print("Os corredores iniciaram a corrida!")
time.sleep(10)
input("Pressione Enterpara encerrar:\n")
