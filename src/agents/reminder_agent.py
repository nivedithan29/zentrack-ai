# src/agents/reminder_agent.py
import random
from datetime import datetime

class ReminderAgent:
    """
    Simulated reminder agent. In a deployed system this would integrate with push/email.
    For demo: it chooses simulated user responses (or you can inject responses).
    """
    def __init__(self, memory, metrics=None, response_fn=None):
        self.memory = memory
        self.metrics = metrics
        # response_fn(schedule_entry) -> status string. If not provided, random simulation is used.
        self.response_fn = response_fn or self._random_response

    def _random_response(self, entry):
        # weights tuned for demo
        return random.choices(population=["done", "skipped", "snoozed"], weights=[0.6, 0.25, 0.15], k=1)[0]

    def send_reminder(self, entry):
        # entry: {"date": "YYYY-MM-DD", "habit": "...", "reminder_time": "..."}
        ts = datetime.now().isoformat()
        status = self.response_fn(entry)
        record = {
            "date": entry["date"],
            "habit": entry["habit"],
            "status": status,
            "timestamp": ts
        }
        # pass to memory/tracker
        self.memory.add_habit_entry(record)
        if self.metrics:
            self.metrics.log("reminder_sent", 1, {"habit": entry["habit"], "status": status})
        return record
