try:
    a=10
    b=0
    l=[1,2,3,4,5]
    for i in range(10):
        l[i]
    c=a/b
except IndexError:
    print("check the indexes")
except Exception as e:
    print(e)
finally:
    print("bye bye")

# else block

try:
    a=10
    b=0
    c=a+b
except IndexError:
    print("check the indexes")
except Exception as e:
    print(e)
else:
    print("in else")

# assertion
try:
    for i in range(0,5):
        assert i>3
except AssertionError:
    print("got assertion error")
