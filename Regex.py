
import re

#------------------------- Metodos -------------------------
def salto():
    print("\n")

#------------------------- Termina metodos -------------------------

def main():
    pass

if __name__ == '__main__':
    main()

f=open('doc.txt')
cadenabusqueda=""

for line in f:
    cadenabusqueda += line

print(cadenabusqueda)


#pahtfinder2=re.compile('^[0-9a-zA-Z]([-.\w]*[0-9a-zA-Z_+])*@([0-9a-zA-Z][-\w]*[0-9a-zA-Z]\.)+[a-zA-Z{2,9}]$',re.IGNORECASE)
#findpath2=re.findall(pahtfinder2,cadenabusqueda)

#for i in findpath2:
 #   print(i)




espacio=re.compile('\s')
escan=re.search(espacio,cadenabusqueda)

digitos=re.compile('\d')
dscan=re.search(digitos,cadenabusqueda)

letras=re.compile('[a-z]',re.IGNORECASE)
fscan=re.search(letras,cadenabusqueda)

url=re.compile('(?:http://|www.).*?["]')
uscan=re.search(url,cadenabusqueda)

#------------------------------- Posiciones ------------------------------------

#print ("Identificadores")
#print(fscan.group())
#print("Posiciones ")
#print(fscan.start())
#print(fscan.end())
#print("Resumen pos")
#print(fscan.span())


#--------------------------------Letras ----------------------------------------
salto()
fscan=re.findall(letras,cadenabusqueda)
for i in fscan:
    print("Letras: " +i)


#-------------------------------Numeros ----------------------------------------
salto()
dscan=re.findall(digitos,cadenabusqueda)
for n in dscan:
    print("Digitos: "+n)


#------------------------------- simbolos---------------------------------------
salto()
pos=0
blanco=re.compile('[*-,-.-/@]')
bscan=re.search(blanco,cadenabusqueda)
bscan=re.findall(blanco,cadenabusqueda)
for b in bscan:
    print("-simbolos: "+b)
#------------------------------- E. Vacios -------------------------------------
salto()
escan=re.findall(espacio,cadenabusqueda)
for e in escan:
    print ("Espacio vacio: " +e)




#--------------------------- Emails --------------------------------------------
salto()
f=open('doc.txt')

for line in f:
    match= re.search(r'[\w.-]+@[\w.-]+',line)
    if match:
        print('email: ')
        print match.group()
#-------------------------------URL --------------------------------------------
salto()
f=open('doc.txt')
for line in f:
    match= re.search(r'www\.[a-zA-Z0-9]*\.[a-zA-Z]{3,}\.*[a-zA-Z]*$',line)
    if match:
        print('Url: ')
        print match.group()
