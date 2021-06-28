'''def quantNdivis():
    a = int(input('Informe um valor: '))
    b = int(input('Informe um valor: '))
    c = int(input('Informe um valor: '))
    if  > valor2:
        contemA = valor1
        valor1 = valor2
        valor2 = contemA

def main():
    quantNdivis()

main()'''
#aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
def quantNdivis():
    a = int(input('Informe um valor para A: '))
    b = int(input('Informe um valor para B: '))
    c = int(input('Informe um valor para C: '))
    if b > c:
        container = b
        b = c
        c = container
    divisiveis = 0
    while b <= c:
        if b%a == 0:
            divisiveis += 1
        b += 1
    print('A quantidade de número divisiveis são: ',divisiveis)

def main():
    quantNdivis()

main()
