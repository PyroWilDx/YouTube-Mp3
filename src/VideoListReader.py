import shlex


def ReadVideoList():
    userVids = []
    with open("VideoList.txt") as vidLinkFile:
        for v in vidLinkFile:
            if len(v) == 0 or v[0] == "\n":
                continue
            if v.startswith("#"):
                continue

            vSplit = shlex.split(v)
            vidLink = vSplit[0]
            userVid = ReadParams(Video(vidLink), vSplit[1:])
            userVids.append(userVid)
    return userVids


def ReadParams(userVid, vParams):
    for vParam in vParams:
        pName, pValue = vParam.split("=", 1)
        if pName == "Title":
            userVid.vidTitle = pValue
        elif pName == "ImgLink":
            userVid.imgLink = pValue
        elif pName == "ImgWidth":
            userVid.imgWidth = pValue
    return userVid


class Video:
    def __init__(self, vidLink):
        self.vidLink = vidLink
        self.vidTitle = None
        self.imgLink = None
        self.imgWidth = None

    def __str__(self):
        r = self.vidLink
        if self.vidTitle is not None:
            r += f" | Title={self.vidTitle}"
        if self.imgLink is not None:
            r += f" | ImgLink={self.imgLink}"
        if self.imgWidth is not None:
            r += f" | ImgWidth={self.imgWidth}"
        return r