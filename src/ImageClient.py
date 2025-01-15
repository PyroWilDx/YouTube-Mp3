import os
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

    return os.path.join(outDir, vFileName + ".webp"), os.path.join(outDir, vFileName + ".jpg")
