from copy import copy,deepcopy
# using copy function will create deep copy of simple objects  but not for nested objects 

l=[1,2,3,4,5,6,7]
m=copy(l)

l=[1,2,3,4,[6,7,8]]
m=copy(l)
m[4].pop()
# this will remove the element from the l as well
print(l)
# using deep copy function to avoid this issue

l=[1,2,3,4,[6,7,8]]
m=deepcopy(l)
m[4].pop()
print(l)