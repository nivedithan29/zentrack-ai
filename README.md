# Zentrack AI
### Your Personal Habit & Wellness Multi-Agent System

Zentrack AI is a multi-agent system designed to help users build and maintain healthy daily habits. It automates reminders, tracks actions, generates summaries, and provides intelligent habit recommendations.

---

## Why Zentrack AI?

Most people struggle with consistency. We forget habits, skip routines, or lose motivation. Manual tracking becomes tiring and inconsistent.

Zentrack AI solves this by:
- Automatically scheduling reminders
- Tracking behavior (done / skipped / snoozed)
- Summarizing daily and weekly progress
- Providing personalized recommendations
- Maintaining long-term memory

---

## Key Features

- Automated habit reminders  
- Daily behavior simulation  
- Summary generation (per-day and weekly)  
- Personalized recommendations  
- Long-term memory storage  
- Observability logs  
- CSV export for analysis  
- 14-day simulation via Kaggle Notebook  

---

## Multi-Agent Architecture

(ASCII diagram)

                 ┌──────────────────────┐
                 │      User Input       │
                 └───────────┬───────────┘
                             │
                             ▼
                ┌──────────────────────────┐
                │     Onboarding Agent      │
                └───────┬───────────────────┘
                        │
                        ▼
               ┌──────────────────────────┐
               │       Memory Bank        │
               └───────┬─────────┬────────┘
                       │         │
                       ▼         ▼
    ┌────────────────────────┐  ┌────────────────────────────┐
    │     Scheduler Agent    │  │     Tracker Agent           │
    └─────────────┬──────────┘  └───────┬────────────────────┘
                  │                      │
                  ▼                      │
        ┌──────────────────────┐         │
        │    Reminder Agent    │─────────┘
        └───────────┬──────────┘
                    ▼
         ┌────────────────────────┐
         │     Summary Agent      │
         └─────────────┬─────────┘
                       ▼
         ┌────────────────────────┐
         │ Recommendation Agent    │
         └────────────────────────┘

---

## Project Structure

zentrack-ai/
- README.md
- notebook/
- src/
- assets/

---

## How to Run Locally

1. Clone the repository
git clone https://github.com/nivedithan29/zentrack-ai.git
cd zentrack-ai

2. Run the demo simulation
python -m src.demo.run_simulation


---

## Example Output

Summary (sample):
- Overall completion: 57.14%
- Completed: 24
- Skipped: 11
- Snoozed: 7

Recommendation (sample):
"Good start! Try reducing targets for the hardest habit or adjusting reminder times."

---

## Technologies Used

- Python
- Pandas
- Multi-agent architecture
- Custom tools (CSV Exporter, Metrics Logger)
- Memory Bank
- Kaggle Notebook

---

## Future Enhancements

- UI or mobile app
- Push notifications
- Google Fit integration
- Habit trend visualization
- Deployment using Agent Engine

---

## License
MIT License
