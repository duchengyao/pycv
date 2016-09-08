# -*- coding: utf-8 -*-

# 使用openCV抓取视频
# 空格-->>截图，ESC-->>退出。
# 代码修改自 http://blog.csdn.net/tanmengwen/article/details/41892977

import cv2.cv as cv

import time

if __name__ == '__main__':

    cv.NamedWindow("camRra", 1)
    capture = cv.CaptureFromCAM(0)            #开启摄像头
    # capture = cv.CaptureFromFile("Video.avi")  # 打开一个视频文件

    num = 0;
    while True:
        img = cv.QueryFrame(capture)
        cv.ShowImage("camera", img)

        key = cv.WaitKey(1) & 0xFF

        if key == 27:
            break
        if key == ord(' '):
            num = num + 1
            filename = "frmaes_%s.jpg" % num
            cv.SaveImage(filename, img)

    del (capture)
    cv.DestroyWindow("camera")