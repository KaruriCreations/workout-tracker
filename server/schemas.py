# Marshmallow Schemas for JSON serialization/deserialization & validation
from marshmallow import Schema, fields, validate
from models import Exercise, Workout, WorkoutExercise

class ExerciseSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.Str(required=True)
    category = fields.Str(required=True)
    equipment_needed = fields.Boolean()

class WorkoutExerciseSchema(Schema):
    id = fields.Integer(dump_only=True)
    workout_id = fields.Integer(required=True)
    exercise_id = fields.Integer(required=True)
    sets = fields.Integer(required=True)
    reps = fields.Integer(required=True)
    duration_seconds = fields.Integer(required=True)

    #relationship:single nested schema
    exercise = fields.Nested(ExerciseSchema, only=('id', 'name', 'category'))



class WorkoutSchema(Schema):
    id = fields.Integer(dump_only=True)
    date = fields.Date(required=True)
    duration_minutes = fields.Integer(required=True)
    notes = fields.Str()
    
    #relationship:many nested schema
    workout = fields.Nested(WorkoutExerciseSchema, only=('id', 'exercise_id', 'sets', 'reps', 'duration_seconds'))

