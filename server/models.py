# Defines DB tables (Exercise, Workout, WorkoutExercise) + @validates
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates

# Initialize SQLAlchemy instance
db = SQLAlchemy()

# Exercise model
class Exercise(db.Model):
    __tablename__ = "exercises"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    category = db.Column(db.String, nullable=False)
    equipment_needed = db.Column(db.Boolean, nullable=False, default=False)

    # Relationship: one exercise has many workout_exercises
    workout_exercises = db.relationship('WorkoutExercise', backref='exercise', cascade='all, delete-orphan')

    # Validations
    @validates('name')
    def validate_name(self, key, value):
        if not value or not value.strip():
            raise ValueError("Exercise name cannot be empty.")
        return value

    @validates('category')
    def validate_category(self, key, value):
        if not value or not value.strip():
            raise ValueError("Exercise category cannot be empty.")
        return value


# Workout model
class Workout(db.Model):
    __tablename__ = "workouts"

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    duration_minutes = db.Column(db.Integer, nullable=False)
    notes = db.Column(db.Text)

    # Relationship: one workout has many workout_exercises
    workout_exercises = db.relationship('WorkoutExercise', backref='workout', cascade='all, delete-orphan')

    # Validations
    @validates('duration_minutes')
    def validate_duration_minutes(self, key, value):
        if value is None or value <= 0:
            raise ValueError("Workout duration must be positive.")
        return value


# WorkoutExercise model
class WorkoutExercise(db.Model):
    __tablename__ = "workout_exercises"

    id = db.Column(db.Integer, primary_key=True)
    workout_id = db.Column(db.Integer, db.ForeignKey('workouts.id'), nullable=False)
    exercise_id = db.Column(db.Integer, db.ForeignKey('exercises.id'), nullable=False)
    sets = db.Column(db.Integer)
    reps = db.Column(db.Integer)
    duration_seconds = db.Column(db.Integer)

    # Validations
    @validates('duration_seconds', 'sets', 'reps')
    def validate_value(self, key, value):
        if value is not None and value <= 0:
            raise ValueError(f"{key} must be greater than zero.")
        return value