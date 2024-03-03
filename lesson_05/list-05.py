# a = 10
# print(a)

# input 3 value from users
# insert data in dict
# make 3 keys [city, temp, user]

city = input("Enter the city name: ")
temp = input("Enter the city temperature: ")
user = input("Enter the user name: ")

input_data = {
    "city" : "Kathmandu",
    "temp" : 32,
    "user" : "ramesh"
}

input_data["city"] = city
input_data["temp"] = temp
input_data["user"] = user

data_result = input_data.items()

# input
test_val = input("Are you developer? (Yes/No): ")

# update
input_data.update({"Are you developer? (Yes/No): " : test_val})

print(data_result)


# a = {}
# a['city'] = input()
# a['temp'] = int(input())
# a['user'] = input()
# a