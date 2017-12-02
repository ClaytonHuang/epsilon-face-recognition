# coding:utf-8
import cv2

def resizeImage(imagePath,resizeWidth,resizeHeight):

    image=cv2.imread(imagePath)
    res=cv2.resize(image,(resizeWidth,resizeHeight),interpolation=cv2.INTER_CUBIC)
    cv2.imshow('iker',res)
    cv2.imshow('image',image)
    cv2.waitKey(0)
    cv2.destoryAllWindows()