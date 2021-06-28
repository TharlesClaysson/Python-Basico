produtos = ('Lápis',1.75,'Borracha',2.00,'Caderno',15.90,
            'Estojo',25.00,'Transferidor',4.20,'Compasso',9.99,
            'Mochila',120.32,'Canetas',22.30,'Livro',34.90)
print('-'*40)
print(f'{"Lista de produtos":^40}')
print('-'*40)
for tabela in range(0,len(produtos)):
    if tabela % 2 == 0:
        print(f'{produtos[tabela]:.<30}',end='')
    else:
         print(f'R$:{produtos[tabela]:>7.2f}')
print('-'*40)
