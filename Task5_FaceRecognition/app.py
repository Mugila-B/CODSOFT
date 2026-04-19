import cv2
import os

recognizer = cv2.face.LBPHFaceRecognizer_create()

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

dataset_path = "dataset"
faces = []
labels = []

label_map = {}
current_label = 0

for person_name in os.listdir(dataset_path):
    person_path = os.path.join(dataset_path, person_name)

    if not os.path.isdir(person_path):
        continue

    label_map[current_label] = person_name

    for img_name in os.listdir(person_path):
        img_path = os.path.join(person_path, img_name)

        img = cv2.imread(img_path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        detected_faces = face_cascade.detectMultiScale(gray, 1.1, 5)

        for (x, y, w, h) in detected_faces:
            face = gray[y:y+h, x:x+w]
            faces.append(face)
            labels.append(current_label)

    current_label += 1

import numpy as np

recognizer.train(faces, np.array(labels))

test_img = cv2.imread("test.jpg")
gray_test = cv2.cvtColor(test_img, cv2.COLOR_BGR2GRAY)

faces_detected = face_cascade.detectMultiScale(gray_test, 1.1, 5)

for (x, y, w, h) in faces_detected:
    face = gray_test[y:y+h, x:x+w]

    label, confidence = recognizer.predict(face)

    name = label_map[label]

    cv2.rectangle(test_img, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cv2.putText(test_img, name, (x, y-10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

cv2.imshow("Face Recognition", test_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
