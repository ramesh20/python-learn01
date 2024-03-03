a = {
    "name": "kist",
    "address": "Morang",
}

b = {
    "name": "Ramesh",
    "school": {
        "name":"KMC",
        "address": a
    }
}

result = f'{b["school"]["address"]["name"]} - {b["school"]["name"]} - {b["name"]}'

print(result)

aa = {
    "city": "pokhara"
}
print(aa.get("city", "NA"))


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
