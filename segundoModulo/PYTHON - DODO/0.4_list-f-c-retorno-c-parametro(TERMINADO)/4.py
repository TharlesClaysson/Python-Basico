#a 4 tem a mesma pergunta que a 3
def aumentoSalario(VP, S):
    converPorcent = VP / 100
    valorAumento = S * converPorcent
    aumentoS = S + valorAumento
    return aumentoS
def main():
    S = float(input('Informe o salário: '))
    VP = int(input('Informe o valor de porcentagem de aumento que o salário vai ter: ')) 
    print(S,'reais mais aumento de ',VP,'por cento =',aumentoSalario(VP, S),'reais') 

main()
