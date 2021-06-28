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
    n = int(input('Digite o número de conta: '))
    for i in range(len(txt)):
      while n == txt[i].num:
        print('\033[1;31mESTA CONTA JÁ EXISTE\033[0m')
        n = int(input('Digite outra: '))
    dados.num = n
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
  nada = 0
  estilo('PESQUISAR CLIENTES','\033[1;37;45m')
  while nada == 0:
    busca = input('Digite o nome do cliente: ').title()
    for c in range(len(txt)):
      if txt[c].nome.count(busca,0,len(busca)) >0:
        respostas(txt,c)
        nada += 1
    if nada == 0:
      print('\033[0;31maNÃO CONSTA NO SISTEMA!\033[0m')


def alterar(txt):
  controle = 0
  while controle == 0:
    busca = int(input('Digite o número da conta: '))
    for c in range(len(txt)):
      if txt[c].num == busca:
        controle += 1
        estilo('Alterar Dados','\033[1;37;40m')
        respostas(txt,c)
        print(f'{"Que campo deseja editar?":^100}')
        print(f'{"1-Nome":<25}{"2-Saldo":^25}{"3-Nome e Saldo":^25}{"4-Sair":>25}')
        alt = int(input('Digite a opção desejada: '))
        if alt < 4:
          if alt ==1:
            txt[c].nome = input('Digite o novo nome: ')
          elif alt == 2:
            txt[c].saldo = int(input('Digite o novo saldo: '))
          elif alt == 3:
            txt[c].nome = input('Digite o novo nome: ')
            txt[c].saldo = int(input('Digite o novo saldo: '))
          respostas0(txt,c)
          print('Dados alterados com sucesso!'^100)
        else:
          print('Voltando ao menu anterior')
    if controle == 0:
      print('\033[0;31m ESSA CONTA NÃO CONSTA NO SISTEMA!\033[0m')  


def respostas(txt,c):
  print(f'\033[47mConta:{txt[c].num:>50}{"":45}')
  print(f'Cliente:{txt[c].nome:.>48}{"":45}')
  print(f'Saldo:{txt[c].saldo:.>50.2f}{"":45}')
  print('\033[0m ')


def estilo(txt,s):
  print('-'*100)
  print(f'{s}{txt:^100}')
  print('\033[0m-'*100)


def excluir(txt):
  estilo('EXCLUIR A CONTA COM MENOR SALDO','\033[1;37;41m')
  menor = float('inf')
  for c in range(len(txt)):
    if txt[c].saldo < menor:
      menor = txt[c].saldo
      posicao = c
  txt.pop(posicao)
    

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
    elif menu == 2:
      mostrar(clientes)
    elif menu == 3:
      consulta(clientes)
    elif menu == 4:
      alterar(clientes)
    elif menu == 5:
      excluir(clientes)
    elif menu == 6:
      print('Até logo!')
    else:
      print(f'\033[1;31m{"COMANDO INVÁLIDO!":^100}')  
      menu = 0
    
  
main()
