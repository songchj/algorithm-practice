def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n - 1)

for n in range(1, 6):
    print factorial(n)