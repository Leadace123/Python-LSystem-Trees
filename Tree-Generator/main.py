from tkinter import *
import turtle
import random

# Creates Root Window
root = Tk()
root.title('drawing GUI')
root.state('zoomed')
root.config(bg='grey')
w = root.winfo_screenwidth()
h = root.winfo_screenheight()


is_drawing = 0


# Generates Tree
def generate_tree():
    clear_scene()
    global is_drawing
    is_drawing = 1
    iterate_path()


# Clears any generated Trees
def clear_scene():
    if is_drawing == 0:
        tree_turtle.clear()
        tree_turtle.hideturtle()
        tree_turtle.penup()
        tree_turtle.setposition(start_pos)
        tree_turtle.setheading(start_heading)
        tree_turtle.showturtle()
        tree_turtle.pendown()


# Iterates path string
def iterate_path():
    cur_string = 'F'
    new_string = ""
    for each in range(int(entries[0].get())):
        for char in cur_string:
            if char == "F":
                new_string += "FF+[+F-F-F]-[-F+F+F]"
            else:
                new_string += char
        cur_string = new_string
        new_string = ""
    draw_tree(cur_string)


# Draws tree
def draw_tree(path):
    saved_pos = []
    saved_angle = []
    for each in path:
        if each == "F":
            tree_turtle.forward(random.randrange(int(entries[1].get()), int(entries[2].get())))
        elif each == "+":
            tree_turtle.left(-random.randrange(int(entries[3].get()), int(entries[4].get())))
        elif each == "-":
            tree_turtle.left(random.randrange(int(entries[3].get()), int(entries[4].get())))
        elif each == "[":
            saved_pos.append(tree_turtle.pos())
            saved_angle.append(tree_turtle.heading())
        elif each == "]":
            tree_turtle.penup()
            tree_turtle.setheading(saved_angle[-1])
            del saved_angle[-1]
            tree_turtle.setposition(saved_pos[-1])
            del saved_pos[-1]
            tree_turtle.pendown()
    tree_turtle.hideturtle()
    global is_drawing
    is_drawing = 0


# Setup turtle canvas & place turtle close to bottom of screen
canvas = Canvas(root, width=(w-200), height=h)
canvas.grid(row=0, column=2, rowspan=100)
tree_turtle = turtle.RawTurtle(canvas)
tree_turtle.speed(-100)
tree_turtle.hideturtle()
tree_turtle.penup()
tree_turtle.sety(-(h/2) + 100)
tree_turtle.left(90)
tree_turtle.showturtle()
tree_turtle.pendown()
start_pos = tree_turtle.pos()
start_heading = tree_turtle.heading()

# Setup entry fields and buttons

fields = ['Iterations: ', 'Seg Length Low: ', 'Seg Length High: ', 'Turn Angle Low: ', 'Turn Angle High: ']
entry_defaults = [3, 8, 16, 10, 22]
entries = []

for i in range(len(fields)):
    lab = Label(root, text=fields[i])
    lab.grid(column=0, row=i)
    en = Entry(root, width=6)
    en.grid(column=1, row=i, padx=10)
    en.insert(END, entry_defaults[i])
    entries.append(en)

generate = Button(root, font='bold', text='Generate', command=generate_tree)
generate.grid(column=0, row=6)


root.mainloop()
