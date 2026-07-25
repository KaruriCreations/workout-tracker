# Marshmallow Schemas for JSON serialization/deserialization & validation
from marshmallow import Schema, fields, validate
from models import Exercise, Workout, WorkoutExercise

class ExerciseSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.Str(required=True)
    category = fields.Str(required=True)
    equipment_needed = fields.Boolean()
    
    

