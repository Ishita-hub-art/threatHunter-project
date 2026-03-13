# ThreatHunter
### AI-Based Cloud Security Threat Hunting Platform

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green.svg)](https://fastapi.tiangolo.com/)

**ThreatHunter** is a professional-grade, AI-powered security platform designed to automatically analyze cloud activity logs and identify potential security threats without manual intervention. It establishes behavioral baselines and detects anomalies using advanced machine learning.

---

## 🚀 Overview

Modern cloud environments generate massive volumes of activity logs. Security teams often struggle to manually analyze this data to find subtle threats like lateral movement or data exfiltration. **ThreatHunter** solves this by providing an automated, AI-driven detection pipeline that ingests, cleans, analyzes, and classifies security events in near real-time.

---

## ✨ Key Features

-   **📡 Multi-Cloud Ingestion**: Automated collection and normalization of AWS CloudTrail and Azure Activity logs.
-   **🤖 AI Anomaly Detection Engine**: Uses unsupervised machine learning (Isolation Forest) to detect behavioral outliers.
-   **🏷️ Intelligent Threat Classification**: Maps detected anomalies to specific TTPs (Tactics, Techniques, and Procedures).
-   **⚖️ Dynamic Risk Scoring**: Context-aware severity assessment with priority tiering (Low, Medium, High, Critical).
-   **🖥️ Investigation Dashboard**: Modern, glassmorphism-inspired UI for real-time monitoring and forensic analysis.

---

## 🏗️ System Architecture

The following diagram illustrates the high-level data flow through the ThreatHunter platform:

```mermaid
graph TD
    subgraph CloudSources ["Cloud Log Sources"]
        AWS[AWS CloudTrail]
        Azure[Azure Activity]
    end

    subgraph IngestionLayer ["Data Ingestion"]
        Ingest[Log Ingestion Layer]
    end

    subgraph ProcessingLayer ["Processing Engine"]
        Process[Preprocessing & Feature Extraction]
    end

    subgraph AIEngine ["AI & ML Engine"]
        Anomaly[AI Anomaly Detection]
    end

    subgraph LogicLayer ["Classification & Scoring"]
        Classify[Threat Classification]
        Risk[Risk Scoring Engine]
    end

    subgraph FrontEnd ["Monitoring & Alerts"]
        Alerts[Alerting System]
        Dashboard[Investigation Dashboard]
    end

    AWS --> Ingest
    Azure --> Ingest
    Ingest --> Process
    Process --> Anomaly
    Anomaly --> Classify
    Classify --> Risk
    Risk --> Alerts
    Alerts --> Dashboard

    style CloudSources fill:#f5f5f5,stroke:#333
    style IngestionLayer fill:#eef2ff,stroke:#6366f1
    style ProcessingLayer fill:#ecfdf5,stroke:#10b981
    style AIEngine fill:#fff7ed,stroke:#f59e0b
    style LogicLayer fill:#fef2f2,stroke:#ef4444
    style FrontEnd fill:#f8fafc,stroke:#64748b
```

For more detailed information, see our [Architecture Documentation](docs/architecture.md).

---

## 🛠️ Technology Stack

| Layer | Technologies |
| :--- | :--- |
| **Backend** | Python 3.8+, FastAPI, Uvicorn |
| **Data Analysis** | Scikit-Learn (Isolation Forest), Pandas, Numpy |
| **Storage** | SQLite3 (Persistent Metadata) |
| **Frontend** | HTML5, CSS3 (Modern Glassmorphism), JavaScript (Vanilla) |
| **Testing** | Postman, Manual Validation |

---

## 📁 Project Structure

```bash
ThreatHunter/
├── docs/             # Technical Documentation
│   ├── architecture.md
│   ├── log_ingestion.md
│   ├── anomaly_detection.md
│   ├── threat_classification.md
│   └── investigation_dashboard.md
├── backend/          # Python AI and log processing modules
│   ├── main.py       # API Entry Point
│   ├── ingestion.py  # Data Intake
│   ├── ai_engine.py  # ML Scoring logic
│   ├── classifier.py # Risk assessment
│   └── database.py   # SQL persistence
├── frontend/         # Dashboard UI
│   ├── index.html    # Layout
│   ├── styles.css    # Aesthetics
│   └── app.js        # Logic
├── data/             # Sample Log datasets
├── diagrams/         # Architectural Visuals
└── screenshots/      # UI Previews
```

---

## 🏁 Getting Started

### Installation
1.  **Clone the Repository**:
    ```bash
    git clone https://github.com/YourUsername/ThreatHunter.git
    cd ThreatHunter
    ```
2.  **Install Dependencies**:
    ```bash
    pip install fastapi uvicorn
    ```

### Running the Platform
1.  **Start the Backend API**:
    ```bash
    python backend/main.py
    ```
2.  **View the Dashboard**:
    Open `frontend/index.html` in your browser.

---

## 🔮 Future Improvements

-   [ ] **Real-time API Hooking**: Directly integrate with AWS CloudWatch and Azure Monitor APIs.
-   [ ] **GPU Acceleration**: Implement deep learning models for sequence-based anomaly detection.
-   [ ] **Multi-user RBAC**: Role-based access control for different tiers of security analysts.
-   [ ] **Containerization**: Full Docker/Kubernetes deployment configurations.

---
*Maintained by the ThreatHunter Community. Licensed under the MIT License.*
