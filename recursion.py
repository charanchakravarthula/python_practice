def fun(i):
    if i==0:
        return 0
    else:
        return i+fun(i-1)
print(fun(10))