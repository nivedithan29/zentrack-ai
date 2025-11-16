# src/tools/scheduler_sim.py
from datetime import date, timedelta

def generate_daily_schedule(habits, days=14, start_date=None):
    """
    habits: list of dicts {"name": "...", "target": "..."}
    returns list of schedule entries: {"date": "YYYY-MM-DD", "habit": name, "reminder_time": "09:00"}
    """
    if start_date is None:
        start = date.today() - timedelta(days=days-1)
    else:
        start = start_date
    schedule = []
    for i in range(days):
        d = start + timedelta(days=i)
        dstr = d.isoformat()
        for h in habits:
            schedule.append({"date": dstr, "habit": h["name"], "reminder_time": "09:00"})
    return schedule
