a=lambda x:x*2
print(a(10))
# using lambda with map function
list_var=[1,2,3,4]

a=list(map(lambda x:x*3,list_var))
print(a)

# using filter and lambda
a=list(filter(lambda x:x%2==0,list_var))
print(a)

# using lambda with reduce
from functools import reduce
a=int(reduce(lambda x,y:x+y,list_var))
print(a)



