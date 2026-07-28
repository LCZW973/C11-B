while True :
  Numero = int(input('Insira um valor entre 1000 e 9999 : '))
  if Numero > 1000 and Numero < 9999 :
     break ; 
  print('O numero inserido esta no intervalo errado')

print('O numero da unidade : ',Numero%10)  
print('O numero da dezena : ',(Numero%100-Numero%10)//10)
print('O numero da centena : ',(Numero%1000-Numero%100)//100)
print('O numero do milhar',(Numero%10000-Numero%1000)//1000)
