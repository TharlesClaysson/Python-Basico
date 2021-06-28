
def somaNumeros(VI, VF):
    if VI > VF:
        contemVI = VI
        VI = VF
        VF = contemVI
    soma = 0
    contador = VI
    while contador <= VF:
        soma = soma + contador
        contador +=1
    print('Soma: ',soma)

def main():
    VI = int(input('Valor inicial: '))
    VF = int(input('Valor final: '))
    somaNumeros(VI, VF)

main()


def somaNumeros(VI, VF):
    if VI > VF:
        contemVI = VI
        VI = VF
        VF = contemVI
    soma = 0
    contador = VI
    while contador <= VF:
        soma = soma + contador
        contador +=1
    print('Soma: ',soma)

def main():
    VI = int(input('Valor inicial: '))
    VF = int(input('Valor final: '))
    somaNumeros(VI, VF)

main()
