import os
import subprocess

import Const


def upScaleImage(imgPath, imgWidth, imgFormat):
    upScaledImgPathPng = f"{imgPath}.png"
    cmd = [Const.upScayl,
           "-i", imgPath,
           "-o", upScaledImgPathPng,
           "-n", "realesr-animevideov3-x4",
           "-w", imgWidth]
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    if imgFormat != "png":
        if imgFormat:
            upScaledImgPath = f"{upScaledImgPathPng}.{imgFormat}"
        else:
            upScaledImgPath = f"{upScaledImgPathPng}.jpg"

        cmd = [Const.ffMpeg,
               "-i", upScaledImgPathPng,
               "-q:v", "0",
               upScaledImgPath]
        subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        os.remove(upScaledImgPathPng)

        return upScaledImgPath

    return upScaledImgPathPng


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
