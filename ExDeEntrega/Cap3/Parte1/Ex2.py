loja_one = {'Galaxy A37','Galaxy A17','Galaxy A16','Galaxy S26','Galaxy S25'}
loja_two = {'Galaxy A37','Galaxy A17','Galaxy A16','Galaxy Z Fold'}

print('modelos da loja A')
for c in loja_one :
  print(c)

print('modelos da loja B')
for c in loja_two :
  print(c)

modelos_disponiveis = loja_two | loja_one
print('Total de modelos disponiveis : ',len(modelos_disponiveis))

modelos_semelhantes = loja_one & loja_two
print('Modelo disponiveis nas duas lojas : ')
for c in modelos_semelhantes :
  print(c)
