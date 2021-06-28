'''Crie uma função que multiplique dois números e apresente o resultado. Crie a função main.
Esta função essa terá parâmetro.'''

def Numerosdaformula(a,b):# a = n1  e b = n2
    r = a * b
    print('Resultado: ',r)
#A diferênça entre elas está na declaração dos parâmetros
def main():
    n1 = int(input('Digite um valor: '))
    n2 = int(input('Digite outro valor: '))
    Numerosdaformula(n1,n2)#chamada da função


#Execução da função
main()
