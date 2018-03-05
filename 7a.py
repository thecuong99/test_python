#import cv2
import glob
import numpy as np
import numpy as array1
import matplotlib.image as mpimg
from sklearn.cluster import KMeans
from PIL import Image
from resizeimage import resizeimage


#Module class from "trainning"
X_data = []
files = glob.glob ("trainning/*.jpg")
for myFile in files:
    print(myFile)
    image1 = mpimg.imread(myFile)  #image = mpimg.imread (myFile)  #matplotlib.image as mpimg thi cho .shape # PIL import Image khong cho .shape
	#print image1.shape
	#image1 = image1.tolist()
    X_data.append (image1)
arrayY = np.asarray(X_data)
print "Data size:"
arrayY = arrayY.reshape(-1,784)
print arrayY.shape
n_class = 5
km2 = KMeans(init='k-means++', n_clusters=n_class, random_state=1, n_init=100).fit(arrayY)
print "Ket qua gan nhan label:"
print km2.labels_
#Reconize
#imaged = mpimg.imread('predict/x.jpg') #imagea = imagea.reshape(1,-1)
myR = "predict/x.jpg"
imaged = Image.open(myR).convert('L')
imaged = resizeimage.resize_cover(imaged, [28, 28])
myR1 = "predict/xxx.jpg"
imaged.save(myR1)
imaged2 = mpimg.imread(myR1)
imaged2 = imaged2.reshape(1,-1)
result = km2.predict(imaged2)
print "Result of prediction is here:"
if (result == 3):
	print "2"
elif(result == 1):
	print "1"
elif(result == 2):
	print "4"
elif(result == 0):
	print "5"
elif(result == 4):
	print "3"
else:
	print "Khong biet."
'''
data = np.array(X_data)
print data.shape

y = np.asarray(x)
y = y.reshape(-1,784)
n_class=5
km2 = KMeans(init='k-means++', n_clusters=n_class, random_state=1, n_init=10).fit(y)
print km2.labels_
print km2.cluster_centers_[:]
'''


