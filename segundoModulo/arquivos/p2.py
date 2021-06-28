class func:
    cod = 0
    nome = ''
    sal = 0


def cadastrar(a):
    print('Cadastro')
    print('-'*50)
    arquivo = open('funcionario.txt','w')
    for c in range(5):
        dados = func()
        dados.cod = int(input('Digite o codigo do funcionário: '))
        dados.nome = input('Digite o nome do funcionário: ')
        dados.sal = float(input('Digite o salário do funcionário: '))
        arquivo.write(f'{dados.cod}_{dados.nome}_{dados.sal:.2f}\n')
        a.append(dados)
    arquivo.close()

def titulo():
    print('-'*50)
    print(f'{"Funcionários cadastrados:":^50}')
    print(f'{"código":<10}{"nome":<30}{"salário":>10}')
    print('-'*50)

    
def mostrarvet(a):
    titulo()
    for c in range(len(a)):
        print(f'{a[c].cod:.<10}{a[c].nome:.<30}{a[c].sal:.>10}')


def mostrararq():
    titulo()
    arquivo = open('funcionario.txt','r')
    for c in arquivo.readlines():
        cod,nome,sal = c.strip().split('_') 
        print(f'{cod:.<10}{nome:.<30}{sal:.>10}')
    arquivo.close()
    

def excluir(a):
    print('-'*50)
    print(f'{"EXCLUSÃO DE FUNCIONÁRIO":^50}')
    print('-'*50)
    while True:
        codigo = int(input('Digite o código do funcionário: '))
        seg = 0
        z = 0
        for c in range(len(a)):
            if codigo == a[c].cod:
                seg += 1
                z = c
        if seg == 0:
            print('Este código nao existe!')
        else:
            break
    a.pop(z)
    arquivo = open('funcionario.txt','w')
    for d in range(len(a)):
        arquivo.write(f'{a[d].cod}_{a[d].nome}_{a[d].sal:.2f}\n')
    arquivo.close()
                

def alterar(a):
    print('-'*50)
    print(f'{"alterar funcionário":^50}')
    print('-'*50)
    while True:
        codigo = int(input('Digite o código do funcionário: '))
        seg = 0
        z = 0
        for c in range(len(a)):
            if codigo == a[c].cod:
                seg += 1
                z = c
        if seg == 0:
            print('Este código nao existe!')
        else:
            break
    a[c].nome = input('digite o novo nome: ')
    a[c].sal = float(input('digite o novo salário: '))
    arquivo = open('funcionario.txt','w')
    for d in range(len(a)):
        arquivo.write(f'{a[d].cod}_{a[d].nome}_{a[d].sal:.2f}\n')
    arquivo.close()
           
                
def main():
    funcionarios =[]
    print('-'*50)
    print(f'{"Menu de opções:^30"}')
    print('-'*50)
    print('1- Cadastrar no vetor e arquivo')
    print('2- Mostrar do vetor')
    print('3- Mostrar do arquivo')
    print('4- Excluir pelo código')
    print('5- Alterar nome e salário')
    print('Sair')
    print('-'*50)
    while True:
        menu = int(input('Digite uma opção: '))
        if menu == 1:
            if len(funcionarios) >= 5:
                print('O cadastro já está completo!')
            else:
                cadastrar(funcionarios)
        elif menu == 2:
            mostrarvet(funcionarios)
        elif menu == 3:
            mostrararq()
        elif menu == 4:
            excluir(funcionarios)
        elif menu == 5:
            alterar(funcionarios)
        elif menu == 6:
            print('Até logo!')
            break
        else:
            print('Comando inválido!')


main()
