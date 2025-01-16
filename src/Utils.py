def clearExtension(fileName):
    lastDotIndex = fileName.rfind(".")
    if lastDotIndex == -1:
        return fileName
    return fileName[:lastDotIndex]
