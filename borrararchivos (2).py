import os

# Obtener la lista de archivos del directorio actual
archivos = os.listdir()

# Recorrer la lista de archivos
for archivo in archivos:
  # Comprobar si el archivo contiene la palabra clave "thumb"
  if "thumb" in archivo:
    # Intentar eliminar el archivo
    try:
      os.remove(archivo)
      print(f"Archivo {archivo} eliminado")
    # Capturar posibles excepciones
    except OSError as e:
      print(f"Error al eliminar el archivo {archivo}: {e}")
