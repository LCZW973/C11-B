pessoas=[]

for c in range (0 , 3) :
  cria_pessoas = f"pessoa{c}"
  nome = input("nome : ")
  peso = float(input("peso : "))
  cria_pessoas ={"nome":nome,"peso":peso}
  pessoas.append(cria_pessoas)

max_peso = pessoas[0].copy()
min_peso = max_peso.copy()

for c in range ( 0 , len(pessoas)) :
   if pessoas[c]['peso'] > max_peso['peso'] :
      max_peso['peso'] = pessoas[c]['peso']
      max_peso['nome'] = pessoas[c]['nome']
   if pessoas[c]['peso'] <min_peso['peso'] :
      min_peso['peso'] = pessoas[c]['peso']
      min_peso['nome'] = pessoas[c]['nome']

print('Mais pesada : ' , max_peso['nome'])
print('Menos pesada : ',min_peso['nome'])      
 
