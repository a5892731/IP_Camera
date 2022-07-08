# author: a5892731
# creation date: 20220-07-05
# last modification: 20220-07-08
# version 1.0


# source: https://stackoverflow.com/questions/49978705/access-ip-camera-in-python-opencv
# source: https://stackoverflow.com/questions/71755653/set-a-custom-timeout-for-opencv-videocapture-read-function


import cv2

from PIL import Image, ImageTk


class Ip_Camera():

    def __init__(self):
        '''
        the ONVIF Device Manager program can be helpful in importing full url of ip camera

        rtsp://192.168.1.201:554/mpeg4?username=admin&password=E10ADC3949BA59ABBE56E057F20F883E
        '''

        self.ip = '192.168.1.200'
        #self.ip = '192.168.1.201'
        self.dns = '192.168.1.1'
        self.http_port = '80'
        self.rtsp_port = '554'
        self.username = "admin"
        self.password = 'E10ADC3949BA59ABBE56E057F20F883E'

        self.frame_width= 640
        self.frame_height = 480

        self.url = 'rtsp://' + self.ip + ':' + self.rtsp_port + \
                   '/mpeg4?' + 'username=' + self.username + '&password=' + self.password

        self.connection = False

    def connect_to_camera(self):
        '''
        ping camera?

        '''

        self.cap = cv2.VideoCapture(self.url)

        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.frame_width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.frame_height)

    def refresh_standard(self):
        '''
        this function need to be in while loop
        '''
        ret, frame = self.cap.read()

        cv2.imshow('frame', frame)
        k = cv2.waitKey(1)

    def refresh_image(self, max_side_size = 600):
        '''
        this function need to be in while loop
        '''
        ret, frame = self.cap.read()

        img = self.resize_image(image = Image.fromarray(frame), max_side_size = 600)
        try:
            self.image = ImageTk.PhotoImage(img)
        except:
            cv2.destroyAllWindows()

    def resize_image(self, image, max_side_size):
        width, height = image.size

        if height > width:
            scale = height / max_side_size
            width = width / scale
            height = height / scale
        else:
            scale = width / max_side_size
            width = width / scale
            height = height / scale

        width = int(width)
        height = int(height)

        return image.resize((width, height))

    def disconnect(self):
        '''
        this function should be called in the end of program
        '''
        cv2.destroyAllWindows()


if __name__ == "__main__":
    camera = Ip_Camera()
    print("0")
    camera.connect_to_camera()
    print("1")
    while True:
        print("2")
        camera.refresh_standard()
        print("3")

    camera.disconect()



