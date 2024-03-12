# forloop 
# tkinter
# in -> membership operator
n = 11
for i in range(2, n):
    if i%2 == 0:
        print(i)

a = [1,4,5,6,8,7]
for num in a:
    print(num)

print('==================')

a = {1, 2, 3, 4, 5,5,5,5,6, 6,6,6,6,6,6} # set
for num in a:
    print(num)

print('==================')
# break and continue
for i in [1,2,3,4,6,7,9,8,4]:
    if i == 8:
        # print("8 is found")
        # break
        continue
    print(i)

print('==================')
# assingemt input 
for i in range(0, 11, 1):
    result = f'2 x {i} = {2*i}'
    print(result)

print('==================')
# n = int(input("Enter the number desired multiplication table: "))
# for i in range(0, 11, 1):
#     result = f'{n} x {i} = {n*i}'
#     print(result)

print('==================')
for i in ["Raesh", "Gautam"]:
    for j in range(1,3):
        print(i, j)

print('==================')
# multiplication table
input_val = {}
for i in input_val:
    number = input(f'Enter the { i } first number: ')
    input_val.append(number)
    # print(input_val)
    for j in range(0, 11,1):
        result = f'{i} x {j} = {i*j}'
        print(result)
    print("-------------")

print('==================')

for i in range(1, 6, 1):
    for j in range(0, 11, 1):
        result = f'{i} x {j} = {i*j}'
        print(result)
    print("-------------")

# get input from user - append use

landuages = ["python", "swift", "c++"]
for i in range(0, len(landuages), 1):
    print(landuages[i])