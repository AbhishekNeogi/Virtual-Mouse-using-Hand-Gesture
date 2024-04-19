from operator import index
from os import read
import mediapipe as mp
import cv2
import numpy as np
from mediapipe.framework.formats import landmark_pb2
import time 
from math import sqrt
from torch import view_as_complex
import win32api
import pyautogui

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
click = 1

video =cv2.VideoCapture(0)
# def next_click():
#     pyautogui.click()
#     vritual_mouse()

with mp_hands.Hands(min_detection_confidence = 0.8, min_tracking_confidence = 0.9) as hands :
	while video.isOpened():
		_, frame = video.read()

		image = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

		image = cv2.flip(image,1)

		imageHeight, imageWidth , _ = image.shape

		results = hands.process(image)

		image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

		if results.multi_hand_landmarks:
			for num, hand in enumerate(results.multi_hand_landmarks):
				mp_drawing.draw_landmarks(image, hand , mp_hands.HAND_CONNECTIONS,mp_drawing.DrawingSpec(color = (250,44,250), thickness = 5,circle_radius = 5),)


		if results.multi_hand_landmarks !=None:
			for handLandmarks in results.multi_hand_landmarks : 
				for point in mp_hands.HandLandmark:

					normalizedLandmark = handLandmarks.landmark[point]
					pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x, normalizedLandmark.y , imageWidth, imageHeight)
					point =str(point)
					# print(point)
					if point == 'HandLandmark.INDEX_FINGER_TIP':
						try:
							indexfingertip_x = int(pixelCoordinatesLandmark[0])
							indexfingertip_y = int(pixelCoordinatesLandmark[1])
							# print(indexfingertip_x,indexfingertip_y)
							cv2.circle(image,(indexfingertip_x,indexfingertip_y),10,(0,0,0),10)
							# pyautogui.moveTo(indexfingertip_x*5, indexfingertip_y*3)
							win32api.SetCursorPos((indexfingertip_x*3,indexfingertip_y*4))

						except:
							print("index capture failed")
							pass

					elif point == 'HandLandmark.THUMB_TIP':
						try:
							thumbfingertip_x = int(pixelCoordinatesLandmark[0])
							thumbfingertip_y = int(pixelCoordinatesLandmark[1])
							# print(thumbfingertip_x,thumbfingertip_y)
							cv2.circle(image,(thumbfingertip_x,thumbfingertip_y),10,(225,0,0),10)

						except:
							print("thumb capture failed")
							pass
					try :
						# Distance_x = np.sqrt(abs((indexfingertip_x)**2-(thumbfingertip_x)**2))
						# Distance_y = np.sqrt(abs((indexfingertip_y)**2-(thumbfingertip_y)**2))
						dist = int(np.sqrt((indexfingertip_x-thumbfingertip_x)**2+(indexfingertip_y-thumbfingertip_y)**2))
						print(dist)
			
						
						if dist<=30 :
							pyautogui.click()
							# last_click_time = time.time()
       
							# next_click()
							# vritual_mouse()
							
					except:
						print("Click failed")
						pass
				cv2.imshow("Hand tracking",image)

			if cv2.waitKey(1) & 0xFF == ord('q'):
				break
video.release()
cv2.destroyAllWindows()

	
	
# vritual_mouse()
