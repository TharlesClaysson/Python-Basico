class TipoCadastroB:
    numeroC = 0
    nomeTit = ''
    saldoTitu = 0.0

def menuOp():
    vetorContas = []
    while True:
        print('__'*30)
        print('Menu de opções:')
        print('1.Cadastrar contas')
        print('2.Visualizar todas as contas')
        print('3.Consultar por nome')
        print('4.Alterar nome e/ou saldo de um número de conta')
        print('5.Excluir a conta com menor saldo')
        print('6.Sair')
        escolha1 = int(input('Informe a opção: '))
        if escolha1 == 1:
            cadastro(vetorContas)
        elif escolha1 == 2:
            visuTcontas(vetorContas)
        elif escolha1 == 3:
            consulN(vetorContas)
        elif escolha1 == 4:
            altNouSaldo(vetorContas)
        elif escolha1 == 5:
            excluirCmenorS(vetorContas)
        elif escolha1 == 6:
            print('Saída efetuada')
            break
        else:
            print('Opção inválida')

def cadastro(vetorContas):#1
    quantCadastro = 0
    repetir = 's'
    while repetir == 'S' or repetir == 's':
        CC = TipoCadastroB()
        CC.numeroC = int(input('Número da conta: '))
        CC.nomeTit = input('Nome do titular: ')
        CC.saldoTitu = float(input('Saldo: '))
        vetorContas.append(CC)
        quantCadastro += 1
        if quantCadastro == 16:
            print('Quantidade maxima de cadastros alcançada')
            return vetorContas
        repetir = input('Cadastrar outra conta ?(S/N): ')
    return vetorContas

def visuTcontas(vetorContas):#2
    for i in range(len(vetorContas)):
        print('__'*30)
        print('Número da conta: {}\nNome do titular: {}\nSaldo: {}'.format(vetorContas[i].numeroC, vetorContas[i].nomeTit, vetorContas[i].saldoTitu))
        print('__'*30)

def consulN(vetorContas):#3
    consultaT1 = input('Informe o nome do titular: ')
    for i in range(len(vetorContas)):
        if vetorContas[i].nomeTit == consultaT1:
            print('__'*30)
            print('Número da conta: {}\nNome do titular: {}\nSaldo: {}'.format(vetorContas[i].numeroC, vetorContas[i].nomeTit, vetorContas[i].saldoTitu))
            print('__'*30)
            
def altNouSaldo(vetorContas):#4
    print('__'*30)
    print('Menu de opções:')
    print('1.Alterar nome')
    print('2.Alterar saldo de um número de conta')
    print('3.Alterar nome e saldo de um número de conta')
    escolha2 = int(input('Informe a opção: '))
    if escolha2 == 1:
        alterarN(vetorContas)
        return vetorContas
    elif escolha2 == 2:
        alterarS(vetorContas)
        return vetorContas
    elif escolha2 == 3:
        altNeS(vetorContas)
        return vetorContas
    else:
        print('Opção inválida')

def alterarN(vetorContas):#4.1
    consultaT2 = input('Informe o nome a ser alterado: ')
    for i in range(len(vetorContas)):
        if vetorContas[i].nomeTit == consultaT2:
            nomeAlt = input('Informe um novo nome: ')
            vetorContas[i].nomeTit = nomeAlt
            print('__'*30)
            print('Número da conta: {}\nNome do titular: {}\nSaldo: {}'.format(vetorContas[i].numeroC, vetorContas[i].nomeTit, vetorContas[i].saldoTitu))
            print('__'*30)
    return vetorContas

def alterarS(vetorContas):#4.2
    consultaT2 = int(input('Informe o número de conta: '))
    for i in range(len(vetorContas)):
        if vetorContas[i].numeroC == consultaT2:
            saldoAlt = input('Informe o novo saldo a ser alterado: ')
            vetorContas[i].saldoTitu = saldoAlt
            print('__'*30)
            print('Número da conta: {}\nNome do titular: {}\nSaldo: {}'.format(vetorContas[i].numeroC, vetorContas[i].nomeTit, vetorContas[i].saldoTitu))
            print('__'*30)
    return vetorContas

def altNeS(vetorContas):#4.3
    consultaT2 = input('Informe o nome a ser alterado: ')
    for i in range(len(vetorContas)):
        if vetorContas[i].nomeTit == consultaT2:
            nomeAlt = input('Informe um novo nome: ')
            vetorContas[i].nomeTit = nomeAlt
    consultaT2 = int(input('Informe o número de conta: '))
    for i in range(len(vetorContas)):
        if vetorContas[i].numeroC == consultaT2:
            saldoAlt = input('Informe o novo saldo a ser alterado: ')
            vetorContas[i].saldoTitu = saldoAlt
    return vetorContas


def excluirCmenorS(vetorContas):
    menorSaldo = 0
    maiorSaldo = 0
    menorSn = 0
    for i in range(len(vetorContas)):
        if vetorContas[i].saldoTitu >= maiorSaldo:
            maiorSaldo = vetorContas[i].saldoTitu
        else: 
            menorSaldo = vetorContas[i].saldoTitu
            menorSn = i
    del(vetorContas[menorSn])

def main():
    menuOp()

main()
