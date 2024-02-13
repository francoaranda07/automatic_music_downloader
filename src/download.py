import youtube_dl #libreria que permite descargar y convertir los videos
import os
import sys
import re
import time
#funcion para extrer el audio del video
def extractSound(link):

    while True:
        try:
            dataSound = youtube_dl.YoutubeDL().extract_info(url=link, download=False)
            title = dataSound['title']
            title = re.sub(r'[^\w\s]', '', title)
            fileSound = f"{title}.webm"
            path_to_save = './webm'
            output_path = os.path.join(path_to_save, fileSound)
            options = {
                'format': 'bestaudio/best',
                'keepvideo': False,
                'outtmpl': output_path,
            }

            with youtube_dl.YoutubeDL(options) as ydl:
                return ydl.download([dataSound['webpage_url']])
        except youtube_dl.utils.DownloadError as e:
            print(f"Error durante la descarga: {e}")
            print("🔁 Reintentando la descarga en 5 segundos...")
            time.sleep(5)
