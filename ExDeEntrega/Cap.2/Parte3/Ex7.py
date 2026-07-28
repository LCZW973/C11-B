palavra = input("digite uma palavra : ")
palavra = palavra.upper()
contador = 0 
detectaA = 0

for c in range (0,len(palavra)) :
    if palavra[c] =='A' :
       contador+=1
       detectaA+=1
    if palavra[c]=='E' :
       contador+=1
    if palavra[c]=='I' :
       contador+=1
    if palavra[c]=='O' :
       contador+=1
    if palavra[c]=='U' :
       contador+=1

print('O numero de vogais sao : ',contador)
print('O numero de letras A sao : ',detectaA)

