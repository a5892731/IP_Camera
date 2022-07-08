from tkinter import Label
from PIL import Image



import numpy as np

'''
https://www.tutorialspoint.com/python/tk_label.htm
https://www.youtube.com/watch?v=ypwOOtU2qus
'''

def label_image(label, image, column = 0, row = 0, text = "", columnspan = 1, ):
    label = Label(label, font=("Arial", 12), image=image, text=text, background="#cfd1cf")
    label.grid(column=column, row=row, columnspan=columnspan, sticky="nesw")
    return label

