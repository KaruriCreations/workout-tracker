# Defines DB tables (Exercise, Workout, WorkoutExercise) + @validates
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates

# Initialize SQLAlchemy instance
db = SQLAlchemy()
