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

    #relationship: one exercise has many  workouts
    workout_exercises = db.relationship('WorkoutExercise', backref='exercise', cascade='all, delete-orphan')

    #validation
    @validates('name')
    def validate_name(self, key, value):
        if not value or value.strip():
            raise ValueError("Exercise name cannot be empty.")
        return value

    @validates('category')
    def validate_category(self, key, value):
        if not value or value.strip():
            raise ValueError("Exercise category cannot be empty.")
        return value