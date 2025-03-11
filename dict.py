dict = {"a": 5, "b": 10}

for key, value in dict.items():
    print(key, value)
    

print(dict["a"])

dict["c"] = 15

dict.pop("c")

# Creating the dictionary
student = {
    "Name": "Alice",
    "Age": 20,
    "Courses": ["Math", "Science"]
}
# Accessing and printing the name and age
print("Name:", student["Name"])
print("Age:", student["Age"])
# Accessing and printing the list of courses
print("Courses:", student["Courses"])
# Adding a new key-value pair for GPA
student["GPA"] = 3.8
# Updating the Age
student["Age"] = 21
# Printing the updated dictionary
print("Updated Student Info:", student)
# Removing the Courses entry
student.pop("Courses")
# Printing the dictionary after removal
print("After Removing Courses:", student)

students = [{"Name": "Alice", "Age": 21, "GPA": 3.8, "Courses": ["Math", "Science"]},
            {"Name": "Bob", "Age": 22, "GPA": 3.6, "Courses": ["History", "Art"]},
            {"Name": "Charlie", "Age": 23, "GPA": 3.9, "Courses": ["Biology", "Chemistry"]} ]

person = {'name': 'bob', 'job': 'egineer', 'salary': 100000}

print(person)

person['hobby'] = 'cards'

print(person)

person['salary'] = 150000

print(person)

person.pop('job')

print(person)

store = {'apple': {'price': 2.50, 'amount': 150}, 'banana': {'price': 3.00, 'amount': 100}, 'dragonfruit': {'price': 5.50, 'amount': 50}}