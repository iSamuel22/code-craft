def verificar_paridade(num):
    if num % 2 == 0:
        return f"{num} é par, bro.\n"
    else:
        return f"{num} é ímpar, bro.\n"

numero = int(input("\ndigite um número: "))
print(verificar_paridade(numero))
