# creating a string

str_var=''

# modifying a string

str_var='abs'

# string concatenation

str_var=str_var+' bike'
print(str_var)

# string capitalisation 

cap_str=str_var.capitalize()
print(cap_str)

str_var='abs12'

# checking if the string contains only alpha numerics or not

print(str_var.isalnum())

#checking if the string contains only nuemirics

print(str_var.isnumeric())

# length of string

print(len(str_var))

#replacing all occurences of a string with another string 

new_str=str_var.replace('abs','bas')
print(new_str)

# find the index of a substring

print(new_str.find("ba"))




