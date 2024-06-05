from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, StreamingHttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import *
from datetime import datetime


# Create your views here.

def home(request):
	return render(request, 'index.html')

def About(request):
	return render(request, 'about.html')

def Contact(request):
	return render(request, 'contact.html')


# def user_signup(request):
# 	if request.method == 'POST':
# 		fname = request.POST['fname']
# 		lname = request.POST['lname']
# 		user = request.POST['username']
# 		pass1 = request.POST['password']
# 		pass2 = request.POST['passwordconf']
# 		emailInp = request.POST['email1']
# 		acType = request.POST['acType']
# 		now = datetime.now()
# 		if(pass1 == pass2):
# 			user_exist = User.objects.filter(email=emailInp).exists()
# 			if user_exist:
# 				messages.error(
# 					request, 'This email id already exists. Please use a different one.')
# 				return HttpResponseRedirect("/signup/")
# 			else:
# 				if(pass1.isalnum() and pass1.isalpha() == False and pass1.isdigit() == False and len(pass1) >= 8):
# 					if str(pass1).find(user) != -1:
# 						messages.error(
# 							request, 'Password should not contain username.')
# 						return HttpResponseRedirect("/signup/")
# 					else:
# 						myuser = User.objects.create_user(user, emailInp, pass1)
# 						myuser.first_name = fname
# 						myuser.last_name = lname
# 						myuser.acCreated = now
# 						if acType == "activeUser":
# 							myuser.is_staff=False
# 						elif acType == "staffUser" or acType == "adminUser":
# 							myuser.is_staff=True
# 						myuser.save()

# 						# return HttpResponseRedirect('/')
# 						# for login after signup
# 						user = authenticate(request, username=user, email=emailInp, password=pass1)
# 						# print(user)
# 						if user is not None:
# 							if user.is_active:
# 								login(request, user)
# 								return HttpResponseRedirect('/')
# 							elif request.user.is_staff:
# 								login(request, user)
# 								print("welcome staff")
# 								return HttpResponseRedirect('/')
# 						else:
# 							messages.error(request, 'User not found')
# 							return HttpResponseRedirect('/signup/')                
# 				else:
# 					messages.error(
# 						request, 'Password should be alphanumeric and should contain atleast 8 characters.')
# 					return HttpResponseRedirect("/signup/")
# 		else:
# 			messages.error(
# 				request, "Password Not match. Re-enter password correctly.")
# 			return HttpResponseRedirect("/signup/")
# 	else:
# 		return render(request, 'signup.html')
	
# def user_login(request):
# 	if not request.user.is_authenticated:
# 		if request.method == 'POST':
# 			username = request.POST.get('username')
# 			emailInp = request.POST.get('email1')
# 			password = request.POST.get('password')
# 			user = authenticate(request, username=username, email=emailInp, password=password)
# 			# print(user)
# 			if user is not None:
# 				if user.is_active:
# 					login(request, user)
# 					return HttpResponseRedirect('/')
# 				elif request.user.is_staff:
# 					login(request, user)
# 					print("welcome staff")
# 					return HttpResponseRedirect('/')
# 			else:
# 				messages.error(
# 					request, "Password Not match. Re-enter password correctly.")
# 				return HttpResponseRedirect('/login/')
				
# 				# if user.is_staff:
# 				#     login(request, user)
# 				#     return HttpResponseRedirect('/')
# 				# else:
# 				#     login(request, user)
# 				#     return HttpResponseRedirect('/')
# 		else:
# 			return render(request, 'login.html')
# 	else:
# 		return HttpResponseRedirect('/')
	
# def user_logout(request):
# 	logout(request)
# 	return HttpResponseRedirect('/')


def bmicalculator(request):
	return render(request, 'bmiCalc.html')

def viesEquip(request):
	return render(request, 'view_equipment.html')

def viewMem(request):
	return render(request, 'view_member.html')

def viewPlan(request):
	return render(request, 'view_plan.html')

def viewEnq(request):
	enq = Enquiry.objects.all()
	d = {'enq': enq}
	return render(request, 'view_enquiry.html', d)

def delEnq(request,pid):	
	enquiry = Enquiry.objects.get(id=pid)
	enquiry.delete()
	return redirect('view_enquiry')

