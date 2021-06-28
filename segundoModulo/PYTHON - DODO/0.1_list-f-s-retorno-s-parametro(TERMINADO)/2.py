def somaNumeros():
    valor1 = float(input('Informe um valor: '))
    valor2 = float(input('Informe outro valor: '))
    if valor1 > valor2:
        contemA = valor1
        valor1 = valor2
        valor2 = contemA
    soma = 0
    contador = valor1
    while contador <= valor2:
        soma = soma + contador
        contador +=1
    print('A soma seria: ',soma)

def main():
    somaNumeros()

main()
