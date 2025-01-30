#1
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
add = arr + 2
mul = arr * 3
div = arr / 2
print("Sum:",add)
print("Product:",mul)
print("Quotient:",div) 


#2
# Reverse
arr = np.array([1,2,3,6,4,5])
r = arr[::1]
print("Reversed Array:",r,"\n")

# Frequency

def most_fre(a):
    f = np.bincount(a).argmax()
    print("Most Frequent Value:",f)
    i = np.where(a==f)[0]
    print("Indices:",i,"\n")

x = np.array([1,2,3,4,5,1,2,1,1,1])
y = np.array([1,1,1,2,3,4,2,4,3,3])
most_fre(x)
most_fre(y)


#3
arr=np.array([[10,20,30],[40,50,60],[70,80,90]])
#a
print(arr[0][1])

#b
print(arr[2][0])


#4
abhinav=np.linspace(10,100,25)
print(abhinav.ndim)
print(abhinav.shape)
print(abhinav.dtype)
print(abhinav.nbytes)

reshape=abhinav.reshape(25,1)
print(reshape)
transpose=reshape.T
print("after transpose ", transpose)



#5
ucs420_abhinav= np.array([[10, 20, 30, 40], [50, 60, 70, 80], [90, 15, 20, 35]])
print( np.mean(ucs420_abhinav))
print(np.median(ucs420_abhinav))
print(np.max(ucs420_abhinav))
print(np.min(ucs420_abhinav))
print(np.unique(ucs420_abhinav))
reshape_ucs420_abhinav=ucs420_abhinav.reshape(4,3)
print("reshape:\n",reshape_ucs420_abhinav)
resize_ucs420_abhinav=np.resize(ucs420_abhinav,(2,6))
print("resize_array:\n",resize_ucs420_abhinav)
