const fs = require("fs");
const path = require("path");
const ffmpeg = require("ffmpeg-static");
const cp = require("child_process");

async function convertToMp3(inputPath, outputPath) {
    return new Promise((resolve, reject) => {
        const ffmpegProcess = cp.spawn(ffmpeg, ["-y", "-i", inputPath, outputPath]);

        ffmpegProcess.on("close", (code) => {
            if (code === 0) {
                resolve();
            } else {
                reject(new Error(`FFmpeg process exited with code ${code}`));
            }
        });
    });
}

async function convertAllToMp3(inputDirectory, outputDirectory) {
    try {
        const convertFilesInDirectory = async (directory) => {
            const allFiles = fs.readdirSync(directory);

            for (const file of allFiles) {
                const filePath = path.join(directory, file);
                const isDirectory = fs.statSync(filePath).isDirectory();

                if (isDirectory) {
                    await convertFilesInDirectory(filePath);
                } else if (path.extname(file) === '.webm' || path.extname(file) === '.mp3') {
                    const outputPath = path.join(outputDirectory, `${path.basename(file, path.extname(file))}.mp3`);
                    await convertToMp3(filePath, outputPath);
                    console.log(`Conversion completa. MP3 guardado en: ${outputPath}`);
                }
            }
        };

        await convertFilesInDirectory(inputDirectory);
        deleteContentFile(inputDirectory);
    } catch (error) {
        console.error("Error:", error.message);
    }
}

const deleteContentFile = (rutaCarpeta) => {
    const carpeta = path.resolve(rutaCarpeta);

    if (fs.existsSync(carpeta)) {
        const filesInfolder = fs.readdirSync(carpeta);

        filesInfolder.forEach(archivo => {
            const routeFile = path.join(carpeta, archivo);

            if (fs.statSync(routeFile).isFile()) {
                fs.unlinkSync(routeFile);
                console.log(`Archivo eliminado: ${routeFile}`);
            } else {
                deleteContentFile(routeFile);
            }
        });
    } else {
        console.log(`La carpeta no existe: ${carpeta}`);
    }
};

const inputDirectory = './webm';
const outputDirectory = './mp3';

if (!inputDirectory || !outputDirectory) {
    console.error("Usage: node convertAllToMp3.js <Input_Directory> <Output_Directory>");
} else {
    console.log("Convirtiendo archivos...")
    convertAllToMp3(inputDirectory, outputDirectory);
}