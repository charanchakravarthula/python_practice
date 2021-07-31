# list comprehensions
l=[i for i in range(0,10)]
print(l)
# conditions in comprehension
l=[i  for i in range(0,10) if i%2==0]
l=[i if i%2==0 else i*2 for i in range(0,10)]
print(l)

# dict comprehension
l={x:x**2 for x in range(0,5)}
print(l)
# conditions 
l={x:x**2 for x in range(0,5) if x%2==0}
print(l)

# set comprehensions
l={x for x in range(0,5)}
print(l)