import os
import shutil
import wget
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
    wget.download(imgLink)

    dlImgPath = os.path.basename(imgLink)
    srcImgPath = os.path.join(outDir, dlImgPath)
    dstImgPath = os.path.join(outDir, f"{dlImgPath}.png")

    shutil.move(dlImgPath, str(srcImgPath))

    return srcImgPath, dstImgPath
