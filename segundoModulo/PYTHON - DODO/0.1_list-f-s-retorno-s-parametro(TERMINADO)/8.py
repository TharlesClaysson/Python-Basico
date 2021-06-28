def inTermJogo():
    hi = int(input('hora inicial do jogo: '))
    mi = int(input('minuto inicial do jogo: '))
    hf = int(input('hora final do jogo: '))
    mf = int(input('minuto final do jogo: '))
    if hi < hf:
        if mi > mf:
            hj = hf - 1 - hi
            mj = mf + 60 - mi
        else:
            hj = hf - hi
            mj = mf - mi
    elif hi > hf:
        if mi > mf:
            hj = hf + 23 - hi
            mj = mf + 60 - mi
        else:
            hj = hf + 24 - hi
            mj = mf - mi
    else:
        if mi > mf:
            hj = hf + 23 - hi
            mj = mf + 60 - mi
        else:
            hj = hf - hi
            mj = mf - mi
    print('tempo de jogo: ',hj,'hr',mj,'min')
def main():
    inTermJogo()

main()
