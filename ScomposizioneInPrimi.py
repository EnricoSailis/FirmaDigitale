def scomposizione_in_fattori_primi(numero):
    fattori_primi = []
    divisore = 2

    while divisore <= numero:
        if numero % divisore == 0:
            fattori_primi.append(divisore)
            numero //= divisore
        else:
            divisore += 1

    return fattori_primi

# Input del numero da scomporre
numero_da_scomporre = int(input("Inserisci un numero intero positivo: "))

# Scomposizione in fattori primi e stampa del risultato
fattori_prim = scomposizione_in_fattori_primi(numero_da_scomporre)
print(f"I fattori primi di {numero_da_scomporre} sono: {fattori_prim}")
