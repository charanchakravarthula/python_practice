# creating a function with no args
def func():
    print("hello functions")
func()

# creating function that takes arguments

def func1(name,age):
    print(f'{name}\'s age is {age}')
func1("charan",10)

# function deafult arguments

def func3(firstname,lastname,age=18):
    print(f'{firstname}{lastname}\'s age is {age}')
func3("charan","chakravarthula",22)
func3("charan","chak")

# args

def func4(a,b,c,*args):
    print(a,b,c)
    for i in args:
        print(i)
func4(1,2,3,4,5)
func4(1,2,3)

# args as first argument

def func5(*args,b,c):
    print(b,c)
func5(1,2,3,b=2,c=5)

# key word args

def func6(b,c,**kwargs):
    print(b,c)
    for i in kwargs.items():
        print(i)
func6(1,2,a=4,d=5)

