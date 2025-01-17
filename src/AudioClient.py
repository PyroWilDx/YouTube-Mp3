import os
import requests
import subprocess

import Const
import Utils


def dlAudio(vidLink, vidTitle, outDir):
    r = requests.get(vidLink, headers=Const.rHeaders, stream=True)

    if r.status_code == 200:
        dlVidPath = os.path.basename(vidLink)
        with open(dlVidPath, 'wb') as dlVid:
            for chunk in r.iter_content(1024):
                dlVid.write(chunk)
    else:
        raise Exception()

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
