
distancia = float(input('Digite a distância em km: '))
tempo = float(input('Digite o tempo em horas para realizar a viagem: '))

while distancia <= 0 or tempo <= 0:
    print('Erro! Digite valores maiores que zero!')
    distancia = float(input('Digite a velocidade em km/h: '))
    tempo = float(input('Digite o tempo em horas para realizar a viagem: '))

velocidade = distancia / tempo

if velocidade > 110:
    print('Você ultrapassou o limite máximo de 110km/h.')
else:
    print('Parabéns, você respeitou o limite de velocidade de 110km/h.')

print('A velocidade média foi de {:.2f}km/h'.format(velocidade))

# Crie novas linhas de código para adicionar ao final do programa par acalcular a quantidade de combustível (em litros) consumida pelo veículo e exiba esta quantidade na tela.
# Obs: considere que o veículo percorre 8km por litro (km/l) se a velocidade média for menor ou igual a 60 km/h; ou percorre 14 km/l se a velocidade média estiver entre 60 e 90 km/h;
# ou percorre 10km/l se a velocidade média for igual ou acima de 90 km/h.

if velocidade <= 60: 
    combustivel = distancia / 8
elif velocidade > 60 and velocidade <= 90:
    combustivel = distancia / 14
elif velocidade > 90:
    combustivel = distancia / 10

print(f'A quantidade de combustível consumida foi de {combustivel:.2f} litros')