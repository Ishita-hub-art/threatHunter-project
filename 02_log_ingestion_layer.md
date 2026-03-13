# Log Ingestion Layer

## Overview
The Log Ingestion Layer is the entry point for the threat hunting platform. It reads raw cloud logs, filters out completely broken or irrelevant entries, and prepares the data for processing.

## Purpose of the Module
To act as a reliable collection mechanism that standardizes inbound data, ensuring the downstream processing and AI engines receive clean, predictable JSON records regardless of whether the log came from AWS or Azure.

## Inputs
* **Raw Cloud Logs:** Local JSON or CSV files simulating cloud provider activity exports.

## Processing Steps
1. **File Reading:** A Python script periodically monitors a local `incoming_logs/` directory and reads new JSON files.
2. **Format Validation:** The script checks if the JSON is properly formatted. Corrupt files are skipped and logged as errors.
3. **Dropping Noise:** Basic heuristic rules drop common, low-risk automated activities (e.g., simple `describe` API calls made by internal monitoring scripts) to save processing time later.
4. **Storage:** The accepted logs are saved to a temporary local database (e.g., SQLite) or a structured staging folder for the next module.

## Outputs
* **Validated Raw Logs:** Clean, valid JSON arrays stored locally, ready for feature extraction.

## Example Data Format
**Input (Raw AWS CloudTrail JSON):**
```json
{
  "Records": [
    {
      "eventVersion": "1.05",
      "userIdentity": { "type": "IAMUser", "userName": "student_admin" },
      "eventTime": "2026-03-13T10:00:00Z",
      "eventSource": "s3.amazonaws.com",
      "eventName": "DeleteBucket",
      "sourceIPAddress": "203.0.113.1"
    }
  ]
}
```

**Output (Validated Record):**
```json
{
  "user": "student_admin",
  "timestamp": "2026-03-13T10:00:00Z",
  "source": "s3.amazonaws.com",
  "action": "DeleteBucket",
  "ip_address": "203.0.113.1"
}
```
