while True :
  Distancia = int(input('Distancia em Km : '))
  if Distancia > 0 :
     break;

if Distancia<=200 :
   Preco = Distancia*0.5
if Distancia>=200 :   
   Preco = Distancia*0.45

print('O valor a ser pago sera : ' ,Preco)
