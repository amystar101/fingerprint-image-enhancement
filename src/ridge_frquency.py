import numpy as np
import cv2 as cv


def ridge_frequency(img,orient,w = 2,mnlamda = 3,mxlamda = 15):

    print("Calculating Ridge frequency")

    frequency = np.zeros(img.shape)
    n,m = img.shape
    l = 32
    fr_block = np.zeros((int(n/w),int(m/w)))


    for i in range(0,n-w,w):
        for j in range(0,m-w,w):
            center_x = int(i+w/2)
            center_y = int(j+w/2)
            X = []
            wavelength = None
            angle = np.mean(orient[i:i+w,j:j+w])/2
            for k in range(0,l):
                X.append(0)
                for d in range(0,w):
                    u = i+w/2+(d-w/2)*np.cos(angle) + (k-l/2)*np.sin(angle)
                    v = j+w/2 + (d-w/2)*np.sin(angle) + (l/2-k)*np.cos(angle)
                    u = int(u)
                    v = int(v)
                    # print(u,v)
                    if u < n and v < m:
                        X[k] += img[u,v]
                X[k] /= w

            last = -1
            cnt = 0
            gap = 0
            for k in range(1,l-1):
                if X[k] > X[k-1] and X[k] > X[k+1]:
                    if last == -1:
                        last = k
                    elif k-last < mnlamda:
                        continue
                    elif k-last > mxlamda:
                        last = k
                    else:
                        gap += k-last+1
                        last = k
                        cnt += 1
            
            if cnt >= 2:
                wavelength = gap/cnt
                frequency[i:i+w,j:j+w] = (1/wavelength)*np.ones((w,w),dtype=np.float64)
                fr_block[int(i/w),int(j/w)] = (1/wavelength)
            elif cnt == 1:
                # need to be interploted by the neighbours
                frequency[i:i+w,j:j+w] = np.zeros((w,w),dtype=np.float64)
                fr_block[int(i/w),int(j/w)] = -1
            else:
                frequency[i:i+w,j:j+w] = np.zeros((w,w),dtype=np.float64)
                fr_block[int(i/w),int(j/w)] = 0

    

    
    # gaussian kernel
    wg = 7
    gauss = cv.getGaussianKernel(ksize = wg,sigma = 9)
    gauss = gauss*gauss.T

   
    # applying linear interpolation 
    for i in range(2,fr_block.shape[0]-2):
        for j in range(2,fr_block.shape[1]-2):
            if fr_block[i][j] == -1:
                total_dis = 0
                for i1 in range(-2,3):
                    for j1 in range(-2,-3):
                        if fr_block[i+i1][j+j1] != -1:
                            dis += np.sqrt(np.square(i1)+np.square(j1))
                fr_block[i][j] = 0
                for i1 in range(-2,3):
                    for j1 in range(-2,-3):
                        if fr_block[i+i1][j+j1] != -1:
                            d = np.sqrt(np.square(i1)+np.square(j1))
                            fr_block[i][j] += (d/dis)*fr_block[i+i1][j+j1]
            
            frequency[i*w:i*w+w,j*w:j*w+w] = fr_block[i][j]*np.ones((w,w),dtype=np.float64)

    frequency = cv.filter2D(frequency,ddepth = -1,kernel = gauss)

    return frequency