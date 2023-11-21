nomesMeses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')
temperaturas = []

for i in range(12):
    temperatura = float(input(f'Digite a temperatura do mês {nomesMeses[i]}: '))
    temperaturas.append(temperatura)

media = sum(temperaturas) / len(temperaturas)
print(f"A média anual das temperaturas é {media}.")

for i in range(12):
    if temperaturas[i] > media:
        print(f"{nomesMeses[i]} — {temperaturas[i]}")

