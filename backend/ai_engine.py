import sqlite3
import os
import json
from database import DB_PATH

class AnomalyDetector:
    def __init__(self):
        pass
        
    def get_logs(self):
        conn = sqlite3.connect(DB_PATH)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM cloud_logs")
        logs = [dict(row) for row in cursor.fetchall()]
        conn.close()
        return logs

    def calculate_anomaly_score(self, log):
        """
        Simplified rule-based anomaly scoring for academic implementation.
        Returns a score from 0-100.
        """
        score = 0
        
        # 1. Unusual Time (Late night: 00:00 - 05:00)
        try:
            # Format: 2026-03-13T10:12:00Z
            time_str = log['timestamp'].split('T')[1].split(':')[0]
            hour = int(time_str)
            if 0 <= hour <= 5:
                score += 30
        except:
            pass
            
        # 2. Status Failure
        if log['status'] == 'Failure':
            score += 25
            
        # 3. Critical Actions (Delete, Write, Put)
        critical_keywords = ['Delete', 'Write', 'Put', 'Terminate', 'Remove']
        if any(kw in log['action'] for kw in critical_keywords):
            score += 25
            
        # 4. Unusual Location (Simplified: IP starting with 185 or 203)
        # In a real app this would use GeoIP. Here we use mock patterns.
        if log['source_ip'].startswith('185.') or log['source_ip'].startswith('203.'):
            score += 20
            
        return min(score, 100)

    def detect_anomalies(self):
        logs = self.get_logs()
        if not logs:
            print("No logs found.")
            return []

        results = []
        for log in logs:
            score = self.calculate_anomaly_score(log)
            # Only flag as suspicious if score is significant
            if score >= 40:
                results.append({
                    "log_id": log['id'],
                    "user_identity": log['user_identity'],
                    "timestamp": log['timestamp'],
                    "anomaly_score": float(score),
                    "status": "SUSPICIOUS"
                })
        
        return results

if __name__ == "__main__":
    detector = AnomalyDetector()
    anomalies = detector.detect_anomalies()
    print(f"Detected {len(anomalies)} anomalies using rule-based engine.")
    for a in anomalies:
        print(a)
