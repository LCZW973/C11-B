n = int(input("Insira a quantidade de produtos a serem cadastrados"))
lista_produtos = []

for c in range ( 0 , n ) :
  dic_produto = f"dic_produto{c}"
  nome = input("Insira o nome do produto")
  preco = float(input("Insira o preço do produto"))
  quant_estoque = int(input("Insira a quantidade em estoque do produto"))
  dic_produto = {
    "nome" : nome,
    "preco" : preco,
    "quant_estoque" : quant_estoque
  }
  lista_produtos.append(dic_produto)

for c in range (0,n) :
  print("nome :",lista_produtos[c]["nome"]," | valor total em estoque ",lista_produtos[c]["preco"]*lista_produtos[c]["quant_estoque"])


  

