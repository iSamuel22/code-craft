n = int(input('\ndigite um valor: '))

fat = 1

if n == 0:
    fat = 1
else:
    for i in range(1, n + 1):
        fat *= i

if n != 0:
    for i in range(n, 0, -1):
        if i == 1:
            print(f'{i} = {fat}')
        else:
            print(f'{i} x ', end='')

print('\n')