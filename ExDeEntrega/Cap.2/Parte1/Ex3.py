while True:
  sexo = input("digite M (masculino) ou F (feminino) : ")
  sexo =sexo.upper()
  if sexo == 'M' or sexo == 'F' :
     break;

if sexo == 'M' :
   print('Homem')
else :
   print('Mulher')
