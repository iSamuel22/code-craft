import random
import string

def gerar_senha(tamanho = 12, usar_simbolos = True):
    caracteres = string.ascii_letters + string.digits
    if usar_simbolos:
        caracteres += string.punctuation

    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

tamanho = int(input("\ndigite o tamanho da senha: "))
usar_simbolos = input("\ndeseja incluir símbolos? (s/n): ").lower() == 's'

senha_gerada = gerar_senha(tamanho, usar_simbolos)
print(f"\nsua senha gerada é: {senha_gerada}\n")
