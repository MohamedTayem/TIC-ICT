# -*- coding: utf-8 -*- 
"""
Created on Wed Sep 28 16:19:16 2022

@author: Fabio Rodríguez Gómez.
        Marcos García Rebollal.
        Mohammad Tayem Abo Hadwa.

"""

import pickle
from bitarray import bitarray 

# =============================================================================
# PROYECTO 1: CODIFICACIÓN DE HUFFMAN BINARIA DE MÍNIMA VARIANZA
# =============================================================================

#f = open(rutaQ, 'r', encoding = 'utf-8')


#------------------------------------------------------------------------------
#--------------- FUNCIONES CORRESPONDIENTES A LA ENTREGA 1: -------------------
#------------------------------------------------------------------------------

'''
    FUNCIÓN: frecuencias
    ------------------------------------
    
    Objetivo de la función: 
    -----------------------
    -> Generar un diccionario con los símbolos ASCII y sus frecuencias absolutas a partir de un archivo de texto.
                    
    Parámetros de Entrada: 
    ----------------------
    -> La ruta del archivo de texto al que pretendemos hallar las frecuencias absolutas de sus carácteres.
    
    Parámetros de Salida:
    ---------------------
    -> El diccionario con los carácteres y sus frecuencias.
    
'''

def frecuencias(ruta):
    #Definimos las variables de clase;
    
    totalCaracteres = []
    totalFrecuencias = []
    i = 0
    
    #Abrimos el fichero en modo de lectura de la ruta que le hemos pasado cómo entrada.
    f = open(ruta, 'r', encoding = 'utf-8')
    
    c = f.read()

    for i in range(0,255):
        
        #Almacenamos en la lista todos los carácteres ASCII:
        totalCaracteres.append(chr(i))
        
        #Almacenamos en la lista todas las frecuencias de su correspondiente carácter:
        totalFrecuencias.append(c.count(chr(i)))
    
    #Creamos el diccionario (usando dict y zip), cerramos el fichero y devolvemos el diccionario:
    D = dict(zip(totalCaracteres, totalFrecuencias))
    f.close()
    return D


'''
    FUNCIÓN: ordenar
    ------------------------------------
    
    Objetivo de la función: 
    -----------------------
    -> Ordenar el diccionario anterior en orden decreciente de frecuencias.
                    
    Parámetros de Entrada: 
    ----------------------
    -> El diccionario generado en la función anterior 'frecuencias'.
    
    Parámetros de Salida:
    ---------------------
    -> Un nuevo diccionario ordenado.
    
'''
def ordenar(D):

   listaOrdenada = sorted (list(D.items()), key = lambda x: x[1], reverse = True)
   return listaOrdenada



'''
    FUNCIÓN: modificar
    ------------------------------------
    
    Objetivo de la función: 
    -----------------------
    -> Modificar la lista anterior de manera que todos los caracteres ASCII con
       frecuencia nula pasen a tener frecuencia 1.
                    
    Parámetros de Entrada: 
    ----------------------
    -> El diccionario de frecuencias ordenado hallado en la funcion 'ordenar'.
    
    Parámetros de Salida:
    ---------------------
    -> El diccionario modificado.
'''

def modificar(listaOrdenada):
    
    listaOrdenada = list(map(list, listaOrdenada))

    for i in range (0,255):
        if(listaOrdenada[i][1] == 0):
           listaOrdenada[i][1] = 1 

    return listaOrdenada


'''
    FUNCIÓN: guardar / guardarTexto
    ------------------------------------
    
    Objetivo de la función: 
    -----------------------
    -> Guardar la lista anterior en un archivo binario.
                    
    Parámetros de Entrada: 
    ----------------------
    -> Nuestro diccionario de datos hallado en la función 'ordenar' y 'modificar'
    
    Parámetros de Salida:
    ---------------------
    -> ---
    
'''

def guardar(O, ruta):
    
    with open (ruta, 'ab') as fi:
        pickle.dump(O, fi)
        
        
    return ruta
        
def guardarTexto(O, ruta):
    
    with open(ruta, 'w', encoding = 'utf-8') as f:
        f.write(O)
        
    return ruta
        

'''
FUNCIÓN: recuperar 
    ------------------------------------
    
    Objetivo de la función: 
    -----------------------
    -> Recuperar el archivo binario guardado anteriormente y obtener un objeto (lista o diccionario) de él.
                    
    Parámetros de Entrada: 
    ----------------------
    -> La ruta en la que se encuentra el archivo binario que queremos recuperar.
    
    Parámetros de Salida:
    ---------------------
    -> El objeto hallado del archivo binario.
'''

