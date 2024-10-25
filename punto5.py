# Punto 5

print (" ")
print ("Torres Olvera Gael")
print (" ")

#Especifica la ruta del archivo

ruta_archivo = "demofile.txt"

#Abrir el archivo en modo anexar

f = open(ruta_archivo, "a")

#Agregar contenido al final del archivo

f.write("Now the file has more content!\n")

#Leer el archivo después de anexar el contenido

f = open(ruta_archivo, "r")

#Leer y mostrar el contenido del archivo

contenido = f.read()

print(contenido)

#Cerrar el archivo si fue abierto

if 'f' in locals():

        f.close()
