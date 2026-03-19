import sqlite3
import os
import math
from collections import defaultdict
from database import DB_PATH

class AnomalyDetector:
    def __init__(self):
        self.action_counts = defaultdict(int)
        self.user_action_counts = defaultdict(lambda: defaultdict(int))
        self.total_logs = 0

    def get_logs(self):
        conn = sqlite3.connect(DB_PATH)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM cloud_logs")
        logs = [dict(row) for row in cursor.fetchall()]
        conn.close()
        return logs

    def build_baselines(self, logs):
        """
        Builds statistical baselines from historical logs without requiring ML libraries.
        Analyzes global action frequency and user-specific behavior.
        """
        self.total_logs = len(logs)
        for log in logs:
            self.action_counts[log['action']] += 1
            self.user_action_counts[log['user_identity']][log['action']] += 1

    def calculate_statistical_anomaly(self, log):
        """
        Calculates an anomaly score (0-100) using statistical rarity (Z-score heuristic approach).
        """
        score = 0.0
        
        # Heuristic 1: Global Action Rarity (Inverse Document Frequency style)
        action_freq = self.action_counts.get(log['action'], 0)
        if self.total_logs > 0:
            probability = action_freq / self.total_logs
            # If an action has never been seen or is extremely rare (< 5% of logs)
            if probability < 0.05:
                score += 35.0 * (1 - probability)
                
        # Heuristic 2: User-Specific Rarity
        user_actions = sum(self.user_action_counts[log['user_identity']].values())
        if user_actions > 0:
            user_specific_freq = self.user_action_counts[log['user_identity']].get(log['action'], 0)
            user_probability = user_specific_freq / user_actions
            # If the user rarely or never does this action
            if user_probability < 0.1:
                score += 40.0 * (1 - user_probability)
        else:
            # Brand new user doing something
            score += 25.0

        # Heuristic 3: Status Failure
        if log['status'] == 'Failure':
            score += 20.0
            
        # Heuristic 4: Critical Resource Context (Heuristic weighting)
        critical_keywords = ['Delete', 'Write', 'Put', 'Terminate', 'Remove']
        if any(kw in log['action'] for kw in critical_keywords):
            score += 15.0

        return min(round(score, 2), 100.0)

    def detect_anomalies(self):
        logs = self.get_logs()
        if not logs:
            print("No logs found.")
            return []

        # Train statistical model on current historical data
        self.build_baselines(logs)

        results = []
        for log in logs:
            score = self.calculate_statistical_anomaly(log)
            # Threshold for statistical outlier
            if score >= 45.0:
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
    print(f"Detected {len(anomalies)} anomalies using Statistical Analysis Engine.")
    for a in anomalies:
        print(a)
