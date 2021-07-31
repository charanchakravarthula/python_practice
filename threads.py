from threading import *
from time import sleep
class a(Thread):
    def run(self):
        for i in range(0,5):
            print("in thread a")
            sleep(1.0)
class b(Thread):
    def run(self):
       for i in range(0,5):
            print("in thread b")
            sleep(1.0)
obj1=a()
obj2=b()
obj1.start()
sleep(0.5)
obj2.start()
obj1.join()
obj2.join()
print("executed")