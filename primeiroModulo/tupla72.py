ext = ('zero','um','dois','três','quatro','cinco','seis','sete',
       'oito','nove','dez','onze','doze','treze','quatorze',
       'quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
restart = 'S'
while restart == 'S':
#meu exemplo
    '''cont = int(input('DIgite um número de zero à vinte: '))
    while cont > 20 or cont < 0: 
        cont = int(input('Tem que ser entre 0 e 20 \n Tente de novo: '))
    print(f'Você digitou o número {ext[cont]}') '''  
# do Guanabara
    while True:
        cont = int(input('DIgite um número de zero à vinte: '))
        if 0 <= cont <= 20:
            break
        print('Tente novamente. ',end='')
    print(f'Você digitou o número {ext[cont]}')
#aqui cabe os dois exemplos    
    restart = input('Quer continuar? (S/N):').upper()
print('Até logo')
