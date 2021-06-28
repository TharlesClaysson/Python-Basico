#fiz de um modo diferente do que estava pedindo no exercicio, e ele nao tem um return
#mas acho que este esta ate melhor do que o primeiro

def soma(N1, N2):# f soma
    somaDoisN = N1 + N2
    print(N1,' + ',N2,' = ',somaDoisN)
    
def subtrai(N1, N2):# f subtrai
    subtraiDoisN = N1 - N2
    print(N1,' - ',N2,' = ',subtraiDoisN)
    
def multiplica(N1, N2):# f multiplica
    multiplicaDoisN = N1 * N2
    print(N1,' x ',N2,' = ',multiplicaDoisN)
    
def divide(N1, N2):# f divide
    divideDoisN = N1 / N2
    print(N1,' % ',N2,' = ',divideDoisN)
    
def main():
    print('*** Minha Calculadora ***')
    operador = input('''Informe a operação matemática:
+ Soma dois números
- Subtrai dois números
* Multiplica dois números
/ Divide dois números
OPERADOR: ''')
    while operador == '+' or operador == '-' or operador == '*' or operador == '/': 
        N1 = float(input('Digite um número: '))
        N2 = float(input('Digite outro número: '))
        
        if operador == '+':
            soma(N1, N2)
            
        elif operador == '-':
            subtrai(N1, N2)
            
        elif operador == '*':
            multiplica(N1, N2)

        else:
            divide(N1, N2)

        operador = input('''Informe a operação matemática:
+ Soma dois números
- Subtrai dois números
* Multiplica dois números
/ Divide dois números
OPERADOR: ''')
        
main()
