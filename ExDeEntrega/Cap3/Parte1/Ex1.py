ordem_times = ['Barcelona','Atlético de Madrid','Osasuna','Elche','Alaves']

#letra A
print(' 2 primeiros times em ordem de colocacao')
for c in range (0,2) :
  print(ordem_times[c])
#letra B
print('Dois ultimos colocados')
for c in range (3,5) :
  print(ordem_times[c])
#letra C
print('Times em ordem alfabetica')
print(sorted(ordem_times))
#letra D
print('A colocacao do Barcelona e : ',ordem_times.index('Barcelona')+1,'°')
