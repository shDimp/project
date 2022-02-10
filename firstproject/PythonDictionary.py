my_dict = {
    "class": "Animal",
    "Name": "lion",
    "age": 13

}
print(my_dict)
print(my_dict["Name"])
for x in my_dict:
    print(my_dict[x])
for x,y in my_dict.items():
    print(x,y)
my_dict["name"]= "Elephnat"
print(my_dict)
my_dict["color"] = "Red"
print(my_dict)
my_dict.pop("color")
print(my_dict)
del my_dict