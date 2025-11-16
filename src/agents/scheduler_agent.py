# src/agents/scheduler_agent.py
from src.tools.scheduler_sim import generate_daily_schedule

class SchedulerAgent:
    def __init__(self, memory, metrics=None):
        self.memory = memory
        self.metrics = metrics

    def create_schedule(self, days=14):
        profile = self.memory.load_user_profile()
        habits = profile.get("habits", [])
        schedule = generate_daily_schedule(habits, days=days)
        # Optionally persist schedule in derived stats
        self.memory.save_derived("last_schedule", schedule)
        if self.metrics:
            self.metrics.log("schedules_created", len(schedule), {"days": days})
        return schedule
