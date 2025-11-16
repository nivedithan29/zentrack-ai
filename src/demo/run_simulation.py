# src/demo/run_simulation.py
import pprint
from src.memory.memory_bank import MemoryBank
from src.memory.session_service import SessionService
from src.tools.metrics_logger import MetricsLogger
from src.tools.csv_export_tool import export_to_csv

from src.agents.onboarding_agent import OnboardingAgent
from src.agents.scheduler_agent import SchedulerAgent
from src.agents.reminder_agent import ReminderAgent
from src.agents.tracker_agent import TrackerAgent
from src.agents.summary_agent import SummaryAgent
from src.agents.recommendation_agent import RecommendationAgent

def run_demo(days=14):
    print("Starting Zentrack AI demo simulation")
    mem = MemoryBank(storage_path="demo_memory.json")
    sess = SessionService()
    metrics = MetricsLogger()

    # Onboard
    onboarding = OnboardingAgent(mem)
    profile = onboarding.onboard(
        name="Demo User",
        timezone="Asia/Kolkata",
        habits=[
            {"name": "Drink Water", "target": "8 glasses/day"},
            {"name": "Walking", "target": "5000 steps/day"},
            {"name": "Meditation", "target": "10 minutes/day"}
        ]
    )
    print("Profile saved:", profile)

    # Scheduler
    scheduler = SchedulerAgent(mem, metrics=metrics)
    schedule = scheduler.create_schedule(days=days)
    print(f"Generated schedule for {len(schedule)} reminders")

    # Reminder + Tracker loop (simulate send & responses)
    reminder = ReminderAgent(mem, metrics=metrics)
    tracker = TrackerAgent(mem, metrics=metrics)

    for entry in schedule:
        reminder.send_reminder(entry)

    # After simulation: compute summary & recommendations
    summary_agent = SummaryAgent(mem, tracker, metrics=metrics)
    summary = summary_agent.weekly_summary()
    print("\n=== Summary ===")
    pprint.pprint(summary)

    rec_agent = RecommendationAgent(mem, metrics=metrics)
    rec = rec_agent.generate()
    print("\n=== Recommendation ===")
    pprint.pprint(rec)

    # Export CSVs
    history = mem.get_habit_history()
    export_to_csv(history, filename="demo_habit_history.csv")

    # Return objects for interactive usage
    return {
        "memory": mem,
        "metrics": metrics,
        "summary": summary,
        "recommendation": rec
    }

if __name__ == "__main__":
    run_demo(days=14)
