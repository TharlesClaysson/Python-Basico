def par(n=0):
    if n%2==0:
        return True
    else:
        return False


num = int(input('Digite um número: '))
print(par(num))
if par(num):
    print(f'{num} é par')
else:
    print(f'{num} é impar')
