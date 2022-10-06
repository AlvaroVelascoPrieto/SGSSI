from os import listdir
from os.path import isfile, join, splitext
import hashlib

FILE_FORMAT = input("Introduce la extension de los archivos a hashear(.jpg,.png,...): ")
HASH = input("Introduce el hash a encontrar: ")
path = input("Introduce la ubicacion de la carpeta que contiene los archivos: ")
files = [f for f in listdir(path) if isfile(join(path, f)) and splitext(f)[1] == FILE_FORMAT]

fileHash = ""
encontrado = False
def es_hash(filepath):
        encontrado = False

        with open(filepath, 'rb') as f:
                md5 = hashlib.md5(f.read())
                myhash = md5.hexdigest()
                if myhash == HASH:
                        encontrado = True

        return encontrado

for f in files:
	encontrado = es_hash(join(path, f))

	if(encontrado):
		fieHash = f
		print(f"Se ha encontrado el archivo correspondiente al hash dado. Archivo: {f}")
		break
