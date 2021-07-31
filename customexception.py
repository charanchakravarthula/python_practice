class custom(Exception):
    def __init__(self,msg):
        self.msg=msg
try:
    a=1
    if a==1:
        raise custom("hey this is custom exception")
except custom as e:
    print(e.msg)
