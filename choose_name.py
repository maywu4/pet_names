import random

file = open('petnames.txt', 'r')

names = file.read()
names_list = names.split("\n")
selected_name = random.choice(names_list)

# print(names)
# print(names_list)
# print(selected_name)


#add name
file.close()

file = open('petnames.txt', 'a')

file.writelines('\nMaxi')

file.close()


#re-select
file = open('petnames.txt', 'r')

names = file.read()
names_list = names.split("\n")
last_name = names_list[-1]

# print(names)
# print(names_list)
print(selected_name)
print(last_name)

