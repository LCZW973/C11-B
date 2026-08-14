import numpy as np 

listaum = np.arange(0,51,2)
listadois = np.arange(100,49,-2)

listadois = sorted(listadois)
lista=np.concatenate([listaum,listadois])

print(lista)
