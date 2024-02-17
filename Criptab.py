# Calcola la potenza b^K in Zn
b = int(input("Inserisci un numero da criptare (la base b): "))
K = int(input("Inserisci la chiave privata K: "))
n = int(input("Inserisci n (di Zn): "))
x=b
y=K
z=1
while y>0:
    if y%2==1:
        z=z*x
        z=z%n
        y=y-1
    x=x*x
    x=x%n
    y=y//2
print('Il numero criptato (La potenza b^K modulo(n)) è:')
print(z)