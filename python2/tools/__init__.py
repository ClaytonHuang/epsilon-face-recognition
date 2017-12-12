# encoding:utf-8

from assembleImage import *

if __name__ == "__main__":

    srcPathList = [
    #     '/Users/huanghaoce/workspace/ARM/人脸数据库/originalPics',
    #     '/Users/huanghaoce/workspace/ARM/亚洲人脸',
    '/Users/huanghaoce/Resources/Images',
        ]
    desPath = '/Users/huanghaoce/Resources/lala'
    assembleImage(srcPathList, desPath);
    # getImageNumber(desPath)
    print "Program end"