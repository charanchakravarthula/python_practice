class demo:
    def __init__(self,msg):
        self.msg=msg
    def greet(self,name):
        print(f'hey {name} whatsapp!!{self.msg}')
a=demo("mann")
a.greet("charan")