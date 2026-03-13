# Technical Implementation Structure (Academic Version)

## Overview
The platform is built as a modular Python application with a simple decoupled frontend. It prioritizes ease of setup, local data handling, and code readability over distributed enterprise scaling.

## Purpose of the Module
To define the software stack and file structure, ensuring that the system can be easily deployed on a single laptop or development environment for demonstration purposes.

## Inputs
* **Source Code:** Python scripts and JS/HTML files.
* **Local Data:** CSV/JSON log files.

## Processing Steps
1. **Backend (Python/FastAPI):**
   * Handles business logic, ML model inference, and API routing.
   * Manages the Local Database (SQLite).
2. **AI Logic:**
   * Uses `scikit-learn` for anomaly detection (Isolation Forest).
   * Loads pre-trained models or trains on the fly using historical logs.
3. **Storage:**
   * Raw logs and alerts are stored in a simple SQLite database (`threat_hunter.db`).
4. **Frontend:**
   * A modern, single-page application built with HTML/CSS/JS (or a framework like React).
   * Communicates with the Backend via REST API.

## Outputs
* **Running Application:** A local web server (Uvicorn/Flask) serving the security dashboard.

## File Structure Example
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
    app.js            # Frontend logic
    styles.css        # UI styling
  /data
    sample_logs.json  # Mock cloud log data
```
