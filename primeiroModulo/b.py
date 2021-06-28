linhas = int(input('Quantas linhas vai querer?: '))
colunas = int(input('quantas colunas vai querer?: '))
m = []
for l in range(linhas):
    ln = 0
    for c in  range(colunas):
        t = int(input(f'qual o valor de [{l},{c}]?: '))
        ln += t
    m.append(ln)
for lin in range(linhas):
    print(m[lin],end='\n')
print()
