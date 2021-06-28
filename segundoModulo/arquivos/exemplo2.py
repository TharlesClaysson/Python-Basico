arquivo = open('numeros.txt', 'a') # append acrescente dados

for linha in range(341,621):
    arquivo.write('%d\n' % linha)
    
arquivo.close()

arquivo = open('numeros.txt', 'r') # lê os arquivos
for x in arquivo.readlines():
    print(x)
arquivo.close()
