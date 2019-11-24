# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 10:15:40 2019

@author: Rameshbabu
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
img=cv2.imread('foto.jpg',0)
hist,bins=np.histogram(img.flatten(),256,[0,256])
plt.plot(hist,color='r')
plt.hist(img.flatten(),256,[0,256],color='g')

cdf=hist.cumsum()
cdf_normalized=cdf*hist.max()/cdf.max()

plt.plot(cdf_normalized, color = 'b')
plt.hist(img.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
plt.legend(('cdf','histogram'), loc = 'upper left')
plt.show()

#
equ = cv2.equalizeHist(img)
cv2.imwrite('equ.jpg',equ)