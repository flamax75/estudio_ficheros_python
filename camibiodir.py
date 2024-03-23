import os

# Directorio al que quieres cambiar
nuevo_directorio = "/home/flamax75"

try:
    # Cambiar el directorio de trabajo
    os.chdir(nuevo_directorio)
    print("Directorio cambiado correctamente.")
except FileNotFoundError:
    print("El directorio especificado no existe.")
except PermissionError:
    print("No tienes permiso para acceder al directorio.")
except Exception as e:
    print("Se produjo un error:", e)
