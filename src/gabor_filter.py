import numpy as np
import cv2 as cv



def gabor(w, theta, fr):
    #create gabor kernel

    theta += np.pi * 0.5
    cosine = np.cos(theta)
    sine = -np.sin(theta)

    ytheta = lambda x, y: x * cosine + y * sine
    xtheta = lambda x, y: -x * sine + y * cosine

    xsigma = ysigma = 4
    kernel = np.empty((w, w))
    for i in range(0, w):
        for j in range(0, w):
            x = i-w/2
            y = j-w/2
            kernel[i][j] = np.exp(-((xtheta(x,y)**2)/(xsigma**2)+(ytheta(x,y)**2)/(ysigma**2))/2)*np.cos(2*np.pi*fr*xtheta(x,y))
            
    return kernel



def gabor_filter(img_norm,frequencies,orientations):
    w = 32
    img_enhance = np.zeros(img_norm.shape)

    mx = 0

    height, width = img_norm.shape
    for y in range(0, height-w, w):
        for x in range(0, width - w, w):
            orientation = orientations[y+w//2, x+w//2]
            frequency = 0
            cnt = 0
            for i in range(y,y+w):
                for j in range(x,x+w):
                    if frequencies[i][j] >= 0:
                        frequency += frequencies[i][j]
                        cnt += 1
            
            if cnt != 0:
                frequency = frequency/cnt

            if cnt == 0:
                img_enhance[y:y+w, x:x+w] = img_norm[y:y+w, x:x+w]
            else:
                kernel = gabor(16, orientation, frequency)
                img_enhance[y:y+w,x:x+w] = cv.filter2D(img_norm[y:y+w,x:x+w],ddepth = -1,kernel = kernel)

            mx = max(np.mean(img_enhance[y:y+w,x:x+w]), mx)
            
    
    for i in range(0, height-w, w):
        for j in range(0, width - w, w):
            if np.mean(img_enhance[i:i+w, j:j+w]) >= 0.2*mx:
                img_enhance[i:i+w, j:j+w] = img_norm[i:i+w, j:j+w]

    img_enhance[height-w:height][:] = img_norm[height-w:height][:]
    for y in range(0,height):
        for x in range(width-w,width):
            img_enhance[y][x] = img_norm[y][x] 

    return img_enhance

