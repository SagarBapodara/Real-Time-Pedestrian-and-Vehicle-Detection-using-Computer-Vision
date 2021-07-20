# Weekly Project : Real-time Pedestrian and Car Detection using Computer Vision
# @author : Sagar Bapodara 

import streamlit as st
import cv2 as cv
import tempfile

st.markdown("<h1 style='text-align: center; color: black;'>Computer Vision Traffic Detection</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: black;'>This Web-App uses OpenCV for processing purposes.</h3>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: black;'>Blue Color = Cars/Vehicles, White Color = Pedestrian </h4>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: black;'>Web App created by Sagar Bapodara for demo purpose.</h4>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center; color: black;'>Ignore the Video Error, it's just waiting for an parameter defined above, as soon as upload the video it vanishes.</h5>", unsafe_allow_html=True)


car_tracker_file = 'Classifier/car_detector.xml'
pedestrian_tracker_file = 'Classifier/pedestrian_detector.xml'

car_tracker = cv.CascadeClassifier(car_tracker_file)
pedestrian_tracker = cv.CascadeClassifier(pedestrian_tracker_file)

f = st.file_uploader("Choose a Video")

if f:
   tfile = tempfile.NamedTemporaryFile(delete=False) 
   tfile.write(f.read())
   vf = cv.VideoCapture(tfile.name)
   # Opens the Video file
   stframe = st.empty()
   i=1

   while(vf.isOpened()):
       ret, frame = vf.read()
       if ret:
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        cars = car_tracker.detectMultiScale(gray)
        pedestrians = pedestrian_tracker.detectMultiScale(gray)
        for (x, y, w, h) in cars:
            cv.rectangle(frame, (x,y), (x+w, y+h), (0, 0, 255),2)
        for (x, y, w, h) in pedestrians:
            cv.rectangle(frame, (x,y), (x+w, y+h), (255, 255, 255),2)
            
        stframe.image(frame)

video.release()

# Quick Fix to video.release() error : To ignore the video error, you can comment the 'video.release()' line, but this not advisable since at the end of the process resources should be freed.