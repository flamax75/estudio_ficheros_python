import os
import time


ruta = "untexto.txt"
print(os.path.getatime(ruta))
print(time.ctime(os.path.getatime(ruta)))


print(os.path.getsize(ruta))
print(os.path.isfile(ruta))


print(os.path.isdir(ruta))


print(os.path.isdir(ruta))
print(os.path.ismount(ruta))
ruta_absoluta = os.path.abspath(ruta)
print(os.path.abspath(ruta))
print(os.path.split(ruta_absoluta)[0])
print(os.path.split(ruta_absoluta)[1])
