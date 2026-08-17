import numpy as np 
#numpy nao trabalha com elementos heterogeneos

#Slice no Numpy
#plantando a mesma semente aleatoria
np.random.seed(10)
#estruturando a matriz 3 x 3
mtz = np.random.randint(1,99,9).reshape(3,3)
print(mtz)
print('extraindo apenas a segunda linha da matriz')
print(mtz[1])
print('extraindo a terceira coluna da matriz')
print(mtz[:,2])
print('extraindo a matriz 2x2 no canto inferior direito da matriz')
print(mtz[1:,1:])

#condicionais no Numpy
print('mostre apenas os elementos menores que setenta')
print(mtz<70)
print(mtz[mtz<70])
print('dessa matriz retorne apenas os numeros pares')
print(mtz%2==0)
print(mtz[mtz%2==0])

  
