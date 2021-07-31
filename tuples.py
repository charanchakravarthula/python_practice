# creating tuple
tup_var=(1,2,3)

# converting a list into tuple
con_var=tuple([1,2,3,4,5])
print(con_var)

# deleting a tuple

del tup_var

# getting the index of a value in the tuple

index_var=con_var.index(4)

print(index_var)

# tuple traversal
for i in con_var:
    print(i)

for i in range(0,len(con_var)):
    print(con_var[i])



