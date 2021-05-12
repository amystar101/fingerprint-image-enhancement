#this files retrun orientation of ridges

import numpy as np
import cv2 as cv
from gradient import gradient


def orientation(img_norm,w = 16):

    print("Calculating local ridge orientation")

    Gx,Gy = gradient(img_norm)

    Gxy = 2*np.multiply(Gx,Gy)
    Gxx = np.power(Gx,2)
    Gyy = np.power(Gy,2)

    kernel = np.ones((w,w),np.float64)

    Vy = cv.filter2D(Gxy,-1,kernel = kernel)
    Vx = cv.filter2D(Gxx-Gyy,-1,kernel = kernel)

    theta = 0.5*np.arctan2(Vy,Vx)

    phi_x = np.cos(2*theta)
    phi_y = np.sin(2*theta)

    low_pass_filter = np.ones((5,5),dtype=np.float64)/(5*5)


    phi_dash_x = cv.filter2D(phi_x,-1,low_pass_filter)
    phi_dash_y = cv.filter2D(phi_y,-1,low_pass_filter)


    orientation = 0.5*np.arctan2(phi_dash_y,phi_dash_x) + np.pi/2

    return orientation

