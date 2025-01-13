import os

import ImageClient
import VidLink
import YouTubeClient

outDir = "out"
imgName = "Image"

userVids = VidLink.ReadVidLink()
for userVid in userVids:
    print(f"Downloading Video {userVid.vLink}...")
    vFilePath = YouTubeClient.yDlMp3(userVid.vLink, userVid.vFileName, outDir)
    print(f"Finished Downloading Video {userVid.vLink} ({vFilePath}).")

    print(f"Downloading Image {userVid.vLink}...")
    iFilePath = ImageClient.yDlImage(userVid.vLink, imgName, outDir)
    print(f"Finished Downloading Image {userVid.vLink} ({iFilePath}).")

    print(f"Upscaling Image {userVid.vLink}...")

    print(f"Finished Upscaling Image {userVid.vLink}.")

    # os.remove(iFilePath)

    print()
