pessoa1={'nome':'leo' ,'peso':70}
pessoa2={'nome':'andrey' ,'peso':60}
pessoa3={'nome':'lucas' , 'peso':72}

pessoas = [pessoa1, pessoa2 ,pessoa3]

max_peso = pessoas[0]['peso']
min_peso = max_peso

for c in range ( 0 , len(pessoas)) :
   if pessoas[c]['peso'] > max_peso :
      max_peso = pessoas[c]['peso']
      max_peso_nome = pessoas[c]['nome']
   if pessoas[c]['peso'] <min_peso :
      min_peso = pessoas[c]['peso']
      min_peso_nome = pessoas[c]['nome']

print('Mais pesada : ' , max_peso_nome)
print('Menos pesada : ',min_peso_nome)      
