# importing libraries
import cv2 as cv
import numpy as np
import normalise
from orientation import orientation
from ridge_frquency import ridge_frequency
from gabor_filter import gabor_filter



#loading images
name = "name of the imag"
img = cv.imread("./input_images/"+name,0)

# padding to create border
w = 40
img0 = 255*np.ones((img.shape[0]+2*w,img.shape[1]+2*w),dtype=np.float64)
img0[w:img.shape[0]+w,w:w+img.shape[1]] = img

#displaying the read image
cv.imshow("orignal image",img)
cv.waitKey(0)

#rows and columns in loaded image
rows,cols = img0.shape
print("rows = ",rows,"columns = ",cols)

#normalising image
img_norm = normalise.normalise(img0,1.0,1.0)

# passing with the low pass filter.
low_pass_filter = np.ones((5,5),dtype=np.float64)/(5*5)
img_norm_low_passed = cv.filter2D(img_norm,ddepth = -1,kernel = low_pass_filter)

cv.imshow("normalise image",img_norm)
cv.waitKey(0)

# calculating orientation of ridges in image
orient_img = orientation(img_norm)
cv.imshow("oreint",orient_img)
cv.waitKey(0)

# ridge frequency
ridge_freq = ridge_frequency(img_norm_low_passed,orient_img)
cv.imshow("ridge_frequecy",ridge_freq)
cv.waitKey(0)


#applying gabor filters
img_enhance = gabor_filter(img_norm,ridge_freq,orient_img)
cv.imshow("enhanced image",img_enhance)
cv.waitKey(0)

print("Image enhancement completed")

