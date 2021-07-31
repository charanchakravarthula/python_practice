a=3
b=5
if(a<b):
    print("a is lesser")
    if(a<0):
        print("a is less than 0")
    elif(a>2):
        print("a grt than 2")
else:
    print("b is lesser")
# shorthand  or terinary
greatest=a if a>b else b
