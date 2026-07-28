numero_selecionado = int(input('Numero selecionada para tabuada : '))
intervalo_inicial = int(input('Intervalo inicial : '))
intervalo_final = int(input('Intervalo final : '))
intervalo_final += 1
for c in range(intervalo_inicial,intervalo_final):
    print(c*numero_selecionado)
