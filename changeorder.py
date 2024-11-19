import os
import random

# Configuración: Define la ruta del pendrive aquí
pendrive_path = "F:\\"  # Cambia esta ruta según sea necesario
# Si estás en Windows, usa algo como: pendrive_path = "D:/"

# Lista de extensiones válidas para identificar archivos de música
extensiones_validas = [".mp3"]

def renombrar_canciones_con_prefijo(directorio_pendrive, extensiones_validas):
    """Renombra canciones añadiendo un prefijo numérico aleatorio."""
    # Verificar si la ruta del pendrive es válida
    if not os.path.exists(directorio_pendrive):
        print(f"La ruta especificada no existe: {directorio_pendrive}")
        return

    # Listar archivos en el directorio con extensiones válidas
    canciones = [
        archivo for archivo in os.listdir(directorio_pendrive)
        if os.path.isfile(os.path.join(directorio_pendrive, archivo)) and archivo.lower().endswith(tuple(extensiones_validas))
    ]

    if not canciones:
        print("No se encontraron canciones en el directorio especificado.")
        return

    # Mezclar canciones aleatoriamente
    random.shuffle(canciones)

    # Renombrar canciones conservando el nombre original
    for i, cancion in enumerate(canciones, start=1):
        # Obtener la extensión del archivo
        nombre_base, extension = os.path.splitext(cancion)

        # Nueva ruta con prefijo numérico y el nombre original
        nuevo_nombre = f"{i:03} - {nombre_base}{extension}"
        nueva_ruta = os.path.join(directorio_pendrive, nuevo_nombre)
        ruta_actual = os.path.join(directorio_pendrive, cancion)

        # Renombrar archivo
        os.rename(ruta_actual, nueva_ruta)
        print(f"Renombrado: {ruta_actual} -> {nueva_ruta}")

    print("\nRenombrado completado. Las canciones tienen un prefijo numérico aleatorio.")

# Ejecutar el script
renombrar_canciones_con_prefijo(pendrive_path, extensiones_validas)
