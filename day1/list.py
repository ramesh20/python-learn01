# python inbuild datatype
# 1. List
colors = [] #empy list
a = [2, 2, 5, 6.7, 'gautam'] # index start a[0]
# b = 3
# print(a, b)

# print(type(a))   # list
# print(type(b))   # int

print(a[0]) # index 1

# method of adding items in list 
# append
# a.append("Ramesh")

color1 = input("Type first color: ")
color2 = input("Type second color: ")
color3 = input("Type third color: ")

colors.append(color1)
colors.append(color2)
colors.append(color3)

colors_list = colors.append(color2)
# colors_list = colors.append(color3)

print(colors_list)
print(colors)
print(len(colors))

# lifo
