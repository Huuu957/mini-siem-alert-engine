from collections import defaultdict
from datetime import datetime, timedelta

def detect_brute_force(log_entries, config=None):
    threshold = config.get("brute_force", {}).get("threshold", 5)
    window_seconds = config.get("brute_force", {}).get("window_seconds", 60)

    alerts = []
    ip_access_times = defaultdict(list)

    for entry in log_entries:
        ip = entry['ip']
        timestamp_str = entry['time']
        path = entry['path']

        if "/login" not in path:
            continue

        try:
            timestamp = datetime.strptime(timestamp_str, "%d/%b/%Y:%H:%M:%S")
        except ValueError:
            continue

        ip_access_times[ip].append(timestamp)

        ip_access_times[ip] = [
            t for t in ip_access_times[ip]
            if timestamp - t <= timedelta(seconds=window_seconds)
        ]

        if len(ip_access_times[ip]) >= threshold:
            alerts.append({
                'ip': ip,
                'count': len(ip_access_times[ip]),
                'time': timestamp_str,
                'path': path,
                'type': 'Brute Force'
            })

    return alerts

def detect_path_scanning(log_entries, config=None):
    threshold = config.get("path_scanning", {}).get("threshold", 7)
    window_seconds = config.get("path_scanning", {}).get("window_seconds", 60)
    from collections import defaultdict
    from datetime import datetime, timedelta

    alerts = []
    ip_paths = defaultdict(list)

    for entry in log_entries:
        ip = entry['ip']
        timestamp_str = entry['time']
        path = entry['path']

        try:
            timestamp = datetime.strptime(timestamp_str, "%d/%b/%Y:%H:%M:%S")
        except ValueError:
            continue

        ip_paths[ip].append((timestamp, path))

        # Filter for entries in the time window
        recent_paths = [
            p for t, p in ip_paths[ip]
            if timestamp - t <= timedelta(seconds=window_seconds)
        ]

        # Unique paths = multiple scanning attempts
        unique_paths = set(recent_paths)

        if len(unique_paths) >= threshold:
            alerts.append({
                'ip': ip,
                'count': len(unique_paths),
                'time': timestamp_str,
                'path': "multiple",
                'type': 'Path Scanning'
            })

    return alerts


# Export all rules here for modular usage
all_rules = [
    detect_brute_force,
    detect_path_scanning
]