class parent:
    def greet(self):
        print("greeting from parent")
class child(parent):
    def greet(self):
        print("greeting from child")
    def parent_greet(self):
        super().greet()
obj=child()
obj.greet()
obj.parent_greet()