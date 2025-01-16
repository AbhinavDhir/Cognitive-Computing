# 9.1
import random
print('Five random numbers between 1 and 100 : ')
for i in range(1,6):
    print(random.randint(1,100),end=" ")

print('\n')
# 9.2
random_num = random.randint(1,100)
print(f'The random number is : {random_num}')

is_prime = True
if random_num < 2:
    is_prime = False
else:
    for i in range(2,int(random_num**0.5)+1):
        if random_num%i==0:
            is_prime = False
            break

if is_prime:
    print(f'{random_num} is a prime numnber')
else:
    print(f'{random_num} is not a prime number')

print('\n')
# 9.3
roll = random.randint(1,6)
print(f'You rolled a {roll}')

print('\n')
# 9.4
num = [2,4,37,7,8,3,5]
print(f'Original list : {num}')

random.shuffle(num)
print(f'Shuffled list : {num}')

print('\n')
# 9.5
l = ['Apple','Orange','Guava','Mango','Pear','Pineapple']
print('the list items are :',l)
s = random.choice(l)
print('Randomly Selcted item from the list :',s)

print('\n')
# 9.6 
import string
length = int(input('enter the length of the password you want : '))
characters = string.ascii_letters + string.digits + string.punctuation

password = ''.join(random.choices(characters,k = length))
print('Generated password :',password)

print('\n')
# 9.7  
deck = ['2','3','4','5','6','7','8','9','10','A','J','Q','K']
suits = ['Spades','Diamonds','Hearts','Clubs']
cards = random.choice(deck)
suit = random.choice(suits)

print(f'{cards} of {suit} is picked randomly')