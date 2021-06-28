def precosP(lojas, produtos):
    print('____Preços dos produtos____')
    matrizP = []
    for lin in range(8):
        print('Informe os preços dos produtos da loja {0}'.format(lojas[lin]))
        precos = []
        for col in range(4):
            precos.append(float(input('Informe o preço do(a) {0} R$: '.format(produtos[col]))))
        matrizP.append(precos)
    print('____Lojas e seus produtos com preço que não ultrapasse R$ 120,00____') 
    for lin in range(8):
        for col in range(4):
            if matrizP[lin][col] <= 120:
                print('A loja ',lojas[lin],' com o produto ',produtos[col],' custa R$ ',matrizP[lin][col])
                print('__'*30)   
def main():
    print('____Nomes das lojas____')
    lojas = []
    for i in range(8):
        lojas.append(input(f'Informe o nome da {i + 1}º loja: '))
    print('____Nome dos produtos____')
    
    produtos = [] 
    for o in range(4):
        produtos.append(input(f'Informe o nome do {o + 1}º produto dessas loja: '))
    precosP(lojas, produtos)
    
main()
