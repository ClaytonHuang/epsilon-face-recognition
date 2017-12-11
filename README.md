# epsilon-face-recognition
The first ARM algorithm contest of zhejiang university. This repository created by A6 epsilon team.

# Introduction
当前维护的主程序目录为：python2 

## 环境配置
### Required Environment
- python 2.7.12
- numpy
- scipy
- matplotlib   
> 上面三个库，在一般的windows或ubuntu下，直接pip install 即可   
- opencv3.2 （cv2 for python)
> 安装OpenCV3.2, 安装完成后，进入安装后的opencv\build\python路径，选择2.7文件夹，将x64文件夹下的cv2.pyd（pyd文件是一种Python动态模块，可以把他理解为C++中的dll文件），将cv2.pyd 复制到python安装目录\lib\site-packages。
在python的IDLE中   
执行   
```
import cv2
cv2.__version__
```
若输出版本号"3.20"，则OpenCV3 for python配置成功

### 环境测试   
#### 摄像头调用与OpenCV环境  
- 确保笔记本自带摄像头可工作，或连接外置摄像头    
- 在./test文件夹下，运行   
```
python __init__.py
```
- 输出tensorflow的线性模型拟合程序结果，tensorflow的配置成功
- 若输出Video窗口，显示视频流即python & OpenCV方面的环境配置成功
- 点击q键退出视频窗口

## ATTENTION!
- 简单的改动可以直接commit；较大的改动，例如涉及模型变动等请发起Pull Request
- 当commit的文件中包含比较大的文件时，请先上传到百度云盘，并在README.md文档中提供链接，并提供其在程序用的具体调用位置和方式等说明，具体请参考
__训练测试数据集__
中的att_faces训练集

## 训练测试数据集
### att_faces  
- 链接&密码：链接:https://pan.baidu.com/s/1kVxMDAv  密码:ghv1        
- 说明：包含40个人，每人10张不同光照、角度下的人脸头像，.pgm格式      
- 程序调用位置：暂无     

## 提交code到github的方法    
- 在命令行中，执行
``` 
git clone git@github.com:Grandh/epsilon-face-recognition.git    
cd epsilon-face-recognition 
```
进入项目目录
- 创建remote连接    
```
git remote add origin git@github.com:Grandh/epsilon-face-recognition.git 
```
- 准备提交时，建议只提交.py文件    
```
git add *.py
git commit -m "对修改做出的comment"
git push origin master
```
- (PS)若有比较大或认为不确定的改动，建议新建一个分支    
```
git branch new_branch_name
git checkout new_branch_name
```



