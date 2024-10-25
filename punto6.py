# Punto 6

print (" ")
print ("Torres Olvera Gael")
print (" ")

#Especifica la ruta del archivo

ruta_archivo = "demofile2.txt"

#Abrir el archivo en modo escritura (sobrescribir)

f = open(ruta_archivo, "w")

# Escribir nuevo contenido en el archivo

f.write("Woops! I have deleted the content!\n")

# Leer el archivo después de sobrescribir el contenido

f = open(ruta_archivo, "r")

#Leer y mostrar el contenido del archivo

contenido = f.read()

print(contenido)

#Cerrar el archivo si fue abierto

if 'f' in locals():

        f.close()