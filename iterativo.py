def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Calcular el factorial de 5
print(factorial(5))