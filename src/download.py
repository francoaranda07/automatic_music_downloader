import yt_dlp as youtube_dl
import os
import re
import time

# función para extraer el audio del video
def extractSound(link):
    while True:
        try:
            # Cambiar youtube_dl.YoutubeDL() a yt_dlp.YoutubeDL()
            dataSound = youtube_dl.YoutubeDL().extract_info(url=link, download=False)
            title = dataSound['title']
            title = re.sub(r'[^\w\s]', '', title)  # Eliminar caracteres especiales del título
            fileSound = f"{title}.webm"
            path_to_save = './webm'
            output_path = os.path.join(path_to_save, fileSound)

            # Opciones para yt-dlp
            options = {
                'format': 'bestaudio/best',
                'keepvideo': False,
                'outtmpl': output_path,
            }

            # Descargar el audio usando yt-dlp
            with youtube_dl.YoutubeDL(options) as ydl:
                return ydl.download([dataSound['webpage_url']])
        except youtube_dl.utils.DownloadError as e:
            print(f"Error durante la descarga: {e}")
            print("🔁 Reintentando la descarga en 5 segundos...")
            time.sleep(5)

