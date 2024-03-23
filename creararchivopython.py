nombre_archivo = "nuevo_archivo.txt"

# Contenido que deseas escribir en el archivo
contenido = "Este es el contenido que quiero escribir en el archivo."

try:
    # Abre el archivo en modo de escritura ('w' para escribir, 'a' para añadir al final)
    with open(nombre_archivo, 'w') as archivo:
        # Escribe el contenido en el archivo
        archivo.write(contenido)
    print(f"Se ha creado el archivo '{nombre_archivo}' con éxito.")
except Exception as e:
    print("Se produjo un error al intentar crear el archivo:", e)
