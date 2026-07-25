# Defines DB tables (Exercise, Workout, WorkoutExercise) + @validates
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates

# Initialize SQLAlchemy instance
db = SQLAlchemy()

#exercise model
class Exercise(db.model):
    __tablename__ = "exercises"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    category = db.Column(db.String, nullable=False)
    equipment_needed = db.Column(db.String, nullable=False)

    
    