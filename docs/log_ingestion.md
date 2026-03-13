# Log Ingestion Layer

## Overview
The **Log Ingestion Layer** is the primary intake point for the security pipeline. It handles the initial connection to cloud environments and ensures data is fetched reliably and consistently.

## Purpose of the Module
To bridge the gap between various cloud provider log formats and the internal processing logic. It ensures that the rest of the system receives a standardized stream of data, abstracting away the complexities of different cloud APIs.

## Inputs
- **Provider Logs**: JSON files or API streams from AWS S3 (CloudTrail) or Azure Event Hubs/Blob Storage.

## Processing Steps
1.  **Connection**: Establishes a secure session with the cloud storage or log export service.
2.  **Fetch**: Periodically retrieves new log files or listens to event-driven triggers.
3.  **Normalization**: Maps provider-specific keys (e.g., `userName` vs `caller`) to a unified internal schema.
4.  **Staging**: Writes the standardized JSON records to the local staging database (SQLite) for processing.

## Output
- **Standardized Logs**: Validated, clean JSON records stored in the `cloud_logs` table.

## Example Data
**Input (Raw AWS JSON):**
```json
{ "userIdentity": { "userName": "dev_user" }, "eventSource": "iam.amazonaws.com", "sourceIPAddress": "1.2.3.4" }
```
**Output (Standardized Payload):**
```json
{ "user_identity": "dev_user", "cloud_provider": "AWS", "source_ip": "1.2.3.4" }
```
