def tabuada(N):
    for i in range(1,11):
        print(N,' x ',i,' = ',N*i)

def main():
    N = int(input('Informe um valor: '))
    tabuada(N)

main()