def recuperar(rutaB):
    
    fi = open(rutaB, 'rb')
    ficherobin = pickle.load(fi)
    print('\tObjeto recuperado con éxito de: ', rutaB)
    return ficherobin


'''
FUNCIÓN: Huffman 
    ------------------------------------
    
    Objetivo de la función: 
    -----------------------
    -> Hallar los códigos óptimos a partir de nuestro diccionario de carácteres-frecuencias.
                    
    Parámetros de Entrada: 
    ----------------------
    -> Nuestro diccionario de carácteres-frecuencias.
    
    Parámetros de Salida:
    ---------------------
    -> Los códigos óptimos hallados tras aplicar el método de Huffman.
'''

def Huffman(listaOrdenadaModificada):
    #declarmos las variables de clase:
    frecuencias = [x[1] for x in listaOrdenadaModificada]
    n = len(frecuencias)-2
    
    i = 0
    aux = frecuencias
    posiciones = []

    for i in range (n):
        suma = aux[-1] + aux [-2]
        aux.pop(-1)
        aux.pop(-1)
        
        aux.append(suma)
        
        #Ordenamos nuestra nueva lista;
        aux.sort(reverse=True)
        
        posiciones.append(aux.index(suma))
        
    traduccion = [bitarray('0'), bitarray('1')]
    for i in range(1, len(posiciones)+1):
        aux = traduccion[posiciones[-i]]
        traduccion.pop(posiciones[-i])
        traduccion.append(aux+bitarray('0'))
        traduccion.append(aux+bitarray('1'))
    return traduccion


'''
FUNCIÓN:  comprimir_Huffman 
    ------------------------------------
    
    Objetivo de la función: 
    -----------------------
    -> Comprimir un un archivo de texto a un fichero binario. Los ratios de compresión esperados se cumplen.
                    
    Parámetros de Entrada: 
    ----------------------
    -> Un diccionario que se refiere al diccionario de carácteres-códigos (la creación se tiene que hacer previa a la llamada de la función. Y cómo segundo argumento el fichero de texto que queremos comprimir (previamente hay que abrirlo en modo escritura y atribuirlo a una variables con el metodo .read()
    
    Parámetros de Salida:
    ---------------------
    -> Devuelve el archivo comprimido (que posteriormente deberemos guardar)
'''

def comprimir_Huffman(diccionario, archivo):
    archivocod = bitarray()
    archivocod.encode(diccionario, archivo)
    #archivocod.append(bitarray('1')) 
    
    return archivocod

'''
FUNCIÓN:  descomprimir_Huffman
    ------------------------------------
    
    Objetivo de la función: 
    -----------------------
    -> Descomprimir un archivo binario (previamente comprimido en la opción comprimir_Huffman) al archivo de texto que originalmente era.
                    
    Parámetros de Entrada: 
    ----------------------
    ->  Cómo primer argumento la ruta donde se encuentra el archivo binario y cómo segundo argumento el diccionario de carácteres-códigos optimos.
    
    Parámetros de Salida:
    ---------------------
    -> El archivo descomprimido. 
'''

def descomprimir_Huffman(rutaFB, diccionarioBits):
   
    cb = bitarray()
    with open (rutaFB, 'rb') as fb:
        cb = pickle.load(fb)
        
   # aux = len(cb) -1
    
   # while( cb[aux] != bitarray('1')):
     #       del(cb[-1])

            
    #del(cb[-1])
   
    td = ''.join(cb.decode(diccionarioBits))
    
    
    #guardar(td)
    return td
    


def menu():
    print('\n\n\t Seleccione una opción: \n\n\t')
    print('1- Generar código de Huffman a partir de un archivo de texto\n\t')
    print('2- Comprimir archivo de texto (es necesario ejecutar la opción anterior previamente)\n\t')
    print('3- Descomprimir archivo binario\n\t')
    print('4- Salir\n\n\t')
    print('Opción: ')
    opcion = input()
    return opcion              
 
