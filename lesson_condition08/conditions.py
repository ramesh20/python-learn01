greeting = "Hello"
number_one = 12

'''
Hello this is multiline comment in python

# syntax
# if ( condition ):
# 	statement

if (number_one == "12"):
	print(greeting)
else:
	print("no greeting")

print("block end")
'''

# val_first = input("Enter the first value: ")
# val_second = input("Enter the second value: ")

# if ( val_first > val_second ):
# 	print(f'the first value {val_first} is grater then second value {val_second}')
# elif ( val_first == val_second ):
# 	print(f'the first value {val_first} is equal to the second value {val_second}')
# else: 
# 	print(f'the second value {val_second} is grater then first value {val_first}')

input_total_number = int(input("Enter your Total SLC number (marks): "))
# input_percentage = input("Enter your SLC percentage: ")
input_percentage = int(input_total_number/8)

if( input_percentage > 100 ):
	print("Seems your score is higher than the total score !")
elif ( input_percentage >= 80 and  input_percentage <= 100 ):
	print("Seems your score is Distinction !")
elif ( input_percentage >= 60 and input_percentage < 45 ):
	print("Seems your score is first division !")
elif ( input_percentage >= 45 and input_percentage < 35 ):
	print("Seems your score is second division !")
elif ( input_percentage >= 35 ):
	print("Seems your score is second division !")
else:
	print("Seems your score is not enough, try again!")