#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import matplotlib.pyplot as plt
import numpy as np
import sys


img = cv2.imread('1.png',0)
edges = cv2.Canny(img,100,200)

# plt.subplot(121),plt.imshow(img,cmap = 'gray')
# plt.title('Original Image'), plt.xticks([]), plt.yticks([])
# plt.subplot(122),plt.imshow(edges,cmap = 'gray')
# plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
# plt.show()
# print(edges.shape)
# plt.rcParams['figure.figsize'] = [16, 8]
# plt.imshow(edges,cmap='gray')
# plt.show()



img = cv2.imread('1.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


edgesi = cv2.Canny(img,600,600)
edgesg = cv2.Canny(gray,600,600)


#img = img[:, :, 0]

sideBySide = np.hstack((edgesi,edgesg))

#cv2.imshow('image',img)
#cv2.imshow('image',gray)
cv2.imshow('image',sideBySide)
cv2.waitKey(0)
cv2.destroyAllWindows()





