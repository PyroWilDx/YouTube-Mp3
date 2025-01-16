import os
import subprocess
import wget

import Const
import Utils


def dlAudio(vidLink, vidTitle, outDir):
    wget.download(vidLink)

    dlVidPath = os.path.basename(vidLink)
    if vidTitle:
        vidPath = os.path.join(outDir, f"{vidTitle}.mp3")
    else:
        vidPath = os.path.join(outDir, f"{Utils.clearExtension(dlVidPath)}.mp3")

    cmd = [Const.ffMpeg,
           "-i", dlVidPath,
           "-q:a", "0",
           vidPath]
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    os.remove(dlVidPath)

    return vidPath
