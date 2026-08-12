import numpy as np 
np.random.seed(10)
mtz = np.random.randint(1,50,16)

mtz = mtz.reshape(4,4)

print(mtz)
media_coluna=mtz.sum(axis=0)/4
media_linha=mtz.sum(axis=1)/4

media_coluna = sorted(media_coluna)
print('maior media por coluna ',media_coluna[3])
media_linha = sorted(media_linha)
print('maior media por linha',media_linha[3])

Arr_unique,Arr_count = np.unique(mtz,return_counts = True)

print('Numero que aparecem e quantidade de vezes que aparecem : ')
for c in range(0,len(Arr_unique)):
    print(Arr_unique[c]," : " ,Arr_count[c])
    
print('Numero que aparecem 2 vezes : ')
for c in range(0,len(Arr_unique)):
    if Arr_count[c]>=2 :
     print(Arr_unique[c]," : " ,Arr_count[c])


