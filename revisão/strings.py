string1 = input('Digite uma string: ')
string2 = input('Digite outra string: ')

print('Você digitou ', string1, 'como primeira string, e o comprimento da primeira string é igual a : ', len(string1))
print('Você digitou ', string2, 'como segunda string, e o comprimento da segunda string é igual a : ', len(string2))

if len(string1) == len(string2):
    if string1 == string2:
        print('As strings tem o mesmo comprimento e conteúdo')
    else:
        print('As strings tem o mesmo comprimento, mas conteúdos diferentes')
else:
    print('As strings tem comprimentos diferentes e conteúdos diferentes')