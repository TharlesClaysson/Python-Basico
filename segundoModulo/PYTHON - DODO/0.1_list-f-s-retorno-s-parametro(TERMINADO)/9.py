def menorMaior():
    primeiro = int(input('Informe o Primeiro número: '))
    segundo  = int(input('Informe o Segundo número : '))
    terceiro = int(input('Informe o Terceiro número: '))
    quarto = int(input('Informe o Quarto número: '))
    quinto = int(input('Informe o quinto número: '))
    maior = primeiro
    if (segundo > maior):
        maior = segundo
    if (terceiro > maior):
        maior = terceiro
    if (quarto > maior):
        maior = quarto
    if (quinto > maior):
        maior = quinto
    print('Maior: ',maior)
    menor = primeiro
    if (segundo < menor):
        menor = segundo
    if (terceiro < menor):
        menor = terceiro
    if (quarto < menor):
        menor = quarto
    if (quinto < menor):
        menor = quinto
    print('Menor: ',menor)
def main():
    menorMaior()
    
main()
