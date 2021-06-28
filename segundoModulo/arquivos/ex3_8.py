class telefone:
  ddd = 0
  fone = 0    


class alunos:
  mat = 0
  nome = ''
  tel = telefone()


def titulo(texto):
  print('-'*60)
  print(f'{texto:^60}')
  print('-'*60)

    
def visualizar():
  titulo('corpo discente:')
  arq = open('alunos.txt.','r')
  print(f'{"matrícula":<10}{"nome":<30}{"telefone":<20}')
  for c in arq.readlines():
    mat,nome,ddd,tel = c.strip().split('_')
    print(f'{mat:.<10}{nome:.<30}({ddd}){tel}')
  arq.close()


def cadastro():
  titulo('Cadastrar')
  arq = open('alunos.txt','w')
  for c in range(1):
    s = alunos()
    s.mat = int(input('Digite a sua matrícula: '))
    s.nome = input('Digite seu nome: ')[0:30].title()
    s.tel.ddd = int(input('Digite o seu ddd: '))
    s.tel.fone = int(input('Digite seu telefone: '))
    arq.write(f'{s.mat}_{s.nome}_{s.tel.ddd}_{s.tel.fone}\n')
  arq.close()
    

def main():
  titulo('Menu de opções digite:')
  print('"Cadastrar" para Cadastrar alunos ')
  print('"Visualizar" parar Visualizar todos os dados ')
  print('"Sair" para sair')
  while True:
    menu = input('Digite uma opção: ').lower()
    if menu == 'cadastrar':
      cadastro()
    elif menu == 'visualizar':
      visualizar()
    elif menu == 'sair':
      print('Até logo!')
      break
    else:
      print('Opção inválida!')

      
main()
