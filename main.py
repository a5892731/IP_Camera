# author: a5892731
# creation date: 20220-07-05
# last modification: 20220-07-08
# version 1.0
#
# description:
# This is a simple template for add video to Tkinter GUI

'''
requirements

system: windos
firewall turn OFF
camera address  '192.168.1.200'

'''


'''
GUI based on:
https://github.com/a5892731/GUI_template

'''


'''
imports
-tkinter: #pip install tk
-PIL: #pip install pillow
-cv2  #pip install opencv-python
'''

from tkinter import Tk
from time import time

'''
state loader is implemented to GUI in:
https://github.com/a5892731/GUI_template
project
'''

#from resources.state_machine.state_loader import StateLoader

from resources.video.ip_cam import Ip_Camera

class ProgramRun:
    from resources.gui._gui_variables import window_variables_init, set_variable_default_values
    from resources.gui._main_window import build_main_window, update_window

    '''>>> imports used in other files connected to this class'''
    from resources.gui.labels._left_menu_label import left_menu_bar, exit_program, button_1
    from resources.gui.labels._central_window import centrtal_window
    '''<<< imports used in other files connected to this class'''


    def __init__(self,):
        '''create window atributes'''
        self.window = Tk()
        self.window_variables_init()
        self.set_variable_default_values()

        '''camera initialization'''
        self.camera1 = Ip_Camera()
        self.camera1.connect_to_camera()
        self.camera_1_size = 640
        self.camera1.refresh_image(video_image_max_side_size = self.camera_1_size)

        '''build wiindow'''
        self.build_main_window()

        '''execute program'''
        self.main_loop()

    def main_loop(self):
        '''
        state loader is implemented to GUI in:
        https://github.com/a5892731/GUI_template
        project
        '''
        #device = StateLoader()

        while True:
            self.update_window()
            '''
            state loader is implemented to GUI in:
            https://github.com/a5892731/GUI_template
            project
            '''
            #device.on_event(self, 'device_locked',)  # call the state machine events




'''---------------------------------------START APP------------------------------------------------------------------'''
app = ProgramRun()