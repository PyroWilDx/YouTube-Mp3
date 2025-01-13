import os
import yt_dlp

import Const


def yDlMp3(vLink, vFileName, outDir):
    yDlFilePath = ""

    def pHook(p):
        nonlocal yDlFilePath
        if p["status"] == "finished":
            yDlFilePath = p["info_dict"]["_filename"]
            yDlFilePath = clearExtension(yDlFilePath)
            yDlFilePath += ".mp3"

    yDlOptions = {
        "ffmpeg_location": Const.ffMpeg,
        "format": "bestaudio/best",
        "noplaylist": True,
        "outtmpl": f"{outDir}/%(title)s.%(ext)s",
        "quiet": True,
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "0"
        }],
        "progress_hooks": [pHook]
    }

    with yt_dlp.YoutubeDL(yDlOptions) as yDl:
        yDl.download([vLink])

    if yDlFilePath and vFileName:
        vFilePath = os.path.join(outDir, f"{vFileName}.mp3")
        if not os.path.exists(vFilePath):
            os.rename(yDlFilePath, vFilePath)
            print(f"Renamed File To {vFileName}.mp3.")
            return vFilePath
        else:
            print(f"Couldn't Rename File To {vFileName}.mp3 (It Already Exists).")

    return yDlFilePath


def clearExtension(fileName):
    lastDotIndex = fileName.rfind(".")
    if lastDotIndex == -1:
        return fileName
    return fileName[:lastDotIndex]
