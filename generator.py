# generator to get 1 to 10
def gen():
    i=1
    while True:  
        if(i>10):
            break 
        yield i
        i+=1

for i in gen():
    print(i)

# different ways to access next values of generator
def smallgen():
    yield 1
    yield 2
    yield 3
a=smallgen()
print(a.__next__())
print(a.__next__())
print(next(a))      
