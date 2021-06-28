linhas = int(input('Quantas linhas vai querer?: '))
colunas = int(input('quantas colunas vai querer?: '))
m = []
n = []
for l in range(linhas):
    ln = []
    lon = 0
    for c in  range(colunas):
        t = int(input(f'qual o valor de [{l},{c}]?: '))
        ln.append(t)
        lon += t
    m.append(ln)
    n.append(lon)
for lin in range(linhas):
    print(n[lin],end='\n')
for lin in range(linhas):
    for col in range(colunas):
        print(f'{m[lin][col]}*{n[lin]}',end='\t',)
    print()
