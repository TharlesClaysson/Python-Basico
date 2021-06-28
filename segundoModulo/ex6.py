'''Crie uma função que some dois números e apresente o resultado.
Não use passagen de parâmetro, mas retorne o resultado para então
apresentar'''
def soma():
    n1 = float(input('Informe um valor '))
    n2 =float(input('Informe outro valor '))
    r = n1+n2
    return r

def main():
    s = soma()#chamada de função
    print(s)
    #ou
    print(soma())#chamada da função

main()
