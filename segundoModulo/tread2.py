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

os.system("cls" if os.name== "nt" else"clear")
input("Pressione Enterpara iniciar a corrida:\n")
print("Os corredores iniciaram a corrida!")
# define e inicia as threads
Thread(target=corredor, args=["Onofre", 0.3, 30]).start()
Thread(target=corredor, args=["Godofredo", 0.3, 30]).start()

# continua com o bloco (thread) principal de comandos
time.sleep(10)
input("Pressione Enterpara encerrar:\n")
