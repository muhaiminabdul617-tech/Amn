"""Direct database setup script."""
from app import create_app
from app.extensions import db
import os

def setup_database():
    """Set up the database directly."""
    # Create Flask app with development config
    os.environ['FLASK_ENV'] = 'development'
    os.environ['DATABASE_URL'] = 'sqlite:///attendance.db'
    
    app = create_app()
    
    with app.app_context():
        # Create all tables
        print("Creating database tables...")
        db.create_all()
        print("Database tables created successfully!")
        
        # Create default data if needed
        from app.models.department import create_default_departments
        from app.models.user import create_default_users
        
        print("Creating default departments...")
        create_default_departments()
        print("Default departments created!")
        
        print("Creating default users...")
        create_default_users()
        print("Default users created!")

if __name__ == '__main__':
    setup_database()
