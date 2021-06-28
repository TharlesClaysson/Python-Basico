def areaTrian():
    base = int(input('Informe a base do triângulo: '))
    altura = int(input('Informe a altura do triângulo: '))
    return (base * altura)//2
    
def main():
    print('A área do triângulo é de: ',areaTrian())

main()
