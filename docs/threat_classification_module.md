# Threat Classification and Risk Scoring Module

## Overview
While the AI engine identifies *that* an anomaly occurred, this module identifies *what* the threat is and *how bad* it is. It maps unusual mathematical scores back to human-understandable security incidents.

## Purpose of the Module
To act as the decision-making brain of the pipeline. It takes an anomaly, assigns it a recognized cybersecurity categorization (e.g., "Insider Threat"), calculates a final priority score based on risk factors, and determines if an alert should be triggered.

## Inputs
* **Anomaly Records:** JSON objects outputted by the AI engine containing Anomaly Scores and event data.

## Processing Steps
1. **Context Enrichment:** The module checks the user's privilege level (e.g., is this a guest or an admin?) from a local configuration file or SQLite database.
2. **Threat Classification Rules:** Uses `if/else` heuristic logic (or a simple Python Random Forest classifier) to label the threat:
   * Example: `IF action='Login_Failure' AND velocity > 20 THEN type='Brute Force Attack'`
3. **Risk Scoring Calculation:** Calculates a final Risk Score by multiplying the AI Anomaly Score by weight factors (e.g., Admin user context multiplies the score by 1.5).
4. **Severity Tiering:** Maps the final score to a severity label:
   * Low: 0-39
   * Medium: 40-69
   * High: 70-89
   * Critical: 90-100

## Outputs
* **Classified Threat Alerts:** JSON payloads enriched with threat categorizations, severity levels, and ready-to-display risk details.

## Example Data Format
**Input (Anomaly Record):**
```json
{
  "user": "db_admin",
  "action": "Mass_Data_Export",
  "anomaly_score": 88.5
}
```

**Output (Classified Threat Alert):**
```json
{
  "event_id": "evt-001",
  "user": "db_admin",
  "threat_type": "Data Exfiltration",
  "risk_score": 96.0,
  "severity_level": "CRITICAL"
}
```
