import torch
from facenet_pytorch import MTCNN, InceptionResnetV1
import cv2
import numpy as np
import csv
from datetime import datetime

# Initialize face detector and face recognizer models
device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
mtcnn = MTCNN(device=device)
resnet = InceptionResnetV1(pretrained='vggface2').eval().to(device)

# Load known face encodings
smit_image = cv2.imread("faces/smit.jpg")
smit_image = cv2.cvtColor(smit_image, cv2.COLOR_BGR2RGB)
smit_face = mtcnn(smit_image)
smit_encoding = resnet(smit_face.unsqueeze(0)).detach().cpu().numpy()

known_face_encodings = [smit_encoding]
known_face_names = ["Smit"]

# Initialize student list
students = known_face_names.copy()

# Get current date
now = datetime.now()
current_date = now.strftime("%d-%m-%Y")

# Initialize CSV writer
with open(f"{current_date}.csv", "w+", newline="") as f:
    lnwriter = csv.writer(f)
    lnwriter.writerow(["Name", "Present Time"])

# Initialize video capture
video_capture = cv2.VideoCapture(0)

while True:
    ret, frame = video_capture.read()
    if not ret:
        break

    # Convert BGR image to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Detect face in the frame
    boxes, _ = mtcnn.detect(rgb_frame)

    if boxes is not None:
        for box in boxes:
            # Convert box to integers
            box = [int(coord) for coord in box]

            # Extract face from the frame
            face = rgb_frame[box[1]:box[3], box[0]:box[2]]

            # Convert face to PIL image and resize
            face_image = Image.fromarray(face)
            face_image = face_image.resize((160, 160), Image.ANTIALIAS)

            # Compute face embedding
            face_embedding = resnet(mtcnn(face_image).unsqueeze(0)).detach().cpu().numpy()

            # Compute cosine similarity
            cosine_similarity = np.dot(known_face_encodings[0], face_embedding.T) / (
                        np.linalg.norm(known_face_encodings[0]) * np.linalg.norm(face_embedding))

            # Threshold for face matching (adjust as needed)
            threshold = 0.5

            if cosine_similarity > threshold:
                cv2.rectangle(frame, (box[0], box[1]), (box[2], box[3]), (0, 255, 0), 2)
                cv2.putText(frame, "Smit", (box[0], box[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            else:
                cv2.rectangle(frame, (box[0], box[1]), (box[2], box[3]), (0, 0, 255), 2)
                cv2.putText(frame, "Unknown", (box[0], box[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    cv2.imshow('Face Recognition', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
