'''Crie uma função para calcular a média de um aluno, a partir de duas provas
P1, P2 e avalie se o aluno foi aprovado ou reprovado.
Crie a função main, calcularMédia, AvaliarSituação
Utilize a passagem de parâmetros'''
def AvaliarSituacao(m):
    print('aprovado'if m >= 6 else 'reprovado')

def calcularMedia(n1,n2):
    media = (n1 + n2)/2
    print('A média do aluno é: ',media)
    AvaliarSituacao(media)
    
def main():
    p1 = float(input('Digite a nota da P1: '))
    p2 = float(input('Digite a nota da P2: '))
    calcularMedia(p1,p2)

main()
