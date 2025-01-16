string1=input("Enter a string ")
vowels="aeiouAEIOU"
count=0

for char in string1:
    if char in vowels:
        count+= 1

print("Number of vowels", count)
 



string2 = input("Enter a string ")
print("Reversed string:", string2[::-1])





string3=input("enter the string: ")
if string3==string3[::-1]:
  print("Pallindrome")
  else
  print("Not a pallindrome")