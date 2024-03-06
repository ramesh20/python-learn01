a = {
    "name": "kist",
    "address": "Morang",
}

# b = {
#     "name": "Ramesh",
#     "school": {
#         "name":"KMC",
#         "address": a
#     }
# }

# result = f'{b["school"]["address"]["name"]} - {b["school"]["name"]} - {b["name"]}'

# print(result)

# aa = {
#     "city": "pokhara"
# }
# print(aa.get("city", "NA"))


# Assignment
b = {
    "name": "sudan",
    "school": [
        {"name": "Trinity", "address": "Kathmandu"},
        {"name": "GIPHSS", "address": "Dang"},
        {"name": "Deepshikha", "address": "Dang"},
    ],
}

# output 
# sudan-Trinity-Kathmandu
# sudan-GIPHSS-Dang
# sudan-Deepshikha-Dang

# for listing in b:
#     print(listing[0])
    # print(f'{listing["name"]}-{listing["school"][i]["name"]}-{listing["school"][i]["address"]}')

result_one = f'{b["name"]}-{b["school"][0]["name"]}-{b["school"][0]["address"]}'
result_two = f'{b["name"]}-{b["school"][1]["name"]}-{b["school"][1]["address"]}'
result_three = f'{b["name"]}-{b["school"][2]["name"]}-{b["school"][2]["address"]}'

final_result = f'{result_one}\n{result_two}\n{result_three}'

print(final_result)

