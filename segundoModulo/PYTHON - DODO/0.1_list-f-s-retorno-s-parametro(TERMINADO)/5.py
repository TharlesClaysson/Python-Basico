def conversao():
    preNovo = float(input('Informe o novo preço: '))
    preAntigo = float(input('Informe o preço antigo: '))
    percentAcresc = (preNovo/preAntigo) * 100 - 100
    print('O percentual de acréscimo é de ',percentAcresc,'%')
    
def main():
    conversao()

main()

def conversao():
    preNovo = float(input('Informe o novo preço: '))
    preAntigo = float(input('Informe o preço antigo: '))
    percentAcresc = (100 * preNovo - 100 * preAntigo) / preAntigo
    print('O percentual de acréscimo é de ',percentAcresc,'%')
    
def main():
    conversao()

main()
