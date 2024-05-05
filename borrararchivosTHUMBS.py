import os
import glob

palabra_clave = "thumb" # la palabra clave que quieres buscar en los nombres de los archivos
directorio = "." # el directorio donde quieres buscar los archivos, puedes cambiarlo según tu preferencia

# crea una lista con los nombres de los archivos que contienen la palabra clave
archivos = glob.glob(os.path.join(directorio, f"*{palabra_clave}*"))

# recorre la lista y elimina cada archivo
for archivo in archivos:
    os.remove(archivo)
    print(f"Archivo {archivo} eliminado")

# muestra un mensaje final
print(f"Se han eliminado {len(archivos)} archivos con la palabra clave {palabra_clave}")
