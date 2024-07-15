# install VIsual Studio Code
# pip install cmake
# pip install face_recognition
# pip install opencv-python
# pip install numpy
import face_recognition
import cv2
import numpy as np
import csv
from datetime import datetime

video_capture = cv2.VideoCapture(0)

# Load Known faces
yash_image = face_recognition.load_image_file("faces/yash.jpg")
yash_encoding = face_recognition.face_encodings(yash_image)[0]

smit_image = face_recognition.load_image_file("faces/smit.jpg")
smit_encoding = face_recognition.face_encodings(smit_image)[0]

known_face_encodings = [yash_encoding, smit_encoding]
known_face_names = ["Yash","Smit"]

# list of expected students
students = known_face_names.copy()

face_locations = []
face_encodings = []

# Get the current date & time
now = datetime.now()
current_date = now.strftime("%d-%m-%Y")

f = open(f"{current_date}.csv", "w+", newline="")
lnwriter = csv.writer(f)
lnwriter.writerow(["Name", "Present Time"])

while True:
    _, frame = video_capture.read()
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    # Recognize faces
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    if len(face_locations) == 0:
            # Handle the case where no faces are detected
            cv2.putText(frame, "No faces detected", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    else:
        for face_encoding in face_encodings:
        # for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            face_distance = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distance)


            match_found = False
            if (matches[best_match_index]):
                name = known_face_names[best_match_index]
                match_found = True

            if match_found:
            # Add the text if the person is present
                if name in known_face_names:
                    font = cv2.FONT_HERSHEY_SIMPLEX
                    bottomLeftCornerOfText = (10, 100)
                    fontScale = 1.5
                    fontColor = (226,97,115)
                    thickness = 3
                    lineType = 2
                    cv2.putText(frame, name + " Present", bottomLeftCornerOfText, font, fontScale, fontColor, thickness, lineType)

                    if name in students:
                        students.remove(name)
                        current_time = now.strftime("%H:%M:%S")
                        with open(f"{current_date}.csv", "a", newline="") as f:
                            lnwriter = csv.writer(f)
                            lnwriter.writerow([name, current_time])


            if not match_found:
                        # Handle the case where no matches are found
                        cv2.putText(frame, "No matches found", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.imshow("Attendance", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video_capture.release()
cv2.destroyAllWindows()
f.close()
