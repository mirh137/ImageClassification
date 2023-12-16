import cv2
import os
import glob
def convertImage(currPath, newPath):
    img = cv2.imread(currPath)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_blur = cv2.GaussianBlur(img_gray, (3,3), 0)
    edges = cv2.Canny(image=img_blur, threshold1=100, threshold2=200)
    cv2.imwrite(newPath, edges)

convertImage("/home/mir/Desktop/PokemonProject/tests/TestImages/greyPokemons/pikachu.jpg", "/home/mir/Desktop/PokemonProject/tests/TestImages/greyPokemons/pikachu.jpg")


# def findFiles():
#     os.chdir("/home/mir/Desktop/PokemonProject/kagglePokemonSet/archive/pokemon")
#     for i in os.listdir():
#         for j in glob.glob(i + "/*"):
#             convertImage(os.getcwd() + "/" + j, "/home/mir/Desktop/PokemonProject/greyscaleSet/archive/pokemon/" + j)
        
# findFiles()