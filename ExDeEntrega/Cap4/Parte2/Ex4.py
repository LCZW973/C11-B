import numpy as np 

mtz = np.arange(0,4,1)
mtz = mtz.reshape(2,2)


linha,coluna = mtz.shape

total = linha*coluna

if(total%2 == 0) :
    print('par')
else :
    print('impar')
