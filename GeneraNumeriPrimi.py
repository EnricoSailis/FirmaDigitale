# Generazione di numeri primi casuali con un numero qualsiasi di cifre con la funzione nextprime() di sympy
import sympy as sp
import secrets as sc
n=int(input('Digita il numero delle cifre del numero primo casuale che vuoi ottenere: '))
# Si calcola il numero nbit di bit che occorrono per rappresentare il numero di n cifre 
# in notazione binaria
nbit = int(3*sp.log(10**n,8))
# viene generato un numero binario casuale sn con nbit bit
sn = sc.randbits(nbit)
# viene cercato il numero primo p successivo al numero intero sn 
p=sp.nextprime(sn)
print(p)