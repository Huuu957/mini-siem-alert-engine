from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>🚨 Mini SIEM Alert Engine UI</h1><p><a href='/alerts'>View Alerts</a></p>"

@app.route("/alerts")
def show_alerts():
    try:
        with open("alerts.txt", "r") as f:
            alerts = f.readlines()
    except FileNotFoundError:
        alerts = ["No alerts found."]

    html = """
    <h2>Detected Alerts</h2>
    <pre style='background:#111;color:#0f0;padding:10px;border-radius:8px;'>{{ alerts }}</pre>
    <a href='/'>Back</a>
    """
    return render_template_string(html, alerts="".join(alerts))

if __name__ == "__main__":
    app.run(debug=True)
