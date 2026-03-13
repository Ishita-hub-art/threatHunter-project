# System Architecture

## Overview
The **ThreatHunter** platform is designed as a modular, end-to-end security pipeline. It transforms raw, unstructured cloud activity logs into high-fidelity, prioritized security alerts by leveraging machine learning and automated risk scoring.

## Purpose of the Module
The architecture defines the structural layout and data flow of the entire system. It ensures that components are decoupled, allowing for modular updates (e.g., swapping the ML model or changing the cloud provider) without disrupting the entire pipeline.

## Inputs
- **Cloud Activity Logs**: Unstructured JSON or CSV exports from AWS (CloudTrail) or Azure (Activity Logs).

## Processing Steps
1.  **Ingestion**: Authenticates with cloud sources and pulls raw activity events.
2.  **Preprocessing**: Cleans, parses, and extracts critical security features (Identity, Context, Resource).
3.  **AI Detection**: Processes the feature vectors through anomaly detection models to find outliers.
4.  **Classification**: Maps anomalies to human-understandable security threats (e.g., Unauthorized Login).
5.  **Alerting & Visualization**: Categorizes threat severity and displays findings on the central dashboard.

## Output
- **Real-Time Security Intelligence**: A live stream of prioritized threats visualized on a web dashboard.

## Example Data
The architecture ensures data transitions from a raw log:
```json
{"eventName": "S3:GetObject", "userId": "admin", "sourceIP": "203.0.113.5"}
```
To a prioritized alert:
```json
{"threat": "Data Exfiltration", "severity": "CRITICAL", "action": "REVOKE_TOKEN"}
```
