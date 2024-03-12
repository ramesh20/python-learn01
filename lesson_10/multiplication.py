input_val = set()

for i in range(5):
    number = int(input(f'Enter the {i + 1} number: '))
    input_val.add(number)

for num in input_val:
    for j in range(1, 11):
        result = f'{num} x {j} = {num * j}'
        print(result)
    print("-------------")

print('==================')