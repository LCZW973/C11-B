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











