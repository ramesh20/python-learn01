i = 1
while(i <= 3):
    print(i)
    i += 1
print("end ehile loop")

# Write a program to display only those numbers from a list that satisfy the following conditions
# 1. The number must be divisible by five
# 2. If the number is greater than 150, then skip it and move to the next number
# 3. If the number is greater than 500, then stop the loop

# numbers = [12, 75, 150, 180, 145, 525, 50]

# for i in numbers:
#     if( (i % 5 == 0) and i >= 150 ):
#         print(i)

import random
a = random.randrange(1, 6)
guess_num = int(input("Guess the number: "))
counter = 0

while(a != guess_num):
    counter =+ 1
    print(f'Congratulation your number is matching. The number is {a} and the counter is {counter}')
    guess_num = int(input("Guess the number: "))
print(f'You guessed the wrong number: {a} and the counter is {counter}')
