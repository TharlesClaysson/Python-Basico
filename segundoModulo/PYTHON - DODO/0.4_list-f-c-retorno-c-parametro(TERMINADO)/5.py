def aumentoSalario(VP, S):
    converPorcent = VP / 100
    valorAumento = S * converPorcent
    aumentoS = S + valorAumento
    return aumentoS

def main():
    VP = int(input('Informe o valor de porcentagem de aumento que o salário vai ter: ')) 
    acumulaVelhoSalario = 0
    acumulaNovoSalario = 0
    for i in range(3):
        S = float(input('Informe o salário: '))
        acumulaVelhoSalario += S
        AS = aumentoSalario(VP, S)
        acumulaNovoSalario += aumentoSalario(VP, S)
    print('Será gasto para pagar os novos salários: ',acumulaNovoSalario,'reais')
    print('A diferença entre o que se pagava para todos os funcionário e o que será pago após o aumento é de ',acumulaNovoSalario-acumulaVelhoSalario,'reais')
main()
