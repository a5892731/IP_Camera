# author: a5892731
# date: 11.05.2022
# last update: 30.05.2022
# version: 1.1
#
# description:
# This is a simple template for programs with Graphic User Interface

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



class ProgramRun:
    from resources.gui._gui_variables import window_variables_init, set_variable_default_values, \
                                             import_variables_to_gui, export_variables_from_gui
    from resources.gui._main_window import build_main_window, update_window

    '''>>> imports used in other files connected to this class'''
    from resources.gui.labels._left_menu_label import left_menu_bar, exit_program, button_1





    '''<<< imports used in other files connected to this class'''
    def __init__(self,):
        self.window = Tk()
        self.window_variables_init()
        self.set_variable_default_values()
        self.build_main_window()

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