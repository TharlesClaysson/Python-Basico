def conversao():
    segundos = int(input('Informe um valor representado em segundos: '))
    h = segundos // 3600
    m = segundos%3600 // 60
    s = segundos%3600 %60 // 1
    print('Horas: ',h,' minutos: ',m,' segundos: ',s)
def main():
    conversao()

main()

