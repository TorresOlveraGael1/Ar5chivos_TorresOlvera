# Punto 2

print (" ")
print ("Torres Olvera Gael")
print (" ")

#Abrir el archivo en modo lectura

f = open("demofile.txt", "r")

#Leer el contenido del archivo

contenido = f.read()

#Imprimir el contenido

print(contenido)

#Cerrar el archivo si fue abierto

if 'f' in locals():
        
        f.close()
