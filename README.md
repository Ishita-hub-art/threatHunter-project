# ThreatHunter

**ThreatHunter** is an AI-powered Cloud Security Threat Hunting Platform designed to automatically analyze cloud activity logs and identify potential security threats without manual intervention.

## 🚀 Overview

The platform ingests activity logs from major cloud providers (AWS, Azure), processes them using machine learning algorithms to detect anomalies, and classifies these anomalies into specific threat categories. It provides a modern investigation dashboard for security analysts to monitor and respond to threats in real-time.

## ✨ Key Features

-   **Log Ingestion**: Seamlessly collects activity logs from AWS CloudTrail and Azure Activity Logs.
-   **Behavior Anomaly Detection**: Uses AI (Isolation Forest) to establish behavioral baselines and detect deviations.
-   **Threat Classification**: Categorizes anomalies into threats like Brute Force, Account Compromise, or Data Exfiltration.
-   **Risk Scoring**: Assigns severity levels (Low, Medium, High, Critical) based on risk factors.
-   **Investigation Dashboard**: A premium UI for visual analytics and real-time threat monitoring.

## 🛠️ Technology Stack

-   **Backend**: Python, FastAPI
-   **Machine Learning**: Scikit-Learn (Behavioral Analysis)
-   **Database**: SQLite (Local storage)
-   **Frontend**: HTML5, CSS3, JavaScript (Vanilla)

## 📁 Project Structure

```bash
/ThreatHunter
  /backend
    main.py           # API Server
    ingestion.py      # Log ingestion logic
    ai_engine.py      # Anomaly detection model
    classifier.py     # Threat grading rules
    database.py       # SQL database management
  /frontend
    index.html        # Main dashboard
    styles.css        # UI styling
    app.js            # Frontend logic
  /docs
    architecture_overview.md
    log_ingestion_layer.md
    ...               # See docs/ for full architectural details
  /data
    sample_logs.json  # Mock cloud log data for development
  /screenshots
    dashboard.png     # Visual preview of the platform
```

## 🏁 Getting Started

### 1. Prerequisites
- Python 3.8+
- pip

### 2. Installation
Clone the repository and install the required dependencies:
```bash
pip install fastapi uvicorn
```

### 3. Running the Project
1. **Start the Backend**:
   ```bash
   cd backend
   python main.py
   ```
2. **Access the Dashboard**:
   Open `frontend/index.html` in your web browser.

---
*Created for Academic Research & Prototype Demonstration.*
