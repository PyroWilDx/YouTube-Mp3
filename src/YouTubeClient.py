import os
import yt_dlp

import Const


def yDlMp3(vidLink, vidTitle, outDir):
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
        yDl.download([vidLink])

    if vidTitle and yDlFilePath:
        vFilePath = os.path.join(outDir, f"{vidTitle}.mp3")
        if not os.path.exists(vFilePath):
            os.rename(yDlFilePath, vFilePath)
            print(f"Renamed File To {vidTitle}.mp3.")
            return vFilePath
        else:
            print(f"Couldn't Rename File To {vidTitle}.mp3 (It Already Exists).")

    return yDlFilePath


def clearExtension(fileName):
    lastDotIndex = fileName.rfind(".")
    if lastDotIndex == -1:
        return fileName
    return fileName[:lastDotIndex]
