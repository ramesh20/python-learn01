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

a = random.randrange(1, 8)
guess_num = int(input("Guess the number: "))
counter = 0

while a != guess_num:
    counter += 1
    print(f'Wrong guess. Try again.')
    guess_num = int(input("Guess the number: "))

print(f'Congratulations! You guessed the correct number {a} in {counter} attempts.')
