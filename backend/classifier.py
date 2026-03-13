import sqlite3
import os
from database import DB_PATH

def classify_threat(anomaly):
    """
    Takes an anomaly result and maps it to a human-readable threat.
    """
    score = anomaly['anomaly_score']
    user = anomaly['user_identity']
    
    # Heuristic mapping for academic demonstration
    threat_type = "Suspicious Behavior"
    severity = "Low"
    explanation = f"Anomaly score of {score} detected for user {user}."
    
    if score > 90:
        severity = "Critical"
        threat_type = "Account Compromise / Exfiltration"
        explanation = "High-confidence anomaly detected: Unusual IP combined with high-impact cloud action."
    elif score > 70:
        severity = "High"
        threat_type = "Insider Threat Pattern"
        explanation = "Significant deviation from user baseline detected in resource access frequency."
    elif score > 50:
        severity = "Medium"
        threat_type = "Unusual API Usage"
        explanation = "Moderate deviation detected. User is performing actions outside of normal hours or patterns."
    
    return {
        "timestamp": anomaly['timestamp'],
        "user_identity": user,
        "threat_type": threat_type,
        "anomaly_score": score,
        "risk_score": round(score * 1.1, 2), # Simplified risk multiplier
        "severity": severity,
        "explanation": explanation
    }

def save_alert(alert):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO alerts (
            timestamp, user_identity, threat_type, anomaly_score, risk_score, severity, explanation
        ) VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (
        alert['timestamp'],
        alert['user_identity'],
        alert['threat_type'],
        alert['anomaly_score'],
        alert['risk_score'],
        alert['severity'],
        alert['explanation']
    ))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    # Test classification
    test_anomaly = {
        "timestamp": "2026-03-13T10:12:00Z",
        "user_identity": "admin_test",
        "anomaly_score": 95.5
    }
    alert = classify_threat(test_anomaly)
    print("Classified Alert:", alert)
