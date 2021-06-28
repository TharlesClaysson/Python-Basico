def avaliarSituacao(media):
    if media >= 6:
        return 'Aprovado'
    else:
        return 'Reprovado'

def calcularMedia(P1, P2):
    media = (P1 + P2) / 2
    avaliarSituacao(media)
    
def main():
    P1 = float(input('Digite a primeira nota: '))
    P2 = float(input('Digite a segunda nota: '))
    calcularMedia(P1, P2)
    avaliarSituacao(media)
    print(avaliarSituacao(media))
    
main()
#outro modo - parece que esse deu certo mas eu nao sei se este modo esta certo
def avaliarSituacao(media):
    if media >= 6:
        print('Aprovado')
    else:
        print('Reprovado')
    return

def calcularMedia(P1, P2):
    media = (P1 + P2) / 2
    avaliarSituacao(media)
    
def main():
    P1 = float(input('Digite a primeira nota: '))
    P2 = float(input('Digite a segunda nota: '))
    calcularMedia(P1, P2)
    
main()
