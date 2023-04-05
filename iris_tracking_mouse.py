import cv2
import mediapipe as mp
import pyautogui
import numpy as np


def normalization(begin, end, iris):
    normalized = (iris - begin) / (end - begin)
    return normalized


def eyeTracking():
    cam = cv2.VideoCapture(0)
    face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
    screen_w, screen_h = pyautogui.size()
    pyautogui.FAILSAFE = False
    temp_normalized = []
    temp_y = []
    temp_x = []
    control = 0
    while True:
        _, frame = cam.read()
        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        output = face_mesh.process(rgb_frame)
        landmark_points = output.multi_face_landmarks
        frame_h, frame_w, _ = frame.shape
        if landmark_points:
            landmarks = landmark_points[0].landmark
            RIGHT_EYE = [362, 374, 263, 385]
            # 362 - wewnetrzny rog
            # 374 - dol
            # 263 - zewnetrzny rog
            # 385 - gora
            # dół - powyżej 0.5 tym większa wartość im mniejsza odległość między powiekami?
            begin_x = landmarks[RIGHT_EYE[0]].x
            end_x = landmarks[RIGHT_EYE[2]].x

            #begin_y = landmarks[RIGHT_EYE[3]].y
            end_y = landmarks[RIGHT_EYE[1]].y

            iris_x = (landmarks[476].x + landmarks[474].x) / 2
            iris_y = (landmarks[477].y + landmarks[475].y) / 2

            iris_normalizedX = normalization(begin_x, end_x, iris_x)
            iris_normalizedY = normalization((end_y - 0.04), end_y, iris_y)

            iris_normalizedX2 = normalization(0.42, 0.6, iris_normalizedX)
            #iris_normalizedY2 = normalization(0.52, 0.64, iris_normalizedY)
            iris_normalizedY2 = normalization(0.52, 0.62, iris_normalizedY)
            temp_normalized.append(iris_normalizedY)
            # temp
            if landmark_points:
                landmarks = landmark_points[0].landmark
                for id, landmark in enumerate(landmarks[474:478]):
                    x = int(landmark.x * frame_w)
                    y = int(landmark.y * frame_h)
                    cv2.circle(frame, (x, y), 3, (0, 255, 0))
            # end temp

            screen_x = round(int(iris_normalizedX2 * screen_w), 2)
            screen_y = round(int(iris_normalizedY2 * screen_h), 2)


            #smoothing
            temp_y.append(screen_y)
            temp_x.append(screen_x)

            if control == 5:
                pyautogui.moveTo(np.mean(temp_x), np.mean(temp_y))
                control += 1
                pyautogui.sleep(0.05)
            elif control == 10:
                pyautogui.moveTo(np.mean(temp_x), np.mean(temp_y))
                temp_x = []
                temp_y = []
                control = 0
                pyautogui.sleep(0.05)
            else:
                control += 1

            #smoothing end
            left = [landmarks[145], landmarks[159]]
            for landmark in left:
                x = int(landmark.x * frame_w)
                y = int(landmark.y * frame_h)
                cv2.circle(frame, (x, y), 3, (0, 255, 255))

            if(landmarks[RIGHT_EYE[1]].y - landmarks[RIGHT_EYE[3]].y) < 0.0055 and (left[0].y - left[1].y) < 0.0055:
                pyautogui.sleep(1)
                if(landmarks[RIGHT_EYE[1]].y - landmarks[RIGHT_EYE[3]].y) < 0.0055 and (left[0].y - left[1].y) < 0.0055:
                    pyautogui.doubleClick()
                    pyautogui.sleep(1)
                    break
            elif (left[0].y - left[1].y) < 0.0045:
                pyautogui.click()
                pyautogui.sleep(1)


        cv2.imshow('Eye Controlled Mouse', frame)
        cv2.waitKey(1)


