"""Create admin user script."""
import os
import sys
import logging
from app import create_app
from app.extensions import db
from app.models.user import User
from app.models.department import Department, create_default_departments
from app.models.faculty import Faculty, create_default_faculties
from config import DevelopmentConfig

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(name)s: %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

def init_database(app):
    """Initialize database tables."""
    with app.app_context():
        try:
            # Create all tables
            db.create_all()
            logger.info("Database tables created successfully")
            return True
        except Exception as e:
            logger.error(f"Error creating database tables: {str(e)}")
            return False

def create_admin_user():
    """Create admin user if it doesn't exist."""
    try:
        # Set environment variables
        os.environ['FLASK_DEBUG'] = '1'
        os.environ['DATABASE_URL'] = 'sqlite:///attendance.db'
        os.environ['SECRET_KEY'] = 'dev-key-123'
        
        # Create app with development config
        app = create_app(DevelopmentConfig)
        
        # Initialize database
        if not init_database(app):
            logger.error("Failed to initialize database")
            return False
        
        with app.app_context():
            try:
                # Create default faculty
                faculty = create_default_faculties()
                if not faculty:
                    faculty = Faculty.query.filter_by(code='SICT').first()
                
                # Create default department
                it_dept = create_default_departments(faculty)
                if not it_dept:
                    it_dept = Department.query.filter_by(code='IT').first()
                
                # Check if admin user exists
                admin = User.query.filter_by(login_id='ADMIN001').first()
                
                if admin:
                    logger.info("Admin user exists, updating password...")
                    admin.password = 'Admin@2024'
                    db.session.commit()
                    logger.info("Admin password updated successfully")
                else:
                    # Create new admin user
                    admin = User(
                        login_id='ADMIN001',
                        email='admin@unilorin.edu.ng',
                        first_name='Administrator',
                        last_name='User',
                        role='admin'
                    )
                    admin.password = 'Admin@2024'
                    admin.department_id = it_dept.id
                    db.session.add(admin)
                    db.session.commit()
                    logger.info("Created admin user successfully")
                
                logger.info("Admin credentials:")
                logger.info("Login ID: ADMIN001")
                logger.info("Password: Admin@2024")
                return True
                
            except Exception as e:
                logger.error(f"Database error: {str(e)}")
                db.session.rollback()
                return False
                
    except Exception as e:
        logger.error(f"Application error: {str(e)}")
        return False

if __name__ == '__main__':
    success = create_admin_user()
    sys.exit(0 if success else 1)
