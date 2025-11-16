# src/agents/tracker_agent.py
import pandas as pd

class TrackerAgent:
    def __init__(self, memory, metrics=None):
        self.memory = memory
        self.metrics = metrics

    def load_history_df(self):
        records = self.memory.get_habit_history()
        if not records:
            return pd.DataFrame(columns=["date","habit","status","timestamp"])
        df = pd.DataFrame(records)
        return df

    def compute_daily_summary(self):
        df = self.load_history_df()
        if df.empty:
            return pd.DataFrame()
        # pivot: counts per date per status
        df_summary = df.groupby(["date", "status"]).size().unstack(fill_value=0)
        return df_summary

    def completion_rate(self):
        df = self.load_history_df()
        if df.empty:
            return 0.0
        return (df["status"] == "done").mean() * 100
