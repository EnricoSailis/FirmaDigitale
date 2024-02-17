import tkinter as tk
import sympy as sp
import secrets as sc

H=0
K=0
n=0
fn=0


# Generazione di numeri primi casuali di 620 cifre con la funzione nextprime() di sympy
def genera_n_primo(n):
    # n è numero delle cifre del numero primo casuale che vogliamo ottenere
    # Si calcola il numero nbit di bit che occorrono per rappresentare il numero di n cifre 
    # in notazione binaria
    nbit = int(3*sp.log(10**n,8))
    # viene generato un numero binario casuale sn con nbit bit
    sn = sc.randbits(nbit)
    # viene cercato il numero primo p successivo al numero intero sn 
    p=sp.nextprime(sn)
    return p

# Generazione del MCD tra due numeri a, b con l'algoritmo di Euclide
def MCD(a,b):
    lx=[]
    lq=[]
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
    # L'ultimo rtext_box.insert("2.0",H)esto non nullo è il MCD
    return lx[i-1]



# Generazione della chiave pubblica
def generaChiave_H():
    p = genera_n_primo(620)
    q = genera_n_primo(620)
    n = p*q
    fn = (p-1)*(q-1)
    H = genera_n_primo(310)
    return H, n, fn
    

def generaChiave_K(H, fn):
    # Determina l'inverso K di H in Zfn
    lx=[]
    lq=[]
    lt=[]
    lx.append(fn)
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
    # viene controllato l'MCD(H,fn) 
    if lx[i-1] != 1:
        # l'Inverso H non esiste in Zfn
        return 0
    else:
        for m in range(i-1):
            lt.append(m)
        lt[m]=1
        lt[m-1]=-lq[m-1]
        lt[m-1]=lt[m-1]%fn
        m=m-2
        while (m>=0):
            lt[m]=-lq[m]*lt[m+1]+lt[m+2]
            lt[m]=lt[m]%fn
            m=m-1
        # lt[0] è l'inverso di H in Zfn se MCD(fn,H)=1
        return lt[0]


    
window = tk.Tk()
window.geometry("1800x1200")
window.title("Chiavi pubblica e privata per crittografia RMS")


text_box = tk.Text(
   # text="Hello, Tkinter",
    fg="white",
    bg="black",
    width=100,
    height=30
)
text_box.insert("1.0",'Hello tKinter \n')
text_box.pack()



button = tk.Button(
    text="Genera le Chiavi",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
)
button.pack()




# Create an event handler
def handle_click(event):
    # The button was clicked!
    H , n , fn = generaChiave_H()
    K = generaChiave_K(H, fn)
    text_box.delete("1.0", tk.END)
    text_box.insert("1.0",'Chiave Pubblica H:\n')
    text_box.insert("2.0",H)
    text_box.insert("14.0", "\n\nModulo n (Pubblico):  \n")
    text_box.insert("16.0", n)
    text_box.insert("30.0",'\n\nChiave Privata K:\n')
    text_box.insert("32.0",K)

button.bind("<Button-1>", handle_click)

# Run the event loop
window.mainloop() 