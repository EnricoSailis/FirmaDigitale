# Trasforma un numero intero in una stringa di caratteri ASCII esteso 
testo = ''
n = int(input("Inserisci un numero intero da convertire in stringa: "))
while n > 0 :
    r = n % 256
    c = chr(r)
    testo = c + testo
    n = n // 256
print('testo:',testo)