# src/agents/onboarding_agent.py
from typing import List

class OnboardingAgent:
    def __init__(self, memory):
        self.memory = memory

    def onboard(self, name: str, timezone: str, habits: List[dict]):
        """
        habits: list of {"name": str, "target": str}
        """
        profile = {
            "name": name,
            "timezone": timezone,
            "habits": habits
        }
        self.memory.save_user_profile(profile)
        return profile

    def load_profile(self):
        return self.memory.load_user_profile()
