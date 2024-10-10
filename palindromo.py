def verificar_palindromo(palavra):
    palavra = palavra.lower().replace(" ", "")
    return palavra == palavra[::-1]

palavra = input("\ndigite uma palavra: ")
if verificar_palindromo(palavra):
    print(f"{palavra} é um palíndromo.\n")
else:
    print(f"{palavra} não é um palíndromo.\n")
