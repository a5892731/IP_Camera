from tkinter import LabelFrame

from resources.gui.widgets.label import label



def centrtal_window(self):
    '''--------------------------------------------------------------------------------------------------------------'''

    menu = LabelFrame(self.main_label, text="CENTRAL WINDOW", background="#cfd1cf", bd=5)
    menu.grid(column=0, row=0, sticky="nesw")

    L1 = label(menu, column=0, row=0,)

    L1['image'] = self.camera1.image




'''------------------------------------------------------------------------------------------------------------------'''


