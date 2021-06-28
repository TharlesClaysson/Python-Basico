def parImpar():
    print('Verificar se o número é par ou ímpar')
    valor = int(input('Informe um valor: '))
    if valor%2:
        return 'É ímpar'
    else:
        return 'É par'
    
def main():
    print(parImpar())

main()
