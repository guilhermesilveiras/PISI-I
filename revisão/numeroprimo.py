# Faça um programa que identifica os 15 primeiros números primos (utilizando a instrução break).

# Define uma função para checar se um número é primo
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Encontrar os 15 primeiros números primos
qtd = 0
n = 2
while qtd < 15:
    if is_prime(n):
        print(n)
        qtd += 1
    n += 1