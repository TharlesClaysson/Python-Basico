from threading import Thread
import time, os

def fat(fatorial,tempo):
    indice =[fatorial] 
    resp = z = fatorial
    print(f'{fatorial}! iniciou!')
    while z > 1:
        z -= 1
        resp *= z
        indice.append(z)
        print(f'{fatorial}! = ',end='')
        for i in range(len(indice)):
            print(f' {indice[i]} * ',end='')
        print('em andamento! Cálculo temporário: =',resp,)
        time.sleep(tempo)
    print(f'{fatorial}! terminou, resposta: {resp} finalizado!')

os.system('cls' if os.name == 'nt' else 'clear')
v = []
t = []
quant = int(input('Digite a quantidade de fatoriais desejada: '))
for c in range(0,quant):
    f = int(input(f'Digite o valor do {c+1}° fatorial: '))
    fatia = float(input(f'Digite a fatia de tempo desejada para {f}!: '))
    v.append(f)
    t.append(fatia)
input(f'Pressione Enter para Calcular os fatoriais: {v}: ')
print('iniciando cálculo dos fatoriais',v)

for i in range(len(v)): 
    Thread(target=fat, args=[v[i], t[i]]).start()

time.sleep(10)
input('Pressione Enter para encerrar:\n')