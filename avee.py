from pathlib import Path

# Crear una ruta al archivo "ejemplo.txt" en el directorio actual
ruta = Path("ejemplo.txt")

# Verificar si el archivo existe
if ruta.exists():
    print("El archivo existe.")
else:
    print("El archivo no existe.")
