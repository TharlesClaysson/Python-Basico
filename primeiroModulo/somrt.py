def somar(*num):
    s = 0
    for valor in num:
        s += valor
    print(f'A soma de {num} é {s} ')
    return s


r1 = somar(3,2,5)
r2 = somar(2,2)
r3 = somar(6)
print(f'os valores foram {r1}, {r2}, {r3} ')

