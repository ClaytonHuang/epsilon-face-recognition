#-*- coding: utf-8 -*-

import cv2
import os,sys,datetime

from PIL import Image

def datetimeNowToString():
    now = datetime.datetime.now()
    return now.strftime("%Y%m%d-%H%M%S");
'''
函数功能：用opencv haarcascade分类器获取实际的人脸图片
参数： window_name 获取人脸的窗口名称
      path_name 保存人脸图像的文件路径名称，默认为../image/catch-face-byopencv
      camera_idx opencv打开的摄像头id，默认为0
      catch_pic_num 每次读取的人脸图片数，默认为40
'''
def CatchPICFromVideo(window_name="catch-human-face", path_name="../image/catch-face-byopencv", camera_idx = 0, catch_pic_num = 40):
    cv2.namedWindow(window_name)
    
    #视频来源，可以来自一段已存好的视频，也可以直接来自USB摄像头
    cap = cv2.VideoCapture(camera_idx)                
    
    #告诉OpenCV使用人脸识别分类器
    #TODO1，将opencv的分类器路径独立取出，并采用os.join
    opencvInstallPath = ""
    classfier = cv2.CascadeClassifier("/usr/local/share/OpenCV/haarcascades/haarcascade_frontalface_alt2.xml")
    
    #识别出人脸后要画的边框的颜色，RGB格式
    color = (0, 255, 0)

    num = 0    
    path_name = os.path.join(path_name,datetimeNowToString())
    print path_name
    if not os.path.exists(path_name): os.makedirs(path_name)

    while cap.isOpened():
        
        ok, frame = cap.read() #读取一帧数据
        if not ok: break                
    
        grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  #将当前桢图像转换成灰度图像            
        
        #人脸检测，1.2和2分别为图片缩放比例和需要检测的有效点数
        # TODO2，调整这里选择的人脸尺寸
        faceRects = classfier.detectMultiScale(grey, scaleFactor = 1.2, minNeighbors = 3, minSize = (32, 32))
        if len(faceRects) > 0:          #大于0则检测到人脸  

            for faceRect in faceRects:  #单独框出每一张人脸
                x, y, w, h = faceRect                        
                
                #将当前帧保存为图片
                # TODO3，将保存的图片文件夹改为时间戳
                img_name = '%s/%d.jpg'%(path_name, num)                
                image = frame[y - 10: y + h + 10, x - 10: x + w + 10]
                cv2.imwrite(img_name, image)                                
                                
                num += 1                
                if num > (catch_pic_num):   #如果超过指定最大保存数量退出循环
                    break
                
                #画出矩形框
                cv2.rectangle(frame, (x - 10, y - 10), (x + w + 10, y + h + 10), color, 2)

                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(frame,'num:%d' % (num),(x + 30, y + 30), font, 1, (255,0,255),4)                
        
        #超过指定最大保存数量结束程序
        if num > (catch_pic_num): break                
                       
        #显示图像
        cv2.imshow(window_name, frame)        
        c = cv2.waitKey(10)
        if c & 0xFF == ord('q'):
            break        
    
    #释放摄像头并销毁所有窗口
    cap.release()
    cv2.destroyAllWindows() 

if __name__ == '__main__':
    
    CatchPICFromVideo()