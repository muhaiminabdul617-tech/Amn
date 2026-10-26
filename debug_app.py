"""Debug application startup."""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Create Flask app
app = Flask(__name__)

# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///attendance.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy with debug mode
db = SQLAlchemy(app)

def main():
    """Run debug checks."""
    try:
        # Test database connection
        with app.app_context():
            db.engine.connect()
            logger.info("Database connection successful!")
            
            # Create tables
            db.create_all()
            logger.info("Database tables created!")
            
    except Exception as e:
        logger.error(f"Error: {str(e)}", exc_info=True)

if __name__ == '__main__':
    main()
