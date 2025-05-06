
class calcs:
    def calc_(self):
        sum1 = 0
        for x in range(0, 100):
            a = (1/(2**x))
            sum1 += a
            print(sum1)
    
    def calc2_(self):
        user_input = float(input("Input here: "))
        range_input = float(input("Enter range(in percents): "))
        #------------------------------
        percent_range = 0.01*range_input
        num_range = user_input*percent_range
        lower_range = user_input-num_range
        upper_range = user_input+num_range
        #------------------------------
        print(percent_range)
        print(num_range)
        print(lower_range)
        print(upper_range)

    def calc3_(self):
        for x in range(15):
            radius = float(input('Radius here: '))
            rsq = radius**2
            ans = rsq*3.14
            print(ans)

    def calc4_(self):
        for x in range(3):
            type_ = input("Which(ex:c 4.71): ")
            type_list = type_.split(' ')
            type_type = type_list[0]
            type_num = float(type_list[1])
            if(type_type=='c'):print(f'r = {type_num}/2*pi, d = 2r')
            elif(type_type=='r'):print(f'd = {type_num}*2, c = 2*pi*r')
            elif(type_type == 'd'):print(f'c = {type_num}*pi, r = d/2')
    #
    #NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE
    #NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE
    #NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE
    #Regular Calculator
    def calc5_(self):
        run = True
        while run:
            eq = input("----------\nHere: ")
            if(eq=="stop"):run=False
            else:exec(f"print({eq})")

    def calc6_(self):
        count = 0
        remainder = int(input("What's the desired remainder?: "))
        divisor = int(input("Divisor: "))
        between_ = input("what's the range?: ")
        between_nums = between_.split()
        between = range(int(between_nums[0]), int(between_nums[1]))
        for num in(between):
            if(num%divisor==remainder): count += 1
        print(count)

    def calc7_(self):
        qs = {}
        for x in range(1, 16): qs[x] = ''
        print(qs)

    #-prints mean, median, mode, and range of the data
    def calc8_(self):
        import os
        import statistics as S
        from termcolor import colored as C
        #-adds a title and space between the text and output in the terminal
        print("--------------------")
        print("Data Point Calculator for Mean, Median, Mode, and Range")
        print("--------------------")
        while True:
            #-asks for the data in format NumberSpaceNumber
            num = input(f"Enter numbers({C("NumberSpaceNumber",'blue')}): ")
            #-stops the loop if input is stop
            if num == 'stop': return False
            #clears terminal if input is clear
            elif num == 'clear':
                os.system('cls')
                calcs.calc8_(self)
            #-puts the data into a list of numbers
            nums_str = num.split()
            nums = [float(x) for x in nums_str if x.isdigit() == True]
            try:
                #-prints the measures of the data
                print(f"Numbers = [ {C(str(nums).replace('[','').replace(']','').replace(',',' '),'green')} ]")
                print(f"{C("---Data Points---",'yellow')}")
                #-prints the info
                print(f"{C("mean", 'cyan')} = {C(round(S.mean(nums),3),'green')}")
                print(f"{C("median", 'cyan')} = {C(round(S.median(nums),3),'green')}")
                print(f"{C("mode", 'cyan')} = {C(round(S.mode(nums),3),'green')}")
                print(f"{C("range", 'cyan')} = {C(max(nums)-min(nums),'green')}")
                #-line to separate data
                print(f"--------------------")
            except:
                print(f"{C("Error", 'red')}")
                print("--------------------")
                print(f"{C("Error: Invalid Response", 'red')}: please use proper syntax({C("NumberSpaceNumber",'blue')})")
                print(f"--------------------")
    def calc9_(self):
        for x in range(20):
            print(7**x,x)

    def calc10_(self):
        import math as M
        for x in range(1,15 +1):
            print(f'{M.factorial(x)}, {x}')

    def calc11_(self):
        import math as M
        sqr = M.sqrt(784)
        if sqr.is_integer() == True:
            return True
        return False

    def calc12_(self):
        import sys
        import sympy as Sy
        print("--------------------",flush=True)
        primes = []
        print("text")
        for x in range(2**24):
            if Sy.isprime(x)==True:
                primes.append(x)
                sys.stdout.write('\x1b[1A')
                print(f"currently on {x},generated {len(primes)} primes")
        with open('primes.nums','w') as prime_nums:
            for line in primes:
                prime_nums.write(str(line)+' ')
        print("Done")

    def calc13_(self):
        ex=input("expression: ")
        ex="12x+8"
        Sign = [x for x in ex if x in ["+","-","*","/",">","<"]]
        Var = [x for x in ex if x.isdigit()==False and x not in Sign]
        Nums = [int(x) for x in ex if x.isdigit()==True]
        print(f"Signs={Sign},Var={Var},Nums={Nums}")
    def calc14_(self):
        password = 1_000_000_000_000
        #
        import sys
        import time
        import termcolor as Tcr
        number = 0
        locked = True
        while locked:
            number += 1
            if number == password:
                print(Tcr.colored(f"Password = {number}","green"))
                return False
            if number > 1_000_000_000_000_000:
                print(Tcr.colored("Password not found.","red"))
                return False
            else:
                pass
                #sys.stdout.write('\x1b[1A')
                #print(f"Currently on {number}")
    def calc15_(self):
        import math
        print(math.remainder(1092387456,9))
    def calc16_(self):
        import random as rdm
        import sys
        password=0.1
        #
        print("t")
        while True:
            number=rdm.choice(range(0,10))
            if number == password:
                print(number)
                return False
            sys.stdout.write('\x1b[1A')
            print(number)
    def calc17_(self):
        import random as rdm
        import sys
        print("__________")
        print("a")
        while True:
            sys.stdout.write('\x1b[1A')
            for x in range(10):
                print(rdm.choice(range(0,10)),end='')
            print()
    def calc18_(self):
        import random as rdm
        import os
        while True:
            os.system('cls')
            for x in range(10):
                print(rdm.choice(range(0,10)),end='')
            print()
    def calc19_(self):
        import sympy as Sy
        num=int(input("Number: "))
        if Sy.isprime(num)==True:
            return True
        return False
    def calc20_(self):
        num_s=[x**2 for x in range(1,20+1)]
        for x in range(1,20+1):
            print(int((x**2)*3.14),num_s[x-1],x)
    def calc21_(self):
        from sys import stdout as syslog
        while True:
            Eq=input("Whole Per. ")
            eq=list(map(float,Eq.split()))
            eq[1]=eq[1]*0.01
            syslog.write(f"{eq[0]+eq[0]*eq[1]}\n")

calculators=calcs()

calculators.calc21_() #NOTE: Can be replaced with any function

#