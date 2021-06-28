def parImpar():
    A = []
    B = []
    for i in range(5):
        N = int(input('Informe um número: '))
        A.append(N)
        fatorial = 1
        calculo = 1
        for i in range(1, N+1):
            while calculo <= N:
              fatorial *= calculo
              calculo += 1
        B.append(fatorial)
    return B
def main():
    print(parImpar())

main()
