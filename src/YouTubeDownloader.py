import yt_dlp
import os

ffMpeg = "bin/ffmpeg.exe"
outDir = "out"


def dlMp3(vLink, vFileName):
    yDlFilePath = ""

    def pHook(p):
        nonlocal yDlFilePath
        if p['status'] == 'finished':
            yDlFilePath = p['info_dict']['_filename']
            yDlFilePath = clearExtension(yDlFilePath)
            yDlFilePath += ".mp3"

    yDlOptions = {
        'ffmpeg_location': ffMpeg,
        'format': 'bestaudio/best',
        'noplaylist': True,
        'outtmpl': f'{outDir}/%(title)s.%(ext)s',
        'quiet': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': "0"
        }],
        'progress_hooks': [pHook]
    }

    with yt_dlp.YoutubeDL(yDlOptions) as yDl:
        yDl.download([vLink])

    if yDlFilePath and vFileName:
        vFilePath = os.path.join(outDir, f"{vFileName}.mp3")
        os.rename(yDlFilePath, vFilePath)
        print(f"Renamed File To {vFilePath}.")
        return vFilePath

    return yDlFilePath


def clearExtension(fileName):
    lastDotIndex = fileName.rfind(".")
    if lastDotIndex == -1:
        return fileName
    return fileName[:lastDotIndex]
