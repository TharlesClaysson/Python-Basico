class alunos:
  matri = 0
  nome = ''
  tel = ''


def cadastrar():
  arquivo = open('produtos.txt','w')
  print('-'*40)
  print(f'{"Cadastro":^35}')
  print('-'*40)
  for c in range(4):
    t = produtos()
    t.nome = input('Nome do aluno: ')
    t.matri = int(input('Matrícula do aluno: '))
    t.tel = input('Telefone do aluno: ')
    arquivo.write(f'{t.nome}_{t.matri}_{t.tel}\n')
  arquivo.close()

def visualizar():
  arquivo = open('produtos.txt','r')
  print('-'*40)
  print(f'{"Produtos":^35}')
  print(f'{"Nome":<15}{"Matrícula":^10}{"Telefone":>15}')
  print('-'*40)
  for c in arquivo.readlines():
    nome,mat,tel = c.strip().split("_") 
    print(f'{nome:.<15}{mat:.^10}{tel:.>15}')
  arquivo.close()


def main():
  print('-'*35)
  print(f'{"Menu de opções":^35}') 
  print('-'*35)
  print('1 - Cadastrar alunos')
  print('2 - Visualizar alunos')
  print('3 - Sair')
  print('-'*35)
  while True:
      menu = int(input('Digite um valor: '))
      if menu == 1:
        cadastrar()
      elif menu == 2:
        visualizar()
      else:
        print('até breve!')
        break

main()
