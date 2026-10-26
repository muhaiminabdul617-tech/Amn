"""Create admin user using direct SQLite."""
import sqlite3
from werkzeug.security import generate_password_hash

def create_admin():
    """Create admin user directly in SQLite."""
    try:
        # Connect to database
        conn = sqlite3.connect('attendance.db')
        cursor = conn.cursor()
        
        # Create users table if not exists
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            login_id VARCHAR(20) UNIQUE NOT NULL,
            email VARCHAR(120) UNIQUE,
            password_hash VARCHAR(128),
            first_name VARCHAR(64),
            last_name VARCHAR(64),
            role VARCHAR(20) NOT NULL,
            is_active BOOLEAN DEFAULT 1
        )
        ''')
        
        # Check if admin exists
        cursor.execute('SELECT * FROM users WHERE login_id = ?', ('ADMIN001',))
        admin = cursor.fetchone()
        
        if admin:
            print("Admin user already exists")
            # Update password
            cursor.execute(
                'UPDATE users SET password_hash = ? WHERE login_id = ?',
                (generate_password_hash('admin123'), 'ADMIN001')
            )
            print("Admin password updated")
        else:
            # Create admin user
            cursor.execute('''
            INSERT INTO users (login_id, email, password_hash, first_name, last_name, role)
            VALUES (?, ?, ?, ?, ?, ?)
            ''', (
                'ADMIN001',
                'admin@unilorin.edu.ng',
                generate_password_hash('admin123'),
                'Administrator',
                'User',
                'admin'
            ))
            print("Admin user created successfully")
            print("Login ID: ADMIN001")
            print("Password: admin123")
        
        # Commit changes
        conn.commit()
        
    except Exception as e:
        print(f"Error: {str(e)}")
        conn.rollback()
    finally:
        conn.close()

if __name__ == '__main__':
    create_admin()
