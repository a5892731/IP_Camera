from PIL import Image, ImageTk

def re_sizer(image, max=600):
    width, height = image.size

    if height > width:
        scale = height / max
        width = width / scale
        height = height / scale
    else:
        scale = width / max
        width = width / scale
        height = height / scale

    image = image.resize((int(width), int((height))), Image.ANTIALIAS)
    my_image = ImageTk.PhotoImage(image)
    #return int(width), int(height)
    return my_image