def dadosPesq():
    I = []
    S = []
    O = []
    C = []
    for i in range(5):
        print('__'*30)
        I.append(int(input('Informe a idade: ')))
        sexo = input('Informe o sexo(M - masculino ou F - feminino): ')
        S.append(sexo)

        corOlhos = input('Informe a cor dos olhos(A - azuis ou C - castanhos): ')
        O.append(corOlhos)

        corCabelo = input('Informe a cor dos cabelos(L - louros, P - pretos ou C - castanhos): ')
        C.append(corCabelo)
    return I, S, O, C

def mediaIdade():
    I, S, O, C = dadosPesq()
    acuIda = 0
    quantP = 0
    for cont in range(5):
        if 'C' in O[cont] and 'P' in C[cont]:
            acuIda += I[cont]
            quantP += 1
    MediaI1 = acuIda / quantP
    return I, S, O, C, MediaI1

def maiorIdade():
    I, S, O, C, MediaI1 = mediaIdade()
    MediaI2 = MediaI1
    MaiorI1 = 0
    for i in range(5):
        if I[i] >= MaiorI1:
            MaiorI1 = I[i]
    return I, S, O, C, MaiorI1, MediaI2

def qIndF():
    I, S, O, C, MaiorI1, MediaI2 = maiorIdade()
    qIndF1 = 0
    for i in range(5):
        if I[i] >= 18 and I[i] <= 35:
            if 'F' in S[i] and 'A' in O[i] and 'L' in C[i]:
                qIndF1 += 1
    return MaiorI1, MediaI2, qIndF1
    
def main():
    MaiorI3, MediaI3, qIndF2 = qIndF()
    print('__Média__'*30)
    print('A média de idades das pessoas com olhos castanhos e cabelos pretos é: ',MediaI3)
    print('__Maior idade__'*30)
    print('A maior idade entre os habitantes é de ',MaiorI3,' anos.')
    print('__Quantidade de individuos__'*30)
    print('A quantidade de indivíduos do sexo feminino com idade entre 18 e 35 anos(inclusive) e que tenham olhos azuis e cabelos louros é: ',qIndF2)
    
main()


