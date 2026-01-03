
# 🌍 GlobeTrotter

**Travel Beyond Boundaries**

GlobeTrotter is a full-featured travel planning application built with **Flask**. It allows users to create detailed itineraries, manage travel budgets in real-time, and organize trips with a modern, glassmorphism-inspired user interface.

## ✨ Key Features

* **🔐 Secure Authentication**: User signup and login system using `Flask-Login` with hashed passwords for security.
* **✈️ Smart Trip Planning**: Create trips with specific travel styles (Luxury, Backpacking, etc.), budget limits, and tags.
* **📍 Interactive Itinerary Builder**:
* Add multiple stops (cities) to your trip.
* Automatically calculates stop orders.
* Integrated city search powered by the **Amadeus API**.


* **📝 Activity Management**:
* Add detailed activities for each stop (Sightseeing, Food, Transport, etc.).
* Track costs, specific dates, times, and booking status.


* **💰 Budget Tracker**: Real-time comparison of your estimated budget vs. actual expenses, complete with a category-wise breakdown.
* **📊 Dashboard**: A comprehensive "My Trips" view to manage Upcoming, Completed, and Draft trips.
* **🎨 Modern UI**: Fully responsive design featuring glassmorphism effects, animated backgrounds, and smooth transitions.

## 🛠️ Tech Stack

* **Backend**: Python, Flask
* **Database**: SQLite (via SQLAlchemy ORM)
* **Frontend**: HTML5, CSS3 (Custom + Tailwind CSS), JavaScript
* **APIs**:
* **Amadeus API**: For city search, suggestions, and location analytics.
* **Unsplash**: Dynamic image sourcing for destinations.



## 📂 Project Structure

```text
Odoo_GlobeTrotter/
├── app.py                 # Main application entry point and route logic
├── models.py              # Database models (User, Trip, Itinerary, Activity)
├── instance/
│   └── globetrotter.db    # SQLite database file
├── static/
│   └── uploads/           # Directory for user-uploaded trip cover photos
└── templates/
    ├── index.html         # Landing page
    ├── login.html         # User login page
    ├── signup.html        # User registration page
    ├── mytrip.html        # User dashboard (My Trips)
    ├── create-trip.html   # Trip creation wizard
    ├── itinerary-builder.html # Main tool for adding stops/activities
    └── itinerary-view.html    # Final read-only view of the trip

```

## 🚀 Installation & Setup

### 1. Clone the Repository

```bash
git clone <repository-url>
cd Odoo_GlobeTrotter

```

### 2. Set Up a Virtual Environment (Recommended)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate

```

### 3. Install Dependencies

You will need the following Python packages:

```bash
pip install flask flask-login flask-sqlalchemy amadeus

```

### 4. Configure API Keys

Open `app.py` and locate the Amadeus configuration section. You will need to replace the client credentials with your own from [Amadeus for Developers](https://developers.amadeus.com/).

```python
# app.py

# Replace these with your actual keys
AMADEUS_CLIENT_ID = "YOUR_CLIENT_ID"
AMADEUS_CLIENT_SECRET = "YOUR_CLIENT_SECRET"

```

But for testing purposes the client ID and secrect of the developer is provided.


### 5. Initialize the Database

The application is configured to automatically create the database tables if they don't exist when you run the app.

### 6. Run the Application

```bash
python app.py

```

Visit `http://127.0.0.1:5000` in your browser.

## 📖 Usage Guide

1. **Sign Up**: Create a new account to start planning.
2. **Create a Trip**: Click "Plan New Trip" or "New Trip" on the dashboard. Enter your destination, dates, and budget.
3. **Build Itinerary**:
* Use the **Sidebar** to add "Stops" (Cities).
* Use the **Activity Modal** to add specific events to each stop (e.g., "Eiffel Tower Visit", Cost: $50).


4. **Manage Budget**: As you add activities, the app automatically updates your "Actual Cost" vs "Target Budget" on the Itinerary View page.
5. **Review**: Go to "Complete Trip" to see a timeline view of your entire journey.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

## 📄 License

This project is open-source and available for educational and personal use.
