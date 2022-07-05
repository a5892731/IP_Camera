from tkinter import *

from resources.gui.widgets.button import button

def left_menu_bar(self):
    '''--------------------------------------------------------------------------------------------------------------'''

    menu = LabelFrame(self.left_menu_label, text="MENU", background="#cfd1cf", bd=5)
    menu.grid(column=1, row=0, sticky="nesw")

    button(label=menu, text="button 1", command=self.button_1, column=0, row=0)

    for i in range(1,16):
        button(label=menu, text="", command="", column=0, row=i)  # row space
    button(label=menu, text="Exit", command=self.exit_program, column=0, row=i+1)
'''------------------------------------------------------------------------------------------------------------------'''

def button_1(self):
    self.tab_name = "button_1"



    print("button_1")



def exit_program(self): #in future: move exit function from gui to state machine
    self.tab_name = "Exit"
    self.window.destroy()