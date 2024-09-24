# Strings
name = "Mayank"
# str
print(type(name))
print(name.upper())
print(name.lower())
print(len(name)) # Start from 1

a = "90"
age = 90
print(type(a))
print(type(age))

name = "This is line"
print(type(name))
name = name + str(1) # Concatenate
print(name)

first_name = "Mayank"
last_name = "kumar"
full_name = first_name + last_name # Concatenation
print(full_name)

how_many_planes_i_have = None
print(type(how_many_planes_i_have)) #NoneType
# null is not present in Python

val = 0 # This is int

#id
age = 10
age1 = 10
print(id(age)) #140705269943000 (Print the memory location)
print(id(age1)) # 140705269943000
