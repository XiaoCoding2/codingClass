
'''

class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return self.name
    

p1 = person('Bob', 12)
print(p1)
print(p1.name, p1.age)
'''

'''
class book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f'{self.title} by {self.author}, ({self.year})'
    
harry_potter = book('Harry Potter', 'JK Rowling', 2001)
print(harry_potter)
'''

from tkinter import *
# Constants for the game
GAME_WIDTH = 1000
GAME_HEIGHT = 700
BACKGROUND_COLOR = "#33ffaf"
RECT_SIZE = 32  # Size of the rectangle
MOVE_DISTANCE = 10  # Distance to move the rectangle with each key press
# Create the main window
window = Tk()
window.title("Move the Rectangle")
window.resizable(False, False)
# Create a canvas and pack it into the window
canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()
# Update the window to set its size and position
window.update()
# Center the window on the screen
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))
window.geometry(f"{window_width}x{window_height}+{x}+{y}")
# Draw a rectangle on the canvas
rectangle = canvas.create_rectangle(100, 100, 100 + RECT_SIZE, 100 + RECT_SIZE, fill="#ffbe33")
# Function to move the rectangle up
def move_up(event):
    canvas.move(rectangle, 0, -MOVE_DISTANCE)
# Function to move the rectangle down
def move_down(event):
    canvas.move(rectangle, 0, MOVE_DISTANCE)
# Function to move the rectangle left
def move_left(event):
    canvas.move(rectangle, -MOVE_DISTANCE, 0)
# Function to move the rectangle right
def move_right(event):
    canvas.move(rectangle, MOVE_DISTANCE, 0)
# Bind the WASD keys to movement functions
window.bind('<w>', move_up)
window.bind('<s>', move_down)
window.bind('<a>', move_left)
window.bind('<d>', move_right)
# Start the Tkinter event loop
window.mainloop()
