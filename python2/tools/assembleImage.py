# encoding:utf-8
import os,shutil

'''
函数功能：将训练集中的所有图片，复制到目标文件夹中
输入参数: [(src,des),(src1,des1)]
'''
# TODO 调整保存的图片文件名不重复
def assembleImage(srcPathList,desPath,endWith="jpg"):

    if not os.path.exists(desPath):
        print desPath + "is not exists, create it now"
        os.makedirs(desPath)

    fileCount = 1
    for srcPath in srcPathList:
        
        if not os.path.exists(srcPath):
            print srcPath + " is not exists"
            continue

        
        for root,dir,files in os.walk(srcPath):

            for file in files:
                try:
                    endMark = file.split(".")[-1]
                    if endMark != endWith: continue
                    filePath = os.path.join(root,file);
                    desFilePath = os.path.join(desPath,"%d" % fileCount + "."+endMark)
                    shutil.copy(filePath,desFilePath)
                    fileCount += 1
                except Exception,e:
                    print file 
                    print e
                    
    print desPath + "中共有图片%d张" % fileCount
            
def getImageNumber(path,endWith="jpg"):
    fileList = []
    for root,dir,files in os.walk(path):
        for file in files:
            if not (file.split(".")[-1] == endWith): continue
            fileList.append(file)
    print path + "中共有图片%d张" % len(fileList)

def randomAssignImage(path):
    pass