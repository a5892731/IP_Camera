from tkinter import LabelFrame

from resources.gui.widgets.label_image import label_image



def centrtal_window(self):
    '''--------------------------------------------------------------------------------------------------------------'''

    menu = LabelFrame(self.main_label, text="CENTRAL WINDOW", background="#cfd1cf", bd=5)
    menu.grid(column=0, row=0, sticky="nesw")

    if self.camera1.connection:
        self.camera_viev1 = label_image(menu, image = self.camera1.image, column=0, row=0, text="", columnspan=1, )







'''------------------------------------------------------------------------------------------------------------------'''


