# Viene letto un file scelto all'avvio del programma e si calcola il digest 
#con l'algoritmo SHA-256. Dopo si cripta il digest del file con l'algoritmo
# RSA con la chiave privata del firmatario e si aggiunge una nuova pagina al 
# file contenente il di digest criptato (firma digitale)
#


# Import Libraries

# import OpenSSL
import os
# import time
# import argparse
from typing import Tuple
from pypdf import PdfReader, PdfWriter
from pypdf.annotations import FreeText
import hashlib

# Funzione per calcolare l'hash SHA-256 di un file
def calcola_hash(file_path):
    try:
        # Apri il file in modalità binaria
        with open(file_path, 'rb') as file:
            # Crea un oggetto hash SHA-256
            sha256_hash = hashlib.sha256()
            
            # Leggi il file in blocchi e aggiorna l'oggetto hash
            while True:
                data = file.read(8192)
                if not data:
                    break
                sha256_hash.update(data)
        
        # Restituisce il digest hash come stringa esadecimale
        return sha256_hash.hexdigest()
    
    except IOError:
        print("Impossibile aprire il file: " + file_path)

# Funzione per criptare una stringa 'digest' esadecimale usando l'algoritmo RSA
# con chiave K e modulo n. 
def CriptaDigest(digest: str, K: int, n: int):
    # il digest da criptare quì è dato come una stringa di caratteri edadecimali
    # ma viene usato come numero intero b,  base della potenza b^K in Zn per la criptazione
    # Il digest perciò viene prima convertito da stringa di un numero esadecimale in numero intero
    b= int(digest, base=16)

    # Calcola la potenza b^K in Zn
    x=b
    y=K
    z=1
    while y>0:
        if y%2==1:
            z=z*x
            z=z%n
            y=y-1
        x=x*x
        x=x%n
        y=y//2
    # Viene reso il degest criptato in esadecimale
    return hex(z)

# Funzione per la firma di un file, i suoi argomenti sono:
# input_file: il nome con il path del file PDF da firmare
# signature_Key: la chiave per la firma RSA usata per criptare il digest del file
# n: il modulo per l'algoritmo di criptazione RSA
# output_file: il nome del file firmato
def sign_file(input_file: str, signature_Key: int, n: int,  
            output_file: str = None):
    """Sign a PDF file"""
    # An output file is automatically generated with the word signed added at its end
    if not output_file:
        output_file = (os.path.splitext(input_file)[0]) + "_signed.pdf"
    
    # Calcola l'hash SHA-256 del file PDF
    digest = calcola_hash(input_file)

    # Cripta il digest del file 'input_file'
    digest_Criptato =  CriptaDigest(digest,signature_Key, n) 

    # Fill the writer with the pages of input_file plus one blank page 
    reader = PdfReader(input_file)
    writer = PdfWriter()
    n_pages = 0
    for page in reader.pages:
        writer.add_page(page)
        n_pages += 1
    writer.add_blank_page()

    # Create the annotation and add it in the end of the output_file
    annotation = FreeText(
        text= '---Begin Digest SHA-256---'+ digest +'---End Digest---'+
        '---Begin Sign--- ' + digest_Criptato + ' ---End Sign---',
        rect=(100, 100, 500, 750),
        font="Arial",
        bold=True,
        italic=True,
        font_size="10pt",
        font_color="00ff00",
        border_color="0000ff",
        background_color="ffffff",
    )
    writer.add_annotation( n_pages, annotation=annotation)

    # Write the annotated file to disk
    with open(output_file, "wb") as fp:
        writer.write(fp)
    return

# Programma

# inserisci il nome del file e il percorso in cui si trova il
# file PDF da cui calcolare il digest
file_path = str(input("Inserisci il path e il nome del file da firmare: "))
#file_path = 'example.pdf'

# Assicurati di inserire il percorso corretto del tuo file PDF nella variabile `file_path`.
# Il programma quindi aprirà il file e calcolerà il digest utilizzando l'algoritmo SHA-256, 
# cripterà il digest e lo aggiungerà al file di output


signature_Key= 69729428827930899183607904616229985842269963177873462806550791243015515893228012754535447283045456093648796565545482388559216998001313772253247131238948916339616616333433642305923161144436208501542593132750598556411082490354646124291265345780548457302706515796763248183218460480964615980283440559800103384466184123378345486832821197227647753570576694822267629113376762083734298444890155036444225723982496268420630059128234068962473779528265669944210192073772136646502432576096952648315253102846980995997507053049038332249490141455541773645199514195246743777790033308370390765864806598857826866817056292458352023063625067683424814091639544978659278094265830691795115576925584040053075671354070113858524846394200765592692996446227904200284972162627234915664507968641619306935061060349821811537298401389960432033986365286407192375084346928759218711447978442884878146896673017590135122027630448808746245478771982722074448477177832006590260829396937572857983512625124793297097332532552621671862163240507060218152775295558835879156033784082866908521551688930028740238747503104986654871675263014782005162233621410448425767197915873026587059041741469459211226946404653305543778380301912356639336870861222291839382224391749106177712251553365086219

# Modulo n di Zn
n= 701064518855611018351478696102506418399825442746726653223259695569509705775468431772016597671558340607176346069752387207300026319363235606235803343592326202997400179617232019898767655393020397478647637150500050978535824202795469084521218646678629269178928306570620187601077271773458876859353270307835027595075038292233528235482015692258319706954736176144228736447145479019798447992154270115981577086151819437202886383848776226342314587052829542561202681322155196513938369788363934202405133469168018152271115890431532142836923770243207039391995003181279950488824074904548090582844789163411833034207527724019908213858019813574716214838351551568686418650274084997640777976729912298861277261397747425777635172396963553598286311289269115577524113338028246799325084673319859124125510550293016147399980140661943934972558897611773600100723236950713154800419871639330290163565729022078814691879197262001467891838174253933635274752948230841496813002422616125866329887302774948331671474309522475458181415662705105517059813429641495185150256124546384599638148221533780634964083425344194795009915658593666194343095352161043369775538059183929274715046394302155444556334070754961373304906265204034240001167623886325280987458856900403236196789147149332993


sign_file(file_path,signature_Key,n)

