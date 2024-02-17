# l'algoritmo SHA (Secure Hash Algorithm):
# In questo esempio, utiliziamo il modulo "hashlib" fornito dalla libreria 
# standard di Python per calcolare l'hash SHA256 di una stringa. 
# La stringa "Ciao Mondo" viene convertita in una sequenza di byte e quindi 
# passata all'oggetto hash di tipo SHA256 tramite il metodo "update()". 
# Infine, otteniamo l'hash esadecimale tramite il metodo "hexdigest()" 
# e lo stampiamo a schermo.

import hashlib

# Stringa da hashare
stringa = "Ciao Mondo"

# Creazione di un oggetto hash di tipo SHA256
hash_object = hashlib.sha256()

# Encoding della stringa in byte
byte_stringa = stringa.encode()

# Calcolo dell'hash della stringa
hash_object.update(byte_stringa)

# Hash finale in formato esadecimale
hash_esadecimale = hash_object.hexdigest()

# Stampa dell'hash
print("L'hash SHA256 del messaggio è:", hash_esadecimale)

