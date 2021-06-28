def menorMaior():
    N = int(input('Informe um número inteiro e positivo: '))
    i = 1
    fatorial = 1
    calculo = 1
    for i in range(N+1):
        while calculo <= N:
          fatorial *= calculo
          calculo += 1
        S = calculo/fatorial + 1
    print('{}! = {}'.format(N,fatorial))
    print('Valor de S é {}'.format(S))
def main():
    menorMaior()
    
main()

