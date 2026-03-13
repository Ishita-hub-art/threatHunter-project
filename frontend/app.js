const API_BASE = "http://localhost:8000/api/v1";

// DOM Elements
const statLogs = document.getElementById('stat-logs');
const statAlerts = document.getElementById('stat-alerts');
const statCritical = document.getElementById('stat-critical');
const threatTableBody = document.querySelector('#threat-table tbody');
const ingestBtn = document.getElementById('ingest-btn');
const analyzeBtn = document.getElementById('analyze-btn');

async function fetchMetrics() {
    try {
        const res = await fetch(`${API_BASE}/metrics`);
        const data = await res.json();
        
        statLogs.innerText = data.total_logs;
        statAlerts.innerText = data.total_alerts;
        statCritical.innerText = data.severity_distribution.Critical || 0;
    } catch (err) {
        console.error("Error fetching metrics:", err);
    }
}

async function fetchAlerts() {
    try {
        const res = await fetch(`${API_BASE}/alerts`);
        const alerts = await res.json();
        
        threatTableBody.innerHTML = '';
        alerts.forEach(alert => {
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${alert.timestamp}</td>
                <td>${alert.user_identity}</td>
                <td>${alert.threat_type}</td>
                <td>${alert.anomaly_score}</td>
                <td><span class="severity-badge severity-${alert.severity.toLowerCase()}">${alert.severity}</span></td>
                <td><span class="view-btn">Investigate</span></td>
            `;
            threatTableBody.appendChild(row);
        });
    } catch (err) {
        console.error("Error fetching alerts:", err);
    }
}

ingestBtn.addEventListener('click', async () => {
    ingestBtn.innerText = "Ingesting...";
    await fetch(`${API_BASE}/ingest`, { method: 'POST' });
    setTimeout(() => {
        ingestBtn.innerText = "Ingest Logs";
        fetchMetrics();
    }, 1000);
});

analyzeBtn.addEventListener('click', async () => {
    analyzeBtn.innerText = "Analyzing...";
    await fetch(`${API_BASE}/analyze`, { method: 'POST' });
    setTimeout(() => {
        analyzeBtn.innerText = "Run AI Analysis";
        fetchMetrics();
        fetchAlerts();
    }, 2000);
});

// Initial Load
fetchMetrics();
fetchAlerts();

// Refresh every 30 seconds
setInterval(() => {
    fetchMetrics();
    fetchAlerts();
}, 30000);
