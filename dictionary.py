# creating a dictionary

dict_var={'a':1,"b":2,'c':3}

# adding a ket value pair to dictionary

dict_var['d']=4

# updating an existing value

dict_var['d']=5

print(dict_var)



# updating multiple values at ones

dict_var.update({'a':"fds","d":9,'v':10})

# deleting a specific key value pair

del dict_var['b']

# remove an key value pair

dict_var.popitem()

print(dict_var)

# getting keys of dict

print(dict_var.keys())

# getting values of dict

print(dict_var.values())

#getting key value pairs or items of dict

print(dict_var.items())