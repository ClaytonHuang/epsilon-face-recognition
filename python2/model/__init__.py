# coding:utf-8
from resizeImage import *
import cv2

if __name__ == "__main__":

    image=cv2.imread("../images/face-test-image/wuyanzu.jpg")
    #cv2.imshow("wyz",image)
    cubeImage = resizeImage(image)
    cv2.imshow("cube",cubeImage)
    cv2.waitKey(0)  # 点击Esc键退出
    cv2.destoryAllWindows()
