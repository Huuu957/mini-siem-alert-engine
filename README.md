# 🛡️ Mini SIEM Alert Engine

A lightweight Python-based detection engine that simulates SIEM behavior by analyzing logs and generating alerts for common attack patterns.

## ✅ Features
- Brute force detection (`/login` attacks)
- Path scanning detection (suspicious endpoint probes)
- Configurable thresholds via `config.json`
- Modular detection rule system
- Alerts printed and saved to `alerts.txt`

## 📁 Files
| File | Description |
|------|-------------|
| `main.py` | Runs the detection engine |
| `detection_rules.py` | All detection logic lives here |
| `alert_manager.py` | Handles alert formatting and output |
| `config.json` | Tuning for thresholds and detection rules |
| `sample_logs.txt` | Sample Apache-style log input |
| `alerts.txt` | Output alerts from engine |

## 🚀 How to Run
```bash
python main.py
