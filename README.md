# 🌍 GlobeTrotter – Smart Travel Planner

GlobeTrotter is a Flask-based travel planning web application inspired by platforms like MakeMyTrip.  
It allows users to plan trips, manage itineraries, track budgets, and explore destinations using real-time travel data.

---

## 🚀 Features

- User Signup & Login (Flask-Login)
- Dashboard / Home Page (MakeMyTrip-style)
- Create & manage trips
- Multi-city itinerary builder
- Activity planner with cost tracking
- Budget summary & category breakdown
- City search & suggestions (Amadeus API)
- Image uploads for trip covers
- Secure authentication & authorization

---

## 🛠 Tech Stack

- **Backend:** Flask (Python)
- **Frontend:** HTML, CSS, JavaScript
- **Database:** SQLite + SQLAlchemy
- **Authentication:** Flask-Login
- **APIs:** Amadeus Travel API
- **Image Source:** Unsplash (dynamic)

---

## 📂 Project Structure

globetrotter/
│
├── app.py
├── models.py
├── requirements.txt
├── README.md
│
├── templates/
│ ├── index.html
│ ├── login.html
│ ├── signup.html
│ ├── create-trip.html
│ ├── itinerary-builder.html
│ └── itinerary-view.html
│
├── static/
│ ├── css/
│ ├── js/
│ └── uploads/
│
└── globetrotter.db


---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone <your-repo-url>
cd globetrotter

2️⃣ Create virtual environment (recommended)
python -m venv venv


Activate it:

Windows

venv\Scripts\activate


Mac / Linux

source venv/bin/activate

3️⃣ Install dependencies
pip install -r requirements.txt

🔑 API Configuration

Create an account at:
👉 https://developers.amadeus.com

Replace your API keys in app.py:

AMADEUS_CLIENT_ID = "YOUR_CLIENT_ID"
AMADEUS_CLIENT_SECRET = "YOUR_CLIENT_SECRET"


(Optional but recommended: use environment variables instead.)

▶️ Run the Application
python app.py


Then open:

http://127.0.0.1:5000/

🔐 Authentication Flow

New users → Signup

Existing users → Login

Unauthorized users are redirected to login

Each user sees only their own trips

💡 Future Enhancements

Flight & hotel booking integration

Map-based itinerary visualization

AI-powered trip recommendations

Export itinerary as PDF

Email notifications & reminders

Payment gateway integration

🧑‍💻 Author

GlobeTrotter Project
Built for academic & hackathon use 🚀

📜 License

This project is for educational purposes only.


