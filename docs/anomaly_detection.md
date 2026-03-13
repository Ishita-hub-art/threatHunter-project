# AI Anomaly Detection Engine

## Overview
The **AI Anomaly Detection Engine** is the core intellectual layer of the project. It uses mathematical modeling to understand established user behaviors and identify outliers that deviate from the norm.

## Purpose of the Module
To detect "unknown unknowns"—security threats that don't match known signatures or rules. By building a behavioral profile for every entity, the engine can flag rare or uncharacteristic actions, such as a developer accessing a production database for the first time.

## Inputs
- **Feature Vectors**: Multi-dimensional numerical arrays representing the "state" of a security event (Time, User, Action Frequency, Resource Sensitivity).

## Processing Steps
1.  **Feature Extraction**: Converts categorical data (e.g., username) into numerical values.
2.  **Baseline Loading**: Retrieves the historical behavioral baseline for the specific user/entity.
3.  **Model Inference**: Feeds the current event into the **Isolation Forest** model to calculate an anomaly score.
4.  **Scoring**: Generates a confidence-adjusted score from 0 (Normal) to 100 (Highly Anomalous).

## Output
- **Anomaly Metadata**: An enriched log record containing the `anomaly_score` and a text-based reason for the suspicion.

## Example Data
**Processing Logic:**
`IF Resource_Sensitivity = High AND User_Baseline_History = None THEN Score = 90`

**Output Result:**
```json
{ "user_identity": "guest_user", "anomaly_score": 92.4, "anomaly_status": "SUSPICIOUS" }
```
