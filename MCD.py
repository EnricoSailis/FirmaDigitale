# Determina il MCD di due numeri assegnati a, b, con
# l'algoritmo di Euclide
lx=[]
lq=[]
a = int(input("Inserisci un  numero a: "))

b = int(input("Inserisci un secondo numero b: "))
if a >= b :
    lx.append(a)
    lx.append(b)
else:
    lx.append(b)
    lx.append(a)
r=1
i=1
q=1
while (r!=0) :
    q=lx[i-1]//lx[i]
    lq.append(q)
    r=lx[i-1]%lx[i]
    lx.append(r)
    i=i+1
# L'ultimo resto non nullo è il MCD
print("MCD(",lx[0],',',lx[1],') = ',lx[i-1])