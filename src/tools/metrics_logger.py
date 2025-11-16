# src/tools/metrics_logger.py
import time

class MetricsLogger:
    def __init__(self):
        self.metrics = []

    def log(self, name, value, meta=None):
        ts = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        entry = {"time": ts, "name": name, "value": value, "meta": meta}
        self.metrics.append(entry)
        print(f"[METRIC] {ts} | {name} = {value} | meta={meta}")

    def get_all(self):
        return self.metrics
