# Determina l'inverso di a in Zn se MCD(n,a)=1
lx=[]
lq=[]
lt=[]
H = int(input("Inserisci il numero da invertire H < fi(n) in Zfi(n), H: "))
n = int(input("Inserisci il numero fi(n): "))
lx.append(n)
lx.append(H)
r=1
i=1
q=1
while (r!=0) :
    q=lx[i-1]//lx[i]
    lq.append(q)
    r=lx[i-1]%lx[i]
    lx.append(r)
    i=i+1
# viene stampato l'MCD(a,n) 
if lx[i-1] != 1:
    print("MCD(",n, ",",H,")=",lx[i-1])
    print('Inverso non calcolabile con questa routine')
    exit
for m in range(i-1):
    lt.append(m)
lt[m]=1
lt[m-1]=-lq[m-1]
lt[m-1]=lt[m-1]%n
m=m-2
while (m>=0):
    lt[m]=-lq[m]*lt[m+1]+lt[m+2]
    lt[m]=lt[m]%n
    m=m-1

# lt[0] è l'inverso di H in Zfi(n) se MCD(fi(n),H)=1
if lx[i-1] == 1:
    print("l'inverso K è:")
    print(lt[0])

