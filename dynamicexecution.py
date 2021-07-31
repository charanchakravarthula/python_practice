# string with python statements\

string="l=[1,2,3,4,5]"

# with the help of exec statmenrs we can dynamically execute strings 

exec(string)

for i in l:
    
    print(i)