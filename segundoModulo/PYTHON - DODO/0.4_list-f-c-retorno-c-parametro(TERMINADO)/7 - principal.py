#primeiro modo que achei, na hora de sair do laço de repetição, eu entendi que era para
#digitar um operador diferente, ou seja algo que seja diferente dos numeradores do menu

def menuCalcu():# menu de opções 
    print('*** Minha Calculadora ***')
    N1 = float(input('Digite um número: '))
    N2 = float(input('Digite outro número: '))

    print('+ Soma dois números')
    print('- Subtrai dois números')
    print('* Multiplica dois números')
    print('/ Divide dois números')
    
    opcaoC = input('Qual opção deseja? ')

    if opcaoC == '+':
        soma(N1, N2)
            
            
    elif opcaoC == '-':
        subtrai(N1, N2)
            
            
    elif opcaoC == '*':
        multiplica(N1, N2)

    elif opcaoC == '/':
        divide(N1, N2)
        
    else:
        S = input('Sair ? S/N: ')
        return
        
def soma(N1, N2):# f soma
    somaDoisN = N1 + N2
    print(N1,' + ',N2,' = ',somaDoisN)
    main()
    
def subtrai(N1, N2):# f subtrai
    subtraiDoisN = N1 - N2
    print(N1,' - ',N2,' = ',subtraiDoisN)
    main()
    
def multiplica(N1, N2):# f multiplica
    multiplicaDoisN = N1 * N2
    print(N1,' x ',N2,' = ',multiplicaDoisN)
    main()
    
def divide(N1, N2):# f divide
    divideDoisN = N1 / N2
    print(N1,' % ',N2,' = ',divideDoisN)
    main()
    
def main():
    sair = menuCalcu()
    while sair == 'S' or sair == 'n':
        menuCalcu()
        
main()
