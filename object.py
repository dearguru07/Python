'''
class Car:
    # print("car is moving")
    a=15
    def disp(self):
        b=44
        c=98
        print(b,c)
object=Car()
object.disp()        
print(object.a)

'''

'''
class Mobile:
    def __init__(self,Brand,battery,price,camera,ram):
        self.Brand=Brand
        self.battery=battery
        self.ram=ram
        self.price=price
        self.camera=camera
    def displsy(self):
        print("Brand:",self.Brand)
        print("battery:",self.battery)    
        print("ram:",self.ram)    
        print("price:",self.price) 
        print("camera:",self.camera) 
        print("------------------")
object=Mobile("apple",4000,60000,"48mp","8gb")  
object1=Mobile("Moto",5000,7990,"64mp","8gb")  
object.displsy() 
object1.displsy()        
'''        