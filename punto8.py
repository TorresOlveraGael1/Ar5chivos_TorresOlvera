# Punto 8

print (" ")
print ("Torres Olvera Gael")
print (" ")

import os

#Especifica la ruta del archivo que deseas eliminar

ruta_archivo = "demofile.txt"

#Comprobar si el archivo existe

if os.path.exists(ruta_archivo):

    # Eliminar el archivo

    os.remove(ruta_archivo)

    print(f"El archivo '{ruta_archivo}' ha sido eliminado.")

else:

    print(f"El archivo '{ruta_archivo}' no existe.")
