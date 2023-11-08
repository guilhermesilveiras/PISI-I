notas = []

for i in range(4):
    nota = float(input('Digite uma nota: '))
    notas.append(nota)

notas.sort(reverse=True)
media = sum(notas[:4]) / len(notas[:4]) 
print("A média das quatro maiores notas é:", media, "e as quatro maiores notas são : ", notas[:4])