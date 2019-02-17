#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import matplotlib.pyplot as plt
import numpy as np
import sys

'''
temp
'''

import pytesseract
from PIL import Image, ImageEnhance, ImageFilter

im = Image.open('temp.jpg')  # the second one

# im = im.filter(ImageFilter.MedianFilter())
# enhancer = ImageEnhance.Contrast(im)
# im = enhancer.enhance(2)
# im = im.convert('1')
# im.save('temp2.jpg')

text = pytesseract.image_to_string(im)
print(text)

# cv2.waitKey(0)
# cv2.destroyAllWindows()
