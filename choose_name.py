import random

file = open('petnames.txt', 'r')

names = file.read()
names_list = names.split("\n")
selected_name = random.choice(names_list)

# print(names)
# print(names_list)
print(selected_name)

