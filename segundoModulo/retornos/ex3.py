def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


def main():
    num = int(input(' Digite um número: '))
    '''print(par(num))'''
    if par(num):
        print(num,'é par')
    else:
        print(num,'é impar')


main()
