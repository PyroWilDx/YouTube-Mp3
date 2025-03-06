import os
import shutil
import subprocess
import zipfile


def buildExecutable():
    buildCommand = [
        "pyinstaller", "--onefile", "--noconfirm", "--icon=NONE", "src/Main.py"
    ]
    subprocess.run(buildCommand, check=True)


def createZip():
    zipFilename = "YouTube-Mp3.zip"

    if os.path.exists(zipFilename):
        os.remove(zipFilename)

    distExe = "dist/Main.exe"
    binFolder = "bin"
    outFolder = "Out"
    vidListTxt = "VidList.txt"

    if not os.path.exists(outFolder):
        os.makedirs(outFolder)

    with zipfile.ZipFile(zipFilename, "w", zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(distExe, "YouTube-Mp3.exe")

        for foldername, subfolders, filenames in os.walk(binFolder):
            for filename in filenames:
                filePath = os.path.join(foldername, filename)
                zipf.write(filePath, os.path.join(binFolder, os.path.relpath(filePath, binFolder)))

        zipf.write(outFolder, outFolder)
        zipf.write(vidListTxt, vidListTxt)


def cleanUp():
    pathsToRemove = ["build", "dist", "Main.spec"]

    for p in pathsToRemove:
        if os.path.exists(p):
            if os.path.isdir(p):
                shutil.rmtree(p)
            else:
                os.remove(p)


def Main():
    try:
        buildExecutable()
        createZip()
    finally:
        cleanUp()


Main()
