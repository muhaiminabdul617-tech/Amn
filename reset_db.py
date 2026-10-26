"""Reset database script."""
import os

def reset_database():
    """Delete the database file and recreate it."""
    try:
        # Delete the database file if it exists
        db_file = 'attendance.db'
        if os.path.exists(db_file):
            os.remove(db_file)
            print(f"Deleted existing database: {db_file}")
        
        print("Database reset successfully")
        
    except Exception as e:
        print(f"Error resetting database: {str(e)}")

if __name__ == '__main__':
    reset_database()
