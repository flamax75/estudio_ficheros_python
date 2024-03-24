import os

# Ruta del archivo actual
ruta_archivo_actual = "/home/flamax75/salida.txt"

# Nuevo nombre del archivo
nuevo_nombre = "mu.txt"

# Ruta del archivo con el nuevo nombre
ruta_nuevo_archivo = "/home/flamax75/Descargas/" + nuevo_nombre

# Cambiamos el nombre del archivo
os.rename(ruta_archivo_actual, ruta_nuevo_archivo)

print(f"El archivo ha sido renombrado a '{nuevo_nombre}'.")
