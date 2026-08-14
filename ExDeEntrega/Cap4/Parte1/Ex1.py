import numpy as np 

lista = np.ones([1,8])

listadois = np.random.randint(0,10,8)

listatres = lista+listadois
if(listatres.sum(axis=1)>=40) :
    listatres= listatres.reshape(4,2)
else :
    listatres= listatres.reshape(2,4)
    
print(listatres)
