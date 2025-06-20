import streamlit as st
import face_recognition
import numpy as np
import pickle
import cv2
from datetime import datetime
from PIL import Image
from attendance_logger import mark_attendance
from web3 import Web3
import json

st.set_page_config(page_title="🛡️ FaceGuard – Blockchain Attendance", layout="centered")
st.title("🛡️ FaceGuard")
st.subheader("Secure, tamper-proof facial attendance system using blockchain.")

# load known face encodings
with open("encodings.pickle", "rb") as f:
    known_faces = pickle.load(f)

known_names = list(known_faces.keys())
known_encodings = list(known_faces.values())

# upload Image
uploaded_file = st.file_uploader("📸 Upload a face image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)

    # preprocess uploaded image
    image = Image.open(uploaded_file).convert("RGB")
    image_np = np.array(image)
    rgb_image = image_np[:, :, ::-1]

    # detect and encode faces
    face_locations = face_recognition.face_locations(rgb_image)
    face_encodings = face_recognition.face_encodings(rgb_image, face_locations)

    if not face_encodings:
        st.error("No recognizable face found.")
    else:
        for face_encoding, face_location in zip(face_encodings, face_locations):
            matches = face_recognition.compare_faces(known_encodings, face_encoding, tolerance=0.45)
            face_distances = face_recognition.face_distance(known_encodings, face_encoding)
            name = "Unknown Aadmi/Aadma"

            if True in matches:
                best_match_index = np.argmin(face_distances)
                name = known_names[best_match_index]

                # mark attendance on blockchain
                now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                try:
                    mark_attendance(name, now)
                    st.success(f"Attendance recorded for **{name}** at `{now}`")
                except Exception as e:
                    st.error(f"Error logging to blockchain: {str(e)}")
            else:
                st.warning("Face not recognized.")

# load contract to show logs
st.header("📜 Attendance Logs")

try:
    # connect to Ganache
    ganache_url = "http://127.0.0.1:7545"
    web3 = Web3(Web3.HTTPProvider(ganache_url))

    # load abi and contract
    with open("AttendanceABI.json", "r") as f:
        abi = json.load(f)

    contract_address = "0xEF8ED6f4c1A7E684a9f49c9A472D5541bC64Ec27"  # replace with your deployed address
    contract = web3.eth.contract(address=contract_address, abi=abi)

    count = contract.functions.getAttendanceCount().call()

    if count == 0:
        st.info("No attendance records yet.")
    else:
        for i in range(count):
            name, timestamp = contract.functions.getRecord(i).call()
            st.write(f"✅ **{i+1}. {name}** at `{timestamp}`")

except Exception as e:
    st.error(f"Error retrieving logs: {str(e)}")
