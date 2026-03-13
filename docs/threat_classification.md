# Threat Classification Module

## Overview
The **Threat Classification Module** provides a qualitative assessment of the mathematical anomalies detected by the AI engine. It contextualizes risk by mapping outliers to known security TTPs.

## Purpose of the Module
To transform raw "anomaly scores" into human-actionable alerts. This module ensures that security analysts receive a clear threat label (e.g., "Brute Force Attack") rather than just a number, allowing for faster triage.

## Inputs
- **Enriched Anomaly Logs**: JSON records containing anomaly scores and original log context.

## Processing Steps
1.  **Pattern Matching**: Compares the anomaly sequence against a library of known attack patterns (Heuristic Engine).
2.  **Risk Calibration**: Adjusts the score based on the sensitivity of the target asset and the privilege level of the actor.
3.  **Severity Mapping**: Groups risks into four tiers (Low, Medium, High, Critical) based on the calculated risk score.
4.  **Alert Generation**: Creates a high-fidelity alert object for transmission to the dashboard.

## Output
- **Classified Security Alert**: A detailed threat object containing classification, severity, and remediation advice.

## Example Data
**Input:**
`Anomaly Score: 95.5; Action: TerminateInstances`

**Output:**
```json
{
  "threat_type": "Data Destruction / DDoS",
  "severity": "CRITICAL",
  "explanation": "High-impact destructive action detected from unauthorized IP."
}
```
