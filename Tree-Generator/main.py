import tkinter as tk
import turtle
import random

LARGE_FONT = ('Verdana', 12)


class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side='top', fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        frame = TreeGenerator(container, self)
        self.frames[TreeGenerator] = frame
        frame.grid(row=0, column=0, sticky='nsew')
        self.show_frame(TreeGenerator)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class TreeGenerator(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        fields = ['Iterations: ', 'Seg Length Low: ', 'Seg Length High: ', 'Turn Angle Low: ', 'Turn Angle High: ']
        entry_defaults = [3, 8, 16, 10, 22]
        entries = []

        for i in range(len(fields)):
            lab = tk.Label(self, text=fields[i])
            lab.grid(column=10, row=(i + 5))
            en = tk.Entry(self, width=6)
            en.grid(column=11, row=(i + 5), padx=10)
            en.insert(0, entry_defaults[i])
            entries.append(en)


app = Application()
app.title('Tree Generator')
app.state('zoomed')
app.mainloop()
