L=[10,20,30,40,50,60,70,80]

# 1.
L.append(200)
L.append(300)
print(L)

# 2.
L.remove(10)
L.remove(30)
print(L)

# 3.
L.sort()
print(L)

# 4.

M=L[::-1]
print(M)

#or 
L.sort(reverse=True)
print(L)