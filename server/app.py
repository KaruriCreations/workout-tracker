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

#Initialize flask app
app = Flask(__name__)

#config my databas
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

#initalize db and migration
