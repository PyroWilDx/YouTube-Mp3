import os
import sys
import yt_dlp

import AudioClient
import ImageClient
import ImageHandler
import Utils
import VidListReader
import YouTubeClient

sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

outDir = "Out"
imgNameDefault = "Image"
imgWidthDefault = "2600"

userVids = VidListReader.ReadVidList()
print(f"Found {len(userVids)} Videos - Starting Download...")

pDelimiter = "======"

for userVid in userVids:
    print()
    print(pDelimiter)

    if os.path.exists(os.path.join(outDir, f"{userVid.vidTitle}.mp3")):
        print(f"Skipping {userVid.vidTitle}.mp3 (Already Exists).")
        continue

    isYouTubeLink = YouTubeClient.isYouTubeLink(userVid.vidLink)

    if not isYouTubeLink:
        vidPath = os.path.join(outDir, f"{Utils.clearExtension(os.path.basename(userVid.vidLink))}.mp3")
        if os.path.exists(vidPath):
            print(f"Skipping {userVid.vidLink} (Already Exists).")
            continue

    print(f"Downloading Video {userVid.vidLink}...")
    vidPath = ""
    if not isYouTubeLink:
        try:
            vidPath = AudioClient.dlAudio(userVid.vidLink, userVid.vidTitle, outDir)
        except (Exception,):
            print(f"Failed To Download Audio {userVid.vidLink}. Skipping.")
            continue
    else:
        while True:
            try:
                vidPath = YouTubeClient.yDlMp3(userVid.vidLink, userVid.vidTitle, outDir)
                break
            except yt_dlp.utils.DownloadError:
                print(f"Failed To Download Video {userVid.vidLink}. Retrying...")
                continue
    print(f"Finished Downloading Video {userVid.vidLink} ({vidPath}).")

    if (not isYouTubeLink) and (not userVid.imgLink):
        continue

    print(f"Downloading Image {userVid.vidLink}...")
    imgPath = ""
    if userVid.imgLink is not None:
        try:
            imgPath = ImageClient.dlImage(userVid.imgLink, outDir)
        except (Exception,):
            print(f"Failed To Download Image {userVid.imgLink}. Skipping.")
            continue
    else:
        while True:
            try:
                imgPath = ImageClient.yDlImage(userVid.vidLink, imgNameDefault, outDir)
                break
            except yt_dlp.utils.DownloadError:
                print(f"Failed To Download Image {userVid.vidLink} - Retrying...")
                continue
    print(f"Finished Downloading Image {userVid.vidLink} ({imgPath}).")

    print(f"UpScaling Image {userVid.vidLink}...")
    imgWidth = imgWidthDefault
    if userVid.imgWidth is not None:
        imgWidth = userVid.imgWidth
    upScaledImgPath = ImageHandler.upScaleImage(imgPath, imgWidth, userVid.imgFormat)
    print(f"Finished UpScaling Image {userVid.vidLink} ({imgPath}).")

    print(f"Applying Image To {vidPath}...")
    ImageHandler.applyImage(upScaledImgPath, vidPath, outDir)
    print(f"Finished Applying Image To {vidPath}.")

    os.remove(imgPath)
    os.remove(upScaledImgPath)

print(pDelimiter)
print("\nPress Enter...")
input()
