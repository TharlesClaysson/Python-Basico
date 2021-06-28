def som():
  r = 0
  for c in range(1,2): 
    n = int(input(f'Digite o {c}° numero par: '))
    s = n % 2
    if s > 0:
      while s > 0:
        print('Tem que ser par')
    else:
      r = n+1
print()
def main():
  pos()

main()      
