def vetorNperf():
    vetor = []
    n = 500
    for i in range(1, n):
        soma = 0
        for o in range(1, i):
            if i % o == 0:
                soma += o
        if i == soma:
            vetor.append(i)
    print(vetor)     
vetorNperf()

def vetorNperf():
    vetor = []
    N = 500
    for I in range(1, N):
        soma = 0
        for D in range(1, I):
            if I % D == 0:
                soma += D
        if I == soma:
            vetor.append(I)
    return vetor
def main():
    print(vetorNperf())
main()
