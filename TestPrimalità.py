# Test di primalità con l'uso della funzione is_prime()
from sympy import *
n=int(input('Digita un numero intero per scoprire se è primo: '))
if isprime(n):
    print('Il numero: ',n," è primo")
else: 
    print('Il numero: ',n, " non è primo")