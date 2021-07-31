# variable assignment
var = 1
print(var)

# multiple values assignment to a variable

var1,var2 =(1,2)
print(var1,var2)

#ignoring unwanted values 

var1,__,__=[1,2,3]
print(var1)

var1=var2=var3=1
print(var1,var2,var3)

# knowing the type of the varible i.e data type of variable

var1=[1,2,3]
var2=('a',"b","c")
var3=1
var4=1.0
var5={'a':1,"b":2}
var6={1,2,3}
print(type(var1),type(var2),type(var3),type(var4),type(var5),type(var6),sep="\n")

# get the memory id of a variable

print(id(var1))



