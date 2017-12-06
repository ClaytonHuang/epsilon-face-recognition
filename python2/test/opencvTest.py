# coding:utf-8 
import cv2
from PIL import Image

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

'''
- 测试摄像头和配置环境
- 在当前目录下执行 python __init__.py 0
- 上面的0对应opencv中camera的id，作为系统参数sys.argv[1]输入
'''

def CatchUsbVideo(window_name="Vedio"):
    cv2.namedWindow(window_name)
    # 视频来源
    # 可以直接来自USB摄像头，也可换为视频
    camera_idx = 0
    cap = cv2.VideoCapture(camera_idx)        
        
    while cap.isOpened():
        ok, frame = cap.read() #读取一帧数据
        if not ok:break                    
                        
        #显示图像并等待10毫秒按键输入，输入‘q’退出程序
        cv2.imshow(window_name, frame)
        c = cv2.waitKey(10)
        if c & 0xFF == ord('q'):
            break        
    
    #释放摄像头并销毁所有窗口
    cap.release()
    cv2.destroyAllWindows() 
