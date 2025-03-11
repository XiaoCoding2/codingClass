#class robot:
#    def robotic(self):
#        print(self.name, self.num)
#
#r = robot()
#r.name = 'tom'
#r.num = 10

#r.robotic()

#Not good ^
#         |

class rob:
    def __init__(self, name, num): #constructer
        self.name = name
        self.num = num

    def hello(self):
        print(self.name, self.num)

    def test(self):
        self.num
        self.name

r1 = rob("Tom", 5)
r1.hello()
r2 = rob("Moo", 15)
r2.hello()

#inheritance, transfering attributes to anouther.
class person:
    def __init__(self, name):
        self.name = name

    def getname(self):
        return(self.name)

    def sitting(self):
        return True

#p1.rob1 = r2
#p1.rob1.hello()

class p2(person):

    def sitting(self):
        return False

p1 = person("Ted")
print(p1.getname(), p1.sitting())

p1 = p2("Lot")
print(p1.getname(), p1.sitting())