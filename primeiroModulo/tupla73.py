brasileirao = ('Atlético-MG','Internacional','Flamengo','São Paulo',
               'FLuminense','Santos','Palmeiras','Fortaleza','Sport Recife',
               'Vasco da Gama','Ceará SC','Atlético-GO','Botafogo','Grêmio',
               'Athlético-PR','Bahia','Corinthians','Coritiba','Bragantino-SP',
               'Goiás')
print('*'*30)
print(f'Os cinco primeiros colocados são: {brasileirao[1:6]}')
print('*'*30)
print(f'Os quatro ultimos colocados são: {brasileirao[-4:]}')
print('*'*30)
print(f'A lista dos times do brasileirão em ordem alfabética é: \n {sorted(brasileirao)}')
print('*'*30)
print(f'o Flamengo está na {brasileirao.index("Flamengo")+1}° posição')
