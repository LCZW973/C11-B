ordem_times = ['Barcelona','Atlético de Madrid','Osasuna','Elche','Alaves']

print(' 2 primeiros times em ordem de colocacao')
for c in range (0,2) :
  print(ordem_times[c])

print('Dois ultimos colocados')
for c in range (3,5) :
  print(ordem_times[c])

ordem_alfabetica = sorted(ordem_times)
print('Times em ordem alfabetica')
for c in range (0,5) :
  print(ordem_alfabetica[c])

for c in range (0,5) :
  if ordem_times[c] =='Barcelona' :
    print('A colocacao do Barcelona e : ',c+1)
