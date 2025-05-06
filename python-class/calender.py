
class MyCalendar(object):

    def __init__(self):
        self.cal2 = [[0, 0]]
    def book(self, start, end):
        for x in self.cal2: 
            if not (end <= x[0] or start >= x[1]): return False 
        self.cal2.append([start, end])
        return True
# Instantiate the MyCalendar class
calendar = MyCalendar()


def tests():
    # Test case 1: Booking an event from 10 to 20
    assert calendar.book(10, 20) == True, "Test case 1 failed"
    print('passed 1')
    # Test case 2: Booking an event from 15 to 25 (should return False due to overlap)
    assert calendar.book(15, 25) == False, "Test case 2 failed"
    print('passed 2')
    # Test case 3: Booking an event from 20 to 30 (should return True, no overlap)
    assert calendar.book(20, 30) == True, "Test case 3 failed"
    print('passed 3')
    # Test case 4: Booking an event from 5 to 10 (should return True, no overlap)
    assert calendar.book(5, 10) == True, "Test case 4 failed"
    print('passed 4')
    # Test case 5: Booking an event from 25 to 35 (should return True, no overlap)
    assert calendar.book(25, 35) == False, "Test case 5 failed"
    print('passed 5')
    # Test case 6: Booking an event from 30 to 40 (should return True, no overlap)
    assert calendar.book(30, 40) == True, "Test case 6 failed"
    print('passed 6')
    # If no assertion errors occur, print success message
    print("All test cases passed!")

tests()


'''
        for x in range(start, end):
            self.cal.append(x)
        self.cal.sort()
        print(self.cal, '1')
        print(self.cal2, '2')
        
        for x in self.cal:
            if self.cal2 == [123123]:
                self.cal2.clear()
                print(self.cal2, '4')
            if x not in self.cal2:
                self.cal2.append(x)
                print(self.cal2, '5')
            else:
                self.cal.clear()
                print(self.cal2, '6')
                return False
        self.cal.clear()
        return True
'''