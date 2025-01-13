import os
import yt_dlp

import ImageClient
import ImageHandler
import VidLink
import YouTubeClient

outDir = "out"
imgName = "Image"
imgWidth = 3200

userVids = VidLink.ReadVidLink()
for userVid in userVids:
    print(f"Downloading Video {userVid.vLink}...")
    vFilePath = ""
    while True:
        try:
            vFilePath = YouTubeClient.yDlMp3(userVid.vLink, userVid.vFileName, outDir)
            break
        except yt_dlp.utils.DownloadError:
            print(f"Failed To Download Video {userVid.vLink} - Retrying...")
            continue
    print(f"Finished Downloading Video {userVid.vLink} ({vFilePath}).")

    print(f"Downloading Image {userVid.vLink}...")
    srcImgPath, dstImgPath = "", ""
    while True:
        try:
            srcImgPath, dstImgPath = ImageClient.yDlImage(userVid.vLink, imgName, outDir)
            break
        except yt_dlp.utils.DownloadError:
            print(f"Failed To Download Image {userVid.vLink} - Retrying...")
            continue
    print(f"Finished Downloading Image {userVid.vLink} ({srcImgPath}).")

    print(f"UpScaling Image {userVid.vLink}...")
    ImageHandler.upScaleImage(srcImgPath, dstImgPath, imgWidth)
    print(f"Finished UpScaling Image {userVid.vLink} ({dstImgPath}).")

    print(f"Applying Image To {vFilePath}...")
    ImageHandler.applyImage(dstImgPath, vFilePath, outDir)
    print(f"Finished Applying Image To {vFilePath}.")

    os.remove(srcImgPath)
    os.remove(dstImgPath)

    print()
