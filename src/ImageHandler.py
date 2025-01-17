import os
import subprocess

import Const
import Utils


def upScaleImage(srcImgPath, dstImgPath, imgWidth):
    cmd = [Const.upScayl,
           "-i", srcImgPath,
           "-o", dstImgPath,
           "-n", "realesr-animevideov3-x4",
           "-w", imgWidth]
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    upScaledImgPath = f"{Utils.clearExtension(dstImgPath)}.jpg"
    cmd = [Const.ffMpeg,
           "-i", dstImgPath,
           "-q:v", "0",
           upScaledImgPath]
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    return upScaledImgPath


def applyImage(imgPath, vidPath, outDir):
    tmpVidPath = os.path.join(outDir, "Tmp.mp3")
    os.rename(vidPath, tmpVidPath)

    cmd = [Const.ffMpeg,
           "-i", tmpVidPath,
           "-i", imgPath,
           "-map",
           "0:0",
           "-map",
           "1:0",
           "-c",
           "copy",
           "-id3v2_version",
           "3",
           vidPath]
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    os.remove(tmpVidPath)
