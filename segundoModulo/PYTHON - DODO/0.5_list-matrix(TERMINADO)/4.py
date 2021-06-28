def recebMatriz(mA, mB):
    qLinhaA = len(mA)
    qColunaA = len(mA[0]) 
    qColunaB = len(mB[0])
    if qColunaB == qLinhaA:
        c_mat = []
        for linA in range(qLinhaA):
            c_mat.append([])
            for colB in range(qColunaB):
                for colA in range(qColunaA):
                    mult = mA[linA][colA] * mB[colA][colB]
                c_mat[linA].append(mult)
                
        qLinhaC = len(c_mat)
        qColunaC = len(c_mat[0])   
        return c_mat, qLinhaC, qColunaC
    
def main():
    qLMmatA = int(input('Informe a quantidade de linha que a matriz A vai ter: '))
    qCmatA = int(input('Informe a quantidade de coluna que a metriz A vai ter: '))
    mA = []
    for lin in range(qLMmatA):
        linha = []
        for col in range(qCmatA):
            linha.append(int(input(f'Informe um valor para [{lin}, {col}]: ')))
        mA.append(linha)

    qLMmatB = int(input('Informe a quantidade de linha que a matriz B vai ter: '))
    qCmatB = int(input('Informe a quantidade de coluna que a metriz B vai ter: '))
    mB = []
    for lin in range(qLMmatB):
        linha = []
        for col in range(qCmatB):
            linha.append(int(input(f'Informe um valor para [{lin}, {col}]: ')))
        mB.append(linha)
    recebMatriz(mA, mB)
    M, LC, CC = recebMatriz(mA, mB)
    for lin in range(LC):
        for col in range(CC):
            print(M[lin][col],end='\t')
        print()
main()
