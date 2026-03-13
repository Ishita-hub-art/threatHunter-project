# Architecture Overview

## Overview
The AI-Based Cloud Security Threat Hunting Platform is a modular system designed to automatically analyze cloud activity logs and detect potential security threats using Machine Learning. This project focuses on a streamlined, implementation-friendly pipeline suitable for academic research and prototyping.

## Purpose of the Module
To provide a clear, logical diagram of how data flows from raw cloud logs through to the final security analyst dashboard, avoiding complex enterprise infrastructure in favor of a clean, programmatic pipeline.

## Inputs
* **Cloud Logs:** Sample JSON files representing AWS CloudTrail Logs or Azure Activity Logs.

## Processing Steps
The architecture follows a strict, linear progression:
1. **Log Ingestion:** Reads the JSON log files from the local file system.
2. **Log Processing:** Cleans the data, extracts necessary features, and normalizes it into a standard format.
3. **AI Anomaly Detection:** Uses Python-based Machine Learning models (e.g., Scikit-Learn Isolation Forests) to evaluate behavioral features and assign anomaly scores.
4. **Threat Classification:** A rule-based or supervised ML module that categorizes anomalies (score > 50) into specific threat types (e.g., Data Exfiltration, Brute Force).
5. **Alert System:** Checks the severity of the classified threat and flags critical items.
6. **Investigation Dashboard:** A simple web interface (e.g., Streamlit or Flask) that queries a basic database (e.g., SQLite or MongoDB) to display the alerts to the user.

## Outputs
* A clear, end-to-end operational pipeline that takes raw JSON files and outputs actionable security alerts on a User Interface.

## Example Data Format
The overarching architecture takes this input:
```json
{"event_name": "ConsoleLogin", "source_ip": "192.168.1.5", "user_agent": "Mozilla", "response_status": "Failure"}
```
And eventually presents this output to the dashboard:
```json
{"threat_type": "Brute Force Attack", "anomaly_score": 92.5, "severity": "High", "action_required": "Investigate User"}
```
