#como importar datasets no numpy
import Numpy as np
dataset = np.loadtxt('space.csv',delimiter = ';',dtype=str,encoding='utf-8')
print(dataset)

#extraindoa as colunas dos datasets
print(dataset[0,:])
#extraindo so os nomes das empresas
print(dataset[1:,1])
#extraindo so os nomes unicos
print(np.unique(dataset[1:,1]))
#extraindo os nomes unicos e mostrando quantas vezes cada empresa fez uma missao
print(np.unique(dataset[1:,1],return_count = True))
