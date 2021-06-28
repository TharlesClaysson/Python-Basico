def recMatriz(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])
    if linhas == colunas:
        return True
        
    else:
        return False
    
def main():
    qL = int(input('Informe a quantidade de linha que a matriz vai ter: '))
    qC = int(input('Informe a quantidade de coluna que a metriz vai ter: '))
    matriz = []
    for lin in range(qL):
        linha = []
        for col in range(qC):
            linha.append(input(f'Informe um valor para [{lin}, {col}]: '))
        matriz.append(linha)
    for lin in range(qL):
        for col in range(qC):
            print(matriz[lin][col],end='\t')
        print()
    recMatriz(matriz)
    print(recMatriz(matriz))

main()
