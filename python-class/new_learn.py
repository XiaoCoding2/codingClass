
from tkinter import * # type: ignore
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
# Start the Tkinter event loop

'''
for x in range(100):
    canvas.move(rectangle, MOVE_DISTANCE, 0)
    print(f'moved, {x}')
'''


#FIXME HACK TODO XXX These are code comments
