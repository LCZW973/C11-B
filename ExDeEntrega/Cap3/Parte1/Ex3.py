nome = input('nome')
media = float(input('media'))

aluno = {'nome':nome,'media':media}
if aluno['media'] >= 50 :
   aluno ['estado'] ='AP'
else :
   aluno['estado'] = 'RP'

for c in aluno :
  print(c,' : ',aluno[c])
