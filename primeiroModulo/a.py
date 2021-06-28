a = int(input('Digite um valor: '))
b = int(input('Digite outro valor: '))
c = int(input('Digite mais um valor: '))
d = int(input('Digite o último valor: '))
e = 0
t = a,b,c,d
for valor in t:
    if valor % 2 == 0:
        e += 1
print(f'O número 9 apareceu {t.count(9)} vezes')
if 3 in t:
    print(f'O número 3 está na posição {t.index(3)} ')
else:
     print(f'O número 3 não está na lista')
print(f'A tupla tem {e} números pares')
