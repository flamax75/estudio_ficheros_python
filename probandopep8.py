from pathlib import Path

miau = Path("untexto.txt")

contenido = miau.read_text()

print(contenido)
