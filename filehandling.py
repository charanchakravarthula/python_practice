# opening a file in read mode without context manager

f=open("./randomfile.txt","r")
# using read function
print(f.read())
# closing file
f.close()


# using readlines to get the list of lines
f=open("./randomfile.txt","r")
print(f.readlines())
f.close()

# using readline with buffer size specified
f=open("./randomfile.txt","r")
print(f.readline(10))
f.close()

# opening the file with context manager
with open("./randomfile.txt","r") as f:
    print(f.readlines())

# opening a file in write mode
with open("./randomfile.txt","w") as f:
    # writing into file using write function
    f.write("this statement is written dynamically1")

with open("./randomfile.txt","w") as f:
    f.writelines(["hey","dfsbjhfbsdjh","dish"])

# dealing with images
with open("./samplepic.png","rb") as f:
    with open("./copypic.png","wb") as e:
        e.write(f.read())

