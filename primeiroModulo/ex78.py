lista = []
maior = -float('inf')
menor = float('inf')
for c in range(0,5):
    lista.append(int(input(f'Digite um número para a posição {c}: ')))
    if lista[c] >= maior:
        maior = lista[c]
    if lista[c] <= menor:
        menor = lista[c]
print('=+'*30)
print('Você digitou os valores: ',lista)
print(f'O maior valor digitado foi {maior} nas posições ',end='')
for pos,m in enumerate(lista):
    if m == maior:
        print(pos,'...',end='')
print()
print(f'O menor valor digitado foi {menor} nas posições ',end='')      
for i,v in enumerate(lista):
    if v == menor:
        print(f'{i}...',end='')
print()
