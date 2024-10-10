def fibonacci(n):
    a, b = 0, 1
    sequencia = []
    for _ in range(n):
        sequencia.append(a)
        a, b = b, a + b
    return sequencia

print('\n')
print(fibonacci(10))
print('\n')