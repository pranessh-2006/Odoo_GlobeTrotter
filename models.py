from datetime import datetime

from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash

# 1. Initialize DB here to prevent circular imports
db = SQLAlchemy()

# --- USER TABLE ---
class User(UserMixin, db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    
    # Optional Profile Fields
    full_name = db.Column(db.String(100), nullable=True)
    avatar_url = db.Column(db.String(255), nullable=True)
    bio = db.Column(db.Text, nullable=True)
    
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationships
    trips = db.relationship('Trip', backref='owner', lazy=True, cascade="all, delete-orphan")
    saved_destinations = db.relationship('SavedDestination', backref='user', lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

# --- TRIP TABLE ---
class Trip(db.Model):
    __tablename__ = 'trips'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
    name = db.Column(db.String(100), nullable=False)
    start_date = db.Column(db.Date, nullable=False) # Keep as Date object
    end_date = db.Column(db.Date, nullable=False)
    description = db.Column(db.Text)
    cover_photo = db.Column(db.String(255))
    
    budget_limit = db.Column(db.Float, default=0.0)
    is_public = db.Column(db.Boolean, default=False)
    
    # Relationships
    itineraries = db.relationship('Itinerary', backref='trip', lazy=True, cascade="all, delete-orphan")

# --- ITINERARY TABLE ---
class Itinerary(db.Model):
    __tablename__ = 'itineraries'
    
    id = db.Column(db.Integer, primary_key=True)
    trip_id = db.Column(db.Integer, db.ForeignKey('trips.id'), nullable=False)
    
    city_name = db.Column(db.String(100), nullable=False)
    country_name = db.Column(db.String(100))
    iata_code = db.Column(db.String(3)) 
    geo_lat = db.Column(db.Float)
    geo_long = db.Column(db.Float)
    
    arrival_date = db.Column(db.Date, nullable=False)
    departure_date = db.Column(db.Date, nullable=False)
    stop_order = db.Column(db.Integer, default=1)
    
    # Relationships
    activities = db.relationship('Activity', backref='itinerary', lazy=True, cascade="all, delete-orphan")

# --- ACTIVITY TABLE ---
class Activity(db.Model):
    __tablename__ = 'activities'
    
    id = db.Column(db.Integer, primary_key=True)
    itinerary_id = db.Column(db.Integer, db.ForeignKey('itineraries.id'), nullable=False)
    
    title = db.Column(db.String(200), nullable=False)
    category = db.Column(db.String(50), nullable=False) # transport, stay, activity, food
    
    cost = db.Column(db.Float, default=0.0)
    currency = db.Column(db.String(10), default='USD')
    
    start_time = db.Column(db.Time, nullable=True)
    duration_minutes = db.Column(db.Integer, nullable=True)
    is_booked = db.Column(db.Boolean, default=False)

# --- SAVED DESTINATIONS TABLE ---
class SavedDestination(db.Model):
    __tablename__ = 'saved_destinations'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
    city_name = db.Column(db.String(100), nullable=False)
    country_name = db.Column(db.String(100))
    image_url = db.Column(db.String(255))
    saved_at = db.Column(db.DateTime, default=datetime.utcnow)
