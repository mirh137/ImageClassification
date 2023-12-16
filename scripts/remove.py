import os
import sys
import glob

def removeDirs(file):
    os.chdir("kagglePokemonSetType/archive")
    container = os.scandir("types")
    container2 = []
    for i in container:
        container2.append(i.name)

    f = open("/home/mir/Desktop/PokemonProject/"+str(file), "r")
    lines = f.readlines()
    temp = []
    for i in lines:
        temp.append(i.strip())
    for i in container2:
        if i not in temp:
            os.system("rm -rf pokemon/"+str(i))


def removePNG():
    os.chdir("/home/mir/Desktop/PokemonProject/kagglePokemonSetType/archive/types")
    for file in glob.glob("*/*.GIF"):
        os.remove(file)
        print(file)

removePNG()