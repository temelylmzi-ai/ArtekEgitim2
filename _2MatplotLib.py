import numpy as np
import matplotlib.pyplot as plt
"""
x = np.arange(5)
y = x

print(x)
print(y)

plt.plot(x, y)

plt.plot(x, -y, 'o')

plt.plot(-x, y, 'o-')

plt.plot(-x, -y, 'o--')

plt.title("x = y, x = -y, -x = y, -x = -y")

plt.show()

a = np.linspace(0,10,11)
b = a

plt.plot(a, b, 'o-')
plt.title("a = b")
plt.show()

d = [1,2,3,4,5]
plt.plot(d,[t**2 for t in d], 'o-')
plt.show()
"""
"""
x = np.arange(5)

plt.plot(x, [y**2 for y in x])
plt.plot(x, [y**3 for y in x])
plt.legend(["x^2", "x^3"])

plt.xlabel("x")
plt.ylabel("y")

plt.axis([0,4,0,64])
plt.grid(True)

plt.title("x^2 and x^3")
plt.show()
"""
"""
path = "C:\\Users\\temel\\OneDrive\\Desktop\\indir.jpg"
img = plt.imread(path)

print("bicim: ",img.shape);print("veri tipi: ",img.dtype);print("boyut: ",img.ndim);print("size: ",img.size)

print("rgb: ",img[50,50,:]) # 50. satır, 50. sütun, tüm renk kanalları (Red[0], Green[1], Blue[2])

plt.imshow(img)
plt.axis("off")
plt.show()
"""