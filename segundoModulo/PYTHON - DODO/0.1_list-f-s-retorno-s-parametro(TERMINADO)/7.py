def notasAluno():
    n1 = int(input('Informe a primeira nota: '))
    n2 = int(input('Informe a segunda nota: '))
    n3 = int(input('Informe a terceira nota: '))
    print('A = calcular média aritimética; P = calcular média ponderada')
    letra = input('Informe a letra: ')
    if letra == 'A' or letra == 'a':
        media_ari = (n1 + n2 + n3) / 3
        print('A média aritimética é de ',media_ari)
    if letra == 'P' or letra == 'p':
        media_ponderada = ((n1*5) + (n2*3) + (n3*2))/ (5+3+2)
        print('A média ponderada é de ',media_ponderada)
    
def main():
    notasAluno()

main()
