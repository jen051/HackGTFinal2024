import cv2
import mediapipe as mp
import numpy as np
import time
import threading
import streamlit as st

buffer_elapsed = False
punch_stance_sequence = []
punch_stance_angle_sequence = []
punch_sequence = []
punch_angle_sequence = []
step_one_passed = False

def timer_buffer(seconds):
   def timer():
       global buffer_elapsed
       buffer_elapsed = False
       time.sleep(seconds)
       buffer_elapsed = True
 
   timer_thread = threading.Thread(target=timer)
   timer_thread.start()

def detect_pose_live():
   mp_drawing = mp.solutions.drawing_utils
   mp_pose = mp.solutions.pose
   pose = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)
   pass_count = 1
   cap = cv2.VideoCapture(0)
   stframe = st.empty()
   while cap.isOpened():
       ret, frame = cap.read()
       try:
           if not ret:
               break
           if pass_count < 2:
               if practice_loop(frame, pose, pass_count) and buffer_elapsed:
                   pass_count += 1
                   timer_buffer(3)
               cv2.putText(frame, str(pass_count-1), (30, 450), cv2.FONT_HERSHEY_SIMPLEX,3, (0,128,0),8, cv2.LINE_AA)
             
               mp_drawing.draw_landmarks(frame, pose.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)).pose_landmarks, mp_pose.POSE_CONNECTIONS)
               stframe.image(frame, channels="BGR")
           else:
               cv2.putText(frame, "Congrats!", (500, 200), cv2.FONT_HERSHEY_SIMPLEX,1.5, (0,128,0),8, cv2.LINE_AA)
               cv2.putText(frame, "You've completed", (500, 250), cv2.FONT_HERSHEY_SIMPLEX,1.5, (0,128,0),8, cv2.LINE_AA)
               cv2.putText(frame, "this module :)", (500, 300), cv2.FONT_HERSHEY_SIMPLEX,1.5, (0,128,0),8, cv2.LINE_AA)
               stframe.image(frame, channels="BGR")
               break 
       except Exception as e:
           print(f"Error: {e}")
           break
   cap.release()
   cv2.destroyAllWindows()

def compare_angle_sequences(live, standing):
   if not live or not standing:
       return 0.0
   accuracy = 0
   if(len(live)>0):
       if(len(live)%8 == 0):
           accuracy = (1 - (compute_mse(standing,live[len(live)-8:len(live)]))/(90**2))*100
   return accuracy

