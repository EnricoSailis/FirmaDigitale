# Trasforma una stringa di caratteri ascii in un numero intero 
n=0
testo = str(input("Inserisci una stringa da convertire in numero: "))
for c in testo:
    n=n*256+ord(c)
print(n)