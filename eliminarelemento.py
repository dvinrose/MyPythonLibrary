# Abre el archivo en modo de lectura y escritura
with open('pythonmetodos.py', 'r+') as archivo:
    # Lee el contenido del archivo
    contenido = archivo.read()
    
    # Reemplaza todos los caracteres "|" con una cadena vacía
    contenido_modificado = contenido.replace('|', '')
    
    # Vuelve al inicio del archivo para escribir el contenido modificado
    archivo.seek(0)
    archivo.write(contenido_modificado)
    
    # Trunca el archivo al nuevo tamaño
    archivo.truncate()
