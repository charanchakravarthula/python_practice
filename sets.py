# creating a set

set_var={1,2,3}

# adding values into set

set_var.add(4)

#adding a duplicate and trying to print the values

set_var.add(1)


print(set_var)
set_var2={2,3,4}

# set diff
print(set_var.difference(set_var2))

# intersection
print(set_var2.intersection(set_var))

#checking if the sets are disjoint sets
print(set_var2.isdisjoint(set_var))

#checking if the set is subset
print(set_var2.issubset(set_var))

# checking if the ser is superset
print(set_var.issuperset(set_var2))

#union
print(set_var2.union(set_var))

# traversing in sets

for i in set_var:
    print(i)