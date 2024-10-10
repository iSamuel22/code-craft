import random 

print('-------------------')
print('JOGO DA ADIVINHAÇÃO')
print('-------------------')

number = random.randint(0, 100)
cont = 1
# print(number)

while(True):
    chute = int(input('\ndigita ai: '))

    if(chute == number):
        print('-------------------------')
        print('acertou na tentativa: ', cont)
        print('\n')
        break
        
    else:
        if(number > chute): 
            print('chutou baixo nengue')
            cont += 1
        else:
            print('chutou alto nengue')
            cont += 1