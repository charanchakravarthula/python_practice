# for loop with pass and continue
for i in range(0,10):
    if i==2:
        continue
    elif i==5:
        pass
    print(i)
# else block with for
for i in range(0,10):
    print(i)
else:
    print("for executed completely")

# else block will not be execued if break is execcuted in for

for i in range(0,10):
    print(i)
    if i==8:
        break
else:
    print("for executed completely")

# enumerate in for loop
l=["a","b","c"]
for i in enumerate(l,2):
    print(i)

# while
i=1
while(i<10):
    print(i)
    i+=1

