"""
USAGE - The code uses MediaPipe Pose to track the angles of the arms during a bicep curl 
        exercise and counts the number of repetitions performed. The left and right angles 
        between the shoulder, elbow, and wrist are calculated and displayed on the screen. 
        If the arm is raised high enough, it is counted as one repetition, and the counter is 
        incremented. The current stage (up or down) and the number of repetitions are displayed 
        on the screen. Finally, the program captures the camera's input and processes the frames 
        until the user quits the program.

AUTHOR - https://github.com/Ahendrix9624/
"""

import cv2
import numpy as np
# from mediapipe import tasks
from .mediapipe import solutions
import mediapipe as mp
mp_drawing = mp.solutions.mediapipe.python.solutions.drawing_utils
mp_pose = mp.solutions.mediapipe.python.solutions.pose

def curl():
    def calculate_angle(a,b,c):
        a = np.array(a) # First aka left shoulder | 11
        b = np.array(b) # Mid aka left elbow | 13 
        c = np.array(c) # End left wrist | 15

        radians = np.arctan2(c[1]-b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])
        angle = np.abs(radians*180.0/np.pi)
    
        if angle > 180.0:
            angle = 360-angle
    
        return angle


    cap = cv2.VideoCapture(0) # 0 is iphone feed

# Variables 
    counter = 0
    stage = None

# Setup mediapipe instance
    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        while cap.isOpened():
            ret, frame = cap.read()
        
        # Recolor image to RGB
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False
        
        # Makes detection
            results = pose.process(image)
        
        # Recolors back to BGR
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        
        # Extract Landmarks
            try:
                landmarks = results.pose_landmarks.landmark
#!################# Left Arm #######################
            # Get Coordinates for left arm
                left_shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
                left_elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
                left_wrist = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]
            
            #Calculate angle left arm
                left_angle = calculate_angle(left_shoulder, left_elbow, left_wrist)
            
            #Visualize angle for left arm
                cv2.putText(image, str(left_angle),
                        tuple(np.multiply(left_elbow, [1800, 720]).astype(int)),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
                        )
#!################# Right Arm #######################
            # Get Coordinates for right arm
                right_shoulder = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
                right_elbow = [landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y]
                right_wrist = [landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y]
            
            #Calculate angle right arm
                right_angle = calculate_angle(right_shoulder, right_elbow, right_wrist)
            
            #Visualize angle for right arm
                cv2.putText(image, str(right_angle),
                        tuple(np.multiply(right_elbow, [1280, 720]).astype(int)),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
                        )
            
            # Curl Counter Logic
                if right_angle > 160 or left_angle > 160:
                    stage = "down"
                if right_angle < 30 and left_angle < 30 and stage == "down":
                    stage = "up"
                    counter += 1
                
            
            except: 
                pass
        
        # Render curl counter
        # Setup Status box
            cv2.rectangle(image, (0,0), (225,73), (245,117,16), -1)
        
        # Put Reps data in box
            cv2.putText(image, "Reps", (15,12), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 1, cv2.LINE_AA)
            cv2.putText(image, str(counter),
                    (10,60),
                    cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 2, cv2.LINE_AA)
        
        # Stage data on screen
            cv2.putText(image, "STAGE", (65,12), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 1, cv2.LINE_AA)
            cv2.putText(image, stage,
                    (60,60),
                    cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 2, cv2.LINE_AA)
        
        # Render detections and change line colors
            mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=2),
                                mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2)
                                )
        
            cv2.imshow("Mediapipe Feed", image)
        
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()
