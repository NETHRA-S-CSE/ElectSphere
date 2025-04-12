# ElectSphere 🗳️

ElectSphere is a web-based voting system built using **Django**, **MongoDB**, and **OpenCV**. It allows voters to securely upload their Voter ID and optionally verify their identity using real-time face capture before casting their vote.

## 🔧 Tech Stack
- **Frontend**: HTML, CSS
- **Backend**: Django (Python)
- **Database**: MongoDB (via Djongo)
- **Face Recognition**: OpenCV + face_recognition

## 🚀 Features
- Voter ID upload and verification
- Optional facial authentication using webcam
- One vote per user (based on voter ID)
- Admin panel to view voting results
- Data stored securely in MongoDB

## 📂 Pages
- Home (`index.html`)
- Upload Voter ID
- Live Face Capture
- Voting Page
- Vote Confirmation
- Admin Dashboard

## 🛡️ Security
- Encrypted face encoding
- One-time voting check
- Secure vote storage in MongoDB

## 📌 Usage
1. Clone the repository
2. Install dependencies
3. Run the Django server
4. Start voting on `localhost:8000`

---

> Built with ❤️ by Nethra – inspired by the vision of secure and easy digital elections.
