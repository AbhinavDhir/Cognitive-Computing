scores = (45, 89.5, 76, 45.4, 89, 92, 58, 45)
#1.
mx = max(scores)
print("Highest score:",mx)
print("Index of highest score:",scores.index(mx))
#2.
mn = min(scores)
print("Lowest score:",mn)
print("Index of lowest score:",scores.count(mn))
#3.
rev_scores = scores[::-1]
print(list(rev_scores))
#4.
find = int(input("Enter a score to find:"))
if find in scores:
    ind = scores.index(find)
    print("The score is present at index:",ind)
else:
    print("The score is not present.")