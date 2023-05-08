def fibonacci(n):
    if n < 0:
        raise ValueError("n tem que ser maior do que zero")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

n = int(input('Digite um número inteiro: '))
if n < 0:
    print(ValueError)
else:
    print(f'fibonacci({n}) = {fibonacci(n)}')