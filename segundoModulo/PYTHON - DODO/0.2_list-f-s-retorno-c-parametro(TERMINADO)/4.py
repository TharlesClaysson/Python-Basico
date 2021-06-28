def precoReajus(preco):
    resul = preco * 1.09
    print('O resultado do preço reajustado em 9 por cento é de R$%.2f'% (resul))
    
def main():
    preco = float(input('Informe o valor do produto R$: '))
    precoReajus(preco)

main()
