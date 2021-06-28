#primeiro modo
def lerM(ML, MC):
    M = []
    for l in range(ML):
        linha = []
        for c in range(MC):
            linha.append(input(f'Informe um valor para [{l}, {c}]: '))
        M.append(linha)
    return M

def main():
    ML = int(input('Informe a quantidade de linha que a matriz vai ter: '))
    MC = int(input('Informe a quantidade de coluna que a metriz vai ter: '))
    apresM = lerM(ML, MC)
    for lin in range(ML):
        for col in range(MC):
            print(apresM[lin][col],end='\t')
        print()
    
main()
#segundo modo
def lerM(ML, MC):
    M = []
    for l in range(ML):
        linha = []
        for c in range(MC):
            linha.append(input(f'Informe um valor para [{l}, {c}]: '))
        M.append(linha)
    return M

def main():
    ML = int(input('Informe a quantidade de linha que a matriz vai ter: '))
    MC = int(input('Informe a quantidade de coluna que a metriz vai ter: '))
    apresM = lerM(ML, MC)
    print(apresM)
    
main()
