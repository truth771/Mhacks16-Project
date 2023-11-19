import cv2
from deepface import DeepFace
import numpy as np
import os

def emotion_detection(filename):
    emotions = {'angry': 0,'disgust': 0, 'fear': 0, 'sad': 0,'happy': 0,'surprise': 0,'neutral': 0,'no face':0}
    # frame_count = 0
    VIDEOS_DIR = os.path.join('.', 'mhacks16-project/videos')
    VIDEO_NAME = filename
    emotion_color_mapping = {
        'angry': (0, 0, 255),
        'disgust': (0, 0, 255),
        'fear': (0, 0, 255),
        'sad': (0, 0, 255),
        'happy': (0, 255, 0),
        'surprise': (0, 255, 0),
        'neutral': (128, 128, 128),
    }

    video_path = os.path.join(VIDEOS_DIR, VIDEO_NAME)
    video_path_out = '{}_out.mp4'.format(video_path[:-4])

    cap = cv2.VideoCapture(video_path)
    ret, frame = cap.read()
    H, W, _ = frame.shape
    out = cv2.VideoWriter(video_path_out, cv2.VideoWriter_fourcc(*'mp4v'), int(cap.get(cv2.CAP_PROP_FPS)), (W, H))

    face_cascade = cv2.CascadeClassifier("mhacks16-project/haarcascade_frontalface_default.xml")


    while ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        face=face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

        for x,y,w,h in face:
            if(w > 100):
                try:
                    analyze = DeepFace.analyze(frame,actions=['emotion'],silent = True)
                    emotion = analyze[0]['dominant_emotion']
                    color = emotion_color_mapping.get(emotion)
                    img = cv2.rectangle(frame,(x,y),(x+w, y+w),color,4)
                    cv2.putText(frame, emotion.upper(), (int(x), int(y - 10)),
                            cv2.FONT_HERSHEY_SIMPLEX, 1.3, color, 3, cv2.LINE_AA)
                    if emotion in emotions:
                        emotions[emotion] += 1
                    else:
                        emotions[emotion] = 1
                except:
                    if "no face" in emotions:
                        emotions["no face"] += 1
                    else:
                        emotions["no face"] = 1
            else:
                if "no face" in emotions:
                    emotions["no face"] += 1
                else:
                    emotions["no face"] = 1
        out.write(frame)
        ret, frame = cap.read()
        # if frame_count % 100 == 0:
        #     print('Processed {} frames.'.format(frame_count))
        # frame_count += 1

    cap.release()
    out.release()
    cv2.destroyAllWindows()

    return emotions
