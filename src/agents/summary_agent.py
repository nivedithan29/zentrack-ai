# src/agents/summary_agent.py
import pandas as pd
from datetime import datetime

class SummaryAgent:
    def __init__(self, memory, tracker, metrics=None):
        self.memory = memory
        self.tracker = tracker
        self.metrics = metrics

    def weekly_summary(self):
        df = self.tracker.load_history_df()
        if df.empty:
            return {"message": "No data"}
        # compute aggregates for last 7 days if possible
        # use date strings in df['date']
        last_date = df['date'].max()
        # create pandas groupings
        summary = self.tracker.compute_daily_summary()
        overall_completion = self.tracker.completion_rate()
        derived = {
            "last_generated": datetime.now().isoformat(),
            "overall_completion_rate_pct": overall_completion,
            "daily_breakdown": summary.to_dict()
        }
        self.memory.save_derived("last_summary", derived)
        if self.metrics:
            self.metrics.log("summary_generated", 1, {"completion_pct": overall_completion})
        return derived
