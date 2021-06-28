def contador(*num):
    '''tam = len(num)
    print(f'Recebi os valores {num} que são ao todo {tam} números')'''
    
    '''for valor in num:
        print(f'{valor} ',end='')
    print('Fim!') '''

    s = 0
    '''print('Somando ',end='')'''
    for valor in num:
        s += valor
        '''print(valor,'+ ',end='')
    print('0 =',s)'''
    print(f'Somando os valores {num} temos {s}')

contador(3,2,5)
contador(8,0)
contador(4,4,7,6,2)
