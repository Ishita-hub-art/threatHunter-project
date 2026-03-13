# Investigation Dashboard (Academic Version)

## Overview
The Investigation Dashboard is a lightweight web interface designed for terminal-level or simple browser-based security monitoring. It provides a visual summary of the AI-detected threats, allowing a student or researcher to see the platform's results in real-time.

## Purpose of the Module
To translate raw database entries into a user-friendly visual display. It enables the security analyst to quickly identify high-risk alerts, view the AI's explanation for a threat, and see historical activity trends.

## Inputs
* **Alert Data:** JSON records from the local database (SQLite/JSON file).
* **Metric Counts:** Aggregate summaries (e.g., total logs, total alerts).

## Processing Steps
1. **Data Retrieval:** The frontend makes a request to the backend API to fetch the latest alerts.
2. **Filtering & Sorting:** The UI allows users to sort alerts by "Risk Score" or filter by "Threat Type".
3. **Visualization:** 
   * A table displays the latest 10-20 alerts.
   * Simple charts (e.g., bar charts or pie charts) show the distribution of threat categories.
4. **Drill-down:** Clicking an alert opens a detail view with the user activity timeline and specific reasons why the AI flagged it.

## Outputs
* **Web Interface:** A responsive dashboard UI.
* **Metric Cards:** Visual boxes showing total counts of threats, categorized by severity.

## Example Data Format
**Input (Alert List from API):**
```json
[
  {
    "id": "1",
    "timestamp": "2026-03-13 13:30",
    "threat": "Brute Force",
    "severity": "High",
    "score": 92.5
  },
  {
    "id": "2",
    "timestamp": "2026-03-13 13:35",
    "threat": "Account Compromise",
    "severity": "Critical",
    "score": 98.2
  }
]
```

**Output (UI Element Concept):**
* A red badge saying "CRITICAL: Account Compromise detected for user: dev_admin"
* A chart showing 60% of threats are "Credential Stuffing".
