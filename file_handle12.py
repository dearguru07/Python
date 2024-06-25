"""
open file

read/write  / append

close file

"""

"""
# ----------------read mode---------------------

s=open("acess12.txt",mode="r")
print(s.read())
s.close()

"""

# ----------write mode---------------

"""
s=open("acess12.txt",mode="w")
s.write("im guru  charan , hkeooo") ===> previous data will be truncate(delete),new text only will get
s.close()

"""



s = open("acess12.txt", mode="a")
s.write("guru charan how are tou man you are a")  #===> this data will be added for the old data
s.close()

'''
s=open("acess12.txt",mode=r+)
print(s.read())
s.'''

