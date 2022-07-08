from tkinter import LabelFrame

from resources.video.ip_cam import Ip_Camera

from resources.gui.widgets.button import button

def left_menu_bar(self):
    '''--------------------------------------------------------------------------------------------------------------'''

    menu = LabelFrame(self.left_menu_label, text="MENU", background="#cfd1cf", bd=5)
    menu.grid(column=1, row=0, sticky="nesw")

    button(label=menu, text="PLAY", command=self.play, column=0, row=0)
    button(label=menu, text="PLAY", command=self.stop, column=0, row=1)

    for i in range(2,16):
        button(label=menu, text="", command="", column=0, row=i)  # row space
    button(label=menu, text="Exit", command=self.exit_program, column=0, row=i+1)
'''------------------------------------------------------------------------------------------------------------------'''

def play(self):
    '''camera initialization'''
    self.camera1.connect_to_camera()
    self.camera1.refresh_image(video_image_max_side_size=self.camera_1_size)

    print("play")
def stop(self):
    self.camera1.connection = False
    print("stop")




def exit_program(self): #in future: move exit function from gui to state machine
    self.tab_name = "Exit"
    self.window.destroy()