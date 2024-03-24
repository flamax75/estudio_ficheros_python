import os

# Nombre del directorio que deseas crear
nombre_directorio = "pruebamkdir"

# Ruta donde deseas crear el directorio
ruta = "/home/flamax75"

# Combinamos la ruta con el nombre del directorio
ruta_completa = os.path.join(ruta, nombre_directorio)

# Creamos el directorio
os.makedirs(ruta_completa)

print(f"Directorio '{nombre_directorio}' creado en '{ruta}'")
