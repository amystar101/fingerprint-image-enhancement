# this returns gradient of image using simple sobel operator

import numpy as np 
import cv2 as cv

def gradient(img):
    #sobel 
    sobelx = np.array([[-5,-4,0,4,5],[-8,-10,0,10,8],[-10,-20,0,20,10],[-8,-10,0,10,8],[-5,-4,0,4,5]])
    sobely = sobelx.transpose()
    Gx = np.zeros(img.shape)
    Gy = np.zeros(img.shape)

    Gx = cv.filter2D(img, ddepth = -1, kernel = sobelx)
    Gy = cv.filter2D(img, ddepth = -1, kernel = sobely)

    return Gx,Gy
                
