arquivo = open('numeros.txt', 'w') # apagando e criando
for linha in range(100,201):
    arquivo.write('%f\n' % linha)
arquivo.close()
