#import cv2
import glob
import numpy as np
import numpy as array1
import matplotlib.image as mpimg
from sklearn.cluster import KMeans
from PIL import Image
from resizeimage import resizeimage


#Module convert and resize

X_data = []
files = glob.glob ('a/*.jpg')
for myFile in files:
    print(myFile)
    image1 = Image.open(myFile).convert('L')
image1 = resizeimage.resize_cover(image1, [28, 28])
print type(image1)
image1.save('trainning/x.jpg')
	
'''
from PIL import Image
img = Image.open('c1.jpg').convert('L')
img.save('c2.jpg')
'''


