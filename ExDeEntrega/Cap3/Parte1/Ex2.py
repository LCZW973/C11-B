loja_one = {'Galaxy A37','Galaxy A17','Galaxy A16','Galaxy S26','Galaxy S25'}
loja_two = {'Galaxy A37','Galaxy A17','Galaxy A16','Galaxy Z Fold'}

print('modelos da loja A')
for c in loja_one :
  print(c)

print('modelos da loja B')
for c in loja_two :
  print(c)

print('total de modelos disponiveis : ',len(loja_one|loja_two))

modelos_semelhantes = loja_one & loja_two

print('modelos semelhantes : ')
for c in modelos_semelhantes :
      print(c)
      
