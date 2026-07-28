Nome = input('Nome completo : ')

print('Nome com letras maiusculas : ',Nome.upper())
print('Nome com letras minusculas : ',Nome.lower())

#for each que varre a str buscando espacos para marcar o inicio da ultima parte do nome e a quantidade de espacos em branco
Tamanho = len(Nome)
MarcadorInicio = 0 ;
Vazio = 0 ;
for C in range (0 ,Tamanho) :
    if Nome[C] == ' ' :
       MarcadorInicio  = C
       Vazio += 1

Tamanho -= Vazio
print('Quantas letras tem em seu nome : ',Tamanho)

if MarcadorInicio!=0 :
   Nome = Nome[:MarcadorInicio] + ' do Inatel'
else :
   Nome = Nome + ' do Inatel'

print('Trocando o ultimo nome por outra palavra : ',Nome)

