# programma  per creare un digest (hash SHA-1) di un file PDF 

import hashlib

# inserisci il nome del file e il percorso in cui si trova
file_path = str(input("Inserisci il path e il nome del file da cui creare l'hash: "))

# Funzione per calcolare l'hash SHA-1 di un file
def calcola_hash(file_path):
    try:
        # Apri il file in modalità binaria
        with open(file_path, 'rb') as file:
            # Crea un oggetto hash SHA-1
            sha1_hash = hashlib.sha1()
            
            # Leggi il file in blocchi e aggiorna l'oggetto hash
            while True:
                data = file.read(8192)
                if not data:
                    break
                sha1_hash.update(data)
        
        # Restituisci il digest hash come stringa esadecimale
        return sha1_hash.hexdigest()
    
    except IOError:
        print("Impossibile aprire il file: " + file_path)

# File PDF da cui calcolare il digest
file_pdf = "path/to/file.pdf"

# Calcola l'hash SHA-1 del file PDF
digest = calcola_hash(file_pdf)

# Stampa il digest ottenuto
print("Digest SHA-1 del file PDF:", digest)

# Assicurati di inserire il percorso corretto del tuo file PDF nella variabile `file_pdf`.
# Il programma quindi aprirà il file e calcolerà il digest utilizzando l'algoritmo SHA-1. 
#Infine, il digest verrà stampato a schermo.