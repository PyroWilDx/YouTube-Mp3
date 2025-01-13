import os

import ImageClient
import ImageScaler
import VidLink
import YouTubeClient

outDir = "out"
imgName = "Image"
imgWidth = 3200

userVids = VidLink.ReadVidLink()
for userVid in userVids:
    print(f"Downloading Video {userVid.vLink}...")
    vFilePath = YouTubeClient.yDlMp3(userVid.vLink, userVid.vFileName, outDir)
    print(f"Finished Downloading Video {userVid.vLink} ({vFilePath}).")

    print(f"Downloading Image {userVid.vLink}...")
    srcImgPath, dstImgPath = ImageClient.yDlImage(userVid.vLink, imgName, outDir)
    print(f"Finished Downloading Image {userVid.vLink} ({srcImgPath}).")

    print(f"Upscaling Image {userVid.vLink}...")
    ImageScaler.upScaleImage(srcImgPath, dstImgPath, imgWidth)
    print(f"Finished Upscaling Image {userVid.vLink} ({dstImgPath}).")

    # os.remove(srcImgPath)
    # os.remove(dstImgPath)

    print()
