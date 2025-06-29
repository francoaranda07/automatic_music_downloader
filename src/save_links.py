import os
import datetime
from colorama import init, Fore, Style
from download import extractSound

# Inicializar colorama
init(autoreset=True)

fileWithLinks = 'youtube_links.txt'
validLink = 'https://www.youtube.com/watch?v=xxxxxxxxxxx'
webmFolder = './webm'
mp3Folder = './mp3'

def log(msg, color=Fore.WHITE):
    timestamp = datetime.datetime.now().strftime("%H:%M:%S")
    print(f"{color}[{timestamp}] {msg}{Style.RESET_ALL}")

def ensure_file_exists(filename):
    if not os.path.exists(filename):
        with open(filename, 'w') as f:
            pass

def create_webm_folder_if_not_exists(folder_route):
    if not os.path.exists(folder_route):
        os.makedirs(folder_route)
        log(f"Carpeta creada: {folder_route} ✅", Fore.GREEN)
    else:
        log(f"La carpeta ya existe: {folder_route} 📂", Fore.CYAN)
        file_in_folder = os.listdir(webmFolder)
        for file in file_in_folder:
            folder_route = os.path.join(webmFolder, file)
            try:
                if os.path.isfile(folder_route):
                    os.remove(folder_route)
                    log(f"Archivo eliminado: {folder_route} 🗑️", Fore.YELLOW)
                elif os.path.isdir(folder_route):
                    os.rmdir(folder_route)
                    log(f"Carpeta eliminada: {folder_route} 🗑️", Fore.YELLOW)
            except Exception as e:
                log(f"No se pudo eliminar {folder_route}: {e}", Fore.RED)

def create_mp3_folder_if_not_exists(folder_route):
    if not os.path.exists(folder_route):
        os.makedirs(folder_route)
        log(f"Carpeta creada: {folder_route} ✅", Fore.GREEN)
    else:
        log(f"La carpeta ya existe: {folder_route} 📂", Fore.CYAN)
        file_in_folder = os.listdir(mp3Folder)
        for file in file_in_folder:
            folder_route = os.path.join(mp3Folder, file)
            try:
                if os.path.isfile(folder_route):
                    os.remove(folder_route)
                    log(f"Archivo eliminado: {folder_route} 🗑️", Fore.YELLOW)
                elif os.path.isdir(folder_route):
                    os.rmdir(folder_route)
                    log(f"Carpeta eliminada: {folder_route} 🗑️", Fore.YELLOW)
            except Exception as e:
                log(f"No se pudo eliminar {folder_route}: {e}", Fore.RED)

def adjust_length(fileWithLinks, validLink):
    youtube_link_length = len(validLink)
    adjusted_lines = []

    with open(fileWithLinks, 'r') as file:
        for line in file:
            line = line.strip()
            if len(line) != youtube_link_length:
                line = line[:youtube_link_length].ljust(youtube_link_length)
                log(f"✂️ Línea ajustada: {line}", Fore.MAGENTA)
            else:
                log(f"✅ Línea válida: {line}", Fore.GREEN)
            adjusted_lines.append(line)

    with open(fileWithLinks, 'w') as file:
        for line in adjusted_lines:
            file.write(line + '\n')
    log("✍️ Archivo guardado con las líneas ajustadas.", Fore.CYAN)

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
    ensure_file_exists(fileWithLinks)
    mylist = []

    try:
        while True:
            youtube_link = input(Fore.YELLOW + "Introduce un enlace de YouTube (o CTRL+C para salir): " + Style.RESET_ALL).strip()

            if len(youtube_link) < len(validLink):
                log("🗑️ Enlace inválido. Demasiado corto.", Fore.RED)
            else:
                sanitized_link = sanitize_link(youtube_link)
                if is_link_already_saved(sanitized_link, fileWithLinks):
                    log("🗑️ -> El enlace ya está guardado.", Fore.RED)
                else:
                    save_links_to_file([sanitized_link], fileWithLinks)
                    log("✅ Enlace guardado", Fore.GREEN)

    except (KeyboardInterrupt, EOFError):
        log("Interrupción detectada. Iniciando descarga...", Fore.CYAN)
        adjust_length(fileWithLinks, validLink)

        with open(fileWithLinks) as f:
            mylist = [line.rstrip('\n') for line in f]

        for link in mylist:
            log(f"Descargando: {link}", Fore.BLUE)
            extractSound(link)

        log("🎶 Descargas finalizadas.", Fore.GREEN)

    finally:
        log("Ejecutando conversión de audio...", Fore.CYAN)
        os.system('node ./convert_audio.js')
        if mylist:
            remove_links_from_file(mylist, fileWithLinks)
            log("Links eliminados del archivo.", Fore.CYAN)
        log("Proceso finalizado. ✅", Fore.GREEN)

if __name__ == "__main__":
    main()
