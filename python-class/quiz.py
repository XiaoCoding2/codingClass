
def quiz():
    q = {
        "What element does the chemical symbol Au stand for?": 'gold',
        "What is the smallest planet in our solar system?": 'mercury',
        "How many feet are in a yard?": 'three'
        }
    corrects = 0
    for key, value in q.items():
        question = input(key)
        if question == value:
            corrects += 1
            print("correct")
        else:
            print("wrong")
    print(f"You got {corrects}/3.")

#quiz()

grades = {"Alice": 85, 
          "Bob": 92, 
          "Charlie": 78, 
          "Diana": 95, "Eve": 88
        }

def find_grades(name_, grades):
    for name, grade in grades.items():
        if name == name_:
            return grade
    return 'Not found'
    
print(find_grades('Charlie', grades))
