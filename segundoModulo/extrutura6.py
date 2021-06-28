class cad:
  cod_serv = 0
  descri = ''

class serv:
  num_serv = 0
  valor = 0
  cod_cliente = 0
  cod = 0

def  cadastro_serv(servicos):
  for c in range(4):
    a = cad()
    a.descri = input('Descreva o serviço: ')
    a.cod_serv = int(input('Digite o código do serviço: '))
    servicos.append(a)


def mostrar(servicos):
  print('-'*100)
  print(f'{"tipo de serviço":<25}{"código do serviço":>25}')
  print('-'*100)
  for i in range(0,4):
    print(f'{servicos[i].descri:.<25}{servicos[i].cod_serv:.>25}')
 

def preparando_matriz(prestacoes):
  for c in range(0,30):
    prestacoes.append([])


def fazer_serv(prestacoes,servicos):
  while True:
    dia = int(input('Digite o dia que receberá os serviços: '))-1
    if dia >=30:
      print('Só armazeno 30 dias!')
      True
    elif dia < 0:
      print('Tá doidão Zé! Inventou a máquina do tempo!')
      True
    else:
      if len(prestacoes[dia]) == 3:
        print('Este dia não suporta mais serviços!')
        True
      else:
        while True:
          print(dia+1)
          dados = serv()
          dados.num_serv = int(input('Digite o número do serviço: '))
          dados.valor = float(input('Digite o valor do serviço R$: '))
          dados.cod_cliente = int(input('Digite o código do cliente: '))
          while True:
            control = 0
            dados.code = int(input('Digite o código do serviço prestado: '))
            for c in range(4):
              if dados.code == servicos[c].cod_serv: 
                prestacoes[dia].insert(0,dados) 
                print(servicos[c].descri)
                control += 1
            if control == 0:
              print('Código inválido!')
              True 
            else:
              break
          if len(prestacoes[dia]) < 3:   
            rec = input('Quer cadastrar mais um serviço neste dia?(s/n) ').upper()
            if rec == 'S':
              True
            else:
              break
          else:
            break
      denovo = input('Quer cadastrar mais um serviço em outro dia?(s/n) ').upper()
      if denovo == 'S':
        True
      else:
        break


def todos_serv(prestacoes,servicos):
  for c in range(30):
    if len(prestacoes[c]) >=1:
      print('-'*100)
      print(f'Dia {c+1}')
      print(f'{"Nº do serviço":<20}{"Valor do serviço R$":<20}{"Código do serviço":>20}{"Descrição":>20}{"Código do cliente":>20}')
      print('-'*100)
      for i in range(len(prestacoes[c])):
        print(f'{prestacoes[c][i].num_serv:.<20}{prestacoes[c][i].valor:.<20}{prestacoes[c][i].code:.>20}',end='')
        for d in range(4):
            if prestacoes[c][i].code == servicos[d].cod_serv:  
              print(f'{servicos[d].descri:.>20}',end='')
        print(f'{prestacoes[c][i].cod_cliente:.>20}')


def mostrar_serv_dia(prestacoes,servicos):
  while True:
    dia = int(input('Digite o dia: '))
    if dia > 30:
      print('Só armazeno 30 dias!')
      True
    elif dia <= 0:
      print('Tá doidão Zé! Inventou a máquina do tempo!')
      True
    else:
      c = dia - 1
      print(f'Dia {c+1}')
      print(f'{"Nº do serviço":<20}{"Valor do serviço R$":<20}{"Código do serviço":>20}{"Descrição":>20}{"Código do cliente":>20}')
      print('-'*100)
      if len(prestacoes[c]) >=1:
        for i in range(len(prestacoes[c])):
          print(f'{prestacoes[c][i].num_serv:.<20}{prestacoes[c][i].valor:.<20}{prestacoes[c][i].code:.>20}',end='')
          for d in range(4):
              if prestacoes[c][i].code == servicos[d].cod_serv:  
                print(f'{servicos[d].descri:.>20}',end='')
          print(f'{prestacoes[c][i].cod_cliente:.>20}')
      else:
        print('Não foram feitas operações neste dia!')
      break


def Mostrar_por_valor(prestacoes,servicos):
  min = float(input('Digite o valor mínimo da busca: '))
  max = float(input('Digite o valor máximo da busca: '))
  aj = 0
  z = -1
  for c in range(len(prestacoes)):
    for i in range(len(prestacoes[c])):
      if min <= prestacoes[c][i].valor <= max:
        if z < c:
          print('-'*100)
          print(f'Dia {c+1}')
          print(f'{"Nº do serviço":<20}{"Valor do serviço R$":<20}{"Código do serviço":>20}{"Descrição":>20}{"Código do cliente":>20}')
        print('-'*100)
        print(f'{prestacoes[c][i].num_serv:.<20}{prestacoes[c][i].valor:.<20}{prestacoes[c][i].code:.>20}',end='')
        for d in range(4):
            if prestacoes[c][i].code == servicos[d].cod_serv:  
              print(f'{servicos[d].descri:.>20}',end='')
        print(f'{prestacoes[c][i].cod_cliente:.>20}')
        z = c  
        aj +=1
  if aj == 0:
    print('Não foram encontrados serviços dentro destes valores!')


def relatorio_geral(prestacoes,servicos):
    for c in range(len(prestacoes)):
      print('-'*100)
      print(f'Dia {c+1}')
      print(f'{"Nº do serviço":<20}{"Valor do serviço R$":<20}{"Código do serviço":>20}{"Descrição":>20}{"Código do cliente":>20}')
      print('-'*100)
      if len(prestacoes[c]) >= 1:
        for i in range(len(prestacoes[c])):  
          print(f'{prestacoes[c][i].num_serv:.<20}{prestacoes[c][i].valor:.<20}{prestacoes[c][i].code:.>20}',end='')
          for d in range(4):
              if prestacoes[c][i].code == servicos[d].cod_serv:  
                print(f'{servicos[d].descri:.>20}',end='')
          print(f'{prestacoes[c][i].cod_cliente:.>20}')
      else:
        print('Não foram feitas operações neste dia!')


def main():
  servicos = []
  prestacoes = []
  preparando_matriz(prestacoes)
  menu = 0
  while 0 <= menu <= 7:
    print('-'*100)
    print(f'{"menu de opções":^100}')
    print('-'*100)
    print('1-Cadastrar os tipos de serviços')
    print('2-Mostrar todos os tipos de serviço')
    print('3-Cadastrar os serviços prestados')
    print('4-Mostrar todos os serviços prestados')
    print('5-Mostrar os serviços prestados em determinado dia')
    print('6-Mostrar os serviços prestados dentro de um intervalo de valor')
    print('7-Mostrar um relatório geral (separado por dia), que exiba, inclusive, a descrição do tipo do serviço')
    print('8-sair')
    menu = int(input('Digite uma opção: '))
    print('')
    if menu == 1:
      if len(servicos) == 4:
        print('Os serviços já foram cadastrados!')
        menu == 0
      else:
        cadastro_serv(servicos)
    elif menu == 2:
      mostrar(servicos)
    elif menu == 3:
      fazer_serv(prestacoes,servicos)       
    elif menu == 4:
      todos_serv(prestacoes,servicos)
    elif menu == 5:
      mostrar_serv_dia(prestacoes,servicos)
    elif menu == 6:
      Mostrar_por_valor(prestacoes,servicos)
    elif menu == 7:
      relatorio_geral(prestacoes,servicos)
    elif menu == 8:
      print('Até Breve!')
    else:
      print('Opção inválida!')
      menu = 0


main()
