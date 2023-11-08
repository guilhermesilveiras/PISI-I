idades = []

for i in range(5):
    idade = int(input('Digite uma idade: '))
    idades.append(idade)

print("A maior idade é: ", max(idades), "e a menor idade é: ", min(idades))