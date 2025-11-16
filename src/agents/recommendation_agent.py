# src/agents/recommendation_agent.py
from datetime import datetime

class RecommendationAgent:
    """
    Simple rule-based recommendations based on completion rate.
    In a richer system you'd call an LLM to generate personalized suggestions.
    """
    def __init__(self, memory, metrics=None):
        self.memory = memory
        self.metrics = metrics

    def generate(self):
        derived = self.memory.load_derived("last_summary") or {}
        pct = derived.get("overall_completion_rate_pct", None)
        rec_text = ""
        if pct is None:
            rec_text = "No sufficient data to generate recommendations yet."
        else:
            if pct >= 80:
                rec_text = "Excellent consistency — keep the routine! Consider adding a small new habit."
            elif pct >= 50:
                rec_text = "Good start. Try reducing targets for the hardest habit or shift reminder times slightly earlier/later."
            else:
                rec_text = "Low completion. Try making the habit smaller (micro-goals) and add a morning trigger (after brushing teeth)."

        rec = {
            "generated_at": datetime.now().isoformat(),
            "completion_rate_pct": pct,
            "recommendation": rec_text
        }
        self.memory.add_recommendation(rec)
        if self.metrics:
            self.metrics.log("recommendation_generated", 1, {"completion_pct": pct})
        return rec
