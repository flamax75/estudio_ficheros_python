import os

# Ruta del archivo que deseas eliminar
ruta_archivo = "/home/flamax75/flaaaa"

# Verificamos si el archivo existe antes de intentar eliminarlo
if os.path.exists(ruta_archivo):
    # Eliminamos el archivo
    os.remove(ruta_archivo)
    print(f"Archivo '{ruta_archivo}' eliminado correctamente.")
else:
    print(f"El archivo '{ruta_archivo}' no existe.")
