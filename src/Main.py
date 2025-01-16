import os
import urllib.error
import yt_dlp

import ImageClient
import ImageHandler
import VidLink
import YouTubeClient

outDir = "Out"
imgNameDefault = "Image"
imgWidthDefault = "3200"

userVids = VidLink.ReadVidLink()
print(f"Found {len(userVids)} Videos - Starting Download...")

for userVid in userVids:
    print()

    if os.path.exists(os.path.join(outDir, f"{userVid.vidTitle}.mp3")):
        print(f"Skipping {userVid.vidTitle}.mp3 (Already Exists).")
        continue

    print(f"Downloading Video {userVid.vidLink}...")
    vFilePath = ""
    while True:
        try:
            vFilePath = YouTubeClient.yDlMp3(userVid.vidLink, userVid.vidTitle, outDir)
            break
        except yt_dlp.utils.DownloadError:
            print(f"Failed To Download Video {userVid.vidLink} - Retrying...")
            continue
    print(f"Finished Downloading Video {userVid.vidLink} ({vFilePath}).")

    print(f"Downloading Image {userVid.vidLink}...")
    srcImgPath, dstImgPath = "", ""
    if userVid.imgLink is not None:
        try:
            srcImgPath, dstImgPath = ImageClient.dlImage(userVid.imgLink, outDir)
            print()
        except (Exception,):
            print(f"Failed To Download Image {userVid.imgLink}. Skipping.")
    else:
        while True:
            try:
                srcImgPath, dstImgPath = ImageClient.yDlImage(userVid.vidLink, imgNameDefault, outDir)
                break
            except yt_dlp.utils.DownloadError:
                print(f"Failed To Download Image {userVid.vidLink} - Retrying...")
                continue
    print(f"Finished Downloading Image {userVid.vidLink} ({srcImgPath}).")

    print(f"UpScaling Image {userVid.vidLink}...")
    imgWidth = imgWidthDefault
    if userVid.imgWidth is not None:
        imgWidth = userVid.imgWidth
    ImageHandler.upScaleImage(srcImgPath, dstImgPath, imgWidth)
    print(f"Finished UpScaling Image {userVid.vidLink} ({dstImgPath}).")

    print(f"Applying Image To {vFilePath}...")
    ImageHandler.applyImage(dstImgPath, vFilePath, outDir)
    print(f"Finished Applying Image To {vFilePath}.")

    os.remove(srcImgPath)
    os.remove(dstImgPath)
