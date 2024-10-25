# Punto 7

print (" ")
print ("Torres Olvera Gael")
print (" ")

#Especifica la ruta del archivo que deseas eliminar

ruta_archivo = "demofile.txt"

import os

#Eliminar el archivo

os.remove(ruta_archivo)

print(f"El archivo '{ruta_archivo}' ha sido eliminado.")

PermissionError

print(f"No tienes permiso para eliminar el archivo '{ruta_archivo}'.")

Exception

print(f"Ocurrió un error al intentar eliminar el archivo:")