# This file contains code on live Traffic Detection of a video file

import cv2

# Enter the path of video links below : 
video = cv2.VideoCapture('Videos/Autopilot_Dashcam.mp4')
# video = cv2.VideoCapture('Videos/Demo_Vid.mp4')
# video = cv2.VideoCapture('Videos/Vid_3_1.mp4')
# video = cv2.VideoCapture('Videos/Pedestrians_1.mp4')

car_tracker_file = 'Classifier/car_detector.xml'
pedestrian_tracker_file = 'Classifier/pedestrian_detector.xml'

car_tracker = cv2.CascadeClassifier(car_tracker_file)
pedestrian_tracker = cv2.CascadeClassifier(pedestrian_tracker_file)

while True:
    read_successful, frame = video.read()

    #safe coding 

    if  read_successful:
        grayscaled_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    else:
        break

    cars = car_tracker.detectMultiScale(grayscaled_frame)
    pedestrians = pedestrian_tracker.detectMultiScale(grayscaled_frame)


    for (x, y, w, h) in cars:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 0, 255),2)
    
    for (x, y, w, h) in pedestrians:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 255),2)


    cv2.imshow('Video',frame)

    key = cv2.waitKey(1)

    if key==81 or key==113:
        break

video.release()
