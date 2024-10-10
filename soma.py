def calcular_media(lista):
    soma = 0
    for num in lista:
        soma += num
    return soma / len(lista)

n = int(input("\nquantos números você deseja inserir? "))

numeros = []

for i in range(1, n + 1):
    num = int(input(f"Digite o {i}º número: "))
    numeros.append(num)

if len(numeros) > 0:
    print(f"\na média dos números é: {calcular_media(numeros):.2f}")
else:
    print("\nnenhum número foi digitado.")

print("\n")