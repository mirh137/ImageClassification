import cv2
import os
import glob
import sys
def convert(path):
    pngIm = cv2.imread(path);
    filename = path[:-4] + ".jpg"
    if(cv2.imwrite(filename, pngIm, [int(cv2.IMWRITE_JPEG_QUALITY), 100])):
        os.remove(path)
    else:
        print("File {} not converted".format(path))

def findFiles(path):
    os.chdir(path)
    for file in glob.glob("*.gif"):
        # convert(file)
        os.remove(file)


def readFile(filePath):
    f = open(filePath, "r")
    lines = f.readlines()
    for line in lines:
        path = "/home/mir/Desktop/PokemonProject/kagglePokemonSet/archive/pokemon/" + line.strip()
        findFiles(path)
    f.close()

readFile(sys.argv[1])