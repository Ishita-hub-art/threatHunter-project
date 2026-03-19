import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "threat_hunter.db")

def get_db_connection():
    """Returns a thread-safe SQLite connection."""
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Logs Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cloud_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            user_identity TEXT,
            source_ip TEXT,
            action TEXT,
            resource TEXT,
            status TEXT,
            cloud_provider TEXT,
            region TEXT
        )
    ''')
    
    # Alerts Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS alerts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            user_identity TEXT,
            threat_type TEXT,
            anomaly_score REAL,
            risk_score REAL,
            severity TEXT,
            explanation TEXT,
            status TEXT DEFAULT 'OPEN'
        )
    ''')
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    print("Database initialized successfully.")
