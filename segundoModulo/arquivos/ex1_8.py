class prod:
  codigo = 0
  nome = ''
  preco = 0


print('-'*35)
print(f'{"Menu de opções":^35}') 
print('-'*35)
print('1 - Cadastrar produtos')
print('2 - Visualizar todos os dados')
print('3 - Sair')
print('-'*35)
while True:
  menu = int(input('Digite um valor: '))
  if menu == 1:
    arquivo = open('prod.txt','a')
    print('-'*35)
    print(f'{"Cadastro":^35}')
    print('-'*35)
    for c in range(4):
      t = prod()
      t.nome = input('Descreva o produto: ')
      t.codigo = int(input('Cadastre o código do produto: '))
      t.preco = float(input('Informe o preço: '))
      arquivo.write(f'{t.nome}_{t.codigo}_{t.preco:.2f}\n')
    arquivo.close()
  elif menu == 2:
    arquivo = open('prod.txt','r')
    print('-'*35)
    print(f'{"Produtos":^35}')
    print(f'{"Nome":<15}{"Código":^10}{"Preço":>10}')
    print('-'*35)
    for c in arquivo.readlines():
      nome,cod,preco = c.strip().split("_") 
      print(f'{nome:.<15}{cod:.^10}{preco:.>10}')
    arquivo.close()
  else:
    print('até breve!')
    break
