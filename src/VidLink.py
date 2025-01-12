def ReadVidLink():
    userVids = []
    with open("VidLink.txt") as vidLinkFile:
        for v in vidLinkFile:
            if len(v) == 0:
                continue

            vSplit = v.split()
            vLink = vSplit[0]
            vFileName = None
            if len(vSplit) >= 2:
                vFileName = " ".join(vSplit[1:])
            userVids.append(Video(vLink, vFileName))
    return userVids


class Video:
    def __init__(self, vLink, vFileName):
        self.vLink = vLink
        self.vFileName = vFileName

    def __str__(self):
        r = self.vLink
        if self.vFileName is not None:
            r += f" - {self.vFileName}"
        return r
