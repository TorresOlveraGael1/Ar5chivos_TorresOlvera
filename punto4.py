# Punto 4

print (" ")
print ("Torres Olvera Gael")
print (" ")

#Especifica la ruta del archivo

ruta_archivo = "demofile.txt"

#Abrir el archivo en modo lectura

f = open(ruta_archivo, "r")
    
#Leer los primeros 5 caracteres del archivo

contenido_parcial = f.read(5)
    
#Imprimir el contenido leído

print(contenido_parcial)

#Cerrar el archivo si fue abierto

if 'f' in locals():
        
        f.close()
