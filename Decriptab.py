# Calcola la potenza b^H in Zn
b = int(input("Inserisci il numero criptato (la base criptata b): "))
H = int(input("Inserisci la chiave pubblica H: "))
n = int(input("Inserisci il modulo n (di Zn): "))
x=b
y=H
z=1
while y>0:
    if y%2==1:
        z=z*x
        z=z%n
        y=y-1
    x=x*x
    x=x%n
    y=y//2
print('Il numero decriptato (La potenza b^H modulo(n)) è:')
print(z)