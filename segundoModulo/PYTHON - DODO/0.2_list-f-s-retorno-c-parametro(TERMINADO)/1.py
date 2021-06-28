#sem parametros
def MultPor2():
    n = int(input('Informe um número para ser multiplicado por 2: '))
    resul = n * 2
    print('O resultado da multiplicaçao é ',resul)
    
def main():
    MultPor2()

main()

print('__'*30)
#com parametros
def MultPor2(n):
    resul = n * 2
    print('O resultado da multiplicaçao é ',resul)
    
def main():
    n = int(input('Informe um número para ser multiplicado por 2: '))
    MultPor2(n)

main()

