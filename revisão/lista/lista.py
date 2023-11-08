notas = []

while True:
    nota = int(input('Digite uma nota: '))
    notas.append(nota)

    continuar = input('Deseja continuar? (S/N) ')
    if continuar.lower() == 'n':
        break

notas.sort(reverse=True)

quatro_maiores_notas = notas[:4]

media = sum(quatro_maiores_notas) / len(quatro_maiores_notas)

print("A média das quatro maiores notas é:", media, "e as quatro maiores notas são : ", quatro_maiores_notas)

x = len(notas)