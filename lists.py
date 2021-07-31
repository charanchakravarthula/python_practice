# nuemeric data types int float and complex

integer_var=-1

float_var=1.0

complex_var=1+2j

print(type(integer_var),type(float_var),type(complex_var),sep="\n")

# playing with list

# creating an empty list

list_var=[]

# creating a list with some values

list_var2=[1,2,'a']

# adding elements to a list

list_var2.append(4)

# adding elements to a list dynamically

for i in range(5):
    list_var.append(i)

print(list_var)
print(list_var2)

# removing last element from the list
list_var.pop()
print(list_var)

# removing an element at particular index

list_var.pop(2)
print(list_var)

# removing a given element

list_var2.remove('a')
print(list_var2)

# updating an element at particular index
list_var2[0]='ab'
print(list_var2)

# merging to lists

list_var.extend(list_var2)
print(list_var)

# insert a value at particular index

list_var.insert(1,"new")
print(list_var)

# getting the length or size of the list

print(len(list_var))

# clearing the list
list_var2.clear()

# deleting values at particular index range

del list_var[0:3]
print(list_var)



