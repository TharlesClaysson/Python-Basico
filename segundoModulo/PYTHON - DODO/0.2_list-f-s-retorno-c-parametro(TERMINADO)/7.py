def parImpar(valor):
    if valor%2:
        print('O valor ',valor,' é Ímpar')
    else:
        print('O valor ',valor,' é Par')

def lerValor():
    print('conferir se o valor é par o ímpar')
    valor = int(input('Informe um valor: '))
    parImpar(valor)
    
def main():
    lerValor()

main()