def addEnq(request):
	if not request.user.is_authenticated:
		messages.error(request, 'Only rigistered users are allowed')
		return redirect('/social/login_social/')
	else:
		if request.method == 'POST':
			n = request.POST['name']
			c = request.POST['contact']
			e = request.POST['emailid']
			a = request.POST['age']
			g = request.POST['gender']
			Enquiry.objects.create(name=n, contact=c, emailid=e, age=a, gender=g)
			messages.success(request, "New enquiry added successfully")
	return render(request, 'add_enquiry.html')


#/AI trainer
# from .AItrainer.in_out import in_out
# from .AItrainer.motion import noise
# from .AItrainer.rect_noise import rect_noise
# from .AItrainer.record import record
# from PIL import Image, ImageTk
# from .AItrainer.find_motion import find_motion
# from .AItrainer.identify import maincall
# from .AItrainer.count import count
# from .AItrainer.PushUpCounter import push_up
# from .AItrainer.curl_counter import curl
# from .AItrainer.squat import squat_count
# from .AItrainer.crunch import crunch
# from .AItrainer.pull import pull
# from .AItrainer.walk import gen_frames
# from .AItrainer.PushIt import push
# from .AItrainer.jump import jump
# from .AItrainer.squattt import squat_count
# from .AItrainer.contra import contra

import cv2
# import threading
# from django.views.decorators import gzip
from imutils.video import VideoStream
from imutils.video import FPS
import imutils
# from .camera import FaceDetect
# from .curl_counter import VideoCamera
from .walk import walk
from .squattt import squat_count
from .PushIt import push
from .pull import pull
from .jump import jump
from .crunch import crunch
import threading
from django.views.decorators import gzip
# from .chestpress import chest
# from .curl_counter import curl

def gen(camera):
	while True:
		frame = camera.get_frame()
		yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

class VideoCamera1(object):
	def __init__(self):
		# self.cap = cv2.VideoCapture("https://192.168.100.4:8080/video")
		self.cap = cv2.VideoCapture(0)
	def __del__(self):
		self.cap.release()
	def get_frame(self):
		ret, jpeg = cv2.imencode('.jpg', walkAi(self))
		return jpeg.tobytes()
			

def AiTrainerHome(request):
	if request.user.is_authenticated:
		return render(request, 'AiTrainerHome.html')
	else:
		messages.error(request, 'Only registered users allowed')
		return HttpResponseRedirect('/social/login/')

# def showCam(request):
# 	return StreamingHttpResponse(gen(FaceDetect()), content_type='multipart/x-mixed-replace; boundary=frame')
@gzip.gzip_page
def showCam(request):
	try:
		cam = VideoCamera()
		return StreamingHttpResponse(gen(cam), content_type="multipart/x-mixed-replace;boundary=frame")
	except:
		pass
	return render(request, 'video.html')
import pandas as pd
import cv2
import numpy as np
# from mediapipe import tasks
from .mediapipe import solutions
from . import mediapipe as mp
import mediapipe as mp
from .utils import *

