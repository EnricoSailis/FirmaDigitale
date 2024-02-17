# Calcola la potenza b^H in Zn
b = int(input("Inserisci la base b: "))
H = int(input("Inserisci l'esponente H: "))
n = int(input("Inserisci n (di Zn): "))
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
print('La potenza b^H modulo(n) è:')
print(z)