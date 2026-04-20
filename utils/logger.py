from datetime import datetime

def log(message, logs):
    logs.append(f"[{datetime.now().strftime('%H:%M:%S')}] {message}")

    if len(logs) > 100:
        logs[:] = logs[-100:]
