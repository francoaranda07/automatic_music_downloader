import os
import hashlib

def obtener_hash_archivo(ruta_archivo):
    """Calcula el hash de un archivo para identificar duplicados."""
    hash_md5 = hashlib.md5()
    with open(ruta_archivo, "rb") as f:
        for bloque in iter(lambda: f.read(4096), b""):
            hash_md5.update(bloque)
    return hash_md5.hexdigest()

def eliminar_archivos_duplicados(directorio_pendrive):
    archivos_hash = {}
    archivos_eliminados = 0

    for root, _, archivos in os.walk(directorio_pendrive):
        for archivo in archivos:
            ruta_archivo = os.path.join(root, archivo)
            
            # Calcula el hash para verificar duplicados
            hash_archivo = obtener_hash_archivo(ruta_archivo)

            if hash_archivo in archivos_hash:
                # Si el archivo ya existe, eliminarlo
                print(f"Archivo duplicado encontrado y eliminado: {ruta_archivo}")
                os.remove(ruta_archivo)
                archivos_eliminados += 1
            else:
                # Si no existe, guardarlo en el diccionario
                archivos_hash[hash_archivo] = ruta_archivo

    print(f"\nTotal de archivos duplicados eliminados: {archivos_eliminados}")

# Ruta del pendrive
directorio_pendrive = "E:\\"  # Cambia esta ruta según sea necesario

if os.path.exists(directorio_pendrive):
    eliminar_archivos_duplicados(directorio_pendrive)
else:
    print("El pendrive no está conectado o la ruta es incorrecta.")
