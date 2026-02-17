import numpy as np

x = np.array([12, 34, 56]) # tek boyutlu dizi
print(x)
print(type(x))
print(x.dtype)
print(x[0]);print(x[1]);print(x[2])
print(x[-1],)

print("***********************")

y = np.array([[1, 2, 3], [4, 5, 6]]) # iki boyutlu dizi (matris)
print(y)
print(type(y))
print(y.dtype)
print(y[0][0], y[0][1], y[0][2])
print(y[1][0], y[1][1], y[1][2])
print(y[:, 0], y[:, 1], y[:, 2]) #sutunlari yazdirma
print(y[0, :], y[1, :]) #satirlari yazdirma

print("***********************")

z = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]]) # üç boyutlu dizi
print(z)
print(type(z))
print(z.dtype)
print(z[0][0][0], z[0][0][1])
print(z[0][1][0], z[0][1][1])
print(z[1][0][0], z[1][0][1])   
print(z[1][1][0], z[1][1][1])

print("***********************")

print(x.ndim) # tek boyutlu dizinin boyutu
print(y.ndim) # iki boyutlu dizinin boyutu
print(z.ndim) # üç boyutlu dizinin boyutu

print(x.shape) # tek boyutlu dizinin şekli
print(y.shape) # iki boyutlu dizinin şekli
print(z.shape) # üç boyutlu dizinin şekli

print(x.size) # tek boyutlu dizinin eleman sayısı
print(y.size) # iki boyutlu dizinin eleman sayısı
print(z.size) # üç boyutlu dizinin eleman sayısı

print("***********************")

a = np.empty([2,5], np.uint8)
print(a)

print("***********************")

b = np.full([2,5], 63, dtype=np.uint8)
print(b)

print("***********************")

c = np.zeros([2,5], dtype=np.uint8)
print(c)

print("***********************")

d = np.ones([2,5], dtype=np.uint8)
print(d)


