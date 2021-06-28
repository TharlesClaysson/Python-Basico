class futebol:
    posicao_jogo = 0
    altura = 0
    peso = 0
    imc = 0


def cabecalho(a,b=''):
    print('-'*35)
    c = (f'{"Dados do arquivo "}{a}')
    print(f'{c:.^35}')
    print('.'*35)
    print(f'{"posição":<15}{"altura":<8}{"peso":<7}{b}')
    print('-'*35)
 

def apresentar():
    arq = open('futebol_imc.txt','r')
    cabecalho('futebol_imc','imc')
    for c in arq.readlines():
        posicao,altura,peso,imc = c.strip().split(',')
        print(f'{posicao:.<15}{altura:.<8}{peso:.<7}{imc}')
    arq.close()


def main():
    arq = open('futebol_imc.txt','w')
    arquivo = open('futebol.txt','r')
    cabecalho('futebol')
    for c in arquivo.readlines():
        a = futebol()
        posicao,altura,peso = c.strip().split(',')
        print(f'{posicao:.<15}{altura:.<8}{peso:.<7}')
        a.posicao_jogo = posicao
        a.altura = float(altura)
        a.peso = float(peso)
        a.imc = a.peso/a.altura**2
        arq.write(f'{a.posicao_jogo},{a.altura},{a.peso},{a.imc:.2f}\n')
    arq.close()
    arquivo.close()
    apresentar()


main()
