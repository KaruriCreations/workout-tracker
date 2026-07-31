from datetime import date
from app import app
from models import db, Exercise, Workout, WorkoutExercise

with app.app_context():
    print("Deleting existing data...")
    WorkoutExercise.query.delete()
    Workout.query.delete()
    Exercise.query.delete()
    db.session.commit()

    print("Seeding exercises...")
    e1 = Exercise(id=1, name="Push-ups", category="Chest", equipment_needed=False)
    e2 = Exercise(id=2, name="Squats", category="Legs", equipment_needed=False)
    e3 = Exercise(id=3, name="Pull-ups", category="Back", equipment_needed=True)

    db.session.add_all([e1, e2, e3])
    db.session.commit()

    print("Seeding workouts...")
    w1 = Workout(id=1, date=date(2026, 7, 26), duration_minutes=45, notes="Morning full body routine")
    w2 = Workout(id=2, date=date(2026, 7, 26), duration_minutes=30, notes="Quick leg workout")

    db.session.add_all([w1, w2])
    db.session.commit()

    print("Seeding workout exercises...")
    we1 = WorkoutExercise(id=1, workout_id=1, exercise_id=1, sets=3, reps=15, duration_seconds=60)
    we2 = WorkoutExercise(id=2, workout_id=1, exercise_id=3, sets=3, reps=10, duration_seconds=90)
    we3 = WorkoutExercise(id=3, workout_id=2, exercise_id=2, sets=4, reps=20, duration_seconds=120)

    db.session.add_all([we1, we2, we3])
    db.session.commit()

    print("Database seeding completed successfully.")
