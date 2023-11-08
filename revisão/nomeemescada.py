nome = input('Digite seu nome: ')

for letra in nome:
    print(letra)

for i in range (len(nome)):
    print(nome[:i+1])