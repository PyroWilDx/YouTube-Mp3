import VidLink
import YouTubeDownloader

userVids = VidLink.ReadVidLink()
for userVid in userVids:
    print(f"Downloading {userVid.vLink}...")
    YouTubeDownloader.dlMp3(userVid.vLink, userVid.vFileName)
    print(f"Finished Downloading {userVid.vLink}.")

    print(f"Upscaling {userVid.vLink} Image...")

    print(f"Finished Upscaling {userVid.vLink} Image.")
