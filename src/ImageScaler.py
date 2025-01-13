import subprocess


def upScaleImage(srcImgPath, dstImgPath, w):
    cmd = ["bin/UpScayl/upscayl-bin.exe"]

    cmd.extend(["-i", srcImgPath])
    cmd.extend(["-o", dstImgPath])
    cmd.extend(["-n", "realesr-animevideov3-x4"])
    cmd.extend(["-w", str(w)])

    subprocess.run(cmd)
