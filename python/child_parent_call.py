
class PPParent:
    def makeChildrenStopCry(self):
        if self.cry():
            self.dowhateverToStopCry()
 
class Parent(PPParent):
    pass

class Children(Parent):
    crying = False
    def makeCry(self):
        self.crying = True

    def dowhateverToStopCry(self):
        self.crying = False

    def cry(self):
        return self.crying
    

child = Children()
child.makeCry() 
print(child.crying)
child.makeChildrenStopCry()
print(child.crying)