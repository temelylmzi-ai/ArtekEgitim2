import cv2
import numpy as np
import matplotlib.pyplot as plt

path = "C:\\Users\\temel\\OneDrive\\Desktop\\indir.jpg"

"""
img = cv2.imread(path,0) # BGR formatında okur.
#img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # BGR formatını RGB formatına çevirir.

plt.imshow(img,cmap = "gray") # RGB formatında gösterir.
plt.show()
"""

"""
img = plt.imread(path)

print(img)

print("min value: ",img.min())
print("max value: ",img.max())
print("mean value: ",img.mean())
print("median value: ",np.median(img))
print("std value: ",img.std()) # standart sapma
"""
"""
img = plt.imread(path)

red = img[:,:,0]
green = img[:,:,1]
blue = img[:,:,2]

output = [img,red,green,blue]
titles = ["Original Image", "Red Channel", "Green Channel", "Blue Channel"]

for i in range(4):
    plt.subplot(2,2,i+1)
    plt.axis("off")
    plt.title(titles[i])
    if i == 0:
        plt.imshow(output[i])
    else:
        plt.imshow(output[i], cmap = "gray")
    plt.show()

output2 = np.dstack((red,green,blue))
plt.axis("off")
plt.imshow(output2)
plt.show()
"""
"""
img = plt.imread(path)

plt.subplot(4,2,1)
plt.axis("off")
plt.title("Original Image")
plt.imshow(img)

plt.subplot(4,2,2)
plt.axis("off")
plt.title("img + img")
plt.imshow(img + img)

plt.subplot(4,2,3)
plt.axis("off")
plt.title("img * 0.5")
plt.imshow(img * 0.5)

plt.subplot(4,2,4)
plt.axis("off")
plt.title("img - img")
plt.imshow(img - img)

plt.subplot(4,2,5)
plt.axis("off")
plt.title("np.flip(img,0)") # x eksenine göre çevirir.
plt.imshow(np.flip(img,0)) #np.fliplr(img) ile de aynı sonucu verir.

plt.subplot(4,2,6)
plt.axis("off")
plt.title("np.flip(img,1)") # y eksenine göre çevirir.
plt.imshow(np.flip(img,1)) #np.flipud(img) ile de aynı sonucu verir.

plt.subplot(4,2,7)
plt.axis("off")
plt.title("np.flip(img,2)") # z eksenine göre çevirir.
plt.imshow(np.flip(img,2)) 

plt.show()
"""