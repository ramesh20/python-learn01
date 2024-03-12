# string 
# check any type 
# a = "ramesn" type(a) / a.lower() / a.upper() | a.title() -> capatalise \n -> line break
# len(a) length check / a[0] -> r

first_name = "Ramesh"

if( first_name.isalpha() ):
    print("Your name is: " + first_name)
else:
    print("Invalid letter")


# input with string
input_string = str("Ramesh Gautam")
# input_string = str(input("Enter the desired string: "))
list_data = list(input_string)
print(list_data)
print(str(list_data))

# tuples -> data types, store the data
# [] list -> [1, 2, 3, 4, 5]
# () tuple (1, 2, 3, 4, 5) -> index(lowest index indeing), count(repeat value count)

first_data = [1, 2, 3, 4, 5]
second_data = (1, 2, 3, 4, 5)
third_data = {1, 2, 3, 4, 5}

type_list = list(second_data)
type_list.pop([2])
# del type_list[2]

print(type(second_data))

print(len(second_data))

print(second_data[0])
print(second_data[-1])

for numbers in second_data:
    print(numbers)