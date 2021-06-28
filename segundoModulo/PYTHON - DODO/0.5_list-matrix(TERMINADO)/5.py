#primeiro mmodo
def mostrarM(matriz):
    diagP = []
    aciDiagP = []
    for l in range(4):
        for c in range(4):
            if l == c:
                diagP.append(matriz[l][c])
            elif l < c:
                aciDiagP.append(matriz[l][c])
                
    print('Elementos da diagonal principal: ',diagP)
    print('Elementos que estão acima da diagonal principal: ',aciDiagP)
    somaDP = 0
    for cont in diagP:
        somaDP += cont
    print('A soma dos elementos da diagonal principal é de ',somaDP)
    somaAcimaDP = 0
    for cont in aciDiagP:
        somaAcimaDP += cont
    print('A soma dos elemento que estão acima da diagonal principal é de ',somaAcimaDP)
                             
def main():
    matriz = []
    for lin in range(4):
        linha = []
        for col in range(4):
            print('__'*30)
            linha.append(int(input(f'Informe um valor para [{lin}, {col}]: ')))
        matriz.append(linha)
    mostrarM(matriz)
main()
#segundo modo
def mostrarM(matriz):
    diagP = aciDiagP = 0
    for l in range(4):
        for c in range(4):
            if l == c:
                diagP += matriz[l][c]
            elif l < c:
                aciDiagP += matriz[l][c]
    print('Elementos da diagonal principal: ',diagP)
    print('Elementos que estão acima da diagonal principal: ',aciDiagP)
    print('A soma dos elementos da diagonal principal é de ',diagP)
    print('A soma dos elemento que estão acima da diagonal principal é de ',aciDiagP)
                 
def main():
    matriz = []
    for lin in range(4):
        linha = []
        for col in range(4):
            print('__'*30)
            linha.append(int(input(f'Informe um valor para [{lin}, {col}]: ')))
            
        matriz.append(linha)
    mostrarM(matriz)
main()
