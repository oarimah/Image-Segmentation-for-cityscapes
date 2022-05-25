import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
 
# https://docs.opencv.org/4.x/d7/d4d/tutorial_py_thresholding.html
 
img = cv.imread('./input3.png',0)
 
plt.imshow(img, 'gray')
plt.show()
 
img = cv.medianBlur(img, 1)
ret,th1 = cv.threshold(img,85,255,cv.THRESH_BINARY)
ret,th2 = cv.threshold(img,90,255,cv.THRESH_BINARY)
ret,th3 = cv.threshold(img,95,255,cv.THRESH_BINARY)
ret,th4 = cv.threshold(img,100,255,cv.THRESH_BINARY)
 
titles = ['Global Thresholding (t = 85)', 'Global Thresholding (t = 90)',
            'Global Thresholding (t = 95)',  'Global Thresholding (t = 100)']
images = [th1, th2, th3, th4]
for i in range(4):
    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([])
plt.show()
 
th1 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY,11,2)
th2 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY,15,2)
th3 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY,25,2)
th4 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY,39,2)
 
titles = ['Block size: 11', 'Block size: 15', 'Block size: 25', 'Block size: 39',]
images = [th1, th2, th3, th4]
for i in range(4):
    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([])
plt.show()
 
th1 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY,15,2)
th2 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY,15,4)
th3 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY,15,6)
th4 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY,15,8)
 
titles = ['C: 2', 'C: 4', 'C: 6', 'C: 8',]
images = [th1, th2, th3, th4]
for i in range(4):
    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([])
plt.show()