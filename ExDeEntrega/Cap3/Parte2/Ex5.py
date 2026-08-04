pessoas = []
n = int(input('insira o numero de pessoas a serem add'))

for c in range ( 0 ,n) :
  nome = input ('nome : ')
  idade= int(input('idade : '))
  sexo = input('sexo(M ou H) : ')
  lista_nome = f"pessoa_{c}"

  lista_nome = {'nome':nome,'idade':idade,'sexo':sexo}
  pessoas.append(lista_nome)

num_mulheres=0
soma_idade=0
for c in range (0,n) :
  soma_idade = soma_idade + pessoas[c]['idade']
  if pessoas[c]['idade']<20 and pessoas[c]['sexo'] =='M' :
     num_mulheres += 1

print('media idade' , soma_idade/n)
print('mulheres com idade<20 ',num_mulheres)
