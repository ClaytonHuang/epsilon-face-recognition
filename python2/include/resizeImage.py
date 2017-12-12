# coding:utf-8
import os,sys
import numpy as np
import cv2 

IMAGE_SIZE = 64

'''
函数功能：将图片缩放至长宽相等
'''
def resizeImage(image,height = IMAGE_SIZE, width = IMAGE_SIZE):

    top, bottom, left, right = (0,0,0,0)
    # 获取图像的长宽
    h, w, _ = image.shape
    print h,w
    longestEdge = max(h,w)

    if (h < longestEdge):
        dh = longestEdge - h
        top = dh // 2
        bottom = dh - top
    elif (w < longestEdge):
        dw = longestEdge - w
        left = dw // 2
        right = dw - left 
    
    constant = cv2.copyMakeBorder(image, top, bottom, left, right, cv2.BORDER_CONSTANT, value = [0,0,0])
    return cv2.resize(constant,(height,width))


'''
函数功能：读取相应的人脸图片，转为等长宽图片后缩放保存，并记录标记
注意：这里读取的人脸图像保存的文件夹是区分人脸标记的来源
'''
def resizeImageGetLabel(path_name):    

    images = []
    labels = [] 
    for dir_item in os.listdir(path_name):
        
        full_path = os.path.abspath(os.path.join(path_name, dir_item))
        if os.path.isdir(full_path): 
            read_path(full_path)
        else:  
            if dir_item.endswith('.jpg'):  # 只支持.jpg结尾
                image = cv2.imread(full_path)                
                image = resizeImage(image)
                images.append(image)   

                # TODO：对标签进行一定的处理             
                labels.append(path_name)                                

    return images,labels
    
'''
从指定路径读取训练数据
'''
def load_dataset(path_name):
    
    images,labels = read_path(path_name)    
    #将输入的所有图片转成四维数组，尺寸为(图片数量*IMAGE_SIZE*IMAGE_SIZE*3 
    images = np.array(images)
    print(images.shape)    
    
    # 将输入的图像标签化
    labels = np.array([])    
    
    return images, labels