def tabMult():
    valor = int(input('Informe um valor inteiro entre 1 e 9: '))
    for i in range(1, valor+1):
        for I in range(1, i+1):
            mult = i * I
            print(mult,end='\t')
        print()
        
def main():
    tabMult()

main()
