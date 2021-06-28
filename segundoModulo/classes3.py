class Produto:
    nome = ''
    codigo = 0
    compra = 0.0
    venda = 0.0


def cadastrar(catalogo):
    for c in range(2):
        dados = Produto()
        dados.nome = input('Digite o nome do produto: ')
        dados.codigo = int(input('Insira o código do produto '))
        dados.compra = float(input('Digite o preço do produto R$: '))
        catalogo.append(dados)


def calcular(prod):
    for c in range(2):
        prod[c].venda = prod[c].compra * 0.1 + prod[c].compra


def visualizar(catalogo):
    print(';'*80)
    print(f'{​​​​"Catálogo":^80}​​​​')  
    print(';'*80)  
    print(f'{​​​​"produto":<20}​​​​{​​​​"código":^20}​​​​{​​​​"preço de custo":<20}​​​​{​​​​"preço de venda":>20}​​​​')
        for i in range(len(catalogo)):
            print(f'{​​​​catalogo[i].nome:.<20}​​​​{​​​​catalogo[i].codigo:.^20}​​​​',end='')
            print(f'R$:{​​​​catalogo[i].compra:.<17.2f}​​​​R$:{​​​​catalogo[i].venda:.>17.2f}​​​​')


def main():
    opcao = 1
    catalogo = []
    while opcao >= 1 and opcao <= 3:
        print('\nMenu de opções')
        print('1. Cadastrar produtos')
        print('2. Calcular aumento')    
        print('3. Visualizar todos os dados')
        print('4. Sair')
        opcao = int(input('Qual opção deseja? '))
        if opcao == 1:
            cadastrar(catalogo)
        elif opcao == 2:
            calcular(catalogo)
        elif opcao == 3:
            visualizar(catalogo)


main()

