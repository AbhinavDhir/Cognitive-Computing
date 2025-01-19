A = {34, 56, 78, 90}
B = {78, 45, 90, 23}

# 1.
union_a= A.union(B)
print("Unique scores are:", union_a)

# 2.
intersection_a= A.intersection(B)
print("Common scores of both teams are:", intersection_a)

# 3.
exclusive_a= A.symmetric_difference(B)
print("Exclusive scores are",exclusive_a)

# 4.
subset = A.issubset(B)
superset = B.issuperset(A)
print(subset)
print(superset)

# 5.
score = int(input("Enter the score u want to remove "))
if score in A:
    A.remove(score)
else:
    print("Score not found")