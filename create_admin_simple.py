"""Simple script to create admin user."""
import os
from app import create_app
from app.models.user import User
from app.models.faculty import Faculty
from app.models.department import Department
from app.extensions import db
from config import DevelopmentConfig

def create_admin():
    """Create admin user."""
    try:
        # Set environment variables
        os.environ['FLASK_DEBUG'] = '1'
        os.environ['DATABASE_URL'] = 'sqlite:///app.db'
        os.environ['SECRET_KEY'] = 'dev-key-123'
        
        # Create app with development config
        app = create_app(DevelopmentConfig)
        
        with app.app_context():
            # Drop all tables and create them again
            db.drop_all()
            db.create_all()
            
            # Create faculty
            faculty = Faculty(name='Science and Technology', code='SICT')
            db.session.add(faculty)
            db.session.flush()  # Get the ID without committing
            
            # Create department
            department = Department(name='Information Technology', code='IT', faculty_id=faculty.id)
            db.session.add(department)
            db.session.flush()  # Get the ID without committing
            
            # Create admin user
            admin = User(
                login_id='ADMIN001',
                email='admin@unilorin.edu.ng',
                first_name='Administrator',
                last_name='User',
                role='admin',
                department_id=department.id
            )
            admin.password = 'Admin@2024'
            
            db.session.add(admin)
            db.session.commit()
            
            print("Database initialized successfully")
            print("Admin user created successfully")
            print("Login ID: ADMIN001")
            print("Password: Admin@2024")
            
    except Exception as e:
        print(f"Error: {str(e)}")
        if 'db' in locals() and hasattr(db, 'session'):
            db.session.rollback()

if __name__ == '__main__':
    create_admin()
