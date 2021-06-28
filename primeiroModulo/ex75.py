a = (int(input('Digite um valor: ')),
    int(input('Digite outro valor: ')),
    int(input('Digite mais um valor: ')),
    int(input('Digite o último valor: ')))
'''meu jeito
e = 0
for valor in a:
    if valor % 2 == 0:
        e += 1         '''

print(f'Você digitou os valores: {a}')
print(f'O número 9 apareceu {a.count(9)} vezes')
if 3 in a:
    print(f'O número 3 está na {a.index(3)+1}° posição ')
else:
     print(f'O número 3 não está na lista')
''' meu print dos valores pares    
print(f'A tupla tem {e} números pares')                     '''
# jeito do guanabara
print('Os valores pares digitados são',end='')
for valor in a:
    if valor % 2 == 0:
        print(f', {valor}',end='')
