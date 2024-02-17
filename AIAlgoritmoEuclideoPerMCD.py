def euclidean_algorithm(a, b):
    while b:
        a, b = b, a % b
    return a

# Esempio di utilizzo:
num1 = 18
num2 = 48

mcd = euclidean_algorithm(num1, num2)

print(f"Il MCD di {num1} e {num2} è {mcd}")
