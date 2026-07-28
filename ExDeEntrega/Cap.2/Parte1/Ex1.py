Nome = input('Nome completo : ')
#padronizacao do nome para evitar erros de comparacao
Nome = Nome.upper()

print('Nome com letras maiusculas : ',Nome)
print('Nome com letras minusculas : ',Nome.lower())
print('Quantas letras tem em seu nome : ',len(Nome))
print('Trocando o ultimo nome por outra palavra : ',Nome.replace('ZANIN','do Inatel'))
