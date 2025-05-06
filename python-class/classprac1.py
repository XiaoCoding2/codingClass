
#Python Classes Learn

'''
Syntax:
class <class name>:
    def __init__(self, <arguments>):
        <argument> = self.<argument name>
    def <func name>(self, argument(s) )
        <code stuff>
<var name> = <class name>(<arguments>)
'''

class SawmillCounter:
    def __init__(self):
        self.threeft = 0
        self.fiveft = 0
        self.pre = []
    def count(self, s0, s1):
        if s0 == False and s1 == True:
            if self.pre == [True, True]:
                self.fiveft += 1
            elif self.pre == [False, False]:
                self.threeft += 1
        else:
            a = 1
        self.pre = [s0, s1]

    def get_counts(self):
        return f'{self.threeft}, {self.fiveft}'
    
counter = SawmillCounter()

# 3ft
counter.count(False, False)
counter.count(True, False)
counter.count(False, False)
counter.count(False, True)
counter.count(False, False)

# 5ft
counter.count(True, False)
counter.count(True, True)
counter.count(False, True)
counter.count(False, False)

# 5ft
counter.count(True, False)
counter.count(True, True)
counter.count(False, True)
counter.count(False, False)
# 5ft
counter.count(True, False)
counter.count(True, True)
counter.count(False, True)
counter.count(False, False)
# 5ft
counter.count(True, False)
counter.count(True, True)
counter.count(False, True)
counter.count(False, False)
# 5ft
counter.count(True, False)
counter.count(True, True)
counter.count(False, True)
counter.count(False, False)
# 3ft
counter.count(False, False)
counter.count(True, False)
counter.count(False, False)
counter.count(False, True)
counter.count(False, False)
# 3ft
counter.count(False, False)
counter.count(True, False)
counter.count(False, False)
counter.count(False, True)
counter.count(False, False)

print(counter.get_counts())