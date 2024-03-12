# .yml / .yaml
# typecasing -> change the type

set_data = {1, 2, 3, 4, 5}
set_data2 = {1, 2, 3, 4, 5,7,9,0}

# Dictionaries are used to store data values in key:value pairs.
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(set_data, thisdict)
print(type(set_data), type(thisdict))

set_data.update(set_data2)
new_setdata = set_data

set_data.remove(1)

print(new_setdata)

data_1 = [88, 3,3,3,3,3]
data_12 = set(data_1)
data_13 = list(data_12)

print(data_13)