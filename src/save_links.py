import os
from download import extractSound

fileWithLinks = 'youtube_links.txt'
validLink = 'https://www.youtube.com/watch?v=xxxxxxxxxxx'
webmFolder = './webm'
mp3Folder = './mp3'

def create_webm_folder_if_not_exists(folder_route):
    if not os.path.exists(folder_route):
        os.makedirs(folder_route)
        print(f"Carpeta creada: {folder_route} ✅")
    else:
        print(f"La carpeta ya existe: {folder_route} 📂")
        # Eliminar contenido de la carpeta
        file_in_folder = os.listdir(webmFolder)
        for file in file_in_folder:
            folder_route = os.path.join(webmFolder, file)
            try:
                if os.path.isfile(folder_route):
                    os.remove(folder_route)
                    print(f"Archivo eliminado: {folder_route} 🗑️")
                elif os.path.isdir(folder_route):
                    os.rmdir(folder_route)
                    print(f"Carpeta eliminada: {folder_route} 🗑️")
            except Exception as e:
                print(f"No se pudo eliminar {folder_route}: {e}")

def create_mp3_folder_if_not_exists(folder_route):
    if not os.path.exists(folder_route):
        os.makedirs(folder_route)
        print(f"Carpeta creada: {folder_route} ✅")
    else:
        print(f"La carpeta ya existe: {folder_route} 📂")
        # Eliminar contenido de la carpeta
        file_in_folder = os.listdir(mp3Folder)
        for file in file_in_folder:
            folder_route = os.path.join(mp3Folder, file)
            try:
                if os.path.isfile(folder_route):
                    os.remove(folder_route)
                    print(f"Archivo eliminado: {folder_route} 🗑️")
                elif os.path.isdir(folder_route):
                    os.rmdir(folder_route)
                    print(f"Carpeta eliminada: {folder_route} 🗑️")
            except Exception as e:
                print(f"No se pudo eliminar {folder_route}: {e}")

def adjust_length(fileWithLinks, validLink):
    # Longitud de un enlace de YouTube válido
    youtube_link_length = len(validLink)

    # Lista para almacenar las líneas ajustadas
    adjusted_lines = []

    # Abrir el archivo de entrada y leer cada línea
    with open(fileWithLinks, 'r') as file:
        for line in file:
            # Eliminar espacios en blanco al inicio y al final de la línea
            line = line.strip()

            # Ajustar la longitud de la línea si es necesario
            if len(line) != youtube_link_length:
                # Si la longitud es diferente, truncar o rellenar la línea
                line = line[:youtube_link_length].ljust(youtube_link_length)
                print("✂️ Línea ajustada:", line)
            else:
                print("✅ Línea válida:", line)

            # Agregar la línea ajustada a la lista
            adjusted_lines.append(line)

    # Escribir las líneas ajustadas de vuelta al archivo
    with open(fileWithLinks, 'w') as file:
        for line in adjusted_lines:
            file.write(line + '\n')

    print("✍️ Archivo guardado con las líneas ajustadas.")

def sanitize_link(link):
    return link.split('&')[0] if '&' in link else link

def save_links_to_file(links, filename):
    with open(filename, 'a') as file:
        file.write('\n'.join(links) + '\n')

def remove_links_from_file(links, filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    with open(filename, 'w') as file:
        for line in lines:
            if line.strip() not in links:
                file.write(line)

def is_link_already_saved(link, filename):
    with open(filename, 'r') as file:
        return link in file.read()

def main():
    create_webm_folder_if_not_exists(webmFolder)
    create_mp3_folder_if_not_exists(mp3Folder)
    try:
        while True:
            youtube_link = input("Introduce un enlace de YouTube (o CTRL+C para salir): ").strip()

            if len(youtube_link) < len(validLink):
                print("🗑️ Enlace inválido. Demasiado corto.")
            else:
                sanitized_link = sanitize_link(youtube_link)
                filename = fileWithLinks

                if is_link_already_saved(sanitized_link, filename):
                    print("🗑️ -> El enlace ya está guardado.")
                else:
                    save_links_to_file([sanitized_link], filename)
                    print("✅ Enlace guardado")

    except (KeyboardInterrupt, EOFError):
        print("\n--------------------------------↓")
        print("Iniciando la descarga")
        adjust_length(fileWithLinks, validLink)
        with open(fileWithLinks) as f:
            mylist = [line.rstrip('\n') for line in f]
        
        for link in mylist:
            print(link)
            extractSound(link)
        print("\n")
        print("Descargados")
        print("----------------------------------↓")

    finally:
        # Ejecutar convert_audio.js con Node.js
        os.system('node .\\src\\convert_audio.js')
        remove_links_from_file(mylist, fileWithLinks)

if __name__ == "__main__":
    main()
