def precoReajus2(preco, porcent):
    conver = (porcent / 100)+1
    resul = preco * conver
    print('O resultado do preço reajustado em %.2f por cento é de R$%.2f' % (porcent, resul))
    
def main():
    preco = float(input('Informe o valor do produto R$: '))
    porcent = float(input('Informe a porcentagem: '))
    precoReajus2(preco, porcent)

main()
