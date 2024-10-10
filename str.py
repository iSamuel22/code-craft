print('---------------------------------')
palavra = input('digite uma frase: ')
print('---------------------------------')

print('maiuscula:', palavra.upper())
print('minuscula:', palavra.lower())

cont = 0
vogais = 0
for i in palavra:
    if i != ' ':
        cont += 1
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
            vogais += 1
        else:
            vogais += 0
    else:
        cont += 0

print('qtd. letras:', cont)
print('qtd. vogais:', vogais)
print('---------------------------------')