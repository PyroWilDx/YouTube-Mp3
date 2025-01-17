import os
import requests
import shutil
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

    srcImgPath = os.path.join(outDir, f"{vFileName}.webp")
    dstImgPath = os.path.join(outDir, f"{vFileName}.png")
    return srcImgPath, dstImgPath


def dlImage(imgLink, outDir):
    r = requests.get(imgLink, headers=Const.rHeaders, stream=True)

    if r.status_code == 200:
        dlImgPath = os.path.basename(imgLink)
        srcImgPath = os.path.join(outDir, dlImgPath)
        dstImgPath = os.path.join(outDir, f"{dlImgPath}.png")

        with open(srcImgPath, 'wb') as dlImg:
            for chunk in r.iter_content(1024):
                dlImg.write(chunk)

        return srcImgPath, dstImgPath
    else:
        raise Exception()
