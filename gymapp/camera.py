from imutils.video import VideoStream
from imutils.video import FPS
import imutils
import cv2
import numpy as np
from django.conf import settings



class FaceDetect(object):
	def __init__(self):
		self.vs = VideoStream(src=0).start()
		self.fps = FPS().start()

	def __del__(self):
		cv2.destroyAllWindows()

	def get_frame(self):
		frame = self.vs.read() #frame nicchi
		frame = cv2.flip(frame,1)

		frame = imutils.resize(frame, width=600) #dimensions set korchi
		(h, w) = frame.shape[:2]

		self.fps.update() #fps meter update korchi
		ret, jpeg = cv2.imencode('.jpg', frame)
		return jpeg.tobytes()
		