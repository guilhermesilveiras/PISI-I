

n = int(input('Digite o valor de M: '))

# Crie uma matriz vazia
matriz = []

for l in range(n):
    # Crie uma linha vazia
    linha = []
    for c in range(n):
        numero = int(input('Digite o número que ficará armazenado {}, {}: '.format(l, c)))
        # Adicione o número à linha
        linha.append(numero)
    # Adicione a linha à matriz
    matriz.append(linha)

print(matriz)
