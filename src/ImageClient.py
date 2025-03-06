import os
import requests
import yt_dlp

import Const


def yDlImage(vidLink, vFileName, outDir):
    yDlOptions = {
        "ffmpeg_location": Const.ffMpeg,
        "outtmpl": f"{outDir}/{vFileName}.%(ext)s",
        "quiet": True,
        "skip_download": True,
        "writethumbnail": True
    }

    with yt_dlp.YoutubeDL(yDlOptions) as yDl:
        yDl.download([vidLink])

    imgPath = os.path.join(outDir, f"{vFileName}.webp")
    return imgPath


def dlImage(imgLink, outDir):
    r = requests.get(imgLink, headers=Const.rHeaders, stream=True)

    if r.status_code == 200:
        dlImgPath = os.path.basename(imgLink)
        srcImgPath = os.path.join(outDir, dlImgPath)
        with open(srcImgPath, "wb") as dlImg:
            for chunk in r.iter_content(1024):
                dlImg.write(chunk)
        return srcImgPath
    else:
        raise Exception()
