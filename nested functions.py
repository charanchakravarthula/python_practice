# nested function
def outer1():
  print("I'm the outer function.")
  def inner1():
    print("And I'm the inner function.")
  inner1()

outer1()

# example of closure
def outer(name,age):
    def inner(score):
        print(name,age,score)
    return inner
func_var=outer("charan",22)
func_var(240)


# even after deleting the outer function from the memory closures or inner functions hold the state
del outer
func_var(230)
