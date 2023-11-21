numeros = []
pares = []
impares = []

for i in range(1, 21):
    numero = int(input('Digite um número: '))
    numeros.append(numero)
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print('A lista de números pares é igual a ', pares)
print('A lista de números ímpares é igual a ', impares)