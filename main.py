import json

with open("config.json", "r") as f:
    config = json.load(f)

from detection_rules import all_rules
from alert_manager import handle_alerts

log_file_path = "sample_logs.txt"
log_entries = []

with open(log_file_path, "r") as file:
    for line in file:
        parts = line.split(" ")

        if len(parts) < 7:
            continue

        ip = parts[0]
        time = parts[3].lstrip("[")
        path = parts[6]

        log_entries.append({
            'ip': ip,
            'time': time,
            'path': path
        })


alerts = []
for rule in all_rules:
    alerts += rule(log_entries, config=config)

handle_alerts(alerts)
