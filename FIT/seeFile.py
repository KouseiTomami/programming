import cv2
import numpy as np

def loadImage():
    img = cv2.imread('./result/output.bmp')
    print(img)

if __name__ == '__main__':
    loadImage()