# src/memory/memory_bank.py
import json
import os
from collections import defaultdict
from datetime import date

class MemoryBank:
    """Simple persistent-ish memory using JSON file (optional)."""
    def __init__(self, storage_path="memory_store.json"):
        self.storage_path = storage_path
        self.data = {
            "user_profile": {},
            "habit_history": [],   # list of dicts {date, habit, status, timestamp}
            "derived_stats": {},
            "recommendation_history": []
        }
        self._load()

    def _load(self):
        if os.path.exists(self.storage_path):
            try:
                with open(self.storage_path, "r", encoding="utf-8") as f:
                    self.data = json.load(f)
            except Exception:
                # if corrupted, start fresh
                self.data = {
                    "user_profile": {},
                    "habit_history": [],
                    "derived_stats": {},
                    "recommendation_history": []
                }

    def _save(self):
        with open(self.storage_path, "w", encoding="utf-8") as f:
            json.dump(self.data, f, default=str, indent=2)

    # Profile methods
    def save_user_profile(self, profile: dict):
        self.data["user_profile"] = profile
        self._save()

    def load_user_profile(self):
        return self.data.get("user_profile", {})

    # Habit history
    def add_habit_entry(self, entry: dict):
        # entry: {"date": "YYYY-MM-DD", "habit": "Drink Water", "status": "done", "timestamp": "..."}
        self.data["habit_history"].append(entry)
        self._save()

    def get_habit_history(self, start_date=None, end_date=None):
        # return all or filter by date strings
        if start_date is None and end_date is None:
            return self.data["habit_history"]
        out = []
        for rec in self.data["habit_history"]:
            if start_date and rec["date"] < start_date:
                continue
            if end_date and rec["date"] > end_date:
                continue
            out.append(rec)
        return out

    # Derived stats
    def save_derived(self, key, value):
        self.data["derived_stats"][key] = value
        self._save()

    def load_derived(self, key):
        return self.data["derived_stats"].get(key)

    # Recommendations
    def add_recommendation(self, rec):
        self.data["recommendation_history"].append(rec)
        self._save()
