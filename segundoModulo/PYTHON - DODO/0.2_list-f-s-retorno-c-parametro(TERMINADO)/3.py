def avaliarSituacao(media):
    if media >= 6:
        print('aprovado')
    else:
        print('reprovado')

def calcularMedia(p1, p2):
    media = (p1 + p2) / 2
    avaliarSituacao(media)
    
def main():
    p1 = float(input('Digite a primeira nota: '))
    p2 = float(input('Digite a segunda nota: '))
    calcularMedia(p1, p2)

main()
