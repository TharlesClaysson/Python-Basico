def veriv(nome):
    if nome == 'Ana' or nome == 'ana':
        print('True')
    else:
        print('False')

def main():
    nome = input('Informe um nome para ser verificado: ')
    veriv(nome)

main()
