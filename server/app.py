# Configures Flask app, DB, and API routes (/workouts, /exercises)
from flask import Flask, request, jsonify
from flask_migrate import Migrate
from datetime import datetime

# Import database, models, and schemas
from models import db, Exercise, Workout, WorkoutExercise
from schemas import (
    workout_schema, workouts_schema,
    exercise_schema, exercises_schema,
    workout_exercise_schema
)