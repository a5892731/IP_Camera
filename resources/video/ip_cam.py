# author: a5892731
# creation date: 20220-07-05
# last modification: 20220-07-05
# version 1.0


# source: https://stackoverflow.com/questions/49978705/access-ip-camera-in-python-opencv
# source: https://stackoverflow.com/questions/71755653/set-a-custom-timeout-for-opencv-videocapture-read-function


import cv2




class Ip_Camera():

    def __init__(self):
        '''
        the ONVIF Device Manager program can be helpful in importing full url of ip camera
        '''
        self.url = 'rtsp://192.168.1.201:554/mpeg4?username=admin&password=E10ADC3949BA59ABBE56E057F20F883E'
        self.url2 = 'rtsp://192.168.1.200:554/mpeg4?username=admin&password=E10ADC3949BA59ABBE56E057F20F883E'
        self.connection = False


    def connect_to_camera(self):
        self.cap = cv2.VideoCapture(self.url2)


    def refresh(self):
        '''
        this function need to be in while loop
        '''
        ret, frame = self.cap.read()
        cv2.imshow('frame', frame)
        k = cv2.waitKey(1)


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
        camera.refresh()
        print("3")

    camera.disconect()



