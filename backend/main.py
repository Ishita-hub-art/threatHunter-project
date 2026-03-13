from fastapi import FastAPI, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
import sqlite3
import os
from database import DB_PATH, init_db
from ingestion import ingest_logs
from ai_engine import AnomalyDetector
from classifier import classify_threat, save_alert

app = FastAPI(title="ThreatHunter API")

# Enable CORS for frontend integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize DB on start
@app.on_event("startup")
def startup():
    init_db()

@app.get("/api/v1/metrics")
def get_metrics():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute("SELECT COUNT(*) FROM cloud_logs")
    total_logs = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM alerts")
    total_alerts = cursor.fetchone()[0]
    
    cursor.execute("SELECT severity, COUNT(*) FROM alerts GROUP BY severity")
    severity_dist = dict(cursor.fetchall())
    
    conn.close()
    
    return {
        "total_logs": total_logs,
        "total_alerts": total_alerts,
        "severity_distribution": severity_dist
    }

@app.get("/api/v1/alerts")
def get_alerts():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM alerts ORDER BY id DESC LIMIT 50")
    alerts = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return alerts

@app.post("/api/v1/analyze")
def run_analysis():
    # 1. Detect
    detector = AnomalyDetector()
    anomalies = detector.detect_anomalies()
    
    # 2. Classify and Save
    new_alerts = []
    for anomaly in anomalies:
        alert = classify_threat(anomaly)
        save_alert(alert)
        new_alerts.append(alert)
        
    return {"status": "Analysis complete", "new_alerts_count": len(new_alerts)}

@app.post("/api/v1/ingest")
def trigger_ingest(background_tasks: BackgroundTasks):
    data_path = os.path.join(os.path.dirname(__file__), "..", "data", "sample_logs.json")
    background_tasks.add_task(ingest_logs, data_path)
    return {"status": "Ingestion started in background"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
