# Metrics Logger (placeholder)
class MetricsLogger:
    def __init__(self):
        self.logs = []

    def log(self, message):
        self.logs.append(message)
        print(f"[LOG]: {message}")
