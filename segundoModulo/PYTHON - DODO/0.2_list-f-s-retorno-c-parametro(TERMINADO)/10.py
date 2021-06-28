def verifiA(QdeA):
    contador = QdeA.count('a')
    contador2 = QdeA.count('A')
    print('A quantidade de letra A(s) da frase é ',contador + contador2)

def main():
    print('Verificador de quantidade de A(s) a frase tem')
    QdeA = input('Escreva uma frase: ')
    verifiA(QdeA)

main()
