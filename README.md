# FaceGuard – Tamper-Proof Facial Attendance System with Blockchain

Focus Areas: Computer Vision, Face Recognition, Blockchain, Security

Objective: To build a secure facial recognition-based attendance system where each attendance record is immutable and tamper-proof using blockchain logging. This system aims to simulate secure attendance verification for environments like classrooms or offices.

---

## Features

- Detects and recognizes faces using `face_recognition`
- Records attendance with timestamp
- Logs attendance on a blockchain smart contract (via Web3)
- Simple frontend interface using Streamlit
- Hashes identity data for secure storage (SHA256)
- Displays stored logs from blockchain in UI

---

## Tech Stack

| Component | Tool/Library |
|----------|--------------|
| Face Recognition | [face_recognition](https://github.com/ageitgey/face_recognition), OpenCV |
| Frontend UI | Streamlit |
| Smart Contract | Solidity |
| Blockchain Environment | Ganache |
| Python–Blockchain Interface | Web3.py |
| Encoding Storage | Pickle |
| Hashing | `hashlib` (SHA256) |

---

## How to Run

### Clone the Repo

```bash
git clone https://github.com/mahaqj/FaceGuard.git
cd FaceGuard
```

### Create and Activate Virtual Environment

```bash
python -m venv fgenv
fgenv\Scripts\activate  # on Windows
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Deploy Smart Contract

1. Open `Attendance.sol` in [Remix](https://remix.ethereum.org)
2. Compile and deploy using the **Injected Web3** environment (connected to Ganache)
3. Copy the contract **address** and **ABI**
4. Paste:
   - ABI in `AttendanceABI.json`
   - Address in both `app.py` and `attendance_logger.py`

### Encode Faces

Place known face images in a folder, then run:

```bash
python encode_faces.py
```

This will create `encodings.pickle`.

---

## Run the App

```bash
streamlit run app.py
```

Then open: [http://localhost:8501](http://localhost:8501)

---

## Sample Output

![Screenshot 2025-06-20 151820](https://github.com/user-attachments/assets/4a92e6d2-8e53-4856-8a50-4ba9449c2123)
![Screenshot 2025-06-20 151853](https://github.com/user-attachments/assets/1a0287f7-271d-4bb2-b479-d55970195339)
![Screenshot 2025-06-20 151920](https://github.com/user-attachments/assets/60be3479-1f44-423f-9728-00b97050990b)

---
---
