import face_recognition
import os
import pickle
import cv2
import numpy as np 

KNOWN_FACES_DIR = "known_faces"
encodings_dict = {}

for person_name in os.listdir(KNOWN_FACES_DIR):
    person_dir = os.path.join(KNOWN_FACES_DIR, person_name)
    if not os.path.isdir(person_dir):
        continue

    for image_name in os.listdir(person_dir):
        image_path = os.path.join(person_dir, image_name)
        image = cv2.imread(image_path)

        if image is None:
            print(f"Failed to read image: {image_path}")
            continue
        
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = np.ascontiguousarray(image)

        image = cv2.resize(image, (400, 400))

        print(f"Loaded {image_path} — dtype: {image.dtype}, shape: {image.shape}")

        if image.dtype != 'uint8' or image.shape[2] != 3:
            print(f"Invalid format: {image_path}")
            continue

        encodings = face_recognition.face_encodings(image)

        if encodings:
            encodings_dict[person_name] = encodings[0]
            print(f"Encoded: {person_name}")
            break
        else:
            print(f"No face found in: {image_path}")

        with open("encodings.pickle", "wb") as f:
            pickle.dump(encodings_dict, f)

        print("All encodings saved.")

        if encodings:
            encodings_dict[person_name] = encodings[0]
            print(f"Encoded: {person_name}")
            break
        else:
            print(f"No face found in: {image_path}")

with open("encodings.pickle", "wb") as f: # save the encodings
    pickle.dump(encodings_dict, f)
print("All encodings saved.")