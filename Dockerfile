# Usamos una imagen base que incluya Node.js y Python
FROM node:18.18.0-slim

# Instalamos Python y herramientas necesarias
RUN apt-get update && apt-get install -y python3 python3-pip python3-venv python3-dev

# Definimos el directorio de trabajo dentro del contenedor
WORKDIR /

# Copiamos los archivos necesarios al directorio de trabajo del contenedor
COPY . .

# Instalamos las dependencias de Node.js
COPY package.json package-lock.json ./
RUN npm ci --ignore-scripts --no-cache

# Creamos un entorno virtual para instalar las dependencias de Python
RUN python3 -m venv /venv
ENV PATH="/venv/bin:$PATH"

# Instalamos las dependencias de Python dentro del entorno virtual
COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

# Comando por defecto para ejecutar la aplicación (tu script .ps1)
CMD ["./download_music.ps1"]
