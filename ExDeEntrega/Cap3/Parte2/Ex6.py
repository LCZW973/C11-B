lista_ing = ['polvilho','acucar','leite']

lista_ing.append('ovos')
lista_ing.insert(1,'chocolate') 

print("Elementos antes da remocao")
print(lista_ing)

lista_valor = [0,1,2,3,4]
dic_ing_valor = {
    'ingredientes':lista_ing,
    'preco':lista_valor
}

indice = dic_ing_valor['preco'].index(4)
lista_ing.pop(indice)
lista_valor.pop(indice) 

print('Elementos apos remocao por valor')
print(dic_ing_valor)
