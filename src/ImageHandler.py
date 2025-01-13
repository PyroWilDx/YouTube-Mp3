import os
import subprocess

import Const


def upScaleImage(srcImgPath, dstImgPath, w):
    cmd = ["bin/UpScayl/upscayl-bin.exe"]

    cmd.extend(["-i", srcImgPath])
    cmd.extend(["-o", dstImgPath])
    cmd.extend(["-n", "realesr-animevideov3-x4"])
    cmd.extend(["-w", str(w)])

    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


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
