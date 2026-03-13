import json
import sqlite3
import os
from database import DB_PATH

def ingest_logs(file_path):
    if not os.path.exists(file_path):
        print(f"File {file_path} not found.")
        return
    
    with open(file_path, 'r') as f:
        logs = json.load(f)
        
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    for log in logs:
        cursor.execute('''
            INSERT INTO cloud_logs (
                timestamp, user_identity, source_ip, action, resource, status, cloud_provider, region
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            log.get("event_time"),
            log.get("user_identity"),
            log.get("source_ip"),
            log.get("action"),
            log.get("resource"),
            log.get("status"),
            log.get("cloud_provider"),
            log.get("region")
        ))
    
    conn.commit()
    conn.close()
    print(f"Successfully ingested {len(logs)} logs.")

if __name__ == "__main__":
    DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "sample_logs.json")
    ingest_logs(DATA_PATH)
