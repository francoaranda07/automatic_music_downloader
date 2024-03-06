# Descargador Automático de Música de YouTube 🎵🚀

Este proyecto proporciona una solución automatizada para descargar música de YouTube utilizando enlaces proporcionados por el usuario. Simplemente, ingresa los enlaces de YouTube al archivo `youtube_links.txt` o directamente en la consola, y el script se encargará de descargar los archivos de audio y convertirlos a formato mp3.

## Uso con Docker 🐳

1. **Clona este repositorio** o descarga el archivo ZIP.

2. **Asegúrate de tener Docker instalado** en tu sistema. Puedes encontrar instrucciones de instalación para [Windows](https://docs.docker.com/desktop/install/) y [Linux](https://docs.docker.com/engine/install/).

3. **Construye la imagen Docker** ejecutando el siguiente comando en la línea de comandos dentro del directorio raíz del proyecto:

   ```bash
   docker build -t download_music .


## Uso 🚀


1. **Ejecuta el script PowerShell** `docker run -it download_music` en la línea de comandos:


2. **Una vez que hayas ingresado todos los enlaces**, el script comenzará a descargar los archivos de audio en formato `.webm` en una carpeta llamada `webm`.

3. **Después de que se completen todas las descargas**, se llamará al script JavaScript `convert_audio.js`. Este script convertirá todos los archivos de audio `.webm` en formato `.mp3` y los guardará en una carpeta llamada `mp3`.

4. ¡Listo! Ahora puedes encontrar tus canciones descargadas y convertidas en la carpeta `mp3`.

## Notas ℹ️

- **Asegúrate de tener una conexión a internet estable** durante el proceso de descarga.
- **No olvides respetar los derechos de autor** y los términos de servicio de YouTube al descargar contenido.
- **Este script está destinado únicamente para uso personal** y no comercial.

¡Disfruta de tu música descargada desde YouTube de forma rápida y sencilla! 🎶🔥

- [Linkedin](http://linkedin.com/in/franco-aranda-054a911b6)
