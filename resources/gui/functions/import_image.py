from PIL import Image, ImageTk

from resources.gui.functions.image_resizer import re_sizer

def import_image(addres='resources/gui/pictures/iss_hd_dragon4.jpg', size=600):
    my_img = Image.open(addres)
    my_img = re_sizer(my_img, size)
    return my_img