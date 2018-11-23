#Numpy exercises

#Exercise 1: Introduction to Numpy arrays
#1:
import numpy as np
x = range(1,11)
a1 = np.array(x, np.int64)
a2 = np.array(x, np.float64)
print(a1.dtype)
print(a2.dtype)

#2:
a = np.zeros((2,3,4))
print(a)
b = np.ones((2,3,4))
print(b)
c = np.arange(1000)
print(c)

#3:
y = [2, 3.2, 5.5, -6.4, -2.2, 2.4]
z = np.array(y)
print(z[1])
print(z[1:4])
p = np.array([[2, 3.2, 5.5, -6.4, -2.2, 2.4], [1, 22, 4, 0.1, 5.3, -9], [3, 1, 2.1, 21, 1.1, -2]])
print(p[:, 3])
print(p[1:4, 0:4])
print(p[1:, 2])


#Exercise 2: Interrogating and manipulating arrays
#1:
arr = np.array([[range(4)],[range(10,14)]])
print(np.shape(arr))
print(np.size(arr))
print(np.max(arr))
print(np.min(arr))

#2:
#Continuing to use the array from exercise 1
print(np.reshape(arr, (2,2,2)))
print(np.transpose(arr))
print(np.ravel(arr))
print("flatten", arr.flatten())
print(arr.astype(np.float64))


#Exercise 3: Array calculations and operations
#1:
d1 = np.array([[range(4)],[range(10,14)]])
d2 = np.array([2, -1, 1, 0])
d3 = d1 * d2
print(d3)
d4 = d2 * 100
d5 = d2 * 100.0
print(d4)
print(d5)
print(d4 == d5)
print(d4.dtype, d5.dtype)

#2:
e = np.arange(10)
print(e < 3)
print(np.less(e, 3))
condition = np.logical_or(3 > e, 8 < e)
e2 = np.where(condition, e * 5, e * -5)
print(e2)

#3:
def wind_magnitude(u, v, min_mag = 0.1):
	mag = ((u ** 2) + (v ** 2)) ** 0.5
	output = np.where(mag > min_mag, mag, min_mag)
	return output

u1 = np.array([[4, 5, 6], [2, 3, 4]])
v1 = np.array([[2, 2, 2], [1, 1, 1]])

print(wind_magnitude(u1, v1))

u2 = np.array([[4, 5, 0.01], [2, 3, 4]])
v2 = np.array([[2, 2, 0.03], [1, 1, 1]])

print(wind_magnitude(u2, v2))


#Exercise 4: Working with missing values
#1: 
import numpy.ma as MA
marr = MA.array(range(10), fill_value = -999)
print(marr)
print(marr, marr.fill_value)
marr[2] = MA.masked
print(marr)
print(marr.mask)
narr = MA.masked_where(marr > 6, marr)
print(narr)
narr_filled = MA.filled(narr)
print(narr_filled)
print(type(narr_filled))

#2:
m1 = MA.array(range(1,9))
print(m1)
m2 = m1.reshape(2,4)
print(m2)
m3 = MA.masked_where(m2 > 6, m2)
print(m3)
m4 = m3 * 100
print(m4)
m5 = np.ones((2,4))
m6 = m3 - m5
print(m6)
