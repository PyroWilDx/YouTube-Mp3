import os
import yt_dlp

import AudioClient
import ImageClient
import ImageHandler
import Utils
import VideoListReader
import YouTubeClient

outDir = "Out"
imgNameDefault = "Image"
imgWidthDefault = "3200"

userVids = VideoListReader.ReadVideoList()
print(f"Found {len(userVids)} Videos - Starting Download...")

for userVid in userVids:
    print()

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
    srcImgPath, dstImgPath = "", ""
    if userVid.imgLink is not None:
        try:
            srcImgPath, dstImgPath = ImageClient.dlImage(userVid.imgLink, outDir)
        except (Exception,):
            print(f"Failed To Download Image {userVid.imgLink}. Skipping.")
            continue
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

    print(f"Applying Image To {vidPath}...")
    ImageHandler.applyImage(dstImgPath, vidPath, outDir)
    print(f"Finished Applying Image To {vidPath}.")

    os.remove(srcImgPath)
    os.remove(dstImgPath)
