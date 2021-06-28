def calcularMedia():
    p1 = float(input('Digite a primeira nota: '))
    p2 = float(input('Digite a segunda nota: '))
    media =(p1 + p2)/2
    return media,p1,p2


def main():
    x = calcularMedia()
    print('A média resultante é: ',x[0],x[1],x[2])


main()
