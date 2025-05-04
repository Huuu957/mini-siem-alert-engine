from flask import Flask, render_template_string
import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return render_template_string("""
    <html>
        <head>
            <title>Mini SIEM Alert Engine</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background-color: #0f0f0f;
                    color: #f5f5f5;
                    text-align: center;
                    padding: 40px;
                }
                a {
                    color: #00ffcc;
                    text-decoration: none;
                    font-size: 20px;
                }
                h1 {
                    color: #00ffcc;
                }
            </style>
        </head>
        <body>
            <h1>🛡️ Mini SIEM Alert Engine</h1>
            <p><a href="/alerts">📊 View Detected Alerts</a></p>
        </body>
    </html>
    """)

@app.route("/alerts")
def show_alerts():
    try:
        with open("alerts.txt", "r") as f:
            alerts = f.readlines()
    except FileNotFoundError:
        alerts = ["No alerts found."]

    return render_template_string("""
    <html>
        <head>
            <title>Alerts - Mini SIEM</title>
            <style>
                body {
                    font-family: monospace;
                    background-color: #121212;
                    color: #00ff88;
                    padding: 40px;
                }
                pre {
                    background-color: #1e1e1e;
                    border: 1px solid #444;
                    padding: 20px;
                    border-radius: 8px;
                    overflow-x: auto;
                    max-width: 100%;
                }
                a {
                    color: #00ffcc;
                    font-size: 16px;
                    text-decoration: none;
                }
            </style>
        </head>
        <body>
            <h1>📊 Alert Log</h1>
            <pre>{{ alerts }}</pre>
            <br><a href="/">← Back</a>
        </body>
    </html>
    """, alerts="".join(alerts))

if __name__ == "__main__":
    app.run(debug=True)
