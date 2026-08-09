loja_one = {'Galaxy A37','Galaxy A17','Galaxy A16','Galaxy S26','Galaxy S25'}
loja_two = {'Galaxy A37','Galaxy A17','Galaxy A16','Galaxy Z Fold'}

#mostra os modelos da loja
print("modelos da loja A : ",loja_one)
print("modelos da loja B : ",loja_two)
#numero de modelos distintos
print('total de modelos disponiveis : ',len(loja_one |loja_two))
#modelos em ambas lojas
modelos_semelhantes = loja_one & loja_two
print('modelos semelhantes : ',modelos_semelhantes)