# rutaQ = 'C:/Users/percu/OneDrive/Escritorio/quijote.txt'
def main():
   c = {} 
   print('----------------------------------------------------------------------------------------')
   print('\t\tBIENVENIDO AL PROYECTO 1 DE TRATAMIENTO AUTOMÁTICO DE LA INFORMACIÓN')
   print('----------------------------------------------------------------------------------------')
   print('\n\tNOTA PARA EL USUARIO: En esta práctica trataremos la codificación de Huffman binaria\n\tde mínima varianza sobre ficheros de texto, siga correctamente las indicaciones e\n\tintroduzca datos válidos. Si tiene alguna duda acuda al Manual para el Usuario de\n\tla Memoria Técnica. <Presiona ENTER para continuar> Buen viaje!')
   input()
  
   #IMPRIMIMOS EL MENÚ
   
   while True:
       opcion = menu()
       try:
       
           #EJECUTAMOS OPCIÓN 1
           
           if opcion == '1':  
           
               while True:
                  print('\tIntroduzca la ruta del fichero de texto: ')
                  rutaFicheroTXT = input()
                  try:  
                      diccionarioFrecuencias = frecuencias(rutaFicheroTXT)
                      break;
                  except FileNotFoundError:
                      print('\tERROR! Ruta del archivo inválida. Comprueba que no tiene errores o si el fichero existe\n\ten la dirección proporcionada.\n')
           
               listaOrdenada = ordenar(diccionarioFrecuencias)
               listaOrdenadaModificada = modificar(listaOrdenada)
              
               print('\n\tApertura exitosa! Se han hallado las frecuencias y se han ordenado y modificado la lista\n\tresultante de manera satisfactoria!\n')
               while True:
                   print('\tIntroduzca la ruta donde guardar el fichero binario resultante: ')
                   rutaBinario = input()
                   try:
                       ruta = guardar(listaOrdenadaModificada, rutaBinario)
                       break;
                   except FileNotFoundError:
                       print('\t ERROR! Ruta de guardado inválida. Comprueba que no tiene errores o si la carpeta existe\n\ten la dirección proporcionada.\n')
                 
               print('\n\tGuardado exitoso!\n\n\t')        
               print('A continuación procedemos a ejecutar Huffman\n\n\t')
               
               while True:
                   abierto = recuperar(ruta)
                   fichero_Huff = Huffman(abierto) 
                   letras = [x[0] for x in listaOrdenadaModificada]
                   diccionarioBits = dict(zip(letras, fichero_Huff))

                   print('\tIntroduzca la ruta donde guardar los códigos óptimos hallados con Huffman: ')
                   rutaFicheroCodigos = input()
                   try:
                       guardar(fichero_Huff, rutaFicheroCodigos)
                       break;
                   except FileNotFoundError:
                       print('\n\n\tHa ocurrido un error al ejecutar Huffman')
                       
               print ('\n\n\t¿Desea regresar al menú?(S/N)')
               regreso = input() 
               if regreso == ('N'):           
                   print('\n\n\tGracias por usar nuestro programa...\n\tPulse Intro para salir')
                   input()
                   break;
                   
                   
           #EJECUTAMOS OPCIÓN 2
                       
           elif opcion == '2':
               print('\n\n\thas elegido la opcion 2')
                              
               print ('Comprimimos el  archivo de texto. ')
               f = open(rutaFicheroTXT, 'r', encoding = 'utf-8')
               c = f.read()
               #Creamos el diccionario:
               archivoCompreso = comprimir_Huffman(diccionarioBits, c)
               
               print('\n\tIntroduzca la ruta donde guardar el archivo comprimido: ')
               rutaGuardarCompreso = input()
               guardar(archivoCompreso, rutaGuardarCompreso)
               f.close()
               
               print ('\n\n\t¿Desea regresar al menú?(S/N)')
               regreso = input() 
               if regreso == ('N'):           
                   print('\n\n\tGracias por usar nuestro programa...\n\tPulse Intro para salir')
                   input()
                   break;
                      
            
          #EJECUTAMOS OPCIÓN 3
           elif opcion == '3':
               print('\n\nVamos a decomprimir el codigo binario')
              
               TBC = descomprimir_Huffman(rutaGuardarCompreso, diccionarioBits)
               
               print("\n\nSe ha descomprimido el archivo binario, se ha generado el archivo de texto satisfactoriamente")
               
               print("\En que dirección quiere guardar el archivo de texto generado:")
               
             
               rutaft = input()
               
               guardarTexto(TBC, rutaft)
               
               print("\nSe ha guardado el archivo de texto")
           
               print ('\n\n\t¿Desea regresar al menú?(S/N)')
               regreso = input() 
               if regreso == ('N'):           
                   print('\n\n\tGracias por usar nuestro programa...\n\tPulse Intro para salir')
                   input()
                   break;
          
           #EJECUTAMOS OPCIÓN 4
           elif opcion == '4':
               print('\n\n\tGracias por usar nuestro programa...\n\tPulse Intro para salir')
               input()
               break;
           
          
           #Control de datos de entrada
           else:
               print('\n\n\tERROR!\tIntroduzca un número del 1-3')
          
       except regreso == 'N':
          
           #EJECUTAMOS OPCIÓN 4
           
               print('\n\n\tGracias por usar nuestro programa...\n\tPulse Intro para salir')
               input()
