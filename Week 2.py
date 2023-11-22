#1.实现灰度化和二值化
from skimage.color import rgb2gray
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import cv2

# 灰度化
img=cv2.imread("lenna.png")  #读取当前项目里的图片 lenna
h,w=img.shape[:2]     #获取图片的高和宽,并且赋值给高和宽
img_gray=np.zeros([h,w],img.dtype)  #创建一张和当前图片一样大小的单通道图片
for i in range(h):
    for j in range(w):
        m=img[i,j]    #取出当前高和宽中的BGR坐标
        img_gray[i,j]=int(m[0]*0.11+m[1]*0.59+m[2]*0.3)  #将BGR坐标转化为gray坐标并赋值给新图像
print(img_gray)
print("img show gray:%s"%img_gray)
cv2.imshow("image show gray",img_gray)
cv2.waitKey()  #按下任意按键继续运行

plt.subplot(221)
img=plt.imread("lenna.png")
#img=cv2.imread("lenna.png",False)
plt.imshow(img)
print("---------image lenna-------")
print(img)


# 二值化

img_gray=rgb2gray(img)
rows,cols=img_gray.shape
for i in range(rows):
    for j in range(cols):
        if (img_gray[i,j]<=0.5):
            img_gray=0
        else:
            img_gray=1
print("---------image binary-------")
print(img_binary)
print(img_binary.shape)

plt.subplot(223)
plt.imshow(img_binary,cmap='gray')
plt.show()




