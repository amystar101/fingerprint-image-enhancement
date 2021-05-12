#function to normalise image
#setting new mean = 1, and new varriance = 1

import numpy as np
import math

def normalise(img,new_mean = 1.0,new_variance = 1.0):
    print("Normalising the image")
    print("setting new mean = "+str(new_mean)+" and new varriance = "+str(new_variance))

    r,c = img.shape

    mean = np.mean(img)
    variance = np.var(img)
    

    new_img = np.zeros(img.shape)



    for i in range(0,r):
        for j in range(0,c):
            if img[i][j] > mean:
                new_img[i][j] = new_mean + math.sqrt(new_variance*(img[i][j]-mean)**2/variance)
            else:
                new_img[i][j] = new_mean - math.sqrt(new_variance*(img[i][j]-mean)**2/variance) 

    # checking mean and variance of normalised image
    
    mean = np.mean(new_img)
    variance = np.var(new_img)

    print("mean = ",mean," variance = ",variance)

    return new_img

