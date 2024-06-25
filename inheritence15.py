'''
single inheritence
mutli-level inheritence
mutliple inheritence
hiratety inheritence

'''

# -------------------single inheritence---------------

'''
class parent:
    def output(slef):
        print("im parent")
class child(parent):
    def outputc(self):
        print("im child")        
C=child()
C.output()   #parent
C.outputc()   #child 
'''

# ------------------mutli-level inheritence-------------------

'''
class Grandfather:
    def outputgf(self):
        print("im grandfather")
class parent(Grandfather):
    def outputp(self):
        print("im parent")
class child(parent):
    def outputc(self):
        print("im child")
C=child()

C.outputc()
C.outputp()   
C.outputgf()
'''
                     
# ---------------------mutliple inheritence-----------------------                     
'''
class father:
    def outputgf(self):
        print("im grandfather")
class mother():
    def outputp(self):
        print("im parent")
class child(father,mother):
    def outputc(self):
        print("im child")
C=child()

C.outputc()
C.outputp()   
C.outputgf()

'''

# --------------------hiratety inheritence-----------------

class father:
    def ouputf(self):
        print("im father")
class child1(father):
    def ouputc(self):
        print("im child1")       
class child2(child1):
    def ouputC(self):
        print("im child 2")
c=child1()
c2=child2()
c.ouputc()
c.ouputf()
c2.ouputc()       
 
                                    
        