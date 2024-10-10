def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

escolha = input("\nescolha a conversão (1: celsius para fahrenheit, 2: fahrenheit para celsius): ")

print('---------------------------------')

if escolha == '1':
    temperatura = float(input("\ndigite a temperatura em celsius: "))
    print(f"\n{temperatura}°C equivale a {celsius_para_fahrenheit(temperatura):.2f}°F\n")
elif escolha == '2':
    temperatura = float(input("\ndigite a temperatura em fahrenheit: "))
    print(f"\n{temperatura}°F equivale a {fahrenheit_para_celsius(temperatura):.2f}°C\n")
else:
    print("opção inválida, bro.\n")
