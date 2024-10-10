def soma(a, b):
    r = a + b
    return r

def subtracao(a, b):
    r = (a - b)
    return r

def multiplicacao(a, b):
    r = (a * b)
    return r

def divisao(a, b):
    r = (a / b)
    return r

print('---------------------------------')
valor1 = float(input('digite o primeiro valor: '))
valor2 = float(input('digite o segundo valor: '))
print('---------------------------------')

resultadoSoma = soma(valor1, valor2)
print('soma:', resultadoSoma)

resultadoSub = subtracao(valor1, valor2)
print('subtração:', resultadoSub)

resultadoMult = multiplicacao(valor1, valor2)
print('multiplicação:', resultadoMult)

if (valor2 != 0):
    resultadoDiv = divisao(valor1, valor2)
    print('divisão:', resultadoDiv)

print('---------------------------------')