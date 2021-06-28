
'''Crie uma função que some dois números e apresente o resultado. Crie a função main.
Estan função não terá retorno e TEM PARÂMETRO

DECLARAÇAO DA FUNÇÃO'''
def SomaNumeros(n1,n2):
    r = n1 + n2
    print('O resultado é ',r)

def main():
    n1 = int(input('Digite um valor: '))
    n2 = int(input('Digite outro valor: '))
    SomaNumeros(n1,n2)

#chamada da função
main()
