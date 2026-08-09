ordem_times = ['Barcelona','Atlético de Madrid','Osasuna','Elche','Alaves']
#letra A
print(' 3 primeiros times em ordem de colocacao')
print(ordem_times[0:3])
#letra B
print('Dois ultimos colocados')
print(ordem_times[3:])
#letra C
print('Times em ordem alfabetica')
print(sorted(ordem_times))
#letra D
print('A colocacao do Barcelona e : ',ordem_times.index('Barcelona')+1,'°')
