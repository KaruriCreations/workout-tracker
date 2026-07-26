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
db.init_app(app)
migrate = Migrate(app, db)

#MY routes

@app.route('/')
def index():
    return jsonify({"message": "Welcome to Workout Tracker API"}),200
#workout endpoints
#for listing all workouts
@app.route('/workouts',methods=['GET'])   
def get_workouts():
    workouts = Workout.query.all()
    result = workouts_schema.dump(workouts)
    return jsonify(result), 200

@app.route('/workouts/<id>',methods=['GET'])
def get_workout(id):
    workout = Workout.query.get(id)
    if workout is None:
        return jsonify({"message": "Workout not found"}),404
    result = workout_schema.dump(workout)
    return jsonify(result), 200
