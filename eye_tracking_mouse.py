import cv2
import mediapipe as mp
import pyautogui


def eyeTracking():
    cam = cv2.VideoCapture(0)
    face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
    screen_w, screen_h = pyautogui.size()
    print(screen_w, screen_h)
    while True:
        _, frame = cam.read()
        frame = cv2.flip(frame,1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        output = face_mesh.process(rgb_frame)
        landmark_points = output.multi_face_landmarks
        frame_h, frame_w, _ = frame.shape
        if landmark_points:
            landmarks = landmark_points[0].landmark
            for id, landmark in enumerate(landmarks[474:478]):
                print(id)
                x = int(landmark.x * frame_w)
                y = int(landmark.y * frame_h)
                cv2.circle(frame, (x,y),3,(0,255,0))
                if id == 1:
                    print(landmark.x, landmark.y)
                    screen_x = int(landmark.x * screen_w)
                    screen_y = int(landmark.y * screen_h)
                    pyautogui.moveTo(screen_x, screen_y)
            RIGHT_EYE = [362, 374, 263, 385]
            # 362 - wewnetrzny rog
            # 374 - dol
            # 263 - zewnetrzny rog
            # 385 - gora
            for element in RIGHT_EYE:
                x = int(landmarks[element].x * frame_w)
                y = int(landmarks[element].y * frame_h)
                cv2.circle(frame, (x, y), 3, (50, 200, 255))
            left = [landmarks[145], landmarks[159]]
            for landmark in left:
                x = int(landmark.x * frame_w)
                y = int(landmark.y * frame_h)
                cv2.circle(frame, (x, y), 3, (0, 255, 255))
            if(left[0].y - left[1].y) < 0.004:
                pyautogui.click()
                pyautogui.sleep(1)
        cv2.imshow('Eye Controlled Mouse', frame)
        cv2.waitKey(1)
