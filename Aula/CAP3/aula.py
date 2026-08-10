import numpy as np 

#criando numpy array 1d
arr = np.array([10,20,30,40,50,60])
print(arr)
print(type(arr))
#propriedades do array
print(arr.size)
print(arr.ndim)
print(arr.shape)


#criando numpy array 2d
mtz = np.array([[10,20],[30,40],[50,60]])
print (mtz)
#propriedades do array
print(mtz.size)
print(mtz.ndim)
print(mtz.shape)

#funcoes pre-prontas pra estruturar numpy_arrays
#ones
mtz = np.ones([5,5])
print (mtz)
#zeros
arr = np.zeros(10)
print(arr.reshape(5,2))
#arange
mtz = np.arange(2,21,2)
print(mtz.reshape(2,5))

#Operacoes entre numpy_arrays
arr1=np.array([10,20,30,40,50])
arr2=np.array([60,40,20,10,5])
arr3 = arr1+arr2
#Operacoes entre arrays
print(arr3)
print(arr1-arr2)
print(arr1*arr2)
#Concatenacao de arrays
arr3 = np.concatenate([arr1,arr2])
print(arr3)
#Broadcasting-quando um escalar faz uma operacao com um array
print(5*arr3)

#estruturando uma matriz com contas
mtz = np.arange(10,96,5)
mtz = mtz.reshape(3,6)
print(mtz)

#extraindo a soma da primeira coluna
print(mtz.sum(axis=0)[0])#eixo 0 = coluna
print(mtz.sum(axis=1)[1])#eixo 1 = coluna
























