# Calcola la potenza a^h in Zn
a = int(input("Inserisci la base a: "))
h = int(input("Inserisci l'esponente h: "))
n = int(input("Inserisci n (di Zn): "))
x=a
y=h
z=1
while y>0:
    if y%2==1:
        z=z*x
        z=z%n
        y=y-1
    x=x*x
    x=x%n
    y=y//2
print(a,'^',h,'=',z,'(modulo',n,')')