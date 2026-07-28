import math
Numero = float(input('Inserir numero decimal : '))

print('Raiz quadrada do numero ',Numero**(0.5))
print('Arredondamento teto : ',math.ceil(Numero))
print('Arredondamento chao : ',math.floor(Numero))
print('Truncamento para inteiro : ',math.trunc(Numero))
