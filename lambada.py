names= [
    {"name":"musabbir"},
    {"name":"malik"},
    {"name":"afsath"}
]

# def f(person):
#     return person["name"]

# names.sort(key=f)

# print(names)

print()

#using lambada:-

names.sort(key=lambda names: names["name"])

print(names)