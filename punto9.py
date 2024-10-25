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
