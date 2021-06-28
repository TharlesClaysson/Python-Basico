def mostrarM(matriz,L ,C):
    for lin in range(L):
        for col in range(C):
            print(matriz[lin][col],end='\t')
        print()
    qLeC(matriz)
    

def qLeC(matriz):
    l = len(matriz)
    c = len(matriz[0])
    print(f'A matriz tem {l} linhas e {c} colunas')
    return
    
def main():
    L = int(input('Informe a quantidade de linha que a matriz vai ter: '))
    C = int(input('Informe a quantidade de coluna que a metriz vai ter: '))
    matriz = []
    for l in range(L):
        linha = []
        for c in range(C):
            linha.append(input(f'Informe um valor para [{l}, {c}]: '))
        matriz.append(linha)
    mostrarM(matriz, L, C)
    
main()
