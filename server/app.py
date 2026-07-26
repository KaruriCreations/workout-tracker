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

import os

#Initialize flask app
app = Flask(__name__)

#config my databas
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(BASE_DIR, 'instance', 'app.db').replace('\\', '/')
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{db_path}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

#initalize db and migration
db.init_app(app)
migrate = Migrate(app, db)

#MY routes

@app.route('/')
def index():
    return jsonify({"message": "Welcome to Vincent Maina Workout Tracker API"}),200
#workout endpoints
#for listing all workouts
@app.route('/workouts',methods=['GET'])   
def get_workouts():
    workouts = Workout.query.all()
    result = workouts_schema.dump(workouts)
    return jsonify(result), 200
#getting one workout
@app.route('/workouts/<id>',methods=['GET'])
def get_workout(id):
    workout = Workout.query.get(id)
    if workout is None:
        return jsonify({"message": "Workout not found"}),404
    result = workout_schema.dump(workout)
    return jsonify(result), 200

#for creating workouts
@app.route('/workouts',methods=['POST'])
def create_workout():
    data = request.get_json()
    try:
        workout_date = datetime.strptime(data['date'], '%Y-%m-%d').date()
        new_workout = Workout(date=workout_date,duration_minutes=data['duration_minutes'],notes=data.get('notes'))
        db.session.add(new_workout)
        db.session.commit()
        return jsonify({'message':'Workout created successfully'}),201
    except ValueError as err:
        return jsonify({'error':str(err)}),400

#for updating workouts
@app.route('/workouts/<id>',methods=['PUT'])
def update_workout(id):
    workout = Workout.query.get(id)
    if workout is None:
        return jsonify({'message':'Workout not found'}),404
    data = request.get_json()
    try:
        workout.date = datetime.strptime(data['date'], '%Y-%m-%d').date()
        workout.duration_minutes = data['duration_minutes']
        workout.notes = data.get('notes')
        db.session.commit()
        return jsonify({'message':'Workout updated successfully'}),200
    except ValueError as err:
        return jsonify({'error':str(err)}),400

#for deleting workouts
@app.route('/workouts/<id>',methods=['DELETE'])
def delete_workout(id):
    workout = Workout.query.get(id)
    if workout is None:
        return jsonify({'message':'Workout not found'}),404
    try:
        db.session.delete(workout)
        db.session.commit()
        return jsonify({'message':'Workout deleted successfully'}),200
    except Exception as err:
        db.session.rollback()
        return jsonify({'error':str(err)}),400

#exercise ednpoints

#for listing all exercises
@app.route('/exercises',methods=['GET']) 
def get_exercises():
    exercises = Exercise.query.all()
    result = exercises_schema.dump(exercises)
    return jsonify(result), 200

#getting one exercise
@app.route('/exercises/<id>',methods=['GET'])
def get_exercise(id):
    exercise = Exercise.query.get(id)
    if exercise is None:
        return jsonify({'message':'Exercise not found'}),404
    result = exercise_schema.dump(exercise)
    return jsonify(result), 200

#creating an exercise
@app.route('/exercises',methods=['POST'])
def create_exercise():
    data = request.get_json()
    try:
        new_exercise = Exercise(name=data['name'],category=data['category'],equipment_needed=data.get('equipment_needed',False))
        db.session.add(new_exercise)
        db.session.commit()
        return jsonify({'message':'Exercise created successfully'}),201
    except ValueError as err:
        return jsonify({'error':str(err)}),400

#deleting an exercise
@app.route('/exercises/<id>',methods=['DELETE'])
def delete_exercise(id):
    exercise = Exercise.query.get(id)
    if exercise is None:
        return jsonify({'message':'Exercise not found'}),404
    try:
        db.session.delete(exercise)
        db.session.commit()
        return jsonify({'message':'Exercise deleted successfully'}),200
    except Exception as err:
        db.session.rollback()
        return jsonify({'error':str(err)}),400

#workout_exerxise endpoints
@app.route('/workouts/<int:workout_id>/exercises/<int:exercise_id>/workout_exercises',methods=['POST'])
def add_exercise_to_workout(workout_id, exercise_id):
    workout = Workout.query.get(workout_id)
    exercise = Exercise.query.get(exercise_id)
    if workout is None or exercise is None:
        return jsonify({'message':'Workout or Exercise not found'}),404
    data = request.get_json()
    try:
        new_workout_exercise = WorkoutExercise(
            workout_id=workout.id,
            exercise_id=exercise.id,
            sets=data.get('sets'),
            reps=data.get('reps'),
            duration_seconds=data.get('duration_seconds')
        )
        db.session.add(new_workout_exercise)
        db.session.commit()
        return jsonify({'message':'Exercise added to workout successfully'}),201
    except ValueError as err:
        db.session.rollback()
        return jsonify({'error':str(err)}),400

if __name__ == '__main__':
    app.run(port=5555, debug=True)     