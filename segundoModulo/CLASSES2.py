class pasta:
  nome =''
  codigo = 0
  compra = 0


def main():
  catalogo = []
  for c in range(5): 
    dados = pasta()
    dados.nome = input('Digite o nome do produto: ')
    dados.codigo = int(input('Insira o código do produto '))
    dados.compra = float(input('Digite o preço do produto R$: '))
    dados.venda = (dados.compra * 0.1)+dados.compra
    catalogo.append(dados)
  print(';'*80)
  print(f'{"Catálogo":^80}')
  print(';'*80)
  print(f'{"produto":<20}{"código":^20}{"preço de custo":<20}{"preço de venda":>20}')
  for i in range(len(catalogo)):
    print(f'{catalogo[i].nome:.<20}{catalogo[i].codigo:.^20}',end='')
    print(f'R$:{catalogo[i].compra:.<17.2f}R$:{catalogo[i].compra * 0.1 + catalogo[i].compra:.>17.2f}')  

main()
