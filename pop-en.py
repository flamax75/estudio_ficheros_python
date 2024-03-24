from subprocess import Popen


salida = Popen(["ls", "-lha"])
salida.wait()
