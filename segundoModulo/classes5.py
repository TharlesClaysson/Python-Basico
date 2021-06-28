class info:
  num = 0
  nome = ''
  saldo = 0


def cadastro(txt):
  print(f'{"Espaço disponível no sistema:":>76} {15 - len(txt):<23}')
  quant = int(input(f'{"Quantos clientes deseja cadastrar ? ":>77}'))  
  while len(txt) + quant > 15:
    print(f'\033[1;31m{"VOCÊ SÓ PODE CADASTRAR ":>64}{15 - len(txt):<2}{" CLIENTES!":<34}')
    print('\033[0;32;47m ',end='')
    quant = int(input(f'{"Quantos clientes deseja cadastrar ? ":>76}'))
  estilo('CADASTRAR CLIENTES','\033[1;37;44m')
  for c in range(quant):
    dados = info()
    print('')
    dados.num = int(input('Digite o número da conta: '))
    dados.nome = input('Digite o nome do cliente: ').title()
    dados.saldo = float(input('Digite o valor depositado R$: '))
    txt.append(dados)
  print('\033[3;34mDADOS CADASTRADOS COM SUCESSO!')
  print('\033[0m ')


def mostrar(txt):
  estilo('RELAÇÃO DE CLIENTES','\033[1;37;42m')
  for c in range(len(txt)):
    respostas(txt,c)


def consulta(txt):
  busca = input('Digite o nome do cliente: ').title()
  nada = 0
  estilo('PESQUISAR CLIENTES','\033[1;37;45m')
  for c in range(len(txt)):
    if txt[c].nome.count(busca,0,len(busca)) >0:
        respostas(txt,c)
        nada += 1
  if nada == 0:
      print('\033[0;31mNÃO CONSTA NO SISTEMA!')


def respostas(txt,c):
  print(f'\033[47mConta:{txt[c].num:>50}{"":45}')
  print(f'Cliente:{txt[c].nome:.>48}{"":45}')
  print(f'Saldo:{txt[c].saldo:.>50.2f}{"":45}')
  print('\033[0m ')


def estilo(txt,s):
  print('-'*100)
  print(f'{s}{txt:^100}')
  print('\033[0m-'*100)


def main():
  estilo('BANCO DO BRASIL','\033[1;43m')
  clientes = []
  menu = 1
  while 0 <= menu <= 5:
    print(f'\033[1;3;4m{"Menu de Opções:":^100}')
    print(f'\033[0;31;47m{"1- CADASTRAR CONTAS":<33}{"2- VISUALIZAR TODAS AS CONTAS":^33}{"3- CONSULTAR POR NOME":>34}')
    print(f'{"4- ALTERAR NOME OU SALDO PELO NÚMERO DA CONTA":<50}{"5- EXCLUIR A CONTA COM MENOR SALDO":>50}')
    print(f'{"6- SAIR":^100}')
    print('\033[32m',end='')
    menu = int(input(f'{"Digite uma opção:":>77} '))
    print('-'*100)
    if menu == 1: 
      if len(clientes) >= 15:
        print(f'\033[1;31m{"!O SISTEMA NÃO SUPORTA MAIS CLIENTES!":^100}')
      else: 
        cadastro(clientes)
    if menu == 2:
      mostrar(clientes)
    if menu == 3:
      consulta(clientes)
    menu = 0
    
  
main()
