class TipoCadastro:
    nomeC = ''
    dataN = ''
    tel = 0
    ender = ''
    serie = 0

def menu():
    vetAluno = []
    while True:
        print('__'*30)
        print('Menu de opções:')
        print('1.Cadastrar alunos')
        print('2.Consulta por nome')
        print('3.Visualizar todos os dados')
        print('4.Sair')
        comando = int(input('Informe a opção: '))
        if comando == 1:
            cadastro(vetAluno)
        elif comando == 2:
            consulta(vetAluno)
        elif comando == 3:
            visuTodDados(vetAluno)
        elif comando == 4:
            print('Saída efetuada')
            break
        else:
            print('Opção inválida')
        
def consulta(vetAluno):
    consultaA = input('Informe o nome completo do aluno: ')
    for i in range(len(vetAluno)):
        if vetAluno[i].nomeC == consultaA:
            print('__'*30)
            print('Nome: {}\nData de nascimento: {}\nTelefone: {}\nEndereço: {}\nSérie: {}'.format(vetAluno[i].nomeC, vetAluno[i].dataN, vetAluno[i].tel, vetAluno[i].ender, vetAluno[i].serie))
            print('__'*30)
        else:
            print('__'*30)
            print('Aluno não encontrado')
            print('__'*30)
            
def visuTodDados(vetAluno):
    for i in range(len(vetAluno)):
        print('__'*30)
        print('Nome: {}\nData de nascimento: {}\nTelefone: {}\nEndereço: {}\nSérie: {}'.format(vetAluno[i].nomeC, vetAluno[i].dataN, vetAluno[i].tel, vetAluno[i].ender, vetAluno[i].serie))
        print('__'*30)
        
def cadastro(vetAluno):
    CA = TipoCadastro()
    CA.nomeC = input('Nome completo do aluno: ')
    CA.dataN = input('Data de nascimento: ')
    CA.tel = int(input('Telefone: '))
    CA.ender = input('Endereço: ')
    CA.serie = int(input('Série(número): '))
    vetAluno.append(CA)
    return vetAluno

def main():
    menu()

main()
