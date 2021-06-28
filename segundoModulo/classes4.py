class informacoes:
  nome =''
  dia = 0
  mes = 0
  ano = 0
  ddd = 0
  tel = 0
  rua =''
  num = 0
  cidade =''
  estado =''
  serie = 0


def enfeite(texto,estilos=''):
  print('-'*100)
  print(f'{estilos}{texto:^100}')
  print(f'{"-"*30}{"_"*40}{"-"*30}')


def cadastro(integ):
  print(' '*100)
  print(f'Vagas disponíveis : {500 - len(integ):}')
  quantidade = int(input(f'{"Quantos alunos deseja cadastrar? ":<30}'))
  b = quantidade + len(integ)
  if b > 500:
    print(f'\033[1;31;47mSÓ TEMOS : {500 - len(integ)} {"VAGAS!":<80}')
  else: 
    for c in range(len(integ),b):
      enfeite('Informações do aluno:','\033[1;37;45m')
      info = informacoes()
      print('\033[0;35;47m '*100)
      info.nome = input(f'Nome completo: ').title()
      enfeite('Data de nascimento:')
      print('\033[0;35;47m '*100)
      info.dia = int(input('Dia: '))
      info.mes = int(input('Mês: '))
      info.ano = int(input('Ano: '))
      enfeite('Telefone:')
      print('\033[0;35;47m '*100)
      info.ddd = int(input('DDD: '))
      info.tel = int(input('Número: '))
      enfeite('Endereço:')
      print('\033[0;35;47m '*100)
      info.rua = input('Rua: ').title()
      info.num = int(input('nº: '))
      info.cidade = input('Cidade: ').title()
      info.estado = input('Estado: ').upper()
      info.serie = int(input('Série: '))
      integ.append(info)    


def pesquisa(busca):
  buscar = input('Nome: ').title()
  nada = 0
  enfeite('Resultado da busca!','\033[1;37;44m')
  for i in range(len(busca)):
    if busca[i].nome.count(buscar,0,len(buscar) > 0:
      print('\033[0;34;47m '*100)
      interface(busca,i)
      nada += 1
  if nada == 0:
    print('\033[0;34;47m '*100)
    print(f'Aluno: {buscar} não está matriculado')


def docentes(respostas):
  enfeite('Corpo Docente:','\033[1;37;46m')
  for c in range(len(respostas)):
    print('\033[0;36;47m'*100)
    interface(respostas,c)


def interface(saidas,c):    
    print(f'Aluno: {saidas[c].nome:<43}Série: {saidas[c].serie:>2}{"Ano":<41}')
    print(f'Data de nascimento: {saidas[c].dia:>2}/{saidas[c].mes:>2}/{saidas[c].ano:<10}',end='')
    print(f'Telefone: ({saidas[c].ddd:2}){saidas[c].tel:<50}')
    print(f'{"Endereço:":<100}')
    print(f'Rua: {saidas[c].rua:<45}nº: {saidas[c].num:<46}')
    print(f'Cidade: {saidas[c].cidade:<42}Estado: {saidas[c].estado:<42}')


def main():
  integrantes = []
  start = 1
  while 0<=start<=3:
    enfeite('Fatec Presidente Prudente SP.','\033[1;37;40m')
    print(f'\033[4;3;30;47m{"Menu de opções:":^100}')
    print(f'\033[0;32;47m{"1- Cadastrar alunos":^26}{"2- Consulta por nome":^25}',end='')
    print(f'{"3- Visualizar todos os dados":^29}{"4- Sair":^20}')
    print('\033[0;32;47m '*100)
    print('\033[0;34;47m ',end='')
    start = int(input(f'{"Digite a opção desejada: ":^50}'))
    if start == 1:
      if len(integrantes) == 500:
        print(f'\033[1;31;47m{"NÃO HÁ VAGAS!":^100}')
      else:            
        cadastro(integrantes)
    elif start == 2:
      pesquisa(integrantes)
    elif start == 3:
      docentes(integrantes)
    elif start == 4:
      print(f'\033[0;32;47m{"Sessão encerrada!":^100}')
    elif 1 > start or start> 4:
      print(f'\033[1;31;47m{"COMANDO INVÁLIDO !":^100}')
      start = 0
  print('\033[1;37;40m-'*100)


main()
