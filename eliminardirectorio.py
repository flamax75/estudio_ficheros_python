import os

ruta_directorio = "/home/flamax75/pomodoro"

# Verificamos si el directorio existe antes de intentar eliminarlo
if os.path.exists(ruta_directorio):
    # Eliminamos el directorio
    os.rmdir(ruta_directorio)
    print(f"Directorio '{ruta_directorio}' eliminado correctamente.")
else:
    print(f"El directorio '{ruta_directorio}' no existe.")