class BodyPartAngle:
	def __init__(self, landmarks):

		self.landmarks = landmarks

	def angle_of_the_left_arm(self):
		l_shoulder = detection_body_part(self.landmarks, "LEFT_SHOULDER")
		l_elbow = detection_body_part(self.landmarks, "LEFT_ELBOW")
		l_wrist = detection_body_part(self.landmarks, "LEFT_WRIST")
		return calculate_angle(l_shoulder, l_elbow, l_wrist)

	def angle_of_the_right_arm(self):
		r_shoulder = detection_body_part(self.landmarks, "RIGHT_SHOULDER")
		r_elbow = detection_body_part(self.landmarks, "RIGHT_ELBOW")
		r_wrist = detection_body_part(self.landmarks, "RIGHT_WRIST")
		return calculate_angle(r_shoulder, r_elbow, r_wrist)

	def angle_of_the_left_leg(self):
		l_hip = detection_body_part(self.landmarks, "LEFT_HIP")
		l_knee = detection_body_part(self.landmarks, "LEFT_KNEE")
		l_ankle = detection_body_part(self.landmarks, "LEFT_ANKLE")
		return calculate_angle(l_hip, l_knee, l_ankle)

	def angle_of_the_right_leg(self):
		r_hip = detection_body_part(self.landmarks, "RIGHT_HIP")
		r_knee = detection_body_part(self.landmarks, "RIGHT_KNEE")
		r_ankle = detection_body_part(self.landmarks, "RIGHT_ANKLE")
		return calculate_angle(r_hip, r_knee, r_ankle)

	def angle_of_the_neck(self):
		r_shoulder = detection_body_part(self.landmarks, "RIGHT_SHOULDER")
		l_shoulder = detection_body_part(self.landmarks, "LEFT_SHOULDER")
		r_mouth = detection_body_part(self.landmarks, "MOUTH_RIGHT")
		l_mouth = detection_body_part(self.landmarks, "MOUTH_LEFT")
		r_hip = detection_body_part(self.landmarks, "RIGHT_HIP")
		l_hip = detection_body_part(self.landmarks, "LEFT_HIP")

		shoulder_avg = [(r_shoulder[0] + l_shoulder[0]) / 2,
						(r_shoulder[1] + l_shoulder[1]) / 2]
		mouth_avg = [(r_mouth[0] + l_mouth[0]) / 2,
					 (r_mouth[1] + l_mouth[1]) / 2]
		hip_avg = [(r_hip[0] + l_hip[0]) / 2, (r_hip[1] + l_hip[1]) / 2]

		return abs(180 - calculate_angle(mouth_avg, shoulder_avg, hip_avg))

	def angle_of_the_abdomen(self):
		# calculate angle of the avg shoulder
		r_shoulder = detection_body_part(self.landmarks, "RIGHT_SHOULDER")
		l_shoulder = detection_body_part(self.landmarks, "LEFT_SHOULDER")
		shoulder_avg = [(r_shoulder[0] + l_shoulder[0]) / 2,
						(r_shoulder[1] + l_shoulder[1]) / 2]

		# calculate angle of the avg hip
		r_hip = detection_body_part(self.landmarks, "RIGHT_HIP")
		l_hip = detection_body_part(self.landmarks, "LEFT_HIP")
		hip_avg = [(r_hip[0] + l_hip[0]) / 2, (r_hip[1] + l_hip[1]) / 2]

		# calculate angle of the avg knee
		r_knee = detection_body_part(self.landmarks, "RIGHT_KNEE")
		l_knee = detection_body_part(self.landmarks, "LEFT_KNEE")
		knee_avg = [(r_knee[0] + l_knee[0]) / 2, (r_knee[1] + l_knee[1]) / 2]

		return calculate_angle(shoulder_avg, hip_avg, knee_avg)


class TypeOfExercise(BodyPartAngle):
	def __init__(self, landmarks):
		super().__init__(landmarks)

	def push_up(self, counter, status):
		left_arm_angle = self.angle_of_the_left_arm()
		right_arm_angle = self.angle_of_the_left_arm()
		avg_arm_angle = (left_arm_angle + right_arm_angle) // 2

		if status:
			if avg_arm_angle < 70:
				counter += 1
				status = False
		else:
			if avg_arm_angle > 160:
				status = True

		return [counter, status]

	# def push_up_method_2():

	def pull_up(self, counter, status):
		nose = detection_body_part(self.landmarks, "NOSE")
		left_elbow = detection_body_part(self.landmarks, "LEFT_ELBOW")
		right_elbow = detection_body_part(self.landmarks, "RIGHT_ELBOW")
		avg_shoulder_y = (left_elbow[1] + right_elbow[1]) / 2

		if status:
			if nose[1] > avg_shoulder_y:
				counter += 1
				status = False

		else:
			if nose[1] < avg_shoulder_y:
				status = True

		return [counter, status]

	def squat(self, counter, status):
		left_leg_angle = self.angle_of_the_right_leg()
		right_leg_angle = self.angle_of_the_left_leg()
		avg_leg_angle = (left_leg_angle + right_leg_angle) // 2

		if status:
			if avg_leg_angle < 70:
				counter += 1
				status = False
		else:
			if avg_leg_angle > 160:
				status = True

		return [counter, status]

	def walk(self, counter, status):
		right_knee = detection_body_part(self.landmarks, "RIGHT_KNEE")
		left_knee = detection_body_part(self.landmarks, "LEFT_KNEE")

		if status:
			if left_knee[0] > right_knee[0]:
				counter += 1
				status = False

		else:
			if left_knee[0] < right_knee[0]:
				counter += 1
				status = True

		return [counter, status]

	def sit_up(self, counter, status):
		angle = self.angle_of_the_abdomen()
		if status:
			if angle < 55:
				counter += 1
				status = False
		else:
			if angle > 105:
				status = True

		return [counter, status]

	def curl(self, counter, status):
		left_arm_angle = self.angle_of_the_left_arm()
		right_arm_angle = self.angle_of_the_right_arm()
		avg_arm_angle = (left_arm_angle + right_arm_angle) // 2

		if status:
			if right_arm_angle > 160 or left_arm_angle > 160:
				stage = "down"
			if right_arm_angle < 90 and left_arm_angle < 90 and stage == "down":
				counter += 1
				status = False
				stage = "up"

		else:
			if avg_arm_angle > 30:
				counter += 1
				status = True

		return [counter, status]

	def calculate_exercise(self, exercise_type, counter, status):
		if exercise_type == "push-up":
			counter, status = TypeOfExercise(self.landmarks).push_up(
				counter, status)
		elif exercise_type == "pull-up":
			counter, status = TypeOfExercise(self.landmarks).pull_up(
				counter, status)
		elif exercise_type == "squat":
			counter, status = TypeOfExercise(self.landmarks).squat(
				counter, status)
		elif exercise_type == "walk":
			counter, status = TypeOfExercise(self.landmarks).walk(
				counter, status)
		elif exercise_type == "sit-up":
			counter, status = TypeOfExercise(self.landmarks).sit_up(
				counter, status)
		elif exercise_type == "curl":
			counter, status = TypeOfExercise(self.landmarks).curl(
				counter, status)

		return [counter, status]

