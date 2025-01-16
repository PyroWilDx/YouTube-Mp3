import os
import yt_dlp

import Const
import Utils


def isYouTubeLink(vidLink):
    return ("youtube.com/" in vidLink) or ("youtu.be/" in vidLink)


def yDlMp3(vidLink, vidTitle, outDir):
    yDlVidPath = ""

    def pHook(p):
        nonlocal yDlVidPath
        if p["status"] == "finished":
            yDlVidPath = p["info_dict"]["_filename"]
            yDlVidPath = Utils.clearExtension(yDlVidPath)
            yDlVidPath += ".mp3"

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

    if vidTitle and yDlVidPath:
        vidPath = os.path.join(outDir, f"{vidTitle}.mp3")
        if not os.path.exists(vidPath):
            os.rename(yDlVidPath, vidPath)
            print(f"Renamed File To {vidTitle}.mp3.")
            return vidPath
        else:
            print(f"Couldn't Rename File To {vidTitle}.mp3 (It Already Exists).")

    return yDlVidPath
