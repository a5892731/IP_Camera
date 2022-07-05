# author: a5892731

# source: https://stackoverflow.com/questions/49978705/access-ip-camera-in-python-opencv


import cv2





#class Ip_Camera():






'''
the ONVIF Device Manager program can be helpful in importing full url of ip camera
'''
url = 'rtsp://192.168.1.201:554/mpeg4?username=admin&password=E10ADC3949BA59ABBE56E057F20F883E'


cap = cv2.VideoCapture(url)




while(True):
    ret, frame = cap.read()
    cv2.imshow('frame',frame)
    print("Running...")
    k = cv2.waitKey(1)




cv2.destroyAllWindows()