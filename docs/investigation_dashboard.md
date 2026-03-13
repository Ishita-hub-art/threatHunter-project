# Investigation Dashboard

## Overview
The **Investigation Dashboard** is the primary interface for security operations. It provides a visual, real-time command center for monitoring cloud security health.

## Purpose of the Module
To facilitate rapid decision-making by human security analysts. It aggregates dozens of complex security modules into a single "pane of glass," presenting the most critical threats in an intuitive, aesthetic layout.

## Inputs
- **Alert API Stream**: Real-time JSON data from the backend alert service.
- **Aggregated Metrics**: Statistical summaries (Counts, Trends) from the SQLite database.

## Processing Steps
1.  **State Management**: Fetches and maintains the current list of active alerts in the browser memory.
2.  **Visual Rendering**: Dynamically builds UI components like severity badges, heatmaps, and trend charts.
3.  **Real-time Updates**: Polls the backend every 30 seconds (or uses WebSockets) to refresh the dashboard state.
4.  **Investigation Workflow**: Handles user interactions, such as clicking an alert to expand the "Blast Radius" or "Activity Timeline".

## Output
- **Graphical UI**: A modern, dark-mode web application accessible via browser.

## Example Data
**Backend Event:**
`{ "threat": "Account Compromise", "count": 1 }`

**UI Result:**
A pulsating red notification card at the top of the dashboard feed.
```html
<div class="severity-badge severity-critical">CRITICAL</div>
```
