import shutil

ruta_directorio = "/home/flamax75/pomodoro"

# Eliminamos el directorio y su contenido de forma recursiva
shutil.rmtree(ruta_directorio)

print(f"Directorio '{ruta_directorio}' eliminado correctamente.")
