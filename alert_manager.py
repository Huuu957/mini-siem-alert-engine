import datetime

def print_alert(alert):
    print(f"[ALERT] {alert['type']} from IP {alert['ip']} at {alert['time']} ({alert['count']} attempts)")

def save_alert_to_file(alert, filename="alerts.txt"):
    with open(filename, "a") as f:
        f.write(f"{datetime.datetime.now()} | {alert['type']} | {alert['ip']} | {alert['time']} | {alert['count']} attempts\n")

def handle_alerts(alerts):
    for alert in alerts:
        print_alert(alert)
        save_alert_to_file(alert)
