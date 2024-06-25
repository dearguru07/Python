'''
Functions ==> block of code
'''

'''
def fuctName():  ===> function definition
  print("this is a one fiunxction")   ==> functtion body
fuct() ========> function calling 
'''

'''
def guru(x,y,z):
  print("this is a new function",x,y,z)
guru(1,2,3)  

  '''
  
  
'''
def guru(*a):
  print("hello world",a)  
guru(1,2,2,3) ====> o/p will come in Tuple Format ()
 
'''
  
'''
def guru(**a):  ==> key word argments
  print("heloo world...",a) 
guru(a=1,b=5,c=9)   ====> o/p will come in Dict Format {}

 '''  
 
#  ----------nested function---------


def outer():
  print("outerfunction")
  def inner():
    print("inner function") 
    def innerin():
      print("inner in function")
    innerin()
  inner()
outer()            



'''
def add(a,b):
  print(a+b)
add(5,9)  
def sub(a,b):
  print(a-b) 
sub(3,2)   
  '''
  
  
# -----------code reuseablilte-----------
  
# def add(a,b):
#   print(a+b)
# def sub(a,b):
#   print(a-b) 
  
# -------create a new file and access with code ---in [code10.py file] ------
  
  
  
  
def outer():
  print("hello world......")
  def inner():
    print("hii world...")  
  return inner
reff=outer()
# print(reff)
reff()  