def walkAi(self):
	# return walkpage(request)
	# try:
	# 	walk()
	# 	return HttpResponseRedirect('/AIGymTrainer/')
	# except:
	# 	return HttpResponseRedirect('/')
	while True:
		with mp.solutions.pose.Pose(min_detection_confidence=0.5,min_tracking_confidence=0.5) as pose:
			counter = 0  # movement of exercise
			status = True  # state of move
				
			
						# print(".......................I am getting cam")
			ret, frame = self.cap.read()
					# result_screen = np.zeros((250, 400, 3), np.uint8)
						# print(".......................I am getting read")
			frame = cv2.resize(frame, (800, 480), interpolation=cv2.INTER_AREA)
					## recolor frame to RGB
			frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
			frame.flags.writeable = False
						# print(".......................I am getting colorfram")
					## make detection
			results = pose.process(frame)
					## recolor back to BGR
			frame.flags.writeable = True
			frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
						# print(".......................I am getting col")
			try:
							# print("........./////")
				landmarks = results.pose_landmarks.landmark
				counter, status = TypeOfExercise(landmarks).calculate_exercise("walk", counter, status)
			except:
				pass
			# score_table("walk", counter, status)
			print(counter, status)

					## render detections (for landmarks)
			mp.solutions.drawing_utils.draw_landmarks(
							frame,
							results.pose_landmarks,
							mp.solutions.pose.POSE_CONNECTIONS,
							mp.solutions.drawing_utils.DrawingSpec(color=(255, 255, 255),
											thickness=2,
											circle_radius=2),
							mp.solutions.drawing_utils.DrawingSpec(color=(174, 139, 45),
											thickness=2,
											circle_radius=2),
						)
			# print("////////////")
			return frame

def walkcount(request):
	return StreamingHttpResponse(gen(VideoCamera1()), content_type='multipart/x-mixed-replace; boundary=frame')

def curlCount(request):
	pass
	# try:
	# 	curl()
	# 	return HttpResponseRedirect('/AIGymTrainer')
	# except:
	# 	return HttpResponseRedirect('/')

def squatCount(request):
	try:
		squat_count()
		return HttpResponseRedirect('/AIGymTrainer/')
	except:
		return HttpResponseRedirect('/')
	
def pushCount(request):
	try:
		push()
		return HttpResponseRedirect('/AIGymTrainer/')
	except:
		return HttpResponseRedirect('/')

def pullCount(request):
	try:
		pull()
		return HttpResponseRedirect('/AIGymTrainer/')
	except:
		return HttpResponseRedirect('/')

def jumpCount(request):
	try:
		jump()
		return HttpResponseRedirect('/AIGymTrainer/')
	except:
		return HttpResponseRedirect('/')

def crunchCount(request):
	try:
		crunch()
		return HttpResponseRedirect('/AIGymTrainer/')
	except:
		return HttpResponseRedirect('/')
# def chestCount(request):
#     chest()
#     try:
#         return StreamingHttpResponse(gen(VideoCamera()), content_type='multipart/x-mixed-replace; boundary=frame')
#     except:
#     	return render(request, 'video.html')
	
	




