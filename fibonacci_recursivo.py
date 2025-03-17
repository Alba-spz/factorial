def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Ejemplo de uso
n = 10
print(f"El número de Fibonacci para {n} es {fibonacci(n)}")