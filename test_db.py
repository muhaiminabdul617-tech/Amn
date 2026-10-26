"""Test database connection."""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define a simple model
class TestModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

def main():
    """Test database connection and operations."""
    with app.app_context():
        # Create tables
        db.create_all()
        print("Database tables created successfully!")

        # Try to add a test record
        test = TestModel(name="Test Record")
        db.session.add(test)
        db.session.commit()
        print("Test record added successfully!")

        # Query the record
        result = TestModel.query.first()
        print(f"Retrieved record: {result.name}")

if __name__ == '__main__':
    main()
