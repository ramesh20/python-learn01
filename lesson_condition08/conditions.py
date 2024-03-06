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

val_first = input("Enter the first value: ")
val_second = input("Enter the second value: ")

if ( val_first > val_second ):
	print(f'the first value {val_first} is grater then second value {val_second}')
elif ( val_first == val_second ):
	print(f'the first value {val_first} is equal to the second value {val_second}')
else: 
	print(f'the second value {val_second} is grater then first value {val_first}')