import os

from pathlib import Path

miau = Path("untexto.txt")

contenido = miau.read_text()

existe = os.access("untexto.txt", os.F_OK)
permiso_ejecucion = os.access("untexto.txt", os.X_OK)
permiso_lectura = os.access("untexto.txt", os.R_OK)
permiso_escritura = os.access("untexto.txt", os.W_OK)


print(permiso_escritura)
print(permiso_lectura)
print(permiso_ejecucion)
print(existe)

print(contenido)
