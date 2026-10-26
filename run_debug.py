"""Debug script for running the application."""
from app import create_app
import logging
import sys
import os

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger(__name__)

def run_app():
    """Run the application with debug logging."""
    try:
        # Set environment variables
        os.environ['FLASK_ENV'] = 'development'
        os.environ['FLASK_DEBUG'] = '1'
        os.environ['DATABASE_URL'] = 'sqlite:///attendance.db'
        
        # Create and configure app
        app = create_app()
        
        # Run app
        app.run(debug=True, use_reloader=False)
        
    except Exception as e:
        logger.error(f"Application error: {str(e)}", exc_info=True)

if __name__ == '__main__':
    run_app()
