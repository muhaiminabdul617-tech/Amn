"""Database migration script."""
from app import create_app
from app.extensions import db
from flask_migrate import Migrate, init, migrate, upgrade
import os
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def migrate_database():
    """Perform database migration."""
    try:
        # Set environment variables
        os.environ['FLASK_ENV'] = 'development'
        os.environ['DATABASE_URL'] = 'sqlite:///attendance.db'
        
        # Create app
        app = create_app()
        
        # Initialize migrations
        migrations_dir = os.path.join(app.root_path, '..', 'migrations')
        
        with app.app_context():
            # Initialize migrations if they don't exist
            if not os.path.exists(migrations_dir):
                logger.info("Initializing migrations...")
                init()
            
            # Create migration
            logger.info("Creating migration...")
            migrate()
            
            # Apply migration
            logger.info("Applying migration...")
            upgrade()
            
            logger.info("Migration completed successfully!")
            
    except Exception as e:
        logger.error(f"Migration error: {str(e)}", exc_info=True)

if __name__ == '__main__':
    migrate_database()
