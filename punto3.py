# Punto 

print (" ")
print ("Torres Olvera Gael")
print (" ")

#Especifica la ruta del archivo

rutaarchivo = "Demofile.txt"

#Abrir el archivo en modo lectura

f = open(rutaarchivo, "r")
    
#Leer el contenido del archivo

contenido = f.read()
    
#Imprimir el contenido

print("Este archivo se localiza en Demofile: ", contenido)

#Cerrar el archivo si fue abierto

if 'f' in locals():
        
        f.close()