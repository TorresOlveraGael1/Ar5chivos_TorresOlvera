# Archivos_TorresOlvera

Torres Olvera Gael

Realizamos codigos en python con archivos

# Punto 1

establecemos un archivo para poder operar los programas con normalidad

Hello! Welcome to demofile.txt
This file is for testing purposes.
Good Luck!

![image](https://github.com/user-attachments/assets/c2107fc6-315c-450b-a20f-f1fa5f247a3b)

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

![image](https://github.com/user-attachments/assets/8e31a094-b8ba-42fc-95fe-447a1bd17735)
![image](https://github.com/user-attachments/assets/20fd4fb3-e5ea-4e82-b1f5-5a9ab05ebde2)

# Punto 3

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

![image](https://github.com/user-attachments/assets/891d58e2-d707-4c14-a555-b3a5c172b956)
![image](https://github.com/user-attachments/assets/7c07b5f9-ab89-49e3-8940-a087f902c699)

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

![image](https://github.com/user-attachments/assets/b1aa858c-64b4-4eab-b5aa-1085db75453f)
![image](https://github.com/user-attachments/assets/0c912d8a-abca-4fe6-86e4-5a0ea6ea8db4)

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

![image](https://github.com/user-attachments/assets/689879e4-4a7e-4c33-8f47-85d309f63f31)
![image](https://github.com/user-attachments/assets/8aff42f9-a68e-434b-8818-1812eee2967e)

# Punto 6

print (" ")
print ("Torres Olvera Gael")
print (" ")

#Especifica la ruta del archivo

ruta_archivo = "demofile2.txt"

#Abrir el archivo en modo escritura (sobrescribir)

f = open(ruta_archivo, "w")

#Escribir nuevo contenido en el archivo

f.write("Woops! I have deleted the content!\n")

#Leer el archivo después de sobrescribir el contenido

f = open(ruta_archivo, "r")

#Leer y mostrar el contenido del archivo

contenido = f.read()

print(contenido)

#Cerrar el archivo si fue abierto

if 'f' in locals():

        f.close()

![image](https://github.com/user-attachments/assets/41b350a3-c53b-4255-8381-e01f9702d968)
![image](https://github.com/user-attachments/assets/ddf34c61-b898-4ca4-afa1-730d8d6aa161)

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

![image](https://github.com/user-attachments/assets/6835b59c-0e05-4a04-ba7a-d8677828b6b9)
![image](https://github.com/user-attachments/assets/cc0be29e-995d-4188-871a-d633af37e6cb)

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

![image](https://github.com/user-attachments/assets/f2cd5dca-6efe-49c8-9739-696996e9aeed)
![image](https://github.com/user-attachments/assets/0ca1e1c1-8422-4a83-9ab7-a1a13b299aa6)

# Punto 9

print (" ")
print ("Torres Olvera Gael")
print (" ")

import os
import shutil

#Nombre de la carpeta a eliminar
carpeta = "demofile"

#Verificar si la carpeta existe
if os.path.exists(carpeta):

    #Eliminar la carpeta y su contenido
    shutil.rmtree(carpeta)
    print(f"La carpeta '{carpeta}' ha sido eliminada.")
else:
    print(f"La carpeta '{carpeta}' no existe.")

![image](https://github.com/user-attachments/assets/9455a1c4-95fd-43ab-8b61-277d5104f6b0)
![image](https://github.com/user-attachments/assets/191a57aa-5e51-4f81-8a17-a4a1be5dcfd8)
