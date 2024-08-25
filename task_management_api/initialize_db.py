from app import db
from run import app
from app.models import User, Task

with app.app_context():
    db.create_all()

print("Database tables created successfully.")
