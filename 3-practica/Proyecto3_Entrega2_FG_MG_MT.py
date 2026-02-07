from bitarray import bitarray

import random 
 

def cuartetos():

  c = bitarray()
  l4c = []
 

  ruta = input()
  with open (ruta, 'rb') as f:

      c.fromfile(f)

  lc = len(c)

  for i in range (0, lc, 4):  
      l4c.append(c[i : i + 4])

  return l4c

 
def Hamming(cuarteto):

    MC = bitarray('1010')
    suma = []

    codigo = bitarray()
   
    #Matriz Generatriz.
    G = [bitarray('10001101'), bitarray('01001011'), bitarray('00100111'), bitarray('00011110')]

    for i in range(0, 8):
        for j in range(0, 4):
           multiplicacion = G[j][i] * cuarteto[j]
           suma.append(multiplicacion)
           
        xor = suma[0] ^ suma[1] ^ suma[2] ^ suma[3]
        codigo.append(xor)
        suma.clear()
   
    return codigo


def codificar():
   
    print("\nHola, introduzca la dirección del fichero de texto:\n")
   
    Lcuartetos = cuartetos()
   
    c = len(Lcuartetos)
    Loctetos = []
    l =[]
   
    for i in range (0, c):
        Loctetos.append(Hamming(Lcuartetos[i]))
   
   
    for i in range(0, len(Loctetos)):
        l.extend(Loctetos[i])

    Lcconcatenados = bytes(l)
   
    print("\nHola, introduzca la dirección donde quiere guargar el archivo")
    ruta = input()
   
    with open (ruta,'wb') as f:
        f.write(Lcconcatenados) 
        
        
def sindrome(codigo):
    
    #Definimos nuestra matriz de control de paridad (H)
    H = [bitarray('1101'), bitarray('1011'), bitarray('0111'), bitarray('1111'), bitarray('1001'), bitarray('0101'), bitarray('0011'), bitarray('0001')]
    suma = []
    
    sindrome = bitarray()
    
    for i in range(0, 4):
        for j in range(0, 8):
            multiplicacion = H[j][i] * codigo[j]
            suma.append(multiplicacion)
        
        xor = suma[0] ^ suma[1] ^ suma[2] ^ suma[3] ^ suma[4] ^ suma[5] ^ suma[6] ^ suma[7]
        sindrome.append(xor)
        suma.clear()
    
    return sindrome
    

def comprobar(codeword):
    
    sindromeValor = sindrome(codeword)
    
    return sindromeValor.any()



def detectar(palabraErronea):
    
    H = [bitarray('1101'), bitarray('1011'), bitarray('0111'), bitarray('1111'), bitarray('1001'), bitarray('0101'), bitarray('0011'), bitarray('0001')]
    sindromeValor = sindrome(palabraErronea)
    contador = 0
    print(sindromeValor)
    
    for i in range(0, 8):
        if (sindromeValor == H[i]):
            return i
            contador = contador + 1
            
    if(contador == 0):
        return -1
    

def flip(entrada, posicion):
    if(entrada[posicion] == True):
        entrada[posicion] = False
        
    elif(entrada[posicion] == False):
        entrada[posicion] = True
        
    return entrada


def octetos(ruta):

  c = bitarray()
  l8o = []
 

  with open (ruta, 'rb') as f:

      c.fromfile(f)

  lo = len(c)

  for i in range (0, lo, 8):  
      l8o.append(c[i : i + 8])

  return l8o
        
        
        
def leer(ruta):
    
    p4 = []
    l = []
    octetosBits = octetos(ruta)
    longitud = len(octetosBits)
            
    for i in range (0, longitud):  
      p4.append(octetosBits[i][0:4]) 
    
    for i in range(0, len(p4)):
        l.extend(p4[i])
     
    Lcconcatenados = bytes(l)    
    ruta = '/home/alumno/Descargas/moji.bin'
    with open (ruta, 'wb') as f:
        f.write(Lcconcatenados)
        
    
    
    return p4


def errores():
    print("\nHola, introduzca la dirección del archivo codificado:\n")
    ruta = input()
    archivobit = bitarray()
    
    with open(ruta,'rb') as f:
     archivo_codificado = f.read()
   
    
    archivobit.frombytes(archivo_codificado)
    
    print(archivobit)
   
    n = random.randint(0, len(archivobit))
   
    archivo_con_errores = flip(archivobit, n)
    
    return archivo_con_errores
