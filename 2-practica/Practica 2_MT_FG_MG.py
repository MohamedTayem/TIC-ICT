º
"""
Spyder Editor
LZ77 Software
Autores: Fabio Rodríguiez, Marcos García, Mohamed Tayem

"""

import pickle 

def buferes(texto, pos):
    diccionario = texto[pos:pos+255]
    busqueda = texto[0:pos]
    
    return(busqueda, diccionario)



def triple(busqueda, codificacion):
    L = len(codificacion)
    patron = ''
    pos = 0
    while patron in busqueda and pos < L:
        patron += codificacion[pos]
        pos += 1
    longitud = len(patron) - 1
    letra = patron[-1]
    if longitud == 0:
        distancia = 0
    else:
        if pos == L - 1:
            longitud += 1
            letra = codificacion[-1]
            indice = busqueda.find(patron)
            distancia = len(busqueda) - indice
        else:
            patron = patron[:-1]
            indice = busqueda.find(patron)
            distancia = len(busqueda) - indice
    return([distancia, longitud, ord(letra)])


def triples():

   print("introduzca la ruta del archivo de texto :\n")
   #ruta = "C:/Users/percu/OneDrive/Escritorio/Prueba.txt"
   ruta = input()
   f = open(ruta, "r", encoding = 'utf-8')
   c = f.read()
   print(c)


   aux = len(c) - 1
   pos = 0
   avance = 0


   listamiTriple = []

   while(pos<aux):

       miBufer = buferes(c, pos)
       miTriple = triple(miBufer[0], miBufer[1])
       listamiTriple.append(miTriple)
      
       avance = miTriple[1]
       pos = pos + avance + 1
      
   return listamiTriple


miLista = triples()


def comprimir(miLista):
    tamañoLista = len(miLista)
    #ListaBytes = [] #Lista donde vamos a guardar los bytes
    i= 0
    #lBytes = []
    l = []
    
    for i in range(0, tamañoLista):
        l.extend(miLista[i])
        
    #ListaBytes = bytearray(lBytes[])
    #print(ListaBytes)
    
    lb = bytes(l)
    print("\n") 
    #print(lBytes)    
    #print("\n") 
   # print(ListaBytes)
   # print("\n") 
    print(lb)
    
    print("\n\tIntroduzca el la ruta donde se guardará el fichero binario. (no olvides introducir el nombre de este último)")
    ruta = input()
    #ruta = "C:/Users/percu/OneDrive/Escritorio/codes.bin"
    
    with open(ruta, "wb") as f:
        #for i in ListaBytes:
            f.write(lb)
    f.close()

comprimir(miLista)


def descomprimir():
    ListaTriples = []
    aux = 0
    
    print("\n\tIntroduzca el la ruta donde se guardará el fichero binario. (no olvides introducir el nombre de este último)")
    ruta = input()
    #ruta = "C:/Users/percu/OneDrive/Escritorio/codes.bin"
    
    lRecuperado = bytearray()
    with open(ruta, "rb") as f:
        l = f.read()
    
    for i in range(0, len(l)):
        x = 0
        lRecuperado[x][i].append(l[i])
        
        if(i == aux + 3):
            aux = i
            x += 1
   
    i=0
    for i in range(0, len(lRecuperado)):
        ListaTriples.append(list(lRecuperado[i]))
    
    return ListaTriples

misTriples = descomprimir()
    


def completar(cadenaEntrada, triple):
    cadenaCompleta = []
    
    cadenaDistancia = cadenaEntrada[-triple[0]:]
    cadenaLongitud = cadenaDistancia[:triple[1]]
    cadenaCompleta = cadenaEntrada + cadenaLongitud + chr(triple[2])
    return cadenaCompleta





def descodificar(triples):
    tamaño = len(triples)
    cadenaDescodificada = []
    
    for i in range(0, tamaño):
        
        if(i == 0):
            cadenaDescodificada = chr(triples[i][2])
        else:
            cadenaDescodificada = completar(cadenaDescodificada, triples[i])
            
            
    return cadenaDescodificada