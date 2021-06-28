from random import randint
num = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))
print('Os valores sorteados são',end='')
maior = -float('inf')
menor = float('inf')
for n in num:
    print(f',{n} ',end='')
    if n > maior:
        maior = n
    if n < menor:
        menor = n
print('\nmaior: ',maior)
print('menor: ',menor)

