import os
import yt_dlp

import Const


def yDlImage(vLink, vFileName, outDir):
    yDlOptions = {
        "ffmpeg_location": Const.ffMpeg,
        "outtmpl": f"{outDir}/{vFileName}.%(ext)s",
        "quiet": False,
        "skip_download": True,
        "writethumbnail": True
    }

    with yt_dlp.YoutubeDL(yDlOptions) as yDl:
        yDl.download([vLink])

    return os.path.join(outDir, vFileName + ".webp")