def detect_punch_stance(image_path):
   mp_drawing = mp.solutions.drawing_utils
   mp_pose = mp.solutions.pose
   pose = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)
   image = cv2.imread(image_path)
   image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
   pose_results = pose.process(image_rgb)
   relevant_results = pose_results.pose_landmarks.landmark
   for lndmrk in relevant_results:
       x = lndmrk.x
       y = lndmrk.y
       z = lndmrk.z
       punch_stance_sequence.append([x, y, z])
   find_angle_sequence(punch_stance_sequence, punch_stance_angle_sequence)
   mp_drawing.draw_landmarks(image, pose_results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
 
def detect_punch(image_path):
   mp_drawing = mp.solutions.drawing_utils
   mp_pose = mp.solutions.pose
   pose = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)
   image = cv2.imread(image_path)
   image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
   pose_results = pose.process(image_rgb)
   relevant_results = pose_results.pose_landmarks.landmark
   for lndmrk in relevant_results:
       x = lndmrk.x
       y = lndmrk.y
       z = lndmrk.z
       punch_sequence.append([x, y, z])
   find_angle_sequence(punch_sequence, punch_angle_sequence)
   mp_drawing.draw_landmarks(image, pose_results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

def find_angle_sequence(sequence, angle_sequence):
   mp_pose = mp.solutions.pose
   right_forearm_1416 = compute_vector_difference(sequence[mp_pose.PoseLandmark.RIGHT_WRIST.value], sequence[mp_pose.PoseLandmark.RIGHT_ELBOW.value])
   right_upper_arm_1214 = compute_vector_difference(sequence[mp_pose.PoseLandmark.RIGHT_ELBOW.value], sequence[mp_pose.PoseLandmark.RIGHT_SHOULDER.value])
   right_body_1224 = compute_vector_difference(sequence[mp_pose.PoseLandmark.RIGHT_ELBOW.value], sequence[mp_pose.PoseLandmark.RIGHT_SHOULDER.value])
   right_thigh_2426 = compute_vector_difference(sequence[mp_pose.PoseLandmark.RIGHT_HIP.value], sequence[mp_pose.PoseLandmark.RIGHT_KNEE.value])
   right_calf_2628 = compute_vector_difference(sequence[mp_pose.PoseLandmark.RIGHT_KNEE.value], sequence[mp_pose.PoseLandmark.RIGHT_ANKLE.value])
 
   left_upper_arm_1113 = compute_vector_difference(sequence[mp_pose.PoseLandmark.LEFT_SHOULDER.value], sequence[mp_pose.PoseLandmark.LEFT_ELBOW.value])
   left_body_1123 = compute_vector_difference(sequence[mp_pose.PoseLandmark.LEFT_SHOULDER.value], sequence[mp_pose.PoseLandmark.LEFT_HIP.value])
   left_forearm_1315 = compute_vector_difference(sequence[mp_pose.PoseLandmark.LEFT_ELBOW.value], sequence[mp_pose.PoseLandmark.LEFT_WRIST.value])
   left_thigh_2325 = compute_vector_difference(sequence[mp_pose.PoseLandmark.LEFT_HIP.value], sequence[mp_pose.PoseLandmark.LEFT_KNEE.value])
   left_calf_2527 = compute_vector_difference(sequence[mp_pose.PoseLandmark.LEFT_KNEE.value], sequence[mp_pose.PoseLandmark.LEFT_ANKLE.value])
 
   right_elbow_angle = compute_angle(right_forearm_1416, right_upper_arm_1214)
   angle_sequence.append(right_elbow_angle)
   right_armpit_angle = compute_angle(right_upper_arm_1214, right_body_1224)
   angle_sequence.append(right_armpit_angle)
   right_hip_angle = compute_angle(right_body_1224, right_thigh_2426)
   angle_sequence.append(right_hip_angle)
   right_knee_angle = compute_angle(right_thigh_2426, right_calf_2628)
   angle_sequence.append(right_knee_angle)
 
   left_elbow_angle = compute_angle(left_forearm_1315, left_upper_arm_1113)
   angle_sequence.append(left_elbow_angle)
   left_armpit_angle = compute_angle(left_upper_arm_1113, left_body_1123)
   angle_sequence.append(left_armpit_angle)
   left_hip_angle = compute_angle(left_body_1123, left_thigh_2325)
   angle_sequence.append(left_hip_angle)
   left_knee_angle = compute_angle(left_thigh_2325, left_calf_2527)
   angle_sequence.append(left_knee_angle)


def compute_vector_difference(final, initial):
   return [final[0] - initial[0],final[1]-initial[1], final[2]-initial[2]]
 
def compute_angle(vector1, vector2):
   angle = np.degrees(np.arccos(np.dot(vector1,vector2)/(np.linalg.norm(vector1)*np.linalg.norm(vector2))))
   return angle


def compute_mse(ref_angles, live_angles):
   sum = 0
   for i in range(len(ref_angles)):
       dif = (ref_angles[i] - live_angles[i])**2
       # weights
       if i is (0 or 1 or 4 or 5):
           dif  = dif*4/3
       else:
           dif = dif*0.75
       sum += dif
   return sum/8


def update_step_one_status(value):
   global step_one_passed
   step_one_passed = value


def get_step_one_status():
   global step_one_passed
   return step_one_passed
 
def practice_loop(live_video, pose, pass_count):
   if pass_count < 6:
       frame_rgb = cv2.cvtColor(live_video, cv2.COLOR_BGR2RGB)           
       pose_results = pose.process(frame_rgb)
       if pose_results.pose_landmarks:
           relevant_results = pose_results.pose_landmarks.landmark
           live_pose_sequence = []
           live_angle_sequence = []
           for lndmrk in relevant_results:
               if(lndmrk.visibility>0.7):
                   x = lndmrk.x
                   y = lndmrk.y
                   z = lndmrk.z
               else:
                   x = 0
                   y = 0
                   z = 0
               live_pose_sequence.append([x, y, z])
           find_angle_sequence(live_pose_sequence, live_angle_sequence)
           if live_angle_sequence:
               # Compare live_angle_sequence with punch_stance_angle_sequence
               accuracy = compare_angle_sequences(live_angle_sequence, punch_stance_angle_sequence)
               if not np.isnan(accuracy):
                   if (accuracy > 90 and buffer_elapsed) or get_step_one_status():
                       cv2.putText(live_video, "now punch!", (30, 100), cv2.FONT_HERSHEY_SIMPLEX,1, (0,0,255),2, cv2.LINE_AA)
                       accuracy = compare_angle_sequences(live_angle_sequence, punch_angle_sequence)
                       cv2.putText(live_video, f"Accuracy: {accuracy:.2f}%", (30, 40), cv2.FONT_HERSHEY_SIMPLEX,1, (0,0,0),4, cv2.LINE_AA)
                       update_step_one_status(True)
                       if accuracy > 90:
                           cv2.putText(live_video, f"Accuracy: {accuracy:.2f}%", (30, 40), cv2.FONT_HERSHEY_SIMPLEX,1, (0,128,0),4, cv2.LINE_AA)
                           pass_count += 1
                           update_step_one_status(False)
                           return True
                       else:
                           cv2.putText(live_video, f"Accuracy: {accuracy:.2f}%", (30, 40), cv2.FONT_HERSHEY_SIMPLEX,1, (0,0,0),4, cv2.LINE_AA)
                   else:
                       cv2.putText(live_video, f"Accuracy: {accuracy:.2f}%", (30, 40), cv2.FONT_HERSHEY_SIMPLEX,1, (0,0,0),4, cv2.LINE_AA)
               else:
                   cv2.putText(live_video, f"Accuracy: {0}%", (30, 40), cv2.FONT_HERSHEY_SIMPLEX,1, (0,0,0),4, cv2.LINE_AA)
   return False




timer_buffer(1)
detect_punch('punch.jpg')
detect_punch_stance('punch_stance.jpg')
detect_pose_live()